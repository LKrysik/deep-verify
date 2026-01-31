# #41 Trade-off Presentation

**Tier:** 5 (Phase 5 - CONVERGE)
**Purpose:** Present options as explicit trade-offs without recommendation.

## Core Principle

The AI's job is to MAP the territory, not CHOOSE the path. 

Trade-off presentation shows the user what they're getting and giving up with each option, enabling THEM to decide based on THEIR values.

## What to do

1. Compile all analysis into a clear trade-off matrix
2. Present options side-by-side with gains/costs
3. Highlight the key trade-offs (what you get vs give up)
4. DO NOT recommend - let user choose

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       TRADE-OFF SUMMARY                                    ║
╠═══════════════════════════════════════════════════════════════════════════╣

OPTION A: [Name]
┌─────────────────────────────────────────────────────────────────────────┐
│ YOU GET:                      │ YOU GIVE UP:                            │
│ • [benefit 1]                 │ • [cost 1]                              │
│ • [benefit 2]                 │ • [cost 2]                              │
│ • [benefit 3]                 │ • [cost 3]                              │
├─────────────────────────────────────────────────────────────────────────┤
│ BEST IF: [conditions where A is best choice]                            │
│ WORST IF: [conditions where A is worst choice]                          │
│ REVERSIBLE: [Yes/Partially/No]                                          │
└─────────────────────────────────────────────────────────────────────────┘

OPTION B: [Name]
┌─────────────────────────────────────────────────────────────────────────┐
│ YOU GET:                      │ YOU GIVE UP:                            │
│ • [benefit 1]                 │ • [cost 1]                              │
│ • [benefit 2]                 │ • [cost 2]                              │
├─────────────────────────────────────────────────────────────────────────┤
│ BEST IF: [conditions]                                                   │
│ WORST IF: [conditions]                                                  │
│ REVERSIBLE: [Yes/Partially/No]                                          │
└─────────────────────────────────────────────────────────────────────────┘

[Repeat for all options]

═══════════════════════════════════════════════════════════════════════════
THE FUNDAMENTAL TRADE-OFF:
═══════════════════════════════════════════════════════════════════════════

This decision comes down to:
"Do you value [X] more, or [Y] more?"

• If [X] matters more → Option [A]
• If [Y] matters more → Option [B]
• If [Z] matters most → Option [C]

WHAT I CANNOT TELL YOU:
• Which of [X, Y, Z] matters most to YOU
• Your risk tolerance
• Your time preference
• Future information you might receive

╚═══════════════════════════════════════════════════════════════════════════╝
```

---

# #42 Uncertainty Documentation

**Tier:** 5 (Phase 5 - CONVERGE)
**Purpose:** Document what remains unknown and how it affects the decision.

## Core Principle

Every decision is made with incomplete information. Documenting uncertainties:
- Sets realistic expectations
- Guides future learning
- Identifies monitoring needs
- Prevents false confidence

## What to do

1. List all remaining uncertainties
2. Classify by: how much it affects decision, how resolvable it is
3. For each: how would we know if our assumption was wrong?
4. Create monitoring plan for key uncertainties

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      UNCERTAINTY DOCUMENTATION                             ║
╠═══════════════════════════════════════════════════════════════════════════╣

WHAT WE DON'T KNOW:

HIGH-IMPACT UNCERTAINTIES (could change the decision):
┌─────────────────────────────────────────────────────────────────────────┐
│ UNCERTAINTY: [what we don't know]                                        │
│ Current assumption: [what we're assuming]                                │
│ Confidence: [%]                                                          │
│ If wrong: [what changes]                                                 │
│ How we'll know: [signal that assumption is wrong]                        │
│ Monitoring: [what to watch]                                              │
└─────────────────────────────────────────────────────────────────────────┘

MEDIUM-IMPACT UNCERTAINTIES (affects execution, not direction):
• [uncertainty]: Assuming [X], would adjust [Y] if wrong

LOW-IMPACT UNCERTAINTIES (good to know, won't change much):
• [uncertainty]: Interesting but not decision-relevant

═══════════════════════════════════════════════════════════════════════════
KNOWN UNKNOWNS VS UNKNOWN UNKNOWNS:
═══════════════════════════════════════════════════════════════════════════

KNOWN UNKNOWNS (we know we don't know):
• [list]

POSSIBLE UNKNOWN UNKNOWNS (things we might be missing):
• [speculation about blind spots]

AREAS NOT EXPLORED (out of scope, time, or expertise):
• [what we didn't look at and why]

═══════════════════════════════════════════════════════════════════════════
MONITORING PLAN:
═══════════════════════════════════════════════════════════════════════════

| Uncertainty | Signal to Watch | Check Frequency | If Triggered |
|-------------|-----------------|-----------------|--------------|
| [U1]        | [metric/event]  | [weekly/etc]    | [action]     |
| [U2]        | [metric/event]  | [monthly/etc]   | [action]     |

╚═══════════════════════════════════════════════════════════════════════════╝
```

---

# #43 Experiment Design

**Tier:** 5 (Phase 5 - CONVERGE)
**Purpose:** For COMPLEX problems, design small experiments to learn before committing.

## Core Principle

In COMPLEX domains (where cause-effect is unclear), analysis has limits. You must PROBE to learn.

An experiment is a small, safe-to-fail probe that generates learning:
- Low cost
- Fast feedback
- High learning value
- Doesn't commit you to anything

## When to use

- Problem type is COMPLEX (not COMPLICATED or CLEAR)
- Key uncertainties are high-impact but resolvable through testing
- Full commitment is risky but small test is possible

## What to do

1. Identify what you most need to learn
2. Design minimal experiment to test it
3. Define success/failure criteria BEFORE running
4. Plan: How will results change decision?

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         EXPERIMENT DESIGN                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣

EXPERIMENT: [Name]

QUESTION: What are we trying to learn?
"[Specific question we need answered]"

HYPOTHESIS:
"We believe [X]. If true, we should see [Y]."

DESIGN:
┌─────────────────────────────────────────────────────────────────────────┐
│ What we'll do: [specific actions]                                        │
│ Duration: [timeframe]                                                    │
│ Cost: [resources required]                                               │
│ Participants/Scope: [who/what is involved]                               │
│ What we'll measure: [metrics]                                            │
└─────────────────────────────────────────────────────────────────────────┘

SUCCESS CRITERIA (defined BEFORE experiment):
• Proceed with [Option A] if: [specific outcome]
• Proceed with [Option B] if: [specific outcome]
• Need more data if: [specific outcome]

RISKS OF EXPERIMENT:
• [what could go wrong with the experiment itself]
• Mitigation: [how to limit risk]

TIMELINE:
Week 1: [action]
Week 2: [action]
Week 3: [evaluate results]

DECISION AFTER EXPERIMENT:
• If success criteria met → [specific next step]
• If not met → [specific next step]

╚═══════════════════════════════════════════════════════════════════════════╝
```

---

# #44 Decision Record

**Tier:** 5 (Phase 5 - CONVERGE)
**Purpose:** Document the decision context, rationale, and review triggers.

## Core Principle

Decisions should be documented for:
- Future reference (why did we decide this?)
- Learning (was our reasoning right?)
- Accountability (what did we know when?)
- Review triggers (when to revisit)

A Decision Record captures the state of knowledge AT THE TIME of decision.

## What to do

1. Record what was decided and why
2. Document alternatives considered and why rejected
3. List assumptions and uncertainties at time of decision
4. Define triggers for revisiting the decision

## Output format

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         DECISION RECORD                                    ║
╠═══════════════════════════════════════════════════════════════════════════╣

DECISION ID: [unique identifier]
DATE: [date of decision]
DECISION MAKER(S): [who decided]

═══════════════════════════════════════════════════════════════════════════
THE DECISION:
═══════════════════════════════════════════════════════════════════════════

WHAT: [what was decided]

WHY: [rationale in 2-3 sentences]

═══════════════════════════════════════════════════════════════════════════
CONTEXT AT TIME OF DECISION:
═══════════════════════════════════════════════════════════════════════════

SITUATION: [brief context]

CONSTRAINTS: [what limited options]

KEY ASSUMPTIONS:
• [assumption 1]
• [assumption 2]

KEY UNCERTAINTIES:
• [uncertainty 1]
• [uncertainty 2]

═══════════════════════════════════════════════════════════════════════════
OPTIONS CONSIDERED:
═══════════════════════════════════════════════════════════════════════════

CHOSEN: [Option X]
├── Reason: [why this one]

REJECTED: [Option Y]
├── Reason for rejection: [why not]

REJECTED: [Option Z]
├── Reason for rejection: [why not]

═══════════════════════════════════════════════════════════════════════════
EXPECTED OUTCOMES:
═══════════════════════════════════════════════════════════════════════════

SUCCESS looks like: [description]
FAILURE looks like: [description]

TIMELINE:
• [milestone 1]: [date]
• [milestone 2]: [date]
• Decision review: [date]

═══════════════════════════════════════════════════════════════════════════
REVIEW TRIGGERS:
═══════════════════════════════════════════════════════════════════════════

REVISIT THIS DECISION IF:
• [trigger 1] occurs
• [trigger 2] occurs
• [assumption] proves wrong
• [date] passes without [expected outcome]

SCHEDULED REVIEW: [date]

═══════════════════════════════════════════════════════════════════════════
SIGNATURES / ACKNOWLEDGMENT:
═══════════════════════════════════════════════════════════════════════════

Decision recorded by: [name]
Acknowledged by: [stakeholders]

╚═══════════════════════════════════════════════════════════════════════════╝
```
