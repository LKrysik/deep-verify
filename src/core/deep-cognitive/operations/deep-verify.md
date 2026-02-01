# Deep Verify V1.0 — Verification Gates

> **Purpose:** Verify phase completeness before transitioning
> **When to use:** Before moving to next phase, after significant work
> **Key output:** Verification score, gap list, pass/fail decision

---

## Operation Contract

```yaml
name: deep-verify
version: "1.0"

applicable_when:
  phases: [idea, specification, architecture, implementation, testing]
  conditions:
    - "phase_progress > 0.8"
    - "user requests verification"
    - "automatic gate check"

inputs:
  required:
    - name: target_gate
      type: string
      description: "Which gate to verify (e.g., idea_to_spec)"
  optional:
    - name: focus_areas
      type: list
      description: "Specific areas to focus on"

outputs:
  - name: verification_score
    type: number
    description: "0.0-1.0 score"

  - name: gaps
    type: list
    description: "List of identified gaps"

  - name: pass_fail
    type: boolean
    description: "Whether gate threshold is met"

state_effects:
  may_update: [verification_gates, current.phase, phases.{phase}]
  may_discover: [unknowns]
```

---

## GATE DEFINITIONS

### Gate 1: idea_to_spec

**Purpose:** Verify idea is clear enough to define requirements

```yaml
gate: idea_to_spec
threshold: 0.70

criteria:
  - name: "Problem clarity"
    weight: 0.25
    checks:
      - "Problem statement is one clear sentence"
      - "Pain point is specific and observable"
      - "Impact of inaction is stated"
    score_guide:
      1.0: "Crystal clear, no ambiguity"
      0.8: "Clear with minor gaps"
      0.5: "Partially clear"
      0.2: "Vague"

  - name: "User definition"
    weight: 0.20
    checks:
      - "Target user is specific (not 'everyone')"
      - "User characteristics described"
      - "Anti-user defined (who is NOT target)"
    score_guide:
      1.0: "Specific persona with validated needs"
      0.8: "Clear description, not validated"
      0.5: "General description"
      0.2: "Undefined or 'everyone'"

  - name: "Success criteria"
    weight: 0.20
    checks:
      - "At least 2 criteria exist"
      - "Criteria are measurable"
      - "Criteria are achievable"
    score_guide:
      1.0: "Clear, measurable, achievable"
      0.8: "Clear but not all measurable"
      0.5: "Vague criteria"
      0.2: "No criteria defined"

  - name: "Scope boundaries"
    weight: 0.20
    checks:
      - "IN scope list exists"
      - "OUT scope list exists"
      - "MVP/minimum defined"
    score_guide:
      1.0: "Clear IN/OUT with MVP"
      0.8: "IN defined, OUT vague"
      0.5: "Partial boundaries"
      0.2: "No boundaries"

  - name: "Unknowns addressed"
    weight: 0.15
    checks:
      - "Critical unknowns identified"
      - "No blocking unknowns remain"
    score_guide:
      1.0: "All unknowns identified and addressed"
      0.8: "Identified, resolution planned"
      0.5: "Partially identified"
      0.2: "Not considered"
```

### Gate 2: spec_to_arch

**Purpose:** Verify specification is complete for architecture

```yaml
gate: spec_to_arch
threshold: 0.85

criteria:
  - name: "Requirements completeness"
    weight: 0.25
    checks:
      - "All functional requirements have acceptance criteria"
      - "Requirements are testable"
      - "No duplicate requirements"
    score_guide:
      1.0: "All complete with clear AC"
      0.8: "Most have AC"
      0.5: "Some missing AC"
      0.2: "Many incomplete"

  - name: "NFR coverage"
    weight: 0.20
    checks:
      - "Performance requirements defined"
      - "Security requirements defined"
      - "Scalability considered"
    score_guide:
      1.0: "All NFR categories covered"
      0.8: "Most covered"
      0.5: "Some covered"
      0.2: "NFRs missing"

  - name: "Consistency"
    weight: 0.20
    checks:
      - "No conflicting requirements"
      - "Terminology consistent"
      - "Priorities don't conflict"
    score_guide:
      1.0: "Fully consistent"
      0.8: "Minor inconsistencies"
      0.5: "Some conflicts"
      0.2: "Major conflicts"

  - name: "Dependencies"
    weight: 0.15
    checks:
      - "External dependencies identified"
      - "Internal dependencies mapped"
    score_guide:
      1.0: "All dependencies mapped"
      0.8: "Most identified"
      0.5: "Partially identified"
      0.2: "Not considered"

  - name: "Risks documented"
    weight: 0.10
    checks:
      - "Major risks identified"
      - "Mitigation strategies exist"
    score_guide:
      1.0: "Risks with mitigations"
      0.8: "Risks identified"
      0.5: "Some risks noted"
      0.2: "No risk consideration"

  - name: "Priorities"
    weight: 0.10
    checks:
      - "Requirements prioritized"
      - "MVP scope clear"
    score_guide:
      1.0: "Clear prioritization"
      0.8: "Most prioritized"
      0.5: "Partial"
      0.2: "No prioritization"
```

### Gate 3: arch_to_impl

**Purpose:** Verify architecture is sound for implementation

```yaml
gate: arch_to_impl
threshold: 0.80

criteria:
  - name: "Requirements coverage"
    weight: 0.25
    checks:
      - "All requirements have architectural home"
      - "Traceability exists"
    score_guide:
      1.0: "Full traceability"
      0.8: "Most requirements mapped"
      0.5: "Partial mapping"
      0.2: "No mapping"

  - name: "Decisions resolved"
    weight: 0.25
    checks:
      - "No blocking decisions pending"
      - "All ADRs accepted or rejected"
    score_guide:
      1.0: "All decisions made"
      0.8: "Minor decisions pending"
      0.5: "Some blocking decisions"
      0.0: "Critical decisions pending"

  - name: "Interfaces defined"
    weight: 0.20
    checks:
      - "Component interfaces documented"
      - "API contracts exist"
      - "Data contracts exist"
    score_guide:
      1.0: "All interfaces documented"
      0.8: "Most documented"
      0.5: "Partial"
      0.2: "Missing interfaces"

  - name: "Data model complete"
    weight: 0.15
    checks:
      - "Entities defined"
      - "Relationships mapped"
      - "Data flows documented"
    score_guide:
      1.0: "Complete data model"
      0.8: "Core entities defined"
      0.5: "Partial model"
      0.2: "No data model"

  - name: "Deployment defined"
    weight: 0.15
    checks:
      - "Deployment strategy documented"
      - "Environments defined"
    score_guide:
      1.0: "Complete deployment plan"
      0.8: "Strategy defined"
      0.5: "Partial"
      0.2: "Not considered"
```

---

## EXECUTION FLOW

### Step 1: Identify Target Gate

```yaml
input: target_gate OR infer from current.phase
output: gate_definition with criteria and threshold
```

### Step 2: Gather Evidence

For each criterion:
1. Load relevant artifacts
2. Check each item in `checks` list
3. Score based on `score_guide`

```yaml
evidence:
  - criterion: "Problem clarity"
    artifact: "docs/idea.md"
    section: "Problem Statement"
    checks_passed: [true, true, false]
    score: 0.8
    notes: "Impact of inaction not explicitly stated"
```

### Step 3: Calculate Score

```
total_score = sum(criterion.score * criterion.weight)
```

### Step 4: Identify Gaps

For each criterion with score < 1.0:
```yaml
gap:
  criterion: "Problem clarity"
  current_score: 0.8
  missing: "Impact of inaction not stated"
  remediation: "Add 'If unsolved...' section to idea.md"
  priority: medium
```

### Step 5: Determine Pass/Fail

```yaml
result:
  gate: "idea_to_spec"
  score: 0.78
  threshold: 0.70
  passed: true

  summary:
    - criterion: "Problem clarity"
      score: 0.8
      status: "PASS"
    - criterion: "User definition"
      score: 0.9
      status: "PASS"
    # ... etc
```

### Step 6: Update State

```yaml
# If passed:
verification_gates:
  - gate: idea_to_spec
    status: passed
    score: 0.78
    passed_at: 2026-02-01T14:00:00Z

current:
  phase: specification  # Advanced!

phases:
  idea:
    status: completed
    verification_score: 0.78

# If failed:
verification_gates:
  - gate: idea_to_spec
    status: failed
    score: 0.58

current:
  blocking_items:
    - type: gate_failure
      gate: idea_to_spec
      gaps: [list of gaps]
```

### Step 7: Present Result

**If Passed:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║  ✓ GATE PASSED: idea_to_spec                                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  Score: 0.78 (threshold: 0.70)                                           ║
║                                                                           ║
║  CRITERIA BREAKDOWN:                                                      ║
║  ├── Problem clarity:     ████████░░  0.80                               ║
║  ├── User definition:     █████████░  0.90                               ║
║  ├── Success criteria:    ███████░░░  0.70                               ║
║  ├── Scope boundaries:    ████████░░  0.80                               ║
║  └── Unknowns addressed:  ██████░░░░  0.60                               ║
║                                                                           ║
║  ADVANCING TO: specification                                              ║
║                                                                           ║
║  RECOMMENDED NEXT: deep-requirements                                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**If Failed:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║  ✗ GATE FAILED: idea_to_spec                                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  Score: 0.58 (threshold: 0.70)                                           ║
║                                                                           ║
║  GAPS IDENTIFIED:                                                         ║
║  ├── User definition (0.40):                                              ║
║  │   • Target user too vague ("busy professionals")                      ║
║  │   • No anti-user defined                                              ║
║  │   → Action: Run deep-challenge focused on user                        ║
║  │                                                                        ║
║  └── Success criteria (0.50):                                            ║
║      • Criteria not measurable                                            ║
║      → Action: Define specific metrics                                    ║
║                                                                           ║
║  RECOMMENDED: deep-challenge with focus on [User definition]              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Integration Points

**Reads from:**
- Project artifacts (docs/idea.md, docs/prd.md, etc.)
- project-state.yaml
- Previous verification results

**Updates:**
- verification_gates in project-state.yaml
- current.phase (if passed)
- phases.{phase}.status
- current.blocking_items (if failed)

**Triggers:**
- Phase transition (if passed)
- Planner re-evaluation
- Unknown detector (during checks)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial PoC with 3 gates |
