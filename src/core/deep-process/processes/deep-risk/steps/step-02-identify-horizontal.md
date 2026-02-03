# Step 02: IDENTIFY — Horizontal Extraction

## Purpose

Discover risks that live AT BOUNDARIES — between components, teams, phases, and organizations. These risks are invisible to vertical analysis because each side assumes the other handles them.

**Time:** 30-60 min (Standard), skip for Quick

**Inputs:** Vertical Risk Inventory from Step 1

**Outputs:** Horizontal Risk Inventory, Complete Risk List

---

## Procedure

### 02.1 Boundary Risk Scan (#108)

📂 Load method: `data/method-procedures/108_Boundary_Risk_Scan.md`

Systematically identify risks at interfaces:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         BOUNDARY MAPPING                                   ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  COMPONENT INTERFACES:                                                     ║
║  ┌────────────────────────────────────────────────────────────────────┐   ║
║  │ Interface: ________________________________________________        │   ║
║  │ Side A assumes: ___________________________________________        │   ║
║  │ Side B assumes: ___________________________________________        │   ║
║  │ Mismatch: _________________________________________________        │   ║
║  │ Documented? [ ] Y [ ] N                                            │   ║
║  │ RISK: _____________________________________________________        │   ║
║  └────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
║  TEAM HANDOFFS:                                                            ║
║  [Same format]                                                             ║
║                                                                            ║
║  PHASE TRANSITIONS (dev→QA→prod, design→impl):                            ║
║  [Same format]                                                             ║
║                                                                            ║
║  ORGANIZATIONAL EDGES (client↔vendor, team↔team):                         ║
║  [Same format]                                                             ║
║                                                                            ║
║  TEMPORAL BOUNDARIES (shifts, sprints, fiscal years):                     ║
║  [Same format]                                                             ║
║                                                                            ║
║  TRUST BOUNDARIES (internal↔external, auth↔anon):                         ║
║  [Same format]                                                             ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝

THE HANDOFF TRIAD (apply to each boundary):
1. What does Side A ASSUME Side B provides?
2. What does Side B ASSUME Side A has done?
3. Are these assumptions WRITTEN DOWN and AGREED?

Where assumptions don't match = BOUNDARY RISK
Where assumptions aren't documented = LATENT BOUNDARY RISK
```

---

### 02.2 Blind Spot Interrogation (#109)

📂 Load method: `data/method-procedures/109_Blind_Spot_Interrogation.md`

Deliberately search for what the team cannot see:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      BLIND SPOT ANALYSIS                                   ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  EXPERTISE GAP:                                                            ║
║  "What domain knowledge is missing?"                                       ║
║  "What would a specialist in [X] flag?"                                   ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  NORMALCY BIAS:                                                            ║
║  "What are we assuming will continue because it always has?"              ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  SUCCESS BIAS:                                                             ║
║  "What risks are we ignoring because current approach 'always worked'?"   ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  PROXIMITY BIAS:                                                           ║
║  "What risks are we downplaying because they seem distant?"               ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  COMPLEXITY HIDING:                                                        ║
║  "Where is complexity swept under abstractions?"                          ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  INCENTIVE MISALIGNMENT:                                                   ║
║  "Who benefits from NOT seeing certain risks?"                            ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  ASYMMETRIC INFORMATION:                                                   ║
║  "Who knows something we don't? (vendor, client, regulator)"              ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  ⚠️ UNKNOWN KNOWNS (MOST DANGEROUS):                                       ║
║  "What does the organization KNOW but refuses to acknowledge?"            ║
║  "What are the taboo topics? What would get you fired for raising?"       ║
║  → _______________________________________________________________        ║
║                                                                            ║
║  SURVIVORSHIP BIAS:                                                        ║
║  "What similar projects failed silently?"                                 ║
║  → _______________________________________________________________        ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝

KEY QUESTION: "Who on the team would be LEAST likely to raise this?"
(That's where blind spots live)

ADVERSARIAL PERSPECTIVE:
"If trying to SABOTAGE this project, what would you exploit?"
→ ___________________________________________________________________
```

---

### 02.3 Chaos Probe Design (#110)

📂 Load method: `data/method-procedures/110_Chaos_Probe_Design.md`

**Note:** Execution only in CRITICAL depth. Design in COMPREHENSIVE.

Design controlled experiments that EMPIRICALLY discover risks:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      CHAOS PROBE DESIGN                                    ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  STEADY STATE DEFINITION:                                                  ║
║  "System working correctly" looks like:                                   ║
║  • Metric 1: _____________________ = ___________                          ║
║  • Metric 2: _____________________ = ___________                          ║
║  • Metric 3: _____________________ = ___________                          ║
║                                                                            ║
║  PROBE 1:                                                                  ║
║  ┌────────────────────────────────────────────────────────────────────┐   ║
║  │ What to break: ________________________________________________    │   ║
║  │ Expected result: ______________________________________________    │   ║
║  │ Blast radius control: _________________________________________    │   ║
║  │ Observation plan: _____________________________________________    │   ║
║  │ Abort criteria: _______________________________________________    │   ║
║  │                                                                    │   ║
║  │ EXECUTION (critical depth only):                                   │   ║
║  │ Actual result: ________________________________________________    │   ║
║  │ UNEXPECTED? [ ] Y [ ] N                                            │   ║
║  │ Discovered risk: ______________________________________________    │   ║
║  └────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
║  [Design 3-5 probes for critical components/dependencies]                 ║
║                                                                            ║
║  WHY THIS MATTERS:                                                         ║
║  Analytical methods suffer from imagination limits.                       ║
║  Chaos probes let the system reveal its own failure modes.               ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

### 02.4 Temporal Risk Archaeology (#111)

📂 Load method: `data/method-procedures/111_Temporal_Risk_Archaeology.md`

Search for risks created by TIME:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    TEMPORAL RISK ARCHAEOLOGY                               ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  FOR EACH COMPONENT/PROCESS/RELATIONSHIP:                                  ║
║                                                                            ║
║  DEGRADATION (what is slowly getting worse):                              ║
║  ┌────────────────────────┬───────────────┬───────────────┬────────────┐ ║
║  │ What                   │ Current State │ Threshold     │ Time to    │ ║
║  │                        │               │               │ Threshold  │ ║
║  ├────────────────────────┼───────────────┼───────────────┼────────────┤ ║
║  │ Performance            │               │               │            │ ║
║  │ Data quality           │               │               │            │ ║
║  │ Test coverage          │               │               │            │ ║
║  │ Documentation accuracy │               │               │            │ ║
║  │ _________________      │               │               │            │ ║
║  └────────────────────────┴───────────────┴───────────────┴────────────┘ ║
║                                                                            ║
║  ACCUMULATION (what is slowly building up):                               ║
║  • Technical debt: _________________________________________________      ║
║  • Configuration drift: ___________________________________________      ║
║  • Permission creep: ______________________________________________      ║
║  • Complexity: ____________________________________________________      ║
║                                                                            ║
║  EXPIRATION (what is slowly running out):                                 ║
║  • Certificates: __________________ expires: __________                   ║
║  • Contracts: _____________________ expires: __________                   ║
║  • Vendor relationships: ____________ risk date: ________                 ║
║  • Team knowledge: _________________ at risk when: ______                 ║
║  • Technology relevance: ____________ obsolete by: ______                 ║
║                                                                            ║
║  VALIDATION DEBT (what worked before but hasn't been re-checked):        ║
║  • Last validated: _________________ Current assumption: ___________     ║
║                                                                            ║
║  ⚠️ KEY INSIGHT:                                                           ║
║  The trigger for temporal risks is NOT an event —                         ║
║  it's the ABSENCE of an event (no one checked, no one updated)           ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

### 02.5 Scenario Planning Matrix (#112)

📂 Load method: `data/method-procedures/112_Scenario_Planning_Matrix.md`

Construct structured scenarios from key uncertainties:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    SCENARIO PLANNING MATRIX                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  STEP 1: Identify 2 most impactful + uncertain dimensions                 ║
║                                                                            ║
║  Dimension 1: ______________________ (LOW vs HIGH)                        ║
║  Dimension 2: ______________________ (LOW vs HIGH)                        ║
║                                                                            ║
║  STEP 2: Construct 2×2 Matrix                                             ║
║                                                                            ║
║                           DIMENSION 2                                      ║
║                       LOW              HIGH                                ║
║              ┌─────────────────┬─────────────────┐                        ║
║   DIMENSION  │  SCENARIO A:    │  SCENARIO B:    │                        ║
║   1: LOW     │  "[name]"       │  "[name]"       │                        ║
║              │                 │                 │                        ║
║              │  Risks:         │  Risks:         │                        ║
║              │  •              │  •              │                        ║
║              │  •              │  •              │                        ║
║              ├─────────────────┼─────────────────┤                        ║
║   DIMENSION  │  SCENARIO C:    │  SCENARIO D:    │                        ║
║   1: HIGH    │  "[name]"       │  "[name]"       │                        ║
║              │                 │                 │                        ║
║              │  Risks:         │  Risks:         │                        ║
║              │  •              │  •              │                        ║
║              │  •              │  •              │                        ║
║              └─────────────────┴─────────────────┘                        ║
║                                                                            ║
║  STEP 3: Identify Risk Robustness                                         ║
║                                                                            ║
║  ROBUST RISKS (appear in 3+ scenarios):                                   ║
║  → These are HIGH PRIORITY regardless of which future materializes       ║
║  • _______________________________________________________________        ║
║  • _______________________________________________________________        ║
║                                                                            ║
║  CONDITIONAL RISKS (unique to 1 scenario):                                ║
║  → Monitor for that scenario's indicators                                 ║
║  • Scenario ___: Risk: _________________ Indicator: ______________        ║
║                                                                            ║
║  CURRENT PLAN ROBUSTNESS:                                                  ║
║  Plan works in scenarios: [ ] A [ ] B [ ] C [ ] D                         ║
║  Plan fails in scenarios: [ ] A [ ] B [ ] C [ ] D                         ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Output: Horizontal Risk Inventory

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  HORIZONTAL RISK INVENTORY                                                 ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  METHODS EXECUTED:                                                         ║
║  □ #108 Boundary Risk Scan                                                ║
║  □ #109 Blind Spot Interrogation                                          ║
║  □ #110 Chaos Probe Design [critical only]                                ║
║  □ #111 Temporal Risk Archaeology                                         ║
║  □ #112 Scenario Planning Matrix                                          ║
║                                                                            ║
║  HORIZONTAL RISKS IDENTIFIED: [count]                                     ║
║  BY TYPE:                                                                  ║
║  • Boundary risks: [n]                                                    ║
║  • Blind spots: [n]                                                       ║
║  • Temporal risks: [n]                                                    ║
║  • Scenario-dependent risks: [n]                                          ║
║  • Chaos-discovered risks: [n]                                            ║
║                                                                            ║
║  CRITICAL FINDINGS:                                                        ║
║  • Undocumented boundaries: [list]                                        ║
║  • Unknown knowns (taboo risks): [list]                                   ║
║  • Approaching thresholds: [list]                                         ║
║  • Robust risks (all scenarios): [list]                                   ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Output: Complete Risk List

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  COMPLETE RISK LIST                                                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  TOTAL RISKS IDENTIFIED: [vertical + horizontal]                          ║
║                                                                            ║
║  VERTICAL (Step 1): [n]                                                   ║
║  HORIZONTAL (Step 2): [n]                                                 ║
║                                                                            ║
║  BY GENESIS SOURCE:                                                        ║
║  • Complexity: [n]      • Coupling: [n]    • Uncertainty: [n]            ║
║  • Agency: [n]          • Temporality: [n] • Boundaries: [n]             ║
║                                                                            ║
║  BY KNIGHT CLASSIFICATION:                                                 ║
║  • Risk (quantifiable): [n]                                               ║
║  • Uncertainty (unknown distribution): [n]                                ║
║  • Ambiguity (unclear question): [n]                                      ║
║                                                                            ║
║  READY FOR QUANTIFICATION                                                  ║
║  PROCEED TO STEP 3? [YES/NO]                                              ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Feedback Loop Check

```
□ Did horizontal extraction reveal scope issues?
  → YES: Return to Step 0

□ Did boundary analysis reveal new components to examine vertically?
  → YES: Return to Step 1

□ Ready for quantification?
  → PROCEED TO STEP 3
```

---

## META Check (after IDENTIFY completion)

📂 Load: `meta/meta-checklist.yaml`

Apply #601 Cognitive Bias Audit:
- [ ] Optimism bias? (underestimating risks)
- [ ] Availability bias? (overweighting recent/vivid risks)
- [ ] Groupthink? (team converging on comfortable assessment)

---

## Transition

- **If complete risk list ready** → Proceed to Step 3 (QUANTIFY)
- **If new vertical risks found** → Return to Step 1
- **If scope issues found** → Return to Step 0
