---
step: 0
name: "Frame"
time_estimate: "15-30 minutes"
goal: "Classify problem type, decompose feasibility questions, define assessment scope"
requires_completion: []
next_steps:
  DEFAULT: "steps/step-01-constrain.md"
  SCOPE_UNCLEAR: "STAY — clarify with user"
data_dependencies:
  - "data/theoretical-foundations.yaml"
  - "data/feasibility-scoring.yaml"
outputs:
  - cynefin_domain_map
  - sub_questions
  - scope_definition
  - complex_mode_flag
---

# Phase 0: FRAME

## MANDATORY EXECUTION RULES

1. **LOAD DATA FIRST** — Read `data/theoretical-foundations.yaml` before proceeding
2. **Complete all three methods** — 001, 002, 003 are mandatory
3. **Flag complexity** — If Complex-domain detected, set `complex_mode = on`
4. **Record outputs** — All outputs go to working document frontmatter

---

## 0.1 Cynefin Domain Classification (#001)

**Load:** `data/method-procedures/001_Cynefin_Domain_Classification.md`

**Purpose:** Determine WHAT TYPE of problem this is — because the type determines whether traditional feasibility assessment is even possible.

### Execute Method #001

```
For the subject being assessed, classify each component/sub-problem:

┌─────────────────────────────────────────────────────────────────────────────┐
│  CYNEFIN DOMAINS                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CLEAR (formerly Simple)                                                    │
│  • Cause→effect obvious to everyone                                         │
│  • Best practice exists                                                      │
│  • Assessment: Direct constraint checking                                   │
│  • Example: "Can we add another field to this form?"                        │
│                                                                              │
│  COMPLICATED                                                                │
│  • Cause→effect requires expertise to see                                   │
│  • Good practice exists (multiple valid approaches)                         │
│  • Assessment: Expert analysis                                              │
│  • Example: "Can we scale this database to 10× load?"                       │
│                                                                              │
│  COMPLEX                                                                    │
│  • Cause→effect only visible in retrospect                                  │
│  • Emergent behavior, no predictable outcome                                │
│  • Assessment: CANNOT ASSESS TRADITIONALLY — must probe                     │
│  • Example: "Will users adopt this new workflow?"                           │
│                                                                              │
│  CHAOTIC                                                                    │
│  • No perceivable cause→effect relationship                                 │
│  • Act first to create stability, assess later                              │
│  • Assessment: Not applicable — stabilize first                             │
│  • Example: "Production is down, everything is broken"                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Classification Process

1. List all components/aspects of the subject
2. For each, ask: "Can we predict the outcome of this?"
   - Yes, obviously → CLEAR
   - Yes, with expertise → COMPLICATED
   - Only in retrospect → COMPLEX
   - No pattern at all → CHAOTIC

3. **RED FLAG:** Treating Complex as Complicated
   - Applying expert analysis to emergent problems
   - This produces **confident but wrong** feasibility assessments
   - If detected: flag for probing instead of analysis

### Record Domain Map

```yaml
domain_map:
  - component: "[Component 1]"
    domain: "[Clear/Complicated/Complex/Chaotic]"
    assessment_approach: "[Direct check/Expert analysis/Probe/Stabilize first]"
    probe_needed: [true/false]
  - component: "[Component 2]"
    domain: "..."
    # continue for all components
```

**IF any component is COMPLEX:**
→ Set `complex_mode = on`
→ Note: "#303 Probe Design will be required for these components"

---

## 0.2 Feasibility Question Decomposition (#002)

**Load:** `data/method-procedures/002_Feasibility_Question_Decomposition.md`

**Purpose:** Break monolithic "Is this feasible?" into atomic, independently assessable sub-questions.

### Execute Method #002

```
Starting question: "Is [subject] feasible?"

DECOMPOSE along these fault lines:

1. BY COMPONENT/MODULE
   - What are the distinct parts?
   - Can each be assessed independently?

2. BY PHASE
   - Design feasibility
   - Build feasibility
   - Test feasibility
   - Deploy feasibility
   - Operate feasibility

3. BY DIMENSION (preview of Step 2)
   - Technically feasible?
   - Resource feasible?
   - Knowledge feasible?
   - Organizationally feasible?
   - Temporally feasible?
   - Compositionally feasible?
   - Economically feasible?
   - Regulatorily feasible?
   - Scale feasible?
   - Cognitively feasible?

4. BY RISK (most uncertain parts)
   - What's the most uncertain?
   - What has the least precedent?
```

### Assess Each Sub-Question

For each sub-question:
- [ ] Is it assessable NOW? (We have information)
- [ ] Does it need investigation? (We need to gather data)
- [ ] Does it depend on other sub-questions? (Dependencies)
- [ ] What Cynefin domain is it in? (From 0.1)

### Record Sub-Questions

```yaml
sub_questions:
  - id: "Q1"
    question: "[Specific feasibility question]"
    assessable_now: [true/false]
    needs_investigation: [true/false]
    depends_on: ["Q2", "Q3"]  # or []
    cynefin_domain: "[Clear/Complicated/Complex]"
  - id: "Q2"
    question: "..."
    # continue for all sub-questions
```

**STOP DECOMPOSING when:**
- Sub-questions are directly assessable, OR
- They clearly need a probe (#303)
- **Zeno's paradox warning:** Infinite decomposition is itself infeasible

---

## 0.3 Feasibility Scope Definition (#003)

**Load:** `data/method-procedures/003_Feasibility_Scope_Definition.md`

**Purpose:** Explicitly define WHAT is being assessed and WHAT IS NOT. Scope creep in feasibility assessment is as real as scope creep in projects.

### Execute Method #003

Answer these questions explicitly:

```
1. SUBJECT: What exactly are we assessing?
   □ The whole project?
   □ A specific component?
   □ A decision between options?
   □ A migration path?

   Answer: _________________________________

2. HORIZON: Feasibility by when?
   □ Next sprint?
   □ Next quarter?
   □ Next year?
   □ No specific deadline?

   Answer: _________________________________

3. STANDARD: Feasible means what?
   □ Working prototype?
   □ Production-ready?
   □ Scaled to target load?
   □ Maintained for X years?

   Answer: _________________________________

4. EXCLUSIONS: What are we NOT assessing?
   (List explicitly — prevents scope creep)

   - _________________________________
   - _________________________________
   - _________________________________

5. ASSUMPTIONS: What are we taking as given?
   (These become risks if wrong — hand off to Deep-Risk)

   - _________________________________
   - _________________________________
   - _________________________________
```

### Record Scope

```yaml
scope:
  subject: "[precise description]"
  horizon: "[deadline/timeline]"
  standard: "[what 'feasible' means]"
  exclusions:
    - "[What we're not assessing]"
  assumptions:
    - "[What we're taking as given]"
```

**Why this matters:** "Is this feasible?" without scope is unanswerable.
"Can we deliver a production-ready Delta Lake pipeline for EPR reporting by Q2 with the current 3-person team assuming Mars provides data in agreed format?" — THAT is assessable.

---

## 0.4 Update Frontmatter

After completing FRAME, update working document:

```yaml
---
workflow: deep-feasibility
subject: "[from 0.3]"
started: "[current ISO timestamp]"
depth: [quick/standard/comprehensive/critical]
complex_mode: [on/off]

domain_map:
  - component: "..."
    domain: "..."
    probe_needed: [true/false]

sub_questions:
  - id: "Q1"
    question: "..."
    assessable_now: [true/false]

scope:
  subject: "..."
  horizon: "..."
  standard: "..."
  exclusions: [...]
  assumptions: [...]

steps_completed: [0]
current_step: 1
dimensions_scored: []
constraints_found: []
conditions: []
decision: null
confidence: null
---
```

---

## 0.5 Proceed to CONSTRAIN

**Before loading Step 1, verify:**

- [ ] Cynefin domain classified for all components
- [ ] Sub-questions decomposed and dependency-mapped
- [ ] Scope explicitly defined (subject, horizon, standard, exclusions, assumptions)
- [ ] Complex components flagged (if any)
- [ ] Frontmatter updated

**Next step:** Load `steps/step-01-constrain.md`

**Navigation:**
- ↓ PROCEED if scope is clear and components classified
- ↓ STAY if framing is unclear — clarify with user first

---

## Output Checklist

Before proceeding, confirm:

- [ ] `domain_map` populated with all components
- [ ] `sub_questions` list complete
- [ ] `scope` fully defined
- [ ] `complex_mode` flag set correctly
- [ ] Ready to identify constraints
