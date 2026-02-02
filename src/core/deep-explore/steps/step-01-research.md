# Step 01: Research

## Purpose

Fill critical knowledge gaps identified in Step 0 BEFORE mapping options.

**Time:** 15-30 min (Quick), 1-2 hours (Standard)

**Inputs:** Research Queue from Step 0, Knowledge Map

**Outputs:** Research Summary, Updated Knowledge Map

---

## Procedure

### 01.1 Execute Research Queue

📂 Load: `data/research-methods.md`

For each item in Research Queue by priority:

```
┌─────────────────────────────────────────────────────────────────┐
│  RESEARCH ITEM: [question]                                      │
├─────────────────────────────────────────────────────────────────┤
│  METHOD: [web search / docs / experiment / ask expert]         │
│  TIME: [X min]                                                  │
│                                                                  │
│  FINDINGS:                                                       │
│  • [finding] - source: [url/reference]                          │
│  • [finding] - source: [url/reference]                          │
│                                                                  │
│  CONFIDENCE: [HIGH / MED / LOW]                                 │
│  NEW QUESTIONS: [any new unknowns discovered]                   │
│  IMPACT: [how this changes understanding]                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 01.2 Handle Research Outcomes

```
CLEAR ANSWER:
→ Move to KNOWN FACTS with source
→ Remove from unknowns

PARTIAL ANSWER:
→ Record what was learned
→ Mark confidence level
→ Decide: research more or accept partial?

CONFLICTING INFO:
→ Record all positions
→ Note conflict explicitly
→ Assess reliability of sources

NO INFO FOUND:
→ Mark as TRUE UNKNOWN
→ Assess: can we proceed without this?
→ Flag for expert if critical

NEW QUESTIONS:
→ Assess priority
→ Add to queue if HIGH priority
→ Park if LOW priority
```

### 01.3 Update Knowledge Map

```
MOVE TO KNOWN FACTS:
+ [finding] - source: [reference]

UPDATE ASSUMPTIONS:
~ [assumption] - confidence now: [new level]

REMOVE FROM UNKNOWNS:
- [question] - answered by: [reference]

ADD TO UNKNOWNS:
+ [new question] - priority: [P1-P4]
```

---

## Output: Research Summary

```
╔═══════════════════════════════════════════════════════════════╗
║  RESEARCH SUMMARY                                              ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Items Researched:      [count]                                ║
║  Time Spent:            [X hours]                              ║
║                                                                ║
║  KEY LEARNINGS:                                                 ║
║  • [learning 1] - impact: ___                                  ║
║  • [learning 2] - impact: ___                                  ║
║                                                                ║
║  Verified (HIGH confidence):    [count]                        ║
║  Partial (MED confidence):      [count]                        ║
║  Unknown (cannot determine):    [count]                        ║
║                                                                ║
║  New Questions Discovered:      [count]                        ║
║  Flagged for Expert:            [count]                        ║
║                                                                ║
║  PROCEED TO STEP 2? [YES/NO]                                  ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Iteration Tracking

```
ITERATION CHECK:
Current iteration: [N] of max [quick:1 / standard:3 / deep:10]

□ If max iterations reached AND critical unknowns remain:
  → Proceed anyway, flag unknowns as TRUE UNCERTAINTY
  → Or ABORT if unknowns are decision-critical
```

---

## Transition

- **If critical unknowns addressed** → Proceed to Step 2
- **If more research needed AND iterations remaining** → Stay in Step 1
- **If more research needed BUT max iterations reached** → Proceed with unknowns flagged
- **If framing changed** → Return to Step 0
- **If research reveals decision should not be made** → ABORT (return to Step 0)
