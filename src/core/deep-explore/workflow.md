# Deep Explore V1.0 — Structured Decision Space Exploration

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP EXPLORE = SYSTEMATIC DIVERGENCE + CONSEQUENCE MAPPING + SYNTHESIS    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Decision problem, strategic question, complex choice              │
│  OUTPUT:  Structured EXPLORATION MAP with options & consequences            │
│                                                                              │
│  PRINCIPLE: NO DIMENSION = NO EXPLORATION                                   │
│             Every option must be traced to its decision dimension           │
│                                                                              │
│  ANTI-PATTERN: PREMATURE CONVERGENCE                                        │
│             Never narrow options before full exploration                    │
│                                                                              │
│  EXECUTION: Designed for LLM CLI (Claude, Gemini, Ollama, etc.)            │
│             Single prompt → Structured exploration output                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## THEORETICAL FOUNDATIONS

### 1. Double Diamond (Design Council)
```
    DIVERGENT          CONVERGENT         DIVERGENT          CONVERGENT
    (Discover)         (Define)           (Develop)          (Deliver)
         
        ╱╲                                    ╱╲
       ╱  ╲                                  ╱  ╲
      ╱    ╲            ╱╲                  ╱    ╲            ╱╲
     ╱      ╲          ╱  ╲                ╱      ╲          ╱  ╲
    ╱        ╲        ╱    ╲              ╱        ╲        ╱    ╲

   PHASE 1-2        PHASE 3-4           PHASE 5           USER DECIDES
```

### 2. Cynefin Framework (Snowden)
```
┌─────────────────────────┬─────────────────────────┐
│       COMPLEX           │      COMPLICATED        │
│   Probe → Sense → Act   │  Sense → Analyze → Act │
│   (Experiment first)    │  (Expert analysis)      │
├─────────────────────────┼─────────────────────────┤
│       CHAOTIC           │       CLEAR             │
│   Act → Sense → Probe   │  Sense → Categorize →  │
│   (Crisis mode)         │  Respond (Obvious)      │
└─────────────────────────┴─────────────────────────┘

Deep Explore is designed for COMPLEX and COMPLICATED domains.
```

### 3. Morphological Analysis (Zwicky)
Systematic exploration of ALL dimension combinations before selection.

### 4. Real Options Theory
Value of keeping options open. Decision = Value + Information from delay.

---

## EXECUTION MODES

### Quick Explore (QE) — Fast Mapping
```
Time: 5-10 min | Methods: Tier 1 only | For: Orientation
Output: Basic dimension map, key options, obvious constraints

1. FRAME → Define vision, constraints
2. PHASE 1 ONLY → Dimension Discovery
3. OUTPUT → Basic Morphological Box

Triggers: `QE`, `quick explore`, `--quick`, `-q`
```

### Standard Explore (SE) — Full Process
```
Time: 30-60 min | Methods: Tiers 1-3 | For: Complete exploration
Output: Full map with consequences, stress-tested options

1. FRAME → Vision + constraints + problem type
2. PHASE 1 → MAP (Divergent)
3. PHASE 2 → ILLUMINATE (Consequences)
4. PHASE 3 → CHALLENGE (Adversarial)
5. PHASE 4 → SYNTHESIZE (Clustering)
6. OUTPUT → Full exploration map

Triggers: `DE`, `explore`, `--full`, default
```

### Deep Explore (DE) — Maximum Breadth
```
Time: 60-120 min | Methods: All + Experiments | For: Strategic decisions

Same as Standard + PHASE 5 (Experiment Design)
+ Second-order effect analysis
+ External validation suggestions

Triggers: `DE --deep`, `--strategic`
```

---

## QUICK EXECUTION PATH

**For most explorations, execute this sequence:**

```
1. FRAME
   □ Define vision (what you want to achieve, not how)
   □ List hard constraints (what's impossible)
   □ Set abstraction level: STRATEGIC / TACTICAL / OPERATIONAL
   □ Identify problem type: COMPLEX / COMPLICATED / CLEAR
   □ Note existing biases and assumptions

2. PHASE 1: MAP (Divergent)
   📂 Loading method: 001_Dimension_Discovery.md
   □ Execute #1 Dimension Discovery
   
   📂 Loading method: 002_Option_Enumeration.md
   □ Execute #2 Option Enumeration
   
   📂 Loading method: 003_Constraint_Mapping.md
   □ Execute #3 Constraint Mapping
   
   □ Build Morphological Box
   □ Calculate Coverage Score (C)

3. PHASE 2: ILLUMINATE (Still Divergent)
   📂 Loading method: 011_Consequence_Analysis.md
   □ Execute #11 Consequence Analysis
   
   📂 Loading method: 012_Reversibility_Check.md
   □ Execute #12 Reversibility Check
   
   📂 Loading method: 013_Dependency_Analysis.md
   □ Execute #13 Dependency Analysis
   
   □ Build Decision Consequence Map
   □ Identify Points of No Return

4. PHASE 3: CHALLENGE (Adversarial)
   📂 Loading method: 021_Premortem.md
   □ Execute #21 Premortem for top options
   
   📂 Loading method: 022_Black_Swan_Hunt.md
   □ Execute #22 Black Swan Hunt
   
   □ Stress-test assumptions
   □ Update options based on findings

5. PHASE 4: SYNTHESIZE
   □ Cluster natural option groups
   □ Identify independent vs dependent decisions
   □ Map critical path (what must be decided first)
   □ Note what can be delayed (Real Options)

6. OUTPUT: EXPLORATION MAP
   □ Present full map without recommendation
   □ Highlight key trade-offs
   □ Note uncertainties and information gaps
   □ Suggest experiments if COMPLEX domain
```

---

## COVERAGE SCORING SYSTEM

### Coverage Score (C)

| Exploration Quality | Points | Notes |
|---------------------|--------|-------|
| New dimension discovered | +2 | Fundamental axis of choice |
| New option in dimension | +1 | Adds to possibility space |
| Consequence mapped | +0.5 | Illuminates trade-off |
| Constraint identified | +0.5 | Eliminates impossible |
| Blind spot found | +1 | Previously unknown unknown |
| Dependency discovered | +0.5 | Reveals decision sequence |
| Assumption surfaced | +0.3 | Makes implicit explicit |

### Coverage Thresholds

| Score | Coverage Level | Meaning |
|-------|----------------|---------|
| C ≥ 20 | COMPREHENSIVE | Most of space explored |
| 10 ≤ C < 20 | ADEQUATE | Key dimensions covered |
| 5 ≤ C < 10 | PARTIAL | Major gaps likely |
| C < 5 | INSUFFICIENT | Premature to decide |

### Exploration Completeness Check

```
Before allowing convergence, verify:
□ All obvious dimensions identified (≥3)
□ Each dimension has ≥2 options
□ Key consequences mapped for each option
□ Constraints eliminate <50% of combinations
□ No dimension has only 1 remaining option (unless true constraint)
```

---

## METHOD TIERS

### Tier 1 — Phase 1: MAP (ALL mandatory)

| # | Method | Purpose | File |
|---|--------|---------|------|
| 1 | Dimension Discovery | Find all axes of choice | `001_Dimension_Discovery.md` |
| 2 | Option Enumeration | List all options per dimension | `002_Option_Enumeration.md` |
| 3 | Constraint Mapping | Identify hard limits | `003_Constraint_Mapping.md` |

### Tier 2 — Phase 2: ILLUMINATE (Select based on complexity)

| Complexity Signal | Recommended Methods |
|-------------------|---------------------|
| Multiple stakeholders | #11, #14 (Consequence, Stakeholder Impact) |
| Long-term implications | #12, #15 (Reversibility, Future Optionality) |
| Technical dependencies | #13, #16 (Dependency, Integration Points) |
| Resource constraints | #17, #18 (Resource Trade-off, Opportunity Cost) |

### Tier 3 — Phase 3: CHALLENGE (Adversarial)

| # | Method | Purpose |
|---|--------|---------|
| 21 | Premortem | Imagine failure, trace causes |
| 22 | Black Swan Hunt | Find low-probability high-impact events |
| 23 | Assumption Stress Test | Break each assumption |
| 24 | Regret Minimization | What would you regret not considering? |

### Tier 4 — Phase 4: SYNTHESIZE

| # | Method | Purpose |
|---|--------|---------|
| 31 | Option Clustering | Group similar strategies |
| 32 | Decision Sequencing | What must be decided first |
| 33 | Real Options Identification | What can be delayed |
| 34 | Information Value Analysis | What to learn before deciding |

---

## DECISION ARCHETYPES

**Load:** `data/decision-archetypes.yaml`

Common patterns in decision spaces:

| ID | Archetype | Pattern | Typical Trap |
|----|-----------|---------|--------------|
| DA-001 | False Dichotomy | Only 2 options presented | There's always a third way |
| DA-002 | Local Optimum | Best in current frame | Reframe reveals better options |
| DA-003 | Sunk Cost Anchor | Past investment weighs | Only future matters |
| DA-004 | Availability Bias | Recent/vivid options dominate | Systematic enumeration needed |
| DA-005 | Premature Optimization | Optimizing before understanding | Explore before exploit |
| DA-006 | Analysis Paralysis | Endless exploration | Set decision criteria upfront |
| DA-007 | Hobson's Choice | Fake choice (one real option) | Challenge the constraint |
| DA-008 | Buridan's Ass | Equal options, can't choose | They're probably not equal |

---

## EXPLORATION MAP FORMAT

### Morphological Box (Phase 1 Output)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         MORPHOLOGICAL BOX                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  DIMENSION 1: [Name]                                                       ║
║  ├── Option A: [description]                                               ║
║  ├── Option B: [description]                                               ║
║  └── Option C: [description]                                               ║
║                                                                            ║
║  DIMENSION 2: [Name]                                                       ║
║  ├── Option A: [description]                                               ║
║  └── Option B: [description]                                               ║
║                                                                            ║
║  DIMENSION 3: [Name]                                                       ║
║  ├── Option A: [description]                                               ║
║  ├── Option B: [description]                                               ║
║  └── Option C: [description]                                               ║
║                                                                            ║
║  CONSTRAINTS (eliminate combinations):                                     ║
║  • [D1:A + D2:B] = impossible because [reason]                            ║
║  • [D3:C] requires [external condition]                                    ║
║                                                                            ║
║  VALID COMBINATIONS: [N] of [total possible]                              ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Decision Consequence Map (Phase 2 Output)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DECISION CONSEQUENCE MAP                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  OPTION: [D1:A + D2:B + D3:C]                                             ║
║  ─────────────────────────────────────────────────────────────────────    ║
║                                                                            ║
║  GAINS:                           │  COSTS:                                ║
║  • [gain 1]                       │  • [cost 1]                            ║
║  • [gain 2]                       │  • [cost 2]                            ║
║                                   │                                        ║
║  OPENS:                           │  CLOSES:                               ║
║  • [future possibility 1]         │  • [option foreclosed 1]               ║
║  • [future possibility 2]         │  • [option foreclosed 2]               ║
║                                   │                                        ║
║  REVERSIBILITY: [HIGH/MED/LOW]    │  POINT OF NO RETURN: [when]           ║
║                                   │                                        ║
║  DEPENDENCIES:                                                             ║
║  • Requires [X] to be decided first                                        ║
║  • Blocks decision on [Y] until [condition]                                ║
║                                                                            ║
║  UNCERTAINTIES:                                                            ║
║  • [assumption 1] - confidence: [%]                                        ║
║  • [assumption 2] - confidence: [%]                                        ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## ANTI-CONVERGENCE RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EXPLORATION COMMANDMENTS                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. NO RECOMMENDATION UNTIL PHASE 4 COMPLETE                                │
│     Never suggest "best" option during exploration                          │
│                                                                              │
│  2. PRESERVE ALL OPTIONS                                                    │
│     Only eliminate by hard constraint, never by preference                  │
│                                                                              │
│  3. DIMENSION BEFORE OPTION                                                 │
│     "What are the axes of choice?" before "What should I choose?"           │
│                                                                              │
│  4. CONSEQUENCE BEFORE JUDGMENT                                             │
│     "What happens if X?" before "Is X good?"                                │
│                                                                              │
│  5. USER CONVERGES, NOT AI                                                  │
│     AI maps territory; User navigates                                       │
│                                                                              │
│  6. EXPLICIT TRADE-OFFS                                                     │
│     Every option has costs; make them visible                               │
│                                                                              │
│  7. ACKNOWLEDGE UNKNOWNS                                                    │
│     Map what you don't know, not just what you know                         │
│                                                                              │
│  8. CHALLENGE "OBVIOUS" CONSTRAINTS                                         │
│     "Why is that impossible?" - often it's not                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## INTERACTION PROTOCOL

### When User Gives Preference

```
WRONG:
User: "I prefer option B"
AI: "Great, let's focus on B. Here are the details..."

RIGHT:
User: "I prefer option B"
AI: "Noted. Before narrowing:
     • B closes options [X, Y, Z] - are you okay with that?
     • Have you considered why A might be better? [reasons]
     • What would make you change to A or C?
     
     If you're confident after considering these, we can explore B deeper.
     Otherwise, let's complete mapping first."
```

### When User Wants Answer

```
WRONG:
User: "Just tell me what to do"
AI: "You should do X because..."

RIGHT:
User: "Just tell me what to do"
AI: "I understand the desire for clarity. Here's what I can offer:
     
     COVERAGE STATUS: [C score] - [level]
     
     If you must decide now:
     • Lowest-risk option: [X] - because [reversible/safe]
     • Highest-upside option: [Y] - but [risks]
     • Most information-gathering: [Z] - learn before committing
     
     What I can't tell you:
     • Which trade-offs matter most to YOU
     • Your risk tolerance
     • Future information you might get
     
     Would you like to:
     [ ] Complete exploration (recommended if time allows)
     [ ] Decide with current map (I'll note what's unexplored)
     [ ] Design an experiment to learn more"
```

---

## INTEGRATION WITH DEEP VERIFY

```
WORKFLOW INTEGRATION
─────────────────────────────────────────────────────────

1. EXPLORE → DECIDE → IMPLEMENT → VERIFY

   Deep Explore          Deep Verify
   ────────────          ───────────
   Map options     →     User decides     →     Create artifact     →     Verify artifact
   
2. VERIFY FINDING → EXPLORE ALTERNATIVES

   Deep Verify finds issue  →  Deep Explore alternatives
   "This approach has flaw"     "What other approaches exist?"
   
3. EXPLORE WITHIN CONSTRAINTS FROM VERIFY

   Deep Verify constraints  →  Deep Explore within bounds
   "Must be stateless"          "Options given stateless constraint"
```

---

## DIRECTORY STRUCTURE

```
deep-explore/
├── workflow.md                 ← YOU ARE HERE
├── data/
│   ├── methods.csv                  # Method definitions
│   ├── method-procedures/           # Individual method procedures
│   │   ├── 001_Dimension_Discovery.md
│   │   ├── 002_Option_Enumeration.md
│   │   ├── 003_Constraint_Mapping.md
│   │   ├── 011_Consequence_Analysis.md
│   │   ├── 012_Reversibility_Check.md
│   │   ├── 013_Dependency_Analysis.md
│   │   ├── 021_Premortem.md
│   │   ├── 022_Black_Swan_Hunt.md
│   │   ├── 023_Assumption_Stress_Test.md
│   │   ├── 024_Regret_Minimization.md
│   │   ├── 031_Option_Clustering.md
│   │   ├── 032_Decision_Sequencing.md
│   │   ├── 033_Real_Options_Identification.md
│   │   └── 034_Information_Value_Analysis.md
│   ├── decision-archetypes.yaml     # Common decision patterns
│   ├── coverage-scoring.yaml        # Scoring rules
│   ├── exploration-template.md      # Output format
│   └── examples.md                  # Worked examples
└── steps/                           # Detailed step files
    ├── step-00-frame.md
    ├── step-01-map.md
    ├── step-02-illuminate.md
    ├── step-03-challenge.md
    ├── step-04-synthesize.md
    └── step-05-output.md
```

---

## CLI INVOCATION EXAMPLES

### Claude CLI
```bash
# Quick explore
claude "QE: What are my options for this product?" < context.md

# Standard explore
claude "DE: Explore architecture decisions" \
  --context requirements.md constraints.md

# Deep explore with domain
claude "DE --strategic: Market entry strategy" < business_context.md
```

### With Deep Verify
```bash
# Explore then verify chosen option
claude "DE: Database options" < requirements.md > exploration.md
# User reviews, decides PostgreSQL
claude "DV: Verify PostgreSQL choice" < postgres_design.md
```

---

## VERSION HISTORY

- **V1.0** — Initial release based on Deep Verify patterns
