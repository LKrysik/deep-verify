# Step 02: Map (Divergent)

## Purpose

Now that we understand the space, map the options systematically.

**Time:** 15-30 min

**Inputs:** Knowledge Map, Research Summary

**Outputs:** Option Map (Morphological Box)

---

## Procedure

### 02.1 Dimension Discovery

📂 Load method: `data/method-procedures/M001_Dimension_Discovery.md`

A DIMENSION is an axis of choice - a category where you must pick one option.

```
DISCOVERY QUESTIONS:
• "What choices emerged from our research?"
• "What are the fundamental axes?"
• "What would an expert add?"

DIMENSIONS FOUND:
├── Dimension 1: [name] - type: [INDEPENDENT/DEPENDENT]
├── Dimension 2: [name] - type: [INDEPENDENT/DEPENDENT]
├── Dimension 3: [name] - type: [INDEPENDENT/DEPENDENT]
└── ...

QUALITY CHECK:
□ At least 3 dimensions?
□ Each dimension has at least 2 options?
□ Dimensions are truly independent?
```

### 02.2 Option Enumeration

📂 Load method: `data/method-procedures/M002_Option_Enumeration.md`

For each dimension, list ALL options:

```
DIMENSION: [name]
├── Option A: [description] - source: [where from?]
├── Option B: [description] - source: [where from?]
├── Option C: [description] - source: [where from?]
└── [Missing options? Apply expansion prompts]

EXPANSION PROMPTS:
• "What would a contrarian choose?"
• "What's the unconventional choice?"
• "What if we combined options?"
• "What's the 'do nothing' option?"
```

### 02.3 Constraint Mapping

📂 Load method: `data/method-procedures/M003_Constraint_Mapping.md`

```
HARD CONSTRAINTS (eliminate combinations):
┌─────────────────────────────────────────────────────────────────┐
│ Constraint                        │ Confidence  │ Source        │
├───────────────────────────────────┼─────────────┼───────────────┤
│ [D1:A + D2:B] impossible because..│ HIGH/MED/LOW│ VERIFIED/ASSUMED│
│                                   │             │               │
└───────────────────────────────────┴─────────────┴───────────────┘

SOFT CONSTRAINTS (reduce attractiveness):
• [Combination] = DIFFICULT because [reason]
```

### 02.4 Build Morphological Box

**What is a Morphological Box?**
A visualization tool (from Zwicky's morphological analysis) that shows all dimensions
as rows and all options per dimension as columns. It makes the full decision space
visible and helps identify valid/invalid combinations.

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
║  CONSTRAINTS:                                                              ║
║  • [constraint 1] - confidence: [level]                                   ║
║                                                                            ║
║  VALID COMBINATIONS: [N] of [total]                                        ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Feedback Loop Check

```
□ Did mapping reveal new unknowns?
  → YES: Return to Step 1

□ Did mapping reveal we misunderstood the problem?
  → YES: Return to Step 0

□ Is the map suspiciously simple?
  → YES: Challenge - are we missing dimensions?

□ PROCEED TO STEP 3? [YES/NO]
```

---

## Transition

- **If map is complete** → Proceed to Step 3
- **If knowledge gaps found** → Return to Step 1
- **If framing wrong** → Return to Step 0
