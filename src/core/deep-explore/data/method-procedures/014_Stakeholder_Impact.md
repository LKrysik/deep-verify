# #14 Stakeholder Impact

**Tier:** 2 (Phase 2 - ILLUMINATE)
**Purpose:** Analyze how each option affects different stakeholders.

## Core Principle

Every decision has stakeholders beyond the decision-maker:
- Some will benefit (allies)
- Some will lose (resistors)
- Some are neutral but could tip either way

Understanding stakeholder impact reveals hidden support and resistance, and helps anticipate implementation challenges.

## What to do

1. Identify all stakeholders affected by the decision
2. For each option, map impact on each stakeholder
3. Identify potential allies and resistors
4. Anticipate resistance sources and strength
5. Plan stakeholder management

## Step-by-step

```
1. Identify stakeholders:
   - Who is directly affected?
   - Who has to implement this?
   - Who has to approve this?
   - Who competes for same resources?
   - Who is indirectly affected?

2. For each stakeholder, assess:
   - How does Option X affect them? (+positive / -negative / 0 neutral)
   - How much do they care? (high/medium/low)
   - How much power do they have? (high/medium/low)

3. Build impact matrix:
   Option A: Stakeholder 1 (+), Stakeholder 2 (-), ...
   Option B: Stakeholder 1 (-), Stakeholder 2 (+), ...

4. Identify:
   - ALLIES: Positive impact + High power = Champions
   - RESISTORS: Negative impact + High power = Blockers
   - SWING: Neutral + High power = Need to win over

5. Plan for resistance:
   - What will resistors do?
   - How can we address their concerns?
   - Can we convert them or neutralize?
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       STAKEHOLDER IMPACT ANALYSIS                          ║
║                    Option: [D1:X + D2:Y + D3:Z]                           ║
╠═══════════════════════════════════════════════════════════════════════════╣

STAKEHOLDER MAP:
═══════════════════════════════════════════════════════════════════════════

STAKEHOLDER: [Name/Role]
├── Impact: [+2 to -2 scale]
├── Cares: [High/Medium/Low]
├── Power: [High/Medium/Low]
├── Likely response: [Support/Resist/Neutral]
└── Key concern: [what matters to them]

[Repeat for each stakeholder]

═══════════════════════════════════════════════════════════════════════════
POWER/INTEREST MATRIX:
═══════════════════════════════════════════════════════════════════════════

                    LOW INTEREST          HIGH INTEREST
                ┌─────────────────────┬─────────────────────┐
    HIGH        │     KEEP            │     MANAGE          │
    POWER       │     SATISFIED       │     CLOSELY         │
                │  [stakeholders]     │  [stakeholders]     │
                ├─────────────────────┼─────────────────────┤
    LOW         │     MONITOR         │     KEEP            │
    POWER       │     (minimum)       │     INFORMED        │
                │  [stakeholders]     │  [stakeholders]     │
                └─────────────────────┴─────────────────────┘

═══════════════════════════════════════════════════════════════════════════
ALLIANCE/RESISTANCE MAP:
═══════════════════════════════════════════════════════════════════════════

CHAMPIONS (Positive + High Power):
• [stakeholder]: Will actively support because [reason]

SUPPORTERS (Positive + Lower Power):
• [stakeholder]: Will support if asked because [reason]

BLOCKERS (Negative + High Power):
• [stakeholder]: Will resist because [reason]
  └── Mitigation: [how to address]

CRITICS (Negative + Lower Power):
• [stakeholder]: Will complain because [reason]

SWING VOTES (Neutral + High Power):
• [stakeholder]: Could go either way
  └── Win by: [what would make them support]

═══════════════════════════════════════════════════════════════════════════
RESISTANCE ANALYSIS:
═══════════════════════════════════════════════════════════════════════════

BLOCKER: [stakeholder]
├── Their concern: [what they lose / fear]
├── Their power: [how they can block]
├── Likely action: [what they'll do]
├── Can we address? [Yes/Partial/No]
└── Strategy: [how to handle]

═══════════════════════════════════════════════════════════════════════════
STAKEHOLDER STRATEGY:
═══════════════════════════════════════════════════════════════════════════

Net support score: [sum of impacts × power]

Critical stakeholders to win:
1. [stakeholder]: [action to take]
2. [stakeholder]: [action to take]

Implementation risk from stakeholders: [High/Medium/Low]

COVERAGE SCORE CONTRIBUTION: +[0.5 × N stakeholders mapped] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Example

```
OPTION: Build in-house engineering team instead of outsourcing

STAKEHOLDER: CEO
├── Impact: +1 (better long-term control, but higher short-term cost)
├── Cares: High
├── Power: High
├── Likely response: Cautious support
└── Key concern: Time to market, burn rate

STAKEHOLDER: CFO
├── Impact: -1 (higher fixed costs, longer payback)
├── Cares: High
├── Power: High
├── Likely response: Resistance
└── Key concern: Runway, unit economics
    └── Mitigation: Show 3-year TCO comparison, milestone-based hiring

STAKEHOLDER: Current outsourced team
├── Impact: -2 (lose the contract)
├── Cares: High
├── Power: Low
├── Likely response: Resistance (may reduce quality during transition)
└── Key concern: Job loss
    └── Mitigation: Transition period, potential hire offers

STAKEHOLDER: Potential new engineers
├── Impact: +2 (job opportunity)
├── Cares: High
├── Power: Low (until hired)
├── Likely response: Eager support
└── Key concern: Interesting work, good culture

RESISTANCE STRATEGY:
- CFO is key blocker. Need financial model showing break-even at month 18.
- Outsourced team may sabotage. Plan for overlap period, document everything.
- CEO is swing vote. Emphasize speed after initial ramp.
```
