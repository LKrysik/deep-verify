# Step 05: Synthesize

## Purpose

Organize findings into actionable understanding.

**Time:** 10-15 min

**Inputs:** Challenged Option Map, Consequence Map

**Outputs:** Synthesis ready for final report

---

## Procedure

### 05.1 Compress to Minimal Assertions

📂 Load method: `data/method-procedures/E003_Minimal_Assertions.md`

Compress insights to essential principles:

```
RAW INSIGHTS FROM EXPLORATION:
[list all key findings]

COMPRESSION:
For each insight, ask: "Can I say this in half the words?"

MINIMAL ASSERTIONS:
1. "[compressed principle 1]"
   └── Useful for: [what decision]

2. "[compressed principle 2]"
   └── Useful for: [what decision]

3. "[compressed principle 3]"
   └── Useful for: [what decision]
```

### 05.2 Cluster Strategic Options

#### Clustering Criteria

Use these criteria to identify natural clusters in your option space:

```
CLUSTERING ALGORITHM:

1. IDENTIFY CLUSTERING DIMENSIONS
   Ask: "Which choices most affect everything else?"

   CLUSTERING DIMENSION: [the most consequential axis]
   └── Why: [how it affects other dimensions]

2. GROUP BY SHARED CHARACTERISTICS
   Options naturally cluster when they share:

   □ RISK PROFILE — similar risk/reward balance
   □ RESOURCE NEED — similar investment required
   □ REVERSIBILITY — similar ability to change later
   □ SPEED — similar time to implement/results
   □ PHILOSOPHY — similar underlying approach

3. NAME CLUSTERS DESCRIPTIVELY
   Good names capture the essence:
   ├── "Conservative Path" vs "Aggressive Path"
   ├── "Build" vs "Buy" vs "Partner"
   ├── "Fast & Risky" vs "Slow & Safe"
   └── "All-in" vs "Hedge" vs "Wait & See"

4. VALIDATE CLUSTERS
   □ Do options within cluster feel similar?
   □ Do options across clusters feel different?
   □ Would choosing Cluster A eliminate Cluster B options?
   □ Are there 2-5 clusters (not 1, not 10)?
```

#### Cluster Template

```
CLUSTER A: "[descriptive name]"
├── Configuration: [D1:X + D2:Y + ...]
├── Core philosophy: [underlying approach]
├── Best for: [what situation]
├── Requires: [resources, skills, conditions]
├── Risk profile: [HIGH/MED/LOW]
├── Reversibility: [HIGH/MED/LOW/IRREVERSIBLE]
├── Time to results: [fast/medium/slow]
└── Key trade-off: [what you sacrifice]

CLUSTER B: "[descriptive name]"
├── Configuration: [D1:A + D2:B + ...]
├── Core philosophy: [underlying approach]
├── Best for: [what situation]
├── Requires: [resources, skills, conditions]
├── Risk profile: [HIGH/MED/LOW]
├── Reversibility: [HIGH/MED/LOW/IRREVERSIBLE]
├── Time to results: [fast/medium/slow]
└── Key trade-off: [what you sacrifice]

CLUSTER C: "[descriptive name]" (if applicable)
├── [same structure]
└── ...
```

#### Cluster Comparison Matrix

```
┌─────────────────┬───────────────┬───────────────┬───────────────┐
│ Criterion       │ Cluster A     │ Cluster B     │ Cluster C     │
├─────────────────┼───────────────┼───────────────┼───────────────┤
│ Risk            │ HIGH/MED/LOW  │ HIGH/MED/LOW  │ HIGH/MED/LOW  │
│ Investment      │ $$$           │ $$            │ $             │
│ Time to results │ fast/med/slow │ fast/med/slow │ fast/med/slow │
│ Reversibility   │ HIGH/MED/LOW  │ HIGH/MED/LOW  │ HIGH/MED/LOW  │
│ Upside          │ HIGH/MED/LOW  │ HIGH/MED/LOW  │ HIGH/MED/LOW  │
│ Complexity      │ HIGH/MED/LOW  │ HIGH/MED/LOW  │ HIGH/MED/LOW  │
└─────────────────┴───────────────┴───────────────┴───────────────┘

BEST CLUSTER FOR:
• Maximize upside: Cluster ___
• Minimize risk: Cluster ___
• Move fast: Cluster ___
• Preserve optionality: Cluster ___
```

#### Independent Decisions

```
INDEPENDENT DECISIONS (not tied to cluster choice):
• [decision] - can be made regardless of cluster
• [decision] - orthogonal to main choice

WHY INDEPENDENT:
• No dependency on cluster dimensions
• Can be combined with any cluster
• Often: timing, communication, process decisions
```

### 05.3 Decision Sequence

```
1. DECIDE FIRST (prerequisite):
   • [decision] - because: [why it must come first]

2. DECIDE NEXT (after #1):
   • [decision] - depends on: [what]

3. CAN WAIT (preserve optionality):
   • [decision] - can delay until: [trigger]

4. WILL EMERGE (don't force):
   • [decision] - will become clear when: [condition]
```

### 05.4 Decision Readiness Assessment

```
┌─────────────────────┬────────────┬────────────────────────────┐
│ Decision            │ Readiness  │ What would help            │
├─────────────────────┼────────────┼────────────────────────────┤
│ [decision 1]        │ READY      │ -                          │
│ [decision 2]        │ ALMOST     │ [verify X]                 │
│ [decision 3]        │ NOT READY  │ [research Y]               │
└─────────────────────┴────────────┴────────────────────────────┘
```

### 05.5 Identify Remaining Information Gaps

📂 Load method: `data/method-procedures/E007_Information_Questions.md`

```
HIGHEST-VALUE QUESTIONS:
"Which information would change my decision the most?"

• [question 1] - impact: [HIGH/MED]
• [question 2] - impact: [HIGH/MED]

IGNORED OBVIOUS:
"What is everyone ignoring because it seems obvious?"

• [observation]
```

---

## Output: Synthesis Summary

```
╔═══════════════════════════════════════════════════════════════╗
║  SYNTHESIS SUMMARY                                             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  MINIMAL ASSERTIONS: [count]                                   ║
║  STRATEGIC CLUSTERS: [count]                                   ║
║                                                                ║
║  DECISION READINESS:                                           ║
║  • Ready:     [count]                                          ║
║  • Almost:    [count]                                          ║
║  • Not Ready: [count]                                          ║
║                                                                ║
║  REMAINING GAPS: [count]                                       ║
║                                                                ║
║  PROCEED TO STEP 6? [YES]                                     ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Transition

- **Proceed to Step 6** (always - synthesis is complete)
