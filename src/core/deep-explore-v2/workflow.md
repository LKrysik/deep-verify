# Deep Explore V2.0 — Knowledge-First Decision Exploration

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP EXPLORE V2 = KNOWLEDGE EXPANSION + UNCERTAINTY MAPPING + EXPLORATION  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Decision problem, strategic question, complex choice              │
│  OUTPUT:  UNDERSTANDING (not just a map)                                    │
│           • What you learned                                                │
│           • What you still don't know                                       │
│           • Options with VERIFIED vs ASSUMED consequences                   │
│           • Decision readiness assessment                                   │
│                                                                              │
│  CORE PRINCIPLE: EXPAND KNOWLEDGE BEFORE MAPPING OPTIONS                    │
│                  You cannot map territory you haven't explored              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FOUNDATIONAL METHODS

Deep Explore V2 is built on these epistemological foundations:

### Epistemological Core (E001-E007)

| ID | Method | Purpose | File |
|----|--------|---------|------|
| E001 | Abductive Reasoning | Generate hypotheses from observations | `data/method-procedures/E001_Abductive_Reasoning.md` |
| E002 | Counterfactual Thinking | Identify causal factors and leverage points | `data/method-procedures/E002_Counterfactual_Thinking.md` |
| E003 | Minimal Assertions | Compress knowledge to actionable principles | `data/method-procedures/E003_Minimal_Assertions.md` |
| E004 | Boundary Analysis | Find limits where things stop working | `data/method-procedures/E004_Boundary_Analysis.md` |
| E005 | Causal Models | Map influence relationships | `data/method-procedures/E005_Causal_Models.md` |
| E006 | Falsification | Test beliefs by trying to disprove them | `data/method-procedures/E006_Falsification.md` |
| E007 | Information Questions | Identify highest-value questions | `data/method-procedures/E007_Information_Questions.md` |

### Fear-Based Exploration (E008-E014)

For users with concerns, fears, or uncertainty about a decision. These methods transform anxiety into structured exploration.

| ID | Method | Purpose | File |
|----|--------|---------|------|
| E008 | Failure Reason Exploration | Transform fear into structured risk map | `data/method-procedures/E008_Failure_Reason_Exploration.md` |
| E009 | Reverse Abduction | Discover paths by assuming success | `data/method-procedures/E009_Reverse_Abduction.md` |
| E010 | Cognitive MVP | Find smallest action that teaches something | `data/method-procedures/E010_Cognitive_MVP.md` |
| E011 | Control vs Influence Analysis | Separate controllable from uncontrollable | `data/method-procedures/E011_Control_Influence_Analysis.md` |
| E012 | Fundamental Block Analysis | Find true "walls" vs false walls | `data/method-procedures/E012_Fundamental_Block_Analysis.md` |
| E013 | Contrast Exploration | Learn from others' successes and failures | `data/method-procedures/E013_Contrast_Exploration.md` |
| E014 | Growth Test | Filter decisions by whether they develop you | `data/method-procedures/E014_Growth_Test.md` |

---

## EXECUTION FLOW

```
                    ┌──────────────────────────────────────────┐
                    │          FEEDBACK LOOPS                  │
                    ▼                                          │
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│ STEP 0  │───►│ STEP 1  │───►│ STEP 2  │───►│ STEP 3  │─────┤
│ AUDIT   │    │ RESEARCH│    │   MAP   │    │ DEEPEN  │     │
└─────────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
                    │              │              │           │
                    └──────────────┴──────────────┘           │
                                          │                   │
                                          ▼                   │
                    ┌─────────┐    ┌─────────┐    ┌─────────┐
                    │ STEP 4  │───►│ STEP 5  │───►│ STEP 6  │
                    │CHALLENGE│    │SYNTHESIZE    │ OUTPUT  │
                    └─────────┘    └─────────┘    └─────────┘
```

---

## EXECUTION MODES

### Quick Explore (QE)
```
Time: 10-20 min | Steps: 0 (light) → 1 (focused) → 2 → 6
Triggers: `QE`, `quick explore`, `--quick`, `-q`
Output: Preliminary map with "QE limitations" noted
```

### Standard Explore (SE)
```
Time: 45-90 min | Steps: All (0-6)
Triggers: `DE`, `explore`, `--full`, default
Output: Full exploration report

NOTE ON "DE" TRIGGER: "DE" stands for "Deep Explore" (the tool name).
When used alone, it invokes Standard Explore (the default mode).
For Deep Explore mode, use `DE --deep` or `--strategic`.
```

### Deep Explore (DE)
```
Time: 2-4 hours | Steps: All + iterations + external research
Triggers: `DE --deep`, `--strategic`, `--critical`
Output: Comprehensive understanding with multiple passes
```

### Fear-Based Exploration (FE)
```
Time: 30-60 min | Steps: 0 (with E008-E014) → 1 → 4 → 6
Triggers: `FE`, `fear explore`, `--fear`, `--concerns`, `-f`
Output: Structured understanding of fears, risks, and paths forward

NOTE: FE skips Steps 2-3 (mapping). If you need BOTH fear analysis
AND option mapping, use FSE (Fearful Standard Exploration) mode.
```

### Fearful Standard Exploration (FSE) — Hybrid Mode
```
Time: 60-120 min | Steps: All (0-6) with E008-E014 in Step 0
Triggers: `FSE`, `--fear --full`, `-f --full`
Output: Full exploration report with fear resolution

When to use:
- User has fears AND needs comprehensive option mapping
- Complex decision with emotional and analytical components
- Want fear analysis but don't want to skip mapping phase

Combines:
- FE's fear methods (E008-E014) in Step 0
- SE's full step progression (0→1→2→3→4→5→6)
- Fear resolution in Step 4
- Fear Map in final report

When to use:
- User expresses uncertainty: "I don't know if this will work"
- User has concerns: "I'm worried about..."
- User sees blockers: "This seems impossible because..."
- User needs validation: "Am I crazy for thinking..."

Method selection in Step 0:
□ E008 Failure Reason Exploration — when fear is general/undefined
□ E009 Reverse Abduction — when user thinks something is impossible
□ E010 Cognitive MVP — when user is paralyzed by risk
□ E011 Control Analysis — when user worries about many things
□ E012 Fundamental Block — when user sees specific blockers
□ E013 Contrast Exploration — when user lacks context/examples
□ E014 Growth Test — when user questions if effort is worth it
```

---

## PARAMETERS

Deep Explore supports optional parameters for customization:

```
┌────────────────────┬─────────────────────┬────────────────────────────────────┐
│ Parameter          │ Values              │ Effect                             │
├────────────────────┼─────────────────────┼────────────────────────────────────┤
│ --max-iterations   │ 1-10 (default: 3)   │ Max feedback loop cycles           │
│ --depth            │ 1-5 (default: 3)    │ Methods per step (1=min, 5=max)    │
│ --focus            │ options|consequences│ Emphasize specific aspect          │
│                    │ |fears|risks|all    │                                    │
│ --output           │ markdown|json|brief │ Output format                      │
│ --domain           │ tech|business|      │ Load domain-specific patterns      │
│                    │ personal|policy     │                                    │
│ --verification     │ strict|balanced|fast│ How much to verify vs assume       │
│ --methods          │ E001,M001,... list  │ Explicit method selection          │
│ --skip-steps       │ 2,3,5 (step nums)   │ Skip specific steps                │
│ --timebox          │ 15m|30m|1h|2h       │ Time limit (triggers compression)  │
└────────────────────┴─────────────────────┴────────────────────────────────────┘
```

### Parameter Examples
```bash
# Quick with 15-minute timebox
claude "QE --timebox 15m: Which framework?"

# Standard with strict verification
claude "DE --verification strict: Architecture decision"

# Deep with specific method focus
claude "DE --deep --methods E001,E002,E006,M021: Market entry"

# Fear-based with business domain
claude "FE --domain business: Will my startup fail?"

# Hybrid with max iterations limit
claude "FSE --max-iterations 2: Career change decision"
```

### Iteration Control

Feedback loops can cycle between steps. To prevent infinite loops:

```
MAX ITERATIONS (--max-iterations, default: 3):
├── Iteration 1: Normal execution
├── Iteration 2: If gaps found, research and retry
├── Iteration 3: Final attempt
└── After max: PROCEED with current state + WARNING

When max iterations reached without resolution:
1. Note unresolved items in report
2. Mark affected consequences as ASSUMED
3. Add to "What We Still Don't Know" section
4. Suggest follow-up research in Next Steps
```

---

## CONTEXT BUDGET MANAGEMENT

LLMs have context window limits. Deep Explore manages this:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONTEXT BUDGET STRATEGY                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PRIORITY 1 (always include):                                               │
│  • Current step file                                                        │
│  • Active method procedure                                                  │
│  • Current artifacts (Maps, Queues)                                         │
│                                                                              │
│  PRIORITY 2 (include if space):                                             │
│  • Previous step outputs (summaries)                                        │
│  • User's original input                                                    │
│  • Research findings                                                        │
│                                                                              │
│  PRIORITY 3 (compress or summarize):                                        │
│  • Earlier step details                                                     │
│  • Intermediate reasoning                                                   │
│  • Raw research data                                                        │
│                                                                              │
│  COMPRESSION TRIGGERS:                                                       │
│  • After Step 2: Compress Step 0-1 to summaries                            │
│  • After Step 4: Compress Step 2-3 to key findings                         │
│  • Before Step 6: Compress all to report-ready format                      │
│                                                                              │
│  IF CONTEXT OVERFLOWS:                                                       │
│  1. Summarize oldest content first                                          │
│  2. Keep artifacts (Maps) intact                                            │
│  3. Note in report: "Context compressed at Step X"                          │
│  4. If critical info lost: Flag for multi-session exploration              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## QUICK EXECUTION PATH

**For most explorations, execute this sequence:**

```
📂 Step 0: KNOWLEDGE AUDIT
   Load: steps/step-00-knowledge-audit.md

   □ Frame the decision (one sentence)
   □ Assess stakes: LOW/MEDIUM/HIGH
   □ Inventory: Known Facts, Assumptions, Known Unknowns
   □ Surface Unknown Unknowns (use E001 Abductive Reasoning)
   □ Prioritize research needs

   IF USER HAS FEARS/CONCERNS (Fear-Based Mode):
   □ Apply E008 Failure Reason Exploration to structure fears
   □ Apply E011 Control Analysis to separate actionable concerns
   □ Apply E012 Fundamental Block Analysis to find true walls
   □ Apply E009 Reverse Abduction if user sees "impossible"
   □ Apply E013 Contrast Exploration to gain context
   → Fears become structured research queue

   Output: Knowledge Map + Research Queue (+ Fear Map if FE mode)

   ↓ PROCEED if research queue is defined
   ↓ STAY if framing is unclear

📂 Step 1: RESEARCH
   Load: steps/step-01-research.md

   □ Execute research queue by priority
   □ Use methods from: data/research-methods.md
   □ Record findings with sources
   □ Update Knowledge Map
   □ Add new unknowns to queue if discovered

   Output: Research Summary + Updated Knowledge Map

   ↓ PROCEED if critical unknowns addressed
   ↓ STAY if more research needed
   ↑ RETURN TO STEP 0 if framing changed

📂 Step 2: MAP (Divergent)
   Load: steps/step-02-map.md

   □ Load method: data/method-procedures/M001_Dimension_Discovery.md
   □ Discover dimensions (axes of choice)

   □ Load method: data/method-procedures/M002_Option_Enumeration.md
   □ Enumerate options per dimension

   □ Load method: data/method-procedures/M003_Constraint_Mapping.md
   □ Map hard and soft constraints

   □ Build Morphological Box

   Output: Option Map (draft)

   ↓ PROCEED if dimensions are complete
   ↑ RETURN TO STEP 1 if knowledge gaps found

📂 Step 3: DEEPEN
   Load: steps/step-03-deepen.md

   □ Apply E002 Counterfactual Thinking to key options
   □ Apply E004 Boundary Analysis to key options
   □ Apply E005 Causal Models to understand relationships

   □ Load method: data/method-procedures/M011_Consequence_Analysis.md
   □ Map consequences (mark VERIFIED vs ASSUMED)

   □ Load method: data/method-procedures/M012_Reversibility_Check.md
   □ Assess reversibility of each option

   □ Load method: data/method-procedures/M013_Dependency_Analysis.md
   □ Map decision dependencies

   Output: Consequence Map with verification status

   ↓ PROCEED if critical consequences verified
   ↑ RETURN TO STEP 1 if consequences need research

📂 Step 4: CHALLENGE (Adversarial)
   Load: steps/step-04-challenge.md

   □ Apply E006 Falsification to key beliefs

   □ Load method: data/method-procedures/M021_Premortem.md
   □ Imagine failure, trace causes

   □ Load method: data/method-procedures/M022_Black_Swan_Hunt.md
   □ Find low-probability high-impact events

   □ Load method: data/method-procedures/M023_Assumption_Stress_Test.md
   □ Break assumptions one by one

   □ Check for cognitive biases
   □ Update map based on findings

   IF FEAR-BASED EXPLORATION MODE:
   □ Apply E010 Cognitive MVP — find smallest test to learn
   □ Apply E014 Growth Test — assess if path develops user
   □ Revisit E008 risks — which are now addressed?
   □ Update Fear Map with verified/falsified concerns

   Output: Challenged map with strengthened/weakened items
           (+ Updated Fear Map with resolution status if FE mode)

   ↓ PROCEED always (challenge is mandatory)

📂 Step 5: SYNTHESIZE
   Load: steps/step-05-synthesize.md

   □ Apply E003 Minimal Assertions to compress insights
   □ Cluster natural strategic options
   □ Identify decision sequence (what first, what can wait)
   □ Assess decision readiness per item
   □ Apply E007 Information Questions for remaining gaps

   Output: Synthesis ready for report

   ↓ PROCEED to final output

📂 Step 6: OUTPUT
   Load: steps/step-06-output.md
   Load template: data/exploration-report-template.md

   □ Section 1: What We Learned
   □ Section 2: What We Still Don't Know
   □ Section 3: Option Map
   □ Section 4: Strategic Clusters
   □ Section 5: Consequence Map
   □ Section 6: Decision Readiness
   □ Section 7: Suggested Next Steps

   Output: EXPLORATION REPORT
```

---

## SCORING SYSTEM

### Exploration Coverage Score (C)

| Exploration Quality | Points | Notes |
|---------------------|--------|-------|
| New dimension discovered | +2 | Fundamental axis of choice |
| New option in dimension | +1 | Adds to possibility space |
| Consequence VERIFIED | +1 | Researched, not assumed |
| Consequence ASSUMED | +0.3 | Believed but not verified |
| Unknown Unknown surfaced | +1.5 | Discovered blind spot |
| Assumption falsified | +1 | Removed false belief |
| Boundary identified | +0.5 | Limit of applicability found |
| Causal relationship mapped | +0.5 | Influence understood |
| Fear classified (E008) | +0.5 | STRUCTURAL/OPERATIONAL/COGNITIVE |
| False wall identified (E012) | +1 | Blocker removed |
| True wall confirmed (E012) | +1 | Saved wasted effort |
| Controllable concern found (E011) | +0.5 | Actionable item identified |
| Success path discovered (E009) | +1.5 | New possibility revealed |
| Comparable analyzed (E013) | +0.5 | Context gained from others |

### Coverage Thresholds

| Score | Coverage Level | Meaning |
|-------|----------------|---------|
| C ≥ 25 | COMPREHENSIVE | Most of space explored |
| 15 ≤ C < 25 | ADEQUATE | Key areas covered |
| 8 ≤ C < 15 | PARTIAL | Major gaps likely |
| C < 8 | INSUFFICIENT | Premature to decide |

---

## METHOD RECOMMENDATION ENGINE

Based on input type and signals, prioritize specific methods:

### By Input Type

| Input Type | Recommended Methods | Rationale |
|------------|---------------------|-----------|
| Technical decision | E001, E004, M001, M011, M013 | Boundaries, dependencies matter |
| Business/strategy | E002, E005, E007, M021, M022 | Causation, black swans matter |
| Personal/life | E008-E014, E003, M012 | Fears, reversibility matter |
| Policy/governance | E006, M003, M023 | Falsification, constraints matter |
| Creative/product | E001, E002, M001, M002 | Hypotheses, options matter |

### By Signal Detection

| If you detect... | Add these methods | Why |
|------------------|-------------------|-----|
| User expresses fear/worry | E008, E011, E012 | Transform fear to map |
| User says "impossible" | E009, E012 | Find hidden paths |
| Many unknowns | E001, E007 | Generate hypotheses, prioritize |
| Complex dependencies | E005, M013 | Map causal structure |
| High stakes | M021, M022, M023 | Stress test everything |
| Time pressure | E003, E010 | Compress, find minimal tests |
| Conflicting info | E006, E004 | Falsify, find boundaries |
| User paralyzed | E010, E014 | Minimal action, growth frame |

### By Mode

| Mode | Core Methods | Optional Methods |
|------|--------------|------------------|
| QE | E001, M001, M002 | E007 (if time) |
| SE | E001-E007, M001-M023 | All available |
| DE | All + multiple passes | Deep dive any |
| FE | E008-E014, E001, E006 | M021 (for fears) |
| FSE | E001-E014, M001-M023 | All available |

### Method Selection Algorithm

```
1. DETECT mode from trigger
2. LOAD core methods for mode
3. SCAN input for signals (fear words, complexity markers, stakes)
4. ADD recommended methods based on signals
5. IF --methods parameter: OVERRIDE with explicit list
6. IF --depth parameter: LIMIT count per step
7. EXECUTE in step order
```

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EXPLORATION COMMANDMENTS (V2)                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. KNOWLEDGE BEFORE MAPPING                                                │
│     Never map options in a space you don't understand                       │
│     Step 0 + Step 1 are NOT optional                                        │
│                                                                              │
│  2. VERIFY BEFORE CLAIMING                                                  │
│     Mark every consequence as VERIFIED or ASSUMED                           │
│     Critical assumptions MUST be verified or flagged                        │
│                                                                              │
│  3. FEEDBACK LOOPS ARE MANDATORY                                            │
│     When you discover unknowns → go back and research                       │
│     Never proceed with false completeness                                   │
│                                                                              │
│  4. USE FOUNDATIONAL METHODS                                                │
│     Apply E001-E007 throughout exploration                                  │
│     Apply E008-E014 when user has fears/concerns                            │
│     These are not optional - they enable real exploration                   │
│                                                                              │
│  5. USER DECIDES, AI EXPLORES                                               │
│     Output is UNDERSTANDING, not recommendation                             │
│     Present options fairly, let user weigh trade-offs                       │
│                                                                              │
│  6. LOAD FILES WHEN NEEDED                                                  │
│     Announce: "📂 Loading [path]"                                           │
│     Follow the procedure in the loaded file                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FILE LOADING PROTOCOL

When you need specific data, announce and load:

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-knowledge-audit.md` | "📂 Loading Step 0: Knowledge Audit" |
| Start Step 1 | `steps/step-01-research.md` | "📂 Loading Step 1: Research" |
| Start Step 2 | `steps/step-02-map.md` | "📂 Loading Step 2: Map" |
| Start Step 3 | `steps/step-03-deepen.md` | "📂 Loading Step 3: Deepen" |
| Start Step 4 | `steps/step-04-challenge.md` | "📂 Loading Step 4: Challenge" |
| Start Step 5 | `steps/step-05-synthesize.md` | "📂 Loading Step 5: Synthesize" |
| Start Step 6 | `steps/step-06-output.md` | "📂 Loading Step 6: Output" |
| Execute method | `data/method-procedures/[ID]_[Name].md` | "📂 Loading method: [Name]" |
| Fear analysis | `data/method-procedures/E008_Failure_Reason_Exploration.md` | "📂 Loading: Failure Reason Exploration" |
| Reverse success | `data/method-procedures/E009_Reverse_Abduction.md` | "📂 Loading: Reverse Abduction" |
| Minimal test | `data/method-procedures/E010_Cognitive_MVP.md` | "📂 Loading: Cognitive MVP" |
| Control analysis | `data/method-procedures/E011_Control_Influence_Analysis.md` | "📂 Loading: Control Analysis" |
| Block analysis | `data/method-procedures/E012_Fundamental_Block_Analysis.md` | "📂 Loading: Fundamental Block Analysis" |
| Learn from others | `data/method-procedures/E013_Contrast_Exploration.md` | "📂 Loading: Contrast Exploration" |
| Growth filter | `data/method-procedures/E014_Growth_Test.md` | "📂 Loading: Growth Test" |
| Generate report | `data/exploration-report-template.md` | "📂 Loading report template" |
| Research guidance | `data/research-methods.md` | "📂 Loading research methods" |
| Scoring | `data/coverage-scoring.yaml` | "📂 Loading scoring rules" |

---

## DIRECTORY STRUCTURE

```
deep-explore-v2/
├── workflow.md                      ← YOU ARE HERE
├── data/
│   ├── method-procedures/                # Exploration methods
│   │   ├── E001_Abductive_Reasoning.md       # Foundational
│   │   ├── E002_Counterfactual_Thinking.md   # Foundational
│   │   ├── E003_Minimal_Assertions.md        # Foundational
│   │   ├── E004_Boundary_Analysis.md         # Foundational
│   │   ├── E005_Causal_Models.md             # Foundational
│   │   ├── E006_Falsification.md             # Foundational
│   │   ├── E007_Information_Questions.md     # Foundational
│   │   ├── E008_Failure_Reason_Exploration.md   # Fear-Based
│   │   ├── E009_Reverse_Abduction.md            # Fear-Based
│   │   ├── E010_Cognitive_MVP.md                # Fear-Based
│   │   ├── E011_Control_Influence_Analysis.md   # Fear-Based
│   │   ├── E012_Fundamental_Block_Analysis.md   # Fear-Based
│   │   ├── E013_Contrast_Exploration.md         # Fear-Based
│   │   ├── E014_Growth_Test.md                  # Fear-Based
│   │   ├── M001_Dimension_Discovery.md       # Mapping
│   │   ├── M002_Option_Enumeration.md        # Mapping
│   │   ├── M003_Constraint_Mapping.md        # Mapping
│   │   ├── M011_Consequence_Analysis.md      # Deepening
│   │   ├── M012_Reversibility_Check.md       # Deepening
│   │   ├── M013_Dependency_Analysis.md       # Deepening
│   │   ├── M021_Premortem.md                 # Challenge
│   │   ├── M022_Black_Swan_Hunt.md           # Challenge
│   │   └── M023_Assumption_Stress_Test.md    # Challenge
│   ├── research-methods.md              # How to research unknowns
│   ├── coverage-scoring.yaml            # Scoring rules
│   ├── exploration-report-template.md   # Output format
│   └── examples.md                      # Worked examples
└── steps/
    ├── step-00-knowledge-audit.md
    ├── step-01-research.md
    ├── step-02-map.md
    ├── step-03-deepen.md
    ├── step-04-challenge.md
    ├── step-05-synthesize.md
    └── step-06-output.md
```

---

## CLI INVOCATION EXAMPLES

### Claude CLI
```bash
# Quick explore
claude "QE: Should we use TypeScript or Python for this project?" < context.md

# Standard explore
claude "DE: Explore product strategy for Deep Verify" \
  --context requirements.md market_research.md

# Deep explore
claude "DE --deep: Strategic decision about market entry" < business_context.md

# Fear-based exploration
claude "FE: I'm worried my startup idea won't work" < my_idea.md

# Fear-based with specific concern
claude "FE: This feels impossible - no one will pay for this" < product_spec.md
```

### With Deep Verify
```bash
# Explore then verify chosen option
claude "DE: Architecture options for API" < requirements.md > exploration.md
# User reviews, decides on option
claude "DV: Verify REST API design" < api_design.md
```

---

## VERSION HISTORY

- **V2.1** — Fear-Based Exploration mode
  - Added fear-based methods (E008-E014)
  - Added Fear-Based Exploration (FE) execution mode
  - Updated Step 0 to handle fears/concerns
  - Updated Step 4 to resolve fears with evidence
  - Methods: Failure Reason, Reverse Abduction, Cognitive MVP,
    Control Analysis, Fundamental Block, Contrast, Growth Test

- **V2.0** — Knowledge-first approach with epistemological foundations
  - Added foundational methods (E001-E007)
  - Added Step 0: Knowledge Audit
  - Added Step 1: Research
  - Added feedback loops between steps
  - Added VERIFIED/ASSUMED distinction
  - Changed output from MAP to UNDERSTANDING
  - Added coverage scoring system
