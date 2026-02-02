# Deep Cognitive V0.1 — Cognitive Architecture for LLM Development

> **Purpose:** Transform vision → working code with full verification and state tracking
> **Philosophy:** "I don't know what I don't know" — active discovery of unknown unknowns
> **Architecture:** 5-layer cognitive system with per-agent working memory

---

## INVOCATION

When user invokes deep-cognitive (or starts a new project):

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           DEEP COGNITIVE                                       ║
║                           Version 0.1 (PoC)                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  Welcome to Deep Cognitive — your AI development partner.                      ║
║                                                                                ║
║  This system will help you:                                                    ║
║  • Transform vague ideas into crystal-clear specifications                     ║
║  • Discover what you don't know you don't know                                 ║
║  • Track progress automatically — never wonder "where are we"                  ║
║  • Verify at every step — ensure quality before proceeding                     ║
║  • Coordinate multiple agents — concurrent work with shared memory             ║
║                                                                                ║
║  THE PIPELINE:                                                                 ║
║  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐ ║
║  │  IDEA  │ → │  SPEC  │ → │  ARCH  │ → │  IMPL  │ → │  TEST  │ → │  DONE  │ ║
║  │        │   │        │   │        │   │        │   │        │   │        │ ║
║  │ ≥0.70  │   │ ≥0.85  │   │ ≥0.80  │   │ ≥0.90  │   │ ≥0.85  │   │  ✓     │ ║
║  └────────┘   └────────┘   └────────┘   └────────┘   └────────┘   └────────┘ ║
║       ↑            ↑            ↑            ↑            ↑                   ║
║   deep-       deep-        deep-        deep-        deep-                    ║
║   challenge   requirements architecture develop      verify                   ║
║                                                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## INITIALIZATION

### First Time Setup

If `.deep/project-state.yaml` does not exist:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PROJECT INITIALIZATION                                                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  Let's set up your project for Deep Cognitive tracking.                        ║
║                                                                                ║
║  1. What is the project name?                                                  ║
║  2. Brief description (1-2 sentences)?                                         ║
║                                                                                ║
║  (Or share your idea and I'll extract these for you)                          ║
║                                                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Actions:**
1. Create `.deep/` directory structure
2. Initialize `project-state.yaml` with project info
3. Create initial agent (`agent-main`)
4. Start session trace
5. Run planner to get first recommendation

---

## SESSION START

### Load State

```yaml
load:
  - .deep/project-state.yaml
  - .deep/agents/agent-main.yaml (if exists)
  - .deep/traces/{latest} (for context)
```

### Present Dashboard

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PROJECT: {name}                                              {date}          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  PHASE: {current_phase}                        Progress: {progress_bar} {%}  ║
║                                                                                ║
║  ┌─────────────────────────────────────────────────────────────────────────┐  ║
║  │  IDEA ──► SPEC ──► ARCH ──► IMPL ──► TEST ──► DONE                     │  ║
║  │  {indicator for each phase: ✓ done, ◉ current, ○ future}               │  ║
║  └─────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                ║
║  {IF blocking_items}                                                           ║
║  BLOCKING:                                                                     ║
║  {list of blocking items}                                                      ║
║  {ENDIF}                                                                       ║
║                                                                                ║
║  UNKNOWNS: {discovered_count} discovered, {addressed_count} addressed         ║
║  DECISIONS: {made_count} made, {pending_count} pending                         ║
║  GATES: {passed_count}/{total_gates} passed                                    ║
║                                                                                ║
║  ─────────────────────────────────────────────────────────────────────────────║
║  RECOMMENDED ACTION: {planner_recommendation}                                  ║
║  Reason: {recommendation_reason}                                               ║
║                                                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## AVAILABLE OPERATIONS

### Core Operations

| Command | Operation | Purpose |
|---------|-----------|---------|
| `/deep-challenge` | deep-challenge | Crystallize vague ideas |
| `/deep-explore` | deep-explore | Discover option space |
| `/deep-verify` | deep-verify | Verify gate readiness |
| `/deep-requirements` | deep-requirements | Define specifications |
| `/deep-architecture` | deep-architecture | Design system |
| `/deep-develop` | deep-develop | Write code |
| `/deep-status` | (built-in) | Show current dashboard |

### Meta Commands

| Command | Purpose |
|---------|---------|
| `/deep-status` | Show current project state |
| `/deep-unknowns` | List all discovered unknowns |
| `/deep-decisions` | List all decisions (made + pending) |
| `/deep-trace` | Show current session trace |

---

## OPERATION FLOW

### Standard Operation Execution

```
1. USER invokes operation (e.g., /deep-challenge)

2. SYSTEM:
   a. Load current project state
   b. Load operation workflow (.../operations/{op}.md)
   c. Load agent working memory
   d. Start trace entry

3. OPERATION executes:
   - Follows workflow steps
   - Updates working memory
   - Discovers unknowns
   - Creates/updates artifacts

4. ON COMPLETION:
   a. Update project-state.yaml
   b. Save agent working memory
   c. Finalize trace entry
   d. Run unknown detector
   e. Check gate readiness
   f. Get planner recommendation
   g. Present result + recommendation
```

---

## FILE LOCATIONS

```
project-root/
├── .deep/                              # Deep Cognitive system
│   ├── project-state.yaml              # Single source of truth
│   ├── tasks/                          # Task queue
│   │   └── task-{id}.yaml
│   ├── agents/                         # Agent working memory
│   │   └── agent-{id}.yaml
│   ├── memory/
│   │   ├── episodic.yaml               # What we did
│   │   ├── semantic.yaml               # Domain knowledge
│   │   └── graph.yaml                  # Knowledge graph
│   └── traces/                         # Reasoning traces
│       └── {date}-session-{n}.yaml
│
├── docs/
│   ├── idea.md                         # Phase: IDEA output
│   ├── prd.md                          # Phase: SPEC output
│   ├── architecture.md                 # Phase: ARCH output
│   └── decisions/                      # ADRs
│       └── ADR-{id}.yaml
│
├── src/                                # Phase: IMPL output
└── tests/                              # Phase: TEST output
```

---

## PHASE TRANSITIONS

### Gate Check Flow

```
1. User requests gate check OR phase_progress > 0.85

2. Run deep-verify for current gate
   - Load gate criteria
   - Check each criterion
   - Calculate score

3. IF score >= threshold:
   - Mark gate as passed
   - Advance phase
   - Update project-state.yaml
   - Celebrate!

4. IF score < threshold:
   - List gaps
   - Add to blocking_items
   - Recommend remediation operation
   - Stay in current phase
```

---

## UNKNOWN DISCOVERY

### Automatic Detection

After each operation, the unknown detector runs:

1. **Phase-specific checks** - Are expected items covered?
2. **Common forgotten items** - Did user forget auth, logging, etc.?
3. **Assumption detection** - Are there hidden assumptions?

### Unknown Lifecycle

```
discovered → exploring → addressed | accepted_risk
```

Each unknown is tracked with:
- ID, description, type
- Discovery context (when, where, how)
- Priority and impact
- Suggested resolution action
- Current status

---

## MULTI-AGENT SUPPORT (Future)

### Working Memory Isolation

```
┌───────────────────┐   ┌───────────────────┐
│   AGENT-MAIN      │   │   AGENT-CODE-01   │
│                   │   │                   │
│ Working Memory:   │   │ Working Memory:   │
│ - Task: task-003  │   │ - Task: task-005  │
│ - Focus: API      │   │ - Focus: Auth     │
│ - Context: ...    │   │ - Context: ...    │
└─────────┬─────────┘   └─────────┬─────────┘
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │   SHARED STATE        │
          │   (project-state.yaml)│
          │                       │
          │   - Phase             │
          │   - Task queue        │
          │   - Decisions         │
          │   - Unknowns          │
          └───────────────────────┘
```

**Rules:**
- Working memory is ISOLATED per agent/task
- Agents COMMIT to shared state when task completes
- Working memory can be SNAPSHOTTED for resumability
- Context is LOADED from shared state at task start

---

## EXAMPLE SESSION

```
User: Chcę zbudować aplikację do zarządzania finansami osobistymi

System: [Initializes project]

╔═══════════════════════════════════════════════════════════════════════════════╗
║  PROJECT: Personal Finance App                               2026-02-01       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  PHASE: IDEA                                   Progress: ░░░░░░░░░░ 0%        ║
║  RECOMMENDED: deep-challenge                                                   ║
║  Reason: Idea needs crystallization                                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝

System: [Runs deep-challenge]
- Asks probing questions
- Discovers unknowns
- Crystallizes idea

╔═══════════════════════════════════════════════════════════════════════════════╗
║  ✓ IDEA CRYSTALLIZED                                                          ║
║  Clarity Score: 0.82 (threshold: 0.70)                                        ║
║  Unknowns discovered: 3                                                        ║
║                                                                                ║
║  Created: docs/idea.md                                                         ║
║                                                                                ║
║  RECOMMENDED: deep-verify (gate: idea_to_spec)                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

User: /deep-verify

System: [Runs verification]

╔═══════════════════════════════════════════════════════════════════════════════╗
║  ✓ GATE PASSED: idea_to_spec                                                  ║
║  Score: 0.82 (threshold: 0.70)                                                ║
║                                                                                ║
║  ADVANCING TO: SPECIFICATION                                                   ║
║                                                                                ║
║  RECOMMENDED: deep-requirements                                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

[...continues through phases...]
```

---

## CONFIGURATION

### Project-level settings

```yaml
# .deep/config.yaml (optional)

settings:
  # Gate thresholds (can override defaults)
  gates:
    idea_to_spec: 0.70
    spec_to_arch: 0.85
    arch_to_impl: 0.80

  # Unknown detector
  unknown_detector:
    auto_run: true
    check_forgotten_items: true

  # Trace verbosity
  traces:
    detail_level: full  # full | summary | minimal
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-02-01 | Initial PoC: deep-challenge, deep-verify, basic state |

---

## ARCHITECTURE REFERENCE

See: `docs/deep/architecture.md` for full 5-layer architecture design.

---

## NEXT STEPS (Roadmap)

### Phase 1: PoC (Current)
- [x] project-state.yaml schema
- [x] deep-challenge operation
- [x] deep-verify operation
- [x] Planner rules
- [x] Unknown detector
- [x] Session orchestrator
- [ ] Test on real project

### Phase 2: Core Operations
- [ ] deep-requirements
- [ ] deep-explore integration
- [ ] deep-risk

### Phase 3: Memory System
- [ ] Episodic memory
- [ ] Knowledge graph
- [ ] Task resumability

### Phase 4: Meta-Cognitive
- [ ] Full planner implementation
- [ ] Active unknown detection
- [ ] Session management

### Phase 5: Full Pipeline
- [ ] deep-architecture
- [ ] deep-develop
- [ ] End-to-end flow
