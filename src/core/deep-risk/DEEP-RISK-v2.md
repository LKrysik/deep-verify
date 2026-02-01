# Deep-Risk v2: Systematic Risk Assessment Methodology

## Overview

Deep-Risk is the third pillar of a complementary triad:

| Process | Question | Nature |
|---------|----------|--------|
| **Deep-Explore** | *What can we do?* | Divergent — maps decision space |
| **Deep-Verify** | *Is this correct?* | Convergent — validates logical/technical correctness |
| **Deep-Risk** | *What can go wrong, how badly, and what do we do about it?* | Probabilistic — assesses threats, interactions, and responses |

Deep-Risk is **not** a generic risk checklist. It is a phased, systematic process that:

1. **Starts from theory** — understands WHY risks exist before looking for WHERE they are
2. **Consumes outputs** from Deep-Explore (options, assumptions, dependencies) and Deep-Verify (validated claims, identified conflicts)
3. **Covers both technical and business risks** — architecture failures AND strategic miscalculations
4. **Extracts risks both vertically** (deep within components) **and horizontally** (across boundaries and interfaces)
5. **Emphasizes risk interactions** — individual risks are table stakes; cascades, correlations, and concentrations are where catastrophes hide
6. **Distinguishes risk from uncertainty** — different types demand fundamentally different responses
7. **Checks its own mitigations** for perverse effects — the cure can be worse than the disease
8. **Produces actionable outputs** — not just a register but mitigation designs, monitoring systems, and escalation protocols

---

## Theoretical Foundations

Deep-Verify is grounded in impossibility theorems (FLP, CAP, Halting, Rice, Gödel, Arrow). Deep-Risk needs analogous theoretical foundations — principles that constrain what risk management CAN and CANNOT achieve:

### Foundational Theorems of Risk

**1. Normal Accident Theory (Perrow, 1984)**
In systems that are simultaneously **complex** (many non-linear interactions) and **tightly coupled** (little slack, fast propagation), accidents are **inevitable** — not a matter of IF but WHEN. Implication: for such systems, the question shifts from "how to prevent all failures" to "how to survive inevitable failures."

**2. Non-Ergodicity (Peters, 2019)**
Ensemble average ≠ time average. A 5% chance of total loss is acceptable for a casino playing 10,000 games simultaneously. It is **catastrophic** for you playing sequentially — because you cannot recover from ruin to play again. Most risk scores (Probability × Impact) implicitly assume ergodicity. For irreversible losses, this assumption is **fatally wrong.** A risk with P=0.05 and I="game over" is NOT equivalent to a risk with P=0.50 and I="minor inconvenience" — even if the expected value is similar.

**3. Fat Tails / Power Laws (Mandelbrot, Taleb)**
Many risks do NOT follow normal distributions. Impact is often power-law distributed: "Impact: 5" is not 5× worse than "Impact: 1" — it can be 100× or 1000× worse. This means: the mean is dominated by rare extreme events, variance may be infinite, and historical data systematically underestimates tail risk.

**4. Swiss Cheese Model (Reason, 1990)**
Accidents occur when holes in multiple defense layers momentarily align. Each layer has holes (weaknesses). Safety depends on layers being INDEPENDENT — if their holes are correlated, multiple layers offer the protection of one. Implication: Defense in Depth is only as strong as the independence between layers.

**5. Cobra Effect / Braess Paradox**
Interventions can produce outcomes OPPOSITE to intentions. British India offered bounty for dead cobras → people bred cobras → bounty cancelled → bred cobras released → more cobras than before. Adding a road to a network can increase total travel time (Braess). Implication: every mitigation must be checked for perverse second-order effects.

**6. Goodhart's Law**
When a measure becomes a target, it ceases to be a good measure. A risk dashboard showing zero alerts may mean: (a) no risks, or (b) team stopped reporting risks, or (c) thresholds set too high. Implication: risk metrics must be audited for gaming/decay.

**7. Knight's Distinction (1921)**
Three fundamentally different epistemic states, each requiring different management:

| State | Definition | Example | Management |
|-------|-----------|---------|------------|
| **Risk** | Known probability distribution | Server failure rate from historical data | Insure, hedge, provision |
| **Uncertainty** | Unknown probability distribution | "Will AI replace data engineers in 5 years?" | Scenario plan, build optionality |
| **Ambiguity** | Question itself is unclear | "Is the system secure?" (secure how? against whom?) | Clarify, decompose, define |

**8. Survivorship Bias**
We only learn from failures that were visible. For every well-known post-mortem, there are N companies that failed identically and disappeared without documenting anything. Historical pattern matching systematically underestimates risk because the evidence set is biased toward survivors.

**9. Lindy Effect**
Things that have survived long will likely survive longer. Conversely: NEW components, processes, relationships, and technologies have **higher base-rate risk of failure** than established ones. Age is evidence of robustness — novelty is a risk factor.

### Integration with Deep-Verify Theorems

| Deep-Verify Theorem | Risk Implication |
|---------------------|-----------------|
| **FLP** (async consensus impossible with failures) | Any claim of reliable distributed consensus under network partition = hidden risk |
| **CAP** (pick 2 of 3) | System claiming C+A+P = unidentified trade-off hiding in design |
| **Halting Problem** | Guaranteed termination of arbitrary computation = impossible claim |
| **Arrow's Theorem** | No voting system satisfies all fairness criteria simultaneously |
| **No-Free-Lunch** | No optimizer is universally best = risk of wrong algorithm choice |

---

## Philosophy

### Core Principles

1. **Risks are not independent.** The most dangerous risks are correlated — they materialize together and compound each other. Analyzing risks in isolation is a classic failure mode.

2. **Probability × Impact is necessary but insufficient.** Velocity (how fast), detectability (will we see it), reversibility (can we recover), and ergodicity (can we survive) complete the picture.

3. **The most dangerous risks are the ones you haven't identified.** The framework invests heavily in multiple complementary discovery methods — vertical AND horizontal.

4. **Different uncertainty types need different responses.** Epistemic uncertainty (we don't know but could) → reduce through investigation. Aleatoric uncertainty (inherently random) → build resilience. Ambiguity (unclear question) → clarify before analyzing.

5. **Mitigation has costs — and sometimes creates NEW risks.** Every mitigation must pass a cost-benefit threshold AND a Cobra Effect check.

6. **Risk assessment decays.** A register from 3 months ago reflects a different reality. Gradual accumulation (Sorites) is as dangerous as sudden events.

7. **For non-ergodic risks, expected value is meaningless.** One irreversible catastrophe cannot be offset by many small gains. Survival comes first, optimization second.

### Integration with Deep-Explore / Deep-Verify

- Deep-Explore's **Assumption Stress Test (#23)** feeds IDENTIFY phase assumptions
- Deep-Explore's **Premortem (#21)** provides narrative failure scenarios
- Deep-Explore's **Dependency Analysis (#13)** maps inputs for dependency risk discovery
- Deep-Verify's **Definitional Contradiction (#154)** surfaces impossible requirements that are risk sources
- Deep-Verify's **Higher-Order Composition Gap (#166)** identifies emergent risks at abstraction boundaries
- Deep-Verify's **Constructive Counterexample (#165)** provides concrete attack vectors

---

## Phases

```
GROUND → IDENTIFY → QUANTIFY → INTERACT → MITIGATE → MONITOR
           ↑                                            |
           └──────────── META (continuous) ─────────────┘
```

| Phase | Goal | Methods | Key Output |
|-------|------|---------|------------|
| **GROUND** | Establish theoretical framing | 001–003 | System characterization, uncertainty map |
| **IDENTIFY** | Discover risks vertically and horizontally | 101–112 | Comprehensive risk inventory |
| **QUANTIFY** | Measure multi-dimensional severity | 201–207 | Scored risk register with fat-tail and ergodicity flags |
| **INTERACT** | Map risk correlations, cascades, and structural weaknesses | 301–307 | Risk network graph |
| **MITIGATE** | Design proportional responses, check for perverse effects | 401–408 | Mitigation portfolio |
| **MONITOR** | Build early warning and accumulation tracking systems | 501–505 | Living dashboard |
| **META** | Govern the process itself | 601–606 | Process health check |

---

## Phase 0: GROUND

*Goal: Before searching for risks, understand WHERE risks come from, WHAT types of uncertainty you face, and HOW your system's structure shapes its vulnerability profile. This phase is the theoretical lens through which all subsequent phases operate.*

---

### 001 — Risk Genesis Model

**What:** Systematically scan six fundamental sources from which ALL risks originate. Instead of searching for risks ad-hoc, use the genesis model as a generative framework — each source PRODUCES risks with predictable characteristics.

**The Six Sources:**

| Source | Mechanism | Risk Character | Detection Difficulty |
|--------|-----------|---------------|---------------------|
| **Complexity** | Emergent behavior, non-linearity, unpredictable interactions between components | Surprising, novel, hard to reproduce | HIGH — emerges only in combination |
| **Coupling** | Propagation, cascade, shared dependencies, tight feedback loops | Fast-moving, amplifying, chain reactions | MEDIUM — visible in architecture |
| **Uncertainty** | Incomplete information, volatility, unknowable futures | Probabilistic, potentially fat-tailed | VARIES — epistemic is reducible, aleatoric is not |
| **Agency** | Adversarial action, negligence, misaligned incentives, human error | Intentional or negligent, exploits weaknesses | HIGH — adversaries adapt |
| **Temporality** | Erosion, drift, accumulation, decay, technical debt, entropy | Gradual, invisible until threshold, boiling frog | VERY HIGH — each increment is small |
| **Boundaries** | Interface mismatches, handoff failures, translation errors, trust boundaries | Appears at edges between components/teams/phases | HIGH — each side thinks the other handles it |

**Process:**
1. For each of the six sources: "How does THIS source manifest in THIS project/decision?"
2. Generate at least 2 risks per source (empty source = blind spot, investigate harder)
3. Tag each risk with its genesis source — this determines which QUANTIFY and MITIGATE methods are most appropriate

**Why genesis matters for response:**
- Complexity risks → build resilience, can't predict specific failure
- Coupling risks → decouple, add circuit breakers, increase slack
- Uncertainty risks → classify (Knight) and respond per type (#002)
- Agency risks → threat model, align incentives, verify
- Temporality risks → monitor trends not events, set degradation thresholds
- Boundary risks → explicit contracts, integration tests, shared mental models

**Output:** `genesis_risks[] → {source, mechanism, risk_description, detection_difficulty, recommended_response_type}`

---

### 002 — Uncertainty Classification

**What:** Classify every identified uncertainty into its fundamental type using Knight's distinction. This is critical because different types of uncertainty require fundamentally different management strategies — applying the wrong strategy is itself a risk.

**Classification Matrix:**

| Type | You Know... | Management Strategy | Anti-Pattern |
|------|------------|--------------------|----|
| **Risk** (known distribution) | Probability AND impact range | Calculate expected value, insure, hedge, provision reserves | Treating as uncertainty (over-investigating what's already quantifiable) |
| **Uncertainty** (unknown distribution) | That you don't know, but not the probabilities | Scenario planning, real options, build optionality, defer commitment | Treating as risk (assigning false probabilities, creating illusion of control) |
| **Ambiguity** (unclear question) | Not even what the question means | Clarify, decompose, define terms, align stakeholders | Treating as uncertainty (analyzing an unclear question produces garbage) |

**Sub-classification for Risk and Uncertainty:**

| Sub-type | Definition | Example | Response |
|----------|-----------|---------|----------|
| **Aleatoric** (inherent randomness) | Cannot be reduced by more information | Server hardware failure rate | Build resilience, redundancy |
| **Epistemic** (knowledge gap) | CAN be reduced by investigation | "Will the API handle our load?" | Investigate, prototype, test, ask |

**Process:**
1. For every risk identified in any phase: classify as Risk / Uncertainty / Ambiguity
2. For Risk and Uncertainty: sub-classify as Aleatoric / Epistemic
3. Check: are you applying the RIGHT management strategy for the type?
4. **Red flag:** Assigning P=3 to something that is fundamentally uncertain (unknown distribution). This is faux precision — worse than admitting "we don't know" because it creates false confidence.

**Rumsfeld Matrix (expanded):**

| | **Known** | **Unknown** |
|---|---|---|
| **Known** | *Known knowns* — facts in your risk register. Manage directly. | *Known unknowns* — you know what you don't know. Investigate or hedge. |
| **Unknown** | *Unknown knowns* — organizational denial, willful blindness, taboo risks. **Most dangerous because addressable but ignored.** | *Unknown unknowns* — true surprises. Build general resilience, maintain reserves. |

**Output:** `classified_uncertainties[] → {risk_id, knight_type, aleatoric_or_epistemic, rumsfeld_quadrant, appropriate_strategy, current_strategy, strategy_mismatch_flag}`

---

### 003 — System Characterization (Perrow Matrix)

**What:** Assess the project/system's position on Perrow's two dimensions — complexity and coupling — to determine its inherent accident propensity. This sets expectations: in some systems, accidents are INEVITABLE and the goal shifts from prevention to survivability.

**Perrow Matrix:**

```
                    COUPLING
                    Loose           Tight
                ┌───────────┬───────────┐
    Linear      │  LOW RISK │  MODERATE │
COMPLEXITY      │  (simple  │  (fast    │
                │  + slack) │   but     │
                │           │   linear) │
                ├───────────┼───────────┤
    Complex     │  MODERATE │  NORMAL   │
    (non-       │  (complex │  ACCIDENTS│
     linear)    │   but     │  zone     │
                │   slack)  │  ← HERE   │
                └───────────┴───────────┘
```

**Complexity Indicators:**
- Many feedback loops
- Non-linear component interactions (output of A depends on state of B and C simultaneously)
- Multiple paths between components (hard to trace propagation)
- Components serve multiple functions (failure has non-obvious effects)
- Emergent properties not predictable from individual components

**Coupling Indicators:**
- Time-dependent processes (sequence matters, can't pause)
- Limited slack/buffer between stages
- One way to achieve goal (no substitution possible)
- Little redundancy (or redundancy is coupled — see #303)
- Fast propagation of effects through system

**Process:**
1. Score your system on complexity (1-5) and coupling (1-5)
2. Plot on Perrow matrix
3. If in "Normal Accidents Zone" (both ≥4):
   - Accept that some failures are inevitable
   - Shift investment from PREVENTION to DETECTION + RECOVERY + GRACEFUL DEGRADATION
   - Design for survivability, not perfection
4. Document: which subsystems are in which zone? (a system may span multiple zones)

**Output:** `system_profile → {complexity_score, coupling_score, perrow_zone, strategic_implication, subsystem_profiles[]}`

---

## Phase 1: IDENTIFY

*Goal: Systematically discover risks from multiple angles. Split into VERTICAL (deep within components) and HORIZONTAL (across boundaries). No single method catches everything — each has blind spots the others cover.*

### Vertical Extraction: Drilling Into Components

---

### 101 — Risk Taxonomy Scan

**What:** Systematic sweep across predefined risk categories to ensure no domain is overlooked. The taxonomy forces consideration of categories the team might naturally ignore.

**Taxonomy (adapt per context):**

| Category | Technical Examples | Business Examples |
|----------|-------------------|-------------------|
| **Architecture** | Single points of failure, scaling limits, tech debt | Vendor lock-in, platform dependency |
| **Data** | Corruption, loss, inconsistency, schema drift | Privacy breach, regulatory non-compliance |
| **Security** | Unauthorized access, injection, supply chain | Reputational damage, legal liability |
| **Operations** | Deployment failure, monitoring gaps, incident response | SLA breach, customer churn |
| **Dependency** | Library vulnerability, API deprecation, service outage | Vendor bankruptcy, contract termination |
| **People** | Key person dependency, skill gaps, turnover | Knowledge loss, hiring market shifts |
| **Regulatory** | Compliance gaps, audit failures | Fines, market access loss, forced changes |
| **Financial** | Cost overrun, resource constraints | ROI miss, budget cuts, currency risk |
| **Timeline** | Deadline miss, scope creep, integration delays | Market window miss, competitive response |
| **Strategic** | Wrong technology choice, wrong abstraction level | Wrong market, wrong timing, wrong positioning |

**Process:**
1. Walk through each category row
2. For each: "What could go wrong in THIS category for THIS project/decision?"
3. Generate at least 1 risk per category (empty category = blind spot, investigate)
4. Tag each with category AND genesis source from #001

**Output:** `risks[] → {id, category, genesis_source, description}`

---

### 102 — Failure Mode Enumeration

**What:** For each component, decision, or process step — systematically enumerate HOW it can fail. Adapted from FMEA but covering both technical and business contexts.

**Process:**
1. List all components/decisions/process steps
2. For each, ask three questions:
   - **How can this fail?** (failure modes)
   - **What happens when it fails?** (effects — local AND downstream)
   - **What causes this failure?** (root causes)
3. Distinguish failure MODES — this is critical because the mode determines the response:
   - **Total failure:** Component stops working entirely (usually detectable)
   - **Partial/degraded:** Works but below spec (harder to detect, may propagate bad data)
   - **Intermittent:** Fails sometimes, works sometimes (hardest to debug, may pass tests)
   - **Silent/undetected:** Produces wrong output with no error signal (**most dangerous**)
   - **Byzantine:** Appears to work to some observers, appears to fail to others (distributed systems)

**Technical example:**
```
Component: Delta Lake merge pipeline
├── Total: Cluster crash → Pipeline stops → Detectable, triggers alert
├── Partial: Merge timeout on large batches → Some records missing → Silent unless row count monitored
├── Intermittent: Concurrent write conflict → Non-deterministic duplicates → Passes individual tests
├── Silent: Schema drift in source → Wrong values in correct columns → No error, wrong downstream reports
└── Byzantine: Databricks UI shows success, but executor OOM killed mid-write → Partial parquet files
```

**Business example:**
```
Decision: Expand to new EU market
├── Total: Regulatory block → Cannot enter at all → Clear signal
├── Partial: GDPR requirements force feature removal → Reduced value proposition → Slow realization
├── Intermittent: Partner commitment varies → Unpredictable support → Hard to plan around
├── Silent: Cultural misread → Product adopted but for wrong use case → Metrics look OK, strategy fails
└── Byzantine: Local team reports success, HQ sees different numbers → Misaligned decisions
```

**Output:** `failure_modes[] → {component, mode_type, effect_local, effect_downstream, root_cause, detectability}`

---

### 103 — Threat Modeling (STRIDE+)

**What:** Structured adversarial analysis — what could a malicious or negligent actor do? Extended beyond traditional security STRIDE to include business and organizational threats.

**STRIDE+ Categories:**

| Threat | Technical | Business |
|--------|-----------|----------|
| **S**poofing | Identity impersonation, credential theft | Brand impersonation, fake partnerships |
| **T**ampering | Data modification, code injection | Contract manipulation, process subversion |
| **R**epudiation | Log deletion, untraceable actions | Deniable commitments, verbal-only agreements |
| **I**nformation Disclosure | Data leak, side-channel attack | Competitive intelligence leak, insider trading |
| **D**enial of Service | DDoS, resource exhaustion, rate limits | Key person unavailability, budget freeze, decision paralysis |
| **E**levation of Privilege | Auth bypass, role escalation | Scope creep, unauthorized decision-making |

**Process:**
1. Define trust boundaries (who/what is inside vs outside)
2. For each boundary crossing, apply STRIDE+ categories
3. For each threat: define attacker motivation, capability, and access
4. Rate: motivation × capability × access = threat level
5. Note: agency risks (#001) live here — misaligned incentives create "adversaries" even among partners

**Output:** `threats[] → {boundary, stride_category, scenario, attacker_profile, threat_level}`

---

### 104 — Dependency Risk Discovery

**What:** Map ALL external dependencies and assess each as a risk source. Dependencies are the #1 blind spot — teams treat them as stable when they're the most volatile risk source.

**Dependency Types:**

| Type | Examples | Risk Pattern |
|------|----------|-------------|
| **Vendor/Service** | Cloud provider, SaaS API, payment processor | Outage, price hike, deprecation, acquisition |
| **Library/Package** | npm packages, Python libs, OS packages | Vulnerability, abandonment, breaking change |
| **Data** | External data feeds, shared databases, APIs | Schema change, quality degradation, access revocation |
| **People** | Key engineer, domain expert, single approver | Departure, illness, bottleneck, burnout |
| **Infrastructure** | DNS, certificates, domains, credentials | Expiry, misconfiguration, provider change |
| **Organizational** | Budget approval, legal review, partner agreement | Delay, rejection, renegotiation |
| **Knowledge** | Undocumented processes, tribal knowledge | Loss on departure, inconsistent execution |

**Process:**
1. List every external dependency (be exhaustive — check build files, CI/CD, DNS, certificates, APIs)
2. For each: what is the **blast radius** if this dependency fails?
3. For each: what is the **substitution cost** — how hard to replace?
4. High blast radius + high substitution cost = CRITICAL dependency risk
5. Apply **Lindy Effect:** How old is this dependency? New dependencies have higher base-rate failure risk.
6. Check: are any dependencies shared between "redundant" systems? (→ feeds into #303)

**Output:** `dependency_risks[] → {dependency, type, blast_radius, substitution_cost, age_lindy, criticality}`

---

### 105 — Assumption Torture

**What:** Graduated stress test of every assumption. Stronger than simple inversion — tests assumptions at increasing levels of wrongness to discover where the breaking point is.

*Upgraded from v1 using the graduated approach from catalog method #130.*

**Process:**
1. Collect all assumptions from:
   - Deep-Explore output (especially Assumption Stress Test #23)
   - Deep-Verify output (claims marked "unsubstantiated" by #163)
   - Implicit assumptions in architecture, timeline, budget, team composition
2. For each assumption, test at three levels:
   - **10% wrong:** Assumption mostly holds but slightly off. What adjustments needed?
   - **50% wrong:** Assumption significantly off. What breaks? What survives?
   - **100% wrong:** Assumption completely inverted. What is the catastrophe? Is it survivable?
3. Classify each assumption:
   - **Robust:** System survives even at 100% wrong (good)
   - **Sensitive:** Breaks between 10-50% wrong (needs monitoring)
   - **Brittle:** Breaks at 10% wrong (CRITICAL — needs mitigation or elimination)
4. Define the **trigger condition** for each — what observable event indicates the assumption is failing?

**Example:**
```
Assumption: "Azure Databricks will auto-scale for our workload"
├── 10% wrong: Occasional scaling delay, 5-min queue time → ADD: pre-scaling schedule for known peaks
├── 50% wrong: Regular scaling failures during peak → BREAKS: SLA for report delivery
├── 100% wrong: Cluster cannot handle workload at all → CATASTROPHE: complete pipeline failure
└── Classification: SENSITIVE (breaks at ~30% wrong). Trigger: queue time >2min sustained.
```

**Output:** `assumption_tests[] → {assumption, at_10pct, at_50pct, at_100pct, classification, breaking_point, trigger}`

---

### 106 — Historical Pattern Matching (Survivorship-Corrected)

**What:** Search for analogies from past projects, industry incidents, and known anti-patterns — while actively correcting for survivorship bias.

**Pattern Libraries to Check:**

| Domain | Known Failure Patterns |
|--------|----------------------|
| **Data Engineering** | Schema drift, silent corruption, pipeline backpressure, zombie jobs, merge storms, credential expiry, cost explosion |
| **Cloud Architecture** | Region outage, cold start cascades, noisy neighbor, terraform state drift, quota exhaustion |
| **Enterprise Integration** | API version mismatch, timeout cascading, retry storms, data format evolution, certificate expiry |
| **Project Management** | 90% done syndrome, integration hell, second system effect, scope creep, Brooks's law |
| **Business Strategy** | Innovator's dilemma, winner's curse, premature scaling, platform dependency trap |
| **Security** | Supply chain attack, credential stuffing, privilege escalation, insider threat, dependency confusion |

**Survivorship Correction:**
After matching patterns, explicitly ask:
- "How many projects/companies failed this exact way and we never heard about it?"
- "Are we only seeing the patterns of those who survived? What patterns killed the others?"
- "What does the BASE RATE of failure look like for this type of project?" (→ feeds into #204)

**Process:**
1. Describe the project/decision in one paragraph
2. Search pattern libraries: "What historical failures look similar?"
3. For each match: root cause, warning signs, outcome
4. Apply survivorship correction: adjust confidence upward (things are probably worse than case studies suggest)
5. Assess: are we repeating any of these patterns?

**Output:** `pattern_matches[] → {pattern_name, similarity, historical_outcome, our_exposure, survivorship_adjustment}`

---

### 107 — Contraposition Failure Guarantee

**What:** Instead of asking "what leads to success," ask "what GUARANTEES failure?" then check if the current plan does any of those things. Based on logical contraposition: if A→B, then ¬B→¬A. Finding guaranteed failure conditions is often easier and more rigorous than finding success conditions.

*From catalog method #109, with theorem integration.*

**Process:**
1. Define the project/decision's success criteria
2. Invert: "What would GUARANTEE this fails?" Generate at least 10 failure guarantees
3. For each: check if the current plan, architecture, or strategy contains this anti-pattern
4. Where known theorems apply, these are PROVEN failure guarantees:
   - Async consensus + crash failures + no synchrony → FLP violation (GUARANTEED deadlock possible)
   - Full consistency + full availability + partition tolerance → CAP violation (GUARANTEED trade-off)
   - Universal termination checker → Halting problem violation (GUARANTEED undecidable)
   - Strategy-proof + individually rational + efficient + budget balanced → M-S violation (GUARANTEED impossible)
5. For practical failure guarantees:
   - No testing + production deployment → GUARANTEED bugs in production
   - Single person knows critical process + no documentation → GUARANTEED knowledge loss on departure
   - No monitoring + distributed system → GUARANTEED undetected failures

**Output:** `failure_guarantees[] → {guarantee, theorem_or_empirical, present_in_plan, severity, remediation}`

---

### Horizontal Extraction: Scanning Across Boundaries

---

### 108 — Boundary Risk Scan

**What:** Systematically identify risks that live AT BOUNDARIES between components, teams, phases, or organizations. These risks are invisible to vertical analysis because each side assumes the other handles them.

**Boundary Types:**

| Boundary | Where risks hide |
|----------|-----------------|
| **Component interfaces** | API contracts, data format assumptions, error handling expectations |
| **Team handoffs** | Responsibility gaps, assumption mismatches, communication failures |
| **Phase transitions** | Dev→QA→Prod, design→implementation, POC→production |
| **Organizational edges** | Client↔vendor, team↔team, company↔regulator |
| **Temporal boundaries** | Shift changes, sprint boundaries, fiscal year transitions |
| **Trust boundaries** | Internal↔external, authenticated↔anonymous, secure↔insecure |

**Process:**
1. Map ALL boundaries in the system/project (draw them explicitly)
2. For each boundary, apply the **Handoff Triad:**
   - **What does Side A ASSUME Side B provides?** (format, quality, timing, error handling)
   - **What does Side B ASSUME Side A has done?** (validation, authorization, completeness)
   - **Are these assumptions WRITTEN DOWN and AGREED?** (verbal = risk, documented = less risk)
3. Where assumptions don't match = **boundary risk**
4. Where assumptions aren't documented = **latent boundary risk** (will surface under stress)

**Why vertical methods miss this:**
Failure Mode Enumeration (#102) asks "how can THIS component fail?" But many failures aren't IN components — they're BETWEEN them. Component A works perfectly. Component B works perfectly. A→B fails because A outputs ISO dates and B expects Unix timestamps. Neither component "failed."

**Example:**
```
Boundary: Databricks pipeline → Synapse Serverless SQL
├── A assumes: Delta tables are always available for Synapse to query
├── B assumes: Queries will complete within serverless timeout
├── Mismatch: Large Delta tables with many small files → Synapse serverless times out
├── Neither side "fails" — the boundary fails
├── Documented? NO — discovered in production
└── RISK: Silent query timeout → stale dashboard → wrong business decisions
```

**Output:** `boundary_risks[] → {boundary_type, side_a_assumption, side_b_assumption, mismatch, documented, risk_description}`

---

### 109 — Blind Spot Interrogation

**What:** Deliberately search for risks the team is psychologically or structurally unable to see. Extended with the Unknown Knowns concept — things the organization knows but denies.

**Blind Spot Categories:**

| Blind Spot Type | Detection Question |
|-----------------|-------------------|
| **Expertise Gap** | What domain knowledge is missing? What would a specialist in [X] flag? |
| **Normalcy Bias** | What are we assuming will continue because it always has? |
| **Success Bias** | What risks are we ignoring because current approach "has always worked"? |
| **Proximity Bias** | What risks are we downplaying because they seem distant? |
| **Complexity Hiding** | Where is complexity swept under abstractions? (cf. Deep-Verify #166) |
| **Incentive Misalignment** | Who benefits from NOT seeing certain risks? |
| **Asymmetric Information** | Who knows something we don't? Vendor, client, regulator? |
| **Unknown Knowns** | What does the organization KNOW but refuses to acknowledge? What are the taboo topics? What would get you fired for raising? **These are the most dangerous blind spots because they are actionable but suppressed.** |
| **Survivorship Bias** | What similar projects failed silently? Are we only learning from survivors? |

**Process:**
1. Walk through each blind spot type
2. For each: "Who on the team would be LEAST likely to raise this?" (that's where blind spots live)
3. For Unknown Knowns specifically: "What risk would a departing employee mention in their exit interview but never in a sprint review?"
4. Explicitly invite adversarial perspectives: "If trying to sabotage this project, what would you exploit?"

**Output:** `blind_spots[] → {type, hypothesis, confidence, investigation_needed, taboo_flag}`

---

### 110 — Chaos Probe Design

**What:** Design controlled experiments that EMPIRICALLY discover risks by deliberately injecting failures. All other IDENTIFY methods are analytical (thinking about what could go wrong). This is the only method that TESTS what actually goes wrong.

*Adapted from catalog method #39 (Chaos Engineering).*

**Process:**
1. Define the **steady state** — what does "system working correctly" look like in measurable terms?
2. For each critical component/dependency: design a probe:
   - **What to break:** Kill process, inject latency, corrupt data, exhaust memory, revoke credentials
   - **Blast radius control:** Can you limit the impact? (feature flags, canary, staging environment)
   - **Observation plan:** What will you measure? How will you know if the system handled it?
   - **Abort criteria:** When do you stop the experiment?
3. Run probes (start in non-production, graduate to production with controls)
4. Document: what actually happened vs what you expected
5. Every UNEXPECTED result = discovered risk

**Why this matters:**
Analytical methods suffer from imagination limits — you can only find risks you can think of. Chaos probes find risks you COULDN'T think of because they let the system reveal its own failure modes.

**Probe Examples:**
```
Probe 1: Kill a Databricks executor mid-merge
├── Expected: Spark retry handles it, merge completes
├── Actual: ???? (might find: partial write, orphaned files, corrupt checkpoint)

Probe 2: Inject 30-second latency to source API
├── Expected: Pipeline retries with backoff
├── Actual: ???? (might find: timeout cascade, connection pool exhaustion)

Probe 3: Feed malformed schema to validation layer
├── Expected: Validation rejects, alert fires
├── Actual: ???? (might find: validation passes null columns, silent data loss)
```

**Output:** `chaos_probes[] → {probe_name, what_to_break, expected_result, actual_result, discovered_risks[], blast_radius_control}`

---

### 111 — Temporal Risk Archaeology

**What:** Explicitly search for risks created by TIME — erosion, drift, accumulation, decay, and entropy. These risks are invisible in point-in-time analysis because each increment is negligible. Only the accumulated effect is catastrophic.

*Grounded in genesis source "Temporality" from #001 and the Sorites paradox.*

**Process:**
1. For each component/process/relationship, ask:
   - **What is slowly degrading?** (performance, data quality, test coverage, documentation accuracy)
   - **What is slowly accumulating?** (technical debt, configuration drift, permission creep, complexity)
   - **What is slowly expiring?** (certificates, contracts, vendor relationships, team knowledge, technology relevance)
   - **What worked N months ago but hasn't been re-validated?** (assumptions, capacity estimates, SLA compliance)
2. For each temporal risk: estimate the **current accumulated state** vs the **threshold where it becomes critical**
3. Plot: time-to-threshold for each — which hits first?
4. Key insight: the trigger for temporal risks is NOT an event — it's the ABSENCE of an event (no one checked, no one updated, no one noticed)

**Examples:**
```
Drift: Terraform state vs actual Azure infrastructure
├── Each manual change adds tiny drift
├── After 6 months: state file doesn't match reality
├── Threshold: next terraform apply DESTROYS resources it doesn't know about
├── Time-to-threshold: unknown (no one is measuring drift)

Accumulation: Technical debt in PySpark pipeline
├── Each "quick fix" adds complexity
├── After 12 months: pipeline is unmaintainable
├── Threshold: new team member cannot understand code → key person dependency
├── Time-to-threshold: approaching (3rd developer couldn't onboard last quarter)
```

**Output:** `temporal_risks[] → {what_is_changing, direction, current_state, critical_threshold, estimated_time_to_threshold, monitoring_exists}`

---

### 112 — Scenario Planning Matrix

**What:** Construct structured scenarios from key uncertainties to identify risks that only emerge in specific futures. Not a single "what could go wrong" but "WHICH WORLD might we be in, and what are the risks in each?"

*Adapted from catalog method #69.*

**Process:**
1. Identify the 2 most impactful and most uncertain dimensions relevant to the project
2. Construct 2×2 matrix creating 4 distinct future scenarios
3. Name each scenario (makes them memorable and discussable)
4. For each scenario: what risks emerge that don't exist in other scenarios?
5. Assess: is your current plan robust across ALL 4 scenarios, or only 1-2?

**Example:**
```
Dimension 1: Data volume growth (LOW vs HIGH)
Dimension 2: Regulatory pressure (LOW vs HIGH)

┌─────────────────────────┬──────────────────────────┐
│  "Steady State"         │  "Compliance Storm"      │
│  Low volume + Low reg   │  Low volume + High reg   │
│  Risk: complacency,     │  Risk: overhead costs     │
│  underinvestment        │  exceed data value,       │
│                         │  talent drain to          │
│                         │  compliant competitors    │
├─────────────────────────┼──────────────────────────┤
│  "Data Explosion"       │  "Perfect Storm"         │
│  High volume + Low reg  │  High volume + High reg  │
│  Risk: scaling costs,   │  Risk: simultaneous      │
│  pipeline bottlenecks,  │  scaling + compliance     │
│  quality at scale       │  = resource impossible    │
└─────────────────────────┴──────────────────────────┘
```

6. Identify risks that appear in 3+ scenarios = HIGH PRIORITY (robust risks)
7. Identify risks unique to 1 scenario = CONDITIONAL (monitor for that scenario's indicators)

**Output:** `scenarios[] → {name, dimensions, risks_unique_to_scenario, robust_risks_across_scenarios, current_plan_robustness}`

---

## Phase 2: QUANTIFY

*Goal: Transform qualitative risk descriptions into multi-dimensional scores. Not just probability × impact — velocity, detectability, reversibility, AND ergodicity.*

---

### 201 — Five-Dimension Risk Scoring

**What:** Score each risk across five dimensions. Single-dimension scoring collapses critical information.

**Dimensions:**

| Dimension | Scale | Question |
|-----------|-------|----------|
| **Probability (P)** | 1-5 | How likely is this to occur? |
| **Impact (I)** | 1-5 | How severe are the consequences? |
| **Velocity (V)** | 1-5 | How fast does it materialize once triggered? (5=instant, 1=months) |
| **Detectability (D)** | 1-5 | How hard to detect BEFORE impact? (5=invisible, 1=obvious) |
| **Reversibility (R)** | 1-5 | How hard to recover? (5=permanent, 1=trivially undone) |

**Composite Score:**
```
Risk Score = P × I × max(V, D, R)
```

The `max()` captures the worst amplifier — invisible (D=5) OR irreversible (R=5) OR instant (V=5) fundamentally changes the character of the risk.

**Calibration Anchors (prevent score inflation):**

| Score | Probability | Impact |
|-------|------------|--------|
| 1 | <5% in project lifetime | Minor inconvenience, workaround exists |
| 2 | 5-20% | Noticeable delay or cost, contained |
| 3 | 20-50% | Significant — requires plan revision |
| 4 | 50-80% | Major — threatens project objectives |
| 5 | >80%, near-certain | Catastrophic — project failure, legal, safety |

**Fat-Tail Flag (from Theoretical Foundations):**
After scoring, check: is Impact ACTUALLY linear? Or is "Impact: 5" potentially 100× worse than "Impact: 4"? If yes, mark risk as **FAT-TAILED** — composite score is UNDERESTIMATE. Fat-tailed risks must be treated as special cases in MITIGATE phase (standard expected value doesn't work).

**Uncertainty Type Flag (from #002):**
If the risk was classified as Knight-Uncertainty (unknown distribution) or Ambiguity, the P score has LOW CONFIDENCE. Mark it. Do not treat a low-confidence P=2 the same as a high-confidence P=2.

**Output:** `scored_risks[] → {risk_id, P, I, V, D, R, composite, fat_tail_flag, confidence_flag, tier}`

---

### 202 — Exposure Window Analysis

**What:** Determine WHEN the system is vulnerable to each risk and for how long. Risks are not constant — they have windows of exposure that open and close.

**Process:**
1. For each risk:
   - **Opens:** When do we become vulnerable?
   - **Closes:** When does vulnerability end? (or: never?)
   - **Peak:** When is vulnerability highest?
2. Plot on project timeline
3. Identify **exposure concentrations** — periods where multiple windows overlap

**Example:**
```
Timeline: ─────────────────────────────────────────────────►
Risk A (data migration):     [████████]
Risk B (vendor dependency):       [██████████████████████████
Risk C (team capacity):    [████████████████]
Risk D (regulatory):                          [████████████
                                    ▲
                            PEAK: 4 risks overlap here
```

**Output:** `exposure_windows[] → {risk_id, opens, closes, peak, duration} + timeline visualization`

---

### 203 — Cost-of-Materialization Estimation

**What:** Estimate concrete cost if each risk materializes — forces specificity beyond vague "High impact" labels.

**Cost Categories:**

| Category | Estimation Method |
|----------|------------------|
| **Direct Financial** | Rework hours × rate, infrastructure costs, penalties, legal fees |
| **Time** | Schedule delay, critical path impact |
| **Opportunity** | Market window missed, deals lost, advantage eroded |
| **Reputation** | Customer trust, employer brand, partner confidence |
| **Technical Debt** | Workaround complexity, refactoring cost, maintenance burden |
| **Knowledge** | Information lost, learning wasted, decisions invalidated |

**Process:**
1. For each high-scoring risk: estimate costs in EACH relevant category
2. Three-point estimation: **best case** / **most likely** / **worst case**
3. Expected Cost = (best + 4×likely + worst) / 6
4. **Fat-tail adjustment:** If risk is fat-tailed (#201), the worst case is MORE likely than the formula assumes. Consider using percentile estimates (P90, P99) instead.

**Output:** `cost_estimates[] → {risk_id, category, best, likely, worst, expected, fat_tail_adjusted, confidence}`

---

### 204 — Precedent Probability Calibration

**What:** Calibrate probability using base rates from historical data and reference class forecasting. Counteracts optimism bias and planning fallacy.

**Process:**
1. For each risk: identify the **reference class** ("What type of event is this?")
2. Find base rate: "How often do events in this class actually occur?"
3. Adjust from base rate using project-specific factors (anchor to base rate, adjust conservatively)
4. Apply **survivorship correction** from #106: published base rates likely underestimate because failures are under-reported

**Reference Class Examples:**

| Risk Type | Base Rate | Source |
|-----------|----------|-------|
| Enterprise SW project >50% over budget | ~66% | Standish CHAOS, Flyvbjerg |
| Cloud major outage per region per year | ~2-4 | Public incident reports |
| Critical CVE in popular npm package/year | ~15-30 | NVD data |
| Key person departure within 12 months | ~15-25% | Industry turnover |
| Data breach per year (mid-size company) | ~10-15% | Verizon DBIR |

**Output:** `calibrated_risks[] → {risk_id, reference_class, base_rate, adjustment, calibrated_P, survivorship_correction}`

---

### 205 — Worst-Case Scenario Construction

**What:** For top-tier risks, construct full worst-case narratives. Ensures the team genuinely understands what their scores mean in human terms.

**Process:**
1. Select top 5-10 risks by composite score
2. For each, write a 3-5 sentence scenario: trigger → cascade → consequence → who is affected
3. Validate: "Is this plausible?" (avoid sci-fi)
4. Test: "Does our current plan survive this?" (if yes, scenario wasn't bad enough)
5. **Ergodicity check:** If this scenario materializes, can we continue operating? Or is it game over?

**Example:**
> *Risk: Delta merge storm during peak EPR reporting.*
> 50 concurrent notebooks write to the same Delta table during month-end close. Merge conflicts cascade, causing exponential retry growth. Cluster auto-scales to maximum within 2 hours, hitting cost ceiling. Pipeline stalls with partial writes. EPR submission deadline is in 4 hours. Manual resolution requires understanding the merge conflict graph — 6-8 hours. Regulatory deadline missed. Penalty: [amount]. Client escalation to VP level.

**Output:** `worst_cases[] → {risk_id, narrative, plausibility, ergodicity_flag, current_plan_survives}`

---

### 206 — Ergodicity Test

**What:** For each high-impact risk, test whether the standard risk score (Probability × Impact) is meaningful for a single pass through time, or only meaningful for an ensemble of parallel runs.

*Grounded in Peters' ergodicity economics — see Theoretical Foundations.*

**The Core Question:**
"If this risk materializes, can we recover and continue, or is it GAME OVER?"

**Process:**
1. For each risk with I≥4 or R≥4:
   - **Ensemble framing:** "Across 100 similar projects, X% would experience this." → Expected value calculation works.
   - **Time-series framing:** "For OUR ONE project, if this hits, what happens NEXT?" → If answer is "nothing, because project is dead" → expected value is MEANINGLESS.
2. Classify:
   - **Ergodic:** We can absorb this loss and continue. Standard scoring applies.
   - **Non-ergodic:** This loss is potentially fatal. **No amount of small wins compensates.** Must be treated as EXISTENTIAL regardless of probability.
3. For non-ergodic risks: traditional P×I optimization doesn't apply. Strategy shifts to:
   - AVOID the risk entirely if possible
   - LIMIT maximum exposure (position sizing, not expected value)
   - Ensure SURVIVAL first, optimize second

**Example:**
```
Risk: Client terminates contract (P:2, I:5, Composite: 50)
├── Ensemble: "20% of vendor contracts are terminated per year" → Plan for it
├── Time-series: "If Mars terminates, that's 60% of Lingaro's revenue from this team"
├── Ergodicity: NON-ERGODIC — team may not survive to get another client
├── Implication: P=2 doesn't make this "low priority." It must be treated as existential.
└── Strategy: Diversify client base (avoid), contract protections (transfer), not just "accept P=2"
```

**Output:** `ergodicity_tests[] → {risk_id, ensemble_framing, time_series_framing, ergodic_or_not, strategy_implication}`

---

### 207 — Stability Basin Mapping

**What:** Define the system's equilibrium state, then test how large a perturbation it can absorb before falling into a different (worse) equilibrium. Maps the "distance to cliff edge."

*Adapted from catalog method #67 (Stability Basin Analysis).*

**Concept:**
A marble in a bowl is stable — push it, it returns to center. But push it too hard, it leaves the bowl entirely and finds a new (possibly worse) resting place. Systems behave the same way: small perturbations → recovery, large perturbations → new (possibly catastrophic) state.

**Process:**
1. Define **equilibrium:** What does "system operating normally" look like in measurable terms?
2. Define **perturbations:** What forces push the system away from equilibrium? (Load spikes, team changes, budget cuts, data quality drops)
3. For each perturbation, classify the system's response:
   - **Stable:** System returns to equilibrium after perturbation stops. (Resilient)
   - **Marginal:** System oscillates or takes long to recover. (Warning zone)
   - **Unstable:** System falls into new state and doesn't return. (Catastrophe)
4. Find the **tipping points:** How large does each perturbation need to be before the system transitions from stable → marginal → unstable?
5. Measure: how close to each tipping point are we NOW?

**Example:**
```
Equilibrium: Pipeline processes 10M records/day within 4-hour window
├── +20% volume (12M): Stable — completes in 4.5 hours, recovers next day
├── +50% volume (15M): Marginal — completes in 7 hours, starts competing with next day's run
├── +100% volume (20M): Unstable — never catches up, backlog grows daily → NEW EQUILIBRIUM: permanently behind
└── Current state: 8M records/day. Distance to tipping: ~87% headroom. SAFE but monitor growth rate.
```

**Output:** `stability_basins[] → {equilibrium_definition, perturbation, stable_threshold, marginal_threshold, unstable_threshold, current_distance_to_tipping}`

---

## Phase 3: INTERACT

*Goal: Map how risks relate to each other. Individual risks are manageable — correlated, cascading, and concentrated risks are what cause catastrophic failures.*

---

### 301 — Risk Cascade Mapping

**What:** Trace how one risk materializing triggers or amplifies others. Build directed graphs of risk propagation.

**Process:**
1. For each risk pair: "If A materializes, does it increase probability or impact of B?"
2. If yes: mechanism and strength (weak/strong/certain)
3. Build directed graph: A → B
4. Find:
   - **Root risks:** High out-degree — mitigate these first (maximum cascade prevention)
   - **Terminal risks:** High in-degree — need robust defenses (many paths lead here)
   - **Chain risks:** A → B → C → ... → long propagation paths
   - **Amplification loops:** A → B → A (positive feedback, exponential escalation)

**Output:** `cascades[] → {source, target, mechanism, strength} + graph visualization`

---

### 302 — Risk Correlation Matrix

**What:** Identify which risks materialize SIMULTANEOUSLY — not because one causes another (#301) but because they share common drivers.

**Process:**
1. Build N×N matrix of risks
2. For each pair: "Could these hit at the same time? What common condition causes both?"
3. Mark: INDEPENDENT / CORRELATED / ANTI-CORRELATED
4. For correlated pairs: identify the common driver
5. Cluster correlated risks — they're a single "scenario" not independent events

**Critical Insight:**
If risks are correlated, P(A and B) >> P(A) × P(B). Most risk registers assume independence — this method breaks that dangerous assumption.

**Output:** `correlations[N×N] → {INDEPENDENT | CORRELATED | ANTI-CORRELATED, common_driver, cluster_id}`

---

### 303 — Common Mode Failure Detection

**What:** Find single points whose failure breaks multiple supposedly independent systems. The most dangerous pattern: N "redundant" things that all depend on one hidden thing.

**Process:**
1. List all "redundancies" and "backup systems"
2. For each pair of "independent" components: trace dependencies until you find shared infrastructure
3. Check across: infrastructure, data, people, process, vendor, knowledge
4. **Red Flag:** "We have redundancy" + shared underlying dependency = **false redundancy**
5. Apply **Swiss Cheese Model:** Are the holes in your defense layers correlated? (Same vendor runs primary and backup? Same person maintains both? Same CI/CD pipeline deploys both?)

**Output:** `common_modes[] → {shared_dependency, affected_components[], false_redundancy_flag, blast_radius}`

---

### 304 — Concentration Risk Detection

**What:** Identify excessive dependency on any single entity. Concentration is the meta-risk that amplifies all other risks.

**Concentration Dimensions:**

| Dimension | Question | Threshold |
|-----------|----------|-----------|
| **Vendor** | What % of critical functions depend on one vendor? | >60% = HIGH |
| **Person** | What functions only one person can perform? | Any = HIGH |
| **Technology** | Migration cost to alternative? | >6 months = HIGH |
| **Geographic** | All resources in one region/country? | All in one = HIGH |
| **Temporal** | Many critical events on one deadline? | >3 concurrent = HIGH |
| **Financial** | Revenue from one client/product? | >40% = HIGH |
| **Knowledge** | Critical knowledge documented? | Undocumented = HIGH |

**Output:** `concentrations[] → {dimension, single_point, dependency_%, failure_impact, diversification_options}`

---

### 305 — Compound Risk Scenarios

**What:** Construct realistic scenarios where multiple individually-acceptable risks combine for catastrophic outcomes. Tests the risk PORTFOLIO, not individual risks.

**Process:**
1. Take top 3-5 correlated clusters from #302
2. Construct compound scenario: "What if ALL of these hit simultaneously?"
3. Assess: additive (sum of individual impacts) or multiplicative (much worse)?
4. Test: do current mitigations hold under compound stress?
5. Apply **Normal Accident Theory:** If your system is complex + tightly coupled (#003), compound scenarios are not hypothetical — they are EXPECTED.

**Output:** `compound_scenarios[] → {cluster, narrative, additive_impact, compound_impact, non_linearity_factor, perrow_expected}`

---

### 306 — Critical Path Severance (Min-Cut Analysis)

**What:** Model the system as a flow graph and find the minimum cut — the smallest set of elements whose simultaneous failure disconnects the system entirely. Mathematical rigor for finding single points of failure.

*Adapted from catalog method #68.*

**Process:**
1. Model system as directed graph: nodes = components, edges = dependencies/data flows
2. Define source (inputs) and sink (outputs/value delivery)
3. Compute **minimum cut:** smallest set of edges (or nodes) whose removal disconnects source from sink
4. Each element in the min-cut set is a **structural SPOF** — failure there severs the value chain
5. For each min-cut element: does redundancy exist? Is it real or false (#303)?
6. Design mitigations: add parallel paths to increase the min-cut size

**Why this beats ad-hoc SPOF hunting:**
You might miss a SPOF by intuition. Min-cut is mathematically complete — if there's a way to sever the system, this finds the cheapest one. That's exactly what an adversary or unlucky coincidence would exploit.

**Output:** `min_cut[] → {elements_in_cut, cut_size, redundancy_status, recommended_additions}`

---

### 307 — Risk Interaction Paradoxes

**What:** Check for paradoxical interactions where managing one risk CREATES or AMPLIFIES another — the risk management equivalent of Braess Paradox. This is the INTERACT-level version of what #407 (Cobra Effect) does at the individual mitigation level.

**Known Interaction Paradoxes:**

| Paradox | Mechanism | Example |
|---------|-----------|---------|
| **Safety-Liveness** | Making system safer (more checks) slows it down → deadline risk | Adding validation layers → pipeline too slow for SLA |
| **Security-Usability** | More security → more friction → users bypass security | Complex passwords → Post-it notes on monitors |
| **Consistency-Availability** | CAP theorem → can't maximize both | Strong consistency → system unavailable during partitions |
| **Efficiency-Resilience** | Optimizing for efficiency removes slack needed for resilience | Just-in-time pipeline → no buffer for retries |
| **Transparency-Security** | More logging for transparency → more data to leak | Detailed audit logs contain sensitive information |
| **Simplicity-Completeness** | Simpler design → fewer edge cases handled | Minimal MVP → fails on real-world data variety |

**Process:**
1. For each pair of risk mitigations: does mitigating Risk A increase Risk B?
2. If yes: is the net effect positive or negative?
3. Where paradoxes exist: find the optimal trade-off point (not maximize one, not maximize other)

**Output:** `paradoxes[] → {risk_a, risk_b, paradox_type, mechanism, optimal_trade_off}`

---

## Phase 4: MITIGATE

*Goal: Design proportional, cost-effective responses. Not every risk needs mitigation — and over-mitigation is itself a risk. Check for perverse effects.*

---

### 401 — Four-T Classification

**What:** Classify each risk into a response strategy. Forces explicit decision rather than default tolerance.

| Strategy | When | Example |
|----------|------|---------|
| **Terminate** | Remove the risk source entirely | Don't use that vendor, don't enter that market |
| **Transfer** | Shift to someone better equipped | Insurance, SLA with penalties, outsource to specialist |
| **Treat** | Reduce probability or impact | Add monitoring, create backups, build redundancy |
| **Tolerate** | Accept consciously | Documented acceptance with owner and review date |

**Process:**
1. For each risk: evaluate all four strategies
2. **Non-ergodic risks (#206):** Terminate or Transfer strongly preferred. Tolerating existential risk requires extraordinary justification.
3. **Every Tolerate decision must have:** an owner, a review date, and a trigger that escalates to Treat/Terminate
4. Anti-pattern: "Tolerate by default" — unclassified risks are implicitly tolerated without decision

**Output:** `mitigations[] → {risk_id, strategy, rationale, owner, review_date, ergodicity_override}`

---

### 402 — Mitigation Cost-Benefit Analysis

**What:** Compare mitigation cost against expected loss. Prevents both under-investment and over-investment.

**Formula:**
```
Mitigation Value = (Expected Loss WITHOUT) - (Expected Loss WITH) - (Mitigation Cost)

Where:
  Expected Loss = P × I × Exposure Duration
  Mitigation Cost = Implementation + Ongoing + Opportunity Cost
```

**Fat-tail adjustment:** For fat-tailed risks, use P90/P99 impact instead of expected value. Expected value systematically underestimates fat-tailed risks.

**Non-ergodic override:** For non-ergodic risks (#206), cost-benefit analysis is secondary. The question isn't "is mitigation profitable?" but "can we survive without mitigation?"

**Output:** `cost_benefit[] → {risk_id, mitigation_cost, loss_reduction, net_value, fat_tail_adjusted, recommendation}`

---

### 403 — Defense in Depth Design (Swiss Cheese Validated)

**What:** For critical risks, design layered defenses where no single layer is sole protection. Validated against Swiss Cheese Model — layers must be INDEPENDENT.

**Layer Pattern:**
```
Layer 1: PREVENT   — Stop the risk from occurring
Layer 2: DETECT    — Identify early when it does occur
Layer 3: CONTAIN   — Limit the blast radius
Layer 4: RECOVER   — Restore normal operation
Layer 5: LEARN     — Prevent recurrence
```

**Swiss Cheese Validation (critical addition):**
After designing layers, check:
- Are any two layers maintained by the same person? → Correlated holes
- Do any two layers share infrastructure? → Common mode failure
- Can the same event disable multiple layers? → Correlated failure
- If Layer N fails SILENTLY, does Layer N+1 still detect? → Independence test

**Output:** `defense[] → {risk_id, layer, mechanism, independence_from_other_layers, silent_failure_detection}`

---

### 404 — Graceful Degradation Planning

**What:** Design how the system behaves when risks partially materialize. Maintain core value delivery under stress.

**Degradation Levels:**
- **Level 0: Normal** — everything works as designed
- **Level 1: Degraded** — non-critical features disabled, performance reduced, core works
- **Level 2: Emergency** — minimal viable operation only
- **Level 3: Controlled shutdown** — orderly stop, preserve data, communicate

**Process:**
1. Define the core value chain — what MUST keep working?
2. For each critical risk: which level does it trigger?
3. Define transitions: automated vs manual, who decides
4. **Test degradation paths** — most orgs have never actually tried running at Level 2

**Output:** `degradation[] → {risk_id, levels_0_through_3, transitions, decision_authority, tested}`

---

### 405 — Residual Risk Assessment

**What:** After designing mitigations, re-score each risk. Residual risk = actual risk carried. Must be explicitly accepted.

**Process:**
1. Re-apply Five-Dimension Scoring (#201) assuming mitigations in place
2. Compare original vs residual score
3. **For each residual risk:** explicit acceptance by risk owner
4. **Portfolio check:** does the collection of residual risks collectively exceed risk appetite? (Individual risks acceptable ≠ portfolio acceptable)
5. Re-check ergodicity: are any residual risks still non-ergodic? If so, are they truly Tolerable?

**Output:** `residual[] → {risk_id, original_score, residual_score, reduction_%, accepted_by, ergodicity_recheck}`

---

### 406 — Contingency Trigger Design

**What:** For tolerated/residual risks, define precise conditions that trigger escalation. Prevents "boiling frog" — gradual increase unnoticed until crisis.

**Process:**
1. For each: define **leading indicators** (early warning)
2. Set **thresholds** — specific, measurable, time-bound
3. Define **response protocol** — what, by whom, within what timeframe
4. Distinguish:
   - **Yellow:** Investigate and prepare (probability increasing)
   - **Red:** Execute contingency immediately (materializing now)

**Output:** `triggers[] → {risk_id, indicator, yellow_threshold, red_threshold, response_protocol, owner, timeframe}`

---

### 407 — Cobra Effect Check

**What:** For every proposed mitigation, explicitly check if it creates NEW risks worse than the original. The cure can be worse than the disease — and often is.

*Grounded in Cobra Effect and Braess Paradox — see Theoretical Foundations.*

**Process:**
1. For each mitigation in #401:
   - **What second-order effects does this mitigation create?**
   - **Who is affected beyond the original risk?**
   - **Does this mitigation create perverse incentives?**
   - **Does removing a constraint (or adding one) actually improve the system?**
2. Construct the causal chain: Mitigation → Intended effect → Second-order effects → Third-order effects
3. If second/third-order effects include NEW risks: assess these new risks with #201
4. If the new risk is worse than the original: REDESIGN the mitigation

**Examples:**
```
Mitigation: "Add comprehensive logging to detect data issues"
├── Intended: Better detectability for data quality risks
├── Second-order: Logs contain PII → new security/compliance risk
├── Third-order: Log volume → storage costs → cost-cutting → logging reduced → back to square one
└── COBRA EFFECT: Mitigation created privacy risk larger than original data quality risk

Mitigation: "Add approval gate before production deployment"
├── Intended: Reduce deployment risk
├── Second-order: Approval becomes bottleneck → deployments batch up → larger deployments
├── Third-order: Larger deployments = higher risk per deployment (exactly the opposite intent)
└── COBRA EFFECT: Safety measure increased average deployment risk

Mitigation: "Hire additional engineer for bus factor"
├── Intended: Reduce key-person dependency
├── Second-order: New hire requires 3 months of senior engineer's time for onboarding
├── Third-order: During onboarding, senior is less available → key-person risk INCREASES temporarily
└── NOT COBRA: Effect is temporary. But must manage the transition window.
```

**Output:** `cobra_checks[] → {mitigation_id, intended_effect, second_order, third_order, cobra_flag, redesign_needed}`

---

### 408 — Regret Minimization Framework

**What:** For irreversible decisions under uncertainty, apply regret minimization — project forward and ask which choice you'd regret more. Especially powerful when probability estimates are unreliable (Knight-Uncertainty).

*Adapted from catalog method #70.*

**Process:**
1. For decisions where #206 (Ergodicity Test) flagged non-ergodic risks:
2. For each option: project to 1 year, 3 years, 10 years from now
3. Ask: "Looking back, what would I regret NOT doing?"
4. Distinguish:
   - **Regret of action:** "I wish I hadn't done X" (usually fades — you learn from mistakes)
   - **Regret of inaction:** "I wish I had done X" (usually grows — missed opportunities haunt)
5. Choose the option that minimizes maximum regret (minimax regret)

**When to use:** When probability estimates are unreliable AND the decision is irreversible AND multiple options exist. For routine, reversible decisions, standard cost-benefit (#402) is sufficient.

**Output:** `regret_analysis[] → {decision, option, regret_of_action, regret_of_inaction, timeframe, minimax_choice}`

---

## Phase 5: MONITOR

*Goal: Build living risk surveillance. A register is a snapshot — monitoring makes it a movie. Track both sudden events AND gradual accumulation.*

---

### 501 — Leading Indicator Identification

**What:** For each risk, identify observable signals that PRECEDE materialization.

**Indicator Types:**

| Type | Example | Lead Time |
|------|---------|-----------|
| **Metric** | Error rate increasing 2× week-over-week | Days to weeks |
| **Event** | Competitor announces similar product | Weeks to months |
| **Behavioral** | Key stakeholder stops attending meetings | Days to weeks |
| **Environmental** | New regulation proposed in draft | Months |
| **Technical** | Dependency releases major version | Weeks |
| **Financial** | Burn rate exceeding forecast >20% | Weeks to months |
| **Temporal** | Certificate expiry in <30 days | Days (but predictable) |

**Process:**
1. For each risk: brainstorm 2-3 leading indicators
2. Assess: measurable? Available? How much lead time?
3. Design collection: automated (preferred) vs manual (schedule it)
4. **Goodhart check:** Can this indicator be gamed? If team is measured on "number of risks reported," they'll either over-report (noise) or under-report (fear). Design indicators that resist gaming.

**Output:** `indicators[] → {risk_id, indicator, type, lead_time, collection_method, goodhart_resistance}`

---

### 502 — Risk Review Cadence Design

**What:** Structured review schedule matching velocity and volatility of the risk portfolio.

| Risk Velocity | Review Frequency | Format |
|---------------|-----------------|--------|
| **Flash** (V=5) | Real-time alerting | Automated dashboard |
| **Fast** (V=4) | Weekly | 15-min standup addition |
| **Medium** (V=3) | Bi-weekly | Dedicated risk review |
| **Slow** (V=1-2) | Monthly / Quarterly | Strategic risk review |

**Output:** `review_schedule → {cadence, risks, participants, ritual, ad_hoc_triggers}`

---

### 503 — Escalation Protocol Design

**What:** Clear escalation paths — who decides what, when, with what authority.

| Level | Authority | Trigger |
|-------|----------|---------|
| **L0: Monitor** | IC | Indicators normal |
| **L1: Investigate** | Team lead | Yellow threshold crossed |
| **L2: Act** | PM/EM | Red threshold crossed |
| **L3: Escalate** | Director/VP | Impact > single team |
| **L4: Crisis** | Executive/steering | Multiple compound risks, existential |

**Output:** `escalation[] → {risk_id, L0_through_L4, info_required, max_response_time}`

---

### 504 — Post-Incident Feedback Loop

**What:** When a risk materializes (or nearly does), capture learnings and feed back into IDENTIFY. Closes the loop.

**Blameless Post-Mortem Template:**
```
1. TIMELINE: What happened, when?
2. DETECTION: How and when did we learn?
3. RESPONSE: What did we do? Per protocol?
4. ROOT CAUSE: Why? (5 whys)
5. RISK PROCESS AUDIT:
   - Was this in our register? (if no → IDENTIFY gap)
   - Was probability accurate? (if no → QUANTIFY gap)
   - Did we see cascades? (if no → INTERACT gap)
   - Did mitigation work? (if no → MITIGATE gap)
   - Did indicators fire? (if no → MONITOR gap)
6. ACTIONS: What changes to prevent recurrence?
```

**Output:** `learnings[] → {incident, phase_gaps, score_adjustments, process_improvements}`

---

### 505 — Sorites Accumulation Watch

**What:** Monitor for gradual, incremental risk accumulation that falls below event-detection thresholds. Each increment is negligible — the accumulated effect is catastrophic. The "boiling frog" detector.

*Grounded in the Sorites Paradox: when does one grain of sand become a heap? Adapted from catalog method #122.*

**The Problem:**
Event-based monitoring catches sudden changes. But many catastrophic failures are GRADUAL:
- Technical debt accumulates one shortcut at a time
- Data quality degrades one bad record at a time
- Performance declines one additional query at a time
- Security posture erodes one exception at a time
- Team morale drops one bad day at a time

No single increment triggers an alert. The accumulation crosses a threshold silently.

**Process:**
1. For each temporal risk identified in #111: define a **trend metric** (not just a threshold)
2. Track the DERIVATIVE, not just the value: is it getting worse over time?
3. Set **accumulation alerts:** triggered not by absolute value but by sustained directional trend
4. Define **periodic recalibration:** every N weeks, re-measure the baseline and ask "are we closer to the cliff than last time?"
5. Apply **Sorites Test:** Remove one element/increment — does it matter? No? Then you won't notice it. That's exactly why the accumulation is dangerous.

**Examples:**
```
Metric: Pipeline execution time
├── Value today: 3.2 hours (threshold: 4 hours) → No alert
├── Trend: +4 minutes/week for 8 weeks → ACCUMULATION ALERT
├── Projection: crosses threshold in 12 weeks
└── Action: investigate growth cause NOW, not in 12 weeks

Metric: Test coverage
├── Value today: 78% (threshold: 70%) → No alert
├── Trend: -0.5%/sprint for 6 sprints → ACCUMULATION ALERT
├── Projection: crosses threshold in 16 sprints
└── Action: address in next sprint, not when coverage hits 70%
```

**Output:** `accumulation_watches[] → {metric, current_value, threshold, trend, trend_duration, projected_threshold_crossing, action}`

---

## META Methods

*Applied continuously throughout all phases. Govern the risk assessment process itself.*

---

### 601 — Cognitive Bias Audit

**What:** Check the risk assessment itself for known cognitive biases.

| Bias | Distortion | Countermeasure |
|------|-----------|----------------|
| **Optimism** | Underestimate P(bad) | Use base rates (#204) |
| **Anchoring** | Over-weight first estimates | Independent re-estimation |
| **Availability** | Overweight recent/vivid risks | Systematic taxonomy (#101) |
| **Groupthink** | Team converges on comfortable assessment | Anonymous scoring |
| **Normalcy** | "It's always been fine" | Historical patterns (#106) |
| **Ostrich** | Avoid looking at uncomfortable risks | Blind spots (#109) |
| **Sunk Cost** | "We've invested too much to acknowledge this" | Pre-committed thresholds |
| **Dunning-Kruger** | Low-expertise areas get overconfident estimates | Explicit expertise gaps |
| **Confirmation** | See evidence supporting current plan, ignore contradicting | Contraposition (#107) |

**Output:** `bias_audit → {bias, affected_risks, score_adjustments}`

---

### 602 — Risk Appetite Calibration

**What:** Make explicit how much risk the team/org will accept — stated vs revealed appetite.

| Dimension | Conservative | Moderate | Aggressive |
|-----------|-------------|----------|------------|
| **Financial** | No risk of loss | Controlled risk | High risk/high return |
| **Timeline** | Buffer everywhere | Tight but achievable | Ambitious, accept slip |
| **Technical** | Proven only | Proven core, experimental edges | Cutting edge |
| **Reputation** | Zero incidents | Managed response | Move fast, apologize |
| **Regulatory** | Exceed requirements | Meet requirements | Minimum viable |

**Critical check:** Compare STATED appetite vs REVEALED appetite (what they actually do). The gap between these is itself a risk.

**Output:** `appetite → {dimension, stated, revealed, gap}`

---

### 603 — Portfolio Risk View

**What:** Aggregate all risks into portfolio view. Portfolio may be unacceptable even if every individual risk is acceptable.

**Portfolio Metrics:**

| Metric | Threshold |
|--------|-----------|
| **Total Expected Loss** | vs total budget/value |
| **Max Simultaneous Loss** (correlated clusters) | vs survivability |
| **Risk Concentration** (top 3 risks as % of total) | >60% = too concentrated |
| **Mitigation Coverage** (critical risks with DiD) | <80% = gap |
| **Monitoring Coverage** (risks with leading indicators) | <70% = blind flying |
| **Non-Ergodic Count** (risks that could end the game) | Any unmitigated = RED |
| **Fat-Tail Count** (risks with power-law impact) | Any unmitigated = RED |

**Output:** `portfolio → {metrics, visualization, acceptable_or_not, single_best_improvement}`

---

### 604 — Risk Communication Framework

**What:** Different stakeholders need different risk views.

| Audience | Needs | Format |
|----------|-------|--------|
| **Engineering** | Technical detail, actions | Detailed register, tickets |
| **PM/EM** | Priority, timeline impact | Top-10 dashboard |
| **Executives** | Business impact, strategic implications | Heat map, 3-bullet summary |
| **Client** | Assurance, material risks | Curated report |
| **Regulators** | Compliance evidence | Formal assessment |

**Output:** `communication → {audience, format, content_filter, frequency}`

---

### 605 — Simpson's Paradox Audit

**What:** Check if aggregate risk metrics hide dangerous subgroup patterns. A portfolio that looks healthy in aggregate may be catastrophic for specific clients, regions, or components.

*Adapted from catalog method #125.*

**Process:**
1. Take all aggregate risk metrics from #603
2. Disaggregate by: client, team, component, geography, time period
3. For each subgroup: do metrics still look acceptable?
4. If aggregate=GREEN but any subgroup=RED → Simpson's Paradox. The aggregate is LYING.

**Examples:**
```
Aggregate: "Average risk score across all components: 2.3" → Looks fine
├── Core pipeline: 1.2 → Fine
├── Authentication: 1.5 → Fine
├── EPR reporting module: 4.8 → CRITICAL
└── Simpson's Paradox: Aggregate hides that the regulatory-critical component is in crisis

Aggregate: "95% of deployments succeed" → Looks great
├── Monday-Thursday: 99% → Great
├── Friday: 72% → Terrible
└── Simpson's Paradox: Friday deploys are 4× riskier (different team? rushed for weekend?)
```

**Output:** `simpson_checks[] → {aggregate_metric, aggregate_value, subgroup, subgroup_value, paradox_detected, hidden_risk}`

---

### 606 — Goodhart's Law Check

**What:** Audit risk metrics and processes for signs they've become targets rather than measures — at which point they stop being useful.

*Grounded in Goodhart's Law — see Theoretical Foundations.*

**Warning Signs:**

| Signal | What it means |
|--------|--------------|
| **All metrics are green** | Either truly excellent OR metrics are being gamed |
| **Risk count never increases** | Either no new risks OR team stopped identifying |
| **All estimates are round numbers** | P=3, I=3, V=3 for everything → not actually estimating |
| **Reviews always take exactly the scheduled time** | Either perfectly calibrated OR rubber-stamped |
| **No risks are ever escalated** | Either nothing serious happens OR escalation is punished |
| **Mitigation completion is 100%** | Either excellent execution OR "done" ≠ "working" |

**Process:**
1. Examine each risk metric: could it be gamed?
2. Look for proxy failure: is the metric measuring what we ACTUALLY care about?
3. Check incentive alignment: what does the team get rewarded for? Does that align with honest risk reporting?
4. Rotate metrics periodically to prevent gaming

**Output:** `goodhart_audit[] → {metric, gaming_signal, proxy_validity, incentive_alignment, recommendation}`

---

## Method Summary

| # | Phase | Method | Core Question |
|---|-------|--------|---------------|
| 001 | GROUND | Risk Genesis Model | Where do risks come from? |
| 002 | GROUND | Uncertainty Classification | Risk vs Uncertainty vs Ambiguity? |
| 003 | GROUND | System Characterization | How accident-prone is this system? |
| 101 | IDENTIFY-V | Risk Taxonomy Scan | What categories apply? |
| 102 | IDENTIFY-V | Failure Mode Enumeration | How can each component fail? |
| 103 | IDENTIFY-V | Threat Modeling (STRIDE+) | What could an adversary do? |
| 104 | IDENTIFY-V | Dependency Risk Discovery | What external dependencies are fragile? |
| 105 | IDENTIFY-V | Assumption Torture | What if assumptions are wrong (10%/50%/100%)? |
| 106 | IDENTIFY-V | Historical Pattern Matching | What historical failures look like ours? |
| 107 | IDENTIFY-V | Contraposition Failure Guarantee | What guarantees failure? Are we doing it? |
| 108 | IDENTIFY-H | Boundary Risk Scan | What risks hide between components? |
| 109 | IDENTIFY-H | Blind Spot Interrogation | What can't we see? What do we deny? |
| 110 | IDENTIFY-H | Chaos Probe Design | What ACTUALLY breaks when we test? |
| 111 | IDENTIFY-H | Temporal Risk Archaeology | What is slowly degrading/accumulating? |
| 112 | IDENTIFY-H | Scenario Planning Matrix | What risks emerge in which futures? |
| 201 | QUANTIFY | Five-Dimension Scoring | P/I/V/D/R + fat-tail + confidence flags? |
| 202 | QUANTIFY | Exposure Window Analysis | When and how long are we vulnerable? |
| 203 | QUANTIFY | Cost-of-Materialization | What's the concrete cost if it hits? |
| 204 | QUANTIFY | Precedent Probability Calibration | What do base rates say? |
| 205 | QUANTIFY | Worst-Case Construction | What does "Impact: 5" actually look like? |
| 206 | QUANTIFY | Ergodicity Test | Can we survive this or is it game over? |
| 207 | QUANTIFY | Stability Basin Mapping | How far from the tipping point are we? |
| 301 | INTERACT | Risk Cascade Mapping | Which risks trigger others? |
| 302 | INTERACT | Risk Correlation Matrix | Which risks hit simultaneously? |
| 303 | INTERACT | Common Mode Failure | What hidden shared dependencies exist? |
| 304 | INTERACT | Concentration Risk Detection | Are we too dependent on single points? |
| 305 | INTERACT | Compound Risk Scenarios | What if multiple risks combine? |
| 306 | INTERACT | Critical Path Severance | What's the minimum cut to kill the system? |
| 307 | INTERACT | Risk Interaction Paradoxes | Does managing A amplify B? |
| 401 | MITIGATE | Four-T Classification | Terminate, Transfer, Treat, or Tolerate? |
| 402 | MITIGATE | Mitigation Cost-Benefit | Is the mitigation worth it? |
| 403 | MITIGATE | Defense in Depth (Swiss Cheese) | Are defenses layered AND independent? |
| 404 | MITIGATE | Graceful Degradation | How do we degrade, not collapse? |
| 405 | MITIGATE | Residual Risk Assessment | What remains after mitigation? |
| 406 | MITIGATE | Contingency Trigger Design | What triggers plan B? |
| 407 | MITIGATE | Cobra Effect Check | Does this mitigation create worse risks? |
| 408 | MITIGATE | Regret Minimization | For irreversible choices — what would we regret? |
| 501 | MONITOR | Leading Indicator ID | What signals precede the risk? |
| 502 | MONITOR | Review Cadence Design | How often do we re-assess? |
| 503 | MONITOR | Escalation Protocol | Who decides what, when? |
| 504 | MONITOR | Post-Incident Feedback | What did materialization teach us? |
| 505 | MONITOR | Sorites Accumulation Watch | Is gradual accumulation approaching threshold? |
| 601 | META | Cognitive Bias Audit | Is assessment distorted by bias? |
| 602 | META | Risk Appetite Calibration | How much risk will we accept? |
| 603 | META | Portfolio Risk View | Is total portfolio acceptable? |
| 604 | META | Risk Communication | Are right people seeing right risks? |
| 605 | META | Simpson's Paradox Audit | Does aggregate hide dangerous subgroups? |
| 606 | META | Goodhart's Law Check | Have metrics become gamed targets? |

**Total: 44 methods** (3 GROUND + 12 IDENTIFY + 7 QUANTIFY + 7 INTERACT + 8 MITIGATE + 5 MONITOR + 6 META)

---

## Usage Guide

### When to Use Deep-Risk

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **New project kickoff** | GROUND → full cycle | Full |
| **Architecture decision** | GROUND → IDENTIFY → QUANTIFY → MITIGATE | Focused |
| **Pre-release review** | IDENTIFY → INTERACT → MONITOR | Focused |
| **Post-incident review** | #504 → re-run relevant phases | Targeted |
| **Periodic risk review** | QUANTIFY (re-score) → INTERACT → MONITOR | Refresh |
| **Strategy/business decision** | GROUND → full cycle | Full |
| **Mitigation design review** | #407 Cobra Effect + #403 Swiss Cheese | Targeted |

### Integration with Deep-Explore and Deep-Verify

```
Deep-Explore (decision space)
     │
     ├── Options, assumptions, dependencies, stakeholders
     │
     ▼
Deep-Verify (correctness check)
     │
     ├── Validated claims, conflicts, impossible requirements
     │
     ▼
Deep-Risk (risk assessment)
     │
     ├── Risk register, mitigations, monitoring, escalation
     │
     ▼
Decision with full awareness:
  WHAT we can do (Explore) +
  WHETHER it's valid (Verify) +
  WHAT can go wrong (Risk)
```

### Scaling Deep-Risk

| Context | Methods | Time |
|---------|---------|------|
| **Quick** | #001 + #101 + #201 + #401 + #501 | 1-2 hours |
| **Standard** | GROUND + full IDENTIFY + QUANTIFY + MITIGATE core | Half day |
| **Comprehensive** | Full cycle including INTERACT + MONITOR | 1-2 days |
| **Critical** | Full cycle + META + stakeholder reviews + chaos probes | Multi-day |

### Phase 0 (GROUND) Guidance

GROUND is NOT optional overhead — it's the lens that makes everything else meaningful:
- Skip GROUND → you'll quantify uncertainty as risk (faux precision), miss temporal risks, misapply mitigations
- GROUND takes 30-60 minutes and saves hours of misdirected analysis
- In repeat assessments (same system, later date): revisit #003 only if system architecture changed

---

## Appendix A: Theoretical Foundation Quick Reference

| Principle | One-Line Summary | Where Applied |
|-----------|-----------------|---------------|
| **Normal Accidents (Perrow)** | Complex + coupled = accidents inevitable | #003, #305, #404 |
| **Non-Ergodicity (Peters)** | Can't average over what you only experience once | #206, #401, #408 |
| **Fat Tails (Taleb)** | Extremes dominate, means mislead | #201, #203, #402 |
| **Swiss Cheese (Reason)** | Aligned holes in layers = failure | #403, #303 |
| **Cobra Effect** | Intervention backfires | #407 |
| **Goodhart's Law** | Measured target → gamed target | #501, #606 |
| **Knight's Distinction** | Risk ≠ Uncertainty ≠ Ambiguity | #002, #201, #402 |
| **Survivorship Bias** | We only learn from visible failures | #106, #204 |
| **Lindy Effect** | Old = robust, new = fragile | #104, #111 |
| **Braess Paradox** | Adding capacity can reduce performance | #307, #407 |
| **Simpson's Paradox** | Aggregate hides subgroup patterns | #605 |
| **Sorites Paradox** | Gradual accumulation below threshold | #111, #505 |

## Appendix B: Output Templates

### Risk Register Entry
```
ID:           RISK-001
Title:        [Short name]
Category:     [From #101]
Genesis:      [Source from #001: Complexity/Coupling/Uncertainty/Agency/Temporality/Boundary]
Uncertainty:  [From #002: Risk/Uncertainty/Ambiguity × Aleatoric/Epistemic]
Description:  [What can go wrong]
Discovery:    [Which method found it: vertical/horizontal]
Scores:       P:_ I:_ V:_ D:_ R:_ Composite:_
Flags:        [Fat-tail? Non-ergodic? Low-confidence P?]
Cascades:     [→ triggers / ← triggered by]
Strategy:     [Terminate / Transfer / Treat / Tolerate]
Mitigation:   [Actions]
Cobra Check:  [Second-order effects of mitigation]
Owner:        [Person]
Indicators:   [Leading indicators + thresholds]
Review:       [Next date]
Accumulation: [Trend metric if temporal risk]
```

### Risk Dashboard (Portfolio View)
```
Total Risks:    [N] | Critical: [N] | High: [N] | Medium: [N] | Low: [N]
Non-Ergodic:    [N] unmitigated (EXISTENTIAL)
Fat-Tailed:     [N] unmitigated (UNDERESTIMATED)
Expected Loss:  [$X] | Max Simultaneous: [$Y] | Concentration: [%]
Top 3 Risks:    1. [___] 2. [___] 3. [___]
Overdue Reviews: [N] | Triggered Indicators: [N] | Accumulation Alerts: [N]
Coverage:       Mitigated: [%] | Monitored: [%] | DiD: [%] | Cobra-Checked: [%]
Simpson Check:  [Subgroups with score > aggregate + 2]
Goodhart Flag:  [Metrics showing gaming signals]
```

## Appendix C: Changes from v1

| Change | Rationale |
|--------|-----------|
| Added Phase GROUND (001-003) | Risk management needs theoretical foundation, not just operational methods |
| Split IDENTIFY into Vertical + Horizontal | Boundary risks invisible to component-focused analysis |
| Added Risk Genesis Model (#001) | Generative framework vs checklist — understands WHY risks exist |
| Added Uncertainty Classification (#002) | Different types need fundamentally different management |
| Added System Characterization (#003) | Perrow matrix determines if prevention or resilience is the right strategy |
| Upgraded Assumption Stress Test → Torture (#105) | Graduated testing (10/50/100% wrong) more rigorous than simple inversion |
| Added Contraposition Failure Guarantee (#107) | Logical rigor — finding guaranteed failures easier than guaranteed successes |
| Added Boundary Risk Scan (#108) | Closes the horizontal gap — risks between components, not within |
| Added Chaos Probe Design (#110) | Only empirical method — all others are analytical |
| Added Temporal Risk Archaeology (#111) | Catches gradual risks invisible to point-in-time analysis |
| Added Scenario Planning Matrix (#112) | Structured futures analysis, not just "what could go wrong" |
| Added Ergodicity Test (#206) | P×I meaningless for non-ergodic (irreversible) risks |
| Added Stability Basin Mapping (#207) | Quantifies "distance to cliff edge" |
| Added Critical Path Severance (#306) | Mathematical min-cut > intuitive SPOF hunting |
| Added Risk Interaction Paradoxes (#307) | Managing Risk A can amplify Risk B |
| Added Cobra Effect Check (#407) | Mitigations can backfire — must be checked |
| Added Regret Minimization (#408) | For irreversible decisions under uncertainty |
| Added Sorites Accumulation Watch (#505) | Monitors gradual accumulation below event thresholds |
| Added Simpson's Paradox Audit (#605) | Aggregate metrics can hide dangerous subgroups |
| Added Goodhart's Law Check (#606) | Risk metrics that become targets cease to measure risk |
| Fat-tail and confidence flags in scoring | P×I assumes normal distribution — flags where this breaks |
| Non-ergodic override in mitigation | Expected value optimization invalid for existential risks |
| Swiss Cheese validation in Defense-in-Depth | Layers must be independent — shared dependencies = false defense |
| Survivorship correction in pattern matching | Historical data biased toward survivors |
| Lindy Effect in dependency assessment | New = fragile, old = robust |
