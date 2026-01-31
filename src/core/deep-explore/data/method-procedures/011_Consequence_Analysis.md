# #11 Consequence Analysis

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Map the full consequence tree for each option/combination.

## Core Principle

Every decision has consequences beyond the immediate effect.
- First-order: Direct result of the choice
- Second-order: Results of the first-order consequences
- Third-order: Results of the second-order consequences

Most decisions are made considering only first-order effects.
Most regret comes from unanticipated second and third-order effects.

## What to do

1. Select key option combinations from Morphological Box
2. For each, trace consequences through 3 orders
3. Separate GAINS (positive) from COSTS (negative)
4. Separate OPENS (new possibilities) from CLOSES (foreclosed options)
5. Identify non-obvious interactions

## Step-by-step

```
1. Select option combination to analyze:
   [D1: Option X] + [D2: Option Y] + [D3: Option Z]

2. First-order consequences (direct effects):
   "What IMMEDIATELY happens when we choose this?"
   → List all direct effects (positive and negative)

3. Second-order consequences:
   For each first-order effect, ask:
   "And then what happens because of THAT?"
   → List ripple effects

4. Third-order consequences:
   For significant second-order effects, ask:
   "And then what happens because of THAT?"
   → List further ripples (usually stop here)

5. Categorize all consequences:
   GAINS: What do we get?
   COSTS: What do we lose/pay?
   OPENS: What new options become available?
   CLOSES: What options are foreclosed?

6. Time-map consequences:
   Immediate (0-3 months)
   Short-term (3-12 months)
   Long-term (1-5 years)
```

## Consequence Discovery Prompts

```
FOR GAINS:
- "What capability do we gain?"
- "What problem does this solve?"
- "What becomes easier?"
- "What becomes possible that wasn't before?"

FOR COSTS:
- "What do we have to give up?"
- "What becomes harder?"
- "What resources does this consume?"
- "What risks does this introduce?"

FOR OPENS:
- "What future options does this enable?"
- "What partnerships become possible?"
- "What markets become accessible?"
- "What skills do we develop?"

FOR CLOSES:
- "What options become impossible?"
- "What relationships might this damage?"
- "What future paths does this block?"
- "What lock-in does this create?"
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      CONSEQUENCE ANALYSIS                                  ║
║               Option: [D1:X + D2:Y + D3:Z]                                ║
╠═══════════════════════════════════════════════════════════════════════════╣

CONSEQUENCE TREE:
═══════════════════════════════════════════════════════════════════════════

FIRST-ORDER (Direct Effects):
├── [F1] [description] ──────────────────────────────────┐
│        └──► Second: [S1a] [description]                │
│             └──► Third: [T1] [description]             │
│        └──► Second: [S1b] [description]                │
│                                                        │
├── [F2] [description] ──────────────────────────────────┤
│        └──► Second: [S2a] [description]                │
│        └──► Second: [S2b] [description]                │
│             └──► Third: [T2] [description]             │
│                                                        │
└── [F3] [description] ──────────────────────────────────┘
         └──► Second: [S3a] [description]


CATEGORIZED SUMMARY:
═══════════════════════════════════════════════════════════════════════════

GAINS (What we get):
┌─────────────────────────────────────────────────────────────────────────┐
│ Immediate (0-3 mo)  │ Short-term (3-12 mo) │ Long-term (1-5 yr)        │
├─────────────────────┼──────────────────────┼───────────────────────────┤
│ • [gain]            │ • [gain]             │ • [gain]                  │
│ • [gain]            │ • [gain]             │                           │
└─────────────────────┴──────────────────────┴───────────────────────────┘

COSTS (What we pay):
┌─────────────────────────────────────────────────────────────────────────┐
│ Immediate (0-3 mo)  │ Short-term (3-12 mo) │ Long-term (1-5 yr)        │
├─────────────────────┼──────────────────────┼───────────────────────────┤
│ • [cost]            │ • [cost]             │ • [cost]                  │
│ • [cost]            │                      │                           │
└─────────────────────┴──────────────────────┴───────────────────────────┘

OPENS (Future options enabled):
• [option that becomes possible]
• [option that becomes possible]

CLOSES (Options foreclosed):
• [option that becomes impossible/difficult]
• [option that becomes impossible/difficult]


NON-OBVIOUS FINDINGS:
═══════════════════════════════════════════════════════════════════════════

INTERACTION EFFECTS:
• [F1] + [F2] together cause [unexpected consequence]

DELAYED EFFECTS:
• [consequence] won't be visible until [timeframe]

CONDITIONAL EFFECTS:
• If [external condition], then [consequence] becomes [more/less severe]


COVERAGE SCORE CONTRIBUTION: +[0.5 × N consequences mapped] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Deep-Dive Questions for Complex Consequences

```
FOR EACH MAJOR CONSEQUENCE:

MAGNITUDE:
- "How big is this effect? (1-10)"
- "Who/what is most affected?"

CERTAINTY:
- "How likely is this consequence? (%)"
- "What would have to happen for this NOT to occur?"

TIMING:
- "When does this consequence manifest?"
- "Is it gradual or sudden?"

REVERSIBILITY:
- "If this consequence is bad, can we undo it?"
- "How costly is reversal?"

DEPENDENCIES:
- "What else needs to happen for this consequence?"
- "What might block this consequence?"
```

## Example

```
CONSEQUENCE ANALYSIS
Option: [Build in-house] + [TypeScript] + [Hire 2 engineers]
═══════════════════════════════════════════════════════════════════════════

FIRST-ORDER (Direct Effects):
├── [F1] Full control over architecture and features
│        └──► Second: Can pivot quickly to new requirements
│        └──► Second: No vendor negotiation for features
│             └──► Third: Engineering team feels ownership
│
├── [F2] Need to hire 2 TypeScript engineers
│        └──► Second: 2-3 month hiring delay
│             └──► Third: Launch date slips
│        └──► Second: $300K annual ongoing cost
│        └──► Second: Team grows → management complexity
│
├── [F3] Initial build time 4-6 months
│        └──► Second: Opportunity cost of delayed market entry
│        └──► Second: Engineers learn domain deeply
│             └──► Third: Better long-term decisions

GAINS:
┌─────────────────────────────────────────────────────────────────────────┐
│ Immediate           │ Short-term           │ Long-term                  │
├─────────────────────┼──────────────────────┼────────────────────────────┤
│ • Full control      │ • Custom features    │ • Unique competitive moat  │
│ • No license cost   │ • Deep domain        │ • IP ownership             │
│                     │   knowledge          │ • Exit value               │
└─────────────────────┴──────────────────────┴────────────────────────────┘

COSTS:
┌─────────────────────────────────────────────────────────────────────────┐
│ Immediate           │ Short-term           │ Long-term                  │
├─────────────────────┼──────────────────────┼────────────────────────────┤
│ • Hiring effort     │ • $300K/yr staff     │ • Ongoing maintenance      │
│ • 2-3 mo delay      │ • Mgmt overhead      │ • Tech debt accumulation   │
│                     │ • Launch slip        │ • Key-person risk          │
└─────────────────────┴──────────────────────┴────────────────────────────┘

OPENS:
• Can license/sell the technology to others
• Can hire more easily (interesting engineering challenges)
• Can open-source parts for community goodwill

CLOSES:
• Quick pivot to established vendor (migration cost now exists)
• Staying lean/outsourced (now have team to support)
• Easy exit to acquirer who has competing tech

NON-OBVIOUS FINDINGS:
• Hiring delay + Launch slip creates compound effect → competitor window
• Deep domain knowledge + IP ownership could INCREASE exit value
• Team growth → management complexity is hidden ongoing cost
```
