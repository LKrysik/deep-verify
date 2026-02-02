---
contract: product-brief
version: "0.1"
required_fields:
  - id
  - name
  - status
  - version
required_sections:
  - Vision
  - Target Users
  - Core Problem
  - Success Metrics
  - MVP Scope
---

# Product Brief Contract

Product briefs created by BMAD workflows MUST follow this format.

---

## Required Frontmatter

| Field | Type | Values | Required |
|-------|------|--------|----------|
| `id` | string | e.g., "product-brief-myapp" | YES |
| `name` | string | Product name | YES |
| `status` | enum | draft, review, approved | YES |
| `version` | string | e.g., "1.0" | YES |
| `created` | date | ISO date | no |
| `author` | string | Author name | no |

---

## Required Sections

### `## Vision`
One-paragraph description of what the product will become and why it matters.

### `## Target Users`
Description of primary user personas with:
- Who they are
- What they need
- Why they would use this product

### `## Core Problem`
Clear statement of the problem being solved:
- Current pain points
- Impact of the problem
- Why existing solutions fail

### `## Success Metrics`
Measurable outcomes that define success:
- Business metrics
- User metrics
- Technical metrics

### `## MVP Scope`
What's included in the minimum viable product:
- In scope (must have)
- Out of scope (future)
- Open questions

---

## Optional Sections

- `## Market Context` — Competitive landscape
- `## Risks` — Known risks and mitigations
- `## Timeline` — High-level milestones
- `## Stakeholders` — Key people involved

---

## Example Valid Output

```markdown
---
id: product-brief-taskflow
name: TaskFlow
status: draft
version: "1.0"
created: 2026-02-02
author: Product Team
---

# TaskFlow Product Brief

## Vision

TaskFlow will be the simplest way for small teams to manage their daily work without the overhead of enterprise project management tools.

## Target Users

**Primary: Small Team Leads (5-15 people)**
- Managing cross-functional teams
- Need visibility without micromanagement
- Currently using spreadsheets or basic tools

**Secondary: Individual Contributors**
- Want to see their priorities clearly
- Need to update status quickly
- Prefer minimal process overhead

## Core Problem

Small teams struggle with task management because:
- Enterprise tools (Jira, Asana) are too complex
- Simple tools (Trello, Todoist) lack team features
- Spreadsheets don't scale and have no notifications

**Impact:** Teams waste 2-3 hours/week on status meetings that could be async.

## Success Metrics

**Business:**
- 1,000 active teams in 6 months
- 20% conversion from free to paid

**User:**
- 80% daily active users per team
- < 2 min average task update time

**Technical:**
- 99.9% uptime
- < 500ms page load

## MVP Scope

**In Scope:**
- Task creation and assignment
- Status updates (todo, doing, done)
- Team dashboard
- Email notifications

**Out of Scope (v2):**
- Time tracking
- Integrations
- Mobile app
- Custom workflows

**Open Questions:**
- Pricing model (per-seat vs per-team)?
- Self-serve or sales-led?
```
