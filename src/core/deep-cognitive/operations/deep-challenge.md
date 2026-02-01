# Deep Challenge V1.0 — Crystallize Vague Ideas

> **Purpose:** Transform unclear, ambiguous ideas into crystallized problem statements
> **When to use:** Beginning of project, unclear vision, too many unknowns
> **Key output:** Clear problem statement, success criteria, scope boundaries

---

## Operation Contract

```yaml
name: deep-challenge
version: "1.0"

applicable_when:
  phases: [idea]
  conditions:
    - "clarity_score < 0.7"
    - "problem_statement_unclear"
    - "scope_undefined"

inputs:
  required:
    - name: raw_idea
      type: text
      description: "User's initial idea, vision, or problem description"
  optional:
    - name: context
      type: text
      description: "Additional context about user, domain, constraints"

outputs:
  - name: crystallized_problem
    type: artifact
    path: docs/idea.md
    description: "Clear problem statement with all components"

  - name: unknowns_discovered
    type: list
    description: "Things we discovered we don't know"

  - name: clarity_score
    type: number
    description: "0.0-1.0 score of idea clarity"

state_effects:
  may_create: [docs/idea.md]
  may_update: [phases.idea, unknowns]
  may_discover: [unknowns, questions]

success_criteria:
  - criterion: "Problem statement is one clear sentence"
    measurement: "Can be read and understood without ambiguity"
  - criterion: "Target user is defined"
    measurement: "Specific persona or user type identified"
  - criterion: "Success criteria exist"
    measurement: "At least 2 measurable success criteria"
  - criterion: "Scope has boundaries"
    measurement: "Clear IN/OUT list exists"
```

---

## INVOCATION

When user triggers deep-challenge:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         DEEP CHALLENGE                                     ║
║                         Version 1.0                                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  This operation crystallizes vague ideas into clear problem statements.   ║
║                                                                            ║
║  I will help you:                                                          ║
║  • Clarify WHAT problem you're solving                                     ║
║  • Define WHO you're solving it for                                        ║
║  • Establish HOW you'll know you succeeded                                 ║
║  • Draw boundaries around scope                                            ║
║                                                                            ║
║  Please share your idea, vision, or problem.                              ║
║  Be as vague or detailed as you want — I'll help crystallize it.          ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## EXECUTION FLOW

### Step 0: Capture Raw Input

Receive user's raw idea. Store verbatim.

**Output:**
```yaml
raw_input:
  text: "[user's exact words]"
  received_at: [timestamp]
  word_count: [count]
  initial_clarity: [quick 0-1 estimate]
```

---

### Step 1: Challenge with Questions

Ask probing questions to uncover hidden assumptions and gaps.

**Core Questions (ask 3-5 relevant ones):**

| Category | Question |
|----------|----------|
| PROBLEM | "What specific pain point triggers this need?" |
| PROBLEM | "What happens if this problem isn't solved?" |
| USER | "Who experiences this problem most acutely?" |
| USER | "What does their day look like right now?" |
| VALUE | "If this exists, what changes for the user?" |
| VALUE | "How would you measure 'success'?" |
| SCOPE | "What is explicitly NOT part of this?" |
| SCOPE | "What's the smallest version that delivers value?" |
| TIMING | "Why now? What makes this urgent?" |
| ALTERNATIVES | "What do people do today instead?" |

**Anti-patterns to challenge:**
- "I want to build X" → Ask: "What problem does X solve?"
- "Everyone needs this" → Ask: "Who specifically, and how do you know?"
- "It should be simple" → Ask: "Simple for whom? To use or to build?"
- "AI-powered" → Ask: "What does AI enable that wasn't possible before?"

---

### Step 2: Extract Core Elements

Based on answers, extract:

```yaml
extracted_elements:
  problem:
    statement: "[one sentence]"
    pain_level: [1-10]
    frequency: [daily/weekly/monthly/occasional]

  user:
    primary: "[specific persona]"
    secondary: "[other users if any]"
    anti_user: "[who is this NOT for]"

  value:
    core_benefit: "[main thing user gets]"
    differentiator: "[why this vs alternatives]"

  success_criteria:
    - criterion: "[measurable outcome 1]"
    - criterion: "[measurable outcome 2]"
    - criterion: "[measurable outcome 3]"

  scope:
    in_scope:
      - "[thing 1]"
      - "[thing 2]"
    out_of_scope:
      - "[thing explicitly excluded]"
    minimum_viable:
      - "[absolute minimum features]"
```

---

### Step 3: Discover Unknowns

Actively probe for things that aren't known:

**Unknown Detection Prompts:**
1. "What assumptions are we making that might be wrong?"
2. "What do we need to learn before we can proceed?"
3. "What expertise might we be missing?"
4. "What could surprise us?"
5. "What are we assuming about the user that we haven't validated?"

**Categorize unknowns:**
```yaml
unknowns:
  technical:
    - "[something we don't know technically]"
  user:
    - "[something about users we're assuming]"
  market:
    - "[something about competitors/alternatives]"
  feasibility:
    - "[something about whether this is possible]"
```

---

### Step 4: Calculate Clarity Score

Score each dimension:

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Problem clarity | 0.25 | Is the problem statement unambiguous? |
| User definition | 0.20 | Is target user specific and validated? |
| Success criteria | 0.20 | Are criteria measurable and achievable? |
| Scope boundaries | 0.20 | Are IN/OUT clearly defined? |
| Unknowns addressed | 0.15 | Are critical unknowns identified? |

**Scoring:**
- 1.0 = Crystal clear, no ambiguity
- 0.8 = Clear, minor gaps
- 0.6 = Mostly clear, some assumptions
- 0.4 = Partial clarity, significant gaps
- 0.2 = Vague, many unknowns
- 0.0 = Completely unclear

**Gate threshold: 0.70**

---

### Step 5: Generate Crystallized Output

If clarity_score >= 0.70:

Create `docs/idea.md`:

```markdown
# [Project Name] — Idea Document

> **Status:** Crystallized
> **Clarity Score:** [score]
> **Date:** [date]
> **Generated by:** deep-challenge v1.0

---

## Problem Statement

[ONE clear sentence describing the problem]

### Pain Point
[Specific pain that triggers need]

### Impact of Inaction
[What happens if not solved]

---

## Target User

**Primary:** [specific persona]
- [key characteristic 1]
- [key characteristic 2]
- Current workaround: [what they do today]

**Not For:** [anti-user]

---

## Success Criteria

| # | Criterion | Measurement | Target |
|---|-----------|-------------|--------|
| 1 | [criterion] | [how measured] | [target value] |
| 2 | [criterion] | [how measured] | [target value] |
| 3 | [criterion] | [how measured] | [target value] |

---

## Scope

### In Scope
- [item 1]
- [item 2]
- [item 3]

### Out of Scope
- [explicitly excluded 1]
- [explicitly excluded 2]

### Minimum Viable (Phase 1)
- [absolute minimum feature 1]
- [absolute minimum feature 2]

---

## Known Unknowns

| Unknown | Type | Impact | How to Resolve |
|---------|------|--------|----------------|
| [unknown] | [tech/user/market/feasibility] | [high/medium/low] | [action] |

---

## Original Input

> [User's original verbatim input preserved]

---

## Reasoning Trace

[Summary of the challenge process, key questions asked, and how answers shaped the output]
```

---

### Step 6: Update Project State

```yaml
# Update project-state.yaml

current:
  phase: idea
  phase_progress: [clarity_score]

phases:
  idea:
    status: in_progress  # or completed if score >= 0.70
    started: [timestamp]
    clarity_score: [calculated score]
    artifacts: [docs/idea.md]

unknowns:
  discovered:
    - id: UNK-001
      description: "[unknown]"
      discovered_at: [timestamp]
      discovered_via: deep-challenge
      status: discovered

metrics:
  unknowns_discovered: [count]
  total_operations: +1
```

---

### Step 7: Recommend Next Action

Based on outcome:

**If clarity_score >= 0.70:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║  ✓ IDEA CRYSTALLIZED                                                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Clarity Score: [score] (threshold: 0.70)                                  ║
║  Artifact: docs/idea.md created                                            ║
║  Unknowns discovered: [count]                                              ║
║                                                                            ║
║  READY FOR: Verification Gate (idea_to_spec)                              ║
║                                                                            ║
║  RECOMMENDED NEXT:                                                         ║
║  → deep-verify: Verify idea completeness before proceeding                 ║
║  → deep-requirements: Begin specification phase                            ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**If clarity_score < 0.70:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║  ⚠ IDEA NEEDS MORE CLARITY                                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Clarity Score: [score] (threshold: 0.70)                                  ║
║                                                                            ║
║  GAPS IDENTIFIED:                                                          ║
║  • [dimension with low score]: [what's missing]                           ║
║  • [dimension with low score]: [what's missing]                           ║
║                                                                            ║
║  RECOMMENDED:                                                              ║
║  → Continue deep-challenge with focus on gaps                              ║
║  → OR: User provides more information on [specific area]                  ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Iteration Support

If user wants to refine:
1. Load previous `docs/idea.md`
2. Identify which dimension to improve
3. Ask targeted questions for that dimension only
4. Recalculate score
5. Update artifact

---

## Integration Points

**Updates project-state.yaml:**
- `current.phase_progress`
- `phases.idea.clarity_score`
- `phases.idea.status`
- `unknowns.discovered`
- `metrics.unknowns_discovered`
- `metrics.total_operations`

**Creates artifacts:**
- `docs/idea.md`

**Triggers:**
- Unknown detection for meta-cognitive layer
- Planner recommendation update

---

## Example Session

```
User: "Chcę zbudować aplikację do śledzenia nawyków"

deep-challenge:
1. "Co konkretnie przeszkadza ci w obecnych aplikacjach do nawyków?"
   → "Są zbyt skomplikowane, tracę czas na konfigurację"

2. "Kto konkretnie będzie używał tej aplikacji?"
   → "Ja i ludzie jak ja - zapracowani programiści"

3. "Jak poznasz że aplikacja 'działa'?"
   → "Jeśli po miesiącu nadal będę jej używał codziennie"

4. "Czego na pewno NIE chcesz w tej aplikacji?"
   → "Gamifikacji, odznak, social features"

→ Crystallized:
Problem: "Existing habit trackers are overcomplicated, causing busy professionals to abandon them within days"
User: "Busy software developers who value simplicity over features"
Success: "Daily usage maintained for 30+ days with <10 sec daily interaction"
Scope IN: Simple habit toggle, streak counter
Scope OUT: Gamification, social, analytics
Clarity Score: 0.82 ✓
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial PoC version |
