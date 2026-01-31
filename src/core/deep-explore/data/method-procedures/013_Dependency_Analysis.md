# #13 Dependency Analysis

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Map which decisions depend on others - what must be decided first.

## Core Principle

Decisions are not independent. Some must come before others:
- **Blocking dependency:** Can't decide B until A is resolved
- **Informing dependency:** B is easier/better after knowing A
- **Parallel decisions:** A and B can be decided independently

Understanding dependencies reveals the critical path and prevents wasted effort on premature decisions.

## What to do

1. List all decisions/dimensions from the Morphological Box
2. For each pair, ask: "Does deciding X affect or require Y?"
3. Build dependency graph
4. Identify: root decisions, dependent decisions, parallel tracks
5. Find the critical path (what must be decided first)

## Step-by-step

```
1. List all decisions:
   D1: [decision]
   D2: [decision]
   D3: [decision]
   ...

2. Build dependency matrix:
   For each pair (Di, Dj), ask:
   - Does Di need Dj resolved first? → Dj blocks Di
   - Does Di inform Dj (makes it easier)? → soft dependency
   - Are they independent? → can parallel

3. Identify dependency types:
   HARD: "Cannot decide X without knowing Y"
   SOFT: "X is easier/better after Y, but could decide X first"
   NONE: "X and Y are independent"

4. Find root decisions:
   Decisions with no dependencies → must/can be decided first

5. Find critical path:
   Longest chain of hard dependencies = critical path
   This determines minimum time to full decision

6. Identify parallel tracks:
   Groups of decisions that can proceed independently
```

## Dependency Questions

```
FOR EACH PAIR OF DECISIONS:

"If we change our mind on D1, does D2 need to change?"
→ Yes = dependency exists

"Can we meaningfully evaluate D2 options without knowing D1?"
→ No = D1 informs D2

"Does D1 constrain which D2 options are valid?"
→ Yes = D1 constrains D2

"Are D1 and D2 the same decision in disguise?"
→ Yes = merge them
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       DEPENDENCY ANALYSIS                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣

DECISIONS ANALYZED:
D1: [decision name]
D2: [decision name]
D3: [decision name]
...

═══════════════════════════════════════════════════════════════════════════
DEPENDENCY MATRIX:
═══════════════════════════════════════════════════════════════════════════

        │ D1  │ D2  │ D3  │ D4  │ D5  │
────────┼─────┼─────┼─────┼─────┼─────┤
D1      │  -  │  →  │     │  →  │     │
D2      │     │  -  │  →  │     │     │
D3      │     │     │  -  │     │  ↔  │
D4      │     │     │     │  -  │     │
D5      │     │     │  ↔  │     │  -  │

Legend:
→  = Row blocks Column (D1 → D2 means D1 must come before D2)
↔  = Mutual dependency (must decide together)
~  = Soft dependency (informs but doesn't block)
   = Independent

═══════════════════════════════════════════════════════════════════════════
DEPENDENCY DETAILS:
═══════════════════════════════════════════════════════════════════════════

D1 → D2: [Business model] blocks [Pricing]
├── Type: HARD
├── Reason: Can't set prices without knowing if B2B or B2C
└── Must resolve D1 first

D2 → D3: [Pricing] informs [Feature scope]
├── Type: SOFT  
├── Reason: Price point suggests feature expectations
└── Could decide D3 first, but D2 helps

D3 ↔ D5: [Feature scope] and [Team size] are coupled
├── Type: MUTUAL
├── Reason: More features need more people, more people enable features
└── Decide together or iterate

═══════════════════════════════════════════════════════════════════════════
CRITICAL PATH:
═══════════════════════════════════════════════════════════════════════════

ROOT DECISIONS (no dependencies, decide first):
• D1: [decision] - START HERE
• D4: [decision] - Can parallel with D1

DEPENDENT DECISIONS (in order):
1. D1 → 2. D2 → 3. D3/D5 (coupled)

CRITICAL PATH LENGTH: [N] decisions in sequence

PARALLEL TRACKS:
Track A: D1 → D2 → D3
Track B: D4 (independent)
Track C: D5 (joins Track A at D3)

═══════════════════════════════════════════════════════════════════════════
DECISION SEQUENCE RECOMMENDATION:
═══════════════════════════════════════════════════════════════════════════

PHASE 1 (Now):
├── D1: [root decision]
└── D4: [parallel root decision]

PHASE 2 (After Phase 1):
└── D2: [depends on D1]

PHASE 3 (After Phase 2):
├── D3: [depends on D2]
└── D5: [coupled with D3]

COVERAGE SCORE CONTRIBUTION: +[0.5 × N dependencies mapped] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Example

```
DECISIONS:
D1: Target market (B2C vs B2B vs Enterprise)
D2: Pricing model (Freemium vs Paid vs Usage)
D3: Technology stack (Language, Framework)
D4: Distribution channel (Direct vs Partners vs PLG)
D5: Team composition (Engineers vs Sales vs Marketing mix)

DEPENDENCY ANALYSIS:

D1 → D2: Target market blocks Pricing
├── B2C typically needs freemium
├── Enterprise typically needs sales-assisted pricing
└── HARD dependency

D1 → D4: Target market blocks Distribution
├── B2C → PLG likely
├── Enterprise → Direct sales likely
└── HARD dependency

D1 → D5: Target market informs Team composition
├── B2C → more engineers, growth hackers
├── Enterprise → more sales, customer success
└── SOFT dependency (can hire generalists first)

D2 ~ D3: Pricing softly informs Technology
├── Usage-based pricing needs metering infrastructure
├── But can add later
└── SOFT dependency

D3 independent of D1, D4, D5
├── Technology choice doesn't depend on business model
└── Can decide in parallel

CRITICAL PATH: D1 → D2 → (D4 parallel) → D5
ROOT: D1 (Target market) and D3 (Technology) 

RECOMMENDATION: Decide D1 and D3 first. They're independent and everything else follows.
```
