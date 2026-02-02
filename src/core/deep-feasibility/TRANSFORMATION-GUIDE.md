# Transformation Guide: Converting DEEP-FEASIBILITY.md to Process Structure

## Overview

This document provides a comprehensive knowledge base for transforming DEEP-FEASIBILITY.md into a full process structure consistent with Deep-Verify, Deep-Risk, and Deep-Explore.

---

## Part 1: Target Directory Structure

Based on the three existing processes, Deep-Feasibility should have this structure:

```
deep-feasibility/
├── workflow.md                           ← Main entry point (TO CREATE)
├── steps/
│   ├── step-00-frame.md                  # FRAME phase (methods 001-003)
│   ├── step-01-constrain.md              # CONSTRAIN phase (methods 101-106)
│   ├── step-02-assess.md                 # ASSESS phase (methods 201-210)
│   ├── step-03-validate.md               # VALIDATE phase (methods 301-306)
│   ├── step-04-decide.md                 # DECIDE phase (methods 401-404)
│   └── step-05-output.md                 # OUTPUT generation
├── data/
│   ├── method-procedures/                # 35 method files
│   │   ├── 001_Cynefin_Domain_Classification.md
│   │   ├── 002_Feasibility_Question_Decomposition.md
│   │   ├── 003_Feasibility_Scope_Definition.md
│   │   ├── 101_Constraint_Hardness_Spectrum.md
│   │   ├── 102_Requisite_Variety_Audit.md
│   │   ├── 103_TRIZ_Contradiction_Detection.md
│   │   ├── 104_Conway_Alignment_Check.md
│   │   ├── 105_Regulatory_Feasibility_Scan.md
│   │   ├── 106_Precedent_Existence_Check.md
│   │   ├── 201_Technical_Feasibility_TRL.md
│   │   ├── 202_Resource_Feasibility.md
│   │   ├── 203_Knowledge_Feasibility.md
│   │   ├── 204_Organizational_Feasibility.md
│   │   ├── 205_Temporal_Feasibility.md
│   │   ├── 206_Compositional_Feasibility.md
│   │   ├── 207_Economic_Feasibility.md
│   │   ├── 208_Scale_Feasibility.md
│   │   ├── 209_Cognitive_Feasibility.md
│   │   ├── 210_Dependency_Feasibility.md
│   │   ├── 301_Reference_Class_Forecasting.md
│   │   ├── 302_Critical_Assumption_Testing.md
│   │   ├── 303_Probe_Design.md
│   │   ├── 304_Expert_Judgment_Calibration.md
│   │   ├── 305_Analogical_Feasibility_Transfer.md
│   │   ├── 306_Integration_Spike.md
│   │   ├── 401_Multi_Axis_Feasibility_Profile.md
│   │   ├── 402_Confidence_Weighted_Decision.md
│   │   ├── 403_Conditional_Feasibility_Map.md
│   │   ├── 404_Feasibility_Decay_Monitoring.md
│   │   ├── 501_Planning_Fallacy_Detection.md
│   │   ├── 502_Hofstadter_Correction.md
│   │   ├── 503_Confidence_Theater_Detection.md
│   │   ├── 504_Dunning_Kruger_Dimension_Map.md
│   │   └── 505_Meta_Feasibility_Check.md
│   ├── feasibility-scoring.yaml          # Dimension scoring (1-5 scale)
│   ├── coverage-scoring.yaml             # Process coverage metrics
│   ├── decision-thresholds.yaml          # Go/No-Go thresholds
│   ├── theoretical-foundations.yaml      # 16 theoretical principles
│   ├── feasibility-register-template.md  # Individual entry template
│   ├── feasibility-report-template.md    # Full report template
│   └── constraint-pattern-library.yaml   # Known constraint patterns
└── meta/
    └── meta-checklist.yaml               # META methods as continuous checklist
```

---

## Part 2: Workflow.md Template

The main workflow.md file should follow this structure (extracted pattern):

### 2.1 INVOCATION Section

```markdown
## INVOCATION

**When user wants to assess feasibility, ALWAYS start with this dialog:**

╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP FEASIBILITY                                      ║
║                      Systematic Feasibility Assessment                     ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Before we begin, select assessment depth:                                 ║
║                                                                            ║
║  [1] QUICK  (30-60 min)                                                   ║
║      • Cynefin classification + basic constraint check                     ║
║      • Top 3 binding constraints identified                                ║
║      • Quick feasibility profile (10 dimensions)                           ║
║      • Go/No-Go with confidence level                                      ║
║      When: Rapid sanity check, low-stakes decisions                        ║
║                                                                            ║
║  [2] STANDARD  (half day)                                                  ║
║      • Full FRAME + CONSTRAIN + ASSESS                                     ║
║      • Reference class forecasting                                         ║
║      • Conditional feasibility map                                         ║
║      • Decay monitoring design                                             ║
║      When: Important decisions, medium-to-high stakes                      ║
║                                                                            ║
║  [3] COMPREHENSIVE  (1-2 days)                                             ║
║      • Everything in STANDARD                                              ║
║      • Full VALIDATE with probes and spikes                                ║
║      • Expert judgment calibration                                         ║
║      • Full META audit                                                     ║
║      When: High-stakes, Go/No-Go decisions                                 ║
║                                                                            ║
║  [4] CRITICAL  (multi-day)                                                 ║
║      • Everything in COMPREHENSIVE                                         ║
║      • Multiple iteration cycles                                           ║
║      • External validation                                                 ║
║      • Stakeholder review integration                                      ║
║      When: Critical, irreversible decisions                                ║
║                                                                            ║
║  Select: [1] / [2] / [3] / [4]                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### 2.2 AUTO-DETECTION Section

Pattern from Deep-Risk (crisis) and Deep-Explore (fear):

```markdown
## COMPLEXITY DETECTION (automatic)

**Do not ask user about complexity mode. Detect automatically from language.**

If description contains:
- "completely new", "never done before", "unprecedented"
- "emergent", "unpredictable", "can't know in advance"
- "many unknowns", "experimental", "research"

**→ Enable `complex_mode = on`**

This means:
- Flag Complex-domain sub-problems in FRAME
- Require Probe Design (#303) for Complex elements
- Adjust confidence levels (lower ceiling)
- In report: add "Cannot Assess Traditionally" section

**If no complexity signals → `complex_mode = off`** (standard assessment)
```

### 2.3 CORE PHILOSOPHY Box

```markdown
## CORE PHILOSOPHY

┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP FEASIBILITY = CONSTRAINTS + DIMENSIONS + VALIDATION + DECISION        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Project, initiative, plan, technology choice, decision            │
│  OUTPUT:  ACTIONABLE FEASIBILITY INTELLIGENCE                               │
│           • Constraint map (hard vs soft limits)                            │
│           • 10-dimension feasibility profile                                │
│           • Conditional feasibility (feasible IF...)                        │
│           • Calibrated estimates with confidence                            │
│           • Decay triggers and monitoring                                   │
│                                                                              │
│  CORE PRINCIPLES:                                                           │
│  1. WEAKEST DIMENSION BINDS — feasible on 9/10 but infeasible on 1 = NO   │
│  2. SELF-ASSESSMENT IS BIASED — planning fallacy is systematic, not random │
│  3. FEASIBILITY IS NOT BINARY — it's a spectrum with conditions            │
│  4. FEASIBILITY DECAYS — reassessment must be continuous                   │
│  5. COMPLEXITY LIMITS ASSESSMENT — some things can only be probed          │
│  6. COMPONENT ≠ SYSTEM — integration is where estimates fail               │
│                                                                              │
│  UNIQUE ERROR: FALSE FEASIBILITY — believing executable when not           │
│                                                                              │
│  INTEGRATION: Consumes outputs from Deep-Explore and Deep-Verify           │
│               Feeds into Deep-Risk for risk-adjusted feasibility           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.4 DEPTH LEVELS Section

```markdown
## DEPTH LEVELS — What executes at each level

### QUICK (depth = quick)

PHASES:          FRAME(lite) → CONSTRAIN(core) → ASSESS(all 10) → DECIDE
METHODS:         001-003 + 101,102,106 + 201-210(basic) + 401,402 + 501
MAX ITERATIONS:  1 (no feedback loops)
COVERAGE TARGET: C ≥ 15

### STANDARD (depth = standard)

PHASES:          FRAME → CONSTRAIN → ASSESS → VALIDATE(core) → DECIDE
METHODS:         All FRAME + All CONSTRAIN + All ASSESS + 301,302,304 + All DECIDE + 501-503
MAX ITERATIONS:  3
COVERAGE TARGET: C ≥ 35

### COMPREHENSIVE (depth = comprehensive)

PHASES:          FRAME → CONSTRAIN → ASSESS → VALIDATE(full) → DECIDE → META
METHODS:         All methods except multi-iteration
MAX ITERATIONS:  5
COVERAGE TARGET: C ≥ 50

### CRITICAL (depth = critical)

PHASES:          All phases, full execution
METHODS:         All 35 methods
MAX ITERATIONS:  Unlimited
COVERAGE TARGET: C ≥ 65
```

### 2.5 EXECUTION FLOW Diagram

```markdown
## EXECUTION FLOW

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

### 2.6 EXECUTION PATH (Detailed)

```markdown
## EXECUTION PATH

📂 Step 0: FRAME
   Load: steps/step-00-frame.md

   □ Define assessment scope (#003)
   □ 📂 #001 → Cynefin Domain Classification
   □ 📂 #002 → Feasibility Question Decomposition
   □ 📂 #003 → Feasibility Scope Definition

   IF complex_mode = on:
   → Flag Complex sub-problems for probing
   → Acknowledge "traditional assessment not possible" for those

   Output: Problem Characterization, Assessment Strategy, Sub-questions

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

   IF H5 (impossible) found:
   → EARLY EXIT possible for that path
   → Recommend redesign or reframe

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
   • quick: basic scoring (1-5) for all 10
   • standard+: full analysis with sub-components

   Output: 10-Dimension Feasibility Profile, Binding Constraint Identified

   ↓ PROCEED to validation
   ↑ RETURN TO STEP 1 if new constraints discovered

📂 Step 3: VALIDATE
   Load: steps/step-03-validate.md

   □ 📂 #301 → Reference Class Forecasting (Flyvbjerg)
   □ 📂 #302 → Critical Assumption Testing
   □ 📂 #303 → Probe Design (Complex Domain) [if complex_mode=on]
   □ 📂 #304 → Expert Judgment Calibration
   □ 📂 #305 → Analogical Feasibility Transfer
   □ 📂 #306 → Integration Spike [comprehensive+]

   DEPTH ADJUSTMENT:
   • quick: skip entirely
   • standard: #301, #302, #304
   • comprehensive+: all

   Output: Calibrated Estimates, Probe Results, Validated Assumptions

   ↓ PROCEED to decision
   ↑ RETURN if validation reveals new constraints

📂 Step 4: DECIDE
   Load: steps/step-04-decide.md

   □ 📂 #401 → Multi-Axis Feasibility Profile
   □ 📂 #402 → Confidence-Weighted Decision
   □ 📂 #403 → Conditional Feasibility Map
   □ 📂 #404 → Feasibility Decay Monitoring

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

### 2.7 SCORING SYSTEM

```markdown
## SCORING SYSTEMS

### Process Coverage Score (C)

| Activity | Points |
|----------|--------|
| Phase completed | +3 |
| Method executed | +1 |
| Dimension scored | +1 |
| Constraint classified | +0.5 |
| Condition mapped | +0.5 |
| Probe designed | +1.5 |
| META method applied | +0.5 |

Load: `data/coverage-scoring.yaml`

### Dimension Feasibility Score (1-5)

Each of 10 dimensions scored on:

| Score | Label | Meaning |
|-------|-------|---------|
| 5 | **Proven** | Demonstrated, precedented, no significant challenges |
| 4 | **Likely** | Strong evidence of feasibility, minor concerns |
| 3 | **Possible** | Feasible but significant challenges / uncertainties |
| 2 | **Doubtful** | Major challenges, may require fundamental changes |
| 1 | **Infeasible** | Cannot be done under current constraints |

**BINDING CONSTRAINT = min(dimension scores)**

Load: `data/feasibility-scoring.yaml`

### Decision Thresholds

| Overall | Confidence | Decision |
|---------|------------|----------|
| 4-5 | High | **GO** |
| 4-5 | Low | **CONDITIONAL GO** — invest in validation |
| 3 | High | **CONDITIONAL GO** — with explicit conditions |
| 3 | Low | **INVESTIGATE** — more information needed |
| 1-2 | High | **NO GO** — stop, redirect, redesign |
| 1-2 | Low | **INVESTIGATE or NO GO** |

Load: `data/decision-thresholds.yaml`
```

### 2.8 CRITICAL RULES Box

```markdown
## CRITICAL RULES

┌─────────────────────────────────────────────────────────────────────────────┐
│  FEASIBILITY ASSESSMENT COMMANDMENTS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. ALWAYS START WITH INVOCATION                                            │
│     Display the depth selection dialog before doing anything                │
│     Wait for user choice before proceeding                                  │
│                                                                              │
│  2. CLASSIFY BEFORE ASSESSING                                               │
│     Cynefin domain classification determines assessment method              │
│     Complex problems CANNOT be assessed traditionally — must probe          │
│                                                                              │
│  3. WEAKEST BINDS                                                           │
│     Overall feasibility = min(dimension scores) (Goldratt)                  │
│     Don't average — identify the binding constraint                         │
│                                                                              │
│  4. APPLY DEBIASING                                                         │
│     Reference class forecasting is MANDATORY for standard+ depths           │
│     Hofstadter correction always applies at the end                         │
│                                                                              │
│  5. CONDITIONS ARE EXPLICIT                                                 │
│     "Feasible IF..." must enumerate ALL conditions                          │
│     Calculate compound probability of conditions holding                    │
│                                                                              │
│  6. DECAY IS CONTINUOUS                                                     │
│     Feasibility assessment decays — design monitoring triggers              │
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

### 2.9 FILE LOADING PROTOCOL

```markdown
## FILE LOADING PROTOCOL

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-frame.md` | "📂 Loading Step 0: Frame" |
| Start Step 1 | `steps/step-01-constrain.md` | "📂 Loading Step 1: Constrain" |
| Start Step 2 | `steps/step-02-assess.md` | "📂 Loading Step 2: Assess" |
| Start Step 3 | `steps/step-03-validate.md` | "📂 Loading Step 3: Validate" |
| Start Step 4 | `steps/step-04-decide.md` | "📂 Loading Step 4: Decide" |
| Start Step 5 | `steps/step-05-output.md` | "📂 Loading Step 5: Output" |
| Execute method | `data/method-procedures/{NNN}_{Name}.md` | "📂 Loading method: #{NNN}" |
| Apply scoring | `data/feasibility-scoring.yaml` | "📂 Loading feasibility scoring" |
| Check patterns | `data/constraint-pattern-library.yaml` | "📂 Loading constraint patterns" |
| Generate register | `data/feasibility-register-template.md` | "📂 Loading register template" |
| Generate report | `data/feasibility-report-template.md` | "📂 Loading report template" |
| Apply META | `meta/meta-checklist.yaml` | "📂 Loading META checklist" |
```

### 2.10 INTEGRATION Section

```markdown
## INTEGRATION WITH OTHER DEEP PROCESSES

### From Deep-Explore

| Deep-Explore Output | Feeds Into |
|--------------------|------------|
| Options identified | Feasibility assessment for each option |
| Assumptions identified | #302 Critical Assumption Testing |
| Constraints mapped | #101 Constraint Hardness Spectrum |
| Consequence map | #207 Economic Feasibility |
| Knowledge gaps | #203 Knowledge Feasibility |

### From Deep-Verify

| Deep-Verify Output | Feeds Into |
|-------------------|------------|
| Impossibility findings (DC-*, TV-*) | Automatic H5 constraints (#101) |
| Definitional contradictions | #103 TRIZ Contradiction inputs |
| Validated requirements | Scope for feasibility assessment (#003) |
| Ungrounded claims | Assumptions to test (#302) |

### To Deep-Risk

| Deep-Feasibility Output | Feeds Into |
|------------------------|------------|
| Feasibility conditions (#403) | Risk triggers for Deep-Risk |
| Low-confidence dimensions | Knight-Uncertainty risks |
| Binding constraints | Structural risk seeds |
| Decay triggers (#404) | Monitoring system design |

### Integration Protocol

IF Deep-Explore was run on same subject:
  □ Load exploration report
  □ Extract options → assess each for feasibility
  □ Extract assumptions → feed to #302
  □ Extract constraints → feed to #101

IF Deep-Verify was run on same subject:
  □ Load verification report
  □ Extract impossibility findings → flag as H5 constraints
  □ Extract contradictions → feed to #103

AFTER Deep-Feasibility:
  □ Conditional feasibility → triggers for Deep-Risk
  □ Low-confidence assessments → uncertainty analysis
```

---

## Part 3: Step File Format

Each step file should follow this frontmatter pattern (from step-00-setup.md):

```yaml
---
step: 0
name: "Frame"
time_estimate: "15-30 minutes"
goal: "Classify problem type and define assessment scope"
requires_completion: []
next_steps:
  DEFAULT: "steps/step-01-constrain.md"
  H5_FOUND: "EARLY_EXIT or REDESIGN"
data_dependencies:
  - "data/feasibility-scoring.yaml"
  - "data/constraint-pattern-library.yaml"
outputs:
  - cynefin_domain
  - sub_questions
  - scope
  - complex_mode_flag
---
```

### Step File Body Structure

```markdown
# Phase X: [Name]

## MANDATORY EXECUTION RULES

1. **LOAD DATA FIRST** — Read dependencies before proceeding
2. **Complete all methods** — Do not skip unless depth adjustment allows
3. **Record outputs** — All outputs go to working document
4. **Check for feedback** — Return conditions trigger re-assessment

---

## X.1 [First Method Group]

**Load:** `data/method-procedures/NNN_Name.md`

[Method execution instructions]

→ **HALT** — Wait for user input if needed

---

## X.2 [Second Method Group]

[Continue pattern...]

---

## Output Checklist

Before proceeding, confirm:
- [ ] All required methods executed
- [ ] Outputs recorded
- [ ] Depth adjustments applied
- [ ] Ready to load next step
```

---

## Part 4: Method Procedure Format

Each method file should follow this pattern (from 071_First_Principles_Analysis.md):

```markdown
# #NNN [Method Name]

**Phase:** X ([Phase Name])
**Tier:** [1/2/3] — [Mandatory/Conditional/Optional]
**Purpose:** [One-line description]

## Theoretical Foundation

[Reference to DEEP-FEASIBILITY.md theoretical section if applicable]

## What to do

1. [High-level step 1]
2. [High-level step 2]
3. [High-level step 3]

## Step-by-step

1. [Detailed instruction]
   - [Sub-instruction]
   - [Sub-instruction]

2. [Detailed instruction]
   □ [Checklist item]
   □ [Checklist item]

3. [Detailed instruction]

## Output format

[Dimension/Aspect]: [Score/Rating/Classification]
  Evidence: [supporting information]
  Confidence: [H/M/L]
  Notes: [additional context]

## Integration Points

- Feeds from: [Other methods that provide input]
- Feeds to: [Other methods that use this output]

## Common Pitfalls

- [Pitfall 1]: [How to avoid]
- [Pitfall 2]: [How to avoid]
```

---

## Part 5: Data File Formats

### 5.1 Scoring YAML (from risk-scoring.yaml pattern)

```yaml
# Feasibility Scoring System — 10-Dimension Assessment
# LOAD: step-02-assess.md
# PURPOSE: Consistent scoring across all dimensions

---
# LOADING INSTRUCTIONS:
# 1. Load this file at the START of ASSESS phase
# 2. Apply dimension_scores for each dimension
# 3. Identify binding constraint (min score)
# 4. Apply confidence level

---
dimension_scale:
  5:
    label: "Proven"
    description: "Demonstrated, precedented, no significant challenges"
  4:
    label: "Likely"
    description: "Strong evidence of feasibility, minor concerns"
  3:
    label: "Possible"
    description: "Feasible but significant challenges / uncertainties"
  2:
    label: "Doubtful"
    description: "Major challenges, may require fundamental changes"
  1:
    label: "Infeasible"
    description: "Cannot be done under current constraints"

---
dimensions:
  technical:
    number: 201
    question: "Does the required technology exist, work, and scale?"
    sub_factors:
      - TRL level
      - Scale tested vs needed
      - Integration complexity

  resource:
    number: 202
    question: "Do we have people, budget, infrastructure, tools?"
    sub_factors:
      - Headcount and skills
      - Budget allocation
      - Infrastructure availability
      - Tools and licenses

  # ... continue for all 10 dimensions

---
confidence_levels:
  high:
    description: "Based on empirical evidence (probes, spikes, reference class)"
    sources:
      - Validated probes
      - Integration spikes
      - Reference class data

  medium:
    description: "Based on expert judgment (calibrated) and analogies"
    sources:
      - Expert estimates
      - Analogies with verified transfer

  low:
    description: "Based on team gut feeling and planning (uncalibrated)"
    sources:
      - Internal planning estimates
      - Intuition

---
binding_constraint:
  formula: "min(all dimension scores)"
  rationale: |
    A project feasible on 9/10 dimensions but infeasible on 1
    is INFEASIBLE overall. Like a chain - strength determined by weakest link.
    (Goldratt's Theory of Constraints)
```

### 5.2 Template Markdown (from report-template.md pattern)

```markdown
# Feasibility Report Template
# LOAD: step-05-output.md
# PURPOSE: Standardized output format for feasibility assessment

---

═══════════════════════════════════════════════════════════════
FEASIBILITY ASSESSMENT REPORT
═══════════════════════════════════════════════════════════════

SUBJECT: [subject_name]
DATE: [ISO date]
WORKFLOW VERSION: Deep Feasibility V1.0

───────────────────────────────────────────────────────────────
DECISION
───────────────────────────────────────────────────────────────

DECISION: [GO / NO GO / CONDITIONAL GO / INVESTIGATE]
CONFIDENCE: [HIGH / MEDIUM / LOW]
BINDING CONSTRAINT: [dimension_name] (score: [X]/5)
OVERALL FEASIBILITY: [X]/5

───────────────────────────────────────────────────────────────
EXECUTIVE SUMMARY
───────────────────────────────────────────────────────────────

[2-3 sentence summary of decision rationale]

Key factors:
- [Factor 1]
- [Factor 2]
- [Factor 3]

───────────────────────────────────────────────────────────────
FEASIBILITY PROFILE
───────────────────────────────────────────────────────────────

Technical     ████████░░  4  Confidence: H
Resource      ██████░░░░  3  Confidence: M
Knowledge     ████████░░  4  Confidence: H
Organization  ██████░░░░  3  Confidence: M
Temporal      ████░░░░░░  2  Confidence: H  ← BINDING
Composition   ██████░░░░  3  Confidence: L
Economic      ████████░░  4  Confidence: M
Regulatory    ██████████  5  Confidence: H
Scale         ██████░░░░  3  Confidence: M
Cognitive     ████████░░  4  Confidence: H

───────────────────────────────────────────────────────────────
CONSTRAINTS IDENTIFIED
───────────────────────────────────────────────────────────────

H5 (Impossible):
- [None / List with evidence]

H4 (Computationally Infeasible):
- [List]

H3 (Structurally Blocked):
- [List]

H2 (Resource Constrained):
- [List]

Contradictions:
- [List with TRIZ resolution status]

───────────────────────────────────────────────────────────────
CONDITIONS FOR FEASIBILITY
───────────────────────────────────────────────────────────────

[List all "feasible IF..." conditions]

1. [Condition] — P: [probability] — Controller: [who] — Fallback: [plan B]
2. [Condition] — P: [probability] — Controller: [who] — Fallback: [plan B]

Compound Probability: [calculated P of all conditions holding]

───────────────────────────────────────────────────────────────
CALIBRATION & VALIDATION
───────────────────────────────────────────────────────────────

Reference Class: [project type]
  Base rate (on-time): [X%]
  Base rate (on-budget): [X%]
  Adjustments: [list]
  Calibrated estimate: [details]

Critical Assumptions Tested:
- [Assumption 1]: [CONFIRMED / REFUTED / UNTESTED]
- [Assumption 2]: [CONFIRMED / REFUTED / UNTESTED]

Probes Run:
- [Probe 1]: [Result]
- [Probe 2]: [Result]

───────────────────────────────────────────────────────────────
META AUDIT
───────────────────────────────────────────────────────────────

Planning Fallacy Signals: [detected / none]
Hofstadter Correction: [applied — multiplier]
Dunning-Kruger Zones: [dimensions with low expertise + high confidence]
Confidence Theater: [genuine / theatrical]

───────────────────────────────────────────────────────────────
DECAY MONITORING
───────────────────────────────────────────────────────────────

Reassessment Triggers:
- [Trigger 1]: [monitoring method]
- [Trigger 2]: [monitoring method]

Scheduled Reviews:
- [Milestone 1]: [date/condition]
- [Milestone 2]: [date/condition]

───────────────────────────────────────────────────────────────
RECOMMENDATIONS
───────────────────────────────────────────────────────────────

[Depends on decision - see template patterns]

───────────────────────────────────────────────────────────────
METADATA
───────────────────────────────────────────────────────────────

Assessment started: [timestamp]
Assessment completed: [timestamp]
Depth level: [quick/standard/comprehensive/critical]
Methods executed: [count]
Coverage score: C = [score]
Complex mode: [on/off]
```

---

## Part 6: Extraction Mapping

The DEEP-FEASIBILITY.md content maps to the process structure as follows:

| DEEP-FEASIBILITY.md Section | Target Location |
|----------------------------|-----------------|
| Overview | workflow.md → CORE PHILOSOPHY |
| Theoretical Foundations (1-16) | data/theoretical-foundations.yaml |
| Philosophy (Core Principles 1-7) | workflow.md → CORE PHILOSOPHY |
| Phases description | workflow.md → EXECUTION PATH |
| Method 001-003 (FRAME) | data/method-procedures/001-003*.md |
| Method 101-106 (CONSTRAIN) | data/method-procedures/101-106*.md |
| Method 201-210 (ASSESS) | data/method-procedures/201-210*.md |
| Method 301-306 (VALIDATE) | data/method-procedures/301-306*.md |
| Method 401-404 (DECIDE) | data/method-procedures/401-404*.md |
| Method 501-505 (META) | data/method-procedures/501-505*.md + meta/meta-checklist.yaml |
| Method Summary table | workflow.md → reference + methods.csv |
| Usage Guide | workflow.md → USAGE GUIDE |
| Appendix A (Register Template) | data/feasibility-register-template.md |
| Paradoxes of Feasibility | data/theoretical-foundations.yaml |
| Integration with Other Deep Processes | workflow.md → INTEGRATION |

---

## Part 7: Implementation Checklist

To transform DEEP-FEASIBILITY.md into the full process:

### Phase 1: Directory Structure
- [ ] Create `steps/` directory
- [ ] Create `data/` directory
- [ ] Create `data/method-procedures/` directory
- [ ] Create `meta/` directory

### Phase 2: Core Files
- [ ] Create `workflow.md` following template above
- [ ] Create `methods.csv` with all 35 methods

### Phase 3: Step Files
- [ ] Create `step-00-frame.md`
- [ ] Create `step-01-constrain.md`
- [ ] Create `step-02-assess.md`
- [ ] Create `step-03-validate.md`
- [ ] Create `step-04-decide.md`
- [ ] Create `step-05-output.md`

### Phase 4: Data Files
- [ ] Create `feasibility-scoring.yaml`
- [ ] Create `coverage-scoring.yaml`
- [ ] Create `decision-thresholds.yaml`
- [ ] Create `theoretical-foundations.yaml`
- [ ] Create `constraint-pattern-library.yaml`

### Phase 5: Method Procedures (35 files)
- [ ] Create all FRAME methods (001-003)
- [ ] Create all CONSTRAIN methods (101-106)
- [ ] Create all ASSESS methods (201-210)
- [ ] Create all VALIDATE methods (301-306)
- [ ] Create all DECIDE methods (401-404)
- [ ] Create all META methods (501-505)

### Phase 6: Templates
- [ ] Create `feasibility-register-template.md`
- [ ] Create `feasibility-report-template.md`

### Phase 7: META
- [ ] Create `meta/meta-checklist.yaml`

### Phase 8: Validation
- [ ] Verify all file paths referenced in workflow.md exist
- [ ] Verify all method numbers are consistent
- [ ] Test workflow with sample input

---

## Part 8: Key Differences from Source Processes

| Aspect | Deep-Verify | Deep-Risk | Deep-Explore | Deep-Feasibility |
|--------|-------------|-----------|--------------|------------------|
| Primary output | Verdict (ACCEPT/REJECT) | Risk Register | Option Map | Decision (GO/NO-GO) |
| Scoring | S-score (evidence) | 5D (P×I×max) | Coverage | 10-dimension profile |
| Binding logic | Score threshold | Portfolio view | N/A | min(dimensions) |
| Unique concept | Pattern matching | Ergodicity/cascades | Fear analysis | Constraint hardness |
| Auto-detect | None | Crisis mode | Fear mode | Complexity mode |
| Integration | Feeds impossibilities | Consumes from others | Feeds options | Central hub |

---

## Appendix: File Naming Conventions

```
Method procedures:  {NNN}_{Name_With_Underscores}.md
                    Example: 201_Technical_Feasibility_TRL.md

Step files:         step-{XX}-{name}.md
                    Example: step-02-assess.md

YAML configs:       {domain}-{type}.yaml
                    Example: feasibility-scoring.yaml

Templates:          {domain}-{type}-template.md
                    Example: feasibility-report-template.md
```
