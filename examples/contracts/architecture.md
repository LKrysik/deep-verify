---
contract: architecture
version: "0.1"
required_fields:
  - id
  - name
  - status
  - version
  - prd
required_sections:
  - Overview
  - Tech Stack
  - Architecture Decisions
  - Data Model
  - API Design
  - Security
  - Infrastructure
---

# Architecture Contract

Architecture documents created by BMAD workflows MUST follow this format.

---

## Required Frontmatter

| Field | Type | Values | Required |
|-------|------|--------|----------|
| `id` | string | e.g., "arch-taskflow" | YES |
| `name` | string | Architecture title | YES |
| `status` | enum | draft, review, approved | YES |
| `version` | string | e.g., "1.0" | YES |
| `prd` | string | Path to PRD | YES |
| `created` | date | ISO date | no |
| `author` | string | Author name | no |
| `reviewers` | list | Reviewer names | no |

---

## Required Sections

### `## Overview`
High-level architecture summary:
- System purpose
- Key architectural drivers
- Major components

### `## Tech Stack`
Technology choices with rationale:
- Frontend
- Backend
- Database
- Infrastructure
- Key libraries/frameworks

### `## Architecture Decisions`
ADRs (Architecture Decision Records):
- Decision ID and title
- Context
- Decision
- Consequences
- Alternatives considered

### `## Data Model`
Core data entities:
- Entity definitions
- Relationships
- Key constraints

### `## API Design`
API structure:
- Endpoints overview
- Authentication approach
- Error handling patterns

### `## Security`
Security architecture:
- Authentication
- Authorization
- Data protection
- Compliance considerations

### `## Infrastructure`
Deployment architecture:
- Environment strategy
- Scaling approach
- Monitoring and observability

---

## Optional Sections

- `## System Context Diagram` — C4 Level 1
- `## Container Diagram` — C4 Level 2
- `## Component Diagram` — C4 Level 3
- `## Sequence Diagrams` — Key flows
- `## Performance Considerations` — Optimization strategies
- `## Disaster Recovery` — Backup and recovery
- `## Migration Strategy` — If applicable

---

## Example Valid Output

```markdown
---
id: arch-taskflow
name: TaskFlow Architecture
status: draft
version: "1.0"
prd: docs/prd.md
created: 2026-02-02
author: Architecture Team
---

# TaskFlow Architecture

## Overview

TaskFlow is a lightweight task management SaaS application optimized for small teams.

**Key Architectural Drivers:**
- Simplicity over features
- Real-time collaboration
- Cost-effective scaling
- Fast time-to-market

**Major Components:**
- Web frontend (SPA)
- REST API backend
- PostgreSQL database
- Redis for real-time

## Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | React + TypeScript | Team expertise, ecosystem |
| Backend | Node.js + Express | JavaScript full-stack, fast development |
| Database | PostgreSQL | Relational data, ACID, proven |
| Cache/RT | Redis | Real-time pub/sub, session cache |
| Infra | AWS (ECS, RDS) | Managed services, scaling |
| CI/CD | GitHub Actions | Integrated with repo |

## Architecture Decisions

### ADR-001: Monolith First

**Context:** Team is small (3 developers), time-to-market is critical.

**Decision:** Start with a modular monolith, split later if needed.

**Consequences:**
- ✅ Faster development
- ✅ Simpler deployment
- ✅ Easier debugging
- ⚠️ Must maintain module boundaries
- ⚠️ May need to split later

**Alternatives Considered:**
- Microservices: Rejected (too complex for team size)
- Serverless: Rejected (cold start issues for real-time)

### ADR-002: PostgreSQL over NoSQL

**Context:** Data is relational (users → teams → tasks).

**Decision:** Use PostgreSQL as primary database.

**Consequences:**
- ✅ Strong consistency
- ✅ Complex queries supported
- ✅ Team familiarity
- ⚠️ Schema migrations required

## Data Model

### Core Entities

```
User
├── id: UUID (PK)
├── email: string (unique)
├── name: string
├── created_at: timestamp
└── team_id: UUID (FK → Team)

Team
├── id: UUID (PK)
├── name: string
├── created_at: timestamp
└── owner_id: UUID (FK → User)

Task
├── id: UUID (PK)
├── title: string
├── description: text
├── status: enum (todo, doing, done)
├── priority: enum (low, medium, high)
├── due_date: date (nullable)
├── created_at: timestamp
├── team_id: UUID (FK → Team)
├── assignee_id: UUID (FK → User, nullable)
└── creator_id: UUID (FK → User)
```

### Relationships
- User belongs to one Team
- Team has many Users
- Team has many Tasks
- Task belongs to one Team
- Task has one Assignee (User, optional)
- Task has one Creator (User)

## API Design

### Base URL
`https://api.taskflow.app/v1`

### Authentication
- JWT tokens (access + refresh)
- Access token in Authorization header
- Refresh via `/auth/refresh`

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/login | Login |
| POST | /auth/register | Register |
| GET | /tasks | List team tasks |
| POST | /tasks | Create task |
| PATCH | /tasks/:id | Update task |
| DELETE | /tasks/:id | Delete task |
| GET | /team | Get team info |
| GET | /team/members | List team members |

### Error Format
```json
{
  "error": {
    "code": "TASK_NOT_FOUND",
    "message": "Task with ID xyz not found",
    "details": {}
  }
}
```

## Security

### Authentication
- Email/password with bcrypt hashing
- JWT with 15min access / 7day refresh
- Future: OAuth (Google, GitHub)

### Authorization
- Team-based isolation (users see only their team)
- Role-based: owner, member
- Owner can: invite/remove members, delete team
- Member can: CRUD tasks

### Data Protection
- TLS 1.3 for all connections
- AES-256 encryption at rest (RDS)
- PII handling per GDPR

## Infrastructure

### Environments
| Env | Purpose | URL |
|-----|---------|-----|
| dev | Development | localhost |
| staging | Pre-production | staging.taskflow.app |
| prod | Production | taskflow.app |

### AWS Architecture
```
CloudFront (CDN)
    ↓
ALB (Load Balancer)
    ↓
ECS Fargate (API containers)
    ↓
RDS PostgreSQL + ElastiCache Redis
```

### Scaling Strategy
- ECS auto-scaling based on CPU/memory
- RDS read replicas if needed
- Redis cluster mode for high availability

### Monitoring
- CloudWatch for logs and metrics
- Sentry for error tracking
- PagerDuty for alerts
```
