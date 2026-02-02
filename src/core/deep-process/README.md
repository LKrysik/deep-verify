# Deep Process Engine

> **Version:** 1.0
> **Purpose:** Meta-framework for defining and executing processes via LLM CLI
> **Philosophy:** LLM follows the process, state is tracked automatically, unknown unknowns are discovered

---

## Quick Start

### 1. Initialize a Project

```
User: "Start a new project management project called MyApp"

LLM will:
1. Create .state/ directory
2. Initialize project-state.yaml
3. Show dashboard
4. Recommend first action
```

### 2. Follow the Process

```
User: "What should I do next?"

LLM will:
1. Read current state
2. Check planner rules
3. Recommend next step
4. Execute when confirmed
```

### 3. Check Status Anytime

```
User: "Show project status"

LLM will:
1. Display dashboard
2. Show blocking items
3. Show progress
4. Recommend next action
```

---

## Available Processes

| Process | Domain | Phases | Use When |
|---------|--------|--------|----------|
| [project-management](processes/project-management.md) | Software Dev | 6 | Building software with epics/stories |
| [ux-design](processes/ux-design.md) | UX Design | 6 | Designing user experiences |
| [code-documentation](processes/code-documentation.md) | Documentation | 5 | Documenting codebases |
| [custom-template](processes/custom-template.md) | Any | N | Creating your own process |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DEEP PROCESS ENGINE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ENGINE (How to execute)              PROCESSES (What to execute)           │
│  ├── executor.md                      ├── project-management.md             │
│  ├── enforcer.md                      ├── ux-design.md                      │
│  ├── state-manager.md                 ├── code-documentation.md             │
│  └── integrations/                    └── custom-template.md                │
│      ├── azure-devops.md                                                    │
│      ├── github.md                    SCHEMAS (Validation)                  │
│      └── mcp-template.md              ├── epic.schema.yaml                  │
│                                       ├── story.schema.yaml                 │
│                                       └── sprint.schema.yaml                │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STATE (.state/)                      ARTIFACTS (artifacts/)                │
│  ├── process.yaml                     ├── idea.md                           │
│  ├── phase.yaml                       ├── prd.md                            │
│  ├── items.yaml                       ├── epics/*.yaml                      │
│  ├── decisions.yaml                   ├── stories/*.yaml                    │
│  ├── unknowns.yaml                    └── ...                               │
│  └── history.yaml                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

### 1. Phases and Gates

Every process has ordered phases. You can't skip phases. Between phases are **gates** with verification criteria.

```
Phase 1 ──[Gate 0.70]──▶ Phase 2 ──[Gate 0.85]──▶ Phase 3
```

### 2. State Tracking

All state is in `.state/` directory. The LLM reads and updates it automatically.

### 3. Enforcement

The LLM **must** follow rules in `engine/enforcer.md`. No skipping steps, no ignoring blockers.

### 4. Unknown Unknowns

The system actively discovers things you don't know you don't know.

### 5. Integrations

Optionally sync with Azure DevOps, GitHub, or other tools.

---

## File Reference

| File | Purpose |
|------|---------|
| `engine/executor.md` | How LLM executes processes |
| `engine/enforcer.md` | Rules LLM must follow |
| `engine/state-manager.md` | How to manage .state/ |
| `engine/integrations/*.md` | External integrations |
| `processes/*.md` | Process definitions |
| `schemas/*.yaml` | Validation schemas |

---

## For LLM: Entry Points

When user wants to work with Deep Process:

1. **New project:** Read `engine/executor.md` → Section 9.1 (Initialization)
2. **Continue project:** Read `.state/phase.yaml` → Check current phase
3. **Execute step:** Read process definition → Find current step
4. **Check status:** Read all `.state/*.yaml` → Generate dashboard

---

## Creating Custom Processes

1. Copy `processes/custom-template.md`
2. Define your phases (3-7 recommended)
3. Define steps with requires/produces
4. Define gates with criteria
5. Test on real project

See [custom-template.md](processes/custom-template.md) for full instructions.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "State not found" | Run initialization |
| "Gate failed" | Address gaps listed in result |
| "Action blocked" | Resolve blockers first |
| "Integration failed" | Check auth, fall back to manual |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial release |
