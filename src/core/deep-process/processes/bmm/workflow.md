# BMM (Business Motivation Model) Workflow V3.0

---

## INVOCATION

**When user wants to build a product, ALWAYS start with this:**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      BMM - Business Motivation Model                       ║
║                      From Idea to Working Product                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  BMM guides you through complete product development lifecycle.            ║
║                                                                            ║
║  PHASES:                                                                   ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [1] ANALYSIS    — Research, Product Brief                          │  ║
║  │  [2] PLANNING    — PRD, UX Design                                   │  ║
║  │  [3] SOLUTIONING — Architecture, Epics & Stories, Readiness Check  │  ║
║  │  [4] IMPLEMENTATION — Sprint Planning, Dev, Review, Deploy         │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  Where are you in the process?                                             ║
║  [1] Starting fresh — go to Phase 1                                       ║
║  [2] Have product brief — go to Phase 2                                   ║
║  [3] Have PRD + Architecture — go to Phase 3                              ║
║  [4] Have Stories ready — go to Phase 4                                   ║
║  [A] Work with an Agent                                                    ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## CONFIGURATION

Before any workflow, load config:
```
📂 Load: config.yaml

Resolve:
- project_name
- output_folder
- planning_artifacts
- user_name
- communication_language
- document_output_language
- user_skill_level
```

---

## PHASE 1: ANALYSIS

**Goal:** Understand the problem space, research, create product brief

**Workflows available:**

| Workflow | Description | Path |
|----------|-------------|------|
| **Research** | Market, domain, or technical research | `workflows/1-analysis/research/workflow.md` |
| **Create Product Brief** | Collaborative discovery to create brief | `workflows/1-analysis/create-product-brief/workflow.md` |

### Research Workflow

```
📂 Load: workflows/1-analysis/research/workflow.md

Supports 3 research tracks:
- Market Research (market-steps/)
- Domain Research (domain-steps/)
- Technical Research (technical-steps/)

Each track has 6 step files executed sequentially.
Output: research/{track}-research.md
```

### Create Product Brief Workflow

```
📂 Load: workflows/1-analysis/create-product-brief/workflow.md

Step-file architecture:
- step-01-init.md → Initialize, check existing brief
- step-01b-continue.md → Continue existing brief
- step-02-vision.md → Product vision discovery
- step-03-users.md → User personas and needs
- step-04-metrics.md → Success metrics
- step-05-scope.md → Scope boundaries
- step-06-complete.md → Finalize brief

Output: {planning_artifacts}/product-brief.md
Template: product-brief.template.md
```

**GATE: Phase 1 → Phase 2**
- [ ] Product Brief exists
- [ ] Problem validated
- [ ] Target users identified

---

## PHASE 2: PLANNING

**Goal:** Define WHAT to build (PRD), HOW it looks (UX)

**Workflows available:**

| Workflow | Description | Path |
|----------|-------------|------|
| **Create PRD** | Tri-modal: Create/Validate/Edit PRD | `workflows/2-plan-workflows/create-prd/workflow.md` |
| **Create UX Design** | User experience design | `workflows/2-plan-workflows/create-ux-design/workflow.md` |

### Create PRD Workflow (Tri-Modal)

```
📂 Load: workflows/2-plan-workflows/create-prd/workflow.md

Modes:
[C] Create — Create new PRD from scratch (steps-c/)
[V] Validate — Validate existing PRD (steps-v/)
[E] Edit — Improve existing PRD (steps-e/)

Create Mode Steps:
- step-01-init.md → Initialize, mode selection
- step-02-discovery.md → Requirements discovery
- step-03-success.md → Success criteria
- step-04-journeys.md → User journeys
- step-05-domain.md → Domain model
- step-06-innovation.md → Innovation areas
- step-07-project-type.md → Project classification
- step-08-scoping.md → Scope definition
- step-09-review.md → Final review

Output: {planning_artifacts}/prd.md
```

### Create UX Design Workflow

```
📂 Load: workflows/2-plan-workflows/create-ux-design/workflow.md

Step-file architecture for UX design discovery.
Output: {planning_artifacts}/ux-design.md
```

**GATE: Phase 2 → Phase 3**
- [ ] PRD complete with acceptance criteria
- [ ] UX flows defined (if UI exists)

---

## PHASE 3: SOLUTIONING

**Goal:** Architecture decisions, break down to stories, validate readiness

**Workflows available:**

| Workflow | Description | Path |
|----------|-------------|------|
| **Create Architecture** | Technical decisions | `workflows/3-solutioning/create-architecture/workflow.md` |
| **Create Epics & Stories** | Break PRD into implementable units | `workflows/3-solutioning/create-epics-and-stories/workflow.md` |
| **Check Implementation Readiness** | Adversarial alignment review | `workflows/3-solutioning/check-implementation-readiness/workflow.md` |

### Create Architecture Workflow

```
📂 Load: workflows/3-solutioning/create-architecture/workflow.md

Collaborative architectural decision facilitation.
Produces decision-focused architecture document.

Steps in steps/ folder executed sequentially.
Data files in data/ folder.

Output: {planning_artifacts}/architecture.md
Template: architecture-decision-template.md
```

### Create Epics & Stories Workflow

```
📂 Load: workflows/3-solutioning/create-epics-and-stories/workflow.md

Transforms PRD + Architecture into:
- Epics (high-level features)
- User Stories (implementable units)

Output:
- {planning_artifacts}/epics/*.md
- {planning_artifacts}/stories/*.md
```

### Check Implementation Readiness Workflow

```
📂 Load: workflows/3-solutioning/check-implementation-readiness/workflow.md

Adversarial review:
- PRD ↔ Architecture alignment
- Architecture ↔ Stories alignment
- Stories completeness check
- Gap identification

Output: Readiness Report (PASS/ISSUES)
```

**GATE: Phase 3 → Phase 4**
- [ ] Architecture documented
- [ ] All stories have acceptance criteria
- [ ] Implementation Readiness: PASSED

---

## PHASE 4: IMPLEMENTATION

**Goal:** Build, test, deploy working software

**Workflows available:**

| Workflow | Description | Path |
|----------|-------------|------|
| **Sprint Planning** | Plan sprint, select stories | `workflows/4-implementation/sprint-planning/workflow.yaml` |
| **Sprint Status** | Check status, surface risks | `workflows/4-implementation/sprint-status/workflow.yaml` |
| **Create Story** | Create next story from epics | `workflows/4-implementation/create-story/workflow.yaml` |
| **Dev Story** | Implement a story | `workflows/4-implementation/dev-story/workflow.yaml` |
| **Code Review** | Adversarial code review | `workflows/4-implementation/code-review/workflow.yaml` |
| **Correct Course** | Handle mid-sprint changes | `workflows/4-implementation/correct-course/workflow.yaml` |
| **Retrospective** | Review and learn | `workflows/4-implementation/retrospective/workflow.yaml` |

### Sprint Planning Workflow

```
📂 Load: workflows/4-implementation/sprint-planning/workflow.yaml

Instructions: instructions.md
Checklist: checklist.md
Template: sprint-status-template.yaml

Produces: {implementation_artifacts}/sprint-status.yaml
```

### Dev Story Workflow

```
📂 Load: workflows/4-implementation/dev-story/workflow.yaml

Instructions: instructions.xml (detailed implementation guide)
Checklist: checklist.md (validation criteria)

Process:
1. Load story file
2. Implement tasks/subtasks
3. Write tests
4. Validate against acceptance criteria
5. Update story status
```

### Code Review Workflow

```
📂 Load: workflows/4-implementation/code-review/workflow.yaml

ADVERSARIAL review:
- Find 3-10 specific problems in EVERY story
- Never accept "looks good"
- Check: code quality, tests, architecture, security, performance

Instructions: instructions.xml
Checklist: checklist.md
```

**GATE: Phase 4 → Done**
- [ ] All sprint stories completed
- [ ] Tests passing
- [ ] Code reviewed and approved

---

## WORKFLOW ARCHITECTURE (Common Pattern)

All BMM workflows use **step-file architecture**:

```
workflow.md (or workflow.yaml)
├── Steps loaded sequentially (never ahead)
├── Each step is self-contained
├── State tracked in output frontmatter (stepsCompleted)
├── Append-only document building
└── Halt at menus, wait for user input

RULES:
🛑 NEVER load multiple step files simultaneously
📖 ALWAYS read entire step file before execution
🚫 NEVER skip steps or optimize sequence
💾 ALWAYS update frontmatter when completing step
⏸️ ALWAYS halt at menus and wait for input
```

---

## AGENTS

Agents are optional. Load from `agents/` folder.

| Agent | Role | Best For |
|-------|------|----------|
| analyst | Business Analyst | Research, Product Brief |
| pm | Product Manager | PRD, Stories |
| architect | System Architect | Architecture |
| ux-designer | UX Designer | UX Design |
| dev | Developer | Implementation |
| sm | Scrum Master | Sprint Management |
| quinn | General Guide | Navigation, Help |

```
📂 Load: agents/_index.yaml → see all agents
📂 Load: agents/{name}.md → activate specific agent
```

---

## FILE STRUCTURE

```
processes/bmm/
├── workflow.md                    ← YOU ARE HERE
├── process.yaml                   ← Minimal metadata
├── config.yaml                    ← Project configuration
├── agents/
│   ├── _index.yaml
│   └── {agent}.md
├── workflows/
│   ├── 1-analysis/
│   │   ├── create-product-brief/
│   │   │   ├── workflow.md
│   │   │   ├── steps/step-01-init.md ... step-06-complete.md
│   │   │   └── product-brief.template.md
│   │   └── research/
│   │       ├── workflow.md
│   │       ├── market-steps/
│   │       ├── domain-steps/
│   │       ├── technical-steps/
│   │       └── research.template.md
│   ├── 2-plan-workflows/
│   │   ├── create-prd/
│   │   │   ├── workflow.md
│   │   │   ├── steps-c/ (create mode)
│   │   │   ├── steps-v/ (validate mode)
│   │   │   └── steps-e/ (edit mode)
│   │   └── create-ux-design/
│   ├── 3-solutioning/
│   │   ├── create-architecture/
│   │   │   ├── workflow.md
│   │   │   ├── steps/
│   │   │   └── data/
│   │   ├── create-epics-and-stories/
│   │   └── check-implementation-readiness/
│   └── 4-implementation/
│       ├── sprint-planning/
│       │   ├── workflow.yaml
│       │   ├── instructions.md
│       │   ├── checklist.md
│       │   └── sprint-status-template.yaml
│       ├── dev-story/
│       │   ├── workflow.yaml
│       │   ├── instructions.xml
│       │   └── checklist.md
│       ├── code-review/
│       ├── sprint-status/
│       ├── create-story/
│       ├── correct-course/
│       └── retrospective/
├── data/
│   └── templates/
└── schemas/
```
