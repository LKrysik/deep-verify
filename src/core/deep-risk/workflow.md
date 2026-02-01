# Deep Risk V1.0 — Systematic Risk Assessment Workflow

---

## INVOCATION

**When user wants to assess risks, ALWAYS start with this dialog:**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP RISK                                             ║
║                      Systematic Risk Assessment                            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Before we begin, select assessment depth:                                 ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [1] QUICK  (1-2 hours)                                             │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Risk Genesis + basic taxonomy scan                               │  ║
║  │  • Top 5-10 risks identified and scored                             │  ║
║  │  • Basic mitigation classification (4T)                             │  ║
║  │  • Key monitoring indicators                                         │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Rapid triage before deeper analysis                              │  ║
║  │  → Low-stakes decisions                                              │  ║
║  │  → Periodic risk refresh                                             │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [2] STANDARD  (half day)                                           │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Full GROUND phase (system characterization)                      │  ║
║  │  • Complete IDENTIFY (vertical + horizontal)                        │  ║
║  │  • 5D scoring for all risks                                         │  ║
║  │  • Risk interaction analysis (cascades, correlations)               │  ║
║  │  • Mitigation portfolio with Cobra Effect checks                    │  ║
║  │  • Monitoring system design                                          │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Important decisions requiring thorough analysis                  │  ║
║  │  → Medium-to-high stakes                                             │  ║
║  │  → Pre-release risk review                                           │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [3] COMPREHENSIVE  (1-2 days)                                      │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in STANDARD                                            │  ║
║  │  • Ergodicity testing for high-impact risks                         │  ║
║  │  • Stability basin mapping                                           │  ║
║  │  • Min-cut analysis for structural vulnerabilities                  │  ║
║  │  • Full META audit (bias, appetite, Goodhart, Simpson)              │  ║
║  │  • Portfolio-level risk view                                         │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → High-stakes decisions                                             │  ║
║  │  → New project kickoff                                               │  ║
║  │  → Architecture decisions                                            │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [4] CRITICAL  (multi-day)                                          │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in COMPREHENSIVE                                       │  ║
║  │  • Chaos probe design and execution                                 │  ║
║  │  • External research and validation                                 │  ║
║  │  • Multiple iteration cycles                                         │  ║
║  │  • Stakeholder review integration                                   │  ║
║  │  • Living risk dashboard                                             │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Critical, irreversible decisions                                 │  ║
║  │  → Very high stakes (company, career, safety)                       │  ║
║  │  → Regulatory/compliance requirements                               │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  Select: [1] / [2] / [3] / [4]                                            ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**After user selection:**
1. Record depth: `depth = quick | standard | comprehensive | critical`
2. Scan input for crisis signals (see: CRISIS DETECTION)
3. Begin execution from Step 0

---

## CRISIS DETECTION (automatic)

**Do not ask user about crisis mode. Detect automatically from language.**

If description contains:
- "urgent", "emergency", "crisis", "incident"
- "already failed", "happening now", "in production"
- "deadline tomorrow", "no time"
- "everything is down", "critical outage"

**→ Enable `crisis_mode = on`**

This means:
- Skip GROUND phase, go directly to IDENTIFY
- Focus on immediate containment, not comprehensive analysis
- Prioritize MITIGATE and MONITOR phases
- In report: add Crisis Response section

**If no crisis signals → `crisis_mode = off`** (standard assessment)

---

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP RISK = THEORY + DISCOVERY + QUANTIFICATION + INTERACTION + RESPONSE  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Project, decision, system, architecture, strategy                 │
│  OUTPUT:  ACTIONABLE RISK INTELLIGENCE                                      │
│           • Risk register with multi-dimensional scores                     │
│           • Risk interaction map (cascades, correlations)                   │
│           • Mitigation portfolio with perverse effect checks                │
│           • Monitoring system with leading indicators                       │
│           • Portfolio view with existential risk flags                      │
│                                                                              │
│  CORE PRINCIPLES:                                                           │
│  1. START FROM THEORY — understand WHY risks exist before looking for them │
│  2. RISKS ARE NOT INDEPENDENT — cascades and correlations cause catastrophe│
│  3. P×I IS INSUFFICIENT — velocity, detectability, reversibility matter    │
│  4. ERGODICITY DETERMINES STRATEGY — can we survive or is it game over?    │
│  5. MITIGATIONS CAN BACKFIRE — every cure must be checked for side effects │
│  6. RISK ASSESSMENT DECAYS — gradual accumulation is as dangerous as events│
│                                                                              │
│  INTEGRATION: Consumes outputs from Deep-Explore and Deep-Verify           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## THEORETICAL FOUNDATIONS

Deep Risk is grounded in foundational theorems that constrain what risk management CAN and CANNOT achieve. Load: `data/theoretical-foundations.yaml`

### Quick Reference

| Principle | One-Line Summary | Applied In |
|-----------|------------------|------------|
| **Normal Accidents (Perrow)** | Complex + tightly coupled = accidents inevitable | #003, #305 |
| **Non-Ergodicity (Peters)** | Can't average what you only experience once | #206, #401, #408 |
| **Fat Tails (Taleb)** | Extremes dominate, means mislead | #201, #203, #402 |
| **Swiss Cheese (Reason)** | Aligned holes in layers = failure | #303, #403 |
| **Cobra Effect** | Interventions can backfire | #407 |
| **Goodhart's Law** | Measured target → gamed target | #501, #606 |
| **Knight's Distinction** | Risk ≠ Uncertainty ≠ Ambiguity | #002, #201 |
| **Survivorship Bias** | We only learn from visible failures | #106, #204 |
| **Lindy Effect** | Old = robust, new = fragile | #104, #111 |

---

## DEPTH LEVELS — What executes at each level

### QUICK (depth = quick)

```
PHASES:          GROUND(lite) → IDENTIFY(V only) → QUANTIFY(basic) → MITIGATE(4T) → MONITOR(indicators)
METHODS:         001, 002, 003 + 101-104 + 201 + 401, 406 + 501
MAX ITERATIONS:  1 (no feedback loops)
RISKS ANALYZED:  Top 10
COVERAGE TARGET: C ≥ 15
```

### STANDARD (depth = standard)

```
PHASES:          GROUND → IDENTIFY(V+H) → QUANTIFY → INTERACT(core) → MITIGATE → MONITOR
METHODS:         All GROUND + All IDENTIFY + 201-205 + 301-304 + 401-407 + 501-503
MAX ITERATIONS:  3
RISKS ANALYZED:  All identified
COVERAGE TARGET: C ≥ 35
```

### COMPREHENSIVE (depth = comprehensive)

```
PHASES:          GROUND → IDENTIFY → QUANTIFY(full) → INTERACT(full) → MITIGATE(full) → MONITOR → META
METHODS:         All methods except chaos probes
MAX ITERATIONS:  5
RISKS ANALYZED:  All + portfolio view
COVERAGE TARGET: C ≥ 50
```

### CRITICAL (depth = critical)

```
PHASES:          All phases, full execution
METHODS:         All 44 methods including chaos probes (#110)
MAX ITERATIONS:  Unlimited
RISKS ANALYZED:  Exhaustive + external validation
COVERAGE TARGET: C ≥ 65
```

---

## EXECUTION FLOW

```
                    ┌──────────────────────────────────────────┐
                    │          FEEDBACK LOOPS                  │
                    │     (standard+ depths only)              │
                    ▼                                          │
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│ STEP 0  │───►│ STEP 1  │───►│ STEP 2  │───►│ STEP 3  │─────┤
│ GROUND  │    │IDENTIFY-V    │IDENTIFY-H    │ QUANTIFY│     │
└─────────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
                    │              │              │           │
                    └──────────────┴──────────────┘           │
                                        │                     │
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│ STEP 4  │───►│ STEP 5  │───►│ STEP 6  │───►│ STEP 7  │◄────┘
│INTERACT │    │MITIGATE │    │ MONITOR │    │ OUTPUT  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                  │
                              ┌────────────────────┘
                              ▼
                         META (continuous)
                    Applied after each phase
```

---

## EXECUTION PATH

**After user selects depth level, execute:**

```
📂 Step 0: GROUND
   Load: steps/step-00-ground.md

   □ Frame the assessment scope
   □ Assess stakes: LOW/MEDIUM/HIGH/CRITICAL
   □ 📂 #001 → Risk Genesis Model (6 sources)
   □ 📂 #002 → Uncertainty Classification (Knight)
   □ 📂 #003 → System Characterization (Perrow Matrix)

   IF crisis_mode = on:
   → Skip GROUND, proceed directly to IDENTIFY

   Output: System Profile, Uncertainty Map, Genesis Risk Seeds

   ↓ PROCEED when system is characterized
   ↓ STAY if scope unclear

📂 Step 1: IDENTIFY — Vertical
   Load: steps/step-01-identify-vertical.md

   □ 📂 #101 → Risk Taxonomy Scan (categories)
   □ 📂 #102 → Failure Mode Enumeration (per component)
   □ 📂 #103 → Threat Modeling STRIDE+ (adversarial)
   □ 📂 #104 → Dependency Risk Discovery (external)
   □ 📂 #105 → Assumption Torture (graduated stress test)
   □ 📂 #106 → Historical Pattern Matching (survivorship-corrected)
   □ 📂 #107 → Contraposition Failure Guarantee (what guarantees failure?)

   DEPTH ADJUSTMENT:
   • quick: #101-104 only
   • standard+: all vertical methods

   Output: Vertical Risk Inventory

   ↓ PROCEED to horizontal extraction
   ↑ RETURN TO STEP 0 if scope needs refinement

📂 Step 2: IDENTIFY — Horizontal
   Load: steps/step-02-identify-horizontal.md

   □ 📂 #108 → Boundary Risk Scan (interface risks)
   □ 📂 #109 → Blind Spot Interrogation (what can't we see?)
   □ 📂 #110 → Chaos Probe Design (empirical discovery) [critical only]
   □ 📂 #111 → Temporal Risk Archaeology (gradual risks)
   □ 📂 #112 → Scenario Planning Matrix (future-dependent risks)

   DEPTH ADJUSTMENT:
   • quick: skip entirely
   • standard: #108-109, #111-112
   • comprehensive+: all including #110 design (not execution)
   • critical: #110 execution included

   Output: Horizontal Risk Inventory, Complete Risk List

   ↓ PROCEED to quantification
   ↑ RETURN TO STEP 0 if new scope elements discovered

📂 Step 3: QUANTIFY
   Load: steps/step-03-quantify.md

   □ 📂 #201 → Five-Dimension Risk Scoring (P/I/V/D/R)
   □ 📂 #202 → Exposure Window Analysis (when vulnerable?)
   □ 📂 #203 → Cost-of-Materialization Estimation
   □ 📂 #204 → Precedent Probability Calibration (base rates)
   □ 📂 #205 → Worst-Case Scenario Construction
   □ 📂 #206 → Ergodicity Test (survivable or game over?)
   □ 📂 #207 → Stability Basin Mapping (distance to tipping point)

   DEPTH ADJUSTMENT:
   • quick: #201 only (basic scoring)
   • standard: #201-205
   • comprehensive+: all including #206, #207

   Output: Scored Risk Register

   ↓ PROCEED to interaction analysis
   ↑ RETURN TO STEP 1/2 if new risks discovered during quantification

📂 Step 4: INTERACT
   Load: steps/step-04-interact.md

   □ 📂 #301 → Risk Cascade Mapping (trigger chains)
   □ 📂 #302 → Risk Correlation Matrix (simultaneous risks)
   □ 📂 #303 → Common Mode Failure Detection (hidden shared dependencies)
   □ 📂 #304 → Concentration Risk Detection (single points)
   □ 📂 #305 → Compound Risk Scenarios (multiple risks combining)
   □ 📂 #306 → Critical Path Severance (min-cut analysis)
   □ 📂 #307 → Risk Interaction Paradoxes (managing A amplifies B?)

   DEPTH ADJUSTMENT:
   • quick: skip entirely
   • standard: #301-304
   • comprehensive+: all

   Output: Risk Network Graph, Interaction Map

   ↓ PROCEED to mitigation
   ↑ RETURN if interactions reveal new risks

📂 Step 5: MITIGATE
   Load: steps/step-05-mitigate.md

   □ 📂 #401 → Four-T Classification (Terminate/Transfer/Treat/Tolerate)
   □ 📂 #402 → Mitigation Cost-Benefit Analysis
   □ 📂 #403 → Defense in Depth Design (Swiss Cheese validated)
   □ 📂 #404 → Graceful Degradation Planning
   □ 📂 #405 → Residual Risk Assessment
   □ 📂 #406 → Contingency Trigger Design
   □ 📂 #407 → Cobra Effect Check (MANDATORY for all mitigations)
   □ 📂 #408 → Regret Minimization Framework (for irreversible decisions)

   DEPTH ADJUSTMENT:
   • quick: #401, #406 only
   • standard: #401-407
   • comprehensive+: all including #408

   Output: Mitigation Portfolio

   ↓ PROCEED to monitoring
   ↓ STAY if Cobra Effect reveals new risks

📂 Step 6: MONITOR
   Load: steps/step-06-monitor.md

   □ 📂 #501 → Leading Indicator Identification
   □ 📂 #502 → Risk Review Cadence Design
   □ 📂 #503 → Escalation Protocol Design
   □ 📂 #504 → Post-Incident Feedback Loop
   □ 📂 #505 → Sorites Accumulation Watch (gradual threshold approach)

   DEPTH ADJUSTMENT:
   • quick: #501 only
   • standard: #501-503
   • comprehensive+: all

   Output: Monitoring System Design

   ↓ PROCEED to output

📂 Step 7: OUTPUT
   Load: steps/step-07-output.md

   □ Apply META methods (#601-606) as final audit
   □ Generate Risk Register
   □ Generate Risk Report
   □ Generate Portfolio Dashboard (comprehensive+)

   Load templates:
   • data/risk-register-template.md
   • data/risk-report-template.md
   • data/portfolio-dashboard-template.md

   Output: RISK ASSESSMENT DELIVERABLES
```

---

## META METHODS (Continuous)

META methods (#601-606) govern the risk assessment process itself. Apply after each phase completion:

| # | Method | Purpose | When to Apply |
|---|--------|---------|---------------|
| 601 | Cognitive Bias Audit | Check for optimism, anchoring, availability bias | After IDENTIFY, QUANTIFY |
| 602 | Risk Appetite Calibration | Stated vs revealed appetite | After MITIGATE |
| 603 | Portfolio Risk View | Aggregate portfolio assessment | After all phases |
| 604 | Risk Communication Framework | Right view for right audience | During OUTPUT |
| 605 | Simpson's Paradox Audit | Aggregate hiding subgroup problems? | After QUANTIFY, OUTPUT |
| 606 | Goodhart's Law Check | Are metrics being gamed? | After MONITOR |

Load: `meta/meta-checklist.yaml`

---

## SCORING SYSTEMS

### Process Coverage Score (C)

Measures how thoroughly the assessment was conducted:

| Activity | Points |
|----------|--------|
| Phase completed | +3 |
| Method executed | +1 |
| Risk identified | +0.5 |
| Risk interaction mapped | +0.5 |
| Mitigation with Cobra check | +1 |
| META method applied | +0.5 |

Load: `data/coverage-scoring.yaml`

### Risk Score (5D)

Each risk scored on 5 dimensions:

| Dimension | Scale | Question |
|-----------|-------|----------|
| **P** Probability | 1-5 | How likely? |
| **I** Impact | 1-5 | How severe? |
| **V** Velocity | 1-5 | How fast once triggered? (5=instant) |
| **D** Detectability | 1-5 | How hard to see coming? (5=invisible) |
| **R** Reversibility | 1-5 | How hard to recover? (5=permanent) |

**Composite:** `Risk Score = P × I × max(V, D, R)`

**Flags:**
- `FAT_TAIL` — Impact may be 100× worse than score suggests
- `NON_ERGODIC` — Survival uncertain, expected value meaningless
- `LOW_CONFIDENCE` — Probability estimate unreliable (Knight-Uncertainty)

Load: `data/risk-scoring.yaml`

### Portfolio Thresholds

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| Total Expected Loss | vs total budget | Aggregate exposure |
| Max Simultaneous Loss | vs survivability | Correlated risk exposure |
| Non-Ergodic Count | Any unmitigated = RED | Existential risks |
| Fat-Tail Count | Any unmitigated = RED | Underestimated risks |
| Mitigation Coverage | <80% = gap | Critical risks without mitigation |

Load: `data/portfolio-thresholds.yaml`

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  RISK ASSESSMENT COMMANDMENTS                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. THEORY BEFORE SEARCH                                                    │
│     Understand WHY risks exist (GROUND) before looking for WHERE            │
│     Skip theory → miss structural risks                                     │
│                                                                              │
│  2. VERTICAL + HORIZONTAL                                                   │
│     Component-level (vertical) misses boundary risks (horizontal)           │
│     Both extractions are mandatory for standard+ depths                     │
│                                                                              │
│  3. INTERACTIONS MATTER MORE THAN INDIVIDUALS                               │
│     Single risks are manageable; cascades cause catastrophe                 │
│     INTERACT phase is mandatory for standard+ depths                        │
│                                                                              │
│  4. CHECK YOUR CURES                                                        │
│     Every mitigation MUST pass Cobra Effect check (#407)                    │
│     Mitigations that create worse risks must be redesigned                  │
│                                                                              │
│  5. FLAG EXISTENTIAL RISKS                                                  │
│     Non-ergodic risks (game over if they hit) need special handling         │
│     Expected value optimization is WRONG for these                          │
│                                                                              │
│  6. WATCH THE GRADUAL                                                       │
│     Temporal risks (drift, accumulation, decay) kill by stealth             │
│     Sorites watch (#505) is mandatory for comprehensive+ depths             │
│                                                                              │
│  7. LOAD FILES WHEN NEEDED                                                  │
│     Announce: "📂 Loading [path]"                                           │
│     Follow the procedure in the loaded file                                 │
│                                                                              │
│  8. META IS CONTINUOUS                                                      │
│     Apply META methods after each phase, not just at end                    │
│     The process can be wrong; check for bias continuously                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FILE LOADING PROTOCOL

When you need specific data, announce and load:

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-ground.md` | "📂 Loading Step 0: Ground" |
| Start Step 1 | `steps/step-01-identify-vertical.md` | "📂 Loading Step 1: Identify (Vertical)" |
| Start Step 2 | `steps/step-02-identify-horizontal.md` | "📂 Loading Step 2: Identify (Horizontal)" |
| Start Step 3 | `steps/step-03-quantify.md` | "📂 Loading Step 3: Quantify" |
| Start Step 4 | `steps/step-04-interact.md` | "📂 Loading Step 4: Interact" |
| Start Step 5 | `steps/step-05-mitigate.md` | "📂 Loading Step 5: Mitigate" |
| Start Step 6 | `steps/step-06-monitor.md` | "📂 Loading Step 6: Monitor" |
| Start Step 7 | `steps/step-07-output.md` | "📂 Loading Step 7: Output" |
| Execute method | `data/method-procedures/{NNN}_{Name}.md` | "📂 Loading method: #{NNN}" |
| Apply scoring | `data/risk-scoring.yaml` | "📂 Loading risk scoring rules" |
| Check patterns | `data/risk-pattern-libraries/*.yaml` | "📂 Loading risk patterns" |
| Generate register | `data/risk-register-template.md` | "📂 Loading register template" |
| Generate report | `data/risk-report-template.md` | "📂 Loading report template" |
| Generate dashboard | `data/portfolio-dashboard-template.md` | "📂 Loading dashboard template" |
| Apply META | `meta/meta-checklist.yaml` | "📂 Loading META checklist" |

---

## INTEGRATION WITH DEEP-EXPLORE AND DEEP-VERIFY

### From Deep-Explore

| Deep-Explore Output | Feeds Into |
|--------------------|------------|
| Assumption Stress Test (#23) | IDENTIFY #105 Assumption Torture |
| Premortem (#21) | IDENTIFY #102, #106 |
| Dependency Analysis (#13) | IDENTIFY #104 |
| Option Map | GROUND scope definition |
| Consequence Map | QUANTIFY #203 |

### From Deep-Verify

| Deep-Verify Output | Feeds Into |
|-------------------|------------|
| Definitional Contradiction (#154) | IDENTIFY impossible requirements |
| Higher-Order Composition Gap (#166) | IDENTIFY emergent risks |
| Constructive Counterexample (#165) | IDENTIFY attack vectors |
| Ungrounded Claims | IDENTIFY hidden assumptions |

### Integration Protocol

```
IF Deep-Explore was run on same subject:
  □ Load exploration report
  □ Extract assumptions → feed to #105
  □ Extract dependencies → feed to #104
  □ Extract consequences → feed to #203

IF Deep-Verify was run on same subject:
  □ Load verification report
  □ Extract impossibility findings → flag as structural risks
  □ Extract ungrounded claims → flag as assumption risks
```

---

## DIRECTORY STRUCTURE

```
deep-risk/
├── workflow.md                           ← YOU ARE HERE
├── steps/
│   ├── step-00-ground.md                 # GROUND phase procedure
│   ├── step-01-identify-vertical.md      # IDENTIFY vertical extraction
│   ├── step-02-identify-horizontal.md    # IDENTIFY horizontal extraction
│   ├── step-03-quantify.md               # QUANTIFY phase procedure
│   ├── step-04-interact.md               # INTERACT phase procedure
│   ├── step-05-mitigate.md               # MITIGATE phase procedure
│   ├── step-06-monitor.md                # MONITOR phase procedure
│   └── step-07-output.md                 # OUTPUT generation + META summary
├── data/
│   ├── method-procedures/                # 44 method procedure files
│   │   ├── 001_Risk_Genesis_Model.md
│   │   ├── 002_Uncertainty_Classification.md
│   │   ├── 003_System_Characterization.md
│   │   ├── 101_Risk_Taxonomy_Scan.md
│   │   ├── ... (all 44 methods)
│   │   └── 606_Goodharts_Law_Check.md
│   ├── risk-pattern-libraries/           # Domain-specific risk patterns
│   │   ├── _manifest.yaml
│   │   ├── core.yaml
│   │   ├── distributed-systems.yaml
│   │   ├── data-engineering.yaml
│   │   ├── enterprise.yaml
│   │   └── project-management.yaml
│   ├── risk-scoring.yaml                 # 5D scoring rules
│   ├── portfolio-thresholds.yaml         # Portfolio-level thresholds
│   ├── coverage-scoring.yaml             # Process coverage metrics
│   ├── method-selection.yaml             # Which methods for which depth
│   ├── theoretical-foundations.yaml      # 9 foundational theorems
│   ├── risk-register-template.md         # Individual risk entry template
│   ├── risk-report-template.md           # Full assessment report template
│   └── portfolio-dashboard-template.md   # Portfolio summary template
└── meta/
    └── meta-checklist.yaml               # META methods as continuous checklist
```

---

## USAGE GUIDE

### When to Use Deep-Risk

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **New project kickoff** | GROUND → full cycle | comprehensive |
| **Architecture decision** | GROUND → MITIGATE | standard |
| **Pre-release review** | IDENTIFY → MONITOR | standard |
| **Post-incident review** | #504 → targeted phases | targeted |
| **Periodic risk refresh** | QUANTIFY (re-score) | quick |
| **Strategy/business decision** | GROUND → full cycle | comprehensive |
| **Regulatory compliance** | GROUND → full cycle + docs | critical |

### Quick Reference

```
Quick assessment:     GROUND(lite) → IDENTIFY(V) → QUANTIFY(basic) → MITIGATE(4T)
Standard assessment:  GROUND → IDENTIFY(V+H) → QUANTIFY → INTERACT → MITIGATE → MONITOR
Full assessment:      All phases + META continuous + portfolio view
Critical assessment:  Full + chaos probes + external validation + multiple iterations
```

---

## VERSION HISTORY

- **V1.0** — Initial release based on DEEP-RISK-v2.md methodology
