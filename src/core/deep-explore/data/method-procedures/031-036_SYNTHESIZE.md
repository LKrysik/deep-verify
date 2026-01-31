# #31 Option Clustering

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Group similar strategies into families - reveal underlying strategic choices.

## Core Principle

Individual options often cluster into "strategy families" - groups that share core characteristics. Seeing clusters helps move from many options to a few fundamental choices.

Instead of choosing between 20 options, you choose between 3-4 strategic directions, then refine within the chosen direction.

## What to do

1. List all viable options from Morphological Box
2. Identify shared characteristics
3. Group options into clusters (strategy families)
4. Name each cluster by its defining characteristic
5. Reduce decision from "which option" to "which cluster"

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         OPTION CLUSTERING                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣

CLUSTER 1: "[Name - defining characteristic]"
├── Core trait: [what defines this cluster]
├── Options in cluster:
│   • [Option A]
│   • [Option B]
│   • [Option C]
├── Cluster trade-off: [what you get vs give up]
└── Best for: [when/who this cluster suits]

CLUSTER 2: "[Name]"
├── Core trait: [defining characteristic]
├── Options: [list]
├── Trade-off: [gets/gives]
└── Best for: [context]

CLUSTER 3: "[Name]"
[same structure]

═══════════════════════════════════════════════════════════════════════════

CLUSTER COMPARISON:
| Cluster | Core Trait | Main Advantage | Main Disadvantage |
|---------|------------|----------------|-------------------|
| 1       | [trait]    | [advantage]    | [disadvantage]    |
| 2       | [trait]    | [advantage]    | [disadvantage]    |
| 3       | [trait]    | [advantage]    | [disadvantage]    |

THE FUNDAMENTAL QUESTION:
Instead of "which of 20 options?", the question is now:
"[Cluster 1 trait] vs [Cluster 2 trait] vs [Cluster 3 trait]?"

╚═══════════════════════════════════════════════════════════════════════════╝
```

---

# #32 Decision Sequencing

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Determine what must be decided first vs what can wait.

## Core Principle

Not all decisions need to be made at once. Some are:
- **Blocking:** Must decide before progress
- **Informing:** Better decided after learning more
- **Parallel:** Can decide independently

The goal is to identify the minimum decisions needed NOW and defer the rest.

## What to do

1. List all decisions/dimensions
2. For each: "Must this be decided now, or can it wait?"
3. Identify dependencies (from #13)
4. Create decision timeline
5. Define trigger points for deferred decisions

## Output format

```
DECISION SEQUENCE:

DECIDE NOW (Blocking, can't progress without):
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. [Decision]: [reason it can't wait]                                   │
│ 2. [Decision]: [reason it can't wait]                                   │
└─────────────────────────────────────────────────────────────────────────┘

DECIDE SOON (Within [timeframe], before [trigger]):
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. [Decision]: Decide by [date/event] because [reason]                  │
│ 4. [Decision]: Decide by [date/event] because [reason]                  │
└─────────────────────────────────────────────────────────────────────────┘

DECIDE LATER (Can wait, more information coming):
┌─────────────────────────────────────────────────────────────────────────┐
│ 5. [Decision]: Wait for [information], decide when [trigger]            │
│ 6. [Decision]: Not needed until [milestone]                             │
└─────────────────────────────────────────────────────────────────────────┘

DECISION TIMELINE:
Now ──────► Month 1 ──────► Month 3 ──────► Month 6
 │              │              │              │
[D1,D2]       [D3]           [D4]          [D5,D6]
```

---

# #33 Real Options Identification

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Find decisions that can be delayed while preserving optionality.

## Core Principle

A "real option" is the right (but not obligation) to take an action in the future. Options have value because:
- You might learn more (information value)
- Circumstances might change
- You preserve flexibility

Some decisions can be structured as options: small investment now, big commitment later IF conditions are right.

## What to do

1. For each major decision, ask: "Can this be structured as an option?"
2. Identify the "option price" (small upfront investment)
3. Identify the "strike conditions" (when to exercise/abandon)
4. Calculate option value: flexibility preserved × probability of good outcome

## Output format

```
REAL OPTIONS IDENTIFIED:

OPTION: [Decision that can be deferred]
├── Instead of: Committing fully now to [big decision]
├── We could: [small investment] now, decide [big commitment] later
├── Option price: [upfront cost to preserve option]
├── Strike conditions:
│   ├── Exercise (commit) if: [condition]
│   └── Abandon if: [condition]
├── Option expiry: [when we must decide]
├── Value of waiting: [what we learn / how circumstances might change]
└── Recommendation: [Structure as option / Decide now / Doesn't apply]

OPTION VALUE SUMMARY:
| Decision | Option Price | Value of Waiting | Recommendation |
|----------|--------------|------------------|----------------|
| [D1]     | [cost]       | [High/Med/Low]   | [option/now]   |
| [D2]     | [cost]       | [High/Med/Low]   | [option/now]   |

DECISIONS TO STRUCTURE AS OPTIONS:
• [decision]: Pay [small amount] now to learn, commit [later] if [condition]
```

---

# #34 Information Value Analysis

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Calculate what information would most reduce uncertainty.

## Core Principle

Not all information is equally valuable. Some information would change your decision, some wouldn't.

Value of Information = (Probability you'd decide differently) × (Value of better decision)

Focus on getting HIGH-VALUE information, not just more information.

## What to do

1. List key uncertainties
2. For each: "If I knew X, would it change my decision?"
3. Prioritize information by decision impact
4. Design ways to get high-value information (experiments)

## Output format

```
UNCERTAINTY INVENTORY:

UNCERTAINTY: [What we don't know]
├── Current assumption: [what we're assuming]
├── Confidence: [%]
├── If we knew for sure, would decision change? [Yes/Maybe/No]
├── Decision impact: [High/Med/Low]
├── How to resolve: [method to get information]
└── Cost to resolve: [time/money]

INFORMATION VALUE RANKING:
| Uncertainty | Would Change Decision? | Cost to Resolve | Priority |
|-------------|------------------------|-----------------|----------|
| [U1]        | [Yes/Maybe/No]         | [cost]          | [1-5]    |
| [U2]        | [Yes/Maybe/No]         | [cost]          | [1-5]    |

HIGH-VALUE INFORMATION TO GET:
1. [uncertainty]: Resolve by [method] - MUST DO before deciding
2. [uncertainty]: Resolve by [method] - SHOULD DO if time
3. [uncertainty]: Nice to know but won't change decision

EXPERIMENTS TO RUN:
• To learn [X]: [experiment design]
• To learn [Y]: [experiment design]
```

---

# #35 Decision Criteria Extraction

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Surface the implicit criteria being used to evaluate options.

## Core Principle

Decisions are made by comparing options against criteria. But criteria are often:
- Implicit (not stated)
- Conflicting (can't optimize all)
- Differently weighted by different people

Making criteria explicit enables rational comparison and reveals hidden disagreements.

## What to do

1. List all criteria being used (stated and unstated)
2. Check for conflicts between criteria
3. Weight criteria by importance
4. Make trade-offs explicit

## Output format

```
CRITERIA EXTRACTED:

CRITERION 1: [name]
├── Definition: [what it means specifically]
├── Why it matters: [reasoning]
├── Measurement: [how to evaluate options against it]
└── Weight: [Critical / Important / Nice-to-have]

[Repeat for all criteria]

CRITERIA CONFLICTS:
• [Criterion A] vs [Criterion B]: [how they conflict]
  └── Trade-off: More A means less B

WEIGHTED CRITERIA:
| Criterion | Weight (1-10) | [Opt A] | [Opt B] | [Opt C] |
|-----------|---------------|---------|---------|---------|
| [C1]      | [weight]      | [score] | [score] | [score] |
| [C2]      | [weight]      | [score] | [score] | [score] |
| Weighted Total |          | [total] | [total] | [total] |

HIDDEN CRITERIA SURFACED:
• [criterion] - was implicit, now explicit
```

---

# #36 Path Dependency Mapping

**Tier:** 4 (Phase 4 - SYNTHESIZE)
**Purpose:** Show how early choices constrain later ones.

## Core Principle

Early decisions create path dependencies - they constrain what's possible later. Some paths lead to good places, others to dead ends.

Mapping path dependencies helps see the long-term implications of short-term choices.

## What to do

1. For each early decision, trace forward: "What does this enable/prevent later?"
2. Identify strategic forks (decisions that lead to very different futures)
3. Find lock-in points (where changing direction becomes very costly)
4. Map decision tree showing path dependencies

## Output format

```
PATH DEPENDENCY MAP:

DECISION: [Early decision]
│
├── IF [Option A]:
│   ├── ENABLES later: [future options opened]
│   ├── PREVENTS later: [future options closed]
│   └── LEADS TO: [likely future state]
│
└── IF [Option B]:
    ├── ENABLES later: [future options opened]
    ├── PREVENTS later: [future options closed]
    └── LEADS TO: [likely future state]

STRATEGIC FORKS (decisions with very different futures):
• [Decision X]: Left path leads to [future A], right to [future B]
  └── This is a fork because: [paths diverge significantly]

LOCK-IN POINTS (where changing becomes very hard):
• After [decision/milestone]: Changing from A to B costs [X]
• After [decision/milestone]: Can no longer [option]

DECISION TREE:

                    [Start]
                       │
              ┌────────┴────────┐
              │                 │
           [D1: A]           [D1: B]
              │                 │
         ┌────┴────┐           [future B]
         │         │
      [D2: X]   [D2: Y]
         │         │
    [future AX] [future AY]
```
