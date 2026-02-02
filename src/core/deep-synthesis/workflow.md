# Deep Synthesis V1.0 — Systematic Knowledge Synthesis Workflow

---

## INVOCATION

**When user wants to synthesize knowledge, ALWAYS start with this dialog:**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP SYNTHESIS                                        ║
║                      Systematic Knowledge Synthesis                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Before we begin, select synthesis depth:                                  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [1] QUICK  (1-2 hours)                                             │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Synthesis question formulation + level selection                 │  ║
║  │  • Basic source collection (2-5 sources)                            │  ║
║  │  • Core claim extraction + relationship mapping                     │  ║
║  │  • Key dialectical integration                                       │  ║
║  │  • Compressed insights (title + thesis + abstract)                  │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Rapid knowledge integration before a meeting                     │  ║
║  │  → Initial orientation in a new domain                              │  ║
║  │  → Low-stakes knowledge consolidation                               │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [2] STANDARD  (half day)                                           │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Full SCOPE phase with source landscape mapping                   │  ║
║  │  • Systematic source collection with quality assessment             │  ║
║  │  • Complete DECOMPOSE (claims, concepts, models, evidence)          │  ║
║  │  • Full RELATE (convergence, divergence, analogies, patterns)       │  ║
║  │  • Dialectical and framework integration                            │  ║
║  │  • Core insights, mental models, principles                         │  ║
║  │  • Basic META validation                                             │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Important decisions requiring integrated knowledge               │  ║
║  │  → Cross-domain research synthesis                                  │  ║
║  │  → Team knowledge consolidation                                     │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [3] RIGOROUS  (2-3 days)                                           │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in STANDARD                                            │  ║
║  │  • Counter-source search and tacit knowledge elicitation            │  ║
║  │  • Full emergence detection and abductive integration               │  ║
║  │  • Boundary condition mapping                                        │  ║
║  │  • Full META audit (apophenia, bias, falsifiability)                │  ║
║  │  • Narrative construction with fallacy guards                       │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → High-stakes strategic decisions                                  │  ║
║  │  → Research synthesis for publication                               │  ║
║  │  → Domain knowledge building                                         │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [4] COMPREHENSIVE  (1-2 weeks)                                     │  ║
║  │                                                                      │  ║
║  │  What you get:                                                       │  ║
║  │  • Everything in RIGOROUS                                            │  ║
║  │  • Multiple iteration cycles with stakeholder review                │  ║
║  │  • External research and validation                                 │  ║
║  │  • Full synthesis quality rubric assessment                         │  ║
║  │  • Living synthesis with decay monitoring                           │  ║
║  │                                                                      │  ║
║  │  When to use:                                                        │  ║
║  │  → Comprehensive knowledge synthesis project                        │  ║
║  │  → Organizational learning initiatives                              │  ║
║  │  → Critical strategic planning                                      │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  Select: [1] / [2] / [3] / [4]                                            ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**After user selection:**
1. Record depth: `depth = quick | standard | rigorous | comprehensive`
2. Scan input for diversity signals (see: DIVERSITY DETECTION)
3. Begin execution from Step 0

---

## DIVERSITY DETECTION (automatic)

**Do not ask user about diversity check. Detect automatically from language.**

If description contains signals of low source diversity:
- "one expert", "single source", "main reference", "primarily from"
- "the book says", "according to [one author]"
- "all sources agree", "no contradiction", "consensus"

**→ Enable `low_diversity_flag = on`**

This means:
- In ACQUIRE: Mandate #105 Counter-Source Search
- In META: Prioritize #601 Apophenia Check, #602 Confirmation Bias Audit
- In report: Add "Diversity Warning" section

If description contains signals of high convergence without exploration:
- "obviously", "everyone knows", "clearly"
- "no need to check", "straightforward"

**→ Enable `convergence_warning = on`**

This means:
- Flag potential confirmation bias
- Require explicit divergence search
- Add confidence ceiling (max = MEDIUM)

**If no signals → `low_diversity_flag = off`, `convergence_warning = off`** (standard synthesis)

---

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP SYNTHESIS = INTEGRATION + EMERGENCE + COMPRESSION + VALIDATION        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Multiple sources, diverse perspectives, knowledge fragments       │
│  OUTPUT:  GENUINE UNDERSTANDING                                              │
│           • Emergent insights not present in any single source              │
│           • Resolved contradictions or productive tensions                  │
│           • Compressed knowledge (shorter than sources, same essence)       │
│           • Falsifiable conclusions with boundary conditions                │
│           • Mental models and principles for future application             │
│                                                                              │
│  CORE PRINCIPLES:                                                           │
│  1. SYNTHESIS CREATES KNOWLEDGE — if no new insight, it's summarization    │
│  2. CONTRADICTION IS FUEL — disagreement drives deeper understanding        │
│  3. COMPRESSION IS THE MEASURE — good synthesis is shorter than sources     │
│  4. EMERGENCE IS THE GOAL — insights visible only in combination            │
│  5. FALSIFIABILITY IS THE CHECK — unfalsifiable synthesis is narrative      │
│  6. LEVEL MATTERS — same data at different levels = different conclusions   │
│  7. DIVERSE SOURCES > MANY SIMILAR — triangulation beats volume             │
│                                                                              │
│  UNIQUE ERROR TYPE: FALSE COHERENCE                                          │
│  Believing you've created genuine understanding when you've actually:       │
│  • Imposed a pattern that doesn't exist (apophenia)                         │
│  • Ignored contradicting evidence (confirmation bias)                        │
│  • Confused correlation with causation (causal illusion)                    │
│  • Created internally consistent but externally wrong model                 │
│  • Synthesized at the wrong level of abstraction                            │
│                                                                              │
│  INTEGRATION:                                                               │
│  • Consumes: Deep-Explore options, Deep-Verify findings, Deep-Risk register│
│  • Produces: Unified understanding for decisions, organizational learning  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## THEORETICAL FOUNDATIONS

Deep Synthesis is grounded in foundational theories across epistemology, information theory, cognitive science, and philosophy of science. Load: `data/theoretical-foundations.yaml`

### Quick Reference

| Principle | One-Line Summary | Applied In |
|-----------|------------------|------------|
| **Hegel's Dialectic (1807)** | Thesis + Antithesis → Synthesis | #302, #401 |
| **Piaget (1952)** | Assimilation + Accommodation | #401, #402 |
| **Bloom's Taxonomy** | Synthesis = highest cognitive level | All phases |
| **Polanyi (1966)** | Tacit knowledge exists between lines | #104 |
| **Shannon (1948)** | Information = surprise; synthesis must add info | #403, #606 |
| **Kolmogorov Complexity** | Synthesis = compression of sources | #405 |
| **Gentner (1983)** | Structure mapping enables cross-domain transfer | #303 |
| **Fauconnier-Turner (2002)** | Conceptual blending produces emergence | #304 |
| **Weick (1995)** | Sensemaking is constructive, not discovered | #504 |
| **Peirce (1903)** | Abduction = inference to best explanation | #404 |
| **Kuhn (1962)** | Paradigm conflicts require translation | #202, #203 |
| **Lakatos (1978)** | Hard core vs protective belt disagreements | #302 |
| **Feyerabend (1975)** | Methodological diversity strengthens synthesis | #103 |
| **Popper (1934)** | Good synthesis is falsifiable | #503, #604 |
| **Glass (1976)** | Meta-analysis: weight by quality, not count | #102, #204 |
| **Glaser & Strauss (1967)** | Grounded theory: patterns emerge from data | #306 |
| **Denzin (1978)** | Triangulation validates through convergence | #103, #301 |
| **Nonaka & Takeuchi (1995)** | SECI: Combination quadrant = synthesis | #402 |
| **Taleb** | Narrative fallacy: stories imposed on random data | #504, #601 |

---

## DEPTH LEVELS — What executes at each level

### QUICK (depth = quick)

```
PHASES:          SCOPE(lite) → ACQUIRE(basic) → DECOMPOSE(core) → RELATE(core) → INTEGRATE(core) → CRYSTALLIZE(minimal)
METHODS:         001-002 + 101-102 + 201,204 + 301-302 + 401,405 + 501
MAX ITERATIONS:  1 (no feedback loops)
SOURCES:         2-5 sources
META:            None (built into process)
COVERAGE TARGET: C ≥ 15
```

### STANDARD (depth = standard)

```
PHASES:          SCOPE → ACQUIRE → DECOMPOSE → RELATE → INTEGRATE → CRYSTALLIZE → META(core)
METHODS:         All SCOPE + 101-103 + 201-205 + 301-306 + 401-405 + 501-504 + 601,602,606
MAX ITERATIONS:  3
SOURCES:         5-15 sources
META:            Core methods after INTEGRATE
COVERAGE TARGET: C ≥ 35
```

### RIGOROUS (depth = rigorous)

```
PHASES:          SCOPE → ACQUIRE(full) → DECOMPOSE → RELATE(full) → INTEGRATE(full) → CRYSTALLIZE → META(full)
METHODS:         All methods except multi-iteration external validation
MAX ITERATIONS:  5
SOURCES:         10-30 sources
META:            Full methods after each major phase
COVERAGE TARGET: C ≥ 50
```

### COMPREHENSIVE (depth = comprehensive)

```
PHASES:          All phases, full execution
METHODS:         All 40 methods
MAX ITERATIONS:  Unlimited
SOURCES:         Comprehensive coverage of landscape
META:            Continuous with stakeholder review
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
│  SCOPE  │    │ ACQUIRE │    │DECOMPOSE│    │ RELATE  │     │
└─────────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
                    │              │              │           │
                    └──────────────┴──────────────┘           │
                                        │                     │
                              ┌─────────┐    ┌─────────┐     │
                              │ STEP 4  │───►│ STEP 5  │◄────┘
                              │INTEGRATE│    │CRYSTALLIZE
                              └─────────┘    └─────────┘
                                                  │
                              ┌────────────────────┘
                              ▼
                         ┌─────────┐
                         │ STEP 6  │
                         │ OUTPUT  │
                         └─────────┘
                              │
              ┌───────────────┘
              ▼
         META (continuous)
    Applied after each phase
```

---

## EXECUTION PATH

**After user selects depth level, execute:**

```
📂 Step 0: SCOPE
   Load: steps/step-00-scope.md

   □ Define synthesis question
   □ 📂 #001 → Synthesis Question Formulation
   □ 📂 #002 → Level-of-Analysis Selection
   □ 📂 #003 → Source Landscape Mapping

   Output: Synthesis Question, Level Selection, Source Landscape Map

   ↓ PROCEED when question is clear and bounded
   ↓ STAY if scope unclear

📂 Step 1: ACQUIRE
   Load: steps/step-01-acquire.md

   □ 📂 #101 → Systematic Source Collection
   □ 📂 #102 → Source Quality Assessment
   □ 📂 #103 → Diversity Verification
   □ 📂 #104 → Tacit Knowledge Elicitation [rigorous+]
   □ 📂 #105 → Counter-Source Search [rigorous+ or low_diversity_flag]

   DEPTH ADJUSTMENT:
   • quick: #101-102 only (2-5 sources)
   • standard: #101-103 (5-15 sources)
   • rigorous+: all methods

   Output: Source Inventory with Quality Grades, Diversity Map

   ↓ PROCEED when sources are sufficient
   ↑ RETURN TO STEP 0 if scope needs refinement

📂 Step 2: DECOMPOSE
   Load: steps/step-02-decompose.md

   □ 📂 #201 → Atomic Claim Extraction
   □ 📂 #202 → Concept Taxonomy Building
   □ 📂 #203 → Model Inventory
   □ 📂 #204 → Evidence Grading
   □ 📂 #205 → Assumption Surfacing
   □ 📂 #206 → Knowledge Gap Identification

   DEPTH ADJUSTMENT:
   • quick: #201, #204 only
   • standard: #201-205
   • rigorous+: all methods

   Output: Claims, Concepts, Models, Evidence Grades, Assumptions, Gaps

   ↓ PROCEED when decomposition is complete
   ↑ RETURN TO STEP 1 if more sources needed

📂 Step 3: RELATE
   Load: steps/step-03-relate.md

   □ 📂 #301 → Convergence-Divergence Mapping
   □ 📂 #302 → Dialectical Tension Mapping
   □ 📂 #303 → Analogical Structure Mapping (Gentner)
   □ 📂 #304 → Conceptual Blend Construction (Fauconnier-Turner)
   □ 📂 #305 → Causal Chain Reconciliation
   □ 📂 #306 → Pattern Detection Across Sources
   □ 📂 #307 → Level Alignment Check
   □ 📂 #308 → Gap Significance Analysis

   DEPTH ADJUSTMENT:
   • quick: #301-302 only
   • standard: #301-306
   • rigorous+: all methods

   Output: Relationship Graph, Dialectical Tensions, Patterns, Analogies

   ↓ PROCEED when relationships are mapped
   ↑ RETURN if new sources or decomposition needed

📂 Step 4: INTEGRATE
   Load: steps/step-04-integrate.md

   □ 📂 #401 → Dialectical Integration (Hegel)
   □ 📂 #402 → Framework Unification
   □ 📂 #403 → Emergence Detection (Shannon Test)
   □ 📂 #404 → Abductive Integration (Peirce)
   □ 📂 #405 → Knowledge Compression (Kolmogorov)
   □ 📂 #406 → Boundary Condition Mapping
   □ 📂 #407 → Synthesis Coherence Check

   DEPTH ADJUSTMENT:
   • quick: #401, #405 only
   • standard: #401-405
   • rigorous+: all methods

   Output: Integrated Framework, Emergent Insights, Compressed Synthesis

   ↓ PROCEED when integration is complete
   ↑ RETURN if integration reveals gaps

📂 Step 5: CRYSTALLIZE
   Load: steps/step-05-crystallize.md

   □ 📂 #501 → Core Insight Distillation
   □ 📂 #502 → Mental Model Design
   □ 📂 #503 → Principle Extraction
   □ 📂 #504 → Narrative Construction (with fallacy guard)
   □ 📂 #505 → Actionability Assessment

   DEPTH ADJUSTMENT:
   • quick: #501 only
   • standard: #501-504
   • rigorous+: all methods

   Output: Core Insights, Mental Models, Principles, Narrative, Actions

   ↓ PROCEED to output

📂 Step 6: OUTPUT
   Load: steps/step-06-output.md

   □ Apply META methods (#601-607) as final audit
   □ Generate Synthesis Record
   □ Generate Synthesis Report

   Load templates:
   • data/synthesis-record-template.md
   • data/synthesis-report-template.md

   Output: SYNTHESIS DELIVERABLES
```

---

## META METHODS (Continuous)

META methods (#601-607) govern the synthesis process itself. Apply after each major phase:

| # | Method | Purpose | When to Apply |
|---|--------|---------|---------------|
| 601 | Apophenia Check | Are detected patterns real or imposed? | After RELATE, OUTPUT |
| 602 | Confirmation Bias Audit | Did prior views distort synthesis? | After INTEGRATE |
| 603 | Completeness Assessment | Does synthesis cover the question? | After CRYSTALLIZE |
| 604 | Falsifiability Check (Popper) | Can synthesis be proven wrong? | After INTEGRATE |
| 605 | Source Bias Propagation Check | Did source biases infect synthesis? | After INTEGRATE |
| 606 | Novel Information Test (Shannon) | Is this genuine synthesis or summary? | After CRYSTALLIZE |
| 607 | Synthesis Decay Monitoring | When will synthesis expire? | During OUTPUT |

Load: `meta/meta-checklist.yaml`

---

## SCORING SYSTEMS

### Process Coverage Score (C)

Measures synthesis thoroughness:

| Activity | Points |
|----------|--------|
| Phase completed | +3 |
| Method executed | +1 |
| Source processed | +0.5 |
| Claim extracted | +0.3 |
| Relationship mapped | +0.5 |
| Tension resolved | +1 |
| Emergent insight identified | +1.5 |
| META method applied | +0.5 |

Load: `data/coverage-scoring.yaml`

### Synthesis Quality Score

Based on Appendix A rubric:

| Criterion | Excellent | Good | Adequate | Poor |
|-----------|-----------|------|----------|------|
| **Novelty** | >50% genuine synthesis | 30-50% | 10-30% | <10% (summary) |
| **Compression** | 5× shorter than sources | 3× | 2× | Same length |
| **Coherence** | Internally consistent | Minor tensions | Some contradictions | Contradicts itself |
| **Coverage** | All aspects addressed | Most, gaps noted | Major gaps acknowledged | Gaps unacknowledged |
| **Falsifiability** | All claims falsifiable | Most | Some | Unfalsifiable narrative |
| **Actionability** | Clear multi-stakeholder actions | Clear primary action | Suggestive | No implications |
| **Bias control** | Counter-sources sought | Some checks | Minimal | No checking |
| **Level clarity** | Level explicit | Mostly clear | Implicit | Levels mixed |

Load: `data/synthesis-scoring.yaml`

### Coverage Thresholds

| Depth | Comprehensive | Adequate | Partial | Insufficient |
|-------|---------------|----------|---------|--------------|
| quick | C ≥ 15 | C ≥ 10 | C ≥ 5 | C < 5 |
| standard | C ≥ 35 | C ≥ 25 | C ≥ 15 | C < 15 |
| rigorous | C ≥ 50 | C ≥ 40 | C ≥ 30 | C < 30 |
| comprehensive | C ≥ 65 | C ≥ 55 | C ≥ 45 | C < 45 |

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SYNTHESIS COMMANDMENTS                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. ALWAYS START WITH INVOCATION                                            │
│     Display the depth selection dialog before doing anything                │
│     Wait for user choice before proceeding                                  │
│                                                                              │
│  2. SYNTHESIS ≠ SUMMARIZATION                                               │
│     If your output contains nothing new, you have summarized, not synthesized│
│     Apply Shannon Test (#606): does insight require COMBINING sources?      │
│                                                                              │
│  3. CONTRADICTION IS VALUABLE                                               │
│     Sources that disagree are MORE valuable than sources that agree         │
│     Don't resolve tensions prematurely — understand WHY they exist          │
│                                                                              │
│  4. COMPRESSION IS MANDATORY                                                │
│     If synthesis is as long as sources, you haven't synthesized             │
│     Title → Thesis → Abstract → Executive Summary → Full                    │
│                                                                              │
│  5. LEVEL MUST BE EXPLICIT                                                  │
│     Same data at different abstraction levels = different conclusions       │
│     State the level; note where conclusions DON'T transfer                  │
│                                                                              │
│  6. FALSIFIABILITY IS REQUIRED                                              │
│     "What would disprove this synthesis?" must have an answer               │
│     Unfalsifiable synthesis is narrative, not knowledge                     │
│                                                                              │
│  7. LOAD FILES WHEN NEEDED                                                  │
│     Announce: "📂 Loading [path]"                                           │
│     Follow the procedure in the loaded file                                 │
│                                                                              │
│  8. META IS CONTINUOUS                                                      │
│     Apply META methods after each phase, not just at end                    │
│     False coherence is the enemy — check for it continuously                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FILE LOADING PROTOCOL

When you need specific data, announce and load:

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-scope.md` | "📂 Loading Step 0: Scope" |
| Start Step 1 | `steps/step-01-acquire.md` | "📂 Loading Step 1: Acquire" |
| Start Step 2 | `steps/step-02-decompose.md` | "📂 Loading Step 2: Decompose" |
| Start Step 3 | `steps/step-03-relate.md` | "📂 Loading Step 3: Relate" |
| Start Step 4 | `steps/step-04-integrate.md` | "📂 Loading Step 4: Integrate" |
| Start Step 5 | `steps/step-05-crystallize.md` | "📂 Loading Step 5: Crystallize" |
| Start Step 6 | `steps/step-06-output.md` | "📂 Loading Step 6: Output" |
| Execute method | `data/method-procedures/{NNN}_{Name}.md` | "📂 Loading method #{NNN}" |
| Apply scoring | `data/synthesis-scoring.yaml` | "📂 Loading synthesis scoring" |
| Generate record | `data/synthesis-record-template.md` | "📂 Loading record template" |
| Generate report | `data/synthesis-report-template.md` | "📂 Loading report template" |
| Apply META | `meta/meta-checklist.yaml` | "📂 Loading META checklist" |

---

## INTEGRATION WITH OTHER DEEP PROCESSES

### From Deep-Explore

| Deep-Explore Output | Feeds Into |
|--------------------|------------|
| Option Map | Sources for synthesis (#101) |
| Assumptions surfaced | Claims to decompose (#201) |
| Consequence Map | Evidence for synthesis (#204) |
| Knowledge gaps | Gap analysis (#206, #308) |

### From Deep-Verify

| Deep-Verify Output | Feeds Into |
|-------------------|------------|
| Validated claims | High-confidence claims (#201, #204) |
| Contradictions found | Dialectical tensions (#302) |
| Ungrounded claims | Assumptions to surface (#205) |

### From Deep-Risk

| Deep-Risk Output | Feeds Into |
|-----------------|------------|
| Risk register | Sources for synthesis (#101) |
| Interaction map | Relationship patterns (#301, #306) |
| Mitigation portfolio | Knowledge to synthesize |

### From Deep-Feasibility

| Deep-Feasibility Output | Feeds Into |
|------------------------|------------|
| Constraint map | Boundary conditions (#406) |
| Feasibility conditions | Claims with context (#201) |
| Decision rationale | Sources for synthesis |

### Synthesis AS OUTPUT to other processes

| Deep-Synthesis Output | Feeds Into |
|----------------------|------------|
| Unified framework | Deep-Explore: broader option space |
| Core insights | Deep-Verify: claims to validate |
| Principles | Deep-Risk: risk patterns to check |
| Mental models | All: shared understanding |

### Integration Protocol

```
IF Deep-Explore was run on same subject:
  □ Load exploration report
  □ Extract options → potential sources
  □ Extract assumptions → claims to decompose
  □ Extract knowledge gaps → feed to #206, #308

IF Deep-Verify was run on same subject:
  □ Load verification report
  □ Extract validated claims → high-confidence inputs
  □ Extract contradictions → dialectical tensions (#302)

IF Deep-Risk was run on same subject:
  □ Load risk report
  □ Extract risk interactions → relationship patterns
  □ Extract mitigations → knowledge to integrate

IF Deep-Feasibility was run on same subject:
  □ Load feasibility report
  □ Extract constraints → boundary conditions (#406)
  □ Extract conditions → contextual claims

AFTER Deep-Synthesis:
  □ Hand off insights → inform other processes
  □ Hand off principles → reusable knowledge
  □ Hand off mental models → shared frameworks
```

---

## DIRECTORY STRUCTURE

```
deep-synthesis/
├── workflow.md                           ← YOU ARE HERE
├── DEEP-SYNTHESIS.md                     ← Methodology document
├── steps/
│   ├── step-00-scope.md                  # SCOPE phase procedure
│   ├── step-01-acquire.md                # ACQUIRE phase procedure
│   ├── step-02-decompose.md              # DECOMPOSE phase procedure
│   ├── step-03-relate.md                 # RELATE phase procedure
│   ├── step-04-integrate.md              # INTEGRATE phase procedure
│   ├── step-05-crystallize.md            # CRYSTALLIZE phase procedure
│   └── step-06-output.md                 # OUTPUT generation
├── data/
│   ├── method-procedures/                # 40 method procedure files
│   │   ├── 001_Synthesis_Question_Formulation.md
│   │   ├── 002_Level_of_Analysis_Selection.md
│   │   ├── 003_Source_Landscape_Mapping.md
│   │   ├── 101_Systematic_Source_Collection.md
│   │   ├── ... (all 40 methods)
│   │   └── 607_Synthesis_Decay_Monitoring.md
│   ├── theoretical-foundations.yaml      # 19 foundational theories
│   ├── synthesis-scoring.yaml            # Quality rubric
│   ├── coverage-scoring.yaml             # Process coverage metrics
│   ├── synthesis-record-template.md      # Individual synthesis template
│   └── synthesis-report-template.md      # Full report template
├── meta/
│   └── meta-checklist.yaml               # META methods as checklist
└── methods.csv                           # Method index
```

---

## USAGE GUIDE

### When to Use Deep-Synthesis

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **Integrating research for decision** | SCOPE → full cycle | rigorous |
| **Post-mortem across incidents** | SCOPE → INTEGRATE | standard |
| **Literature review** | SCOPE → RELATE | standard |
| **Cross-team knowledge sharing** | ACQUIRE → CRYSTALLIZE | standard |
| **Making sense of conflicting advice** | DECOMPOSE → INTEGRATE | standard |
| **Synthesizing Deep Framework outputs** | All outputs as sources | comprehensive |
| **Domain knowledge building** | Full cycle | comprehensive |
| **Quick knowledge consolidation** | SCOPE → CRYSTALLIZE | quick |

### Quick Reference

```
Quick synthesis:     SCOPE(lite) → ACQUIRE(basic) → DECOMPOSE(core) → RELATE(core) → INTEGRATE(core) → CRYSTALLIZE(minimal)
Standard synthesis:  SCOPE → ACQUIRE → DECOMPOSE → RELATE → INTEGRATE → CRYSTALLIZE → META(core)
Rigorous synthesis:  All phases + full methods + full META
Comprehensive:       Full + iterations + stakeholder review + decay monitoring
```

---

## VERSION HISTORY

- **V1.0** — Initial release based on DEEP-SYNTHESIS.md methodology
