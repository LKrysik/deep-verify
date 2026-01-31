# #21 Premortem

**Tier:** 3 (Phase 3 - CHALLENGE)
**Purpose:** Imagine failure has already occurred and trace back to causes.

## Core Principle

A postmortem happens AFTER failure to understand what went wrong.
A premortem happens BEFORE decision to imagine what COULD go wrong.

Psychological research (Gary Klein) shows premortems:
- Increase ability to identify reasons for future outcomes by 30%
- Overcome optimism bias and groupthink
- Surface risks that "good news" framing suppresses

The key insight: It's easier to explain failure than predict it.

## What to do

1. Select an option combination to stress-test
2. Imagine it's 12 months later and it FAILED COMPLETELY
3. Write the failure story - what went wrong?
4. Identify the 3-5 key causes of failure
5. For each cause, assess: preventable? detectable? recoverable?
6. Document risk mitigation strategies

## Step-by-step

```
1. Set the scene:
   "It's [date + 12 months]. We chose [option combination].
    It has failed catastrophically. The project/decision is a disaster."

2. Write the failure story:
   - What does failure look like specifically?
   - Who is affected? How badly?
   - What's the narrative of how we got here?

3. Brainstorm failure causes (work backwards):
   "Why did this fail?"
   - List ALL possible causes (aim for 10+)
   - Include internal causes (our mistakes)
   - Include external causes (market, competition, luck)
   - Include interaction causes (things that combined badly)

4. Prioritize causes:
   "Which causes were most critical to the failure?"
   - Select top 5 by: likelihood × impact

5. For each critical cause, analyze:
   □ PREVENTABLE: Could we have avoided this?
   □ DETECTABLE: Would we have seen warning signs?
   □ RECOVERABLE: Once it happened, could we recover?

6. Generate mitigations:
   "How might we prevent, detect, or recover from this?"
```

## Failure Mode Categories

When brainstorming causes, check each category:

```
EXECUTION FAILURES:
├── We underestimated complexity
├── We lacked required skills
├── We couldn't hire/retain talent
├── We missed deadlines
├── We exceeded budget
└── Quality was insufficient

MARKET FAILURES:
├── Customers didn't want it
├── Pricing was wrong
├── Competition moved faster
├── Market shrank/changed
├── Timing was wrong
└── Distribution failed

TECHNICAL FAILURES:
├── Technology didn't work
├── Couldn't scale
├── Security breach
├── Integration failed
├── Vendor failed us
└── Technical debt overwhelmed

ORGANIZATIONAL FAILURES:
├── Leadership conflict
├── Lost key people
├── Communication breakdown
├── Stakeholder resistance
├── Political interference
└── Culture clash

EXTERNAL FAILURES:
├── Regulation changed
├── Economy crashed
├── Pandemic/disaster
├── Supplier failed
├── Partner defected
└── Black swan event
```

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                            PREMORTEM ANALYSIS                              ║
║                    Option: [D1:X + D2:Y + D3:Z]                           ║
╠═══════════════════════════════════════════════════════════════════════════╣

FAILURE SCENARIO:
═══════════════════════════════════════════════════════════════════════════

DATE: [Today + 12 months]

THE HEADLINE:
"[One sentence describing the failure]"

THE STORY:
[2-3 paragraph narrative of how the failure unfolded.
 Be specific and vivid. Include timeline, key events, consequences.]


FAILURE CAUSE ANALYSIS:
═══════════════════════════════════════════════════════════════════════════

BRAINSTORMED CAUSES (all possible):
1. [cause]
2. [cause]
3. [cause]
... (aim for 10+)

TOP 5 CRITICAL CAUSES (by likelihood × impact):

CAUSE 1: [Name]
├── Description: [What happened]
├── Category: [Execution/Market/Technical/Organizational/External]
├── Likelihood: [High/Medium/Low] - Why: [reasoning]
├── Impact: [High/Medium/Low] - Why: [reasoning]
├── Preventable? [Yes/Partial/No] - How: [action]
├── Detectable? [Yes/Partial/No] - Signal: [what to watch]
├── Recoverable? [Yes/Partial/No] - Plan: [recovery action]
└── MITIGATION: [Specific action to reduce risk]

CAUSE 2: [Name]
├── Description: [What happened]
├── Category: [Execution/Market/Technical/Organizational/External]
├── Likelihood: [High/Medium/Low]
├── Impact: [High/Medium/Low]
├── Preventable? [Yes/Partial/No]
├── Detectable? [Yes/Partial/No]
├── Recoverable? [Yes/Partial/No]
└── MITIGATION: [Specific action]

[Continue for causes 3-5]


RISK SUMMARY:
═══════════════════════════════════════════════════════════════════════════

HIGH RISK (High likelihood + High impact):
• [cause]: [mitigation summary]

MEDIUM RISK:
• [cause]: [mitigation summary]

WATCH LIST (Low likelihood but High impact):
• [cause]: [early warning signal]


DECISION IMPLICATIONS:
═══════════════════════════════════════════════════════════════════════════

Should this option be:
□ PROCEED - Risks are acceptable/mitigatable
□ PROCEED WITH CAUTION - Need specific mitigations in place first
□ RECONSIDER - Risks are too high, explore alternatives
□ REJECT - Fatal risks identified

If proceeding, MUST implement:
• [critical mitigation 1]
• [critical mitigation 2]

Early warning system - trigger review if:
• [signal 1] occurs
• [signal 2] occurs


COVERAGE SCORE CONTRIBUTION: +[1 × N risks identified] = +[points]

╚═══════════════════════════════════════════════════════════════════════════╝
```

## Premortem Prompts (Role-Play)

Adopt different perspectives to find different failures:

```
THE PESSIMIST:
"I knew this would fail. Here's what everyone ignored..."

THE COMPETITOR:
"We destroyed them by doing [X] while they were busy with [Y]..."

THE REGRETFUL FOUNDER:
"If I could go back, I would have [Z] instead..."

THE ANGRY CUSTOMER:
"They promised [A] but delivered [B]. I switched to..."

THE EXHAUSTED ENGINEER:
"We couldn't possibly ship with [constraint]. The technical debt..."

THE FIRED EMPLOYEE:
"They blamed me, but the real problem was..."
```

## Example

```
PREMORTEM ANALYSIS
Option: [SaaS model] + [Self-serve onboarding] + [Freemium pricing]
═══════════════════════════════════════════════════════════════════════════

DATE: January 2026

THE HEADLINE:
"Startup burns through $2M runway with zero paying customers"

THE STORY:
We launched in March with a beautiful self-serve product and generous free
tier. Signups were great - 5,000 users in first month! We celebrated.

By June, we noticed something: conversion to paid was 0.2%, not the 2-5%
we projected. Free users loved it but had no urgency to pay. Our free tier
was "good enough" for 95% of use cases.

We tried adding paywalls, but free users churned instead of converting.
Turns out our target SMB market was extremely price-sensitive, and we'd
trained them that our product should be free.

Meanwhile, our infrastructure costs scaled with free users. By October,
we were spending $40K/month on AWS for users generating $3K revenue.

By December, runway was gone. We couldn't raise - metrics were toxic.
No acquirer wanted a product with negative unit economics.


TOP 5 CRITICAL CAUSES:

CAUSE 1: Free tier too generous
├── Category: Market
├── Likelihood: HIGH - We have no data on where to draw the line
├── Impact: HIGH - Entire business model depends on conversion
├── Preventable? PARTIAL - Could A/B test tier boundaries
├── Detectable? YES - Track free→paid conversion weekly
├── Recoverable? PARTIAL - Can adjust tiers but may anger free users
└── MITIGATION: Launch with 14-day trial instead of freemium

CAUSE 2: Wrong customer segment
├── Category: Market  
├── Likelihood: MEDIUM - Assumption based on competitor analysis
├── Impact: HIGH - SMB price sensitivity kills unit economics
├── Preventable? YES - More customer research before build
├── Detectable? YES - Watch conversion by segment
├── Recoverable? PARTIAL - Pivot upmarket but product may not fit
└── MITIGATION: Run pricing tests with real customers before launch

CAUSE 3: Infrastructure costs scale with free users
├── Category: Technical
├── Likelihood: HIGH - This is structural to our architecture
├── Impact: HIGH - Directly burns cash
├── Preventable? YES - Design for cost efficiency from start
├── Detectable? YES - Track cost per user metric
├── Recoverable? PARTIAL - Can re-architect but expensive
└── MITIGATION: Set hard limits on free tier usage, serverless architecture


DECISION IMPLICATIONS:

Should this option be: PROCEED WITH CAUTION

MUST implement before proceeding:
• Validate pricing with 50+ customer interviews
• Design free tier with hard usage caps
• Implement cost tracking from day 1
• Have pivot plan if conversion <1%

Early warning - trigger review if:
• Free→paid conversion <1% after month 3
• Cost per user exceeds $5/month
• Churn increases when paywalls added
```
