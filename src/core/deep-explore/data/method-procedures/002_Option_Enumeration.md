# #2 Option Enumeration

**Tier:** 1 (Mandatory - Phase 1)
**Purpose:** Systematically list ALL options for each dimension.

## Core Principle

Humans naturally gravitate to 2-3 obvious options.
Systematic enumeration reveals 5-10+ options that often include better choices.

The goal is COMPLETENESS, not evaluation.
We list options here; we evaluate them later.

## What to do

1. For each dimension from #1 Dimension Discovery
2. Apply systematic enumeration techniques
3. Include non-obvious options
4. Note but don't eliminate "bad" options yet
5. Check for hybrid/combination options

## Step-by-step

```
1. Take one dimension at a time
   Dimension: [name from #1]

2. Start with obvious options:
   "What options immediately come to mind?"
   → List 2-4 obvious ones

3. Apply SCAMPER to generate more:
   - Substitute: What else could work here?
   - Combine: Can two approaches merge?
   - Adapt: What works in other domains?
   - Modify: What variations exist?
   - Put to other use: Repurpose something?
   - Eliminate: What's the minimal version?
   - Reverse: What's the opposite approach?

4. Apply extreme options:
   - "What's the MOST aggressive option?"
   - "What's the MOST conservative option?"
   - "What would an unlimited budget choose?"
   - "What would a zero budget choose?"
   - "What would a startup do?"
   - "What would an incumbent do?"

5. Apply analogical options:
   - "What does industry X do for this?"
   - "What did this look like 10 years ago?"
   - "What might this look like in 10 years?"

6. Check for hybrid options:
   - Can options A and B combine?
   - Can you start with A and migrate to B?
   - Can different users get different options?

7. Include the "null option":
   - "Do nothing / status quo"
   - "Defer decision"
   - "Outsource decision"
```

## Enumeration Completeness Checks

```
For each dimension, verify:

□ Minimum 3 options listed (ideally 4-6)
□ Includes at least one non-obvious option
□ Includes extreme options (max/min)
□ Includes null/defer option where applicable
□ Hybrid options considered
□ No options eliminated based on preference (only hard constraints)
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       OPTION ENUMERATION RESULTS                           ║
╠═══════════════════════════════════════════════════════════════════════════╣

DIMENSION: [Name]
═══════════════════════════════════════════════════════════════════════════

OPTION A: [Name]
├── Description: [1-2 sentences]
├── Source: [Obvious / SCAMPER / Extreme / Analog / Hybrid]
├── Example: [Real-world example if exists]
└── Note: [Any immediate observation - NOT evaluation]

OPTION B: [Name]
├── Description: [1-2 sentences]
├── Source: [Obvious / SCAMPER / Extreme / Analog / Hybrid]
├── Example: [Real-world example if exists]
└── Note: [Any immediate observation]

OPTION C: [Name]
├── Description: [1-2 sentences]
├── Source: [Obvious / SCAMPER / Extreme / Analog / Hybrid]
├── Example: [Real-world example if exists]
└── Note: [Any immediate observation]

[Continue for all options]

OPTION NULL: [Status quo / Defer / Outsource]
├── Description: What happens if we don't decide
└── Note: Often overlooked but valid

HYBRID OPTIONS CONSIDERED:
• [A + B] = [Name]: [feasible? why/why not]
• [B → C migration] = [Name]: [feasible? why/why not]

ENUMERATION QUALITY:
□ Total options: [N]
□ Non-obvious options: [N]
□ Extreme options included: [Yes/No]
□ Null option included: [Yes/No]

COVERAGE SCORE CONTRIBUTION: +[1 × N options] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝

[REPEAT FOR EACH DIMENSION]
```

## Option Generation Prompts by Domain

### Technology Decisions
```
- Build vs Buy vs Open-source vs Hybrid
- Monolith vs Microservices vs Serverless vs Modular-monolith
- Cloud-native vs Cloud-agnostic vs On-premise vs Hybrid-cloud
- Sync vs Async vs Event-driven vs Hybrid
```

### Business Decisions
```
- DIY vs Partner vs Acquire vs Joint-venture
- Premium vs Mid-market vs Budget vs Freemium
- Direct vs Channel vs Marketplace vs Hybrid
- Specialize vs Diversify vs Platform vs Ecosystem
```

### Process Decisions
```
- Waterfall vs Agile vs Hybrid vs No-process
- Centralized vs Distributed vs Federated vs Autonomous
- Manual vs Semi-automated vs Fully-automated vs AI-assisted
- Standard vs Customized vs Personalized vs Self-service
```

## Anti-Patterns to Avoid

```
❌ BINARY FRAMING
   "Should we build or buy?"
   → Missing: Open-source, Acquire company, Partner, Hybrid, etc.

❌ PREMATURE ELIMINATION
   "Option X is too expensive" [removes from list]
   → Keep it! Expense is evaluated later, not during enumeration

❌ ANCHORING ON FIRST OPTIONS
   Stopping at 3 obvious options
   → Force yourself to find 2 more non-obvious ones

❌ IGNORING NULL OPTION
   Assuming decision must be made
   → "Do nothing" or "Defer" is always an option

❌ MISSING HYBRID OPTIONS
   Treating options as mutually exclusive
   → Many can be combined or sequenced
```

## Example

```
DIMENSION: Market Entry Strategy
═══════════════════════════════════════════════════════════════════════════

OPTION A: Direct Sales
├── Description: Build internal sales team, go direct to customers
├── Source: Obvious
├── Example: Salesforce's enterprise approach
└── Note: High control, high cost

OPTION B: Channel Partners
├── Description: Work through resellers, integrators, distributors
├── Source: Obvious
├── Example: Microsoft's partner ecosystem
└── Note: Leverage existing relationships

OPTION C: Marketplace/Platform
├── Description: List on AWS/Azure/Shopify marketplace, let platform sell
├── Source: SCAMPER (Adapt from other industries)
├── Example: Monday.com on Atlassian Marketplace
└── Note: Lower friction, platform takes cut

OPTION D: Product-Led Growth
├── Description: Free tier, self-service, users become advocates
├── Source: Analog (SaaS playbook)
├── Example: Slack, Notion, Figma
└── Note: Requires product virality

OPTION E: Acquisition as Distribution
├── Description: Get acquired by company with distribution
├── Source: Extreme
├── Example: Instagram → Facebook distribution
└── Note: Unconventional but valid exit-to-scale

OPTION F: White-Label/OEM
├── Description: Let others rebrand and sell your product
├── Source: SCAMPER (Reverse - others do selling)
├── Example: Stripe for platforms
└── Note: Volume over margin

OPTION G: Community-First
├── Description: Build community, monetize later
├── Source: Analog (Open-source playbook)
├── Example: HashiCorp, Confluent
└── Note: Long-term play

OPTION NULL: Stay Small / Lifestyle Business
├── Description: Don't scale, stay with current organic growth
└── Note: Valid if founder goals align

HYBRID OPTIONS CONSIDERED:
• [PLG + Direct Sales] = Product-Led Sales: Self-serve for SMB, sales for Enterprise
• [Direct → Channel] = Start direct, add channel at scale
• [Community → Enterprise] = Build community, then offer enterprise tier

ENUMERATION QUALITY:
□ Total options: 8
□ Non-obvious options: 4 (C, E, F, G)
□ Extreme options included: Yes (E - Acquisition)
□ Null option included: Yes

COVERAGE SCORE CONTRIBUTION: +8 points
```
