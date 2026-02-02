# Integration: MCP Template

> **Purpose:** Template for creating MCP (Model Context Protocol) integrations
> **Use:** When MCP server provides better tools than CLI
> **Benefit:** Structured responses, better error handling, authentication management

---

## 1. WHEN TO USE MCP

### 1.1 MCP vs CLI

| Aspect | MCP Tool | CLI (Bash) |
|--------|----------|------------|
| Error handling | Structured | Parse output |
| Authentication | Managed | Manual |
| Response format | JSON/structured | Text |
| Availability | Requires MCP server | Always available |
| Reliability | Higher | Depends on CLI |

### 1.2 Decision Rule

```markdown
## INSTRUKCJA: Choose MCP or CLI

1. CHECK if MCP tool available:
   - List available MCP tools
   - Look for matching tool (e.g., "azure_devops_create_work_item")

2. IF MCP tool available:
   - Prefer MCP tool
   - Better error handling
   - Structured response

3. IF MCP tool NOT available:
   - Fall back to CLI (Bash)
   - Use commands from azure-devops.md or github.md
```

---

## 2. MCP INTEGRATION STRUCTURE

### 2.1 Configuration

```yaml
# .state/process.yaml
integrations:
  mcp:
    enabled: true

    # MCP server connection (if configurable)
    server:
      name: "project-management-mcp"
      url: "mcp://localhost:3000"  # or however MCP connects

    # Tool preferences
    prefer_mcp_for:
      - azure_devops
      - github
      - jira

    # Fallback behavior
    fallback_to_cli: true
```

### 2.2 Tool Discovery

```markdown
## INSTRUKCJA: Discover Available MCP Tools

At session start:

1. List available MCP tools (method depends on LLM/CLI)
2. Check for project management tools:
   - azure_devops_*
   - github_*
   - jira_*
   - etc.
3. Store available tools in context
4. Use MCP tools when available, CLI otherwise
```

---

## 3. CREATING A NEW MCP INTEGRATION

### 3.1 Template Structure

```markdown
# Integration: {Service Name} (MCP)

## 1. AVAILABLE TOOLS

| Tool Name | Purpose | Parameters |
|-----------|---------|------------|
| {service}_create_item | Create work item | title, description, type |
| {service}_update_item | Update work item | id, fields |
| {service}_query_items | Query items | filter, limit |

## 2. TOOL MAPPING

| Local Operation | MCP Tool | Parameters |
|-----------------|----------|------------|
| Create Epic | {service}_create_item | type="epic", title, description |
| Create Story | {service}_create_item | type="story", title, description, parent_id |
| Update Status | {service}_update_item | id, status |

## 3. USAGE EXAMPLES

### Create Epic
```
Tool: {service}_create_item
Parameters:
  type: "epic"
  title: "{epic.title}"
  description: "{epic.description}"
  project: "{config.project}"

Response:
  id: 12345
  url: "https://..."
```

### Update Story Status
```
Tool: {service}_update_item
Parameters:
  id: "{story.external_id}"
  fields:
    status: "{mapped_status}"

Response:
  success: true
  updated_at: "2026-02-01T..."
```

## 4. ERROR HANDLING

| Error Code | Meaning | Action |
|------------|---------|--------|
| AUTH_ERROR | Not authenticated | Re-authenticate |
| NOT_FOUND | Item doesn't exist | Check ID |
| PERMISSION | No access | Check permissions |

## 5. FALLBACK

If MCP tool fails, fall back to CLI:
- See: integrations/{service}.md
```

---

## 4. EXAMPLE: AZURE DEVOPS MCP

### 4.1 If MCP Tools Available

```markdown
## Azure DevOps MCP Tools

### azure_devops_create_work_item

Creates a work item in Azure DevOps.

**Parameters:**
- organization: string (required)
- project: string (required)
- type: "Feature" | "User Story" | "Task" | "Bug"
- title: string (required)
- description: string
- parent_id: number (optional)
- area_path: string (optional)
- iteration_path: string (optional)
- fields: object (optional, additional fields)

**Response:**
```json
{
  "id": 12345,
  "url": "https://dev.azure.com/...",
  "title": "...",
  "state": "New"
}
```

**Usage:**
```
Use tool: azure_devops_create_work_item
Parameters:
  organization: "myorg"
  project: "MyProject"
  type: "Feature"
  title: "User Authentication"
  description: "Complete auth system..."
```

### azure_devops_update_work_item

Updates an existing work item.

**Parameters:**
- id: number (required)
- organization: string (required)
- fields: object (fields to update)

**Example:**
```
Use tool: azure_devops_update_work_item
Parameters:
  id: 12345
  organization: "myorg"
  fields:
    state: "Active"
    story_points: 5
```

### azure_devops_query

Queries work items.

**Parameters:**
- organization: string
- project: string
- wiql: string (Work Item Query Language)

**Example:**
```
Use tool: azure_devops_query
Parameters:
  organization: "myorg"
  project: "MyProject"
  wiql: "SELECT [System.Id] FROM workitems WHERE [System.WorkItemType] = 'Feature'"
```
```

---

## 5. EXAMPLE: GITHUB MCP

### 5.1 If MCP Tools Available

```markdown
## GitHub MCP Tools

### github_create_issue

Creates an issue in a repository.

**Parameters:**
- owner: string (required)
- repo: string (required)
- title: string (required)
- body: string
- labels: string[] (optional)
- milestone: number (optional)
- assignees: string[] (optional)

**Response:**
```json
{
  "number": 42,
  "html_url": "https://github.com/...",
  "state": "open"
}
```

### github_update_issue

Updates an existing issue.

**Parameters:**
- owner: string
- repo: string
- issue_number: number
- state: "open" | "closed"
- labels: string[]
- milestone: number

### github_create_milestone

Creates a milestone (for epics).

**Parameters:**
- owner: string
- repo: string
- title: string
- description: string
- due_on: string (ISO date, optional)
```

---

## 6. HYBRID APPROACH

### 6.1 Best Practice

```markdown
## INSTRUKCJA: Hybrid MCP + CLI

1. At session start:
   - Detect available MCP tools
   - Store in context

2. For each operation:
   - IF MCP tool available → Use MCP
   - ELSE → Use CLI command

3. Example flow:
```python
# Pseudocode
if mcp_tool_available("azure_devops_create_work_item"):
    result = use_mcp_tool("azure_devops_create_work_item", params)
else:
    result = run_bash("az boards work-item create ...")
```

4. Handle responses:
   - MCP: Structured JSON
   - CLI: Parse text output
```

---

## 7. CREATING CUSTOM MCP SERVER

### 7.1 When to Create

- Frequent integration with a service
- CLI is unreliable or slow
- Need better authentication management
- Want structured responses

### 7.2 Basic Structure

```javascript
// Example MCP server structure (Node.js)

const tools = {
  "custom_create_item": {
    description: "Creates an item in Custom Service",
    parameters: {
      type: "object",
      properties: {
        title: { type: "string" },
        description: { type: "string" }
      },
      required: ["title"]
    },
    handler: async (params) => {
      // Call external API
      const result = await customApi.createItem(params);
      return {
        id: result.id,
        url: result.url
      };
    }
  }
};
```

---

## 8. VOCABULARY

| Term | Meaning |
|------|---------|
| MCP | Model Context Protocol |
| MCP Server | Server providing tools via MCP |
| MCP Tool | Function callable through MCP |
| Fallback | Alternative method when MCP unavailable |
| Hybrid | Using both MCP and CLI as appropriate |
