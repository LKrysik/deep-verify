# Deep Analysis Framework — Integration Guide & SKILL.md

## Overview

The Deep Analysis Framework is a tetrad of complementary reasoning processes:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   EXPLORE ──→ VERIFY ──→ FEASIBILITY ──→ RISK       │
│      ↑           │            │            │        │
│      └───────────┴────────────┴────────────┘        │
│                 (feedback loops)                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

| Process | Question | Deliverable | Methods |
|---------|----------|-------------|---------|
| **Deep-Explore** | What CAN we do? | Decision space map | 54 methods in 5 phases + META |
| **Deep-Verify** | Is this CORRECT? | Validation report | 14 methods in 5 categories |
| **Deep-Feasibility** | CAN we do it? | Feasibility profile | 35 methods in 5 phases + META |
| **Deep-Risk** | What can go WRONG? | Risk register + mitigations | 44 methods in 6 phases + META |

**Why a tetrad, not sequential steps:**
These are not a linear pipeline. They form a graph with feedback loops. Feasibility may invalidate Explore options. Risk assessment may reveal that mitigation itself is infeasible. Verification may surface impossibilities that reframe the entire decision. The integration guide defines HOW to navigate this graph.

---

## System Prompt

```
<deep_analysis_framework>
You are an expert analytical agent equipped with four complementary reasoning processes. Use them systematically to provide thorough, rigorous analysis.

THE FOUR PROCESSES:

1. DEEP-EXPLORE: Maps the decision space. Use when the user needs to understand options, generate alternatives, or make a decision among choices.
   Phases: MAP → ILLUMINATE → CHALLENGE → SYNTHESIZE → CONVERGE
   Key strength: Divergent thinking, option discovery, trade-off analysis
   Key methods: Dimension Discovery, Option Enumeration, Premortem, Black Swan Hunt

2. DEEP-VERIFY: Validates logical and technical correctness. Use when claims need checking, requirements need conflict detection, or theoretical limits apply.
   Categories: theory, conflict, depend, coherence, sanity
   Key strength: Finding impossibilities, contradictions, and false claims
   Key methods: Theoretical Impossibility Check, Definitional Contradiction, Pairwise Compatibility, Constructive Counterexample

3. DEEP-FEASIBILITY: Assesses whether something can actually be executed. Use when a plan, architecture, or decision needs executability assessment.
   Phases: FRAME → CONSTRAIN → ASSESS → VALIDATE → DECIDE
   Key strength: Multi-dimensional feasibility, planning fallacy correction, constraint identification
   Key methods: Constraint Hardness, Requisite Variety, TRL Analysis, Reference Class Forecasting, Compositional Feasibility

4. DEEP-RISK: Assesses what can go wrong and designs responses. Use when threats need identification, quantification, and mitigation planning.
   Phases: GROUND → IDENTIFY → QUANTIFY → INTERACT → MITIGATE → MONITOR
   Key strength: Risk interactions, cascade mapping, non-ergodic risk detection, defense design
   Key methods: Risk Genesis, Ergodicity Test, Cascade Mapping, Cobra Effect Check, Defense in Depth

ROUTING LOGIC — Which process to invoke:

PRIMARY SIGNAL → PROCESS:
- "What should we do?" / "What are our options?" / Decision needed → EXPLORE
- "Is this correct?" / "Does this work?" / Validate claims → VERIFY
- "Can we do this?" / "Is this achievable?" / Go/No-Go → FEASIBILITY
- "What could go wrong?" / "How risky is this?" / Threat assessment → RISK

COMPOUND SIGNALS → SEQUENCE:
- "Should we do X?" → EXPLORE (options) → VERIFY (correctness) → FEASIBILITY (can we?) → RISK (what if?)
- "Review this architecture" → VERIFY (correctness) → FEASIBILITY (scalability, resources) → RISK (failure modes)
- "We're deciding between A and B" → EXPLORE (illuminate both) → VERIFY (both valid?) → FEASIBILITY (both achievable?) → RISK (compare risk profiles)
- "Is this plan realistic?" → FEASIBILITY (primary) → RISK (what threatens it?)
- "Debug this design" → VERIFY (primary) → RISK (what we missed)

SCALING — How deep to go:

| Complexity | Approach | Time |
|-----------|---------|------|
| Simple question | Single process, core methods only | Minutes |
| Standard decision | 1-2 processes, standard depth | Hours |
| Major decision | Full tetrad, comprehensive | Days |
| Critical/irreversible | Full tetrad + META + validation | Week+ |

HANDOFF PROTOCOL:

When one process produces findings that trigger another:
1. State: "[PROCESS-A] finding triggers [PROCESS-B]"
2. Pass: specific finding (not the entire output)
3. Run: targeted methods in Process-B
4. Return: findings back to original context

Examples:
- VERIFY finds impossibility → EXPLORE needs new options
- FEASIBILITY finds binding constraint → EXPLORE needs reframing
- RISK finds non-ergodic threat → FEASIBILITY must assess mitigation feasibility
- EXPLORE finds novel option → VERIFY must check correctness, FEASIBILITY must assess executability

FEEDBACK LOOPS:

Always check for these circular dependencies:
- Risk mitigation needs its own feasibility assessment
- Feasibility conditions create new risks to monitor
- Verification findings may invalidate explored options
- Exploration of alternatives may introduce new verification needs

When a loop is detected, resolve by:
1. Identifying the tightest constraint (what must be true for anything to work)
2. Validating that constraint first
3. Building outward from the validated core

META-AWARENESS:

After completing analysis, always ask:
- Did I use the RIGHT process(es) for this question?
- Did I miss a feedback loop?
- Is my analysis biased toward one process? (e.g., all Explore, no Verify)
- Would a different sequence have been more efficient?
- Is the analysis deep ENOUGH for the stakes involved?

IMPORTANT CONSTRAINTS:
- Never skip VERIFY for technical claims — optimism kills projects
- Never skip FEASIBILITY for plans — planning fallacy is universal
- Never skip RISK for irreversible decisions — non-ergodic risks can end the game
- Always apply META methods when stakes are high
- For Complex (Cynefin) problems: probe, don't analyze
</deep_analysis_framework>
```

---

## Routing Decision Tree

```
User request received
│
├── What TYPE of question?
│   │
│   ├── "What should we do?" / Options / Decision
│   │   └── → EXPLORE (primary)
│   │       └── If options are technical → + VERIFY
│   │       └── If options need execution → + FEASIBILITY
│   │       └── If stakes are high → + RISK
│   │
│   ├── "Is this correct?" / Validate / Review
│   │   └── → VERIFY (primary)
│   │       └── If issues found → EXPLORE (alternatives)
│   │       └── If valid → FEASIBILITY (can we build it?)
│   │
│   ├── "Can we do this?" / Achievable / Realistic
│   │   └── → FEASIBILITY (primary)
│   │       └── If conditionally feasible → RISK (threats to conditions)
│   │       └── If infeasible → EXPLORE (reframe, alternatives)
│   │
│   ├── "What could go wrong?" / Risks / Threats
│   │   └── → RISK (primary)
│   │       └── If mitigation designed → FEASIBILITY (is mitigation feasible?)
│   │       └── If non-ergodic risks found → FEASIBILITY (can we survive?)
│   │
│   └── Compound / "Should we...?" / Full analysis
│       └── → FULL TETRAD (sequence below)
│
├── What are the STAKES?
│   │
│   ├── Low (easily reversible, small impact)
│   │   └── Single process, core methods, quick
│   │
│   ├── Medium (meaningful but recoverable)
│   │   └── 1-2 processes, standard depth
│   │
│   ├── High (significant impact, hard to reverse)
│   │   └── Full tetrad, comprehensive
│   │
│   └── Critical (irreversible, existential)
│       └── Full tetrad + META + validation + stakeholder review
│
└── What DOMAIN is the problem? (Cynefin)
    │
    ├── Clear → Direct analysis, minimal process
    ├── Complicated → Expert-driven, full processes
    ├── Complex → PROBE first, then analyze
    └── Chaotic → ACT first, then stabilize, then analyze
```

---

## Sequencing Patterns

### Pattern 1: Full Tetrad (Comprehensive)

The default sequence for major decisions:

```
EXPLORE                    VERIFY                    FEASIBILITY               RISK
───────                    ──────                    ───────────               ────
1. MAP options         →   4. Check correctness  →   7. Assess feasibility →  10. Identify risks
2. ILLUMINATE effects      5. Find conflicts         8. Validate critical      11. Quantify severity
3. CHALLENGE assumptions   6. Test impossibilities    9. Decide Go/No-Go       12. Design mitigations
                                                                               13. Build monitoring

Feedback loops:
- Step 6 (impossibility) → Step 1 (new options)
- Step 9 (infeasible) → Step 1 (reframe) or Step 3 (new constraints)
- Step 12 (mitigation) → Step 8 (is mitigation feasible?)
- Step 10 (risks) → Step 7 (risks change feasibility)
```

### Pattern 2: Validate-First (Technical Review)

For reviewing existing designs, architectures, or plans:

```
VERIFY → FEASIBILITY → RISK → (EXPLORE if issues found)
```

Start by checking correctness. If correct, assess feasibility. If feasible, assess risks. Only explore alternatives if issues found.

### Pattern 3: Feasibility-Gate (Go/No-Go)

For investment or commitment decisions:

```
FEASIBILITY → RISK → DECIDE
                └──→ EXPLORE (only if No-Go, to find alternatives)
```

Skip Explore (options already known). Skip Verify (correctness assumed). Focus on "can we?" and "what threatens us?"

### Pattern 4: Risk-First (Crisis/Incident)

For urgent situations or incident response:

```
RISK (rapid identification) → FEASIBILITY (of response) → EXPLORE (alternatives if blocked)
```

### Pattern 5: Iterative Deepening

For evolving understanding:

```
Round 1: EXPLORE (quick) → VERIFY (quick) → FEASIBILITY (quick) → RISK (quick)
Round 2: Deep dive into whatever process surfaced the biggest concern
Round 3: Targeted analysis of specific findings
```

---

## Handoff Specifications

### What Each Process Passes to Others

**EXPLORE produces → consumed by:**

| Output | Consumer | How It's Used |
|--------|----------|---------------|
| Options list | VERIFY | Check each option for correctness |
| Options list | FEASIBILITY | Assess each option's executability |
| Options list | RISK | Assess each option's risk profile |
| Assumptions (#23) | FEASIBILITY #302 | Critical assumption testing |
| Assumptions (#23) | RISK #105 | Assumption torture |
| Dependencies (#13) | FEASIBILITY #210 | Dependency feasibility |
| Dependencies (#13) | RISK #104 | Dependency risk discovery |
| Stakeholder map (#14) | FEASIBILITY #204 | Organizational feasibility |
| Constraints (#3) | FEASIBILITY #101 | Constraint hardness spectrum |

**VERIFY produces → consumed by:**

| Output | Consumer | How It's Used |
|--------|----------|---------------|
| Impossibility findings (#153) | FEASIBILITY #101 | H5 hard constraints |
| Impossibility findings (#153) | EXPLORE | Eliminate impossible options, reframe |
| Contradictions (#154, #161) | FEASIBILITY #103 | TRIZ contradiction input |
| Validated claims (#163) | RISK | Scope of risk assessment (what's actually claimed) |
| Composition gaps (#166) | FEASIBILITY #206 | Compositional feasibility concerns |
| Composition gaps (#166) | RISK #108 | Boundary risk scan inputs |
| Conflict matrix (#158) | FEASIBILITY | Requirements that cannot coexist |

**FEASIBILITY produces → consumed by:**

| Output | Consumer | How It's Used |
|--------|----------|---------------|
| Infeasible options | EXPLORE | Eliminate, generate alternatives |
| Binding constraints (#401) | EXPLORE | Reframe problem around constraints |
| Conditions for feasibility (#403) | RISK #406 | Contingency trigger design |
| Conditions for feasibility (#403) | RISK #501 | Leading indicator identification |
| Scale concerns (#208) | RISK #207 | Stability basin mapping |
| Conway misalignment (#104) | RISK #304 | Concentration risk (org dimension) |
| TRL gaps (#201) | RISK #101 | Technology category risks |
| Resource gaps (#202) | RISK #202 | Exposure window timing |

**RISK produces → consumed by:**

| Output | Consumer | How It's Used |
|--------|----------|---------------|
| Mitigation plans (#401-407) | FEASIBILITY | Assess feasibility of mitigations |
| Non-ergodic risks (#206) | FEASIBILITY #207 | Economic feasibility (survival constraint) |
| Cascade maps (#301) | FEASIBILITY #206 | Compositional feasibility (cascade = integration risk) |
| Compound scenarios (#305) | FEASIBILITY #302 | Critical assumption testing under stress |
| Risk-driven requirements | VERIFY | New requirements need conflict checking |
| Cobra effect findings (#407) | EXPLORE | Need alternative mitigations |
| Leading indicators (#501) | FEASIBILITY #404 | Feasibility decay triggers |

---

## Feedback Loop Protocols

### Loop 1: Impossibility → Reframe

```
VERIFY finds impossibility (e.g., CAP theorem violation)
    │
    ├── STOP: Current approach is invalid
    │
    └── TRIGGER: EXPLORE with new constraint
        "Given that we CANNOT have X+Y+Z simultaneously,
         what options exist if we sacrifice X? Or Y? Or Z?"
        │
        └── EXPLORE generates new options → return to VERIFY
```

### Loop 2: Infeasibility → Redesign

```
FEASIBILITY finds binding constraint (e.g., timeline infeasible)
    │
    ├── Can constraint be loosened? (negotiate deadline, reduce scope)
    │   └── If yes → reassess with new constraint
    │
    └── Cannot be loosened → TRIGGER: EXPLORE
        "Given hard constraint [X], how do we reframe
         the problem to be feasible within [X]?"
        │
        └── EXPLORE generates feasible alternatives → VERIFY → FEASIBILITY
```

### Loop 3: Mitigation Feasibility

```
RISK designs mitigation (e.g., "add redundant pipeline")
    │
    └── TRIGGER: FEASIBILITY for the mitigation itself
        "Is it feasible to add redundant pipeline given
         current team size and timeline?"
        │
        ├── Feasible → proceed with mitigation
        │
        └── Infeasible → TRIGGER: RISK
            "Mitigation is infeasible. What's the residual risk?
             What alternative mitigation exists?"
            │
            └── RISK designs alternative → back to FEASIBILITY
```

### Loop 4: Condition-Risk Bridge

```
FEASIBILITY identifies condition: "Feasible IF vendor delivers by March"
    │
    └── TRIGGER: RISK
        "What risks threaten the condition 'vendor delivers by March'?"
        │
        ├── RISK identifies risks to condition
        │
        └── RISK designs monitoring/mitigation for the condition
            │
            └── → FEASIBILITY's condition monitoring (#404)
```

### Loop 5: Verification-Driven Scope Change

```
VERIFY finds conflict: "Requirement A contradicts Requirement B"
    │
    ├── Cannot have both → EXPLORE: which to keep?
    │
    └── Resolved by redefining → FEASIBILITY: is resolution feasible?
        │
        └── → RISK: what new risks from the resolution?
```

---

## Process Selection Heuristics

### When to Use Each Process ALONE

| Signal | Process | Skip Others Because |
|--------|---------|-------------------|
| "List my options for X" | EXPLORE only | Not evaluating yet, just mapping |
| "Is this theorem correct?" | VERIFY only | Pure correctness, no execution or risk |
| "Can we deliver this by Friday?" | FEASIBILITY only | Specific constraint check |
| "What are the risks of X?" | RISK only | Option already chosen, need risk profile |

### When to Combine (Most Cases)

| Signal | Sequence | Why This Order |
|--------|----------|---------------|
| "Should we use Kafka or Pulsar?" | EXPLORE → VERIFY → FEASIBILITY → RISK | Need full picture before deciding |
| "Review this architecture" | VERIFY → FEASIBILITY → RISK | Already designed, need validation |
| "Can we migrate to Unity Catalog?" | FEASIBILITY → RISK | Option known, need Go/No-Go |
| "We're getting errors in pipeline" | VERIFY (find bug) → RISK (what else is affected?) | Debug first, then assess blast radius |
| "Plan our Q3 OKRs" | EXPLORE → FEASIBILITY | Generate goals, then reality-check |
| "This proposal seems too good" | VERIFY → FEASIBILITY → RISK | Suspicion = check correctness first |

### When to Use META

| Signal | Action |
|--------|--------|
| Analysis feels "too clean" | Apply Cognitive Bias Audit, Confidence Theater Detection |
| Team quickly agrees | Apply Groupthink check, Devil's Advocate |
| Estimate seems aggressive | Apply Planning Fallacy Detection, Hofstadter Correction |
| All scores are similar | Apply Simpson's Paradox Audit |
| Dashboard all green | Apply Goodhart's Law Check |
| High stakes, irreversible | Apply ALL META methods from every process |

---

## Cross-Process Method Synergies

Some methods from different processes are particularly powerful when combined:

### Synergy 1: Assumption Chain
```
EXPLORE #23 (Assumption Stress Test)
    → FEASIBILITY #302 (Critical Assumption Testing)
        → RISK #105 (Assumption Torture at 10/50/100%)
```
Progressively deeper assumption analysis: discover → test → stress to failure.

### Synergy 2: Contradiction Resolution
```
VERIFY #154 (Definitional Contradiction)
    → FEASIBILITY #103 (TRIZ Contradiction Detection)
        → EXPLORE if TRIZ resolves → new option
        → RISK if unresolved → fundamental risk
```
Find contradiction → attempt creative resolution → manage what remains.

### Synergy 3: Dependency Chain
```
EXPLORE #13 (Dependency Analysis)
    → FEASIBILITY #210 (Dependency Feasibility)
        → RISK #104 (Dependency Risk Discovery)
            → RISK #303 (Common Mode Failure)
```
Map dependencies → assess feasibility → assess risk → find hidden shared dependencies.

### Synergy 4: Scale Stress
```
FEASIBILITY #208 (Scale Feasibility)
    → RISK #207 (Stability Basin Mapping)
        → RISK #110 (Chaos Probe Design)
```
Assess theoretical scale → measure distance to tipping → empirically test failure.

### Synergy 5: Organizational Reality
```
FEASIBILITY #104 (Conway Alignment)
    → FEASIBILITY #204 (Organizational Feasibility)
        → RISK #304 (Concentration Risk - people dimension)
            → EXPLORE #14 (Stakeholder Impact)
```
Check org-architecture alignment → assess org capability → find people concentration → understand stakeholder dynamics.

---

## Scaling Guide

### For AI Agents (Claude, etc.)

**Quick analysis (single response):**
- Identify primary question type
- Select ONE process, 3-5 core methods
- Apply methods inline
- Note what WASN'T covered and why

**Standard analysis (multi-turn):**
- Turn 1: Identify question type, propose process sequence
- Turn 2-4: Execute primary process
- Turn 5-6: Execute secondary process(es) triggered by findings
- Turn 7: Synthesize and present decision

**Deep analysis (project mode):**
- Full tetrad execution across multiple sessions
- Maintain state across turns (risk register, feasibility profile, verified claims)
- Use feedback loops between processes
- Apply META at end of each process

### For Human Teams

**Workshop format (half day):**
1. 30 min: EXPLORE core methods (MAP + ILLUMINATE)
2. 30 min: VERIFY quick scan (impossibilities + conflicts)
3. 60 min: FEASIBILITY core assessment (10 dimensions)
4. 60 min: RISK core methods (IDENTIFY + QUANTIFY)
5. 30 min: Synthesis and decision

**Sprint integration:**
- Sprint planning: FEASIBILITY quick check on new stories
- Design review: VERIFY + FEASIBILITY focused
- Pre-release: RISK focused
- Retrospective: META methods across all processes

**Quarterly strategic review:**
- Full tetrad on strategic decisions
- Re-assess feasibility of in-flight projects
- Refresh risk registers
- Challenge assumptions from previous quarters

---

## Anti-Patterns

### Process Anti-Patterns

| Anti-Pattern | Description | Fix |
|-------------|-------------|-----|
| **Analysis Paralysis** | Running all methods from all processes on every question | Scale depth to stakes. Quick check for small decisions. |
| **Process Skipping** | Skipping VERIFY because "we trust the design" | Non-negotiable: always verify technical claims |
| **Sequential Only** | Never using feedback loops | After each process, ask "does this change previous findings?" |
| **Feasibility Last** | Assessing feasibility only after full design | Feasibility early prevents wasted design effort |
| **Risk First** | Starting with "what could go wrong" before understanding options | Risk without context is anxiety, not analysis |
| **Single Process** | Only using EXPLORE (or only VERIFY, etc.) | At minimum: primary process + one complementary |
| **All META** | Spending more time auditing the process than doing analysis | META should be ~10-15% of total effort |
| **No META** | Never checking for bias in the analysis | Minimum: Planning Fallacy check for any estimate |

### Handoff Anti-Patterns

| Anti-Pattern | Description | Fix |
|-------------|-------------|-----|
| **Data Loss** | Not passing findings between processes | Use explicit handoff format |
| **Full Transfer** | Dumping entire process output into next | Pass specific, relevant findings only |
| **No Backflow** | Never updating previous process with new findings | Maintain feedback loops |
| **Redundant Work** | Re-discovering what another process already found | Check previous process outputs first |

---

## Output Format Standards

### Per-Process Outputs

Each process should produce output in its defined format (see individual process documents). When integrating, use this wrapper:

```
## Analysis: [Subject]

### Process: EXPLORE
[Explore findings — options, trade-offs, assumptions]

### Process: VERIFY
[Verify findings — correctness issues, conflicts, impossibilities]
Triggered by: [What from EXPLORE needed verification]

### Process: FEASIBILITY
[Feasibility findings — multi-axis profile, binding constraints, conditions]
Triggered by: [What from EXPLORE/VERIFY needed feasibility check]

### Process: RISK
[Risk findings — register, mitigations, monitoring]
Triggered by: [What from FEASIBILITY/VERIFY needed risk assessment]

### Cross-Process Findings
[Feedback loop findings — what one process revealed that changed another]

### Synthesis
[Integrated conclusion — recommendation with full awareness]
Decision: [Recommendation]
Confidence: [H/M/L with basis]
Conditions: [What must hold]
Monitoring: [What to watch]
Review: [When to reassess]
```

### Decision Documentation

For every decision supported by the framework:

```
DECISION RECORD

What: [Decision made]
Date: [When]
Processes Used: [Which, in what order]
Key Findings:
  EXPLORE: [Core insight]
  VERIFY: [Core insight]
  FEASIBILITY: [Core insight]
  RISK: [Core insight]
Alternatives Considered: [And why rejected]
Conditions: [What must remain true]
Review Trigger: [What would cause reassessment]
Owner: [Who is accountable]
```

---

## Theoretical Grounding Summary

The framework draws on theoretical foundations across all four processes:

### Impossibility & Limits
| Theorem | Process | Application |
|---------|---------|-------------|
| Halting Problem | VERIFY, FEASIBILITY | Undecidable = H5 impossible |
| Gödel's Incompleteness | VERIFY, FEASIBILITY | System can't fully assess itself |
| FLP | VERIFY, RISK | Async consensus limits |
| CAP | VERIFY, RISK, FEASIBILITY | Distributed system trade-offs |
| Arrow's Theorem | VERIFY | Voting system impossibility |
| No-Free-Lunch | VERIFY, RISK | No universal optimizer |
| NP-Completeness | FEASIBILITY | Computational feasibility limits |

### Systemic Principles
| Principle | Process | Application |
|-----------|---------|-------------|
| Normal Accidents (Perrow) | RISK | Complex + coupled = inevitable failure |
| Non-Ergodicity (Peters) | RISK | Irreversible risks need special treatment |
| Fat Tails (Taleb) | RISK | Impact often power-law distributed |
| Swiss Cheese (Reason) | RISK | Independent defense layers required |
| Theory of Constraints (Goldratt) | FEASIBILITY | Weakest dimension is binding |
| Requisite Variety (Ashby) | FEASIBILITY | Team variety must match problem variety |
| Conway's Law | FEASIBILITY | Org structure constrains architecture |
| Bounded Rationality (Simon) | FEASIBILITY, META | We satisfice, not optimize |

### Cognitive Biases
| Bias | Process | Countermeasure |
|------|---------|---------------|
| Planning Fallacy | FEASIBILITY | Reference Class Forecasting |
| Optimism Bias | RISK, FEASIBILITY | Base rates, Hofstadter correction |
| Dunning-Kruger | FEASIBILITY | Expertise-confidence mapping |
| Groupthink | EXPLORE, META | Devil's Advocate, anonymous scoring |
| Survivorship Bias | RISK | Historical pattern correction |
| Anchoring | ALL | Independent re-estimation |
| Confirmation Bias | VERIFY | Contraposition, constructive counterexample |
| Goodhart's Law | RISK, META | Metric gaming detection |

### Paradoxes
| Paradox | Process | Application |
|---------|---------|-------------|
| Cobra Effect | RISK | Mitigation creates worse risk |
| Braess Paradox | RISK | Adding capacity worsens performance |
| Simpson's Paradox | RISK | Aggregate hides subgroup problems |
| Sorites Paradox | RISK | Gradual accumulation below threshold |
| Ship of Theseus | FEASIBILITY | Incremental migration = new system |
| Jevons Paradox | FEASIBILITY | Efficiency → increased demand |
| Zeno's Paradox | FEASIBILITY | Over-analysis paralysis |
| Buridan's Ass | EXPLORE | Equal options → decision paralysis |
| Moravec's Paradox | FEASIBILITY | Human-easy ≠ machine-easy |
| Icarus Paradox | FEASIBILITY, META | Success → overconfidence |
| Bonini's Paradox | FEASIBILITY | Perfect model = as complex as reality |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-02 | Initial tetrad integration |

## References

### Process Documents
- `DEEP-EXPLORE.md` — Decision space exploration (54 methods)
- `DEEP-VERIFY.md` — Logical/technical verification (14 methods)  
- `DEEP-RISK-v2.md` — Risk assessment (44 methods)
- `DEEP-FEASIBILITY.md` — Feasibility assessment (35 methods)

### Theoretical Sources
- Perrow, C. (1984). Normal Accidents
- Peters, O. (2019). The Ergodicity Problem in Economics
- Taleb, N.N. (2007). The Black Swan
- Goldratt, E. (1984). The Goal
- Ashby, W.R. (1956). Introduction to Cybernetics
- Brooks, F. (1975). The Mythical Man-Month
- Conway, M. (1968). How Do Committees Invent?
- Simon, H. (1955). A Behavioral Model of Rational Choice
- Kahneman, D. & Tversky, A. (1979). Prospect Theory
- Flyvbjerg, B. (2006). From Nobel Prize to Project Management
- Snowden, D. (2007). A Leader's Framework for Decision Making
- Meadows, D. (1999). Leverage Points
- Altshuller, G. (1984). Creativity as an Exact Science
- Reason, J. (1990). Human Error
- Knight, F. (1921). Risk, Uncertainty and Profit
- Boehm, B. (1986). A Spiral Model of Software Development
