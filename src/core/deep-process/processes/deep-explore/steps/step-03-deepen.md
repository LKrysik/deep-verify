# Step 03: Deepen

## Purpose

Understand consequences at multiple abstraction levels.

**Time:** 20-40 min

**Inputs:** Option Map from Step 2

**Outputs:** Consequence Map with VERIFIED/ASSUMED status

---

## Procedure

### 03.1 Abstraction Navigation

For key options, explore multiple levels:

```
ZOOM OUT (WHY):
• "Why does this option exist?"
• "What higher goal does it serve?"
• "Are we solving the right problem?"

CURRENT (WHAT):
• "What is this option?"
• "What are the trade-offs?"

DRILL DOWN (HOW):
• "How would we implement this?"
• "What skills/resources needed?"
• "What could go wrong?"

DRILL DEEPER (DETAILS):
• "What specific tools/technologies?"
• "What integrations needed?"
• "What's the learning curve?"
```

### 03.2 Apply Foundational Methods

📂 Load method: `data/method-procedures/E002_Counterfactual_Thinking.md`

For key options, ask:
- "What would NOT happen if this option didn't exist?"
- "Which elements are NECESSARY vs NICE-TO-HAVE?"

📂 Load method: `data/method-procedures/E004_Boundary_Analysis.md`

For key options, ask:
- "Where does this option stop working?"
- "What are the limits?"

📂 Load method: `data/method-procedures/E005_Causal_Models.md`

Build causal model:
- "What influences what?"
- "Where are the leverage points?"

### 03.3 Consequence Analysis

📂 Load method: `data/method-procedures/M011_Consequence_Analysis.md`

For each significant option/combination:

```
┌─────────────────────────────────────────────────────────────────┐
│  OPTION: [description]                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IMMEDIATE CONSEQUENCES:                                         │
│  ├── Gain: [what] - [VERIFIED/ASSUMED]                          │
│  ├── Cost: [what] - [VERIFIED/ASSUMED]                          │
│  └── Risk: [what] - [VERIFIED/ASSUMED]                          │
│                                                                  │
│  DOWNSTREAM CONSEQUENCES:                                        │
│  ├── Opens: [possibilities] - [VERIFIED/ASSUMED]                │
│  ├── Closes: [possibilities] - [VERIFIED/ASSUMED]               │
│  └── Requires: [next steps] - [VERIFIED/ASSUMED]                │
│                                                                  │
│  VERIFICATION REQUIREMENT:                                       │
│  Critical ASSUMED consequences → Return to Step 1               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 03.4 Reversibility Check

📂 Load method: `data/method-procedures/M012_Reversibility_Check.md`

```
REVERSIBILITY: [HIGH / MEDIUM / LOW / IRREVERSIBLE]

HIGH = Can change with minimal cost
MEDIUM = Can change with significant cost
LOW = Very difficult to change
IRREVERSIBLE = Cannot undo

POINT OF NO RETURN: [when does this become hard to reverse?]
```

### 03.5 Dependency Analysis

📂 Load method: `data/method-procedures/M013_Dependency_Analysis.md`

```
DECISION DEPENDENCIES:
├── [Decision A] blocks [Decision B]
├── [Decision C] requires [Decision A] first
└── [Decision D] can be made independently

EXTERNAL DEPENDENCIES:
• [dependency] - controlled by: [who]
```

---

## Feedback Loop Check

```
□ Did deepening reveal consequences we can't assess?
  → YES: Return to Step 1 (if iterations remaining)

□ Are critical consequences still ASSUMED?
  → YES: Return to Step 1 to verify (if iterations remaining)

□ Did we discover the problem is different?
  → YES: Return to Step 0

□ Are ALL options' consequences unacceptable?
  → YES: Consider ABORT - no good path exists

□ PROCEED TO STEP 4? [YES/NO]
```

---

## Iteration Tracking

```
VERIFICATION LOOP COUNT: [N]

□ If returning to Step 1 more than [quick:1 / standard:2 / deep:3] times:
  → STOP: Proceed with ASSUMED consequences marked as risks
  → Perfect information is often unattainable
```

---

## Transition

- **If consequences verified** → Proceed to Step 4
- **If verification needed AND iterations remaining** → Return to Step 1
- **If verification needed BUT max loops reached** → Proceed with assumptions flagged
- **If reframe needed** → Return to Step 0
- **If all consequences unacceptable** → Consider ABORT (return to Step 0)
