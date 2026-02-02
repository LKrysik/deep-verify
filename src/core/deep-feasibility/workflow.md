# Deep Feasibility V1.0 — Systematic Feasibility Assessment Workflow

---

## INVOCATION

**When user wants to assess feasibility, ALWAYS start with this dialog:**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP FEASIBILITY                                      ║
║                      Systematic Feasibility Assessment                     ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Before we begin, select assessment depth:                                 ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [1] QUICK  (30-60 min)                                             │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Cynefin classification + basic constraint check                  │  ║
║  │  • 10-dimension feasibility profile (basic scoring)                 │  ║
║  │  • Top 3 binding constraints identified                             │  ║
║  │  • Go/No-Go decision with confidence level                          │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Rapid sanity check before deeper analysis                        │  ║
║  │  → Low-stakes decisions                                              │  ║
║  │  → Initial feasibility triage                                        │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [2] STANDARD  (half day)                                           │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Full FRAME phase (Cynefin + decomposition + scope)               │  ║
║  │  • Complete CONSTRAIN (all 6 methods)                               │  ║
║  │  • Full ASSESS (10 dimensions with sub-analysis)                    │  ║
║  │  • Core VALIDATE (reference class + assumption testing)             │  ║
║  │  • Conditional feasibility map                                       │  ║
║  │  • Decay monitoring design                                           │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Important decisions requiring thorough analysis                  │  ║
║  │  → Medium-to-high stakes                                             │  ║
║  │  → Technology or architecture choices                               │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [3] COMPREHENSIVE  (1-2 days)                                      │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in STANDARD                                            │  ║
║  │  • Full VALIDATE with probes and integration spikes                 │  ║
║  │  • Expert judgment calibration                                       │  ║
║  │  • Analogical feasibility transfer                                  │  ║
║  │  • Full META audit (planning fallacy, Dunning-Kruger, etc.)        │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → High-stakes Go/No-Go decisions                                   │  ║
║  │  → New project kickoff                                               │  ║
║  │  → Major investment decisions                                        │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [4] CRITICAL  (multi-day)                                          │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in COMPREHENSIVE                                       │  ║
║  │  • Multiple iteration cycles with feedback loops                    │  ║
║  │  • External validation and research                                 │  ║
║  │  • Stakeholder review integration                                   │  ║
║  │  • Living feasibility dashboard                                     │  ║
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
2. Scan input for complexity signals (see: COMPLEXITY DETECTION)
3. Begin execution from Step 0

---

## COMPLEXITY DETECTION (automatic)

**Do not ask user about complexity mode. Detect automatically from language.**

If description contains:
- "completely new", "never done before", "unprecedented", "first time"
- "emergent", "unpredictable", "can't know in advance", "experimental"
- "many unknowns", "research project", "innovative", "cutting-edge"
- "complex adaptive", "no one has solved", "novel combination"

**→ Enable `complex_mode = on`**

This means:
- Flag Complex-domain sub-problems in FRAME (#001)
- Require Probe Design (#303) for Complex elements
- Adjust confidence ceiling (max = MEDIUM for Complex parts)
- In report: add "Cannot Assess Traditionally" section
- Skip traditional assessment for Complex sub-problems → design probes instead

**If no complexity signals → `complex_mode = off`** (standard assessment)

---

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP FEASIBILITY = CONSTRAINTS + DIMENSIONS + VALIDATION + DECISION        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Project, initiative, plan, technology choice, decision            │
│  OUTPUT:  ACTIONABLE FEASIBILITY INTELLIGENCE                               │
│           • Constraint map (H0-H5: impossible → inconvenient)               │
│           • 10-dimension feasibility profile with binding constraint        │
│           • Conditional feasibility map (feasible IF...)                    │
│           • Calibrated estimates with confidence levels                     │
│           • Decay triggers and monitoring design                            │
│                                                                              │
│  CORE PRINCIPLES:                                                           │
│  1. WEAKEST DIMENSION BINDS — 9/10 feasible + 1/10 infeasible = INFEASIBLE │
│  2. SELF-ASSESSMENT IS BIASED — planning fallacy is systematic, not random │
│  3. FEASIBILITY IS NOT BINARY — spectrum with conditions (IF...)           │
│  4. FEASIBILITY DECAYS — reassessment must be continuous (Boehm Spiral)    │
│  5. COMPLEXITY LIMITS ASSESSMENT — Complex domains require probing, not analysis │
│  6. COMPONENT ≠ SYSTEM — integration is where feasibility estimates fail   │
│  7. CONTRADICTIONS SIGNAL INFEASIBILITY — or innovation opportunity (TRIZ) │
│                                                                              │
│  UNIQUE ERROR TYPE: FALSE FEASIBILITY                                       │
│  Believing something is executable when it is not.                          │
│  Distinct from incorrectness (Verify), risk (Risk), or missing options (Explore). │
│                                                                              │
│  INTEGRATION:                                                               │
│  • Consumes: Deep-Explore options, Deep-Verify impossibilities             │
│  • Produces: Conditions for Deep-Risk, decisions for implementation        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## THEORETICAL FOUNDATIONS

Deep Feasibility is grounded in foundational theorems that constrain what feasibility assessment CAN and CANNOT achieve. Load: `data/theoretical-foundations.yaml`

### Quick Reference

| Principle | One-Line Summary | Applied In |
|-----------|------------------|------------|
| **Turing / Halting (1936)** | Some problems are provably undecidable | #101 (H5 constraints) |
| **Cook-Karp / NP (1971)** | Even decidable may be practically infeasible | #101 (H4 constraints) |
| **Gödel (1931)** | System cannot fully assess its own feasibility | #301, #505 |
| **Goldratt / TOC (1984)** | Throughput limited by single tightest constraint | #401 (binding constraint) |
| **Ashby / Requisite Variety (1956)** | Controller must match system complexity | #102 |
| **Brooks (1975)** | Adding people to late project makes it later | #202, #205 |
| **Conway (1968)** | Orgs produce systems mirroring communication | #104 |
| **Simon / Bounded Rationality (1955)** | Humans satisfice, don't optimize | #505 |
| **Kahneman / Planning Fallacy (1979)** | Systematic underestimation of time/cost | #501 |
| **Flyvbjerg / Reference Class (2006)** | External base rates beat internal estimates | #301 |
| **Hofstadter's Law** | Takes longer even accounting for this law | #502 |
| **Snowden / Cynefin (2007)** | Assessment method depends on problem type | #001 |
| **Altshuller / TRIZ (1946-85)** | Contradictions signal infeasibility or innovation | #103 |
| **NASA / TRL** | System feasibility = min(component TRLs) | #201 |
| **Boehm / Spiral (1986)** | Iterative feasibility reassessment | #404 |

---

## DEPTH LEVELS — What executes at each level

### QUICK (depth = quick)

```
PHASES:          FRAME(lite) → CONSTRAIN(core) → ASSESS(all 10 basic) → DECIDE(core)
METHODS:         001-003 + 101,102,106 + 201-210(basic) + 401,402 + 501
MAX ITERATIONS:  1 (no feedback loops)
DIMENSIONS:      10 (basic 1-5 scoring)
COVERAGE TARGET: C ≥ 15
```

### STANDARD (depth = standard)

```
PHASES:          FRAME → CONSTRAIN → ASSESS → VALIDATE(core) → DECIDE → META(core)
METHODS:         All FRAME + All CONSTRAIN + All ASSESS + 301,302,304 + All DECIDE + 501-503
MAX ITERATIONS:  3
DIMENSIONS:      10 (full sub-analysis)
COVERAGE TARGET: C ≥ 35
```

### COMPREHENSIVE (depth = comprehensive)

```
PHASES:          FRAME → CONSTRAIN → ASSESS → VALIDATE(full) → DECIDE → META(full)
METHODS:         All methods except multi-iteration external validation
MAX ITERATIONS:  5
DIMENSIONS:      10 + integration analysis
COVERAGE TARGET: C ≥ 50
```

### CRITICAL (depth = critical)

```
PHASES:          All phases, full execution
METHODS:         All 35 methods
MAX ITERATIONS:  Unlimited
DIMENSIONS:      Exhaustive + external validation
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
│  FRAME  │    │CONSTRAIN│    │ ASSESS  │    │VALIDATE │     │
└─────────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
                    │              │              │           │
                    └──────────────┴──────────────┘           │
                                        │                     │
                              ┌─────────┐    ┌─────────┐     │
                              │ STEP 4  │───►│ STEP 5  │◄────┘
                              │ DECIDE  │    │ OUTPUT  │
                              └─────────┘    └─────────┘
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
📂 Step 0: FRAME
   Load: steps/step-00-frame.md

   □ Define what is being assessed
   □ 📂 #001 → Cynefin Domain Classification
   □ 📂 #002 → Feasibility Question Decomposition
   □ 📂 #003 → Feasibility Scope Definition

   IF complex_mode = on:
   → Flag Complex sub-problems
   → Note: "Traditional assessment not possible for these — probes required"

   Output: Problem Characterization, Sub-questions, Scope, Domain Map

   ↓ PROCEED when problem is characterized
   ↓ STAY if scope unclear

📂 Step 1: CONSTRAIN
   Load: steps/step-01-constrain.md

   □ 📂 #101 → Constraint Hardness Spectrum (H0-H5)
   □ 📂 #102 → Requisite Variety Audit (Ashby)
   □ 📂 #103 → TRIZ Contradiction Detection
   □ 📂 #104 → Conway Alignment Check
   □ 📂 #105 → Regulatory Feasibility Scan
   □ 📂 #106 → Precedent Existence Check

   DEPTH ADJUSTMENT:
   • quick: #101, #102, #106 only
   • standard+: all constraint methods

   EARLY EXIT CONDITIONS:
   → H5 (impossible) found → STOP analysis on that path, recommend redesign
   → Unresolved physical contradiction → infeasible as stated

   Output: Constraint Map, Impossibility Flags, Contradiction List

   ↓ PROCEED to dimension assessment
   ↑ RETURN TO STEP 0 if scope needs refinement

📂 Step 2: ASSESS
   Load: steps/step-02-assess.md

   □ 📂 #201 → Technical Feasibility (TRL Analysis)
   □ 📂 #202 → Resource Feasibility
   □ 📂 #203 → Knowledge Feasibility
   □ 📂 #204 → Organizational Feasibility
   □ 📂 #205 → Temporal Feasibility (Critical Path)
   □ 📂 #206 → Compositional Feasibility
   □ 📂 #207 → Economic Feasibility
   □ 📂 #208 → Scale Feasibility
   □ 📂 #209 → Cognitive Feasibility
   □ 📂 #210 → Dependency Feasibility

   DEPTH ADJUSTMENT:
   • quick: basic 1-5 scoring for all 10
   • standard+: full analysis with sub-factors

   BINDING CONSTRAINT = min(dimension scores)

   Output: 10-Dimension Feasibility Profile, Binding Constraint Identified

   ↓ PROCEED to validation
   ↑ RETURN TO STEP 1 if new constraints discovered

📂 Step 3: VALIDATE
   Load: steps/step-03-validate.md

   □ 📂 #301 → Reference Class Forecasting (Flyvbjerg)
   □ 📂 #302 → Critical Assumption Testing
   □ 📂 #303 → Probe Design (Complex Domain) [if complex_mode=on or comprehensive+]
   □ 📂 #304 → Expert Judgment Calibration
   □ 📂 #305 → Analogical Feasibility Transfer
   □ 📂 #306 → Integration Spike [comprehensive+ only]

   DEPTH ADJUSTMENT:
   • quick: skip entirely
   • standard: #301, #302, #304
   • comprehensive+: all validation methods

   Output: Calibrated Estimates, Probe Results, Validated/Refuted Assumptions

   ↓ PROCEED to decision
   ↑ RETURN if validation reveals new constraints

📂 Step 4: DECIDE
   Load: steps/step-04-decide.md

   □ 📂 #401 → Multi-Axis Feasibility Profile (visual)
   □ 📂 #402 → Confidence-Weighted Decision
   □ 📂 #403 → Conditional Feasibility Map
   □ 📂 #404 → Feasibility Decay Monitoring

   DEPTH ADJUSTMENT:
   • quick: #401, #402 only
   • standard+: all decision methods

   Output: Decision (GO/NO-GO/CONDITIONAL/INVESTIGATE), Conditions, Triggers

   ↓ PROCEED to output

📂 Step 5: OUTPUT
   Load: steps/step-05-output.md

   □ Apply META methods (#501-505) as final audit
   □ Generate Feasibility Register Entry
   □ Generate Feasibility Report

   Load templates:
   • data/feasibility-register-template.md
   • data/feasibility-report-template.md

   Output: FEASIBILITY ASSESSMENT DELIVERABLES
```

---

## META METHODS (Continuous)

META methods (#501-505) govern the feasibility assessment process itself. Apply after each phase completion:

| # | Method | Purpose | When to Apply |
|---|--------|---------|---------------|
| 501 | Planning Fallacy Detection | Check for systematic optimism | After ASSESS, before DECIDE |
| 502 | Hofstadter Correction | Recursive estimation adjustment | After all estimates |
| 503 | Confidence Theater Detection | Genuine vs performed confidence | After DECIDE |
| 504 | Dunning-Kruger Dimension Map | Low expertise + high confidence zones | After ASSESS |
| 505 | Meta-Feasibility Check | Can we even assess this? | During FRAME, after VALIDATE |

Load: `meta/meta-checklist.yaml`

---

## SCORING SYSTEMS

### Process Coverage Score (C)

Measures how thoroughly the assessment was conducted:

| Activity | Points |
|----------|--------|
| Phase completed | +3 |
| Method executed | +1 |
| Dimension scored | +1 |
| Constraint classified (H0-H5) | +0.5 |
| Condition mapped | +0.5 |
| Assumption tested | +1 |
| Probe designed | +1.5 |
| META method applied | +0.5 |

Load: `data/coverage-scoring.yaml`

### Dimension Feasibility Score (1-5)

Each of 10 dimensions scored:

| Score | Label | Meaning |
|-------|-------|---------|
| 5 | **Proven** | Demonstrated, precedented, no significant challenges |
| 4 | **Likely** | Strong evidence of feasibility, minor concerns |
| 3 | **Possible** | Feasible but significant challenges / uncertainties |
| 2 | **Doubtful** | Major challenges, may require fundamental changes |
| 1 | **Infeasible** | Cannot be done under current constraints |

**BINDING CONSTRAINT = min(dimension scores)** (Goldratt)

**Confidence Levels:**
- **High:** Based on empirical evidence (probes, spikes, reference class)
- **Medium:** Based on expert judgment (calibrated) and analogies
- **Low:** Based on team gut feeling and planning (uncalibrated)

Load: `data/feasibility-scoring.yaml`

### Decision Thresholds

| Overall Score | Confidence | Decision |
|---------------|------------|----------|
| 4-5 | High | **GO** — proceed with standard management |
| 4-5 | Low | **CONDITIONAL GO** — invest in validation |
| 3 | High | **CONDITIONAL GO** — explicit conditions and checkpoints |
| 3 | Low | **INVESTIGATE** — more information needed |
| 1-2 | High | **NO GO** — stop, redirect, or redesign |
| 1-2 | Low | **INVESTIGATE or NO GO** — may be infeasible, may be unknown |

Load: `data/decision-thresholds.yaml`

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FEASIBILITY ASSESSMENT COMMANDMENTS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. ALWAYS START WITH INVOCATION                                            │
│     Display the depth selection dialog before doing anything                │
│     Wait for user choice before proceeding                                  │
│                                                                              │
│  2. CLASSIFY BEFORE ASSESSING                                               │
│     Cynefin domain classification (#001) determines assessment method       │
│     Complex problems CANNOT be assessed traditionally — must probe          │
│                                                                              │
│  3. WEAKEST BINDS                                                           │
│     Overall feasibility = min(dimension scores) (Goldratt)                  │
│     Don't average — identify and address the binding constraint             │
│                                                                              │
│  4. APPLY DEBIASING                                                         │
│     Reference class forecasting (#301) is MANDATORY for standard+ depths    │
│     Hofstadter correction (#502) always applies at the end                  │
│                                                                              │
│  5. CONDITIONS ARE EXPLICIT                                                 │
│     "Feasible IF..." must enumerate ALL conditions (#403)                   │
│     Calculate compound probability of all conditions holding                │
│                                                                              │
│  6. DECAY IS CONTINUOUS                                                     │
│     Feasibility assessment decays — design monitoring triggers (#404)       │
│     Reassess at project milestones (Boehm's Spiral)                         │
│                                                                              │
│  7. LOAD FILES WHEN NEEDED                                                  │
│     Announce: "📂 Loading [path]"                                           │
│     Follow the procedure in the loaded file                                 │
│                                                                              │
│  8. META IS CONTINUOUS                                                      │
│     Apply META methods after each phase, not just at end                    │
│     Check for planning fallacy, confidence theater, Dunning-Kruger          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FILE LOADING PROTOCOL

When you need specific data, announce and load:

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-frame.md` | "📂 Loading Step 0: Frame" |
| Start Step 1 | `steps/step-01-constrain.md` | "📂 Loading Step 1: Constrain" |
| Start Step 2 | `steps/step-02-assess.md` | "📂 Loading Step 2: Assess" |
| Start Step 3 | `steps/step-03-validate.md` | "📂 Loading Step 3: Validate" |
| Start Step 4 | `steps/step-04-decide.md` | "📂 Loading Step 4: Decide" |
| Start Step 5 | `steps/step-05-output.md` | "📂 Loading Step 5: Output" |
| Execute method | `data/method-procedures/{NNN}_{Name}.md` | "📂 Loading method #{NNN}" |
| Apply scoring | `data/feasibility-scoring.yaml` | "📂 Loading feasibility scoring" |
| Check thresholds | `data/decision-thresholds.yaml` | "📂 Loading decision thresholds" |
| Load patterns | `data/constraint-patterns.yaml` | "📂 Loading constraint patterns" |
| Generate register | `data/feasibility-register-template.md` | "📂 Loading register template" |
| Generate report | `data/feasibility-report-template.md` | "📂 Loading report template" |
| Apply META | `meta/meta-checklist.yaml` | "📂 Loading META checklist" |

---

## INTEGRATION WITH DEEP-EXPLORE AND DEEP-VERIFY

### From Deep-Explore

| Deep-Explore Output | Feeds Into |
|--------------------|------------|
| Options identified | Feasibility assessment for each option |
| Assumptions surfaced (E001) | #302 Critical Assumption Testing |
| Constraints mapped (M003) | #101 Constraint Hardness Spectrum |
| Consequence map (M011) | #207 Economic Feasibility |
| Knowledge gaps | #203 Knowledge Feasibility |
| Dependencies (E005) | #210 Dependency Feasibility |

### From Deep-Verify

| Deep-Verify Output | Feeds Into |
|-------------------|------------|
| Impossibility findings (DC-*, TV-*) | Automatic H5 constraints (#101) |
| Definitional contradictions | #103 TRIZ Contradiction inputs |
| Validated requirements | Scope for feasibility assessment (#003) |
| Ungrounded claims | Assumptions to test (#302) |
| Pattern matches | Constraint pattern evidence |

### To Deep-Risk

| Deep-Feasibility Output | Feeds Into |
|------------------------|------------|
| Feasibility conditions (#403) | Risk triggers for Deep-Risk monitoring |
| Low-confidence dimensions | Knight-Uncertainty risks |
| Binding constraints | Structural risk seeds |
| Decay triggers (#404) | Monitoring system design |
| Non-ergodic flags | Existential risk identification |

### Integration Protocol

```
IF Deep-Explore was run on same subject:
  □ Load exploration report
  □ Extract options → assess feasibility of each
  □ Extract assumptions → feed to #302
  □ Extract constraints → feed to #101
  □ Extract dependencies → feed to #210

IF Deep-Verify was run on same subject:
  □ Load verification report
  □ Extract impossibility findings → flag as H5 constraints (#101)
  □ Extract contradictions → feed to #103
  □ Extract ungrounded claims → assumptions to test (#302)

AFTER Deep-Feasibility:
  □ Hand off conditions → triggers for Deep-Risk
  □ Hand off low-confidence → uncertainty analysis
  □ Hand off decay triggers → monitoring design
```

---

## DIRECTORY STRUCTURE

```
deep-feasibility/
├── workflow.md                           ← YOU ARE HERE
├── steps/
│   ├── step-00-frame.md                  # FRAME phase procedure
│   ├── step-01-constrain.md              # CONSTRAIN phase procedure
│   ├── step-02-assess.md                 # ASSESS phase procedure
│   ├── step-03-validate.md               # VALIDATE phase procedure
│   ├── step-04-decide.md                 # DECIDE phase procedure
│   └── step-05-output.md                 # OUTPUT generation
├── data/
│   ├── method-procedures/                # 35 method procedure files
│   │   ├── 001_Cynefin_Domain_Classification.md
│   │   ├── 002_Feasibility_Question_Decomposition.md
│   │   ├── 003_Feasibility_Scope_Definition.md
│   │   ├── 101_Constraint_Hardness_Spectrum.md
│   │   ├── ... (all 35 methods)
│   │   └── 505_Meta_Feasibility_Check.md
│   ├── theoretical-foundations.yaml      # 16 foundational theorems
│   ├── feasibility-scoring.yaml          # Dimension scoring rules
│   ├── coverage-scoring.yaml             # Process coverage metrics
│   ├── decision-thresholds.yaml          # Go/No-Go thresholds
│   ├── constraint-patterns.yaml          # Known constraint patterns
│   ├── feasibility-register-template.md  # Individual entry template
│   └── feasibility-report-template.md    # Full assessment report
└── meta/
    └── meta-checklist.yaml               # META methods as continuous checklist
```

---

## USAGE GUIDE

### When to Use Deep-Feasibility

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **Go/No-Go decision** | FRAME → full cycle | comprehensive |
| **New project kickoff** | FRAME → full cycle | standard |
| **Technology choice** | CONSTRAIN → ASSESS (Technical, Scale) | focused |
| **Make vs buy** | ASSESS (Resource, Knowledge, Temporal, Economic) | focused |
| **Scope change** | ASSESS (affected dimensions) → DECIDE | reassessment |
| **Milestone checkpoint** | ASSESS (re-score) → DECIDE | Boehm spiral |
| **Post-failure analysis** | META (what did we miss?) → full reassessment | retrospective |

### Quick Reference

```
Quick assessment:     FRAME(lite) → CONSTRAIN(core) → ASSESS(basic) → DECIDE(core)
Standard assessment:  FRAME → CONSTRAIN → ASSESS → VALIDATE(core) → DECIDE → META
Full assessment:      All phases + full VALIDATE + full META
Critical assessment:  Full + probes + spikes + external validation + iterations
```

---

## VERSION HISTORY

- **V1.0** — Initial release based on DEEP-FEASIBILITY.md methodology
