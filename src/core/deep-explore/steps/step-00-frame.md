---
step: 0
name: "Frame"
time_estimate: "5-10 minutes"
goal: "Define exploration context, constraints, and abstraction level"
requires_completion: []
next_steps:
  DEFAULT: "steps/step-01-map.md"
outputs:
  - vision
  - hard_constraints
  - abstraction_level
  - problem_type
  - exploration_scope
---

# Phase 0: Frame

## MANDATORY EXECUTION RULES

1. **NO SOLUTIONS YET** — This phase defines the problem, not options
2. **Complete all sections** — Do not skip problem type assessment
3. **Challenge stated constraints** — Soft constraints disguised as hard
4. **Set abstraction level explicitly** — Prevents scope creep
5. **Record in frontmatter** — All outputs go to document frontmatter

---

## 0.1 Vision Capture

**Define what you want to ACHIEVE, not HOW to achieve it.**

The vision should be:
- Outcome-focused (what success looks like)
- Solution-agnostic (no specific approach embedded)
- Measurable (how would you know you succeeded?)

```
VISION TEMPLATE:

In [timeframe], we want to [achieve outcome] 
so that [benefit/value] 
as measured by [success metrics].

Example:
"In 6 months, we want to have a scalable system for processing 
customer orders so that we can handle 10x current volume 
as measured by orders processed per hour and error rate."

NOT:
"In 6 months, we want to build a microservices architecture 
on Kubernetes" ← This is a solution, not a vision
```

**Capture:**

```
VISION:
_________________________________________________________
_________________________________________________________

SUCCESS LOOKS LIKE:
1. ______________________________________________________
2. ______________________________________________________
3. ______________________________________________________

SUCCESS METRICS:
1. ______________________________________________________
2. ______________________________________________________
```

→ **HALT** — Wait for vision to be defined

---

## 0.2 Hard Constraints Identification

**List what is TRULY impossible, not merely difficult.**

Apply the constraint test to each:

```
For each stated constraint, ask:

1. What happens if we violate it?
   - Legal consequences? → HARD
   - Someone gets upset? → SOFT
   
2. Who imposed this constraint?
   - Laws of physics/math? → HARD
   - A person who could change their mind? → SOFT
   
3. Could $10M change this constraint?
   - No → HARD
   - Yes → SOFT

4. Is this POLICY or PHYSICS?
   - Physics → HARD (can't change gravity)
   - Policy → SOFT (policies can be changed)
```

**Record:**

```
HARD CONSTRAINTS (truly immovable):

1. ______________________________________________________
   Source: _______________  Test: _______________

2. ______________________________________________________
   Source: _______________  Test: _______________

3. ______________________________________________________
   Source: _______________  Test: _______________


SOFT CONSTRAINTS (reclassified as preferences):

1. Originally stated: ___________________________________
   Reclassified because: _______________________________

2. Originally stated: ___________________________________
   Reclassified because: _______________________________
```

→ **HALT** — Wait for constraints to be classified

---

## 0.3 Abstraction Level Selection

**Choose the level at which to explore:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  STRATEGIC                                                               │
│  ─────────────────────────────────────────────────────────────────────  │
│  • "Should we enter this market?"                                       │
│  • "What business model should we use?"                                 │
│  • "Build vs Buy vs Partner?"                                           │
│  • Time horizon: 1-5 years                                              │
│  • Decision maker: Executives, Board                                    │
│  • Consequences: Company direction, major investment                    │
├─────────────────────────────────────────────────────────────────────────┤
│  TACTICAL                                                                │
│  ─────────────────────────────────────────────────────────────────────  │
│  • "How should we structure this product?"                              │
│  • "Which vendor should we use?"                                        │
│  • "What technology stack?"                                             │
│  • Time horizon: 3-12 months                                            │
│  • Decision maker: Directors, Leads                                     │
│  • Consequences: Project success, team allocation                       │
├─────────────────────────────────────────────────────────────────────────┤
│  OPERATIONAL                                                             │
│  ─────────────────────────────────────────────────────────────────────  │
│  • "How should we implement this feature?"                              │
│  • "Which library should we use?"                                       │
│  • "How should we structure this code?"                                 │
│  • Time horizon: Days-Weeks                                             │
│  • Decision maker: Individual contributors                              │
│  • Consequences: Implementation quality, velocity                       │
└─────────────────────────────────────────────────────────────────────────┘
```

**Select:**

```
ABSTRACTION LEVEL: [ ] STRATEGIC  [ ] TACTICAL  [ ] OPERATIONAL

Justification: ___________________________________________

Scope boundaries:
• IN SCOPE: ____________________________________________
• OUT OF SCOPE (too high): _____________________________
• OUT OF SCOPE (too low): ______________________________
```

→ **HALT** — Wait for level selection

---

## 0.4 Problem Type Assessment (Cynefin)

**Identify what type of problem you're facing:**

```
┌─────────────────────────┬─────────────────────────┐
│       COMPLEX           │      COMPLICATED        │
│                         │                         │
│  "We don't know what    │  "We can analyze this   │
│   we don't know"        │   and find the answer"  │
│                         │                         │
│  Characteristics:       │  Characteristics:       │
│  • Novel situation      │  • Known problem type   │
│  • Cause-effect unclear │  • Experts can solve    │
│  • Emergent patterns    │  • Best practices exist │
│  • Need experiments     │  • Analysis works       │
│                         │                         │
│  Approach:              │  Approach:              │
│  Probe → Sense → Act    │  Sense → Analyze → Act  │
│  (Small experiments)    │  (Expert analysis)      │
│                         │                         │
│  Examples:              │  Examples:              │
│  • New market entry     │  • Database selection   │
│  • Org culture change   │  • Vendor evaluation    │
│  • Innovation strategy  │  • Architecture design  │
├─────────────────────────┼─────────────────────────┤
│       CHAOTIC           │       CLEAR             │
│                         │                         │
│  "Crisis mode"          │  "Obvious answer"       │
│                         │                         │
│  Characteristics:       │  Characteristics:       │
│  • No time to analyze   │  • Best practice known  │
│  • Must act now         │  • Everyone agrees      │
│  • Stabilize first      │  • Simple cause-effect  │
│                         │                         │
│  Approach:              │  Approach:              │
│  Act → Sense → Respond  │  Sense → Categorize →   │
│  (Stabilize, then...)   │  Respond (Apply rule)   │
│                         │                         │
│  Examples:              │  Examples:              │
│  • Security breach      │  • Standard procedures  │
│  • Leadership vacuum    │  • Routine decisions    │
│  • System down          │  • Well-trodden paths   │
└─────────────────────────┴─────────────────────────┘
```

**Assess:**

```
PROBLEM TYPE: [ ] COMPLEX  [ ] COMPLICATED  [ ] CLEAR  [ ] CHAOTIC

Evidence for this classification:
1. ______________________________________________________
2. ______________________________________________________
3. ______________________________________________________

If COMPLEX:
  → Exploration should include EXPERIMENT DESIGN
  → Accept that "best answer" may not exist
  → Focus on learning, not finding

If COMPLICATED:
  → Expert analysis will work
  → Good/better/best likely exists
  → Deep Explore will find it

If CLEAR:
  → Do you actually need Deep Explore?
  → Maybe just execute the obvious answer
  → [ ] Yes, still explore  [ ] No, skip to action

If CHAOTIC:
  → Stabilize first, then explore
  → What must be done IMMEDIATELY? _____________________
```

→ **HALT** — Wait for problem type assessment

---

## 0.5 Existing Assumptions & Biases

**What are you already assuming? What might you be biased toward?**

```
KNOWN ASSUMPTIONS (make explicit):

1. I'm assuming: ________________________________________
   If wrong: ___________________________________________

2. I'm assuming: ________________________________________
   If wrong: ___________________________________________

3. I'm assuming: ________________________________________
   If wrong: ___________________________________________


POTENTIAL BIASES (acknowledge):

□ Anchoring: Am I fixated on a specific option already?
  If yes, which? _______________________________________

□ Confirmation: Am I looking to validate a decision already made?
  If yes, what decision? ________________________________

□ Availability: Am I over-weighting recent/vivid examples?
  If yes, which? _______________________________________

□ Sunk Cost: Am I considering past investments that shouldn't matter?
  If yes, what investment? ______________________________

□ Authority: Am I deferring to someone's opinion without evidence?
  If yes, whose? _______________________________________


COMMITMENT:
"I will explore ALL options fully before converging,
 even if early options seem obviously better."

[ ] Acknowledged
```

→ **HALT** — Wait for bias check completion

---

## 0.6 Update Frontmatter

After completing frame, initialize working document:

```yaml
---
workflow: deep-explore
decision: "[name from user]"
started: "[current ISO timestamp]"

# Frame outputs
vision: "[from 0.1]"
success_metrics: ["metric1", "metric2", "metric3"]
hard_constraints: ["constraint1", "constraint2"]
soft_constraints_reclassified: ["former_constraint1"]
abstraction_level: [STRATEGIC / TACTICAL / OPERATIONAL]
problem_type: [COMPLEX / COMPLICATED / CLEAR / CHAOTIC]

# Scope
in_scope: ["item1", "item2"]
out_of_scope: ["item1", "item2"]

# Bias awareness
known_assumptions: ["assumption1", "assumption2"]
potential_biases: ["bias1", "bias2"]
anchored_option: "[option if any, or null]"

# Exploration state
stepsCompleted: [0]
currentStep: 1
coverageScore: 0
dimensions: []
options: []
consequences: []
risks: []

# Output
recommendation: null
experiments_suggested: []
---
```

---

## 0.7 Proceed to MAP Phase

**Before proceeding, verify:**

- [ ] Vision is outcome-focused (not solution-focused)
- [ ] Hard constraints tested and validated
- [ ] Soft constraints reclassified
- [ ] Abstraction level selected with clear scope
- [ ] Problem type identified
- [ ] Biases acknowledged
- [ ] Frontmatter initialized

**Next step:** Load `steps/step-01-map.md`

**Guidance for Phase 1 based on problem type:**

| Problem Type | Phase 1 Guidance |
|--------------|------------------|
| COMPLEX | Extra dimension discovery effort; include "experiment" as option |
| COMPLICATED | Standard execution; experts may help identify dimensions |
| CLEAR | Quick pass; may exit early if obvious answer confirmed |
| CHAOTIC | Focus on stabilization dimensions first |

---

## Output Checklist

Before proceeding, confirm:

- [ ] `vision` captures outcome, not solution
- [ ] `hard_constraints` survive all tests
- [ ] `abstraction_level` is explicit
- [ ] `problem_type` is classified
- [ ] `known_assumptions` are documented
- [ ] `potential_biases` are acknowledged
- [ ] Frontmatter initialized with all required fields
- [ ] Ready to load Phase 1 methods
