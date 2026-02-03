# Step 00: GROUND

## Purpose

Establish theoretical framing BEFORE searching for risks. Understand WHERE risks come from, WHAT types of uncertainty you face, and HOW your system's structure shapes its vulnerability profile.

**Time:** 30-60 min (Standard), 15 min (Quick)

**Inputs:** Subject description, context, Deep-Explore/Verify outputs if available

**Outputs:** System Profile, Uncertainty Map, Genesis Risk Seeds

---

## Procedure

### 00.1 Frame the Assessment Scope

```
ASSESSMENT SCOPE:
"We are assessing risks for: _______________________________________"

SCOPE BOUNDARIES:
• In scope: ________________________________________________
• Out of scope: ____________________________________________
• Timeframe: ______________________________________________

STAKES: [ ] LOW  [ ] MEDIUM  [ ] HIGH  [ ] CRITICAL

WHY STAKES MATTER:
• LOW: Inconvenience if risks materialize
• MEDIUM: Significant cost/delay but recoverable
• HIGH: Major impact, recovery uncertain
• CRITICAL: Existential threat, irreversible consequences
```

### 00.2 Check for Integration Inputs

```
DEEP-EXPLORE INPUTS:
□ Exploration report available? [Y/N]
  → If Y: Extract assumptions, dependencies, consequences

DEEP-VERIFY INPUTS:
□ Verification report available? [Y/N]
  → If Y: Extract impossibility findings, ungrounded claims

EXTRACTED INPUTS:
• From Explore: ___________________________________________
• From Verify: ____________________________________________
```

---

## 00.3 Risk Genesis Model (#001)

📂 Load method: `data/method-procedures/001_Risk_Genesis_Model.md`

Systematically scan six fundamental sources from which ALL risks originate:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         RISK GENESIS SCAN                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  SOURCE 1: COMPLEXITY                                                      ║
║  "How does emergent behavior, non-linearity manifest here?"               ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: HIGH (emerges only in combination)             ║
║                                                                            ║
║  SOURCE 2: COUPLING                                                        ║
║  "How does propagation, cascade, shared dependencies manifest here?"      ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: MEDIUM (visible in architecture)               ║
║                                                                            ║
║  SOURCE 3: UNCERTAINTY                                                     ║
║  "Where is information incomplete, volatile, unknowable?"                 ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: VARIES (epistemic reducible, aleatoric not)   ║
║                                                                            ║
║  SOURCE 4: AGENCY                                                          ║
║  "Who could act adversarially, negligently, with misaligned incentives?" ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: HIGH (adversaries adapt)                       ║
║                                                                            ║
║  SOURCE 5: TEMPORALITY                                                     ║
║  "What is slowly eroding, drifting, accumulating, decaying?"             ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: VERY HIGH (each increment is small)           ║
║                                                                            ║
║  SOURCE 6: BOUNDARIES                                                      ║
║  "Where do interfaces, handoffs, trust boundaries create gaps?"          ║
║  ├── Risk: ________________________________________________              ║
║  ├── Risk: ________________________________________________              ║
║  └── Detection difficulty: HIGH (each side assumes the other handles it) ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝

GENESIS QUALITY CHECK:
□ At least 2 risks per source? (Empty source = blind spot, investigate)
□ Tagged each risk with genesis source?
□ Noted detection difficulty?
```

---

## 00.4 Uncertainty Classification (#002)

📂 Load method: `data/method-procedures/002_Uncertainty_Classification.md`

Classify every identified uncertainty into its fundamental type:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    UNCERTAINTY CLASSIFICATION                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  KNIGHT'S DISTINCTION:                                                     ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │ Type        │ You Know...           │ Management Strategy           │  ║
║  ├─────────────┼───────────────────────┼───────────────────────────────┤  ║
║  │ RISK        │ Probability + Impact  │ Calculate EV, hedge, insure   │  ║
║  │ UNCERTAINTY │ That you don't know   │ Scenario plan, build options  │  ║
║  │ AMBIGUITY   │ Not even the question │ Clarify, decompose, define    │  ║
║  └─────────────┴───────────────────────┴───────────────────────────────┘  ║
║                                                                            ║
║  SUB-CLASSIFICATION:                                                       ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │ Sub-type    │ Definition            │ Response                      │  ║
║  ├─────────────┼───────────────────────┼───────────────────────────────┤  ║
║  │ ALEATORIC   │ Inherent randomness   │ Build resilience, redundancy  │  ║
║  │ EPISTEMIC   │ Knowledge gap         │ Investigate, prototype, test  │  ║
║  └─────────────┴───────────────────────┴───────────────────────────────┘  ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝

CLASSIFY EACH GENESIS RISK:
┌─────────────────────────────────┬───────────┬───────────┬─────────────────┐
│ Risk                            │ Knight    │ Sub-type  │ Strategy Match? │
├─────────────────────────────────┼───────────┼───────────┼─────────────────┤
│                                 │ R/U/A     │ ALE/EPI   │ Y/N             │
│                                 │ R/U/A     │ ALE/EPI   │ Y/N             │
│                                 │ R/U/A     │ ALE/EPI   │ Y/N             │
└─────────────────────────────────┴───────────┴───────────┴─────────────────┘

⚠️ RED FLAG: Assigning P=3 to something that is fundamentally UNCERTAIN
   (unknown distribution). This is faux precision — worse than "we don't know."

RUMSFELD AUDIT:
□ Known knowns: _____ (facts in register)
□ Known unknowns: _____ (questions to investigate)
□ Unknown knowns: _____ (organizational denial?) ← MOST DANGEROUS
□ Unknown unknowns: _____ (build general resilience)
```

---

## 00.5 System Characterization (#003)

📂 Load method: `data/method-procedures/003_System_Characterization.md`

Assess position on Perrow's complexity-coupling matrix:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    PERROW MATRIX ASSESSMENT                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  COMPLEXITY SCORE (1-5):                                                   ║
║  □ Many feedback loops? ___                                                ║
║  □ Non-linear component interactions? ___                                  ║
║  □ Multiple paths between components? ___                                  ║
║  □ Components serve multiple functions? ___                                ║
║  □ Emergent properties? ___                                                ║
║  COMPLEXITY = ___ / 5                                                      ║
║                                                                            ║
║  COUPLING SCORE (1-5):                                                     ║
║  □ Time-dependent processes? ___                                           ║
║  □ Limited slack/buffer? ___                                               ║
║  □ One way to achieve goal? ___                                            ║
║  □ Little redundancy? ___                                                  ║
║  □ Fast propagation of effects? ___                                        ║
║  COUPLING = ___ / 5                                                        ║
║                                                                            ║
║                          PERROW MATRIX                                     ║
║                                                                            ║
║                        COUPLING                                            ║
║                    Loose (1-2)    Tight (4-5)                             ║
║              ┌───────────────┬───────────────┐                            ║
║   Linear     │   LOW RISK    │   MODERATE    │                            ║
║ COMPLEXITY   │   (simple     │   (fast but   │                            ║
║   (1-2)      │   + slack)    │   linear)     │                            ║
║              ├───────────────┼───────────────┤                            ║
║   Complex    │   MODERATE    │   NORMAL      │                            ║
║   (4-5)      │   (complex    │   ACCIDENTS   │                            ║
║              │   but slack)  │   ZONE ←      │                            ║
║              └───────────────┴───────────────┘                            ║
║                                                                            ║
║  YOUR POSITION: Complexity=___ Coupling=___ → ZONE: ___________           ║
║                                                                            ║
║  IF IN NORMAL ACCIDENTS ZONE:                                              ║
║  → Accept that some failures are INEVITABLE                                ║
║  → Shift investment from PREVENTION to DETECTION + RECOVERY               ║
║  → Design for survivability, not perfection                                ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝

SUBSYSTEM PROFILES (if system spans multiple zones):
┌─────────────────────────────┬───────────┬─────────┬────────────────────┐
│ Subsystem                   │ Complexity│ Coupling│ Zone               │
├─────────────────────────────┼───────────┼─────────┼────────────────────┤
│                             │           │         │                    │
│                             │           │         │                    │
└─────────────────────────────┴───────────┴─────────┴────────────────────┘
```

---

## Output: System Profile

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  SYSTEM PROFILE                                                            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  SCOPE: ___________________________________________________               ║
║  STAKES: [ ] LOW  [ ] MEDIUM  [ ] HIGH  [ ] CRITICAL                      ║
║                                                                            ║
║  PERROW CHARACTERIZATION:                                                  ║
║  • Complexity: ___ / 5                                                     ║
║  • Coupling: ___ / 5                                                       ║
║  • Zone: _________________                                                 ║
║  • Strategic implication: ________________________________                ║
║                                                                            ║
║  GENESIS RISKS SEEDED: [count] per source                                 ║
║  • Complexity: [n]                                                         ║
║  • Coupling: [n]                                                           ║
║  • Uncertainty: [n]                                                        ║
║  • Agency: [n]                                                             ║
║  • Temporality: [n]                                                        ║
║  • Boundaries: [n]                                                         ║
║                                                                            ║
║  UNCERTAINTY MAP:                                                          ║
║  • Knight-Risk (quantifiable): [n]                                        ║
║  • Knight-Uncertainty (unknown distribution): [n]                         ║
║  • Knight-Ambiguity (unclear question): [n]                               ║
║                                                                            ║
║  INTEGRATION INPUTS:                                                       ║
║  • From Deep-Explore: [list]                                              ║
║  • From Deep-Verify: [list]                                               ║
║                                                                            ║
║  PROCEED TO STEP 1? [YES/NO]                                              ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Transition

- **If system profiled** → Proceed to Step 1 (IDENTIFY Vertical)
- **If scope unclear** → Stay in Step 0, refine scope
- **If crisis_mode = on** → Skip to Step 1 with minimal profiling
