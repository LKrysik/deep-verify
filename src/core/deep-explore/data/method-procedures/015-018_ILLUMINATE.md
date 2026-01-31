# #15 Future Optionality

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Assess which options preserve vs foreclose future possibilities.

## Core Principle

Some decisions open doors, others close them. The value of an option includes not just its direct value but also the future options it preserves (Real Options thinking).

Option Value = Intrinsic Value + Optionality Value

A slightly worse choice that preserves more options may be better than a slightly better choice that locks you in.

## What to do

1. For each option, list future possibilities it ENABLES
2. List future possibilities it FORECLOSES
3. Assess the value of preserved optionality
4. Consider: What options do you WANT to preserve?

## Output format

```
OPTION: [name]

ENABLES (future possibilities opened):
• [future option]: Value if exercised: [High/Med/Low]
• [future option]: Value if exercised: [High/Med/Low]

FORECLOSES (future possibilities closed):
• [future option]: Loss if needed: [High/Med/Low]
• [future option]: Loss if needed: [High/Med/Low]

OPTIONALITY SCORE: [sum of enabled - foreclosed]

CRITICAL OPTIONS:
• Must preserve: [option] because [reason]
• Okay to lose: [option] because [reason]
```

---

# #16 Integration Points

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Identify where options connect to existing systems/processes.

## Core Principle

No decision exists in isolation. New systems must integrate with existing:
- Technical systems (APIs, databases, infrastructure)
- Human systems (processes, workflows, habits)
- Business systems (contracts, partnerships, regulations)

Integration points are where complexity hides and where implementations fail.

## What to do

1. List all systems/processes the decision touches
2. For each option, identify integration requirements
3. Assess integration complexity and risk
4. Find hidden dependencies

## Output format

```
OPTION: [name]

TECHNICAL INTEGRATIONS:
• [system]: Integration complexity: [Low/Med/High]
  └── Risk: [what could go wrong]

PROCESS INTEGRATIONS:
• [workflow]: Change required: [None/Minor/Major]
  └── Risk: [adoption challenges]

BUSINESS INTEGRATIONS:
• [contract/partner]: Impact: [None/Renegotiate/Break]
  └── Risk: [relationship damage]

TOTAL INTEGRATION COMPLEXITY: [Low/Med/High/Very High]

HIDDEN DEPENDENCIES FOUND:
• [dependency]: Not obvious because [reason]
```

---

# #17 Resource Trade-off

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Map resource requirements for each option - reveal hidden costs.

## Core Principle

Every option consumes resources. The question is which resources and how much:
- Money (capex, opex, opportunity cost)
- Time (calendar time, person-hours)
- Attention (management focus, cognitive load)
- Skills (existing, need to hire, need to learn)
- Political capital (favors, goodwill)

Some resources are more scarce than others. The bottleneck resource often determines feasibility.

## What to do

1. For each option, list all resource requirements
2. Identify the scarcest resource (bottleneck)
3. Map trade-offs: "To get X, we must give up Y"
4. Check: Do we have the resources? What do we sacrifice?

## Output format

```
OPTION: [name]

RESOURCE REQUIREMENTS:
├── Money: $[amount] ([one-time/recurring])
├── Time: [duration] calendar, [hours] effort
├── People: [N] FTEs with [skills]
├── Attention: [High/Med/Low] management focus
└── Other: [political capital, partnerships, etc.]

SCARCEST RESOURCE: [which one]
└── This is the bottleneck because: [reason]

TRADE-OFFS:
• To afford this, we must [give up X]
• To staff this, we must [pull from Y]
• This consumes [%] of available [resource]

FEASIBILITY: [Yes / Stretch / No without changes]
```

---

# #18 Opportunity Cost

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Calculate what you give up by choosing each option.

## Core Principle

The true cost of a choice is not what you spend, but what you can't do because you made that choice.

Opportunity Cost = Value of best alternative foregone

If you choose A, you can't choose B. The cost of A includes losing B's benefits.

## What to do

1. For each option, identify what alternatives you're giving up
2. Estimate the value of those foregone alternatives
3. Calculate net value = option value - opportunity cost
4. Check if the "obvious best" is still best after opportunity cost

## Output format

```
IF WE CHOOSE: [Option A]

WE GIVE UP:
├── [Option B]: Value foregone = [estimate]
│   └── Specifically: [what B would have given us]
├── [Option C]: Value foregone = [estimate]
│   └── Specifically: [what C would have given us]
└── [Time/Resources for other projects]: [value]

OPPORTUNITY COST OF A: [total foregone value]

NET VALUE CALCULATION:
├── Value of A: [estimate]
├── Minus opportunity cost: -[foregone value]
└── Net value: [A value - opportunity cost]

COMPARISON:
| Option | Direct Value | Opportunity Cost | Net Value |
|--------|--------------|------------------|-----------|
| A      | [value]      | [opp cost]       | [net]     |
| B      | [value]      | [opp cost]       | [net]     |
| C      | [value]      | [opp cost]       | [net]     |

Does opportunity cost change the ranking? [Yes/No]
```
