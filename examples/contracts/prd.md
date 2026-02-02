---
contract: prd
version: "0.1"
required_fields:
  - id
  - name
  - status
  - version
  - product_brief
required_sections:
  - Overview
  - Goals & Success Metrics
  - User Personas
  - Functional Requirements
  - Non-Functional Requirements
  - MVP Scope
---

# PRD Contract

Product Requirements Documents created by BMAD workflows MUST follow this format.

---

## Required Frontmatter

| Field | Type | Values | Required |
|-------|------|--------|----------|
| `id` | string | e.g., "prd-taskflow" | YES |
| `name` | string | PRD title | YES |
| `status` | enum | draft, review, approved | YES |
| `version` | string | e.g., "1.0" | YES |
| `product_brief` | string | Path to product brief | YES |
| `created` | date | ISO date | no |
| `author` | string | Author name | no |
| `reviewers` | list | Reviewer names | no |

---

## Required Sections

### `## Overview`
Executive summary of the product:
- What it is
- Why we're building it
- Key value proposition

### `## Goals & Success Metrics`
Detailed success criteria:
- Business goals with metrics
- User goals with metrics
- Technical goals with metrics

### `## User Personas`
Detailed persona descriptions:
- Name and role
- Demographics
- Goals and motivations
- Pain points
- How they'll use the product

### `## Functional Requirements`
Feature specifications:
- Organized by feature area
- Each requirement has ID (e.g., FR-001)
- Clear acceptance criteria

### `## Non-Functional Requirements`
Quality attributes:
- Performance requirements
- Security requirements
- Scalability requirements
- Accessibility requirements

### `## MVP Scope`
Prioritized feature list:
- Must have (P0)
- Should have (P1)
- Nice to have (P2)
- Out of scope

---

## Optional Sections

- `## User Journeys` — Step-by-step flows
- `## Wireframes` — UI sketches
- `## Data Requirements` — Data entities
- `## Integration Requirements` — External systems
- `## Risks & Mitigations` — Risk register
- `## Timeline` — Release plan
- `## Glossary` — Domain terms

---

## Example Valid Output

```markdown
---
id: prd-taskflow
name: TaskFlow PRD
status: draft
version: "1.0"
product_brief: docs/product-brief.md
created: 2026-02-02
author: Product Team
---

# TaskFlow Product Requirements Document

## Overview

TaskFlow is a lightweight task management tool for small teams (5-15 people) who need visibility into work without the complexity of enterprise tools.

**Value Proposition:** Replace status meetings with real-time task visibility.

## Goals & Success Metrics

### Business Goals
| Goal | Metric | Target |
|------|--------|--------|
| User acquisition | Active teams | 1,000 in 6 months |
| Revenue | Conversion rate | 20% free → paid |
| Retention | Monthly churn | < 5% |

### User Goals
| Goal | Metric | Target |
|------|--------|--------|
| Adoption | DAU per team | 80% |
| Efficiency | Task update time | < 2 min |
| Satisfaction | NPS | > 40 |

### Technical Goals
| Goal | Metric | Target |
|------|--------|--------|
| Reliability | Uptime | 99.9% |
| Performance | Page load | < 500ms |
| Scalability | Concurrent users | 10,000 |

## User Personas

### Sarah - Team Lead
- **Role:** Engineering manager, 8 direct reports
- **Goals:** Know what everyone is working on without micromanaging
- **Pain Points:** Too many status meetings, lost context in Slack
- **Usage:** Checks dashboard every morning, reviews weekly

### Mike - Developer
- **Role:** Senior developer, works on 3-4 tasks at a time
- **Goals:** Clear priorities, minimal process overhead
- **Pain Points:** Jira is too complex, forgets to update status
- **Usage:** Updates tasks when switching context, daily

## Functional Requirements

### FR-100: Task Management
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-101 | User can create a task with title and description | P0 |
| FR-102 | User can assign a task to a team member | P0 |
| FR-103 | User can set task status (todo, doing, done) | P0 |
| FR-104 | User can set task priority (low, medium, high) | P1 |
| FR-105 | User can add due date to task | P1 |

### FR-200: Team Dashboard
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-201 | Dashboard shows all team tasks grouped by status | P0 |
| FR-202 | Dashboard shows tasks assigned to each member | P0 |
| FR-203 | Dashboard updates in real-time | P1 |

### FR-300: Notifications
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-301 | User receives email when assigned a task | P0 |
| FR-302 | User receives email for approaching due dates | P1 |

## Non-Functional Requirements

### Performance
- Page load time < 500ms (P50), < 1s (P95)
- API response time < 100ms (P50), < 500ms (P95)

### Security
- All data encrypted at rest and in transit
- SOC 2 Type II compliance within 12 months

### Scalability
- Support 10,000 concurrent users
- Support teams up to 50 members

### Accessibility
- WCAG 2.1 AA compliance
- Keyboard navigation support

## MVP Scope

### P0 - Must Have (MVP)
- [ ] Task CRUD operations
- [ ] Task assignment
- [ ] Status workflow (todo → doing → done)
- [ ] Team dashboard
- [ ] Email notifications for assignment

### P1 - Should Have (v1.1)
- [ ] Due dates and reminders
- [ ] Priority levels
- [ ] Real-time updates
- [ ] Basic search

### P2 - Nice to Have (v1.2+)
- [ ] Comments on tasks
- [ ] File attachments
- [ ] Custom statuses

### Out of Scope
- Time tracking
- External integrations
- Mobile app
- Custom workflows
```
