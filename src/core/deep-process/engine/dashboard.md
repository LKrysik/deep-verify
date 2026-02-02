# Deep Process Engine — Dashboard

> **Purpose:** Visual representation of project state
> **When to show:** Session start, after operations, on user request
> **Principle:** User should always know where they are

---

## 1. MAIN DASHBOARD

### 1.1 Full Dashboard Template

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PROJECT: {project.name}                                      {current_date}  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  PROCESS: {process_id} v{version}                                             ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────────┐  ║
║  │  PHASE PROGRESS                                                          │  ║
║  │                                                                          │  ║
║  │  {phase_1}    {phase_2}    {phase_3}    {phase_4}    {phase_5}          │  ║
║  │     {s1}         {s2}         {s3}         {s4}         {s5}            │  ║
║  │                                                                          │  ║
║  │  Legend: ✓ = done, ◉ = current, ○ = future, ✗ = blocked                 │  ║
║  └─────────────────────────────────────────────────────────────────────────┘  ║
║                                                                               ║
║  CURRENT PHASE: {current_phase}                                               ║
║  PROGRESS: {progress_bar} {progress_percent}%                                 ║
║                                                                               ║
║  ─────────────────────────────────────────────────────────────────────────────║
║                                                                               ║
║  BLOCKERS: {blocker_count}                                                    ║
║  {blocker_list}                                                               ║
║                                                                               ║
║  ─────────────────────────────────────────────────────────────────────────────║
║                                                                               ║
║  STATS:                                                                       ║
║  ├── Decisions: {decisions_made} made, {decisions_pending} pending            ║
║  ├── Unknowns: {unknowns_total} ({unknowns_unaddressed} unaddressed)         ║
║  ├── Gates: {gates_passed}/{gates_total} passed                               ║
║  └── Items: {epics_count} epics, {stories_count} stories                      ║
║                                                                               ║
║  ─────────────────────────────────────────────────────────────────────────────║
║                                                                               ║
║  RECOMMENDED ACTION:                                                          ║
║  └── {recommendation}                                                         ║
║      Reason: {recommendation_reason}                                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### 1.2 Generating Dashboard

```markdown
## INSTRUKCJA: Generate Dashboard

1. LOAD state:
   - .state/process.yaml
   - .state/phase.yaml
   - .state/items.yaml
   - .state/decisions.yaml
   - .state/unknowns.yaml

2. CALCULATE values:
   - progress_percent = phase.phase_progress * 100
   - progress_bar = generate_bar(phase_progress)
   - blocker_count = len(phase.blocking_items)
   - decisions_made = count decisions with status: accepted
   - decisions_pending = count decisions with status: pending
   - unknowns_total = len(unknowns.unknowns)
   - unknowns_unaddressed = count with status: discovered | exploring
   - gates_passed = count gates with status: passed
   - gates_total = len(process.phases) - 1

3. DETERMINE phase indicators:
   For each phase in process.phases:
   - If phase.status == completed: "✓"
   - If phase == current_phase: "◉"
   - If phase blocked: "✗"
   - Else: "○"

4. GET recommendation:
   - Apply planner rules
   - Get highest priority recommendation

5. FORMAT and display
```

### 1.3 Progress Bar Generator

```markdown
## Progress Bar

10 segments, filled based on percentage:

0%   = ░░░░░░░░░░
10%  = █░░░░░░░░░
20%  = ██░░░░░░░░
30%  = ███░░░░░░░
40%  = ████░░░░░░
50%  = █████░░░░░
60%  = ██████░░░░
70%  = ███████░░░
80%  = ████████░░
90%  = █████████░
100% = ██████████
```

---

## 2. COMPACT DASHBOARD

For quick status checks:

```
╔═════════════════════════════════════════════════════════╗
║  {project.name} | {current_phase} | {progress}%         ║
║  Blockers: {n} | Unknowns: {n} | Next: {action}         ║
╚═════════════════════════════════════════════════════════╝
```

---

## 3. PHASE DETAIL VIEW

When user wants details about current phase:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PHASE: {phase_name}                                                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Status: {status}                                                             ║
║  Started: {started_at}                                                        ║
║  Progress: {progress_bar} {percent}%                                          ║
║                                                                               ║
║  STEPS:                                                                       ║
║  ├── [✓] {step_1_name}                                                       ║
║  ├── [✓] {step_2_name}                                                       ║
║  ├── [◉] {step_3_name} ← CURRENT                                             ║
║  ├── [ ] {step_4_name}                                                       ║
║  └── [ ] {step_5_name}                                                       ║
║                                                                               ║
║  ARTIFACTS CREATED:                                                           ║
║  ├── {artifact_1_path}                                                       ║
║  └── {artifact_2_path}                                                       ║
║                                                                               ║
║  NEXT GATE: {gate_name}                                                       ║
║  Threshold: {threshold}                                                       ║
║  Current readiness: {readiness}                                               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 4. BLOCKERS VIEW

When blockers exist:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  ⛔ BLOCKERS                                                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🔴 DECISIONS NEEDED:                                                         ║
║  ├── DEC-003: Database choice                                                ║
║  │   Options: PostgreSQL, MongoDB, SQLite                                    ║
║  │   Blocks: STORY-004, STORY-006                                            ║
║  │   Needed by: 2026-02-02                                                   ║
║  │                                                                            ║
║  └── DEC-005: Auth provider                                                  ║
║      Options: Auth0, Firebase, Custom                                        ║
║      Blocks: EPIC-002                                                        ║
║                                                                               ║
║  🟡 QUESTIONS PENDING:                                                        ║
║  └── Q-001: Expected concurrent users?                                       ║
║      Asked: 2 hours ago                                                      ║
║      Blocks: NFR-003 sizing                                                  ║
║                                                                               ║
║  🟠 GATE FAILURES:                                                            ║
║  └── spec_to_arch: Score 0.72, needed 0.85                                   ║
║      Missing: NFR coverage, risk documentation                               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 5. ITEMS VIEW

For project management process:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  WORK ITEMS                                                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  EPICS:                                                                       ║
║  ├── EPIC-001: User Authentication                [████████░░] 80%           ║
║  │   └── 4 stories (3 done, 1 in progress)                                   ║
║  ├── EPIC-002: Habit Tracking                     [████░░░░░░] 40%           ║
║  │   └── 5 stories (2 done, 1 blocked, 2 pending)                            ║
║  └── EPIC-003: Analytics                          [░░░░░░░░░░] 0%            ║
║      └── 3 stories (0 done, 3 pending)                                       ║
║                                                                               ║
║  CURRENT SPRINT: Sprint 1 - Foundation                                       ║
║  ├── Goal: Basic auth working                                                ║
║  ├── Progress: 8/20 points (40%)                                             ║
║  ├── Days remaining: 5                                                       ║
║  └── Stories:                                                                ║
║      ├── [✓] STORY-001: User registration (3pts)                            ║
║      ├── [✓] STORY-002: User login (5pts)                                   ║
║      ├── [◉] STORY-003: Password reset (5pts) ← IN PROGRESS                 ║
║      └── [ ] STORY-004: Session management (7pts) ← BLOCKED by DEC-003      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 6. UNKNOWNS VIEW

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  UNKNOWNS                                                                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  SUMMARY: 8 total (4 need attention)                                         ║
║                                                                               ║
║  🔴 HIGH PRIORITY (unaddressed):                                              ║
║  ├── UNK-003: Security model not defined                                     ║
║  │   Discovered: 2 days ago                                                  ║
║  │   Action: Add security section to architecture                            ║
║  │                                                                            ║
║  └── UNK-005: Rate limiting not considered                                   ║
║      Discovered: 1 day ago                                                   ║
║      Action: Define API rate limits                                          ║
║                                                                               ║
║  🟡 MEDIUM PRIORITY (unaddressed):                                            ║
║  ├── UNK-007: Logging strategy undefined                                     ║
║  └── UNK-008: Backup frequency not specified                                 ║
║                                                                               ║
║  ✓ RECENTLY ADDRESSED:                                                        ║
║  ├── UNK-001: Offline sync → Addressed in architecture.md                    ║
║  └── UNK-002: Auth method → Addressed in ADR-001                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 7. HISTORY VIEW

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  RECENT ACTIVITY                                                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  TODAY:                                                                       ║
║  ├── 15:30  Created STORY-007 "Notifications"                                ║
║  ├── 14:45  Gate passed: arch_to_planning (0.82)                             ║
║  ├── 14:00  Decision made: DEC-002 → PostgreSQL                              ║
║  └── 10:00  Session started                                                  ║
║                                                                               ║
║  YESTERDAY:                                                                   ║
║  ├── 16:00  Created architecture.md                                          ║
║  ├── 14:30  Discovered UNK-003: Security model                               ║
║  └── 10:30  Gate passed: spec_to_arch (0.88)                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 8. COMMANDS

| User says | Dashboard shown |
|-----------|-----------------|
| "Show status" | Main dashboard |
| "Show phase" | Phase detail view |
| "Show blockers" | Blockers view |
| "Show items" | Items view |
| "Show unknowns" | Unknowns view |
| "Show history" | History view |
| "What's blocking?" | Blockers view |
| "Where are we?" | Main dashboard |

---

## 9. IMPLEMENTATION

```markdown
## INSTRUKCJA: Display Dashboard

1. User requests status (or session starts)

2. Load all state files:
   ```
   process = read(.state/process.yaml)
   phase = read(.state/phase.yaml)
   items = read(.state/items.yaml)
   decisions = read(.state/decisions.yaml)
   unknowns = read(.state/unknowns.yaml)
   ```

3. Calculate all metrics

4. Select appropriate dashboard:
   - Full for session start or "show status"
   - Compact for quick checks
   - Specific views for specific requests

5. Format using templates above

6. Display to user
```
