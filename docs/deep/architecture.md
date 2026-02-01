# Deep Cognitive Architecture v0.1

> **Status:** Draft / Proof-of-Concept
> **Data:** 2026-02-01
> **Cel:** Transformacja wizji → działający kod z pełną weryfikacją i śledzeniem stanu

---

## Problem Statement

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  PROBLEM 1: "Nie wiem czego nie wiem"                                             ║
║  → System musi aktywnie ODKRYWAĆ unknown unknowns                                 ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  PROBLEM 2: "Żebym nie musiał myśleć gdzie jesteśmy"                              ║
║  → Automatyczne śledzenie stanu, pełna visibility                                 ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  PROBLEM 3: "LLM nie może całości ogarnąć"                                        ║
║  → Hierarchiczna pamięć, context compression, knowledge graph                     ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  PROBLEM 4: "Wizja → Kod" z weryfikacją                                           ║
║  → End-to-end pipeline z checkpoints i verification gates                         ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  PROBLEM 5: "Dostosowywać workflow do projektu"                                   ║
║  → Modular processes, configurable per project                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  PROBLEM 6: "Wielu agentów pracuje równocześnie"                                  ║
║  → Per-agent/per-task working memory, task resumability                           ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Inspiracje i źródła

### CoALA (Cognitive Architectures for Language Agents)
- Paper: https://arxiv.org/abs/2309.02427
- Framework dzieli agenta na moduły pamięci:
  - **Working Memory** — aktualny kontekst
  - **Episodic Memory** — co robiliśmy wcześniej
  - **Semantic Memory** — wiedza o świecie
  - **Procedural Memory** — jak wykonywać operacje

### Architecture Decision Records (ADR)
- Guide: https://adr.github.io/
- Proven pattern do śledzenia decyzji z rationale

### Knowledge Graphs dla kodu
- Paper: https://arxiv.org/html/2505.14394v1
- Rozwiązanie problemu "LLM nie ogania całości"

### LangGraph
- State as first-class citizen
- Checkpoints/Persistence
- Human-in-the-loop interrupts

---

## Architektura — 5 warstw

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                         DEEP COGNITIVE ARCHITECTURE                               ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║
║  │                        LAYER 5: META-COGNITIVE                              │  ║
║  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │  ║
║  │  │ What to do next │  │ Which operation │  │ Is this working │             │  ║
║  │  │ (Planner)       │  │ (Selector)      │  │ (Evaluator)     │             │  ║
║  │  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │  ║
║  └───────────┼─────────────────────┼─────────────────────┼─────────────────────┘  ║
║              │                     │                     │                        ║
║  ┌───────────▼─────────────────────▼─────────────────────▼─────────────────────┐  ║
║  │                        LAYER 4: COGNITIVE OPERATIONS                        │  ║
║  │                                                                              │  ║
║  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │  ║
║  │  │ deep-    │ │ deep-    │ │ deep-    │ │ deep-    │ │ deep-    │          │  ║
║  │  │ explore  │ │ challenge│ │ verify   │ │ risk     │ │ synthesis│   ...    │  ║
║  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘          │  ║
║  │                                                                              │  ║
║  └──────────────────────────────────┬───────────────────────────────────────────┘  ║
║                                     │                                              ║
║  ┌──────────────────────────────────▼───────────────────────────────────────────┐  ║
║  │                        LAYER 3: PROJECT STATE                                │  ║
║  │                                                                              │  ║
║  │  ┌─────────────────────────────────────────────────────────────────────┐    │  ║
║  │  │  PROJECT STATE MACHINE                                              │    │  ║
║  │  │  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐   │    │  ║
║  │  │  │IDEA │───►│SPEC │───►│ARCH │───►│IMPL │───►│TEST │───►│DONE │   │    │  ║
║  │  │  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘   │    │  ║
║  │  └─────────────────────────────────────────────────────────────────────┘    │  ║
║  │                                                                              │  ║
║  │  + Task Queue + Agent Assignments + Verification Gates                      │  ║
║  │                                                                              │  ║
║  └──────────────────────────────────┬───────────────────────────────────────────┘  ║
║                                     │                                              ║
║  ┌──────────────────────────────────▼───────────────────────────────────────────┐  ║
║  │                        LAYER 2: MEMORY SYSTEM                                │  ║
║  │                                                                              │  ║
║  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐           │  ║
║  │  │ WORKING MEMORY   │  │ EPISODIC MEMORY  │  │ SEMANTIC MEMORY  │           │  ║
║  │  │ (per agent/task) │  │ (per project)    │  │ (global)         │           │  ║
║  │  └──────────────────┘  └──────────────────┘  └──────────────────┘           │  ║
║  │                                                                              │  ║
║  │  ┌──────────────────┐  ┌──────────────────┐                                 │  ║
║  │  │ PROCEDURAL MEM   │  │ PROJECT GRAPH    │                                 │  ║
║  │  │ (how to do ops)  │  │ (knowledge graph)│                                 │  ║
║  │  └──────────────────┘  └──────────────────┘                                 │  ║
║  │                                                                              │  ║
║  └──────────────────────────────────┬───────────────────────────────────────────┘  ║
║                                     │                                              ║
║  ┌──────────────────────────────────▼───────────────────────────────────────────┐  ║
║  │                        LAYER 1: ARTIFACTS                                    │  ║
║  │                                                                              │  ║
║  │  📄 project-state.yaml     📄 decisions/*.yaml    📄 reasoning-traces/      │  ║
║  │  📄 tasks/*.yaml           📄 artifacts/*         📄 code/**                │  ║
║  │                                                                              │  ║
║  └──────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## LAYER 1: Artifacts — Struktura plików

### Struktura katalogu projektu

```
my-project/
├── .deep/                          # Deep Cognitive system files
│   ├── project-state.yaml          # Single source of truth
│   ├── tasks/                      # Task queue
│   │   ├── task-001.yaml
│   │   └── task-002.yaml
│   ├── agents/                     # Per-agent working memory
│   │   ├── agent-main.yaml
│   │   └── agent-code-001.yaml
│   ├── memory/
│   │   ├── episodic.yaml           # Session history
│   │   ├── semantic.yaml           # Domain knowledge
│   │   └── graph.yaml              # Project knowledge graph
│   └── traces/                     # Reasoning traces
│       └── 2026-02-01-session-1.yaml
│
├── docs/
│   ├── idea.md                     # Phase: IDEA output
│   ├── prd.md                      # Phase: SPEC output
│   ├── architecture.md             # Phase: ARCH output
│   └── decisions/                  # ADRs
│       ├── ADR-001.yaml
│       └── ADR-002.yaml
│
├── src/                            # Phase: IMPL output
└── tests/                          # Phase: TEST output
```

### 1.1 project-state.yaml — Single Source of Truth

```yaml
# .deep/project-state.yaml

version: "0.1"
project:
  name: "MyApp"
  created: 2026-02-01
  description: "Habit tracking application"

# ═══════════════════════════════════════════════════════════════
# CURRENT STATE
# ═══════════════════════════════════════════════════════════════

current:
  phase: architecture          # idea | specification | architecture | implementation | testing | done
  phase_progress: 0.42         # 0.0 - 1.0

  active_agents:
    - id: agent-main
      task: task-003
      status: working
    - id: agent-code-001
      task: task-005
      status: waiting_for_input

  blocking_items:
    - type: decision
      id: ADR-003
      title: "Database choice"
      blocks: [task-004, task-006]
    - type: question
      id: Q-007
      title: "Expected concurrent users?"
      asked_at: 2026-02-01T14:30:00Z

# ═══════════════════════════════════════════════════════════════
# PHASES HISTORY
# ═══════════════════════════════════════════════════════════════

phases:
  idea:
    status: completed
    started: 2026-02-01T10:00:00Z
    completed: 2026-02-01T11:30:00Z
    verification_score: 0.85
    artifacts: [docs/idea.md]
    decisions_made: [ADR-001]

  specification:
    status: completed
    started: 2026-02-01T11:30:00Z
    completed: 2026-02-01T14:00:00Z
    verification_score: 0.92
    artifacts: [docs/prd.md]
    decisions_made: [ADR-002]
    requirements:
      functional: 15
      non_functional: 8
      coverage: 1.0

  architecture:
    status: in_progress
    started: 2026-02-01T14:00:00Z
    verification_score: null      # not yet verified
    artifacts: [docs/architecture.md]
    decisions_made: []
    decisions_pending: [ADR-003, ADR-004]

  implementation:
    status: not_started

  testing:
    status: not_started

# ═══════════════════════════════════════════════════════════════
# VERIFICATION GATES
# ═══════════════════════════════════════════════════════════════

verification_gates:
  - gate: idea_to_spec
    status: passed
    score: 0.85
    threshold: 0.70
    passed_at: 2026-02-01T11:30:00Z

  - gate: spec_to_arch
    status: passed
    score: 0.92
    threshold: 0.85
    passed_at: 2026-02-01T14:00:00Z

  - gate: arch_to_impl
    status: pending
    required_score: 0.80
    blocking_reasons:
      - "2 decisions pending"
      - "Architecture not verified"

  - gate: impl_to_test
    status: not_reached

  - gate: test_to_done
    status: not_reached

# ═══════════════════════════════════════════════════════════════
# UNKNOWN UNKNOWNS TRACKING
# ═══════════════════════════════════════════════════════════════

unknowns:
  discovered:
    - id: UNK-001
      description: "Mobile app needs different auth flow"
      discovered_at: 2026-02-01T12:15:00Z
      discovered_via: deep-challenge
      status: addressed
      addressed_in: ADR-002

    - id: UNK-002
      description: "Rate limiting not considered in PRD"
      discovered_at: 2026-02-01T13:45:00Z
      discovered_via: deep-verify
      status: added_to_requirements

  to_explore:
    - id: UNK-003
      description: "Scaling strategy unclear"
      priority: medium
      suggested_operation: deep-explore

# ═══════════════════════════════════════════════════════════════
# TASK QUEUE
# ═══════════════════════════════════════════════════════════════

task_queue:
  pending:
    - task-004  # Blocked by ADR-003
    - task-006  # Blocked by ADR-003
  in_progress:
    - task-003  # agent-main
    - task-005  # agent-code-001
  completed:
    - task-001
    - task-002

# ═══════════════════════════════════════════════════════════════
# METRICS
# ═══════════════════════════════════════════════════════════════

metrics:
  decisions_made: 2
  decisions_pending: 2
  unknowns_discovered: 3
  unknowns_addressed: 2
  verification_gates_passed: 2
  verification_gates_remaining: 3
  total_sessions: 3
  total_operations: 12
```

### 1.2 Task File — Per-task definition

```yaml
# .deep/tasks/task-003.yaml

id: task-003
title: "Design API endpoints"
type: cognitive_operation

status: in_progress
assigned_to: agent-main
started_at: 2026-02-01T14:30:00Z

# What this task does
operation: deep-architecture
scope: "API layer design"

# Dependencies
depends_on: [task-001, task-002]
blocks: [task-007, task-008]
blocked_by: []

# Input context (what agent needs to know)
input_context:
  artifacts:
    - path: docs/prd.md
      sections: [functional_requirements, api_requirements]
    - path: docs/architecture.md
      sections: [high_level_design]
  decisions:
    - ADR-001
    - ADR-002
  questions_to_resolve:
    - "REST or GraphQL?"
    - "Authentication mechanism?"

# Expected outputs
expected_outputs:
  - type: artifact_section
    path: docs/architecture.md
    section: api_design
  - type: decisions
    ids: [ADR-004, ADR-005]

# Working memory snapshot (for resumability)
working_memory_snapshot:
  last_updated: 2026-02-01T15:00:00Z
  current_focus: "Evaluating REST vs GraphQL"
  progress: 0.6
  open_threads:
    - "Need to consider mobile app constraints"
    - "WebSocket for real-time updates?"
  tentative_conclusions:
    - "REST seems simpler for our use case"
    - "JWT for authentication"
```

### 1.3 Agent Working Memory — Per-agent state

```yaml
# .deep/agents/agent-main.yaml

agent:
  id: agent-main
  type: orchestrator
  created: 2026-02-01T10:00:00Z

# Current assignment
current_task:
  id: task-003
  started: 2026-02-01T14:30:00Z

# Working memory (task-specific, enables resumability)
working_memory:
  task_id: task-003

  # What I'm currently thinking about
  focus:
    topic: "API design decision"
    sub_topic: "REST vs GraphQL evaluation"

  # Loaded context (what's in my "head")
  loaded_context:
    - source: docs/prd.md
      summary: "15 FRs, mobile-first app, real-time sync needed"
      key_points:
        - "FR-003: Real-time habit updates"
        - "FR-007: Offline support required"
        - "NFR-002: Response time < 200ms"

    - source: docs/architecture.md
      summary: "Modular monolith, React Native frontend"
      relevant_decisions:
        - "ADR-001: React Native chosen"

  # My current thinking
  reasoning_state:
    hypothesis: "REST + WebSocket hybrid might be best"
    evidence_for:
      - "REST is simpler, team knows it"
      - "WebSocket can handle real-time"
    evidence_against:
      - "Two protocols to maintain"
      - "GraphQL could do both with subscriptions"
    confidence: 0.65

  # Questions I need answered
  open_questions:
    - question: "What's the team's GraphQL experience?"
      status: asked_user
      asked_at: 2026-02-01T15:10:00Z
    - question: "Is real-time critical or nice-to-have?"
      status: pending

  # Things I've decided (tentatively)
  tentative_decisions:
    - decision: "JWT for auth"
      confidence: 0.9
      rationale: "Standard, works offline, mobile-friendly"

  # Things to remember for later
  notes:
    - "User mentioned budget constraints - keep infra simple"
    - "Mobile app is priority, web is phase 2"

# Session history (for this agent)
sessions:
  - date: 2026-02-01
    tasks_worked: [task-001, task-003]
    operations_performed: [deep-challenge, deep-explore, deep-architecture]

# Learned preferences (agent-specific)
learned:
  - "User prefers simple solutions over clever ones"
  - "Always check mobile implications"
```

### 1.4 Decision Record (ADR)

```yaml
# docs/decisions/ADR-003.yaml

id: ADR-003
title: "Database technology choice"
status: pending  # draft | pending | accepted | rejected | superseded

created: 2026-02-01T14:00:00Z
decision_needed_by: 2026-02-02T00:00:00Z  # blocking impl

# Context
context:
  problem: |
    Need to choose database for habit tracking app.
    Must support: user data, habit definitions, daily logs, streaks.

  drivers:
    - "Mobile-first, needs offline sync"
    - "Expected 10k users in year 1"
    - "Team familiar with SQL"
    - "Budget: prefer managed service"

  discovered_via: deep-architecture
  related_requirements: [FR-001, FR-005, NFR-001, NFR-003]

# Options analysis
options:
  - id: postgresql
    name: "PostgreSQL (Supabase)"
    pros:
      - "Team knows SQL"
      - "Supabase has good React Native SDK"
      - "Built-in auth, real-time subscriptions"
      - "Generous free tier"
    cons:
      - "Offline sync more complex"
      - "Need to design conflict resolution"
    effort: medium
    risk: low

  - id: mongodb
    name: "MongoDB Atlas"
    pros:
      - "Flexible schema for habits"
      - "Realm SDK for offline"
    cons:
      - "Team needs to learn"
      - "More expensive at scale"
    effort: high
    risk: medium

  - id: sqlite_sync
    name: "SQLite + Custom Sync"
    pros:
      - "Perfect offline support"
      - "No vendor lock-in"
    cons:
      - "Must build sync layer"
      - "Significant effort"
    effort: very_high
    risk: high

# Evaluation (if performed)
evaluation:
  method: deep-explore
  performed_at: 2026-02-01T16:00:00Z

  scoring:
    postgresql:
      team_fit: 0.9
      feature_fit: 0.8
      cost: 0.9
      risk: 0.9
      total: 0.875
    mongodb:
      team_fit: 0.5
      feature_fit: 0.85
      cost: 0.7
      risk: 0.7
      total: 0.688
    sqlite_sync:
      team_fit: 0.8
      feature_fit: 0.95
      cost: 0.95
      risk: 0.4
      total: 0.775

  recommendation: postgresql
  confidence: 0.8
  reasoning: |
    PostgreSQL via Supabase offers best balance of team familiarity,
    features, and cost. Offline sync is harder but doable with
    existing libraries.

# Decision (when made)
decision: null  # will be: postgresql | mongodb | sqlite_sync
decided_by: null
decided_at: null
rationale: null

# Consequences (filled after decision)
consequences:
  positive: []
  negative: []
  neutral: []

# Traceability
traces:
  requirements: [FR-001, FR-005, NFR-001, NFR-003]
  architecture_sections: [data_layer, sync_strategy]
  affected_tasks: [task-004, task-006]
```

### 1.5 Reasoning Trace

```yaml
# .deep/traces/2026-02-01-session-2.yaml

session:
  id: session-002
  date: 2026-02-01
  started: 2026-02-01T14:00:00Z
  ended: 2026-02-01T16:30:00Z

  goal: "Design system architecture"
  outcome: partial_success
  outcome_reason: "Main architecture done, 2 decisions still pending"

  agents_involved:
    - agent-main

  phase_at_start: specification
  phase_at_end: architecture

# Operations performed
operations:
  - order: 1
    operation: deep-explore
    agent: agent-main
    started: 2026-02-01T14:00:00Z
    duration_minutes: 25

    input:
      artifacts: [docs/prd.md]
      goal: "Explore architectural patterns"

    output:
      dimensions_discovered: 4
      options_found: 12
      constraints_identified: 3

    insights:
      - "Microservices overkill for MVP"
      - "Monolith with modules sufficient"
      - "Need to decide: SQL vs NoSQL"

    unknowns_discovered:
      - UNK-002: "Rate limiting not in PRD"

  - order: 2
    operation: deep-challenge
    agent: agent-main
    started: 2026-02-01T14:25:00Z
    duration_minutes: 20

    input:
      target: "Monolith decision"

    challenges_raised:
      - "What if one module needs scaling?"
      - "How to deploy updates safely?"

    resolution: |
      Modular monolith with clear API boundaries.
      Can extract to microservice later if needed.

    confidence_change: 0.7 -> 0.85

  - order: 3
    operation: deep-architecture
    agent: agent-main
    started: 2026-02-01T14:45:00Z
    duration_minutes: 60

    input:
      scope: "Full system architecture"
      constraints: [budget_limited, team_small, mobile_first]

    output:
      artifact_created: docs/architecture.md
      sections_written:
        - high_level_design
        - component_diagram
        - data_flow
      decisions_needed:
        - ADR-003: "Database choice"
        - ADR-004: "API style"

  - order: 4
    operation: deep-explore
    agent: agent-main
    started: 2026-02-01T15:45:00Z
    duration_minutes: 45

    input:
      target: ADR-003
      goal: "Evaluate database options"

    output:
      options_analyzed: 3
      recommendation: postgresql
      confidence: 0.8

    awaiting: "User decision"

# Session summary
summary:
  operations_count: 4
  decisions_made: 0
  decisions_pending: 2
  unknowns_discovered: 1
  artifacts_created: 1
  artifacts_updated: 0

  key_learnings:
    - "User prefers pragmatic solutions"
    - "Budget is a real constraint"
    - "Mobile offline is critical"

  next_session_should:
    - "Get user decision on ADR-003"
    - "Complete ADR-004 (API style)"
    - "Run deep-verify on architecture"
```

---

## LAYER 2: Memory System

### 2.1 Memory Types

| Memory Type | Scope | Persistence | Purpose |
|-------------|-------|-------------|---------|
| **Working Memory** | Per agent, per task | Session (with snapshots) | Current thinking, loaded context |
| **Episodic Memory** | Per project | Permanent | What we did, what worked |
| **Semantic Memory** | Global | Permanent | Domain knowledge, patterns |
| **Procedural Memory** | Global | Permanent | How to do operations (deep-*) |
| **Project Graph** | Per project | Permanent | Knowledge graph of artifacts |

### 2.2 Working Memory — Multi-agent design

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           WORKING MEMORY ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐            │
│  │   AGENT-MAIN    │    │  AGENT-CODE-01  │    │  AGENT-CODE-02  │            │
│  │                 │    │                 │    │                 │            │
│  │  Task: task-003 │    │  Task: task-005 │    │  Task: task-006 │            │
│  │  ┌───────────┐  │    │  ┌───────────┐  │    │  ┌───────────┐  │            │
│  │  │ Working   │  │    │  │ Working   │  │    │  │ Working   │  │            │
│  │  │ Memory    │  │    │  │ Memory    │  │    │  │ Memory    │  │            │
│  │  │           │  │    │  │           │  │    │  │           │  │            │
│  │  │ • Focus   │  │    │  │ • Focus   │  │    │  │ • Focus   │  │            │
│  │  │ • Context │  │    │  │ • Context │  │    │  │ • Context │  │            │
│  │  │ • State   │  │    │  │ • State   │  │    │  │ • State   │  │            │
│  │  └───────────┘  │    │  └───────────┘  │    │  └───────────┘  │            │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘            │
│           │                      │                      │                      │
│           └──────────────────────┼──────────────────────┘                      │
│                                  │                                             │
│                                  ▼                                             │
│                    ┌─────────────────────────┐                                 │
│                    │    SHARED PROJECT       │                                 │
│                    │       STATE             │                                 │
│                    │                         │                                 │
│                    │  • project-state.yaml   │                                 │
│                    │  • Episodic Memory      │                                 │
│                    │  • Project Graph        │                                 │
│                    │  • Decision Log         │                                 │
│                    └─────────────────────────┘                                 │
│                                                                                 │
│  KEY PRINCIPLE:                                                                │
│  • Working Memory is ISOLATED per agent/task                                   │
│  • Agents COMMIT to shared state when task completes                          │
│  • Working Memory can be SNAPSHOTTED for task resumability                    │
│  • Context is LOADED from shared state at task start                          │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Project Knowledge Graph

```yaml
# .deep/memory/graph.yaml

# Nodes represent artifacts, decisions, requirements
nodes:
  requirements:
    FR-001:
      type: functional_requirement
      title: "User registration"
      status: implemented

    FR-002:
      type: functional_requirement
      title: "Habit creation"
      status: in_architecture

    NFR-001:
      type: non_functional_requirement
      title: "Response time < 200ms"
      status: specified

  decisions:
    ADR-001:
      type: decision
      title: "React Native for mobile"
      status: accepted

    ADR-003:
      type: decision
      title: "Database choice"
      status: pending

  architecture:
    ARCH-001:
      type: component
      title: "Auth Module"
      status: designed

    ARCH-002:
      type: component
      title: "Habit Service"
      status: in_progress

  code:
    CODE-auth:
      type: code_module
      path: src/auth/
      files: 8
      test_coverage: 0.85

# Edges represent relationships
edges:
  # Requirements -> Architecture
  - from: FR-001
    to: ARCH-001
    type: implemented_by

  - from: FR-002
    to: ARCH-002
    type: implemented_by

  # Decisions -> Architecture
  - from: ADR-001
    to: ARCH-001
    type: affects

  - from: ADR-003
    to: ARCH-002
    type: blocks

  # Architecture -> Code
  - from: ARCH-001
    to: CODE-auth
    type: realized_by

# Queries this enables:
# - "What requirements are not yet implemented?"
# - "What is blocked by ADR-003?"
# - "What code implements FR-001?"
# - "What decisions affect the Auth Module?"
```

---

## LAYER 3: Project State Machine

### 3.1 Phases and Gates

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                           PROJECT STATE MACHINE                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌────────┐ ║
║   │   IDEA   │────►│   SPEC   │────►│   ARCH   │────►│   IMPL   │────►│  TEST  │ ║
║   │          │     │          │     │          │     │          │     │        │ ║
║   │ Clarity  │     │ Complete │     │ Sound    │     │ Working  │     │ Verified║
║   │ ≥ 0.70   │     │ ≥ 0.85   │     │ ≥ 0.80   │     │ tests ✓  │     │ cov ≥  │ ║
║   └────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘     │  0.80  │ ║
║        │                │                │                │           └───┬────┘ ║
║   ─────┴────────────────┴────────────────┴────────────────┴───────────────┴───── ║
║      GATE 1           GATE 2           GATE 3           GATE 4          GATE 5   ║
║                                                                                   ║
║   Gate = deep-verify with specific criteria                                       ║
║   Failed gate = loop back or address issues                                       ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

### 3.2 Verification Gate Definitions

```yaml
# Gate definitions

gates:
  idea_to_spec:
    name: "Idea Clarity Gate"
    operation: deep-verify
    criteria:
      - check: "Problem statement is clear"
        weight: 0.3
      - check: "Target user defined"
        weight: 0.2
      - check: "Success criteria stated"
        weight: 0.2
      - check: "Scope boundaries exist"
        weight: 0.2
      - check: "No critical unknowns blocking"
        weight: 0.1
    threshold: 0.70
    on_fail:
      action: loop_back
      target: idea
      suggested_operation: deep-challenge

  spec_to_arch:
    name: "Specification Completeness Gate"
    operation: deep-verify
    criteria:
      - check: "All user stories have acceptance criteria"
        weight: 0.25
      - check: "Non-functional requirements defined"
        weight: 0.20
      - check: "No conflicting requirements"
        weight: 0.20
      - check: "Dependencies identified"
        weight: 0.15
      - check: "Risks documented"
        weight: 0.10
      - check: "Priorities assigned"
        weight: 0.10
    threshold: 0.85
    on_fail:
      action: address_gaps
      suggested_operation: deep-requirements

  arch_to_impl:
    name: "Architecture Soundness Gate"
    operation: deep-verify
    criteria:
      - check: "All requirements have architectural home"
        weight: 0.25
      - check: "No blocking decisions pending"
        weight: 0.25
      - check: "Component interfaces defined"
        weight: 0.20
      - check: "Data model complete"
        weight: 0.15
      - check: "Deployment strategy defined"
        weight: 0.15
    threshold: 0.80
    on_fail:
      action: resolve_blockers
      suggested_operation: deep-architecture

  impl_to_test:
    name: "Implementation Completeness Gate"
    operation: deep-verify
    criteria:
      - check: "All planned features implemented"
        weight: 0.30
      - check: "Unit tests pass"
        weight: 0.25
      - check: "No critical bugs known"
        weight: 0.25
      - check: "Code review completed"
        weight: 0.20
    threshold: 0.90
    on_fail:
      action: fix_issues
      suggested_operation: deep-develop

  test_to_done:
    name: "Quality Assurance Gate"
    operation: deep-verify
    criteria:
      - check: "Test coverage ≥ 80%"
        weight: 0.25
      - check: "All acceptance criteria verified"
        weight: 0.30
      - check: "Performance requirements met"
        weight: 0.20
      - check: "Security review passed"
        weight: 0.15
      - check: "Documentation complete"
        weight: 0.10
    threshold: 0.85
    on_fail:
      action: address_quality
```

---

## LAYER 4: Cognitive Operations

### 4.1 Operation Registry

| Operation | Purpose | When to use | Key outputs |
|-----------|---------|-------------|-------------|
| `deep-challenge` | Crystallize vague ideas | Unclear vision, ambiguity | Clear problem statement |
| `deep-explore` | Discover option space | Before decisions | Dimensions, options, constraints |
| `deep-requirements` | Define what to build | After idea crystallized | PRD, FRs, NFRs |
| `deep-architecture` | Design how to build | After requirements | Architecture doc, ADRs |
| `deep-risk` | Identify threats | Any phase | Risk register |
| `deep-feasibility` | Check if possible | After architecture | Feasibility report |
| `deep-verify` | Check consistency | Gate transitions | Verification score |
| `deep-develop` | Write code | Implementation phase | Working code |
| `deep-synthesis` | Compress knowledge | After exploration | Minimal assertions |

### 4.2 Operation Interface Contract

```yaml
# Template for each operation

operation_contract:
  name: string                    # e.g., "deep-explore"
  version: string                 # e.g., "1.0"

  # When this operation is applicable
  applicable_when:
    phases: [list of phases]      # e.g., [idea, specification, architecture]
    conditions: [list]            # e.g., ["decision_pending", "unknowns_exist"]

  # Required inputs
  inputs:
    required:
      - name: string
        type: artifact | decision | question
        description: string
    optional:
      - name: string
        type: any
        default: value

  # Guaranteed outputs
  outputs:
    - name: string
      type: artifact | decision | insight | unknown
      description: string

  # Side effects on project state
  state_effects:
    may_create: [artifact types]
    may_update: [state fields]
    may_discover: [unknowns, questions]
    may_resolve: [decisions, questions]

  # Success criteria
  success_criteria:
    - criterion: string
      measurement: string

  # Estimated effort
  effort:
    typical_duration: string      # e.g., "15-30 min"
    context_needed: low | medium | high
```

---

## LAYER 5: Meta-Cognitive Layer

### 5.1 Planner — "What to do next"

```yaml
# meta-cognitive/planner-rules.yaml

rules:
  # Phase-based rules
  - name: "Unclear idea"
    condition:
      phase: idea
      clarity_score: "< 0.7"
    recommend:
      operation: deep-challenge
      reason: "Idea not clear enough to proceed"
      priority: critical

  - name: "Too many open questions"
    condition:
      any_phase: true
      open_questions_count: "> 3"
    recommend:
      operation: deep-challenge
      target: open_questions
      reason: "Too many unanswered questions blocking progress"
      priority: high

  - name: "Blocking decision"
    condition:
      blocking_decisions_count: "> 0"
    recommend:
      operation: deep-explore
      target: "oldest_blocking_decision"
      reason: "Decision needed to unblock work"
      priority: high

  - name: "Ready for gate"
    condition:
      phase_progress: "> 0.9"
      blocking_decisions_count: 0
      open_questions_count: "< 2"
    recommend:
      operation: deep-verify
      target: "current_phase_gate"
      reason: "Phase looks complete, verify before proceeding"
      priority: medium

  - name: "Unknown discovered"
    condition:
      unknowns_to_explore_count: "> 0"
    recommend:
      operation: deep-explore
      target: "highest_priority_unknown"
      reason: "Discovered unknown needs exploration"
      priority: medium

  # Fallback
  - name: "Continue current work"
    condition:
      always: true
    recommend:
      action: continue
      reason: "No blockers, continue with current task"
      priority: low
```

### 5.2 Unknown Detector

```yaml
# meta-cognitive/unknown-detector.yaml

detection_rules:
  # Check for common oversights
  - name: "NFRs coverage"
    check: "Are all NFR categories addressed?"
    categories: [performance, security, scalability, reliability, usability]
    on_gap:
      add_unknown: "NFR category '{category}' not addressed"

  - name: "External dependencies"
    check: "Are all external dependencies identified?"
    sources: [apis, libraries, services, data_sources]
    on_gap:
      add_unknown: "External dependency may be missing"

  - name: "Edge cases"
    check: "Are error/edge cases considered?"
    for_each: [user_story, api_endpoint, data_flow]
    on_gap:
      add_unknown: "Edge cases for '{item}' not documented"

  - name: "Implicit assumptions"
    check: "Are there unstated assumptions?"
    prompt: |
      Review the current phase artifacts and identify assumptions
      that are NOT explicitly documented. For each:
      - What is assumed?
      - What if it's wrong?
      - Should it be verified?

  - name: "User didn't mention"
    check: "Common requirements user might forget"
    common_forgotten:
      - "Authentication/authorization"
      - "Error handling"
      - "Logging/monitoring"
      - "Backup/recovery"
      - "Email notifications"
      - "Rate limiting"
    on_missing:
      ask_user: "Did you consider {item}?"
```

### 5.3 Session Orchestrator

```yaml
# meta-cognitive/session-orchestrator.yaml

session_flow:
  on_start:
    - load: project-state.yaml
    - check: blocking_items
    - check: pending_tasks
    - run: planner
    - present: recommended_action

  on_operation_complete:
    - update: project-state.yaml
    - update: agent_working_memory
    - append: reasoning_trace
    - run: unknown_detector
    - check: gate_readiness
    - run: planner
    - present: next_recommended_action

  on_decision_made:
    - update: decision_record
    - update: project_graph
    - unblock: dependent_tasks
    - run: planner

  on_session_end:
    - save: all_working_memories
    - update: episodic_memory
    - generate: session_summary
    - present: state_overview
```

---

## Dashboard View — "Gdzie jesteśmy"

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  PROJECT: MyApp                                                    2026-02-01    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║  PHASE: ARCHITECTURE                              Progress: ████████░░░░ 67%     ║
║                                                                                    ║
║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║
║  │  IDEA ──────► SPEC ──────► ARCH ──────► IMPL ──────► TEST ──────► DONE     │  ║
║  │   ✓           ✓          ◉ HERE                                             │  ║
║  │  0.85        0.92         0.67                                              │  ║
║  └─────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                    ║
║  BLOCKING ITEMS:                                                                   ║
║  ├── 🔴 ADR-003: Database choice (2 tasks blocked)                               ║
║  └── 🟡 Q-007: Expected concurrent users? (asked 2h ago)                         ║
║                                                                                    ║
║  ACTIVE AGENTS:                                                                    ║
║  ├── agent-main: Designing API (task-003) - 60% done                             ║
║  └── agent-code-01: Waiting for ADR-003                                          ║
║                                                                                    ║
║  NEXT RECOMMENDED ACTION:                                                          ║
║  └── 📋 Resolve ADR-003 (Database choice)                                        ║
║       Reason: Blocking 2 tasks and 1 agent                                        ║
║       Suggested: Run deep-explore on database options                             ║
║                                                                                    ║
║  UNKNOWNS DISCOVERED: 3 (2 addressed, 1 to explore)                              ║
║  DECISIONS: 2 made, 2 pending                                                     ║
║  VERIFICATION GATES: 2/5 passed                                                   ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Implementation Roadmap

### Phase 1: Proof of Concept
- [ ] Define project-state.yaml schema
- [ ] Implement basic state tracking
- [ ] Create one cognitive operation (deep-challenge)
- [ ] Test on simple project: "idea → crystallized problem"

### Phase 2: Core Operations
- [ ] Implement deep-explore
- [ ] Implement deep-verify
- [ ] Implement deep-requirements
- [ ] Add verification gates

### Phase 3: Memory System
- [ ] Working memory per agent
- [ ] Episodic memory
- [ ] Task resumability

### Phase 4: Meta-Cognitive Layer
- [ ] Planner rules
- [ ] Unknown detector
- [ ] Session orchestrator

### Phase 5: Full Pipeline
- [ ] deep-architecture
- [ ] deep-develop
- [ ] End-to-end: idea → working code

---

## Open Questions

1. **File format:** YAML vs JSON vs custom?
2. **Agent coordination:** How do agents communicate?
3. **Conflict resolution:** What if two agents update same thing?
4. **Versioning:** How to version project-state.yaml?
5. **Recovery:** What if something goes wrong mid-session?

---

## References

- [CoALA Paper](https://arxiv.org/abs/2309.02427) — Cognitive Architectures for Language Agents
- [ADR Guide](https://adr.github.io/) — Architecture Decision Records
- [LangGraph](https://docs.langchain.com/oss/python/langgraph) — State management for agents
- [Knowledge Graph Code Gen](https://arxiv.org/html/2505.14394v1) — KG for code understanding
