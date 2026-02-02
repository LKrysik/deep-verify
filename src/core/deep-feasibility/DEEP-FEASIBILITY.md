# Deep-Feasibility: Systematic Feasibility Assessment Methodology

## Overview

Deep-Feasibility is the fourth pillar of a complementary tetrad:

| Process | Question | Nature | Error Type |
|---------|----------|--------|------------|
| **Deep-Explore** | *What can we do?* | Divergent — maps decision space | Missing options |
| **Deep-Verify** | *Is this correct?* | Convergent — validates logical/technical correctness | False validity |
| **Deep-Risk** | *What can go wrong?* | Probabilistic — assesses threats and responses | Underestimated danger |
| **Deep-Feasibility** | *Can we actually do this?* | Evaluative — assesses executability across dimensions | **False feasibility** |

**False feasibility** is Deep-Feasibility's unique error type: believing something is executable when it is not. This is distinct from incorrectness (Verify), risk (Risk), or missing options (Explore). A plan can be logically correct, have manageable risks, and still be **completely infeasible** because the team lacks the skill, time, organizational structure, or technological maturity to execute it.

---

## Theoretical Foundations

### Computability & Complexity — The Hardest Limits

**1. Turing / Halting Problem (1936)**
Some problems are **provably undecidable** — no algorithm can solve them regardless of resources. This is the absolute ceiling of infeasibility. Not a matter of effort — a matter of mathematical impossibility.

**2. Cook-Karp / NP-Completeness (1971)**
Even decidable problems may be practically infeasible. The feasibility spectrum:

| Class | Feasibility | Implication |
|-------|------------|-------------|
| **P** | Feasible at scale | Polynomial — do it |
| **NP** | Verify feasible, solve maybe not | May need approximation |
| **NP-hard** | Infeasible at scale (exact) | Approximate, decompose, or accept heuristic |
| **PSPACE/EXPTIME** | Theoretical only | Redesign the problem |
| **Undecidable** | Impossible | Stop trying. Reframe. |

**Key insight:** Many real problems are NP-hard but have **good approximations**. Feasibility question is not "can we solve optimally?" but "can we solve WELL ENOUGH?"

**3. Gödel's Incompleteness (1931)**
In any sufficiently rich system, there exist true statements that cannot be proven within the system. Implication: a system cannot fully assess its OWN feasibility. External perspective is required — one reason Reference Class Forecasting (#302) uses EXTERNAL data.

### Resource & Constraint Theory

**4. Goldratt — Theory of Constraints (1984)**
A system's throughput is determined by its single tightest constraint (bottleneck). Optimizing anything OTHER than the bottleneck is waste. Implication: feasibility depends on identifying the TRUE constraint, not on general resource analysis. A project with 10 adequate resources and 1 missing resource is infeasible.

**5. Ashby — Law of Requisite Variety (1956)**
A controller must have AT LEAST as many response varieties as the system it controls. If problem has N dimensions of complexity and your team/tools cover M < N, control is **fundamentally impossible**. Not hard — impossible. Implication: feasibility requires matching team variety to problem variety.

**6. Brooks — Mythical Man-Month (1975)**
- **Brooks's Law:** Adding people to a late project makes it later. Team capacity is NOT linearly scalable — communication overhead grows as n(n-1)/2.
- **No Silver Bullet:** No single technique provides order-of-magnitude improvement. Essential complexity cannot be reduced, only accidental complexity.
- **Second System Effect:** V2 is over-engineered because "now we know what we're doing" — leading to false feasibility confidence.

**7. Conway's Law (1968)**
Organizations produce systems that mirror their communication structures. If required architecture demands cross-team integration that doesn't exist in org structure, that architecture is **structurally infeasible** regardless of individual competence.

### Estimation & Decision Theory

**8. Simon — Bounded Rationality (1955)**
Humans don't optimize — they satisfice (find "good enough"). Feasibility assessment itself is bounded: we cannot evaluate ALL paths. Heuristics for when to stop investigating are essential.

**9. Kahneman & Tversky — Planning Fallacy (1979)**
Systematic underestimation of time, cost, and difficulty; overestimation of benefits. NOT random error — directional bias. Empirical data: 86% of projects exceed budget, 80% exceed timeline (Flyvbjerg). Every self-generated feasibility estimate is systematically optimistic.

**10. Flyvbjerg — Reference Class Forecasting (2006)**
The only proven antidote to planning fallacy: use EXTERNAL base rates from similar projects instead of internal "inside view" analysis. Inside view ("our project is special") is systematically worse than outside view ("what happens to projects like this").

**11. Hofstadter's Law**
"It always takes longer than you expect, even when you take into account Hofstadter's Law." The recursive nature of estimation error — awareness of bias does not eliminate it.

### Systems Theory

**12. Snowden — Cynefin Framework (2007)**
Feasibility assessment method DEPENDS on problem type:

| Domain | Cause→Effect | Feasibility Approach |
|--------|-------------|---------------------|
| **Clear** | Obvious | Direct constraint check — straightforward |
| **Complicated** | Requires expertise | Expert analysis — feasible with right knowledge |
| **Complex** | Emergent, retrospective only | **Traditional feasibility is impossible.** Must probe. |
| **Chaotic** | No perceivable relationship | Act first to create stability, assess later |

For Complex problems, feasibility assessment in advance is a **category error**. You can only learn feasibility by doing small experiments.

**13. Meadows — Leverage Points (1999)**
Not all interventions are equally feasible. 12 levels from parameters (easy to change, small effect) to paradigms (hard to change, transformational). Feasibility of change depends on which level you're targeting.

**14. Altshuller — TRIZ (1946-1985)**
Inventive Problem Solving Theory. Two types of contradictions:
- **Technical contradiction:** Improving X worsens Y (e.g., stronger but heavier)
- **Physical contradiction:** Element must have property A AND not-A simultaneously (e.g., hot and cold)

40 inventive principles for resolving contradictions. Implication: feasibility analysis should search for CONTRADICTIONS in requirements, not just missing resources. Unresolved contradiction = infeasibility OR innovation opportunity.

### Engineering Frameworks

**15. NASA — Technology Readiness Levels (TRL)**

| TRL | Description | Feasibility Status |
|-----|-------------|-------------------|
| 1 | Basic principles observed | Theoretical only |
| 2 | Technology concept formulated | Concept only |
| 3 | Proof of concept | Lab validation |
| 4 | Component validated in lab | Component works |
| 5 | Component validated in relevant environment | Moving toward real |
| 6 | System demonstrated in relevant environment | Prototype works |
| 7 | System prototype in operational environment | Near-production |
| 8 | System complete and qualified | Ready |
| 9 | System proven in operations | Proven |

System feasibility is limited by its LOWEST TRL component. A system with nine TRL-9 components and one TRL-2 component has an effective TRL of 2.

**16. Boehm — Spiral Model (1986)**
Iterative feasibility reassessment — each cycle re-evaluates feasibility with new information. Feasibility is not a one-time gate but a continuous signal that degrades and improves over the project lifecycle.

### Paradoxes of Feasibility

| Paradox | Mechanism | Implication |
|---------|-----------|-------------|
| **Zeno** | Infinite decomposition | Over-analysis: if every step requires sub-analysis, assessment never completes |
| **Ship of Theseus** | Incremental change | Each migration step "feasible" but total migration creates entirely new system |
| **Sorites** | Gradual accumulation | Each added requirement "feasible" but scope total is infeasible |
| **Icarus** | Success → overconfidence | Past feasibility success → overestimate future feasibility |
| **Jevons** | Efficiency → increased demand | Making something feasible → everyone uses it → new bottleneck |
| **Observer** | Assessment consumes resources | Feasibility study itself costs time/money that affects feasibility |
| **Buridan's Ass** | Equal options → paralysis | Multiple feasible paths → decision paralysis delays all paths |
| **Moravec** | Human-easy ≠ machine-easy | Feasibility intuition fails for automated systems |
| **Bonini** | Model as complex as reality | Perfect feasibility model is as hard to build as the actual system |

---

## Philosophy

### Core Principles

1. **Feasibility is multi-dimensional.** A project feasible on 9 of 10 axes but infeasible on 1 is INFEASIBLE. The weakest dimension is the binding constraint (Goldratt).

2. **Feasibility is not binary.** It's a spectrum: Impossible → Infeasible → Difficult → Achievable → Easy. And: Unconditional → Conditional (feasible IF...) → Aspirational (feasible only under ideal conditions).

3. **Self-assessed feasibility is systematically optimistic.** Planning fallacy is not a bug — it's a feature of human cognition. Every internal estimate requires external calibration.

4. **Feasibility decays and grows.** It's not static. Team changes, market shifts, technology evolution, scope creep — all change feasibility over time. Assessment must be repeated.

5. **The feasibility of assessing feasibility varies.** For Complex-domain problems (Cynefin), traditional assessment is impossible — you must probe. Knowing WHEN you can't assess is as important as assessing.

6. **Component feasibility ≠ system feasibility.** Every part can be individually feasible while the whole is infeasible (compositional gap). Integration complexity is where feasibility estimates most often fail.

7. **Feasibility constraints can be creative opportunities.** TRIZ shows that contradictions (apparent infeasibilities) are often the source of breakthrough innovations when resolved creatively.

---

## Phases

```
FRAME → CONSTRAIN → ASSESS → VALIDATE → DECIDE
           ↑                               |
           └────── META (continuous) ──────┘
```

| Phase | Goal | Methods | Key Output |
|-------|------|---------|------------|
| **FRAME** | Classify problem type, define scope of assessment | 001–003 | Problem characterization, assessment strategy |
| **CONSTRAIN** | Identify hard vs soft limits, contradictions, structural blocks | 101–106 | Constraint map, impossibility flags |
| **ASSESS** | Evaluate feasibility across 10 dimensions | 201–210 | Multi-axis feasibility profile |
| **VALIDATE** | Empirically test critical assumptions and estimates | 301–306 | Calibrated estimates, probe results |
| **DECIDE** | Synthesize into Go/No-Go/Conditional with confidence | 401–404 | Decision with conditions and monitoring |
| **META** | Detect bias in the assessment process itself | 501–505 | Bias audit, corrected estimates |

---

## Phase 0: FRAME

*Goal: Before assessing feasibility, understand WHAT TYPE of problem this is — because the type determines whether traditional feasibility assessment is even possible.*

---

### 001 — Cynefin Domain Classification

**What:** Classify the problem/project into the Cynefin framework to determine the APPROPRIATE feasibility assessment method. For Complex problems, traditional feasibility assessment is a category error.

**Process:**
1. Assess cause-and-effect relationship:
   - **Clear:** Cause→effect obvious to everyone → assess directly via constraint checking
   - **Complicated:** Cause→effect requires expertise → assess via expert analysis
   - **Complex:** Cause→effect only visible in retrospect → **cannot assess traditionally, must probe (#303)**
   - **Chaotic:** No perceivable cause→effect → act first, assess later
2. Most real projects are MIXED — decompose into sub-problems, each may be in a different domain
3. For each sub-problem in Complex domain: flag that standard feasibility methods will fail, design probes instead
4. **Critical red flag:** Treating Complex as Complicated (applying expert analysis to emergent problems) — this produces confident but wrong feasibility assessments

**Why this comes first:** If you skip this and the problem is Complex, ALL subsequent feasibility analysis produces false confidence. Better to know "we can't assess this traditionally" than to produce a detailed-but-wrong assessment.

**Output:** `domain_map → {sub_problem, cynefin_domain, assessment_approach, probe_needed_flag}`

---

### 002 — Feasibility Question Decomposition

**What:** Break the monolithic "is this feasible?" into atomic, independently assessable sub-questions. "Can we build this system?" is unanswerable. "Can we build the authentication module with current team skills?" is assessable.

**Process:**
1. Start with the top-level feasibility question
2. Decompose along natural fault lines:
   - By component/module
   - By phase (design, build, test, deploy, operate)
   - By dimension (technical, resource, time, organization)
   - By risk (what's the most uncertain part?)
3. For each sub-question: is it assessable NOW or does it require investigation?
4. Identify DEPENDENCIES between sub-questions (B's feasibility depends on A's outcome)
5. **Stop decomposing when:** sub-questions are either directly assessable or clearly need a probe (#303). Zeno's paradox warning: infinite decomposition is itself infeasible.

**Output:** `sub_questions[] → {question, assessable_now, needs_investigation, depends_on, cynefin_domain}`

---

### 003 — Feasibility Scope Definition

**What:** Explicitly define WHAT is being assessed for feasibility and WHAT IS NOT. Scope creep in feasibility assessment is as real as scope creep in projects — and equally dangerous.

**Process:**
1. Define the SUBJECT: What exactly are we assessing? (The whole project? A specific component? A decision? A migration?)
2. Define the HORIZON: Feasibility by when? (Next sprint? Next quarter? Next year?)
3. Define the STANDARD: Feasible means what? (Working prototype? Production-ready? Scaled to 10× current load?)
4. Define EXCLUSIONS: What are we NOT assessing? (Explicitly.)
5. Define ASSUMPTIONS: What are we taking as given? (These become risks if wrong — hand off to Deep-Risk #105)

**Why this matters:** "Is this feasible?" without scope is unanswerable. "Can we deliver a production-ready Delta Lake pipeline for EPR reporting by Q2 with the current 3-person team assuming Mars provides data in agreed format?" — THAT is assessable.

**Output:** `scope → {subject, horizon, standard, exclusions, assumptions}`

---

## Phase 1: CONSTRAIN

*Goal: Identify what is truly IMPOSSIBLE vs what is merely DIFFICULT. Distinguish hard physical/logical/legal limits from soft practical/organizational challenges. Find contradictions that signal fundamental infeasibility.*

---

### 101 — Constraint Hardness Spectrum

**What:** Classify every constraint on a spectrum from absolutely impossible to merely inconvenient. This prevents two errors: (1) treating hard impossibilities as "challenges to overcome" and (2) treating soft difficulties as hard impossibilities.

**The Spectrum:**

| Level | Name | Nature | Example | Response |
|-------|------|--------|---------|----------|
| **H5** | Logically Impossible | Violates mathematics/logic/physics | Halting problem, perpetual motion, FLP | **STOP.** Redesign. |
| **H4** | Computationally Infeasible | NP-hard at scale, no good approximation | Optimal scheduling for 10K variables | Approximate, decompose, heuristic |
| **H3** | Structurally Blocked | Organization/architecture prevents | Conway misalignment, no authority to decide | Restructure org, change architecture |
| **H2** | Resource Constrained | Lack of people/money/time/skills | Need 5 specialists, have 2 | Acquire, trade, defer, reduce scope |
| **H1** | Practically Difficult | Doable but hard, risky, expensive | Migrate legacy system with no docs | Plan carefully, accept cost |
| **H0** | Inconvenient | Minor friction, easily overcome | Need to learn a new API | Just do it |

**Process:**
1. List all identified constraints (from Deep-Explore #3, from stakeholders, from technical analysis)
2. Classify each on H0-H5 spectrum
3. For H5 (impossible): STOP further analysis on that path. It cannot be overcome with effort. Reframe the problem.
4. For H4 (computationally infeasible): investigate approximations. Exact solution infeasible ≠ good-enough solution infeasible.
5. For H3-H2: these are the real feasibility battleground — hard but potentially addressable
6. **Red flag:** Team treating H5 as H2 ("if we just work harder...") or H1 as H5 ("it's impossible" when it's just inconvenient)

**Output:** `constraints[] → {constraint, hardness_level, nature, response_strategy, misclassification_risk}`

---

### 102 — Requisite Variety Audit (Ashby)

**What:** Measure whether the team/tools/process have enough VARIETY (response options, skills, capabilities) to control the problem's complexity. If problem variety exceeds team variety, the project is structurally infeasible.

**Process:**
1. Enumerate **problem dimensions** — every independent axis of complexity:
   - Technologies involved (languages, platforms, services)
   - Domains required (data engineering, security, compliance, UX, business logic)
   - Integration points (APIs, databases, services, organizations)
   - Failure modes that must be handled
   - Stakeholder perspectives to satisfy
2. Enumerate **team variety** — response capabilities:
   - Skills present on team
   - Tools available
   - Decision authority held
   - Time available for learning
3. Compare: for each problem dimension, does the team have a corresponding capability?
4. **Variety Gap = Problem Dimensions - Team Capabilities**
5. If gap > 0: project is infeasible WITHOUT acquiring the missing variety (hire, train, outsource, simplify)

**Example:**
```
Problem dimensions: Databricks, Terraform, Python, Delta Lake, Synapse, 
                    EPR regulations, Mars data model, Azure AD, CI/CD
Team variety:       Databricks ✓, Terraform ✓, Python ✓, Delta Lake ✓, 
                    Synapse ~, EPR regulations ✗, Mars data model ~, Azure AD ✓, CI/CD ✓
Variety gap: EPR regulations (missing), Synapse (partial), Mars data model (partial)
Assessment: CONDITIONALLY feasible — need EPR domain expert or steep learning curve
```

**Output:** `variety_audit → {problem_dimensions[], team_capabilities[], gap[], feasibility_given_gap}`

---

### 103 — TRIZ Contradiction Detection

**What:** Search for technical and physical contradictions in requirements that signal fundamental design conflicts. Unresolved contradictions mean the requirements AS STATED are infeasible — but TRIZ resolution principles may reveal creative solutions.

**Technical Contradiction:** Improving parameter X worsens parameter Y.
- "Must be real-time AND process massive batches" (speed vs throughput)
- "Must be fully secure AND zero-friction user experience" (security vs usability)
- "Must be highly available AND strongly consistent" (CAP theorem — H5 impossibility)

**Physical Contradiction:** Element must simultaneously have property A and NOT-A.
- "Data must be encrypted at rest AND queryable by Synapse serverless" (encrypted AND readable)
- "Pipeline must be idempotent AND process exactly once" (retryable AND non-duplicating)
- "System must be simple AND handle all edge cases" (simple AND comprehensive)

**Process:**
1. For each pair of requirements: does satisfying R1 conflict with R2?
2. If yes: is it a technical contradiction (X improves, Y worsens) or physical (A and not-A)?
3. For technical contradictions: check TRIZ 40 Inventive Principles for resolution strategies:
   - Separation in time ("real-time for latest data, batch for historical")
   - Separation in space ("encrypt at rest, decrypt in secure compute enclave")
   - Separation in scale ("simple API surface, complex internal logic")
   - Separation by condition ("available normally, consistent during writes")
4. For physical contradictions: if no separation resolves it AND it maps to a theorem (CAP, FLP, etc.) → H5 impossible. Hand off to Deep-Verify.
5. Resolved contradiction → feasible with creative design. Unresolved → infeasible as stated.

**Output:** `contradictions[] → {R1, R2, type, triz_resolution_attempted, resolved, resolution_method}`

---

### 104 — Conway Alignment Check

**What:** Assess whether the required system architecture is compatible with the organizational structure that must build and maintain it. Misalignment between architecture and org is a STRUCTURAL infeasibility.

**Process:**
1. Map the required system architecture (components, interfaces, data flows)
2. Map the organizational structure (teams, reporting lines, communication channels)
3. For each architectural interface: does a corresponding organizational communication channel exist?
4. **Aligned:** Component A↔B interface maps to Team X↔Y communication → feasible
5. **Misaligned:** Component A↔B interface has no Team X↔Y channel → infeasible WITHOUT org change
6. Assess: can the org change? Or must the architecture change to match the org?

**Example:**
```
Architecture requires: Tight integration between Databricks pipeline and Synapse reporting
Org structure: Pipeline team (Lingaro) ↔ Reporting team (Mars internal)
Communication: Monthly review meetings, no shared Slack, different JIRA boards
Conway Assessment: MISALIGNED — tight technical integration requires tight communication
                   Monthly meetings insufficient for daily integration issues
Resolution: Either (a) create shared daily standup or (b) redesign for loose coupling
```

**Output:** `conway_check → {arch_interface, org_channel, aligned, resolution_if_misaligned}`

---

### 105 — Regulatory Feasibility Scan

**What:** Determine whether the project is LEGALLY PERMITTED. Brilliant technical execution of something illegal is worthless — and regulatory constraints are often H5 (cannot be overcome by effort).

**Process:**
1. Identify all regulatory jurisdictions that apply
2. For each: what activities are required, permitted, restricted, prohibited?
3. Map requirements against regulations:
   - **Required by regulation:** Must do regardless of project plan
   - **Permitted:** Can do
   - **Restricted:** Can do under conditions (what conditions? Are they feasible?)
   - **Prohibited:** Cannot do → H5 constraint
4. Check for regulatory contradictions: Jurisdiction A requires X, Jurisdiction B prohibits X
5. Assess regulatory stability: is this regulation likely to change during project timeline?

**Output:** `regulatory_map → {regulation, jurisdiction, requirement_mapping, status, stability}`

---

### 106 — Precedent Existence Check

**What:** Has anyone done something substantially similar before? Existence of precedent is strong evidence of feasibility. Absence of precedent is a WARNING (not proof of infeasibility, but reason for deeper investigation).

**Process:**
1. Define the core capability/outcome being assessed
2. Search for precedents: same domain, adjacent domains, analogous problems
3. Classify:
   - **Direct precedent:** Someone did essentially this → STRONG feasibility evidence
   - **Analogous precedent:** Someone did something structurally similar in different domain → moderate evidence
   - **Partial precedent:** Parts exist but combination is novel → each part feasible, composition uncertain (#207)
   - **No precedent:** Nobody has done this → WARNING. Not impossible, but investigate deeply.
4. For each precedent: what was their context? (team size, timeline, budget, tools) How does ours compare?
5. **Novel combination alert:** All components have precedent but this specific combination doesn't → composition feasibility (#207) is the key question

**Output:** `precedents[] → {precedent, type, context_comparison, feasibility_evidence_strength}`

---

## Phase 2: ASSESS

*Goal: Evaluate feasibility across 10 independent dimensions. The project's feasibility is bounded by its WEAKEST dimension (Goldratt). Like a chain — strength determined by weakest link.*

---

### 201 — Technical Feasibility (TRL Analysis)

**What:** Assess whether the required technology exists, works, and works at the needed scale. Uses NASA TRL framework adapted for software/data projects.

**Process:**
1. List all technology components required
2. For each: assign TRL (1-9):
   - TRL 1-3: Research phase — can it work at all?
   - TRL 4-6: Development phase — does it work in relevant conditions?
   - TRL 7-9: Operations phase — does it work in production?
3. **System TRL = min(component TRLs)** — weakest component limits the whole
4. For components with TRL < 7: what is needed to reach TRL 7? How long? What could block it?
5. **Scale assessment:** Something that works for 1K records may not work for 1B. Assess each component at TARGET scale, not demo scale.

**Feasibility Rating:**

| System TRL | Assessment |
|-----------|-----------|
| 7-9 | Technically feasible — proven technology |
| 5-6 | Conditionally feasible — needs validation at production conditions |
| 3-4 | Uncertain — requires significant development |
| 1-2 | Research — feasibility unknown, probe required |

**Output:** `technical_feasibility → {component, TRL, scale_tested, scale_needed, gap, development_needed}`

---

### 202 — Resource Feasibility

**What:** Do we have the people, money, infrastructure, and tools — or can we acquire them within constraints?

**Resource Types:**

| Resource | Check | Common Failure Mode |
|----------|-------|-------------------|
| **People** | Headcount, skills, availability, continuity | Key person bottleneck, skill gap, part-time allocation |
| **Budget** | Allocated vs needed, contingency, approval | Hidden costs, no contingency, late budget cuts |
| **Infrastructure** | Compute, storage, network, environments | Provisioning delays, capacity limits, environment parity |
| **Tools/Licenses** | Software, services, access | Procurement delays, license restrictions, vendor approval |
| **Time** | Calendar time, work time, elapsed time | Calendar ≠ work time, holidays, context switching |

**Process:**
1. For each resource type: what's NEEDED vs what's AVAILABLE?
2. Gap analysis: can gaps be closed? At what cost? In what timeframe?
3. **Brooks's Law check:** If gap is people, can you actually add people productively? (Communication overhead: n people = n(n-1)/2 communication channels)
4. Check for resource CONTENTION: same resources needed by multiple workstreams simultaneously
5. Three-point estimation for each resource: optimistic / likely / pessimistic

**Output:** `resource_feasibility → {resource_type, needed, available, gap, closable, cost_to_close, brooks_law_flag}`

---

### 203 — Knowledge Feasibility

**What:** Does the team know HOW to do this? Knowledge feasibility is distinct from resource feasibility — you can have enough people but not enough knowledge. An epistemic constraint.

**Knowledge Types:**

| Type | Question | If Missing |
|------|----------|-----------|
| **Domain** | Do we understand the business domain? (EPR regulations, Mars processes) | Hire expert, consult client, study |
| **Technical** | Do we know the technologies? (Databricks, Terraform, Synapse) | Train, hire, consultant |
| **Architectural** | Do we know how to design at this scale/complexity? | Senior architect, reference architecture |
| **Procedural** | Do we know the processes? (CI/CD, testing, deployment) | Document, train, automate |
| **Tacit** | Is there undocumented knowledge needed? (Tribal knowledge, conventions) | Knowledge transfer, pairing, risk acceptance |

**Process:**
1. For each sub-question from #002: what knowledge is required?
2. For each knowledge need: does it exist on the team?
3. If not: can it be acquired within the project timeline?
4. **Tacit knowledge alert:** Tacit knowledge cannot be transferred by documentation — requires pairing, mentoring, or hiring someone who has it. Significantly harder to close.
5. Apply **Dunning-Kruger check:** Low knowledge in an area → team likely OVERESTIMATES their capability in that area. Most dangerous: areas where team has "a little" knowledge.

**Output:** `knowledge_feasibility → {knowledge_type, domain, present, acquirable, acquisition_method, dunning_kruger_risk}`

---

### 204 — Organizational Feasibility

**What:** Can the organization execute this? Not just "do we have people" but "can our org structure, processes, culture, and decision-making support this?"

**Organizational Dimensions:**

| Dimension | Question |
|-----------|---------|
| **Decision authority** | Can the necessary decisions be made by people on the project? Or do they require approvals that add weeks? |
| **Cross-team coordination** | Does this require coordinated effort across teams? How well do those teams coordinate? |
| **Conway alignment** | Does org structure match required architecture? (From #104) |
| **Culture fit** | Does the approach align with org culture? (Agile in a waterfall org? Data mesh in a centralized org?) |
| **Change capacity** | How much change is the org already absorbing? Is there capacity for more? |
| **Stakeholder alignment** | Are key stakeholders aligned on goals and approach? Misalignment = decision paralysis |
| **Political feasibility** | Are there political dynamics that could block execution? Champions? Opponents? |

**Process:**
1. Assess each dimension honestly
2. For each "No": is it changeable within project timeline?
3. **Organizational debt** is like technical debt — accumulated dysfunction that taxes every project. High org debt = lower feasibility for everything.

**Output:** `org_feasibility → {dimension, assessment, changeable, impact_on_project}`

---

### 205 — Temporal Feasibility (Critical Path Analysis)

**What:** Can we do this in the time available? Not just total effort but CALENDAR time considering dependencies, parallelism limits, and waiting time.

**Process:**
1. Decompose into tasks with effort estimates
2. Map dependencies: what must happen before what?
3. Identify critical path: longest dependency chain = minimum calendar time
4. Identify parallelism limits: how much can happen simultaneously? (Constrained by team size, environments, dependencies)
5. Add non-work time: holidays, context switching, meetings, sick days, vacations
6. Add WAITING time: approvals, provisioning, third-party dependencies, feedback cycles
7. Compare total against deadline
8. **Hofstadter correction:** After all this, add 30-50% because it STILL takes longer than estimated
9. **Flyvbjerg correction:** Check reference class — what % of similar projects delivered on time?

**Common Calendar Time Traps:**
- **Effort ≠ duration:** 40 hours of work ≠ 1 week (meetings, context switches, interruptions)
- **Parallelism assumption:** "Two people = half the time" — almost never true (Brooks)
- **Waiting time invisibility:** 2 weeks of waiting for environment provisioning not in any task estimate
- **Integration time:** Individual components done ≠ system done. Integration typically takes 30-50% of total

**Output:** `temporal_feasibility → {critical_path, total_effort, calendar_time, deadline, buffer, hofstadter_adjusted, reference_class_rate}`

---

### 206 — Compositional Feasibility

**What:** Every component is individually feasible — but does the WHOLE work? Integration is where feasibility estimates most often fail. The gap between "parts work" and "system works" is often larger than the effort to build the parts.

**Process:**
1. List all components that must integrate
2. For each pair: what's the interface? Is it defined? Has it been tested?
3. Identify integration complexity drivers:
   - **Data format mismatches** (timestamps, encodings, schemas)
   - **Timing assumptions** (sync vs async, timeout expectations)
   - **Error handling gaps** (what does component A do when B fails?)
   - **State management** (who owns state? How is it synchronized?)
   - **Version coupling** (do components need to be deployed together?)
4. **Precedent check:** Has this specific combination been built before? (#106)
5. Estimate integration effort as % of total:
   - Well-defined interfaces, existing precedent: ~15-20%
   - Partially defined interfaces, partial precedent: ~30-40%
   - Undefined interfaces, no precedent: ~50-70%
6. **Ship of Theseus test:** If the system will be migrated incrementally, is each step feasible AND does the accumulated change remain coherent?

**Output:** `composition_feasibility → {components, interfaces, integration_complexity, integration_effort_%, precedent, feasible}`

---

### 207 — Economic Feasibility

**What:** Is it WORTH doing? Even if technically achievable, if costs exceed benefits, the project is economically infeasible.

**Process:**
1. Estimate total cost: development + infrastructure + operations + maintenance + opportunity cost
2. Estimate total benefit: revenue, cost savings, risk reduction, strategic value
3. Calculate:
   - **ROI:** (Benefit - Cost) / Cost
   - **Payback period:** When does cumulative benefit exceed cumulative cost?
   - **NPV:** Net present value at appropriate discount rate
4. Sensitivity analysis: how much can costs increase / benefits decrease before it's negative?
5. **Strategic value assessment:** Some projects have value beyond direct ROI (capability building, market positioning, compliance). Quantify or explicitly acknowledge.
6. Compare against alternatives: is there a cheaper way to achieve 80% of the benefit?

**Output:** `economic_feasibility → {total_cost, total_benefit, ROI, payback, NPV, sensitivity, strategic_value}`

---

### 208 — Scale Feasibility

**What:** Does it work at PRODUCTION scale? The most common false feasibility: "it works in demo" ≠ "it works in production." The gap between proof-of-concept and production is often 10× the PoC effort.

**Scale Dimensions:**

| Dimension | Demo | Production | Typical Gap |
|-----------|------|-----------|------------|
| **Data volume** | 1K records | 1B records | 1,000,000× |
| **Concurrent users** | 1-5 | 100-10,000 | 1,000× |
| **Uptime requirement** | Best effort | 99.9%+ | Qualitative shift |
| **Error handling** | Happy path | All paths | 10× code complexity |
| **Security** | None/basic | Production-grade | 5-10× effort |
| **Monitoring** | Console logs | Full observability | Separate workstream |
| **Data quality** | Clean test data | Messy real data | Unpredictable |

**Process:**
1. For each scale dimension: what's the demo/PoC level vs production requirement?
2. Is there a qualitative shift? (Not just "more" but "fundamentally different")
   - Example: 99.9% uptime is not just "better" 99% — it requires completely different architecture
3. For each dimension: has this been tested at production scale?
4. **PoC-to-production multiplier:** Estimate effort to go from working PoC to production-ready. Common range: 3× to 10×.

**Output:** `scale_feasibility → {dimension, demo_level, production_level, qualitative_shift, tested_at_scale, poc_to_prod_multiplier}`

---

### 209 — Cognitive Feasibility

**What:** Can the team UNDERSTAND what they're building? A system that exceeds the cognitive capacity of its builders/operators is infeasible even if each component is individually understandable.

*Grounded in Ashby's Requisite Variety and George Miller's "7±2" cognitive limit.*

**Process:**
1. Count the number of INDEPENDENT concepts someone must hold in mind simultaneously to:
   - Design the system
   - Modify a component
   - Debug a production issue
   - Onboard a new team member
2. If count > 7-9: system exceeds working memory → errors inevitable → infeasible to maintain
3. Assess **concept coupling:** how many concepts interact with each other? High coupling = exponential cognitive load
4. Check for **abstraction adequacy:** do good abstractions exist that reduce cognitive load? (If you must understand implementation details to use the system, abstractions are leaky)
5. **Onboarding test:** How long would it take a competent engineer to become productive? >3 months = cognitive feasibility risk.

**Output:** `cognitive_feasibility → {concept_count, coupling_degree, abstraction_quality, onboarding_time, feasible}`

---

### 210 — Dependency Feasibility

**What:** Are all external dependencies actually available, reliable enough, and affordable? Every external dependency is a feasibility assumption that must be verified.

**Process:**
1. List ALL external dependencies (services, APIs, data sources, approvals, partner deliverables)
2. For each dependency:
   - **Available?** Does it exist? Can we access it? (Licensing, approvals, network access)
   - **Reliable enough?** Does it meet our uptime/quality requirements? (SLA, historical reliability)
   - **Affordable?** Can we pay for it at production scale? (Pricing models often change at scale)
   - **Stable?** Will it still exist/work in 12 months? (Deprecation risk, vendor viability)
   - **Timely?** Will it be available WHEN we need it? (Partner deliverables, provisioning delays)
3. For each "No" or "Uncertain": is there an alternative? At what cost?
4. **Dependency chain check:** If we depend on A, and A depends on B, and B depends on C — is the CHAIN feasible?

**Output:** `dependency_feasibility → {dependency, available, reliable, affordable, stable, timely, alternative}`

---

## Phase 3: VALIDATE

*Goal: Empirically test the most critical feasibility assumptions. Analysis tells you what SHOULD work — validation tells you what ACTUALLY works.*

---

### 301 — Reference Class Forecasting (Flyvbjerg)

**What:** Replace inside-view estimates with outside-view base rates from similar projects. The single most effective debiasing technique for feasibility assessment.

**Process:**
1. Define the project's **reference class:** What type of project is this? (Data platform migration? New product launch? Regulatory compliance system?)
2. Find base rates for that class:
   - What % deliver on time? On budget? With full scope?
   - What's the median cost overrun? Schedule overrun?
   - What's the common failure mode?
3. **Start from the base rate,** then adjust for project-specific factors:
   - Factors that make THIS project better than typical: experienced team, proven technology, clear requirements
   - Factors that make it worse: novel technology, unclear requirements, organizational complexity
4. **Anchor to the base rate.** Adjustments should be modest — the base rate is almost always more accurate than internal estimates.

**Reference Class Examples:**

| Project Type | On-Time Rate | Avg Cost Overrun | Avg Schedule Overrun |
|-------------|-------------|-----------------|---------------------|
| Enterprise data platform | ~25% | +60-100% | +50-80% |
| Cloud migration | ~30% | +40-80% | +40-60% |
| Regulatory compliance system | ~35% | +30-60% | +30-50% |
| Greenfield software product | ~20% | +100-200% | +80-150% |
| Infrastructure automation | ~40% | +30-50% | +30-50% |

*(Ranges from Standish CHAOS, Flyvbjerg meta-analyses, industry surveys. Use domain-specific data when available.)*

**Output:** `reference_forecast → {reference_class, base_rate, adjustments, calibrated_estimate, confidence}`

---

### 302 — Critical Assumption Testing

**What:** Identify the assumptions that feasibility MOST depends on, then test them empirically before committing.

**Process:**
1. From all assessment dimensions (#201-210): list key assumptions
2. Rank by: **impact if wrong** × **uncertainty**
3. Top 3-5 assumptions → design a MINIMAL test:
   - What would CONFIRM the assumption? What would REFUTE it?
   - What's the cheapest/fastest way to test?
   - What's the decision threshold? (If test shows X, we proceed. If Y, we stop.)
4. RUN the tests before the Go/No-Go decision
5. **No test = assumption is accepted on faith.** Make that explicit.

**Example:**
```
Critical assumption: "Databricks cluster can process 10M records in 4-hour window"
├── Test: Run 10M records on production-sized cluster with production-like data
├── Cost: 1 day of engineering + cluster costs (~$200)
├── Decision threshold: <3.5 hours = proceed, 3.5-5 hours = investigate, >5 hours = redesign
├── Outcome: 2.8 hours → CONFIRMED
└── Value of test: Prevented potential $100K+ discovery-in-production
```

**Output:** `assumption_tests[] → {assumption, impact, uncertainty, test_design, cost, threshold, outcome}`

---

### 303 — Probe Design (Complex Domain)

**What:** For sub-problems classified as Complex in #001, design safe-to-fail experiments that REVEAL feasibility through action, not analysis. You cannot analyze your way to feasibility in a complex domain — you must probe.

*From Cynefin: Complex domain → Probe-Sense-Respond.*

**Probe Properties:**
- **Safe-to-fail:** Probe failure must be survivable (limited blast radius)
- **Informative:** Probe outcome must change your feasibility assessment
- **Fast:** Probe must deliver results in days/weeks, not months
- **Cheap:** Probe cost must be small relative to full project cost
- **Multiple:** Run several probes in parallel (different approaches to same question)

**Process:**
1. For each Complex sub-problem: define what "feasibility" means in observable terms
2. Design 2-3 parallel probes that explore different approaches
3. Define success/failure criteria BEFORE running probes (prevent post-hoc rationalization)
4. Run probes with explicit time/cost limits
5. **Amplify or dampen:** If probe succeeds → amplify (invest more). If probe fails → dampen (stop that path).

**Example:**
```
Complex question: "Can we build ML-based data quality detection for Mars packaging data?"
├── Probe A: Rule-based anomaly detection (3 days) — baseline feasibility
├── Probe B: Statistical outlier detection (3 days) — moderate complexity
├── Probe C: Transformer-based detection (5 days) — high complexity
├── Success criteria: Detect >80% of known-bad records in test set
├── Results: A=60%, B=82%, C=75% (overfit)
└── Decision: B is feasible, A needs enhancement, C is not feasible within our skill set
```

**Output:** `probes[] → {complex_question, probe_design, cost, time_limit, success_criteria, outcome, amplify_or_dampen}`

---

### 304 — Expert Judgment Calibration

**What:** Gather expert estimates but apply structured debiasing. Raw expert judgment is better than non-expert but still systematically biased. Calibration corrects for known biases.

**Process:**
1. Identify the right experts (domain experience, relevant track record)
2. Structure the elicitation:
   - Ask for THREE-POINT estimate (optimistic, likely, pessimistic) — forces acknowledgment of uncertainty
   - Ask for CONFIDENCE LEVEL ("How confident are you in the likely estimate? 60%? 90%?")
   - Ask experts INDEPENDENTLY (prevent anchoring and groupthink)
3. Apply debiasing:
   - **Widen the range:** Experts' 80% confidence intervals typically contain the true value only ~50% of the time. Double the range.
   - **Shift the center:** Planning fallacy shifts estimates optimistic. Apply 20-30% pessimistic adjustment.
   - **Weight by track record:** If expert's past estimates are available, calibrate based on their historical accuracy.
4. **Aggregate:** If multiple experts, use median (not mean — resistant to outliers)

**Output:** `expert_estimates[] → {question, expert, three_point, confidence, debiased_estimate, aggregated}`

---

### 305 — Analogical Feasibility Transfer

**What:** Find structurally similar projects/systems that have been successfully built and assess how well the analogy transfers. Precedent (#106) checks existence — this method checks structural SIMILARITY.

**Process:**
1. Identify candidate analogies (from #106 or broader search)
2. For each analogy, assess structural similarity:
   - **Surface similarity:** Same domain, same technologies → useful but can be misleading
   - **Structural similarity:** Same architecture patterns, similar complexity, similar integration challenges → more valuable
   - **Context similarity:** Similar team size, similar org structure, similar timeline pressure → most valuable
3. For each dimension where analogy DIVERGES: assess impact on feasibility
4. **Anti-pattern:** "Netflix did it, so can we" — surface similarity without structural/context similarity is dangerous

**Output:** `analogies[] → {analogy, surface_sim, structural_sim, context_sim, divergences, transferability}`

---

### 306 — Integration Spike

**What:** Build the HARDEST integration point first as a focused spike. If the hardest part is feasible, the project is likely feasible. If it's not, you find out early and cheaply.

**Process:**
1. From #206 (Compositional Feasibility): identify the riskiest integration point
2. Build a minimal spike that tests ONLY that integration:
   - Happy path: does data flow across the boundary?
   - Error path: what happens when one side fails?
   - Scale path: does it work at representative volume?
3. Time-box the spike: if you can't get basic integration working in N days, that's a STRONG infeasibility signal
4. **This is NOT a PoC of the whole system.** It's a targeted test of the compositional risk.

**Output:** `spike_results → {integration_point, happy_path, error_path, scale_path, effort, feasibility_verdict}`

---

## Phase 4: DECIDE

*Goal: Synthesize all evidence into an actionable decision. Not just Go/No-Go but CONDITIONAL Go with explicit conditions, confidence levels, and monitoring triggers.*

---

### 401 — Multi-Axis Feasibility Profile

**What:** Aggregate all 10 assessment dimensions into a visual profile showing the feasibility shape. The weakest dimension determines overall feasibility (Goldratt).

**Scoring per Dimension:**

| Score | Label | Meaning |
|-------|-------|---------|
| 5 | **Proven** | Demonstrated, precedented, no significant challenges |
| 4 | **Likely** | Strong evidence of feasibility, minor concerns |
| 3 | **Possible** | Feasible but significant challenges / uncertainties |
| 2 | **Doubtful** | Major challenges, may require fundamental changes |
| 1 | **Infeasible** | Cannot be done under current constraints |

**Profile:**
```
Technical     ████████░░  4
Resource      ██████░░░░  3
Knowledge     ████████░░  4
Organization  ██████░░░░  3
Temporal      ████░░░░░░  2  ← BINDING CONSTRAINT
Composition   ██████░░░░  3
Economic      ████████░░  4
Regulatory    ██████████  5
Scale         ██████░░░░  3
Cognitive     ████████░░  4

Overall: CONDITIONALLY FEASIBLE (limited by temporal — need deadline extension or scope reduction)
```

**Process:**
1. Score each dimension (1-5) based on Phase 2 evidence
2. Identify binding constraint (lowest score)
3. Determine overall: MIN score determines ceiling
4. For binding constraint: what would it take to raise it by 1 point?

**Output:** `feasibility_profile → {dimension_scores[10], binding_constraint, overall, improvement_path}`

---

### 402 — Confidence-Weighted Decision

**What:** Combine feasibility score with CONFIDENCE in that score. A score of 4 with high confidence is very different from a score of 4 with low confidence.

**Decision Matrix:**

| | High Confidence | Low Confidence |
|---|---|---|
| **Feasible (4-5)** | **GO** — proceed with standard risk management | **CONDITIONAL GO** — proceed but invest in validation |
| **Borderline (3)** | **CONDITIONAL GO** — proceed with explicit conditions and checkpoints | **INVESTIGATE** — more information needed before deciding |
| **Infeasible (1-2)** | **NO GO** — stop, redirect, or fundamentally redesign | **INVESTIGATE or NO GO** — may be infeasible, may be unknown |

**Confidence Assessment:**
- **High:** Based on empirical evidence (probes, spikes, reference class data)
- **Medium:** Based on expert judgment (calibrated) and analogies
- **Low:** Based on team gut feeling and planning (uncalibrated)

**Output:** `decision → {feasibility_score, confidence_level, decision, conditions, next_steps}`

---

### 403 — Conditional Feasibility Map

**What:** Most projects are not simply "feasible" or "infeasible" — they are "feasible IF." Map all conditions that must hold for feasibility to remain valid.

**Process:**
1. List ALL conditions identified across assessment dimensions:
   - "Feasible IF Mars delivers data in agreed format by March"
   - "Feasible IF we hire a Synapse specialist within 4 weeks"
   - "Feasible IF Databricks cluster costs stay under $X/month"
   - "Feasible IF no regulatory changes before go-live"
2. For each condition:
   - **Probability of condition holding:** High / Medium / Low / Unknown
   - **Who controls it:** Us / Partner / External (regulatory, market)
   - **Fallback if condition fails:** What happens? Is there a Plan B?
   - **Monitoring:** How will we know if condition is failing?
3. **Compounding probability:** If you need 5 independent conditions to hold, and each has P=0.8, overall P = 0.8^5 = 0.33. Many "likely" conditions → unlikely combined feasibility.

**Output:** `conditions[] → {condition, probability, controller, fallback, monitoring, compound_probability}`

---

### 404 — Feasibility Decay Monitoring

**What:** Feasibility is not static. Design triggers that indicate feasibility is degrading and reassessment is needed.

**Decay Triggers:**

| Trigger | Mechanism |
|---------|-----------|
| **Scope change** | New requirements → reassess compositional, temporal, cognitive |
| **Team change** | Person leaves → reassess knowledge, resource, organizational |
| **Dependency change** | API deprecated, vendor acquired → reassess technical, dependency |
| **Budget change** | Cut → reassess resource, economic |
| **Timeline change** | Accelerated deadline → reassess temporal |
| **Regulatory change** | New regulation → reassess regulatory |
| **Technology change** | Major version, deprecation → reassess technical |
| **Market change** | Competitor launch, market shift → reassess economic |

**Process:**
1. For each assessed dimension: what events would change the score?
2. Define monitoring cadence: how often to re-check?
3. Define threshold: what score change triggers full reassessment?
4. **Boehm's Spiral:** Major project milestones should include feasibility re-evaluation as standard practice

**Output:** `decay_monitors[] → {dimension, trigger_event, check_cadence, reassessment_threshold}`

---

## META Methods

*Applied continuously. Detect bias in the assessment process itself.*

---

### 501 — Planning Fallacy Detection

**What:** Actively search for signs that the assessment is affected by systematic optimism.

**Detection Signals:**

| Signal | What It Means |
|--------|--------------|
| All dimensions score ≥3 | Possible optimism — how does this compare to reference class? |
| No critical conditions identified | Likely blind spots |
| Timeline has no buffer | Planning fallacy active |
| "If everything goes well" | Assuming best case as base case |
| First estimate accepted without challenge | Anchoring to initial guess |
| Integration effort < 20% of total | Almost certainly underestimated |
| No acknowledged unknowns | Dunning-Kruger or wishful thinking |

**Correction:** When detected, apply Hofstadter correction and reference class adjustment. If no reference class data available, add 50% to timeline and 80% to cost as default correction.

**Output:** `planning_fallacy_check → {signals_detected, severity, corrections_applied}`

---

### 502 — Hofstadter Correction

**What:** After all estimation and calibration, apply one final recursive correction: it STILL takes longer and costs more than you think, even after you've corrected for that.

**Process:**
1. Take final calibrated estimates (time, cost, effort)
2. Apply reference-class-based correction factor
3. If no reference class: multiply by 1.5× (time) and 1.8× (cost) as empirical default
4. Ask: "If I told a friend this estimate, would they believe it? Or would they laugh?"
5. **The estimate that feels uncomfortably pessimistic is usually the most accurate.**

**Output:** `hofstadter_adjusted → {original_estimate, correction_factor, adjusted_estimate, gut_check}`

---

### 503 — Confidence Theater Detection

**What:** Distinguish genuine confidence (based on evidence) from performed confidence (based on social pressure to appear certain).

**Theater vs Genuine:**

| Confidence Theater | Genuine Confidence |
|---|---|
| "We'll definitely deliver on time" (no basis) | "Reference class shows 40% on-time, but we have mitigations X and Y" |
| All estimates are single points (no range) | Three-point estimates with explicit uncertainty |
| "We've done this before" (but context was different) | "We've done the data pipeline part; the regulatory module is new to us" |
| Consensus reached quickly without debate | Consensus after exploring disagreements |
| No one mentions risks or concerns | Team actively identifies concerns |

**Process:**
1. Evaluate how estimates were produced: evidence-based or consensus-based?
2. Check for dissent: was disagreement expressed and explored?
3. Look for specificity: are responses detailed (genuine) or vague (theater)?
4. **Ask the uncomfortable question:** "What's the most likely way this fails?" If no one has a specific answer, confidence is theatrical.

**Output:** `theater_check → {indicator, theater_or_genuine, evidence}`

---

### 504 — Dunning-Kruger Dimension Mapping

**What:** Identify dimensions where team expertise is LOW but confidence is HIGH — the Dunning-Kruger danger zone. These dimensions produce the most dangerously wrong feasibility assessments.

**Process:**
1. For each of the 10 assessment dimensions: rate team EXPERTISE (Low/Medium/High)
2. For each: rate team CONFIDENCE in their feasibility score (Low/Medium/High)
3. **Danger zones:**
   - Expertise LOW + Confidence HIGH = **DUNNING-KRUGER ALERT** — scores are unreliable, seek external validation
   - Expertise HIGH + Confidence LOW = **Imposter syndrome** — scores may be too pessimistic
   - Expertise LOW + Confidence LOW = **Acknowledged gap** — investigation needed
   - Expertise HIGH + Confidence HIGH = **Calibrated** — most reliable scores

**Output:** `dk_map → {dimension, expertise, confidence, zone, action}`

---

### 505 — Meta-Feasibility Check

**What:** Can we even assess feasibility? The feasibility of feasibility assessment. For Complex-domain problems (#001), the answer may be "no" — and that's a valid, important answer.

**When assessment itself is infeasible:**
- Problem is in Complex domain (emergent, unpredictable)
- No reference class exists (truly novel)
- Key variables are unknowable in advance
- Assessment would cost as much as doing the project (Bonini's paradox)

**In these cases:**
1. Acknowledge: "We cannot assess feasibility of this with traditional analysis"
2. Shift strategy: design probes (#303) instead of comprehensive assessment
3. Adopt: "fail fast, fail cheap" approach — make small bets to learn
4. Set: maximum investment threshold — "We'll invest $X to find out if this is feasible"

**Output:** `meta_feasibility → {assessable, reason_if_not, alternative_strategy}`

---

## Method Summary

| # | Phase | Method | Core Question |
|---|-------|--------|---------------|
| 001 | FRAME | Cynefin Domain Classification | Can we even assess feasibility traditionally? |
| 002 | FRAME | Feasibility Question Decomposition | What exactly are we assessing? |
| 003 | FRAME | Feasibility Scope Definition | What's in/out, by when, to what standard? |
| 101 | CONSTRAIN | Constraint Hardness Spectrum | Impossible vs hard vs inconvenient? |
| 102 | CONSTRAIN | Requisite Variety Audit | Does team variety match problem variety? |
| 103 | CONSTRAIN | TRIZ Contradiction Detection | Are requirements fundamentally contradictory? |
| 104 | CONSTRAIN | Conway Alignment Check | Does org structure support required architecture? |
| 105 | CONSTRAIN | Regulatory Feasibility Scan | Is it legally permitted? |
| 106 | CONSTRAIN | Precedent Existence Check | Has anyone done this before? |
| 201 | ASSESS | Technical Feasibility (TRL) | Does the technology exist and scale? |
| 202 | ASSESS | Resource Feasibility | Do we have people/money/tools? |
| 203 | ASSESS | Knowledge Feasibility | Do we know HOW? |
| 204 | ASSESS | Organizational Feasibility | Can our org execute this? |
| 205 | ASSESS | Temporal Feasibility | Can we do it in time? |
| 206 | ASSESS | Compositional Feasibility | Do the parts work together? |
| 207 | ASSESS | Economic Feasibility | Is it worth doing? |
| 208 | ASSESS | Scale Feasibility | Demo → production gap? |
| 209 | ASSESS | Cognitive Feasibility | Can the team understand it? |
| 210 | ASSESS | Dependency Feasibility | Are dependencies available and reliable? |
| 301 | VALIDATE | Reference Class Forecasting | What do base rates say? |
| 302 | VALIDATE | Critical Assumption Testing | Do key assumptions hold empirically? |
| 303 | VALIDATE | Probe Design (Complex Domain) | Safe-to-fail experiments for emergent problems |
| 304 | VALIDATE | Expert Judgment Calibration | Debiased expert estimates |
| 305 | VALIDATE | Analogical Feasibility Transfer | How well does precedent transfer? |
| 306 | VALIDATE | Integration Spike | Does the hardest integration point work? |
| 401 | DECIDE | Multi-Axis Feasibility Profile | 10-dimension visual assessment |
| 402 | DECIDE | Confidence-Weighted Decision | Feasibility × confidence → Go/No-Go |
| 403 | DECIDE | Conditional Feasibility Map | Feasible IF what conditions hold? |
| 404 | DECIDE | Feasibility Decay Monitoring | When does feasibility need reassessment? |
| 501 | META | Planning Fallacy Detection | Is the assessment systematically optimistic? |
| 502 | META | Hofstadter Correction | Recursive estimation adjustment |
| 503 | META | Confidence Theater Detection | Is confidence genuine or performed? |
| 504 | META | Dunning-Kruger Dimension Map | Low expertise + high confidence zones? |
| 505 | META | Meta-Feasibility Check | Can we even assess this? |

**Total: 35 methods** (3 FRAME + 6 CONSTRAIN + 10 ASSESS + 6 VALIDATE + 4 DECIDE + 5 META + implicit overlap management)

---

## Usage Guide

### When to Use Deep-Feasibility

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **Go/No-Go decision** | FRAME → full cycle | Full |
| **New project/initiative** | FRAME → CONSTRAIN → ASSESS | Standard |
| **Technology choice** | CONSTRAIN → ASSESS (Technical, Scale) → VALIDATE | Focused |
| **Make vs buy** | ASSESS (Resource, Knowledge, Temporal, Economic) → DECIDE | Focused |
| **Scope change** | ASSESS (affected dimensions) → VALIDATE → DECIDE | Reassessment |
| **Milestone checkpoint** | ASSESS (re-score) → VALIDATE → DECIDE | Boehm spiral |
| **Post-failure analysis** | META (what did we miss?) → full reassessment | Retrospective |

### Scaling Deep-Feasibility

| Context | Methods | Time |
|---------|---------|------|
| **Quick sanity check** | #001 + #101 + #401 + #501 | 30-60 min |
| **Standard assessment** | FRAME + CONSTRAIN + ASSESS + DECIDE | Half day |
| **Rigorous** | Full cycle including VALIDATE | 2-3 days |
| **Critical Go/No-Go** | Full cycle + META + stakeholder review + spikes | 1-2 weeks |

### Integration with Other Deep Processes

Deep-Feasibility has specific handoff points with each other process:

**From Deep-Explore:**
- Options identified → assess feasibility of each option
- Assumptions identified → feed into #302 Critical Assumption Testing
- Constraints mapped → feed into #101 Constraint Hardness Spectrum

**From Deep-Verify:**
- Impossibility findings → automatic H5 constraints (#101)
- Logical conflicts → TRIZ contradiction inputs (#103)
- Validated requirements → scope for feasibility assessment (#003)

**From/To Deep-Risk:**
- Feasibility conditions (#403) → risk triggers for Deep-Risk monitoring
- Deep-Risk mitigation plans → assess feasibility of mitigations
- Non-ergodic risks → existential feasibility constraints

**Back to Deep-Explore:**
- Infeasible options → eliminate from consideration
- Conditional feasibility → new constraints for option generation
- Binding constraints → reframe the problem

---

## Appendix A: Feasibility Register Entry Template

```
ID:           FEAS-001
Subject:      [What is being assessed]
Scope:        [From #003: horizon, standard, exclusions]
Cynefin:      [From #001: Clear/Complicated/Complex/Chaotic]

CONSTRAINTS:
  Hard (H5-H4): [Impossibilities and computational limits]
  Structural (H3): [Conway misalignment, regulatory blocks]
  Resource (H2):   [Missing people, budget, tools]
  Difficulty (H1):  [Challenges, not blockers]

DIMENSION SCORES:
  Technical:      _/5  Confidence: H/M/L
  Resource:       _/5  Confidence: H/M/L
  Knowledge:      _/5  Confidence: H/M/L
  Organizational: _/5  Confidence: H/M/L
  Temporal:       _/5  Confidence: H/M/L
  Compositional:  _/5  Confidence: H/M/L
  Economic:       _/5  Confidence: H/M/L
  Regulatory:     _/5  Confidence: H/M/L
  Scale:          _/5  Confidence: H/M/L
  Cognitive:      _/5  Confidence: H/M/L

BINDING CONSTRAINT: [Weakest dimension]
OVERALL SCORE: [Min of dimensions]

VALIDATION:
  Reference class: [Base rates]
  Probes run: [Results]
  Spikes run: [Results]
  Expert estimates: [Calibrated]

CONDITIONS:
  1. [Condition] — P: ___ Controller: ___ Fallback: ___
  2. [Condition] — P: ___ Controller: ___ Fallback: ___

DECISION: GO / NO GO / CONDITIONAL GO / INVESTIGATE
CONDITIONS FOR GO: [If conditional]
REASSESSMENT: [When and what triggers]

META:
  Planning fallacy signals: [Y/N, details]
  Hofstadter adjustment: [Applied?]
  DK zones: [Which dimensions?]
  Confidence: Theater / Genuine
```
