# Integration: Azure DevOps

> **Purpose:** Synchronize work items between Deep Process and Azure DevOps
> **Tool:** Azure CLI (`az boards`)
> **Fallback:** Manual sync instructions if CLI fails

---

## 1. PREREQUISITES

### 1.1 Required Tools

```bash
# Check if Azure CLI installed
az --version

# If not installed, show:
# "Azure CLI not found. Install from: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
# "Or disable Azure DevOps integration in .state/process.yaml"
```

### 1.2 Authentication Check

```bash
# Check if logged in
az account show

# If not logged in:
az login

# If wrong account:
az account set --subscription "{subscription_id}"
```

### 1.3 Extension Check

```bash
# Azure DevOps extension required
az extension show --name azure-devops

# If not installed:
az extension add --name azure-devops

# Configure default org and project
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}
```

---

## 2. CONFIGURATION

### 2.1 In .state/process.yaml

```yaml
integrations:
  azure_devops:
    enabled: true
    organization: "myorg"                    # Azure DevOps org name
    project: "MyProject"                     # Project name
    area_path: "MyProject\\Team"             # Optional: Area path
    iteration_path: "MyProject\\Sprint {n}"  # Optional: Iteration pattern

    sync_options:
      sync_on_create: true      # Auto-sync when item created
      sync_on_update: true      # Auto-sync on status change
      sync_on_delete: false     # Don't delete in Azure DevOps

    work_item_mapping:
      epic: "Feature"           # Epic → Feature
      story: "User Story"       # Story → User Story
      task: "Task"              # Task → Task
      bug: "Bug"                # Bug → Bug
```

### 2.2 Validation

```markdown
## INSTRUKCJA: Validate Azure DevOps Config

1. Check required fields:
   - organization: REQUIRED
   - project: REQUIRED

2. Test connection:
   ```bash
   az boards work-item show --id 1 --org "https://dev.azure.com/{org}" --project "{project}"
   ```

3. If fails:
   - Check organization name
   - Check project name
   - Check permissions
   - FALLBACK: Disable integration, use manual
```

---

## 3. WORK ITEM OPERATIONS

### 3.1 Create Epic (Feature)

```markdown
## INSTRUKCJA: Create Epic in Azure DevOps

TRIGGER: After creating artifacts/epics/EPIC-XXX.yaml

1. BUILD command:
```bash
az boards work-item create \
  --org "https://dev.azure.com/{org}" \
  --project "{project}" \
  --type "Feature" \
  --title "{epic.title}" \
  --description "{epic.description}" \
  --area "{area_path}" \
  --output json
```

2. PARSE response:
   - Extract: id (work item ID)
   - Extract: url (web URL)

3. UPDATE local:
   - Set epic.azure_devops_id = {id}
   - Set epic.azure_devops_url = {url}
   - Save artifacts/epics/EPIC-XXX.yaml
   - Update .state/items.yaml

4. REPORT:
   "Created Azure DevOps Feature #{id}: {title}"
   "URL: {url}"

5. ON ERROR:
   - Log error
   - WARN user: "Failed to sync to Azure DevOps: {error}"
   - Continue without sync (local item still valid)
```

**Command Template:**

```bash
# Variables from epic
TITLE="{epic.title}"
DESC="{epic.description}"
ORG="{config.organization}"
PROJECT="{config.project}"
AREA="{config.area_path}"

# Create Feature
RESULT=$(az boards work-item create \
  --org "https://dev.azure.com/$ORG" \
  --project "$PROJECT" \
  --type "Feature" \
  --title "$TITLE" \
  --description "$DESC" \
  --area "$AREA" \
  --output json)

# Extract ID
AZURE_ID=$(echo $RESULT | jq -r '.id')
AZURE_URL=$(echo $RESULT | jq -r '._links.html.href')

echo "Created: #$AZURE_ID - $AZURE_URL"
```

### 3.2 Create Story (User Story)

```markdown
## INSTRUKCJA: Create Story in Azure DevOps

TRIGGER: After creating artifacts/stories/STORY-XXX.yaml

1. GET parent epic's Azure DevOps ID:
   - Read epic from .state/items.yaml
   - Get epic.azure_devops_id
   - If not synced: sync epic first

2. BUILD command:
```bash
az boards work-item create \
  --org "https://dev.azure.com/{org}" \
  --project "{project}" \
  --type "User Story" \
  --title "{story.title}" \
  --description "{story.description}" \
  --area "{area_path}" \
  --output json
```

3. LINK to parent:
```bash
az boards work-item relation add \
  --id {new_story_id} \
  --relation-type "System.LinkTypes.Hierarchy-Reverse" \
  --target-id {epic.azure_devops_id} \
  --org "https://dev.azure.com/{org}"
```

4. SET story points (if available):
```bash
az boards work-item update \
  --id {new_story_id} \
  --fields "Microsoft.VSTS.Scheduling.StoryPoints={story.points}" \
  --org "https://dev.azure.com/{org}"
```

5. UPDATE local with azure_devops_id

6. REPORT success or error
```

**Command Template:**

```bash
# Create User Story
RESULT=$(az boards work-item create \
  --org "https://dev.azure.com/$ORG" \
  --project "$PROJECT" \
  --type "User Story" \
  --title "$STORY_TITLE" \
  --description "$STORY_DESC" \
  --output json)

STORY_AZURE_ID=$(echo $RESULT | jq -r '.id')

# Link to parent Feature
az boards work-item relation add \
  --id $STORY_AZURE_ID \
  --relation-type "System.LinkTypes.Hierarchy-Reverse" \
  --target-id $EPIC_AZURE_ID \
  --org "https://dev.azure.com/$ORG"

# Set story points
az boards work-item update \
  --id $STORY_AZURE_ID \
  --fields "Microsoft.VSTS.Scheduling.StoryPoints=$POINTS" \
  --org "https://dev.azure.com/$ORG"
```

### 3.3 Update Story Status

```markdown
## INSTRUKCJA: Sync Story Status to Azure DevOps

TRIGGER: When story.status changes locally

STATUS MAPPING:
| Local Status | Azure DevOps State |
|--------------|-------------------|
| draft        | New               |
| ready        | New               |
| in_progress  | Active            |
| done         | Resolved          |
| reviewed     | Resolved          |
| verified     | Closed            |
| blocked      | New (+ blocked tag)|

COMMAND:
```bash
az boards work-item update \
  --id {story.azure_devops_id} \
  --state "{mapped_state}" \
  --org "https://dev.azure.com/{org}"
```

FOR BLOCKED:
```bash
az boards work-item update \
  --id {story.azure_devops_id} \
  --state "New" \
  --fields "System.Tags=blocked;{existing_tags}" \
  --org "https://dev.azure.com/{org}"
```
```

### 3.4 Assign to Sprint (Iteration)

```markdown
## INSTRUKCJA: Assign Story to Sprint/Iteration

TRIGGER: When story is added to sprint

1. BUILD iteration path:
   - Pattern: "{project}\\{iteration_path_pattern}"
   - Replace {n} with sprint number
   - Example: "MyProject\\Sprint 1"

2. UPDATE work item:
```bash
az boards work-item update \
  --id {story.azure_devops_id} \
  --iteration "{iteration_path}" \
  --org "https://dev.azure.com/{org}"
```

NOTE: Iteration must exist in Azure DevOps project settings.
If not exists, WARN user to create it manually.
```

---

## 4. QUERY OPERATIONS

### 4.1 Get Work Item

```bash
az boards work-item show \
  --id {id} \
  --org "https://dev.azure.com/{org}" \
  --output json
```

### 4.2 List Work Items by Query

```bash
# Get all Features in project
az boards query \
  --wiql "SELECT [System.Id], [System.Title], [System.State] FROM workitems WHERE [System.WorkItemType] = 'Feature' AND [System.TeamProject] = '{project}'" \
  --org "https://dev.azure.com/{org}" \
  --output json
```

### 4.3 Check Sync Status

```markdown
## INSTRUKCJA: Verify Sync Status

1. For each local item with azure_devops_id:
   a. Query Azure DevOps for that ID
   b. Compare key fields:
      - Title
      - State/Status
      - Parent link
   c. Report discrepancies

2. Output:
   "Sync status: X items in sync, Y items diverged"
   List diverged items with differences
```

---

## 5. ERROR HANDLING

### 5.1 Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| `AADSTS700016` | Not logged in | Run `az login` |
| `TF401019` | Project not found | Check project name |
| `TF14045` | Iteration not found | Create iteration in Azure DevOps |
| `VS403507` | No permission | Check user permissions |
| `Rate limit exceeded` | Too many requests | Wait and retry |

### 5.2 Error Handling Flow

```markdown
## INSTRUKCJA: Handle Azure DevOps Error

1. CATCH error from az command
2. IDENTIFY error type:
   - Auth error → Prompt re-login
   - Permission error → Suggest check permissions
   - Not found → Suggest check config
   - Rate limit → Wait 60s, retry
   - Other → Log and continue without sync

3. ALWAYS:
   - Log error to .state/history.yaml
   - WARN user what failed
   - Local operation still succeeds
   - Offer manual sync instructions

4. NEVER:
   - Fail local operation because sync failed
   - Retry indefinitely
   - Hide errors from user
```

### 5.3 Retry Logic

```bash
# Retry wrapper
retry_azure() {
  local max_attempts=3
  local delay=5
  local attempt=1

  while [ $attempt -le $max_attempts ]; do
    if "$@"; then
      return 0
    fi

    echo "Attempt $attempt failed. Retrying in ${delay}s..."
    sleep $delay
    delay=$((delay * 2))
    attempt=$((attempt + 1))
  done

  echo "All attempts failed"
  return 1
}

# Usage
retry_azure az boards work-item create --type "Feature" --title "Test"
```

---

## 6. MANUAL SYNC FALLBACK

### 6.1 When to Use

- Azure CLI not installed
- Authentication issues
- Network problems
- User preference

### 6.2 Manual Instructions

```markdown
## MANUAL SYNC: Create Feature in Azure DevOps

Since automatic sync failed, please create manually:

1. Open Azure DevOps: https://dev.azure.com/{org}/{project}
2. Go to Boards → Work Items
3. Click "New Work Item" → "Feature"
4. Fill in:
   - Title: {epic.title}
   - Description: {epic.description}
5. Save
6. Copy the Work Item ID (e.g., #12345)
7. Tell me the ID so I can update local state

Or run this command manually:
```
az boards work-item create --type "Feature" --title "{title}" --project "{project}"
```
```

---

## 7. BULK OPERATIONS

### 7.1 Initial Sync (Full Export)

```markdown
## INSTRUKCJA: Export All Items to Azure DevOps

1. Get all local items without azure_devops_id
2. For each epic:
   a. Create Feature
   b. Store ID
3. For each story:
   a. Create User Story
   b. Link to parent Feature
   c. Store ID
4. Report: "Synced X epics, Y stories"
```

### 7.2 Import from Azure DevOps

```markdown
## INSTRUKCJA: Import from Azure DevOps

1. Query all Features and User Stories
2. For each item not in local state:
   a. Create local artifact
   b. Store azure_devops_id
3. For each item in both:
   a. Compare and report differences
   b. Ask user which version to keep
```

---

## 8. CONFIGURATION VALIDATION

```markdown
## CHECKLIST: Azure DevOps Integration Ready

□ Azure CLI installed (`az --version`)
□ Logged in (`az account show`)
□ DevOps extension installed (`az extension show --name azure-devops`)
□ Organization accessible
□ Project exists
□ User has Work Item write permissions
□ Iterations exist (if using sprints)

If any check fails:
- Provide specific fix instructions
- Offer to disable integration
- Continue with local-only mode
```

---

## 9. VOCABULARY

| Term | Meaning |
|------|---------|
| Organization | Azure DevOps organization (myorg in dev.azure.com/myorg) |
| Project | Azure DevOps project |
| Work Item | Generic term for Feature, User Story, Task, Bug |
| Feature | Azure DevOps equivalent of Epic |
| Iteration | Azure DevOps equivalent of Sprint |
| Area Path | Hierarchical categorization |
