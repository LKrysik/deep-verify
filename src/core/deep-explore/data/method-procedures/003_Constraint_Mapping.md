# #3 Constraint Mapping

**Tier:** 1 (Mandatory - Phase 1)
**Purpose:** Identify hard constraints that eliminate combinations.

## Core Principle

Constraints are NOT preferences. 

- Constraint: "Budget is $50K max" (hard limit)
- Preference: "We'd like to keep costs low" (evaluation criterion)

Constraints ELIMINATE options from the space.
Preferences RANK remaining options.

This method identifies TRUE constraints to shrink the combinatorial space
while preserving optionality where it actually exists.

## What to do

1. List all stated and implied constraints
2. Classify each as HARD vs SOFT
3. Challenge HARD constraints - are they truly immovable?
4. Map which dimension-option combinations are eliminated
5. Calculate remaining valid space

## Step-by-step

```
1. Gather stated constraints:
   "What has been stated as non-negotiable?"
   "What limitations have been mentioned?"

2. Identify implied constraints:
   "What resources are actually available?"
   "What timeline is realistic?"
   "What technical/legal/political limits exist?"

3. For each constraint, apply the HARD test:
   
   Is it TRULY HARD? Ask:
   □ What happens if we violate it?
   □ Who imposed this constraint?
   □ Can that person/entity flex?
   □ What would make them flex?
   □ Is this constraint from POLICY or PHYSICS?
   
   PHYSICS = truly hard (can't violate laws of nature)
   POLICY = potentially soft (humans made it, humans can change it)

4. For HARD constraints, map eliminations:
   "Constraint X eliminates: [list options/combinations]"

5. Challenge each "hard" constraint once:
   "If this constraint didn't exist, what would change?"
   "Is there any scenario where this could flex?"
   
6. Document remaining valid space:
   Count combinations that survive all constraints
```

## Constraint Classification Guide

```
DEFINITELY HARD (Physics/Math/Law):
├── Physical impossibilities
├── Mathematical proofs
├── Laws of physics/thermodynamics
├── Regulatory requirements (if violation = criminal)
├── Contractual obligations (if violation = lawsuit)
└── Immutable past events

PROBABLY HARD (Strong Policy):
├── Board mandates
├── Investor term sheets
├── Key customer requirements
├── Critical compliance (if violation = major damage)
└── Union agreements

OFTEN SOFT (Challengeable Policy):
├── "We've always done it this way"
├── Current budget (can sometimes be expanded)
├── Current timeline (can sometimes be extended)
├── Team preferences
├── Internal politics
└── Industry "best practices"

DEFINITELY SOFT (Preferences disguised as constraints):
├── "We prefer X"
├── "It would be nice if Y"
├── "Ideally Z"
├── Assumed but unverified limits
└── Fear-based restrictions
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       CONSTRAINT MAPPING RESULTS                           ║
╠═══════════════════════════════════════════════════════════════════════════╣

CONSTRAINT INVENTORY:
═══════════════════════════════════════════════════════════════════════════

CONSTRAINT 1: [Name]
├── Statement: "[exact constraint as stated]"
├── Source: [Who/what imposed this]
├── Type: [HARD: Physics/Legal/Contract] or [SOFT: Policy/Preference]
├── Challenge: "[what would change this?]"
│   └── Outcome: [Truly immovable / Could flex if...]
├── Eliminates:
│   └── [Dimension:Option] combinations removed
└── Final classification: [HARD / SOFT / RECLASSIFIED]

CONSTRAINT 2: [Name]
├── Statement: "[exact constraint]"
├── Source: [Who/what imposed this]
├── Type: [HARD / SOFT]
├── Challenge: "[what would change this?]"
│   └── Outcome: [description]
├── Eliminates:
│   └── [Dimension:Option] combinations removed
└── Final classification: [HARD / SOFT / RECLASSIFIED]

[Continue for all constraints]

═══════════════════════════════════════════════════════════════════════════
CONSTRAINT SUMMARY:
═══════════════════════════════════════════════════════════════════════════

HARD CONSTRAINTS (truly immovable):
• [C1]: [one-line summary] → eliminates [N] combinations
• [C2]: [one-line summary] → eliminates [N] combinations

SOFT CONSTRAINTS (reclassified as preferences):
• [C3]: [one-line summary] → moved to evaluation criteria
• [C4]: [one-line summary] → moved to evaluation criteria

CHALLENGED CONSTRAINTS (could flex):
• [C5]: Would flex if [condition] → keep in mind for negotiation

═══════════════════════════════════════════════════════════════════════════
VALID SPACE CALCULATION:
═══════════════════════════════════════════════════════════════════════════

Total theoretical combinations (from Morphological Box):
[D1 options] × [D2 options] × [D3 options] × ... = [N]

Combinations eliminated by HARD constraints:
- [C1] eliminates: [N1]
- [C2] eliminates: [N2]
- Overlap (already eliminated): [N_overlap]
Total eliminated: [N_total_eliminated]

REMAINING VALID COMBINATIONS: [N - N_total_eliminated]

Constraint efficiency: [% of space eliminated]

COVERAGE SCORE CONTRIBUTION: +[0.5 × N constraints mapped] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Constraint Challenge Questions

Use these to test if a constraint is truly HARD:

```
THE MONEY QUESTION:
"If someone offered $10M to violate this constraint, could it be violated?"
→ Yes = Policy constraint (negotiable)
→ No = Physics/Legal constraint (truly hard)

THE CEO QUESTION:
"Could the CEO override this constraint if they wanted to?"
→ Yes = Policy constraint
→ No = External constraint

THE TIME QUESTION:
"Could this constraint change in 6 months / 2 years?"
→ Yes = Temporal policy constraint
→ No = Likely hard constraint

THE ORIGIN QUESTION:
"Who created this constraint and why?"
→ If you can't answer, it might be assumed, not real

THE CONSEQUENCE QUESTION:
"What's the ACTUAL consequence of violating this?"
→ Minor inconvenience = Soft
→ Legal action / Safety issue / Business failure = Hard
```

## Anti-Patterns to Avoid

```
❌ TREATING PREFERENCES AS CONSTRAINTS
   "We must use TypeScript" [when it's actually a preference]
   → Challenge: What happens if we don't?

❌ ACCEPTING INHERITED CONSTRAINTS
   "Last team said this was impossible"
   → Challenge: Did they prove it or assume it?

❌ OVER-CONSTRAINING
   Listing 20 "hard" constraints that eliminate all options
   → Challenge: Are these really all hard?

❌ UNDER-CONSTRAINING
   Ignoring real constraints to keep options open
   → Reality will re-assert them later

❌ CONSTRAINT INFLATION
   "We need enterprise-grade security" for internal tool
   → Match constraint strength to actual need
```

## Example

```
CONSTRAINT INVENTORY:
═══════════════════════════════════════════════════════════════════════════

CONSTRAINT 1: Budget Cap
├── Statement: "Maximum budget is $100K for first year"
├── Source: CFO approval
├── Type: SOFT (Policy)
├── Challenge: "What if we showed 3x ROI?"
│   └── Outcome: CFO indicated flexibility for proven value
├── Eliminates: Enterprise vendors ($200K+)
└── Final classification: SOFT → Move to evaluation criteria

CONSTRAINT 2: GDPR Compliance
├── Statement: "Must comply with GDPR"
├── Source: Legal requirement (EU operations)
├── Type: HARD (Legal)
├── Challenge: "Can we exit EU market?"
│   └── Outcome: No - 40% of revenue
├── Eliminates: US-only vendors without DPA, data residency violations
└── Final classification: HARD ✓

CONSTRAINT 3: AWS Only
├── Statement: "Must run on AWS"
├── Source: Infrastructure team preference
├── Type: SOFT (Policy)
├── Challenge: "Why AWS only?"
│   └── Outcome: Team familiarity - could train for compelling alternative
├── Eliminates: Azure-only, GCP-only solutions
└── Final classification: SOFT → Preference, not constraint

CONSTRAINT 4: Q4 Launch
├── Statement: "Must launch by end of Q4"
├── Source: Sales commitment to key customer
├── Type: HARD (Contract)
├── Challenge: "Can we renegotiate?"
│   └── Outcome: Customer will churn if delayed
├── Eliminates: Options requiring >4 months implementation
└── Final classification: HARD ✓

═══════════════════════════════════════════════════════════════════════════
VALID SPACE CALCULATION:
═══════════════════════════════════════════════════════════════════════════

Total theoretical combinations: 5 × 4 × 3 × 4 = 240

HARD constraints eliminate:
- GDPR eliminates: 48 combinations (non-compliant vendors)
- Q4 Launch eliminates: 60 combinations (long-implementation options)
- Overlap: 12 combinations
Total eliminated: 96

REMAINING VALID COMBINATIONS: 144 (60% of space)

Two "constraints" reclassified as preferences for Phase 2 evaluation.
```
