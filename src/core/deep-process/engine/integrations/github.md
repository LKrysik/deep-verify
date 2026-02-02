# Integration: GitHub

> **Purpose:** Synchronize work items between Deep Process and GitHub Issues/Projects
> **Tool:** GitHub CLI (`gh`)
> **Fallback:** Manual sync instructions if CLI fails

---

## 1. PREREQUISITES

### 1.1 Required Tools

```bash
# Check if GitHub CLI installed
gh --version

# If not installed, show:
# "GitHub CLI not found. Install from: https://cli.github.com/"
# "Or disable GitHub integration in .state/process.yaml"
```

### 1.2 Authentication Check

```bash
# Check if logged in
gh auth status

# If not logged in:
gh auth login

# Verify repo access
gh repo view {owner}/{repo}
```

---

## 2. CONFIGURATION

### 2.1 In .state/process.yaml

```yaml
integrations:
  github:
    enabled: true
    owner: "myorg"              # GitHub org or username
    repo: "myrepo"              # Repository name

    sync_options:
      sync_on_create: true
      sync_on_update: true
      use_projects: true        # Use GitHub Projects for sprints

    work_item_mapping:
      epic: "milestone"         # Epic → Milestone
      story: "issue"            # Story → Issue
      sprint: "project"         # Sprint → Project (v2)

    labels:
      epic: "epic"
      story: "user-story"
      task: "task"
      blocked: "blocked"
      priority:
        must_have: "priority:critical"
        should_have: "priority:high"
        could_have: "priority:medium"
        wont_have: "priority:low"
```

### 2.2 Validation

```markdown
## INSTRUKCJA: Validate GitHub Config

1. Check required fields:
   - owner: REQUIRED
   - repo: REQUIRED

2. Test connection:
   ```bash
   gh repo view {owner}/{repo} --json name
   ```

3. If fails:
   - Check owner/repo names
   - Check authentication
   - Check repository permissions
   - FALLBACK: Disable integration
```

---

## 3. WORK ITEM OPERATIONS

### 3.1 Create Epic (Milestone)

```markdown
## INSTRUKCJA: Create Epic as GitHub Milestone

TRIGGER: After creating artifacts/epics/EPIC-XXX.yaml

1. BUILD command:
```bash
gh api repos/{owner}/{repo}/milestones \
  --method POST \
  -f title="{epic.title}" \
  -f description="{epic.description}" \
  -f state="open"
```

2. PARSE response:
   - Extract: number (milestone number)
   - Extract: html_url

3. UPDATE local:
   - Set epic.github_milestone_number = {number}
   - Set epic.github_url = {html_url}
   - Save artifacts/epics/EPIC-XXX.yaml
   - Update .state/items.yaml

4. REPORT:
   "Created GitHub Milestone #{number}: {title}"
   "URL: {html_url}"

5. ON ERROR:
   - Log error
   - WARN user
   - Continue without sync
```

**Command Template:**

```bash
# Variables
OWNER="{config.owner}"
REPO="{config.repo}"
TITLE="{epic.title}"
DESC="{epic.description}"

# Create Milestone
RESULT=$(gh api repos/$OWNER/$REPO/milestones \
  --method POST \
  -f title="$TITLE" \
  -f description="$DESC" \
  -f state="open")

MILESTONE_NUMBER=$(echo $RESULT | jq -r '.number')
MILESTONE_URL=$(echo $RESULT | jq -r '.html_url')

echo "Created Milestone #$MILESTONE_NUMBER: $MILESTONE_URL"
```

### 3.2 Create Story (Issue)

```markdown
## INSTRUKCJA: Create Story as GitHub Issue

TRIGGER: After creating artifacts/stories/STORY-XXX.yaml

1. GET parent epic's GitHub Milestone number:
   - Read epic from .state/items.yaml
   - Get epic.github_milestone_number
   - If not synced: sync epic first

2. BUILD issue body:
```markdown
## User Story

{story.description}

## Acceptance Criteria

{for each criterion}
- [ ] {criterion.criterion}
{end for}

## Details

- **Epic:** {epic.title}
- **Points:** {story.points}
- **Priority:** {story.priority}

---
_Managed by Deep Process_
```

3. CREATE issue:
```bash
gh issue create \
  --repo "{owner}/{repo}" \
  --title "{story.title}" \
  --body "{body}" \
  --milestone "{epic.github_milestone_number}" \
  --label "user-story,{priority_label}"
```

4. PARSE response and store github_issue_number

5. REPORT success
```

**Command Template:**

```bash
# Create Issue with Milestone
gh issue create \
  --repo "$OWNER/$REPO" \
  --title "$STORY_TITLE" \
  --body "$STORY_BODY" \
  --milestone "$MILESTONE_NUMBER" \
  --label "user-story,$PRIORITY_LABEL"

# Get issue number from output (e.g., "https://github.com/owner/repo/issues/42")
ISSUE_URL=$(gh issue create ... | tail -1)
ISSUE_NUMBER=$(echo $ISSUE_URL | grep -oE '[0-9]+$')
```

### 3.3 Update Story Status

```markdown
## INSTRUKCJA: Sync Story Status to GitHub

TRIGGER: When story.status changes locally

STATUS MAPPING:
| Local Status | GitHub State | Action |
|--------------|--------------|--------|
| draft        | open         | - |
| ready        | open         | Add label "ready" |
| in_progress  | open         | Add label "in-progress" |
| done         | open         | Add label "done" |
| reviewed     | open         | Add label "reviewed" |
| verified     | closed       | Close issue |
| blocked      | open         | Add label "blocked" |

COMMAND (close):
```bash
gh issue close {issue_number} --repo "{owner}/{repo}"
```

COMMAND (add label):
```bash
gh issue edit {issue_number} \
  --repo "{owner}/{repo}" \
  --add-label "{label}"
```

COMMAND (remove label):
```bash
gh issue edit {issue_number} \
  --repo "{owner}/{repo}" \
  --remove-label "{label}"
```
```

### 3.4 Sprint as GitHub Project

```markdown
## INSTRUKCJA: Create Sprint as GitHub Project

TRIGGER: After creating artifacts/sprints/SPRINT-XXX.yaml

NOTE: Uses GitHub Projects V2 (GraphQL API)

1. CREATE project:
```bash
gh api graphql -f query='
  mutation {
    createProjectV2(input: {
      ownerId: "{owner_id}",
      title: "{sprint.name}"
    }) {
      projectV2 {
        id
        number
        url
      }
    }
  }
'
```

2. ADD stories to project:
```bash
# For each story in sprint
gh api graphql -f query='
  mutation {
    addProjectV2ItemById(input: {
      projectId: "{project_id}",
      contentId: "{issue_node_id}"
    }) {
      item {
        id
      }
    }
  }
'
```

3. ALTERNATIVE (simpler): Use Milestone as Sprint
   - Assign all sprint stories to a milestone named "Sprint {n}"
   - Less features but simpler
```

---

## 4. QUERY OPERATIONS

### 4.1 Get Issue

```bash
gh issue view {number} --repo "{owner}/{repo}" --json number,title,state,milestone,labels
```

### 4.2 List Issues by Milestone

```bash
gh issue list \
  --repo "{owner}/{repo}" \
  --milestone "{milestone_title}" \
  --json number,title,state
```

### 4.3 List All Milestones

```bash
gh api repos/{owner}/{repo}/milestones --jq '.[].title'
```

### 4.4 Check Sync Status

```markdown
## INSTRUKCJA: Verify GitHub Sync Status

1. For each local item with github_issue_number:
   a. Query GitHub for that issue
   b. Compare:
      - Title
      - State (open/closed)
      - Milestone
      - Labels
   c. Report discrepancies

2. Output:
   "Sync status: X items in sync, Y items diverged"
```

---

## 5. ERROR HANDLING

### 5.1 Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| `HTTP 401` | Not authenticated | Run `gh auth login` |
| `HTTP 404` | Repo/Issue not found | Check owner/repo/number |
| `HTTP 403` | No permission | Check repo access |
| `HTTP 422` | Invalid data | Check field values |
| `rate limit` | Too many requests | Wait and retry |

### 5.2 Error Handling Flow

```markdown
## INSTRUKCJA: Handle GitHub Error

1. CATCH error from gh command
2. IDENTIFY error type:
   - Auth error (401) → Prompt re-login
   - Not found (404) → Check config
   - Permission (403) → Suggest check permissions
   - Rate limit → Wait 60s, retry
   - Other → Log and continue

3. ALWAYS:
   - Log error to .state/history.yaml
   - WARN user what failed
   - Local operation still succeeds
   - Offer manual sync

4. NEVER:
   - Fail local operation because sync failed
   - Hide errors
```

---

## 6. MANUAL SYNC FALLBACK

### 6.1 Manual Instructions

```markdown
## MANUAL SYNC: Create Issue in GitHub

Since automatic sync failed, please create manually:

1. Open: https://github.com/{owner}/{repo}/issues/new
2. Fill in:
   - Title: {story.title}
   - Description: {story.description}
   - Milestone: {epic.title}
   - Labels: user-story, {priority}
3. Save
4. Copy the Issue number (e.g., #42)
5. Tell me the number so I can update local state

Or run this command manually:
```
gh issue create --title "{title}" --body "{body}" --milestone "{milestone}"
```
```

---

## 7. LABELS SETUP

### 7.1 Required Labels

```markdown
## INSTRUKCJA: Setup GitHub Labels

For full integration, ensure these labels exist:

1. CHECK existing labels:
```bash
gh label list --repo "{owner}/{repo}"
```

2. CREATE missing labels:
```bash
# Story types
gh label create "epic" --color "0052CC" --description "Epic/Feature" --repo "{owner}/{repo}"
gh label create "user-story" --color "1D76DB" --description "User Story" --repo "{owner}/{repo}"
gh label create "task" --color "5319E7" --description "Task" --repo "{owner}/{repo}"

# Status
gh label create "ready" --color "0E8A16" --description "Ready for development"
gh label create "in-progress" --color "FBCA04" --description "Work in progress"
gh label create "blocked" --color "D93F0B" --description "Blocked"
gh label create "done" --color "0E8A16" --description "Done"
gh label create "reviewed" --color "006B75" --description "Code reviewed"

# Priority
gh label create "priority:critical" --color "B60205" --description "Must have"
gh label create "priority:high" --color "D93F0B" --description "Should have"
gh label create "priority:medium" --color "FBCA04" --description "Could have"
gh label create "priority:low" --color "C5DEF5" --description "Won't have this time"
```

3. REPORT which labels were created
```

---

## 8. GITHUB PROJECTS V2 (Advanced)

### 8.1 Overview

GitHub Projects V2 provides:
- Custom fields (status, points, sprint)
- Kanban boards
- Roadmap views
- Automation

### 8.2 Setup Project for Sprints

```markdown
## INSTRUKCJA: Setup GitHub Project for Sprint Tracking

1. CREATE project:
```bash
gh api graphql -f query='
  mutation {
    createProjectV2(input: {
      ownerId: "{owner_node_id}",
      title: "Sprint Board"
    }) {
      projectV2 {
        id
        number
      }
    }
  }
'
```

2. ADD custom fields:
   - Status: To Do, In Progress, Done
   - Story Points: Number
   - Sprint: Iteration

3. ADD issues to project when sprint planned

4. UPDATE status when story status changes
```

### 8.3 Simplified Alternative

If Projects V2 is too complex:
- Use Milestones as Sprints
- Use Labels for status
- Use Issue body for points

---

## 9. BULK OPERATIONS

### 9.1 Export All to GitHub

```bash
# Export all epics as milestones
for epic in artifacts/epics/*.yaml; do
  # Parse epic and create milestone
  gh api repos/{owner}/{repo}/milestones --method POST -f title="..." -f description="..."
done

# Export all stories as issues
for story in artifacts/stories/*.yaml; do
  # Parse story and create issue
  gh issue create --title "..." --body "..." --milestone "..."
done
```

### 9.2 Import from GitHub

```bash
# List all issues
gh issue list --repo "{owner}/{repo}" --json number,title,state,milestone,labels --limit 1000

# For each issue not in local state:
# - Create local artifact
# - Store github_issue_number
```

---

## 10. CONFIGURATION VALIDATION

```markdown
## CHECKLIST: GitHub Integration Ready

□ GitHub CLI installed (`gh --version`)
□ Authenticated (`gh auth status`)
□ Repository accessible (`gh repo view {owner}/{repo}`)
□ Write permissions (can create issues)
□ Labels created (optional but recommended)

If any check fails:
- Provide specific fix instructions
- Offer to disable integration
- Continue with local-only mode
```

---

## 11. VOCABULARY

| Term | Meaning |
|------|---------|
| Owner | GitHub user or organization |
| Repo | Repository name |
| Issue | GitHub's work item |
| Milestone | Grouping of issues (like Epic) |
| Project V2 | GitHub's project management (like Sprint board) |
| Label | Tag for categorization |
