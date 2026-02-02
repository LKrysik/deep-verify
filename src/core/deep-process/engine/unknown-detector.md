# Deep Process Engine — Unknown Detector

> **Purpose:** Actively discover "unknown unknowns" — things you don't know you don't know
> **When to run:** After each operation, at phase transitions, on user request
> **Philosophy:** Better to discover unknowns early than be surprised later

---

## 1. CORE CONCEPT

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        KNOWLEDGE QUADRANTS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│         KNOWN                           UNKNOWN                             │
│    ┌─────────────────┐            ┌─────────────────┐                      │
│    │                 │            │                 │                      │
│  K │  Known Knowns   │          K │ Known Unknowns  │                      │
│  N │  "We know this" │          N │ "We know we     │                      │
│  O │                 │          O │  don't know"    │                      │
│  W │  → Document it  │          W │  → Research it  │                      │
│  N │                 │          N │                 │                      │
│    └─────────────────┘            └─────────────────┘                      │
│                                                                             │
│    ┌─────────────────┐            ┌─────────────────┐                      │
│    │                 │            │                 │                      │
│  U │ Unknown Knowns  │          U │ Unknown Unknowns│                      │
│  N │ "We forgot we   │          N │ "We don't know  │  ← THIS IS THE       │
│  K │  know this"     │          K │  we don't know" │    DANGEROUS ONE     │
│  N │                 │          N │                 │                      │
│  O │ → Surface it    │          O │ → DETECT IT!    │                      │
│  W │                 │          W │                 │                      │
│  N └─────────────────┘          N └─────────────────┘                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. DETECTION RULES

### 2.1 Process-Agnostic Rules (apply to all processes)

```yaml
universal_checks:
  # ═══════════════════════════════════════════════════════════════
  # ASSUMPTION DETECTION
  # ═══════════════════════════════════════════════════════════════

  - name: "Implicit assumptions"
    trigger: "After each artifact creation"
    check: |
      Scan artifact for assumption patterns:
      - "users will..."
      - "obviously..."
      - "simple..."
      - "just..."
      - "everyone knows..."
      - "later..."
      - "probably..."
      - "should be..."
    on_match:
      action: create_unknown
      template: "Assumption detected: '{matched_phrase}' - is this validated?"
      priority: medium

  # ═══════════════════════════════════════════════════════════════
  # COMMON FORGOTTEN ITEMS
  # ═══════════════════════════════════════════════════════════════

  - name: "Authentication not mentioned"
    trigger: "After specification phase"
    check: "Search all artifacts for 'auth', 'login', 'password', 'permission'"
    if_not_found:
      action: ask_user
      question: "Does this system need authentication?"
      priority: high

  - name: "Error handling not mentioned"
    trigger: "After specification phase"
    check: "Search for 'error', 'fail', 'exception', 'invalid'"
    if_not_found:
      action: create_unknown
      template: "Error handling strategy not documented"
      priority: medium

  - name: "Logging not mentioned"
    trigger: "After architecture phase"
    check: "Search for 'log', 'monitor', 'trace', 'debug'"
    if_not_found:
      action: ask_user
      question: "Do you need logging/monitoring?"
      priority: medium

  - name: "Backup not mentioned"
    trigger: "After architecture phase"
    check: "Search for 'backup', 'recovery', 'disaster', 'restore'"
    if_not_found:
      action: create_unknown
      template: "Backup/recovery strategy not defined"
      priority: low

  - name: "Security not addressed"
    trigger: "After architecture phase"
    check: "Search for 'security', 'vulnerability', 'attack', 'OWASP'"
    if_not_found:
      action: create_unknown
      template: "Security considerations not documented"
      priority: high

  - name: "Performance not addressed"
    trigger: "After architecture phase"
    check: "Search for 'performance', 'latency', 'throughput', 'scale'"
    if_not_found:
      action: ask_user
      question: "Are there performance requirements?"
      priority: medium

  # ═══════════════════════════════════════════════════════════════
  # SCOPE DRIFT DETECTION
  # ═══════════════════════════════════════════════════════════════

  - name: "Scope creep"
    trigger: "When adding new requirement"
    check: "Is this requirement in original scope?"
    if_not:
      action: warn_user
      message: "This seems outside original scope. Intentional expansion?"
      priority: medium

  - name: "Missing out-of-scope"
    trigger: "After ideation phase"
    check: "Does idea.md have OUT OF SCOPE section?"
    if_not:
      action: create_unknown
      template: "Scope boundaries not defined - risk of scope creep"
      priority: high

  # ═══════════════════════════════════════════════════════════════
  # VALIDATION GAPS
  # ═══════════════════════════════════════════════════════════════

  - name: "User not validated"
    trigger: "After personas created"
    check: "Are personas based on actual research or assumptions?"
    prompt: "How do you know these personas are accurate?"
    priority: high

  - name: "Problem not validated"
    trigger: "After idea crystallized"
    check: "Is problem statement based on evidence or assumption?"
    prompt: "What evidence confirms this problem exists?"
    priority: high
```

### 2.2 Project Management Specific Rules

```yaml
pm_checks:
  - name: "Dependencies not mapped"
    trigger: "After stories created"
    check: "Do stories have dependencies defined?"
    if_not:
      action: create_unknown
      template: "Story dependencies not mapped - risk of blocked work"

  - name: "Acceptance criteria vague"
    trigger: "When story created"
    check: "Are acceptance criteria testable?"
    look_for: ["verify", "check", "ensure", "should"] # vague words
    if_found:
      action: warn_user
      message: "Acceptance criteria may not be testable"

  - name: "Sprint overcommitted"
    trigger: "After sprint planning"
    check: "committed_points <= capacity"
    if_not:
      action: create_unknown
      template: "Sprint may be overcommitted"
      priority: high

  - name: "No MVP defined"
    trigger: "After specification"
    check: "Search for 'MVP', 'minimum', 'phase 1'"
    if_not_found:
      action: ask_user
      question: "What is the absolute minimum for first release?"
```

### 2.3 UX Design Specific Rules

```yaml
ux_checks:
  - name: "Edge cases not considered"
    trigger: "After wireframes"
    check: "Are error states, empty states, loading states designed?"
    if_not:
      action: create_unknown
      template: "Edge case UI states not designed"

  - name: "Accessibility not addressed"
    trigger: "After prototype"
    check: "Search for 'accessibility', 'a11y', 'WCAG', 'screen reader'"
    if_not_found:
      action: create_unknown
      template: "Accessibility not considered"
      priority: medium

  - name: "Mobile not considered"
    trigger: "After wireframes"
    check: "Search for 'mobile', 'responsive', 'touch'"
    if_not_found:
      action: ask_user
      question: "Should this work on mobile devices?"
```

### 2.4 Documentation Specific Rules

```yaml
docs_checks:
  - name: "Audience not defined"
    trigger: "Before documenting"
    check: "Is documentation audience specified?"
    if_not:
      action: ask_user
      question: "Who is the documentation for? (developers, users, admins)"

  - name: "No examples"
    trigger: "After API docs"
    check: "Does each endpoint have at least 1 example?"
    if_not:
      action: create_unknown
      template: "API documentation lacks examples"
      priority: high

  - name: "Version not specified"
    trigger: "After documentation"
    check: "Is documentation versioned?"
    if_not:
      action: warn_user
      message: "Documentation should specify which version it applies to"
```

---

## 3. EXECUTION FLOW

### 3.1 When to Run

```yaml
triggers:
  - event: "operation_complete"
    run: universal_checks + process_specific_checks

  - event: "phase_transition"
    run: all_checks_for_previous_phase

  - event: "artifact_created"
    run: assumption_detection

  - event: "user_request"
    command: "check for unknowns"
    run: all_checks
```

### 3.2 How to Run

```markdown
## INSTRUKCJA: Detect Unknown Unknowns

1. IDENTIFY which checks apply:
   - Universal checks (always)
   - Process-specific checks (based on process_id)
   - Phase-specific checks (based on current_phase)

2. FOR EACH applicable check:
   a. Execute the check condition
   b. If triggered:
      - If action = create_unknown → Add to .state/unknowns.yaml
      - If action = ask_user → Present question
      - If action = warn_user → Display warning

3. REPORT findings:
   - List new unknowns discovered
   - List questions for user
   - List warnings

4. UPDATE state:
   - Append new unknowns to .state/unknowns.yaml
```

---

## 4. UNKNOWN LIFECYCLE

```
┌─────────────┐     User addresses     ┌────────────┐
│  DISCOVERED │ ───────────────────────▶│  ADDRESSED │
└─────────────┘                        └────────────┘
      │                                       │
      │ Assigned for                          │ Documented
      │ investigation                         │ where resolved
      ▼                                       │
┌─────────────┐                               │
│  EXPLORING  │ ◀─────────────────────────────┘
└─────────────┘
      │
      │ Cannot resolve /
      │ Accepted as risk
      ▼
┌───────────────┐
│ ACCEPTED_RISK │
└───────────────┘
```

### 4.1 Unknown Schema

```yaml
# Entry in .state/unknowns.yaml

- id: UNK-001
  description: "Offline sync strategy unclear"
  type: technical          # technical | user | market | feasibility | scope
  priority: high           # high | medium | low

  # Discovery
  discovered_at: 2026-02-01T12:00:00Z
  discovered_during: specification
  discovered_via: unknown-detector
  discovered_by_rule: "Common forgotten: offline"

  # Current status
  status: discovered       # discovered | exploring | addressed | accepted_risk

  # Resolution (when addressed)
  addressed_at: null
  addressed_in: null       # artifact path or decision ID
  resolution_notes: null

  # If accepted as risk
  risk_accepted_at: null
  risk_accepted_by: null
  risk_notes: null

  # Impact
  impact_if_unaddressed: "App may not work without internet"
  suggested_action: "Define offline-first architecture"
  blocks: []               # What this unknown might block
```

---

## 5. REPORTING

### 5.1 After Detection

```markdown
## Unknown Discovery Report

╔═══════════════════════════════════════════════════════════════════════════╗
║  ⚠ UNKNOWNS DISCOVERED                                                    ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  NEW UNKNOWNS: 3                                                          ║
║                                                                           ║
║  🔴 HIGH PRIORITY:                                                        ║
║  ├── UNK-005: Security considerations not documented                     ║
║  │   Impact: Potential vulnerabilities                                    ║
║  │   Action: Add security section to architecture                         ║
║  │                                                                        ║
║  🟡 MEDIUM PRIORITY:                                                      ║
║  ├── UNK-006: Logging strategy not defined                               ║
║  │   Impact: Difficult debugging in production                           ║
║  │   Action: Define logging approach                                      ║
║  │                                                                        ║
║  ├── UNK-007: Assumption detected: "users will understand"               ║
║  │   Impact: May not match reality                                        ║
║  │   Action: Validate with user testing                                   ║
║                                                                           ║
║  QUESTIONS FOR YOU:                                                       ║
║  └── Do you need rate limiting for the API?                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### 5.2 Summary View

```markdown
## Unknowns Summary

TOTAL: 12 discovered

BY STATUS:
├── Discovered: 5 (need attention)
├── Exploring: 2 (being investigated)
├── Addressed: 4 (resolved)
└── Accepted Risk: 1 (acknowledged)

BY PRIORITY:
├── 🔴 High: 3
├── 🟡 Medium: 5
└── 🟢 Low: 4

OLDEST UNADDRESSED:
└── UNK-002 (3 days ago): "Rate limiting not considered"
```

---

## 6. INTEGRATION WITH WORKFLOW

### 6.1 Blocking Behavior

```yaml
blocking_rules:
  - condition: "High priority unknown exists for 3+ days"
    action: WARN at session start
    message: "Unaddressed high-priority unknown: {description}"

  - condition: "Unknown blocks current work"
    action: BLOCK
    message: "Cannot proceed: {unknown.description} must be addressed"

  - condition: "5+ unaddressed unknowns"
    action: WARN
    message: "Many unaddressed unknowns - consider addressing before proceeding"
```

### 6.2 Gate Integration

```yaml
# Unknowns can affect gate scores

gate_impact:
  - gate: "*"  # All gates
    criterion: "No blocking unknowns"
    check: "No unknowns with blocks: [current_work]"
    weight: 0.10  # Add to gate criteria
```

---

## 7. USER COMMANDS

| User says | Action |
|-----------|--------|
| "Check for unknowns" | Run all applicable checks |
| "Show unknowns" | Display unknowns summary |
| "Address unknown UNK-001" | Mark as exploring, guide resolution |
| "Accept risk UNK-001" | Mark as accepted_risk with notes |
| "What am I missing?" | Run comprehensive unknown scan |
