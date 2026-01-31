# Step 04: Challenge (Adversarial)

## Purpose

Stress-test the exploration for blind spots and weak thinking.

**Time:** 15-20 min

**Inputs:** Option Map, Consequence Map from Steps 2-3

**Outputs:** Challenged map with strengthened/weakened items

---

## Procedure

### 04.1 Falsification

📂 Load method: `data/method-procedures/E006_Falsification.md`

For each key belief/assumption:

```
BELIEF: "[statement]"

FALSIFICATION TEST:
"What would show this is FALSE?"

ATTEMPT:
[Try to find evidence against]

RESULT:
[ ] FALSIFIED - evidence: [what was found]
    → REMOVE or MODIFY belief

[ ] SURVIVED - attempts: [what was tried]
    → STRENGTHEN confidence

[ ] UNTESTABLE - reason: [why]
    → FLAG as assumption
```

### 04.2 Premortem

📂 Load method: `data/method-procedures/M021_Premortem.md`

For top 2-3 options, imagine failure:

```
OPTION: [name]

SCENARIO: "It's 12 months later. We chose this. It failed badly."

WHAT WENT WRONG:
• [cause 1] - could we have seen this? [Y/N]
• [cause 2] - could we have seen this? [Y/N]
• [cause 3] - could we have seen this? [Y/N]

PREVENTABLE CAUSES:
→ Add to risks and mitigation plan

UNPREVENTABLE CAUSES:
→ Note as TRUE UNCERTAINTY

SURVIVABLE?
→ If failure happens, can we recover?
```

### 04.3 Black Swan Hunt

📂 Load method: `data/method-procedures/M022_Black_Swan_Hunt.md`

```
LOW PROBABILITY, HIGH IMPACT EVENTS:

POSITIVE BLACK SWANS (upside):
• [event] - would enable: [what]
• [event] - would enable: [what]

NEGATIVE BLACK SWANS (downside):
• [event] - would destroy: [what]
• [event] - would destroy: [what]

PREPARATION:
• How to position for positive swans?
• How to survive negative swans?
```

### 04.4 Assumption Stress Test

📂 Load method: `data/method-procedures/M023_Assumption_Stress_Test.md`

```
For each key assumption:

ASSUMPTION: "[statement]"
CONFIDENCE: [HIGH/MED/LOW]

STRESS TESTS:
• What would disprove this?
• Who would disagree?
• What if 50% wrong?

RESULT:
[ ] HOLDS - survives challenge
[ ] WEAKENED - reduce confidence
[ ] BROKEN - update map
```

### 04.5 Bias Check

Run through this comprehensive checklist. For each bias detected, apply the remediation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  COGNITIVE BIAS CHECKLIST                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INFORMATION PROCESSING BIASES                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  □ CONFIRMATION BIAS                                                         │
│    Detection: "Did I seek out evidence that contradicts my view?"            │
│    Symptoms: Only sources that agree, dismissing contrary data              │
│    Remediation: Force-search for 3 sources that disagree                    │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ AVAILABILITY BIAS                                                         │
│    Detection: "Am I overweighting recent or vivid examples?"                │
│    Symptoms: "I just read about X" driving conclusions                      │
│    Remediation: Check base rates, find statistical evidence                 │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ ANCHORING                                                                 │
│    Detection: "Did the first number/option overly influence me?"            │
│    Symptoms: All estimates close to first reference point                   │
│    Remediation: Generate estimate BEFORE seeing anchors, compare            │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ FRAMING EFFECT                                                            │
│    Detection: "Would I decide differently if framed as loss vs gain?"       │
│    Symptoms: "70% success" feels different than "30% failure"               │
│    Remediation: Reframe each option in opposite terms                       │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  DECISION-MAKING BIASES                                                      │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  □ SUNK COST FALLACY                                                         │
│    Detection: "Am I continuing because of past investment?"                 │
│    Symptoms: "We've already spent X" as reason to continue                  │
│    Remediation: Imagine starting fresh today - same choice?                 │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ STATUS QUO BIAS                                                           │
│    Detection: "Am I favoring 'do nothing' without justification?"           │
│    Symptoms: Change feels risky, current state feels safe                   │
│    Remediation: List costs of NOT changing                                  │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ LOSS AVERSION                                                             │
│    Detection: "Am I overweighting potential losses vs gains?"               │
│    Symptoms: Avoiding options with downside despite larger upside           │
│    Remediation: Calculate expected value, not worst case                    │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ PLANNING FALLACY                                                          │
│    Detection: "Am I underestimating time/cost/difficulty?"                  │
│    Symptoms: Optimistic estimates despite past evidence                     │
│    Remediation: Use reference class forecasting (similar projects)          │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  SOCIAL & EMOTIONAL BIASES                                                   │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  □ OPTIMISM BIAS                                                             │
│    Detection: "Am I assuming things will go better than typical?"           │
│    Symptoms: "It'll be fine" without evidence                               │
│    Remediation: Ask "What if I'm wrong?" and plan for it                    │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ OVERCONFIDENCE                                                            │
│    Detection: "How certain am I, and is that justified?"                    │
│    Symptoms: 90% confidence but 50% historical accuracy                     │
│    Remediation: Track past predictions, calibrate                           │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ AUTHORITY BIAS                                                            │
│    Detection: "Am I believing X because expert said so?"                    │
│    Symptoms: Accepting claims without evidence because of source            │
│    Remediation: Check expert's track record, seek opposing experts          │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ GROUPTHINK                                                                │
│    Detection: "Is everyone agreeing too easily?"                            │
│    Symptoms: No dissent, pressure to conform                                │
│    Remediation: Assign devil's advocate role, seek outside opinion          │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
│  □ SURVIVORSHIP BIAS                                                         │
│    Detection: "Am I only seeing successes, not failures?"                   │
│    Symptoms: "Company X did it!" (ignoring 100 that failed)                 │
│    Remediation: Actively search for failure cases                           │
│    Impact on map: [ ] None [ ] Minor [ ] Significant [ ] Critical           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

BIAS CHECK SUMMARY:
┌────────────────────────┬──────────┬────────────────────────────────────────┐
│ Bias Detected          │ Impact   │ Remediation Applied                    │
├────────────────────────┼──────────┼────────────────────────────────────────┤
│                        │          │                                        │
│                        │          │                                        │
│                        │          │                                        │
└────────────────────────┴──────────┴────────────────────────────────────────┘

TOTAL BIASES: [count]
SIGNIFICANT/CRITICAL: [count] → Must update map before proceeding
```

---

## 04.6 Fear Resolution (IF FEAR-BASED MODE)

**When to use:** User went through Fear-Based Exploration in Step 0.

### Design Minimal Tests

📂 Load method: `data/method-procedures/E010_Cognitive_MVP.md`

```
FOR EACH UNRESOLVED FEAR:

FEAR: "[what user is afraid of]"
STATUS: [still uncertain after research]

MINIMAL TEST:
"What's the SMALLEST thing I can do to learn if this fear is valid?"

PROBE DESIGN:
• Action: [minimal action]
• Effort: [LOW/MED/HIGH]
• Learning if succeeds: ___
• Learning if fails: ___

→ Failure becomes DATA, not defeat
```

### Growth Assessment

📂 Load method: `data/method-procedures/E014_Growth_Test.md`

```
FOR EACH MAJOR OPTION:

GROWTH TEST:
"Will attempting this force me to learn something new?"

┌────────────────────────────┬────────┬────────────────────┐
│ Growth Type                │ Y/N    │ What specifically  │
├────────────────────────────┼────────┼────────────────────┤
│ New learning forced        │        │                    │
│ New skill developed        │        │                    │
│ New experience gained      │        │                    │
│ Network/access expanded    │        │                    │
│ Thinking changed           │        │                    │
└────────────────────────────┴────────┴────────────────────┘

VERDICT:
[ ] HIGH GROWTH - worth doing even if "fails"
[ ] GAMBLING - reconsider
[ ] NEEDS REDESIGN - add learning component
```

### Fear Map Resolution

```
FEAR MAP UPDATE:

┌─────────────────────────────────────────────────────────────────┐
│ Fear from Step 0               │ Resolution Status              │
├────────────────────────────────┼────────────────────────────────┤
│ [fear 1]                       │ RESOLVED/ADDRESSED/REMAINS     │
│ [fear 2]                       │ RESOLVED/ADDRESSED/REMAINS     │
│ [fear 3]                       │ RESOLVED/ADDRESSED/REMAINS     │
└────────────────────────────────┴────────────────────────────────┘

RESOLUTION KEY:
• RESOLVED = Evidence shows fear was unfounded
• ADDRESSED = Mitigation plan exists
• REMAINS = True risk, accepted or pivoted
```

---

## Output: Challenge Results

```
╔═══════════════════════════════════════════════════════════════╗
║  CHALLENGE RESULTS                                             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  Beliefs Tested:        [count]                                ║
║  • Falsified:           [count]                                ║
║  • Survived:            [count]                                ║
║  • Modified:            [count]                                ║
║                                                                ║
║  Risks Identified:      [count]                                ║
║  Black Swans Found:     [count]                                ║
║  Biases Detected:       [list]                                 ║
║                                                                ║
║  MAP UPDATES:                                                   ║
║  • [what changed based on challenge]                           ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

## Output: Fear Resolution (if Fear-Based Mode)

```
╔═══════════════════════════════════════════════════════════════╗
║  FEAR RESOLUTION RESULTS                                       ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  FEARS FROM STEP 0:     [count]                                ║
║  • Resolved:            [count] (unfounded)                    ║
║  • Addressed:           [count] (mitigation exists)            ║
║  • Remains:             [count] (accepted risk)                ║
║                                                                ║
║  MINIMAL TESTS DESIGNED: [count]                               ║
║  • [test 1] → learns: [what]                                   ║
║  • [test 2] → learns: [what]                                   ║
║                                                                ║
║  GROWTH ASSESSMENT:                                             ║
║  • High growth options: [count]                                 ║
║  • Gambling options:    [count] (reconsider)                   ║
║                                                                ║
║  USER'S CONTROL ZONE:                                           ║
║  • Actionable items:    [list]                                 ║
║  • Let go of:           [list]                                 ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Transition

- **Always proceed to Step 5** (challenge is mandatory, never skip)
