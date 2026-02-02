# Step 00: SCOPE

## Purpose

Define WHAT you're synthesizing, WHY, for WHOM, and at what LEVEL of abstraction. Bounding the synthesis prevents infinite scope and the Frame Problem.

**Time:** 15-30 min (Standard), 10 min (Quick)

**Inputs:** Synthesis request, context, available source indicators

**Outputs:** Synthesis Question, Level Selection, Source Landscape Map

---

## Procedure

### 00.1 Synthesis Question Formulation (#001)

📂 Load method: `data/method-procedures/001_Synthesis_Question_Formulation.md`

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    SYNTHESIS QUESTION FORMULATION                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  SYNTHESIS QUESTION:                                                       ║
║  "What do the combined [sources] tell us about [topic] for [purpose]?"    ║
║                                                                            ║
║  ________________________________________________________________________  ║
║                                                                            ║
║  QUALITY CHECKS:                                                           ║
║  □ Is it ANSWERABLE? (Not too broad, not too vague)                       ║
║  □ Does it require MULTIPLE sources? (If one source answers it,           ║
║    you don't need synthesis)                                               ║
║  □ Does it seek INTEGRATION, not just collection?                         ║
║    (Pattern, principle, framework — not just a list)                      ║
║                                                                            ║
║  WHAT WOULD A GOOD ANSWER LOOK LIKE?                                      ║
║  Form: [ ] Framework [ ] Principle set [ ] Mental model [ ] Narrative     ║
║  Length: [ ] Abstract (100w) [ ] Summary (500w) [ ] Full document         ║
║  Confidence: [ ] High certainty [ ] Best current understanding [ ] Hypothesis ║
║                                                                            ║
║  BAD QUESTIONS (avoid):                                                    ║
║  ✗ "What do we know?" (unbounded)                                         ║
║  ✗ "Summarize these documents" (not synthesis, just summarization)        ║
║  ✗ "Is this good?" (too vague, not about knowledge integration)           ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

### 00.2 Level-of-Analysis Selection (#002)

📂 Load method: `data/method-procedures/002_Level_of_Analysis_Selection.md`

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    LEVEL-OF-ANALYSIS SELECTION                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ABSTRACTION LEVELS:                                                       ║
║  ┌────────────────┬─────────────────────────────────────┬───────────────┐ ║
║  │ Level          │ Description                          │ Risk          │ ║
║  ├────────────────┼─────────────────────────────────────┼───────────────┤ ║
║  │ ATOMIC         │ Individual facts, events, data points│ Atomistic     │ ║
║  │                │ "Server X crashed at 14:32"          │ fallacy       │ ║
║  ├────────────────┼─────────────────────────────────────┼───────────────┤ ║
║  │ PATTERN        │ Recurring relationships across atoms │ Correlation   │ ║
║  │                │ "Crashes correlate with memory"      │ ≠ causation   │ ║
║  ├────────────────┼─────────────────────────────────────┼───────────────┤ ║
║  │ STRUCTURAL     │ Underlying mechanisms and models     │ Model may     │ ║
║  │                │ "Memory leak causes cascading fail"  │ not match     │ ║
║  ├────────────────┼─────────────────────────────────────┼───────────────┤ ║
║  │ SYSTEMIC       │ System-wide dynamics and behaviors   │ Ecological    │ ║
║  │                │ "Our incident response is reactive"  │ fallacy       │ ║
║  ├────────────────┼─────────────────────────────────────┼───────────────┤ ║
║  │ PARADIGMATIC   │ Fundamental assumptions/worldviews   │ Hard to       │ ║
║  │                │ "We treat reliability as a feature"  │ detect        │ ║
║  └────────────────┴─────────────────────────────────────┴───────────────┘ ║
║                                                                            ║
║  TARGET LEVEL FOR THIS SYNTHESIS: [ ] Atomic [ ] Pattern [ ] Structural   ║
║                                   [ ] Systemic [ ] Paradigmatic           ║
║                                                                            ║
║  SOURCE LEVELS:                                                            ║
║  • Source 1 operates at: _____________ level                              ║
║  • Source 2 operates at: _____________ level                              ║
║  • Source 3 operates at: _____________ level                              ║
║                                                                            ║
║  ⚠️ WARNING: If sources operate at DIFFERENT levels:                       ║
║  → They need ALIGNMENT before synthesis                                   ║
║  → Conclusions may NOT TRANSFER between levels                            ║
║  → Same data can produce CONTRADICTORY conclusions at different levels    ║
║                                                                            ║
║  CROSS-LEVEL INTERACTIONS:                                                 ║
║  □ Any atomic detail that changes systemic understanding?                 ║
║  □ Any systemic insight that reframes atomic facts?                       ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

### 00.3 Source Landscape Mapping (#003)

📂 Load method: `data/method-procedures/003_Source_Landscape_Mapping.md`

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    SOURCE LANDSCAPE MAPPING                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  SOURCE TYPES — What kinds of knowledge exist for this question?          ║
║                                                                            ║
║  ┌───────────────────┬───────────┬───────────┬───────────────────────────┐║
║  │ Type              │ Available │ Relevant  │ Gap?                      │║
║  ├───────────────────┼───────────┼───────────┼───────────────────────────┤║
║  │ Empirical data    │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Expert knowledge  │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Documented procs  │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Academic/research │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Experiential      │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Theoretical       │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Tacit knowledge   │ Y/N/?     │ Y/N       │ _________________________ │║
║  │ Cross-domain      │ Y/N/?     │ Y/N       │ _________________________ │║
║  └───────────────────┴───────────┴───────────┴───────────────────────────┘║
║                                                                            ║
║  DIVERSITY AUDIT:                                                          ║
║  □ Multiple perspectives represented?                                      ║
║  □ Multiple methods represented?                                           ║
║  □ Multiple domains contributing?                                          ║
║                                                                            ║
║  STREETLIGHT CHECK:                                                        ║
║  "Are we looking where the knowledge IS, or only where it's convenient?"  ║
║                                                                            ║
║  Known sources we're NOT including (and why):                             ║
║  1. _______________ because _______________                               ║
║  2. _______________ because _______________                               ║
║                                                                            ║
║  LANDSCAPE SUMMARY:                                                        ║
║  • Source types needed: _____________________________________________     ║
║  • Source types available: __________________________________________     ║
║  • Critical gaps: ___________________________________________________     ║
║  • Streetlight risk: [ ] LOW [ ] MEDIUM [ ] HIGH                          ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Output: Scope Definition

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  SCOPE DEFINITION                                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  SYNTHESIS QUESTION:                                                       ║
║  ____________________________________________________________________     ║
║  ____________________________________________________________________     ║
║                                                                            ║
║  LEVEL OF ANALYSIS:                                                        ║
║  Target: ________________                                                  ║
║  Source alignment needed: [ ] YES [ ] NO                                   ║
║                                                                            ║
║  SOURCE LANDSCAPE:                                                         ║
║  • Types needed: ________________________________________________         ║
║  • Gaps identified: _____________________________________________         ║
║  • Diversity status: [ ] ADEQUATE [ ] NEEDS IMPROVEMENT                   ║
║                                                                            ║
║  ANSWER FORM EXPECTED:                                                     ║
║  • Format: ___________________                                             ║
║  • Length: ___________________                                             ║
║  • Confidence target: ___________________                                  ║
║                                                                            ║
║  PROCEED TO STEP 1? [ ] YES [ ] NO (refine scope)                         ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Transition

- **If scope is clear** → Proceed to Step 1 (ACQUIRE)
- **If question too broad** → Decompose into sub-questions, repeat #001
- **If level unclear** → Clarify with stakeholder, repeat #002
- **If landscape unmapped** → Complete #003 before proceeding
