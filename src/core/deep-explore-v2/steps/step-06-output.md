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

SECTION 8: FEAR RESOLUTION (if Fear-Based Mode)
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
COVERAGE CALCULATION:

Dimensions discovered:     [N] × 2 = [score]
Options enumerated:        [N] × 1 = [score]
Consequences VERIFIED:     [N] × 1 = [score]
Consequences ASSUMED:      [N] × 0.3 = [score]
Unknown unknowns surfaced: [N] × 1.5 = [score]
Assumptions falsified:     [N] × 1 = [score]
Boundaries identified:     [N] × 0.5 = [score]
Causal relationships:      [N] × 0.5 = [score]

IF FEAR-BASED MODE:
Fears classified:          [N] × 0.5 = [score]
False walls identified:    [N] × 1 = [score]
True walls confirmed:      [N] × 1 = [score]
Controllable concerns:     [N] × 0.5 = [score]
Success paths discovered:  [N] × 1.5 = [score]
Comparables analyzed:      [N] × 0.5 = [score]

TOTAL COVERAGE SCORE: [sum]

INTERPRETATION:
C ≥ 25: COMPREHENSIVE
15 ≤ C < 25: ADEQUATE
8 ≤ C < 15: PARTIAL
C < 8: INSUFFICIENT
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
║  MODE: [QE/SE/DE/FE]                                                       ║
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

**If Fear-Based Mode, user also has:**
- Resolution status for each original fear
- Minimal tests designed to learn (failure = data)
- Clear separation of controllable vs uncontrollable
- False walls cleared (proceed with confidence)
- True walls confirmed (save wasted effort)
- Growth assessment for each option
