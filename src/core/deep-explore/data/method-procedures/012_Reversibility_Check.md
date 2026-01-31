# #12 Reversibility Check

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Assess which decisions can be undone and at what cost.

## Core Principle

Not all decisions are equal. Some can be easily reversed, others are one-way doors.

- **Two-way door:** Can walk back through. Low cost to change mind.
- **One-way door:** Once through, can't return. High cost or impossible to reverse.

Jeff Bezos: "Most decisions should be made with around 70% of the information you wish you had. If you wait for 90%, you're probably being slow. But one-way doors require more caution."

## What to do

1. For each major option/decision, assess reversibility
2. Identify the "point of no return" - when does it become irreversible?
3. Calculate reversal cost (time, money, relationships, opportunity)
4. Classify: Easily reversible → Costly to reverse → Irreversible

## Step-by-step

```
1. List key decisions in the option:
   - Decision A: [description]
   - Decision B: [description]
   - Decision C: [description]

2. For each decision, ask:
   "If we did this and it was wrong, what would it take to undo?"
   
   Categories:
   - TRIVIAL: Change a config, flip a switch
   - EASY: Some rework, days of effort
   - COSTLY: Significant rework, weeks/months, money lost
   - VERY COSTLY: Major rework, relationships damaged, market position lost
   - IRREVERSIBLE: Can't undo (contracts, public announcements, burned bridges)

3. Identify point of no return:
   "At what moment does this become irreversible?"
   - Before signing? Before announcing? Before shipping?
   - After 1 customer? After 100? After integration?

4. Calculate reversal cost:
   - Direct cost: $X to undo
   - Time cost: Y weeks/months
   - Opportunity cost: What we miss while fixing
   - Relationship cost: Trust damaged with whom?
   - Reputation cost: How does market perceive the change?
```

## Reversibility Factors

```
MAKES MORE REVERSIBLE:
+ Modular architecture (can swap components)
+ Clear contracts/interfaces
+ Staged rollout (can stop early)
+ Short commitments (month-to-month vs multi-year)
+ Private beta (not public yet)
+ Feature flags (can turn off)

MAKES LESS REVERSIBLE:
- Public announcement
- Signed contracts
- Customer dependencies
- Data migration completed
- Team restructured
- Relationships burned
- Market positioning established
- Regulatory filings
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       REVERSIBILITY ASSESSMENT                             ║
║                    Option: [D1:X + D2:Y + D3:Z]                           ║
╠═══════════════════════════════════════════════════════════════════════════╣

DECISION-BY-DECISION ANALYSIS:
═══════════════════════════════════════════════════════════════════════════

DECISION: [Name]
├── Description: [what we're deciding]
├── Reversibility: [TRIVIAL / EASY / COSTLY / VERY COSTLY / IRREVERSIBLE]
├── Point of no return: [when it becomes hard to reverse]
├── Reversal cost:
│   ├── Direct: $[amount]
│   ├── Time: [duration]
│   ├── Opportunity: [what we miss]
│   └── Relationship: [who is affected]
└── Can we defer? [Yes - until X / No - because Y]

[Repeat for each decision]

═══════════════════════════════════════════════════════════════════════════
REVERSIBILITY SUMMARY:
═══════════════════════════════════════════════════════════════════════════

TWO-WAY DOORS (decide fast, can change):
• [decision]: [why reversible]
• [decision]: [why reversible]

ONE-WAY DOORS (decide carefully):
• [decision]: [why irreversible] - Point of no return: [when]
• [decision]: [why irreversible] - Point of no return: [when]

DECISION TIMING RECOMMENDATION:
┌─────────────────────────────────────────────────────────────────────────┐
│ Decide NOW (two-way, blocking other work):                              │
│ • [decision]                                                            │
│                                                                         │
│ Decide LATER (can defer without losing options):                        │
│ • [decision] - decide by [date] to preserve options                     │
│                                                                         │
│ Decide CAREFULLY (one-way door):                                        │
│ • [decision] - need [more info / more validation] first                 │
└─────────────────────────────────────────────────────────────────────────┘

COVERAGE SCORE CONTRIBUTION: +[0.5 × N decisions assessed] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Example

```
DECISION: Choice of primary programming language (TypeScript vs Python)
├── Reversibility: VERY COSTLY
├── Point of no return: After ~10K lines of code / 3 months development
├── Reversal cost:
│   ├── Direct: $50-100K (rewrite labor)
│   ├── Time: 2-4 months
│   ├── Opportunity: Delayed roadmap
│   └── Relationship: Team frustration
└── Can we defer? No - blocks all development

DECISION: Cloud provider (AWS vs Azure vs GCP)
├── Reversibility: COSTLY (but possible)
├── Point of no return: After using provider-specific services heavily
├── Reversal cost:
│   ├── Direct: $20-50K (migration)
│   ├── Time: 1-2 months
│   ├── Opportunity: Feature freeze during migration
│   └── Relationship: Minimal
└── Can we defer? Partially - start cloud-agnostic, decide specifics later

DECISION: Pricing model (freemium vs trial vs paid-only)
├── Reversibility: COSTLY (market perception)
├── Point of no return: After public launch with pricing
├── Reversal cost:
│   ├── Direct: Minimal
│   ├── Time: Days to change
│   ├── Opportunity: Confused customers
│   └── Relationship: Early adopters feel betrayed if changed
└── Can we defer? Yes - until launch, can A/B test
```
