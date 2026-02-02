# Step 06: Output

## Purpose

Deliver complete exploration report.

**Time:** 5-10 min

**Inputs:** All outputs from Steps 0-5

**Outputs:** EXPLORATION REPORT

---

## Procedure

### 06.1 Load Report Template

📂 Load template: `data/exploration-report-template.md`

### 06.2 Fill Report Sections

```
SECTION 1: WHAT WE LEARNED
□ Key discoveries (from Step 1)
□ Surprises
□ Changed assumptions

SECTION 2: WHAT WE STILL DON'T KNOW
□ Critical unknowns (flagged in Step 1)
□ True uncertainties (from Step 4)
□ Parked questions
□ Flagged for expert

SECTION 3: OPTION MAP
□ Dimensions and options (from Step 2)
□ Constraints
□ Valid combinations

SECTION 4: STRATEGIC CLUSTERS
□ Clusters (from Step 5)
□ Best-for scenarios
□ Trade-offs

SECTION 5: CONSEQUENCE MAP
□ Consequences per cluster (from Step 3)
□ Mark VERIFIED vs ASSUMED
□ Risks

SECTION 6: DECISION READINESS
□ Sequence (from Step 5)
□ Readiness per decision
□ What would help

SECTION 7: SUGGESTED NEXT STEPS
□ If want more clarity
□ If ready to decide
□ If want to explore deeper

SECTION 8: FEAR RESOLUTION (when fear_analysis=on)
□ Original fears (from Step 0)
□ Resolution status (RESOLVED/ADDRESSED/REMAINS)
□ Minimal tests designed (from Step 4)
□ Growth assessment
□ What user controls vs accepts
□ False walls cleared
□ True walls confirmed
```

### 06.3 Calculate Coverage Score

📂 Load: `data/coverage-scoring.yaml`

```
COVERAGE CALCULATION (V2.1.1 - Quality over Quantity):

DISCOVERY (with caps to prevent gaming):
Dimensions discovered:     min([N], 8) × 1.5 = [score]
Options enumerated:        min([N], 20) × 0.5 = [score]

VERIFICATION (high value):
Consequences VERIFIED:     [N] × 2.0 = [score]
Consequences ASSUMED:      [N] × 0.2 = [score]
Assumptions tested:        [N] × 1.5 = [score]
Assumptions falsified:     [N] × 2.0 = [score]

ANALYSIS:
Unknown unknowns surfaced: [N] × 1.5 = [score]
Boundaries identified:     [N] × 1.0 = [score]
Causal relationships:      [N] × 1.0 = [score]

CHALLENGE:
Premortem causes:          [N] × 0.5 = [score]
Black swans identified:    [N] × 0.5 = [score]
Biases checked:            [N] × 0.3 = [score]
Beliefs stress tested:     [N] × 0.5 = [score]

IF fear_analysis=on:
Fears classified:          [N] × 0.5 = [score]
False walls identified:    [N] × 1.5 = [score]
True walls confirmed:      [N] × 1.5 = [score]
Controllable concerns:     [N] × 0.5 = [score]
Success paths discovered:  [N] × 2.0 = [score]
Comparables analyzed:      [N] × 0.5 = [score]

RAW SCORE: [sum]
```

```
QUALITY GATE CHECK (must pass to achieve level):

┌────────────────────────────┬────────┬──────────┬────────┐
│ Requirement                │ Quick  │ Standard │ Deep   │
├────────────────────────────┼────────┼──────────┼────────┤
│ Dimensions (min)           │ 3      │ 4        │ 5      │
│ Options (min)              │ 6      │ 12       │ 15     │
│ Verified consequences (min)│ 2      │ 5        │ 10     │
│ Assumptions tested (min)   │ 1      │ 3        │ 5      │
│ Verification ratio (min)   │ -      │ 30%      │ 50%    │
│ Premortem causes (min)     │ -      │ 3        │ 5      │
│ Biases checked (min)       │ -      │ -        │ 5      │
└────────────────────────────┴────────┴──────────┴────────┘

VERIFICATION RATIO = verified / (verified + assumed) × 100%
Your ratio: [N]% — Required: [M]% — [✓ PASS / ✗ FAIL]

QUALITY GATE: [PASSED / FAILED - reason]
```

```
THRESHOLDS (by depth):

Quick:    C ≥ 15 COMPREHENSIVE | C ≥ 10 ADEQUATE | C ≥ 5 PARTIAL
Standard: C ≥ 35 COMPREHENSIVE | C ≥ 22 ADEQUATE | C ≥ 12 PARTIAL
Deep:     C ≥ 50 COMPREHENSIVE | C ≥ 35 ADEQUATE | C ≥ 20 PARTIAL

NOTE: Quality gate failure caps level regardless of score.
```

---

## Final Output

📂 Generate report using: `data/exploration-report-template.md`

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP EXPLORE REPORT                                   ║
║                      Version 2.0                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  DECISION: [from Step 0]                                                   ║
║  DATE: [today]                                                             ║
║  CONFIG: depth=[quick|standard|deep] fear_analysis=[on|off]                ║
║  TIME: [total]                                                             ║
║  COVERAGE: [score] - [level]                                               ║
║                                                                            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  [SECTION 1-7 content]                                                     ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Exploration Complete

The report is the final deliverable.

User now has:
- Understanding of what they learned
- Clarity on what they don't know
- Map of options with consequences
- Assessment of decision readiness
- Guidance on next steps

**When fear_analysis=on, user also has:**
- Resolution status for each original fear
- Minimal tests designed to learn (failure = data)
- Clear separation of controllable vs uncontrollable
- False walls cleared (proceed with confidence)
- True walls confirmed (save wasted effort)
- Growth assessment for each option
