# #1 Dimension Discovery

**Tier:** 1 (Mandatory - Phase 1)
**Purpose:** Identify all axes of choice in the decision space.

## Core Principle

A decision is not a single choice but a COMBINATION of choices across multiple dimensions.
"What database should I use?" is actually:
- Dimension: Data model (SQL vs NoSQL vs Graph vs Time-series)
- Dimension: Hosting (Self-hosted vs Managed vs Serverless)
- Dimension: Scale (Single-node vs Clustered vs Global)
- Dimension: Cost model (License vs Open-source vs Usage-based)

## What to do

1. Start with the apparent question
2. Decompose into underlying dimensions
3. For each dimension, verify it's truly independent
4. Check for hidden dimensions not initially apparent
5. Validate dimensions cover the full decision space

## Step-by-step

```
1. State the apparent decision:
   "[User's stated question]"

2. Ask decomposition questions:
   - "What TYPE of X?" → Dimension
   - "HOW will X be done?" → Dimension
   - "WHO will do/use X?" → Dimension
   - "WHEN will X happen?" → Dimension
   - "WHERE will X exist?" → Dimension
   - "With WHAT RESOURCES?" → Dimension
   - "Under WHAT CONSTRAINTS?" → Dimension

3. For each candidate dimension, verify independence:
   "Can I change Dimension A without necessarily changing Dimension B?"
   - Yes → Independent dimensions (keep both)
   - No → Dependent (merge or note dependency)

4. Check for hidden dimensions:
   - "What am I ASSUMING is fixed that could vary?"
   - "What would a competitor/critic add to this list?"
   - "What dimension would make the BIGGEST difference if it changed?"

5. Validate completeness:
   - "If I specify all dimensions, is the decision fully determined?"
   - "Are there aspects of the decision not captured?"
```

## Dimension Discovery Prompts

Use these to uncover hidden dimensions:

```
ABSTRACTION PROMPTS:
- "What level of [X] am I assuming?" (scale, complexity, quality)
- "What timeframe am I implicitly considering?"
- "What scope boundaries am I taking for granted?"

STAKEHOLDER PROMPTS:
- "Whose needs am I not considering?"
- "Who else is affected by this decision?"
- "Who would disagree with how I've framed this?"

CONSTRAINT PROMPTS:
- "What constraints am I treating as fixed that might flex?"
- "What resources am I assuming available/unavailable?"
- "What capabilities am I assuming exist/don't exist?"

CONTEXT PROMPTS:
- "What environmental factors could change this?"
- "What market/technical/regulatory changes matter?"
- "What dependencies am I not seeing?"
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       DIMENSION DISCOVERY RESULTS                          ║
╠═══════════════════════════════════════════════════════════════════════════╣

APPARENT DECISION:
"[User's stated question]"

DIMENSIONS DISCOVERED:

DIMENSION 1: [Name]
├── Type: [Choice / Continuous / Constraint]
├── Why independent: [explanation]
├── Options will be: [preview - detailed in Option Enumeration]
└── Discovery method: [which prompt/question revealed this]

DIMENSION 2: [Name]
├── Type: [Choice / Continuous / Constraint]
├── Why independent: [explanation]
├── Options will be: [preview]
└── Discovery method: [which prompt/question revealed this]

DIMENSION 3: [Name]
├── Type: [Choice / Continuous / Constraint]
├── Why independent: [explanation]
├── Options will be: [preview]
└── Discovery method: [which prompt/question revealed this]

[Continue for all dimensions - aim for 3-7]

DEPENDENCIES NOTED:
• [Dimension X] constrains [Dimension Y] when [condition]
• [Dimension A] + [Dimension B] interact at [point]

HIDDEN DIMENSIONS CHECKED:
□ Timeframe dimension? [found/not applicable]
□ Scale dimension? [found/not applicable]
□ Stakeholder dimension? [found/not applicable]
□ Resource dimension? [found/not applicable]
□ Risk tolerance dimension? [found/not applicable]

COVERAGE ASSESSMENT:
• Dimensions found: [N]
• Estimated coverage: [%] of decision space
• Notable gaps: [any areas not captured]

COVERAGE SCORE CONTRIBUTION: +[2 × N dimensions] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Common Dimension Categories

Reference when exploring:

| Category | Example Dimensions |
|----------|-------------------|
| WHAT | Type, Scope, Features, Quality level |
| HOW | Approach, Method, Technology, Process |
| WHO | User, Provider, Partner, Team |
| WHEN | Timing, Sequence, Duration, Deadline |
| WHERE | Location, Platform, Environment, Market |
| RESOURCES | Budget, Time, Skills, Tools |
| CONSTRAINTS | Regulations, Compatibility, Dependencies |

## Anti-Patterns to Avoid

```
❌ SINGLE-DIMENSION FRAMING
   "Should I use React or Vue?" 
   → Missing: rendering strategy, state management, team skills, etc.

❌ FALSE CONSTRAINTS AS DIMENSIONS
   "Should I use AWS?" when client requires Azure
   → This is a constraint, not a dimension

❌ PREFERENCES AS DIMENSIONS
   "Do I want modern or traditional?"
   → This is evaluation criteria, not a dimension

❌ CONFLATING DEPENDENT DIMENSIONS
   "Frontend framework AND styling approach"
   → These might be independent; check
```

## Example

```
APPARENT DECISION:
"How should we monetize our new SaaS product?"

DIMENSIONS DISCOVERED:

DIMENSION 1: Pricing Model
├── Type: Choice
├── Why independent: Can change without changing other dimensions
├── Options: Freemium, Trial, Pay-from-start, Usage-based
└── Discovery: "What TYPE of pricing?"

DIMENSION 2: Price Point Strategy
├── Type: Choice
├── Why independent: Model can be same with different positioning
├── Options: Premium, Market-rate, Undercut, Penetration
└── Discovery: "HOW will we position on price?"

DIMENSION 3: Billing Cycle
├── Type: Choice
├── Why independent: Orthogonal to model and point
├── Options: Monthly, Annual, Lifetime, Per-transaction
└── Discovery: "WHEN do customers pay?"

DIMENSION 4: Customer Segment
├── Type: Choice
├── Why independent: Same product, different packaging
├── Options: SMB, Mid-market, Enterprise, Mixed
└── Discovery: "WHO are we primarily targeting?"

DIMENSION 5: Feature Gating
├── Type: Choice
├── Why independent: Affects what's in each tier
├── Options: Usage-limits, Feature-tiers, User-seats, Hybrid
└── Discovery: "What CONSTRAINTS differentiate tiers?"

DEPENDENCIES NOTED:
• Enterprise segment typically requires Annual billing
• Usage-based model interacts with Feature Gating approach

COVERAGE SCORE CONTRIBUTION: +10 (5 dimensions × 2)
```
