# Step 00: Knowledge Audit

## Purpose

Map what you know and don't know BEFORE exploring options.

**Time:** 10-15 min (Standard), 5 min (Quick)

**Inputs:** User's decision/question, context provided

**Outputs:** Knowledge Map, Research Queue

---

## Procedure

### 00.1 Frame the Decision

```
DECISION STATEMENT:
"We need to decide: _______________________________________"

STAKES: [ ] HIGH  [ ] MEDIUM  [ ] LOW

WHY IT MATTERS:
• Good outcome: ________________________________________
• Bad outcome: _________________________________________
• Not deciding: ________________________________________
```

### 00.2 Inventory Known Knowledge

```
KNOWN FACTS (certain, with evidence):
┌─────────────────────────────────────────────────────────────────┐
│ Fact                              │ Source/Evidence             │
├───────────────────────────────────┼─────────────────────────────┤
│                                   │                             │
│                                   │                             │
└───────────────────────────────────┴─────────────────────────────┘

ASSUMPTIONS (believed, not verified):
┌─────────────────────────────────────────────────────────────────┐
│ Assumption                        │ Confidence  │ Verify?       │
├───────────────────────────────────┼─────────────┼───────────────┤
│                                   │ HIGH/MED/LOW│ Y/N           │
│                                   │ HIGH/MED/LOW│ Y/N           │
└───────────────────────────────────┴─────────────┴───────────────┘

KNOWN UNKNOWNS (questions you have):
┌─────────────────────────────────────────────────────────────────┐
│ Question                          │ Importance  │ Can research? │
├───────────────────────────────────┼─────────────┼───────────────┤
│                                   │ HIGH/MED/LOW│ Y/N           │
│                                   │ HIGH/MED/LOW│ Y/N           │
└───────────────────────────────────┴─────────────┴───────────────┘
```

### 00.3 Surface Unknown Unknowns

**Knowledge categories:**
- **Known Facts** = Things you know and can verify
- **Assumptions** = Things you believe but haven't verified
- **Known Unknowns** = Questions you know you have
- **Unknown Unknowns** = Blind spots you don't know exist yet

This step targets **Unknown Unknowns** — the most dangerous category because
you can't research what you don't know to ask about.

📂 Load method: `data/method-procedures/E001_Abductive_Reasoning.md`

Use abductive reasoning to discover blind spots:

```
PROMPT 1: DOMAIN EXPERTISE GAP
"What would someone with 10 years experience in [domain] know
that a newcomer typically doesn't?"

PROMPT 2: COMMON MISTAKES
"What are the most common mistakes people make when deciding
about [decision area]?"

PROMPT 3: HIDDEN DEPENDENCIES
"What external factors affect [decision] that aren't obvious?"

PROMPT 4: TECHNICAL CONSTRAINTS
"What technical limitations exist that could eliminate options?"

PROMPT 5: ECOSYSTEM STATE
"What is the current state of [relevant market/technology]?
What has changed recently?"
```

For each prompt, list discoveries and add to Known Unknowns.

### 00.4 Prioritize Research Needs

```
                      IMPACT ON DECISION
                    HIGH              LOW
         ┌─────────────────────┬─────────────────────┐
    HIGH │  P1: MUST RESEARCH  │  P3: IF TIME        │
  EFFORT ├─────────────────────┼─────────────────────┤
    LOW  │  P2: MUST RESEARCH  │  P4: SKIP           │
         └─────────────────────┴─────────────────────┘

RESEARCH QUEUE:
1. [unknown] - priority: P1/P2 - method: ___
2. [unknown] - priority: P1/P2 - method: ___
3. ...
```

---

## 00.5 Fear Analysis (when fear_analysis=on)

**Triggered when:** User expresses uncertainty, fear, or sees blockers. Automatically enabled with `--fear` flag.

📂 Load method: `data/method-procedures/E008_Failure_Reason_Exploration.md`

**Note:** E008 uses the UNIFIED FAILURE TAXONOMY (shared with M021 Premortem in Step 4).
Use E008 here for vague fears; M021 later for specific option stress-testing.

```
FEAR INVENTORY:
"What am I afraid will go wrong?"

┌─────────────────────────────────────────────────────────────────┐
│ Fear                          │ Type        │ Status            │
├───────────────────────────────┼─────────────┼───────────────────┤
│                               │ STRUCTURAL  │ BLOCKER/OK        │
│                               │ OPERATIONAL │ ADDRESSABLE       │
│                               │ EXTERNAL    │ MONITOR           │
│                               │ COGNITIVE   │ VERIFY/DISMISS    │
└───────────────────────────────┴─────────────┴───────────────────┘

UNIFIED TYPE KEY (used by E008 and M021):
• STRUCTURAL = Hard limits (physics, law, economics) → cannot work around
• OPERATIONAL = Constraints (resources, skills, time) → can potentially address
• EXTERNAL = Outside control (market, technology, stakeholders) → monitor + contingency
• COGNITIVE = Assumptions (untested beliefs, biases) → verify or dismiss
```

📂 Load method: `data/method-procedures/E011_Control_Influence_Analysis.md`

```
CONTROL ANALYSIS:
For each concern, classify:

┌─────────────────────────────────────────────────────────────────┐
│ Concern                       │ Zone        │ Response          │
├───────────────────────────────┼─────────────┼───────────────────┤
│                               │ CTRL/INF/NO │ [action]          │
│                               │ CTRL/INF/NO │ [action]          │
└───────────────────────────────┴─────────────┴───────────────────┘

ZONE KEY:
• CTRL = Control (you can directly change)
• INF = Influence (you can affect but not control)
• NO = No Control (accept or ignore)
```

📂 Load method: `data/method-procedures/E012_Fundamental_Block_Analysis.md`

```
BLOCKER ANALYSIS:
"What do I think makes this impossible?"

┌─────────────────────────────────────────────────────────────────┐
│ Suspected Wall                │ Status      │ Workaround        │
├───────────────────────────────┼─────────────┼───────────────────┤
│                               │ TRUE/FALSE  │                   │
│                               │ /MOVEABLE   │                   │
└───────────────────────────────┴─────────────┴───────────────────┘
```

📂 Load method: `data/method-procedures/E009_Reverse_Abduction.md` (if user sees "impossible")

```
IF USER THINKS SOMETHING IS IMPOSSIBLE:

"If this worked, what would need to be true?"

REQUIRED CONDITIONS FOR SUCCESS:
1. ___
2. ___
3. ___

Which conditions are actually achievable? [list]
```

📂 Load method: `data/method-procedures/E013_Contrast_Exploration.md`

```
CONTRAST ANALYSIS:
"Who has done something similar? What can I learn from them?"

┌─────────────────────────────────────────────────────────────────┐
│ Comparable                    │ Outcome     │ Key Lesson        │
├───────────────────────────────┼─────────────┼───────────────────┤
│                               │ SUCCESS/FAIL│                   │
│                               │ SUCCESS/FAIL│                   │
└───────────────────────────────┴─────────────┴───────────────────┘

MY POSITION:
• Similar to [who] because: ___
• Different because: ___
• Key advantage I have: ___
• Key risk I share: ___
```

**Add fear-related items to Research Queue.**

---

## Output: Knowledge Map

```
╔═══════════════════════════════════════════════════════════════╗
║  KNOWLEDGE MAP                                                 ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  DECISION: ________________________________________           ║
║  STAKES: [ ] HIGH  [ ] MEDIUM  [ ] LOW                        ║
║                                                                ║
║  Known Facts:           [count]                                ║
║  Assumptions:           [count] (need verify: [count])        ║
║  Known Unknowns:        [count]                                ║
║  Discovered Unknowns:   [count]                                ║
║                                                                ║
║  Research Queue:        [count] items                          ║
║                                                                ║
║  PROCEED TO STEP 1? [YES/NO]                                  ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

## Output: Fear Map (when fear_analysis=on)

```
╔═══════════════════════════════════════════════════════════════╗
║  FEAR MAP                                                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  FEARS INVENTORIED: [count]                                   ║
║    • Structural: [count]                                       ║
║    • Operational: [count]                                      ║
║    • Cognitive: [count]                                        ║
║                                                                ║
║  CONTROL ANALYSIS:                                             ║
║    • Controllable: [count] → add to action list               ║
║    • Influenceable: [count] → do best effort                  ║
║    • No control: [count] → accept or ignore                   ║
║                                                                ║
║  BLOCKERS ANALYZED: [count]                                   ║
║    • True walls: [count] → pivot or stop                      ║
║    • False walls: [count] → proceed                           ║
║    • Moveable walls: [count] → research how to move           ║
║                                                                ║
║  FEAR-RELATED RESEARCH: [count] items added to queue          ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Transition

- **If research queue has items** → Proceed to Step 1
- **If research queue is empty** → Skip to Step 2 (rare)
- **If frame is unclear** → Stay in Step 0, refine
- **If decision should not be made** → ABORT exploration (see below)

---

## ABORT: When NOT to Decide

Sometimes exploration reveals the decision should not be made at all. Valid reasons to ABORT:

```
□ PREMATURE: Critical information unavailable and cannot be obtained
  → Output: "Wait until [condition] before deciding"

□ WRONG QUESTION: The framed decision is not the real problem
  → Output: "Reframe to [better question] instead"

□ EXTERNAL DEPENDENCY: Decision depends on someone else's action first
  → Output: "Blocked by [dependency], escalate to [who]"

□ NO VIABLE OPTIONS: All options have unacceptable consequences
  → Output: "No good options exist, consider [alternatives]"
```

**ABORT OUTPUT:**
```
╔═══════════════════════════════════════════════════════════════╗
║  EXPLORATION ABORTED                                           ║
╠═══════════════════════════════════════════════════════════════╣
║  REASON: [PREMATURE / WRONG QUESTION / EXTERNAL / NO OPTIONS] ║
║  RECOMMENDATION: [what to do instead]                          ║
║  REVISIT WHEN: [condition for re-exploration]                  ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Escalation: When Stuck in Step 0

If frame remains unclear after 3 attempts:

1. **Simplify**: Break into smaller sub-decisions
2. **Consult**: Ask user for clarification or external input
3. **Pivot**: Try different framing angle
4. **Abort**: If still unclear, decision may be premature
