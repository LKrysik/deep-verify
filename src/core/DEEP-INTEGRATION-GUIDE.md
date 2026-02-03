# Deep Analysis Framework — Integration Guide & SKILL.md

## Overview

The Deep Analysis Framework is a pentad of complementary reasoning processes:

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   EXPLORE ──→ VERIFY ──→ FEASIBILITY ──→ RISK                    │
│      ↑           │            │            │                     │
│      └───────────┴────────────┴────────────┘                     │
│                        │                                         │
│                        ▼                                         │
│                    SYNTHESIS                                     │
│              (integrates all outputs                             │
│               into coherent understanding)                       │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

| Process | Question | Deliverable | Methods |
|---------|----------|-------------|---------|
| **Deep-Explore** | What CAN we do? | Decision space map | 54 methods in 5 phases + META |
| **Deep-Verify** | Is this CORRECT? | Validation report | 14 methods in 5 categories |
| **Deep-Feasibility** | CAN we do it? | Feasibility profile | 35 methods in 5 phases + META |
| **Deep-Risk** | What can go WRONG? | Risk register + mitigations | 44 methods in 6 phases + META |
| **Deep-Synthesis** | What does it all MEAN? | Integrated understanding | 40 methods in 6 phases + META |

**Why a pentad, not sequential steps:**
These are not a linear pipeline. They form a graph with feedback loops. Feasibility may invalidate Explore options. Risk assessment may reveal that mitigation itself is infeasible. Verification may surface impossibilities that reframe the entire decision. Synthesis integrates findings from all processes into coherent understanding — and may reveal emergent insights that trigger re-analysis. The integration guide defines HOW to navigate this graph.

---

## System Prompt

```
<deep_analysis_framework>
You are an expert analytical agent equipped with five complementary reasoning processes. Use them systematically to provide thorough, rigorous analysis.

THE FIVE PROCESSES:

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

5. DEEP-SYNTHESIS: Integrates knowledge from multiple sources into coherent understanding. Use when diverse information needs combining, patterns need discovering across domains, or a unified framework needs building.
   Phases: SCOPE → ACQUIRE → DECOMPOSE → RELATE → INTEGRATE → CRYSTALLIZE
   Key strength: Cross-domain pattern discovery, contradiction resolution, emergent insight generation, knowledge compression
   Key methods: Dialectical Integration, Analogical Structure Mapping, Conceptual Blending, Emergence Detection, Abductive Integration

ROUTING LOGIC — Which process to invoke:

PRIMARY SIGNAL → PROCESS:
- "What should we do?" / "What are our options?" / Decision needed → EXPLORE
- "Is this correct?" / "Does this work?" / Validate claims → VERIFY
- "Can we do this?" / "Is this achievable?" / Go/No-Go → FEASIBILITY
- "What could go wrong?" / "How risky is this?" / Threat assessment → RISK
- "What does this all mean?" / "How do these pieces fit together?" / Integration → SYNTHESIS

COMPOUND SIGNALS → SEQUENCE:
- "Should we do X?" → EXPLORE (options) → VERIFY (correctness) → FEASIBILITY (can we?) → RISK (what if?) → SYNTHESIS (integrate all findings)
- "Review this architecture" → VERIFY (correctness) → FEASIBILITY (scalability, resources) → RISK (failure modes)
- "We're deciding between A and B" → EXPLORE (illuminate both) → VERIFY (both valid?) → FEASIBILITY (both achievable?) → RISK (compare risk profiles) → SYNTHESIS (unified recommendation)
- "Is this plan realistic?" → FEASIBILITY (primary) → RISK (what threatens it?)
- "Debug this design" → VERIFY (primary) → RISK (what we missed)
- "What have we learned from these projects?" → SYNTHESIS (primary) → EXPLORE (what new options emerge?)
- "How do these reports/findings fit together?" → SYNTHESIS (primary)
- "Make sense of this research" → SYNTHESIS (primary) → VERIFY (are findings valid?)

SCALING — How deep to go:

| Complexity | Approach | Time |
|-----------|---------|------|
| Simple question | Single process, core methods only | Minutes |
| Standard decision | 1-2 processes, standard depth | Hours |
| Major decision | Full pentad, comprehensive | Days |
| Critical/irreversible | Full pentad + META + validation | Week+ |

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
- SYNTHESIS discovers emergent pattern → VERIFY must check if pattern is valid, RISK must assess new threats
- ALL processes complete → SYNTHESIS integrates into unified understanding
- SYNTHESIS reveals contradiction → VERIFY resolves, EXPLORE generates alternatives

FEEDBACK LOOPS:

Always check for these circular dependencies:
- Risk mitigation needs its own feasibility assessment
- Feasibility conditions create new risks to monitor
- Verification findings may invalidate explored options
- Exploration of alternatives may introduce new verification needs
- Synthesis findings may trigger re-exploration, re-verification, or re-assessment
- Synthesis of risk + feasibility may reveal compound concerns invisible to either alone

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
- Have I SYNTHESIZED findings or just listed them? (Collection ≠ synthesis)

IMPORTANT CONSTRAINTS:
- Never skip VERIFY for technical claims — optimism kills projects
- Never skip FEASIBILITY for plans — planning fallacy is universal
- Never skip RISK for irreversible decisions — non-ergodic risks can end the game
- Never skip SYNTHESIS when multiple processes have been run — unintegrated findings miss emergent insights
- Always apply META methods when stakes are high
- For Complex (Cynefin) problems: probe, don't analyze
- After 3+ processes complete: consider CPCPA to find mega-critical points

CROSS-PROCESS CRITICAL PATH ANALYSIS (CPCPA):
An integrative method (not a sixth process) that identifies MEGA-CRITICAL POINTS where multiple dimensions of criticality converge on the same element.

Six dimensions of criticality:
- Temporal: What determines minimum time? (from FEASIBILITY)
- Reliability: What failure cascades? (from RISK)
- Value: What creates/destroys value? (from EXPLORE + SYNTHESIS)
- Resource: What constrains throughput? (from FEASIBILITY)
- Decision: Which choice determines others? (from EXPLORE)
- Information: What knowledge gap blocks progress? (from SYNTHESIS)

Run CPCPA when:
- At least 3 processes have completed
- You need to prioritize where to focus attention
- You suspect hidden dependencies across process findings
- You need to identify what MUST NOT FAIL

A mega-critical point (3+ dimensions) requires disproportionate attention: protection, redundancy, monitoring, and contingency planning.
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
│   │       └── If multiple processes run → + SYNTHESIS (integrate)
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
│   ├── "What does this mean?" / "How do these fit together?" / Integration
│   │   └── → SYNTHESIS (primary)
│   │       └── If emergent pattern found → VERIFY (is pattern valid?)
│   │       └── If contradiction found → EXPLORE (new options) or VERIFY (resolve)
│   │       └── If actionable insight → FEASIBILITY + RISK (assess)
│   │
│   └── Compound / "Should we...?" / Full analysis
│       └── → FULL PENTAD (sequence below)
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
│   │   └── Full pentad, comprehensive
│   │
│   └── Critical (irreversible, existential)
│       └── Full pentad + META + validation + stakeholder review
│
└── What DOMAIN is the problem? (Cynefin)
    │
    ├── Clear → Direct analysis, minimal process
    ├── Complicated → Expert-driven, full processes
    ├── Complex → PROBE first, then analyze, SYNTHESIZE learnings
    └── Chaotic → ACT first, then stabilize, then analyze
```

---

## Sequencing Patterns

### Pattern 1: Full Pentad (Comprehensive)

The default sequence for major decisions:

```
EXPLORE                    VERIFY                    FEASIBILITY               RISK                     
───────                    ──────                    ───────────               ────                     
1. MAP options         →   4. Check correctness  →   7. Assess feasibility →  10. Identify risks       
2. ILLUMINATE effects      5. Find conflicts         8. Validate critical      11. Quantify severity    
3. CHALLENGE assumptions   6. Test impossibilities    9. Decide Go/No-Go       12. Design mitigations   
                                                                               13. Build monitoring     
                                                         │
                                                         ▼
                                                      CPCPA (after 3+ processes)
                                                         │
                                                         ▼
                                                     SYNTHESIS
                                                     ─────────
                                                     14. Integrate all
                                                     15. Find emergence
                                                     16. Build framework
                                                     17. Distill principles

Feedback loops:
- Step 6 (impossibility) → Step 1 (new options)
- Step 9 (infeasible) → Step 1 (reframe) or Step 3 (new constraints)
- Step 12 (mitigation) → Step 8 (is mitigation feasible?)
- Step 10 (risks) → Step 7 (risks change feasibility)
- CPCPA (mega-critical point) → disproportionate attention, may trigger re-analysis
- Step 15 (emergence) → Step 4 (verify emergent pattern) or Step 1 (new options from insight)
- Step 16 (framework) → may reveal gaps requiring more EXPLORE or VERIFY
```

### Pattern 2: Validate-First (Technical Review)

For reviewing existing designs, architectures, or plans:

```
VERIFY → FEASIBILITY → RISK → (EXPLORE if issues found) → SYNTHESIS (if multiple processes ran)
```

Start by checking correctness. If correct, assess feasibility. If feasible, assess risks. Only explore alternatives if issues found. Synthesize if significant findings from multiple processes.

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

### Pattern 5: Synthesis-First (Knowledge Building)

For research integration, learning from experience, or domain understanding:

```
SYNTHESIS (primary) → VERIFY (are findings valid?) → EXPLORE (what options emerge?) → FEASIBILITY/RISK (assess emerging options)
```

Start by integrating knowledge, then validate insights, then explore implications.

### Pattern 6: Post-Mortem / Retrospective

For learning from experience across multiple events:

```
SYNTHESIS (integrate incidents/experiences) → RISK (update risk model) → FEASIBILITY (assess preventive measures) → EXPLORE (new approaches)
```

### Pattern 7: Iterative Deepening

For evolving understanding:

```
Round 1: EXPLORE (quick) → VERIFY (quick) → FEASIBILITY (quick) → RISK (quick)
Round 2: SYNTHESIS (integrate Round 1 findings) → identify biggest concern
Round 3: Deep dive into the process that addresses the biggest concern
Round 4: SYNTHESIS (re-integrate with new depth)
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
| All risk findings | SYNTHESIS | Source material for integrated understanding |

**SYNTHESIS produces → consumed by:**

| Output | Consumer | How It's Used |
|--------|----------|---------------|
| Emergent patterns (#403) | VERIFY | Validate emergent insight is real, not apophenia |
| Emergent patterns (#403) | RISK | New risk sources from cross-domain patterns |
| Framework unification (#402) | EXPLORE | Reframe decision space using unified model |
| Core insights (#501) | FEASIBILITY | New constraints or enablers discovered |
| Contradictions unresolved (#407) | VERIFY | Logical resolution needed |
| Contradictions unresolved (#407) | EXPLORE | Generate options to resolve |
| Boundary conditions (#406) | RISK | Monitor for boundary violations |
| Principles (#503) | ALL | General principles inform all processes |
| Knowledge gaps (#206) | EXPLORE | Gaps suggest where to investigate |
| Analogical transfers (#303) | EXPLORE | Cross-domain solutions to import |
| Actionable conclusions (#505) | FEASIBILITY + RISK | Assess feasibility and risks of recommended actions |

**ALL processes produce → consumed by SYNTHESIS:**

| Output | From | Synthesis Use |
|--------|------|---------------|
| Options + trade-offs | EXPLORE | Source material for integration |
| Correctness findings | VERIFY | Evidence base with validation status |
| Feasibility profile | FEASIBILITY | Constraint landscape |
| Risk register | RISK | Threat landscape |
| All META findings | ALL | Bias and quality context for synthesis |

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

### Loop 6: Synthesis-Triggered Re-Analysis

```
SYNTHESIS discovers emergent pattern across process outputs
    │
    ├── TRIGGER: VERIFY — is the pattern valid?
    │   └── If valid → RISK: does pattern reveal new threats?
    │   └── If invalid → SYNTHESIS re-integrates without false pattern
    │
    ├── TRIGGER: EXPLORE — does pattern suggest new options?
    │   └── New options → VERIFY → FEASIBILITY → RISK → back to SYNTHESIS
    │
    └── TRIGGER: FEASIBILITY — does pattern change feasibility assessment?
        └── Re-assess affected dimensions
```

### Loop 7: Synthesis Contradiction Resolution

```
SYNTHESIS finds unresolved contradiction between process outputs
(e.g., FEASIBILITY says "yes" but RISK says "unacceptable")
    │
    ├── TRIGGER: VERIFY — is the contradiction real or apparent?
    │   └── Apparent → Different scopes or levels → acknowledge, don't force resolution
    │   └── Real → Must resolve:
    │       ├── EXPLORE: are there options that satisfy both?
    │       └── FEASIBILITY: can we change constraints to resolve?
    │
    └── If irresolvable → SYNTHESIS documents as productive tension
        with explicit decision criteria for when to favor each side
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
| "How do these reports fit together?" | SYNTHESIS only | Pure knowledge integration |
| "What patterns do you see across these?" | SYNTHESIS only | Pattern discovery from existing material |

### When to Combine (Most Cases)

| Signal | Sequence | Why This Order |
|--------|----------|---------------|
| "Should we use Kafka or Pulsar?" | EXPLORE → VERIFY → FEASIBILITY → RISK → SYNTHESIS | Need full picture, then integrate for decision |
| "Review this architecture" | VERIFY → FEASIBILITY → RISK | Already designed, need validation |
| "Can we migrate to Unity Catalog?" | FEASIBILITY → RISK | Option known, need Go/No-Go |
| "We're getting errors in pipeline" | VERIFY (find bug) → RISK (what else is affected?) | Debug first, then assess blast radius |
| "Plan our Q3 OKRs" | EXPLORE → FEASIBILITY | Generate goals, then reality-check |
| "This proposal seems too good" | VERIFY → FEASIBILITY → RISK | Suspicion = check correctness first |
| "What did we learn from last 3 projects?" | SYNTHESIS (primary) → RISK (emerging patterns) | Learning = synthesis, then apply |
| "Make sense of this vendor evaluation" | SYNTHESIS → VERIFY → FEASIBILITY | Integrate first, verify key claims, assess executability |
| "How should we think about this domain?" | SYNTHESIS → EXPLORE | Build understanding, then generate options from it |

### When to Use META

| Signal | Action |
|--------|--------|
| Analysis feels "too clean" | Apply Cognitive Bias Audit, Confidence Theater Detection |
| Team quickly agrees | Apply Groupthink check, Devil's Advocate |
| Estimate seems aggressive | Apply Planning Fallacy Detection, Hofstadter Correction |
| All scores are similar | Apply Simpson's Paradox Audit |
| Dashboard all green | Apply Goodhart's Law Check |
| High stakes, irreversible | Apply ALL META methods from every process |
| 3+ processes completed | Run CPCPA to identify mega-critical points |
| Unclear where to focus | Run CPCPA to find convergent criticalities |

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

### Synergy 6: Knowledge-to-Action Chain
```
SYNTHESIS #301 (Convergence-Divergence Mapping)
    → SYNTHESIS #302 (Dialectical Tension Mapping)
        → SYNTHESIS #401 (Dialectical Integration)
            → EXPLORE (new options from resolved tensions)
                → VERIFY + FEASIBILITY + RISK (assess new options)
```
Map disagreements → identify productive tensions → resolve into higher understanding → generate new options → validate.

### Synergy 7: Learning Loop
```
RISK #504 (Post-Incident Feedback)
    → SYNTHESIS #306 (Pattern Detection Across Sources)
        → SYNTHESIS #503 (Principle Extraction)
            → ALL processes (principles inform future analysis)
```
Learn from incidents → find patterns across incidents → extract general principles → apply to future work.

### Synergy 8: Research-to-Decision Pipeline
```
SYNTHESIS (full cycle on research/domain knowledge)
    → SYNTHESIS #505 (Actionability Assessment)
        → EXPLORE (options from synthesized understanding)
            → FEASIBILITY + RISK (assess options)
                → SYNTHESIS (integrate process outputs into final recommendation)
```
Build domain understanding → identify actionable implications → generate options → assess → synthesize into recommendation.

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

## Cross-Process Critical Path Analysis (CPCPA)

*An integrative method that identifies what is CRITICAL across all five processes. Not a sixth process, but a lens that synthesizes findings from the pentad to reveal mega-critical points.*

### The Problem CPCPA Solves

Each process identifies its own "critical" elements:
- EXPLORE finds critical decisions and dependencies
- VERIFY finds critical correctness concerns
- FEASIBILITY finds binding constraints and critical path (temporal)
- RISK finds critical risks and SPOFs
- SYNTHESIS finds critical patterns and insights

**But no single process answers:** "What is critical ACROSS ALL DIMENSIONS simultaneously?"

A component might be:
- On the temporal critical path (delay here = project delay)
- A single point of failure (failure here = system failure)
- A binding constraint (this limits everything else)
- A critical decision point (this choice determines downstream options)
- A critical knowledge gap (we don't understand this well enough)

When multiple criticalities **converge on the same element** → that's a **mega-critical point** requiring disproportionate attention.

### Six Dimensions of Criticality

| Dimension | Question | Source Process | Detection Method |
|-----------|----------|----------------|------------------|
| **Temporal** | What determines minimum time? | FEASIBILITY #205 | Critical Path Method (CPM), longest dependency chain |
| **Reliability** | What failure would cascade/paralyze? | RISK #306 | Min-cut analysis, SPOF detection |
| **Value** | What creates/destroys the most value? | EXPLORE + SYNTHESIS | Value stream mapping, impact analysis |
| **Resource** | What constrains throughput? | FEASIBILITY #102, #202 | Theory of Constraints, bottleneck identification |
| **Decision** | Which decision determines others? | EXPLORE | Dependency analysis, option trees |
| **Information** | What knowledge gap blocks progress? | FEASIBILITY #203, SYNTHESIS #206 | Knowledge dependency mapping |

### CPCPA Method

#### Step 1: Collect Criticality Data from Each Process

| From Process | Extract | Format |
|--------------|---------|--------|
| **EXPLORE** | Critical decisions (gates that determine downstream) | `decisions[] → {decision, downstream_impact, reversibility}` |
| **EXPLORE** | Key dependencies between options | `dependencies[] → {from, to, strength}` |
| **VERIFY** | Critical correctness concerns | `concerns[] → {claim, if_wrong_impact, confidence}` |
| **FEASIBILITY** | Binding constraint | `binding_constraint → {dimension, element, score}` |
| **FEASIBILITY** | Critical path (temporal) | `critical_path[] → {task, duration, float}` |
| **FEASIBILITY** | Resource bottlenecks | `bottlenecks[] → {resource, utilization, queue_depth}` |
| **RISK** | High-severity risks | `critical_risks[] → {risk, composite_score, non_ergodic}` |
| **RISK** | Min-cut elements | `spofs[] → {element, cut_size, blast_radius}` |
| **RISK** | Cascade root risks | `cascade_roots[] → {risk, downstream_count}` |
| **SYNTHESIS** | Critical knowledge gaps | `gaps[] → {gap, impact_on_synthesis, addressable}` |
| **SYNTHESIS** | Unresolved contradictions | `contradictions[] → {tension, impact, resolution_status}` |

#### Step 2: Map Elements to Criticality Dimensions

Create a matrix: Elements × Dimensions

```
                    Temporal  Reliability  Value  Resource  Decision  Information
                    ────────  ───────────  ─────  ────────  ────────  ───────────
Delta merge logic      ●          ●          ●                           ●
EPR calculation        ●          ●          ●                 ●
Senior engineer                   ●                   ●                  ●
Mars data format       ●                     ●                 ●         ●
Databricks cluster               ●                   ●
Q2 deadline            ●                     ●                 ●

● = element is critical in this dimension
```

#### Step 3: Identify Mega-Critical Points

**Mega-critical point:** Element with criticality in 3+ dimensions

Rank by: `criticality_score = count(dimensions) × max(severity_in_any_dimension)`

```
MEGA-CRITICAL POINTS (3+ dimensions):

1. EPR calculation logic — 4 dimensions (Temporal, Reliability, Value, Decision)
   ├── On temporal critical path (delay = missed regulatory deadline)
   ├── SPOF in reliability (bug = wrong filing = regulatory penalty)
   ├── Core value delivery (the whole point of the project)
   └── Decision gate (approach choice affects all downstream)
   → REQUIRES: Disproportionate testing, review, documentation, backup plan

2. Mars data format — 4 dimensions (Temporal, Value, Decision, Information)
   ├── On critical path (waiting for spec = project delay)
   ├── Value dependency (wrong format = rework)
   ├── Decision dependency (format determines architecture choices)
   └── Knowledge gap (we don't fully understand their data model)
   → REQUIRES: Immediate clarification, format validation spike, assumption documentation

3. Senior engineer — 3 dimensions (Reliability, Resource, Information)
   ├── Key person SPOF (if unavailable, no one else knows the system)
   ├── Resource bottleneck (100% utilized, queue forming)
   └── Knowledge concentration (tacit knowledge not documented)
   → REQUIRES: Knowledge transfer, documentation sprint, backup person identification
```

#### Step 4: Validate Criticality

Not everything that LOOKS critical IS critical. Validate:

| Validation Method | What It Tests | From Process |
|-------------------|---------------|--------------|
| **Float analysis** | Is temporal criticality real? (zero float = truly critical) | FEASIBILITY |
| **Chaos probe** | Is reliability criticality real? (does failure actually cascade?) | RISK #110 |
| **Sensitivity analysis** | Is value criticality real? (does change here change outcome?) | FEASIBILITY #207, SYNTHESIS |
| **Utilization measurement** | Is resource criticality real? (is it actually the bottleneck?) | FEASIBILITY |
| **Decision tree pruning** | Is decision criticality real? (do alternatives exist?) | EXPLORE |
| **Knowledge test** | Is information criticality real? (can we proceed without it?) | SYNTHESIS |

**False criticality** is dangerous — it wastes attention on non-bottlenecks while real bottlenecks are ignored.

#### Step 5: Respond to Mega-Critical Points

| Response Type | When | Actions |
|---------------|------|---------|
| **Protect** | Cannot eliminate criticality | Redundancy, buffers, monitoring, documentation |
| **Reduce** | Can add parallel paths | Parallelize, add alternatives, decouple |
| **Transfer** | Can shift criticality elsewhere | Redesign to move critical path, outsource |
| **Accept** | Low severity despite criticality | Document, monitor, have contingency |

For each mega-critical point, define:
1. **Primary response** — how to address the criticality
2. **Contingency** — what if the critical element fails anyway?
3. **Monitoring** — how will we know if criticality is shifting?

### Criticality Shift Detection

Critical paths are not static. They shift when:
- A task completes faster/slower than planned → new temporal critical path
- A risk materializes → new reliability critical point
- Requirements change → new value critical elements
- Team changes → new resource bottleneck
- Decision is made → new decision tree active

**Monitoring protocol:**
1. After each major milestone: re-run CPCPA Step 2-3
2. After any process output changes significantly: check if mega-critical points changed
3. Weekly (for active projects): quick criticality pulse check

### Integration with Pentad Workflow

CPCPA runs AFTER at least 3 processes have completed (minimum data for meaningful cross-process analysis):

```
EXPLORE → VERIFY → FEASIBILITY → RISK
                       │
                       ▼
                    CPCPA ←───── Can run here (enough data)
                       │
                       ▼
                  SYNTHESIS ←─── CPCPA findings feed into synthesis
                       │
                       ▼
                    CPCPA ←───── Re-run after synthesis (may reveal new criticalities)
```

CPCPA output feeds into:
- **SYNTHESIS** — mega-critical points are key elements for integration
- **RISK** — mega-critical points need monitoring design
- **FEASIBILITY** — if mega-critical point is infeasible, project is infeasible

### CPCPA Output Template

```
CROSS-PROCESS CRITICAL PATH ANALYSIS

Date: [When]
Processes included: [Which processes contributed data]

CRITICALITY MATRIX:
[Element × Dimension matrix with ● marks]

MEGA-CRITICAL POINTS (3+ dimensions):

1. [Element]
   Dimensions: [List]
   Why critical in each: [Brief explanation per dimension]
   Validation: [How confirmed]
   Response: [Primary response]
   Contingency: [If element fails]
   Monitoring: [How to detect shift]

2. [Element]
   ...

CRITICALITY SHIFTS TO WATCH:
- [What could shift the critical path]
- [Early indicators of shift]

NEXT CPCPA: [When to re-run]
```

### Theoretical Grounding

| Principle | Application in CPCPA |
|-----------|---------------------|
| **Theory of Constraints (Goldratt)** | System limited by ONE constraint. But which dimension's constraint is binding? CPCPA finds where constraints COMPOUND. |
| **Min-Cut/Max-Flow (Ford-Fulkerson)** | Reliability critical path is the min-cut. CPCPA extends to multi-dimensional cuts. |
| **Little's Law (L = λW)** | Queues reveal bottlenecks. CPCPA looks for queues across all dimensions — decisions waiting, knowledge waiting, not just tasks waiting. |
| **Drum-Buffer-Rope (Goldratt)** | Protect the constraint with buffers. CPCPA identifies WHICH constraint to protect when multiple exist. |
| **Value Stream Mapping (Lean)** | Map value flow, find waste. CPCPA extends to decision flow, knowledge flow, not just material/work flow. |
| **DSM (Steward)** | Dependency Structure Matrix reveals coupling. CPCPA uses multi-dimensional DSM. |

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
| **Collection Without Synthesis** | Running 4 processes, listing findings, never integrating | After multiple processes, ALWAYS synthesize — list ≠ understanding |
| **Premature Synthesis** | Synthesizing before adequate analysis | Ensure at least decomposition before attempting integration |
| **Summary Disguised as Synthesis** | Summarizing sources without generating novel insight | Apply Shannon test: does output contain information NOT in any single source? |

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
- `DEEP-SYNTHESIS.md` — Knowledge synthesis (40 methods)

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
- Hegel, G.W.F. (1807). Phenomenology of Spirit
- Piaget, J. (1952). The Origins of Intelligence in Children
- Polanyi, M. (1966). The Tacit Dimension
- Shannon, C. (1948). A Mathematical Theory of Communication
- Gentner, D. (1983). Structure-Mapping: A Theoretical Framework for Analogy
- Fauconnier, G. & Turner, M. (2002). The Way We Think: Conceptual Blending
- Weick, K. (1995). Sensemaking in Organizations
- Peirce, C.S. (1903). Harvard Lectures on Pragmatism
- Kuhn, T. (1962). The Structure of Scientific Revolutions
- Lakatos, I. (1978). The Methodology of Scientific Research Programmes
- Feyerabend, P. (1975). Against Method
- Popper, K. (1934). The Logic of Scientific Discovery
- Glass, G. (1976). Primary, Secondary, and Meta-Analysis of Research
- Glaser, B. & Strauss, A. (1967). The Discovery of Grounded Theory
- Nonaka, I. & Takeuchi, H. (1995). The Knowledge-Creating Company
- Anderson, L.W. & Krathwohl, D.R. (2001). A Taxonomy for Learning, Teaching, and Assessing
- Ford, L.R. & Fulkerson, D.R. (1956). Maximal Flow Through a Network
- Little, J. (1961). A Proof for the Queuing Formula: L = λW
- Steward, D.V. (1981). The Design Structure System
- Ohno, T. (1988). Toyota Production System: Beyond Large-Scale Production
- Womack, J. & Jones, D. (1996). Lean Thinking
