# Deep-Synthesis: Systematic Knowledge Synthesis Methodology

## Overview

Deep-Synthesis is the fifth pillar of the Deep Analysis Framework — a pentad of complementary reasoning processes:

| Process | Question | Operation | Error Type |
|---------|----------|-----------|------------|
| **Deep-Explore** | *What can we do?* | Divergence — generate options | Missing options |
| **Deep-Verify** | *Is this correct?* | Validation — check truth | False validity |
| **Deep-Feasibility** | *Can we do it?* | Evaluation — assess executability | False feasibility |
| **Deep-Risk** | *What can go wrong?* | Probabilistic — assess threats | Underestimated danger |
| **Deep-Synthesis** | *What does it all MEAN?* | Integration — build understanding | **False coherence** |

**False coherence** is Deep-Synthesis's unique error type: believing you've created genuine understanding when you've actually:
- Imposed a pattern that doesn't exist (apophenia)
- Ignored contradicting evidence (confirmation bias)
- Confused correlation with causation (causal illusion)
- Overfitted a narrative to selective data (hindsight bias)
- Created an internally consistent but externally wrong model (beautiful theory, ugly facts)
- Synthesized at the wrong level of abstraction (ecological fallacy / atomistic fallacy)

---

## Why Synthesis Needs Its Own Process

Knowledge doesn't integrate itself. Having correct facts (Verify), feasible plans (Feasibility), and managed risks (Risk) does NOT mean you UNDERSTAND the situation. Understanding requires **active integration** — finding patterns across sources, resolving contradictions, detecting emergence, and building mental models that generate novel insight.

**The synthesis gap manifests as:**
- Teams with excellent data but poor decisions (data-rich, insight-poor)
- Reports that present information but don't conclude anything
- Expertise siloed by domain — no one sees the cross-domain pattern
- Analysis paralysis from too much unintegrated information
- "We knew all the pieces but didn't put them together" (every post-mortem of intelligence failure)

**What synthesis IS NOT:**
- **Not summarization** — summarization REDUCES information; synthesis CREATES new understanding
- **Not aggregation** — aggregation COMBINES data points; synthesis finds PATTERNS across them
- **Not consensus** — consensus averages opinions; synthesis resolves contradictions into higher-order insight
- **Not collection** — a binder of reports is not a synthesis; a framework that explains WHY the reports diverge IS

---

## Theoretical Foundations

### Epistemology — How Knowledge Is Created

**1. Hegel's Dialectic (1807)**
The foundational model of synthesis:
- **Thesis:** An initial position or claim
- **Antithesis:** A contradicting position or evidence
- **Synthesis:** A higher-order understanding that preserves the valid elements of both while transcending their contradiction

Implication: Contradiction is not a problem to eliminate — it is the ENGINE of synthesis. Sources that disagree are more valuable for synthesis than sources that agree.

**2. Piaget — Assimilation and Accommodation (1952)**
- **Assimilation:** Fitting new information into existing mental models
- **Accommodation:** Changing mental models to fit new information

Synthesis requires BOTH: assimilate when new knowledge fits, accommodate when it doesn't. The error: always assimilating (forcing new data into old framework) without ever accommodating (changing the framework itself).

**3. Bloom's Taxonomy — Revised (Anderson & Krathwohl, 2001)**
Synthesis operates at the highest cognitive levels:
```
Remember → Understand → Apply → Analyze → Evaluate → CREATE
                                                       ↑
                                              Synthesis lives here
```
Synthesis is not possible without prior analysis. The process must include analytical decomposition BEFORE integrative synthesis.

**4. Polanyi — Tacit Knowledge (1966)**
"We know more than we can tell." Some knowledge resists explicit articulation. Implications:
- Sources may contain tacit knowledge that isn't captured in their explicit claims
- Experts may synthesize intuitively but can't articulate the synthesis
- Deep-Synthesis must account for knowledge that exists between the lines

### Information Theory

**5. Shannon — Information Theory (1948)**
Information = surprise. A synthesis that merely repeats what sources say contains ZERO new information. A valid synthesis must produce statements that are NOT present in any single source but EMERGE from their combination.

**Test of genuine synthesis:** Can you derive insight X from source A alone? From source B alone? If yes to either, it's extraction, not synthesis. If it requires BOTH A and B, it's synthesis.

**6. Kolmogorov Complexity**
The shortest program that produces a dataset. Synthesis is a form of COMPRESSION — finding the simplest model that explains all the data. A good synthesis is shorter than the sum of its sources but contains their essential information.

**Anti-pattern:** Synthesis that is LONGER than the original sources has failed to compress — it's elaboration, not synthesis.

**7. Mutual Information**
Measures what two sources SHARE vs what's unique to each:
- High mutual information → sources agree → synthesis strengthens confidence
- Low mutual information → sources cover different territory → synthesis expands coverage
- Negative mutual information → sources contradict → synthesis must resolve

The MOST valuable synthesis opportunity exists where sources have SOME overlap (enough to bridge) but significant unique coverage (enough to add value).

### Cognitive Science

**8. Gentner — Structure Mapping Theory (1983)**
Analogical reasoning works by mapping STRUCTURAL relationships (not surface features) from a known domain to a new one. Synthesis between domains requires finding structural parallels — shared relationship patterns even when surface details differ.

Example: "Pipeline backpressure" (data engineering) maps structurally to "supply chain bottleneck" (logistics) — different surface, same structure. This structural mapping enables TRANSFER of solutions between domains.

**9. Fauconnier & Turner — Conceptual Blending (2002)**
Mental spaces from different domains can be blended into a NEW mental space that has emergent properties. The blend is not just A+B — it produces C that neither A nor B contains.

Four-space model:
```
Input Space 1    Input Space 2
     ↘              ↙
    Generic Space (shared structure)
           ↓
      Blended Space (novel insight)
```

This is the cognitive mechanism BEHIND synthesis. Deep-Synthesis must facilitate this blending process deliberately.

**10. Weick — Sensemaking (1995)**
Sensemaking is retrospective, social, ongoing, grounded in identity, focused on extracted cues, driven by plausibility rather than accuracy. Key insight: people don't DISCOVER meaning in data — they CONSTRUCT meaning from data. Synthesis is a constructive act.

Implication: The synthesizer's frame, identity, and prior knowledge SHAPE the synthesis. This is both a feature (expertise enables synthesis) and a bug (bias distorts synthesis).

**11. Peirce — Abductive Reasoning (1903)**
Three types of inference:
- **Deduction:** A + rule → conclusion (certain but no new knowledge)
- **Induction:** observations → generalization (probable but may be wrong)
- **Abduction:** observations → best explanation (creative, novel, but uncertain)

Synthesis primarily uses ABDUCTION — inferring the best explanation that accounts for all sources. This is the most creative but also the most fallible form of reasoning.

### Philosophy of Science

**12. Kuhn — Paradigm Shifts (1962)**
Normal science works within paradigms. Anomalies accumulate until a paradigm shift occurs. Sources from DIFFERENT paradigms are incommensurable — their terms mean different things.

Implication: When synthesizing across paradigms (e.g., waterfall project management literature + agile literature), recognize that the same words ("requirements," "plan," "delivery") may mean fundamentally different things. Synthesis across paradigms requires TRANSLATION before integration.

**13. Lakatos — Research Programmes (1978)**
Theories have a HARD CORE (unfalsifiable assumptions) and a PROTECTIVE BELT (auxiliary hypotheses that can be adjusted). When sources disagree, check: is the disagreement about the hard core (paradigm conflict) or the protective belt (adjustable difference)?

Synthesizing protective belt disagreements is straightforward. Hard core conflicts require paradigm-level synthesis (much harder, potentially revolutionary).

**14. Feyerabend — Methodological Pluralism (1975)**
"Against Method" — no single methodology is universally best. Synthesis of knowledge from different methodological traditions (quantitative + qualitative, empirical + theoretical, analytical + experiential) is MORE robust than any single tradition.

Implication: Diverse sources using different methods are MORE valuable for synthesis than many sources using the same method (methodological triangulation).

**15. Popper — Falsification (1934)**
A good theory is falsifiable — it makes predictions that could be wrong. A synthesis that explains EVERYTHING explains NOTHING (unfalsifiable). Good synthesis should generate testable predictions that could prove it wrong.

Test: What would DISPROVE this synthesis? If nothing could, it's narrative, not knowledge.

### Research Methodology

**16. Meta-Analysis (Glass, 1976)**
Statistical synthesis of multiple quantitative studies. Addresses the question: what does the BODY of evidence say, accounting for sample sizes, effect sizes, and study quality? Not all studies are equal — weight by quality and sample size.

Relevant even for non-statistical synthesis: weight sources by quality, not just count.

**17. Grounded Theory (Glaser & Strauss, 1967)**
Theory emerges from systematic analysis of data, not from imposing pre-existing theory onto data. Relevant to synthesis: let the PATTERN emerge from sources rather than imposing a pattern and finding confirming evidence.

Key method: **constant comparison** — each new piece of data is compared with all previous data to find emerging categories.

**18. Triangulation (Denzin, 1978)**
Using multiple data sources, methods, investigators, or theories to cross-validate findings. Types:
- **Data triangulation:** Multiple data sources on same phenomenon
- **Methodological triangulation:** Multiple methods studying same thing
- **Investigator triangulation:** Multiple researchers analyzing same data
- **Theory triangulation:** Multiple theoretical frameworks interpreting same data

Convergence across triangulation = HIGH confidence in synthesis. Divergence = need to understand why.

### Knowledge Management

**19. Nonaka & Takeuchi — SECI Model (1995)**
Knowledge creation spirals through four modes:
- **Socialization:** Tacit → Tacit (shared experience)
- **Externalization:** Tacit → Explicit (articulation)
- **Combination:** Explicit → Explicit (systematization — THIS IS SYNTHESIS)
- **Internalization:** Explicit → Tacit (learning by doing)

Deep-Synthesis operates primarily in the COMBINATION quadrant but must draw on Externalization (surfacing tacit knowledge) and should aim to produce knowledge that enables Internalization.

### Paradoxes & Traps of Synthesis

| Paradox | Mechanism | Synthesis Implication |
|---------|-----------|---------------------|
| **Simpson's Paradox** | Trend reverses when data disaggregated | Synthesis at wrong level produces wrong conclusion |
| **Ecological Fallacy** | Group-level pattern doesn't apply to individuals | Can't synthesize DOWN from aggregate to individual |
| **Atomistic Fallacy** | Individual pattern doesn't apply to group | Can't synthesize UP from individual to aggregate |
| **Frame Problem** | Infinite possible relevant context | Synthesis must BOUND what's relevant — but how? |
| **Duhem-Quine** | Can't test hypothesis in isolation | Sources carry hidden auxiliary assumptions |
| **Bonini's Paradox** | Model as complex as reality is useless | Synthesis simpler than sources or it's not synthesis |
| **McNamara Fallacy** | Only measuring what's measurable | Synthesis ignores what can't be quantified |
| **Streetlight Effect** | Searching where the light is | Synthesis from available sources, not relevant sources |
| **Narrative Fallacy** (Taleb) | Humans impose stories on random data | Synthesized narrative may be confabulation |
| **Apophenia** | Seeing patterns in noise | Synthesis may "discover" patterns that don't exist |
| **Curse of Knowledge** | Can't un-know what you know | Synthesizer's expertise creates blind spots |

---

## Philosophy

### Core Principles

1. **Synthesis creates knowledge.** A valid synthesis contains information not present in any individual source. If it doesn't, it's summarization, not synthesis.

2. **Contradiction is fuel, not failure.** Sources that disagree provide more synthesis value than sources that agree. Disagreement forces deeper understanding. (Hegel)

3. **The map is not the territory.** Every synthesis is a MODEL — useful but incomplete. Declare what the synthesis DOESN'T cover, not just what it does. (Korzybski)

4. **Level matters.** The SAME data synthesized at different levels of abstraction produces different (potentially contradictory) conclusions. Always specify the level. (Simpson, ecological/atomistic fallacy)

5. **Diverse sources > many similar sources.** Five sources from different methods/perspectives are more valuable than fifty sources from the same perspective. (Feyerabend, triangulation)

6. **Compression is the measure.** A good synthesis is SHORTER than its sources but captures their essential structure. If your synthesis is as long as the source material, you haven't synthesized. (Kolmogorov)

7. **Emergence is the goal.** The synthesis should contain insights that EMERGE from combining sources — things no single source stated but that become visible in combination.

8. **Falsifiability is the check.** A synthesis that explains everything explains nothing. State what would DISPROVE your synthesis. (Popper)

### Integration with Other Processes

Deep-Synthesis interacts with each other process in specific ways:

**Synthesis OF other process outputs:**
- Synthesize Explore options, Verify findings, Feasibility assessment, and Risk register into a unified decision basis
- This is the "final integration" use case

**Synthesis AS INPUT to other processes:**
- Synthesize domain knowledge before Exploring options
- Synthesize research before Verifying claims
- Synthesize case studies before assessing Feasibility
- Synthesize incident reports before assessing Risk

**Synthesis BETWEEN domains:**
- Synthesize technical and business knowledge for architecture decisions
- Synthesize research findings across disciplines for novel approaches
- Synthesize team experiences across projects for organizational learning

---

## Phases

```
SCOPE → ACQUIRE → DECOMPOSE → RELATE → INTEGRATE → CRYSTALLIZE
           ↑                                            |
           └──────────── META (continuous) ─────────────┘
```

| Phase | Goal | Methods | Key Output |
|-------|------|---------|------------|
| **SCOPE** | Define synthesis question, boundaries, and approach | 001–003 | Clear question, bounded domain |
| **ACQUIRE** | Gather diverse, quality sources | 101–105 | Source inventory with quality grades |
| **DECOMPOSE** | Extract atomic claims, models, and evidence | 201–206 | Structured knowledge atoms |
| **RELATE** | Map relationships between knowledge atoms | 301–308 | Relationship graph |
| **INTEGRATE** | Build unified understanding from relationships | 401–407 | Integrated framework |
| **CRYSTALLIZE** | Distill into communicable, actionable form | 501–505 | Models, principles, narratives |
| **META** | Validate synthesis quality and detect bias | 601–607 | Quality assurance |

---

## Phase 0: SCOPE

*Goal: Define WHAT you're synthesizing, WHY, for WHOM, and at what LEVEL of abstraction. Bounding the synthesis prevents infinite scope and the Frame Problem.*

---

### 001 — Synthesis Question Formulation

**What:** Articulate the specific question the synthesis must answer. "What do we know about X?" is too vague. A good synthesis question constrains the scope while enabling genuine integration.

**Good Synthesis Questions:**
- "What do the combined findings from our PoC, the vendor documentation, and the architecture review tell us about whether Delta Lake meets our needs?" → Specific, bounded, actionable
- "How do the principles of sustainable packaging design interact with EPR compliance requirements across EU markets?" → Cross-domain, bounded by topic
- "What patterns emerge from our last 5 project post-mortems that point to systemic issues?" → Multi-source, pattern-seeking

**Bad Synthesis Questions:**
- "What do we know?" → Unbounded
- "Summarize these documents" → Not synthesis, just summarization
- "Is this good?" → Too vague, not about knowledge integration

**Process:**
1. Draft the question
2. Check: Is it ANSWERABLE? (Not too broad, not too vague)
3. Check: Does it require MULTIPLE sources? (If one source answers it, you don't need synthesis)
4. Check: Does it seek INTEGRATION, not just collection? (Pattern, principle, framework — not list)
5. Define: What would a GOOD answer look like? What form? What level of detail?

**Output:** `synthesis_question → {question, answerable, multi_source, integration_type, answer_form}`

---

### 002 — Level-of-Analysis Selection

**What:** Explicitly choose the level of abstraction for synthesis. Different levels produce different (and potentially contradictory) conclusions. This prevents Simpson's Paradox, ecological fallacy, and atomistic fallacy.

**Levels:**

| Level | Abstraction | Example | Risk |
|-------|------------|---------|------|
| **Atomic** | Individual facts, events, data points | "Server X crashed at 14:32" | Atomistic fallacy — can't generalize |
| **Pattern** | Recurring relationships across atoms | "Crashes correlate with memory pressure" | Correlation ≠ causation |
| **Structural** | Underlying mechanisms and models | "Memory leak in service Y causes cascading failures" | Model may not match reality |
| **Systemic** | System-wide dynamics and behaviors | "Our incident response is reactive, not preventive" | Ecological fallacy — doesn't apply to every subsystem |
| **Paradigmatic** | Fundamental assumptions and worldviews | "We treat reliability as a feature, not a requirement" | Paradigm conflicts are hard to detect from inside |

**Process:**
1. What level does the synthesis question target?
2. What level do the sources operate at? (Sources at different levels need alignment)
3. Are there CROSS-LEVEL interactions? (Atomic detail that changes systemic understanding?)
4. **Declare the level explicitly** — and note when conclusions CANNOT be transferred to other levels

**Output:** `level_selection → {target_level, source_levels[], cross_level_interactions, transfer_limitations}`

---

### 003 — Source Landscape Mapping

**What:** Before gathering sources, map the LANDSCAPE of available knowledge. What types of sources exist? Where are the gaps? This prevents the Streetlight Effect (searching only where convenient).

**Source Types:**

| Type | Nature | Strength | Weakness |
|------|--------|----------|----------|
| **Empirical data** | Measurements, metrics, logs | Objective, quantifiable | May lack context |
| **Expert knowledge** | Specialist opinions, experience | Nuanced, contextual | Subject to bias |
| **Documented procedures** | Processes, runbooks, standards | Official, auditable | May not reflect reality |
| **Academic/research** | Papers, studies, reviews | Rigorous, peer-reviewed | May not be practical |
| **Experiential** | Lessons learned, post-mortems, war stories | Practical, real-world | Survivorship bias |
| **Theoretical** | Frameworks, models, theorems | General, principled | May not apply to specifics |
| **Tacit** | Undocumented "tribal" knowledge | Often the most critical | Hard to access, verify |
| **Cross-domain** | Knowledge from adjacent fields | Novel perspectives | Transfer may not hold |

**Process:**
1. For the synthesis question: which source types are RELEVANT?
2. Which are AVAILABLE?
3. Which are MISSING? (Gaps are as informative as sources)
4. **Diversity audit:** Are multiple perspectives represented? Multiple methods? Multiple domains?
5. **Streetlight check:** Are we looking where the knowledge IS, or only where it's convenient to look?

**Output:** `source_landscape → {type, available, relevant, gap, diversity_score, streetlight_risk}`

---

## Phase 1: ACQUIRE

*Goal: Gather diverse, quality-assessed sources. Not just "more sources" but the RIGHT sources — diverse in perspective, method, and domain.*

---

### 101 — Systematic Source Collection

**What:** Structured gathering of sources that covers the landscape mapped in #003. Ensures no major source type is missed.

**Process:**
1. From landscape map (#003): list all source types needed
2. For each type: identify specific sources
3. Prioritize: which sources are most likely to contribute to synthesis?
4. Include sources that are EXPECTED TO DISAGREE — these are the most valuable (Hegel)
5. Set a boundary: when to STOP collecting. More sources ≠ better synthesis after a saturation point.

**Saturation heuristic:** When new sources add information that is >80% redundant with what you already have, you've likely reached saturation. Exception: if a DISSENTING source exists, it's never redundant.

**Output:** `sources[] → {source_id, type, description, expected_contribution, expected_disagreement}`

---

### 102 — Source Quality Assessment

**What:** Not all sources are equal. Assess quality to weight contributions appropriately during synthesis. Poor-quality sources given equal weight distort synthesis.

**Quality Dimensions:**

| Dimension | Question | Rating |
|-----------|----------|--------|
| **Reliability** | Is the source consistently accurate? Track record? | H/M/L |
| **Validity** | Does it measure/describe what it claims to? | H/M/L |
| **Recency** | Is the information current? | H/M/L |
| **Methodology** | Was information gathered rigorously? | H/M/L |
| **Bias** | Does the source have systematic distortion? | None/Low/High |
| **Completeness** | Does it cover its claimed scope? | H/M/L |
| **Provenance** | Can we trace where the information came from? | Clear/Partial/Unknown |

**Process:**
1. For each source: rate on all dimensions
2. Assign overall quality grade: A (high confidence) / B (moderate) / C (use with caution) / D (unreliable — use only for triangulation)
3. During synthesis: weight contributions by quality grade
4. **Red flag:** If ALL high-quality sources agree but a low-quality source disagrees, investigate the disagreement before dismissing it — the dissenter may have access to information others don't.

**Output:** `source_quality[] → {source_id, dimension_ratings, grade, weight_in_synthesis}`

---

### 103 — Diversity Verification

**What:** Verify that the source set is genuinely diverse — not just many sources saying the same thing from the same perspective.

**Diversity Dimensions:**

| Dimension | Question | Why It Matters |
|-----------|----------|---------------|
| **Methodological** | Different methods? (quant + qual, empirical + theoretical) | Triangulation — convergence from different methods = strong evidence |
| **Perspectival** | Different viewpoints? (technical + business, builder + user) | Blind spots of one perspective covered by another |
| **Domain** | Different fields contributing? | Cross-domain synthesis produces novel insight |
| **Temporal** | Different time periods? | Temporal patterns only visible across time |
| **Geographical/Cultural** | Different contexts? | What works in one context may fail in another |
| **Epistemic** | Different levels of certainty? (established fact + emerging theory + speculation) | Range of certainty matters for synthesis confidence |

**Process:**
1. Map each source onto diversity dimensions
2. Identify clusters: if most sources are in one cluster, synthesis is biased toward that perspective
3. **Deliberately seek** sources from underrepresented clusters
4. Minimum: at least 2 of the 6 diversity dimensions should be well-represented

**Output:** `diversity_map → {dimension, coverage, clusters, gaps, deliberate_additions_needed}`

---

### 104 — Tacit Knowledge Elicitation

**What:** Surface knowledge that exists in people's heads but isn't documented. Often the most valuable synthesis input — and the hardest to access.

*Grounded in Polanyi (tacit knowledge) and Nonaka & Takeuchi (SECI model — Externalization quadrant).*

**Elicitation Methods:**

| Method | Best For | Limitation |
|--------|----------|-----------|
| **Structured interview** | Deep domain knowledge | Time-intensive |
| **Critical incident technique** | Experience-based knowledge | Memory bias |
| **Think-aloud protocol** | Procedural knowledge | Disrupts natural flow |
| **Concept mapping** (collaborative) | Relational knowledge | Requires facilitation skill |
| **Retrospective** | Project/event knowledge | Hindsight bias |
| **Apprenticeship/shadowing** | Embodied knowledge | Very time-intensive |

**Process:**
1. Identify: who holds tacit knowledge relevant to the synthesis question?
2. Select appropriate elicitation method
3. Externalize: capture in structured form (claims, models, stories)
4. Validate: cross-check elicited knowledge against other sources
5. **Caveat:** Tacit knowledge is shaped by individual experience — it's hypothesis-grade evidence, not established fact. Weight accordingly.

**Output:** `tacit_knowledge[] → {holder, method, extracted_claims[], validation_status, confidence}`

---

### 105 — Counter-Source Search

**What:** Actively seek sources that DISAGREE with the emerging direction. Confirmation bias makes us stop searching once we find agreement. This method forces continuing until disagreement is found.

**Process:**
1. After initial collection: what's the EMERGING consensus?
2. Deliberately search for: sources that would CONTRADICT that consensus
3. Steel-man the counter-source: present the strongest version of its argument
4. If NO counter-source can be found: either the consensus is very strong, OR you're not searching hard enough
5. **The absence of disagreement is suspicious.** Real knowledge domains always have contested areas.

**Output:** `counter_sources[] → {source, counter_argument, strength, implication_for_synthesis}`

---

## Phase 2: DECOMPOSE

*Goal: Break sources into ATOMIC knowledge elements — individual claims, concepts, models, and evidence. Synthesis requires knowing exactly what each source contributes at a granular level.*

---

### 201 — Atomic Claim Extraction

**What:** Extract individual, independent claims from each source. Each claim should be testable or evaluable on its own.

**Claim Types:**

| Type | Example | Evidence Need |
|------|---------|--------------|
| **Factual** | "Delta Lake supports ACID transactions" | Verification |
| **Causal** | "Tight coupling caused the cascade failure" | Mechanism + evidence |
| **Evaluative** | "Databricks is better than Synapse for this use case" | Criteria + comparison |
| **Prescriptive** | "Always use Unity Catalog for governance" | Justification |
| **Predictive** | "Data volumes will double in 12 months" | Basis + track record |
| **Definitional** | "EPR compliance means filing reports in each EU market" | Authority + scope |

**Process:**
1. For each source: list every distinct claim
2. Classify claim type
3. Separate EXPLICIT claims from IMPLICIT claims (what the source assumes but doesn't state)
4. Note the SOURCE and CONTEXT for each claim (a claim about Delta Lake performance in a PoC may not apply at production scale)
5. Tag with quality grade from #102

**Output:** `claims[] → {claim_id, source_id, text, type, explicit_or_implicit, context, quality_grade}`

---

### 202 — Concept Taxonomy Building

**What:** Identify all distinct CONCEPTS used across sources and build a shared vocabulary. Different sources often use different terms for the same concept, or same terms for different concepts.

**Process:**
1. List all domain concepts mentioned across sources
2. Identify **synonyms:** different words, same meaning ("pipeline" vs "workflow" vs "ETL job")
3. Identify **homonyms:** same word, different meanings ("schema" in database vs "schema" in psychology)
4. Build concept map: concept → definition → which sources use it → relationships to other concepts
5. **Kuhn alert:** When concepts have different PARADIGMATIC meanings across sources, flag this. "Agile" means something different to a developer vs a PMO. These differences are NOT superficial — they reflect deep framework conflicts.

**Output:** `taxonomy → {concept, definition, synonyms[], homonyms[], sources[], paradigm_flag}`

---

### 203 — Model Inventory

**What:** Identify all MODELS, FRAMEWORKS, and THEORIES used by different sources. Sources don't just present facts — they use models to organize and interpret facts. The model shapes what's visible and what's hidden.

**Process:**
1. For each source: what model/framework does it use? (Implicit or explicit)
2. Map each model's:
   - **Assumptions:** What does the model take for granted?
   - **Scope:** What does it explain?
   - **Blind spots:** What does it NOT explain?
   - **Level of analysis:** What level does it operate at? (#002)
3. Compare models across sources: do they agree? conflict? complement?
4. Identify: is any source model-free (pure data), or do all sources have interpretive frameworks?

**Example:**
```
Source A (Databricks blog): Model = "Lakehouse architecture solves all data problems"
├── Assumes: Unified batch+streaming is always better
├── Scope: Data engineering, analytics
├── Blind spot: Organizational readiness, skill requirements
├── Level: Technical architecture

Source B (Gartner report): Model = "Technology maturity lifecycle"
├── Assumes: Technologies follow predictable adoption curves
├── Scope: Market-level technology trends
├── Blind spot: Specific technical capabilities
├── Level: Market/industry

Source C (Team retrospective): Model = "Our experience doing this"
├── Assumes: Our context is representative
├── Scope: What worked and didn't for us
├── Blind spot: Why it might be different elsewhere
├── Level: Individual project
```

**Output:** `models[] → {source_id, model_name, assumptions, scope, blind_spots, level, paradigm}`

---

### 204 — Evidence Grading

**What:** Assess the STRENGTH of evidence behind each claim. Not all evidence is equal — a controlled experiment provides stronger evidence than an anecdote.

**Evidence Hierarchy (adapted from medical evidence hierarchy):**

| Grade | Evidence Type | Strength |
|-------|-------------|----------|
| **A** | Systematic review / meta-analysis of multiple studies | Strongest |
| **B** | Controlled experiment / rigorous A/B test | Strong |
| **C** | Observational study / careful measurement | Moderate |
| **D** | Case study / single observation | Weak-moderate |
| **E** | Expert opinion / professional experience | Weak |
| **F** | Anecdote / assumption / marketing material | Weakest |

**Process:**
1. For each claim from #201: what evidence supports it?
2. Grade the evidence
3. During synthesis: weight claims by evidence grade, not by source reputation or volume
4. **Red flag:** High-impact claims supported only by F-grade evidence. Either investigate further or flag as uncertain.
5. **Red flag:** Claims that "everyone knows" with no evidence at all — check for Unknown Knowns or conventional wisdom that's wrong.

**Output:** `evidence[] → {claim_id, evidence_description, grade, weight_in_synthesis}`

---

### 205 — Assumption Surfacing

**What:** Make EXPLICIT the implicit assumptions that each source carries. Assumptions are the hidden load-bearing elements — when they break, everything built on them collapses.

**Process:**
1. For each source: what does it ASSUME that it doesn't state?
   - Domain assumptions ("customers want this feature")
   - Technical assumptions ("the system can handle this load")
   - Temporal assumptions ("this will still be true in 12 months")
   - Methodological assumptions ("our measurement captures reality")
   - Paradigmatic assumptions ("agile is the right approach")
2. Compare assumptions across sources: where do they DIVERGE?
3. Diverging assumptions are the most important synthesis opportunities — they reveal where integration requires deeper understanding

**Output:** `assumptions[] → {source_id, assumption, explicit_or_surfaced, diverges_from_source[], criticality}`

---

### 206 — Knowledge Gap Identification

**What:** Identify what the source set DOESN'T cover — the negative space. Gaps in knowledge are as important as the knowledge itself for synthesis.

**Gap Types:**

| Type | Description | Implication |
|------|-------------|-------------|
| **Coverage gap** | A relevant topic with no sources | Synthesis is incomplete in that area |
| **Evidence gap** | Claims without supporting evidence | Synthesis is uncertain in that area |
| **Perspective gap** | A relevant viewpoint with no representation | Synthesis may be biased |
| **Temporal gap** | A time period with no data | Synthesis may miss time-dependent patterns |
| **Level gap** | A level of analysis with no sources | Can't draw conclusions at that level |
| **Method gap** | A relevant method not represented | Can't triangulate |

**Process:**
1. Compare source coverage against synthesis question scope
2. Identify all gaps
3. For each: is it addressable (can we find/generate the missing knowledge)?
4. For non-addressable gaps: acknowledge in synthesis as limitation
5. **Critical:** A synthesis that doesn't acknowledge its gaps is more dangerous than incomplete data — it creates false completeness.

**Output:** `gaps[] → {type, description, addressable, impact_on_synthesis}`

---

## Phase 3: RELATE

*Goal: Map relationships between knowledge atoms. This is where synthesis starts — not in the atoms themselves but in the CONNECTIONS between them.*

---

### 301 — Convergence-Divergence Mapping

**What:** For every pair of claims: do they agree, disagree, or address different aspects?

**Relationship Types:**

| Relationship | Definition | Synthesis Action |
|-------------|------------|-----------------|
| **Convergence** | Multiple sources make same/similar claim | Strengthens confidence — especially valuable if sources used different methods (triangulation) |
| **Divergence** | Sources contradict each other | MOST VALUABLE — requires understanding WHY. Resolve or preserve as productive tension |
| **Complementarity** | Sources address different aspects of same topic | Combine for more complete picture |
| **Independence** | No meaningful relationship | May or may not be relevant |
| **Dependency** | Claim B is only true IF claim A is true | Create conditional chains |
| **Subsumption** | Claim A is a special case of broader claim B | Organize into hierarchies |

**Process:**
1. For key claims: map pairwise relationships
2. Focus on DIVERGENCES — these are synthesis opportunities
3. For each divergence: is it because of different data? Different methods? Different assumptions? Different levels of analysis?
4. Build relationship graph: claims as nodes, relationships as edges

**Output:** `relationships[] → {claim_a, claim_b, type, explanation, synthesis_priority}`

---

### 302 — Dialectical Tension Mapping

**What:** Identify thesis-antithesis pairs — positions that are in productive tension. These are the raw material for Hegelian synthesis.

*Grounded in Hegel's dialectic.*

**Process:**
1. From divergences in #301: identify pairs that represent genuine opposing positions
2. For each pair:
   - **Thesis:** What is the position?
   - **Antithesis:** What is the counter-position?
   - **Valid in thesis:** What is TRUE about this position?
   - **Valid in antithesis:** What is TRUE about this position?
   - **Synthesis opportunity:** What HIGHER understanding preserves both valid elements?
3. Some tensions are IRRESOLVABLE at the current level — they require moving to a higher level of abstraction
4. Some tensions are FALSE — they appear contradictory but actually address different scopes/contexts

**Example:**
```
Thesis: "Centralized data governance ensures consistency" (Mars IT)
Antithesis: "Federated data ownership enables agility" (Lingaro data team)

Valid in thesis: Consistency IS important for regulatory reporting
Valid in antithesis: Agility IS important for iterative development

Synthesis: "Centralized policies + federated execution"
→ Define governance rules centrally (consistency)
→ Let teams implement within rules (agility)
→ This is actually what Unity Catalog enables — centralized catalog, federated workspaces
```

**Output:** `tensions[] → {thesis, antithesis, valid_in_each, synthesis_opportunity, resolution_level}`

---

### 303 — Analogical Structure Mapping (Gentner)

**What:** Find structural parallels between different domains in the source set. Surface features may differ but RELATIONAL STRUCTURE may be identical — enabling powerful cross-domain transfer.

**Process:**
1. For each pair of DOMAIN-DIFFERENT sources: map the structural relationships
2. Identify **structural alignments:** same relationship pattern despite different domains
   - "A causes B" in domain 1 maps to "X causes Y" in domain 2
   - The CAUSE relationship is the structural element, not the specific entities
3. Assess **systematicity:** do multiple relational mappings align, or just one?
   - One mapping = analogy (weak)
   - Multiple aligned mappings = structural isomorphism (strong)
4. **Transfer test:** Does knowledge from the more-understood domain apply to the less-understood domain via the structural mapping?
5. **Danger:** Surface similarity without structural similarity produces FALSE analogies.

**Example:**
```
Domain 1: Data pipeline (data engineering)
├── Backpressure from slow consumer
├── Buffer overflow when buffer full
├── Cascading failure when one stage stalls

Domain 2: Supply chain (logistics)
├── Backlog from slow processing
├── Warehouse overflow when storage full
├── Cascade when one supplier delays

Structural mapping: BOTH are flow systems with capacity constraints
Transfer: Supply chain solutions (kanban, JIT, buffer management) may apply to data pipelines
Validated: Kafka's consumer groups ARE a form of kanban
```

**Output:** `analogies[] → {domain_1, domain_2, structural_mappings[], systematicity, transfer_candidates[]}`

---

### 304 — Conceptual Blend Construction (Fauconnier-Turner)

**What:** Deliberately blend concepts from different input spaces to generate emergent insights that exist in neither space alone.

**Process:**
1. Select two (or more) input spaces from different sources/domains
2. Identify the **generic space** — shared abstract structure
3. Construct the **blended space** — selectively combine elements
4. Look for **emergent structure** — properties of the blend that aren't in either input
5. Evaluate: is the emergent insight genuine (produces testable predictions) or spurious (just sounds clever)?

**Example:**
```
Input 1: "Immune system" (biology)
├── Recognizes self vs non-self
├── Memory of past threats
├── Adaptive response to new threats
├── Autoimmune = attacking self

Input 2: "Data quality system" (data engineering)
├── Needs to recognize valid vs invalid data
├── Should learn from past quality issues
├── Should adapt to new data patterns
├── Over-strict validation = rejecting good data

Generic space: Adaptive recognition system

Blended space: "Data immune system"
├── EMERGENT: Just as immune systems need tolerance training to avoid autoimmune disease,
│   data quality systems need calibration periods to avoid rejecting legitimate new patterns
├── EMERGENT: Immune memory suggests a "data quality memory" that remembers past
│   issues and checks for recurrence — not just current rules
├── PREDICTION: A data quality system that "remembers" past issues will catch more
│   problems than a purely rule-based system → testable claim
```

**Output:** `blends[] → {input_spaces, generic_space, blended_space, emergent_insights[], testable_predictions[]}`

---

### 305 — Causal Chain Reconciliation

**What:** Different sources may present different causal explanations for the same phenomenon. Reconcile into a unified causal model — or explain why they diverge.

**Process:**
1. Extract causal claims from each source (A causes B)
2. Build causal graph per source
3. Compare graphs: where do they agree? Where do they diverge?
4. For divergences:
   - **Missing variable:** Source A omits mediator that Source B includes
   - **Reversed causation:** A says X→Y, B says Y→X
   - **Confounded:** Both are correct, but unmeasured variable Z causes both X and Y
   - **Level difference:** A describes micro-level cause, B describes macro-level cause — both correct at their level
   - **Temporal:** A describes short-term, B describes long-term — causation reverses over time
5. Build UNIFIED causal model that accounts for all sources' evidence

**Output:** `causal_model → {unified_graph, source_contributions, divergences_resolved, remaining_conflicts}`

---

### 306 — Pattern Detection Across Sources

**What:** Look for recurring patterns that appear across multiple sources, even if the sources don't recognize the pattern. The pattern may only be visible from the synthesis viewpoint.

**Pattern Types:**

| Pattern | Description | Synthesis Value |
|---------|------------|----------------|
| **Recurrence** | Same finding across different contexts | High confidence — context-independent |
| **Scaling** | Pattern changes character at different scales | Reveals scale-dependent dynamics |
| **Oscillation** | Phenomenon alternates between states | Suggests dynamic equilibrium, not static |
| **Emergence** | New property appears at higher level | System-level insight, not reducible to components |
| **Decay/Growth** | Consistent directional trend across sources | Temporal insight — trajectory matters |
| **Phase transition** | Abrupt change at a threshold | Reveals tipping points |

**Process:**
1. Lay out key findings from all sources
2. Look for patterns that span MULTIPLE sources
3. For each pattern: is it real or apophenia? (→ validate in META #601)
4. For real patterns: does any source EXPLAIN the pattern? Or is it a novel synthesis finding?

**Output:** `patterns[] → {pattern_type, description, sources_showing_it, explained_by_source, novel_finding}`

---

### 307 — Level Alignment Check

**What:** Ensure that when combining claims from different sources, they're operating at the SAME level of analysis. Mixing levels produces invalid synthesis.

*Grounded in Simpson's Paradox, ecological fallacy, atomistic fallacy.*

**Process:**
1. For each claim to be synthesized: at what level does it apply?
2. For claims being COMBINED: are they at the same level?
3. **Red flags:**
   - Combining group-level finding with individual-level data → ecological fallacy
   - Generalizing from individual case to population → atomistic fallacy
   - Aggregate trend contradicts subgroup trends → Simpson's Paradox
4. When levels don't match: either align to the same level or explicitly note the cross-level inference with appropriate caveats

**Output:** `level_check[] → {claim_pair, levels, aligned, fallacy_risk, caveat_if_misaligned}`

---

### 308 — Gap Significance Analysis

**What:** Determine whether knowledge gaps (#206) are RANDOM or SYSTEMATIC. Systematic gaps reveal blind spots in the field itself — and are themselves a synthesis finding.

**Process:**
1. Take all gaps from #206
2. Look for patterns: do gaps cluster around a topic? A perspective? A methodology?
3. **Random gaps:** Just missing data — address by seeking more sources
4. **Systematic gaps:** The field/team/organization consistently avoids this area → this IS a finding
   - Why is this area avoided? Politically sensitive? Hard to study? Doesn't fit dominant paradigm?
5. **Systematic gaps often contain the most important insights** — what no one studies or discusses is often what everyone needs to understand

**Output:** `gap_analysis → {gap, random_or_systematic, if_systematic_why, synthesis_implication}`

---

## Phase 4: INTEGRATE

*Goal: Build unified understanding from the relationship map. This is the CORE synthesis step — where atomistic analysis becomes holistic understanding.*

---

### 401 — Dialectical Integration

**What:** For each dialectical tension (#302), construct a genuine synthesis that preserves valid elements of both thesis and antithesis while transcending their contradiction.

**Synthesis Strategies:**

| Strategy | When to Use | Example |
|----------|------------|---------|
| **Separation in scope** | Both true in different contexts | "Centralized for governance, federated for execution" |
| **Separation in time** | Both true at different times | "Explore broadly first, then commit deeply" |
| **Separation in scale** | Both true at different scales | "Simple interface, complex internals" |
| **Higher-order principle** | Both are special cases of a general truth | "Optimize for ADAPTABILITY, which sometimes means centralized, sometimes federated" |
| **Integration** | Both contribute to something neither describes alone | "Real-time data quality" is neither "real-time processing" nor "batch quality checks" but a synthesis |
| **Productive tension** | Resolution would destroy value; maintain both | "Innovation and reliability exist in productive tension — don't resolve, manage" |

**Process:**
1. For each tension from #302: which synthesis strategy applies?
2. Construct the synthesis: articulate the higher-order understanding
3. Test: does the synthesis actually PRESERVE valid elements of both? Or did it sneak in a bias toward one side?
4. Test: does the synthesis generate NEW insight or prediction that wasn't in either thesis or antithesis?

**Output:** `syntheses[] → {tension_id, strategy, synthesis_statement, preserves_from_thesis, preserves_from_antithesis, novel_insight}`

---

### 402 — Framework Unification

**What:** When multiple sources use different models/frameworks (#203), build a UNIFIED framework that incorporates the valid elements of each.

**Process:**
1. List all models/frameworks from #203
2. Map overlaps: where do frameworks describe the same thing?
3. Map gaps: what does each framework cover that others don't?
4. Map conflicts: where do frameworks make contradictory claims?
5. Construct unified framework:
   - Take the BEST explanation from each framework for its area of strength
   - Resolve conflicts via #401 strategies
   - Fill gaps by extending frameworks or acknowledging limitations
6. Test: does the unified framework explain MORE than any individual framework?
7. Test: is the unified framework SIMPLER than the sum of individual frameworks? (Kolmogorov — compression)

**Output:** `unified_framework → {component_frameworks, coverage, resolution_of_conflicts, novel_coverage, compression_ratio}`

---

### 403 — Emergence Detection

**What:** Look for properties, insights, or patterns that EMERGE from the combination of sources but aren't present in any single source. This is the core test of genuine synthesis.

*Grounded in systems theory — emergence: the whole is more than the sum of parts.*

**Shannon Test:**
For each synthesis finding, ask:
- Can this be derived from Source A alone? → If yes, it's extraction, not synthesis
- Can this be derived from Source B alone? → If yes, it's extraction, not synthesis
- Does it require BOTH A and B (and possibly more)? → If yes, it's genuine emergence

**Categories of Emergent Insight:**

| Category | Description | Example |
|----------|-------------|---------|
| **Cross-domain pattern** | Same pattern visible across different domains | Risk cascade in pipelines mirrors supply chain disruption |
| **Missing middle** | Gap between sources reveals an unexplored territory | Source A covers input, Source C covers output — what happens in between? |
| **Contradiction resolution** | Understanding WHY sources disagree reveals deeper truth | They disagree because they measured at different scales |
| **Implication chain** | A implies B (Source 1), B implies C (Source 2), therefore A implies C (novel) | Technology trend + regulatory direction → market opportunity no source identified |
| **Boundary condition** | Synthesis reveals WHERE something is true vs false | "This approach works for < 1M records" (from combining success and failure reports) |

**Process:**
1. For each synthesis finding from #401 and #402: apply Shannon Test
2. Classify emergent insights by category
3. For each: is it testable? What would confirm or refute it?
4. Rate confidence: more sources contributing → higher confidence in emergence

**Output:** `emergent_insights[] → {insight, category, contributing_sources, shannon_test_pass, testable, confidence}`

---

### 404 — Abductive Integration

**What:** When evidence doesn't fully determine a conclusion, construct the BEST EXPLANATION that accounts for all evidence — the inference to the best explanation. This is the creative core of synthesis.

*Grounded in Peirce's abductive reasoning.*

**Process:**
1. Gather all evidence from all sources
2. Generate candidate explanations that could account for ALL evidence
3. Evaluate candidates on:
   - **Coverage:** How much evidence does it explain?
   - **Simplicity:** How simple is it? (Occam's razor)
   - **Consistency:** Does it conflict with any established knowledge?
   - **Fertility:** Does it generate new testable predictions?
   - **Plausibility:** Is it believable given domain knowledge?
4. Select the best explanation — the one that BEST balances all criteria
5. **Explicit caveat:** Abductive conclusions are HYPOTHESES, not certainties. They are the best current explanation, not the final truth.

**Output:** `abductive_conclusions[] → {evidence_base, candidate_explanations, best_explanation, coverage, simplicity, fertility, confidence}`

---

### 405 — Knowledge Compression

**What:** Compress the synthesis into its MINIMAL representation — the shortest description that captures the essential structure. If your synthesis is as long as your sources, you haven't synthesized.

*Grounded in Kolmogorov Complexity.*

**Compression Levels:**

| Level | Format | Size | Audience |
|-------|--------|------|----------|
| **Title** | One phrase | ~5 words | Everyone |
| **Thesis** | One sentence | ~20 words | Decision-makers |
| **Abstract** | One paragraph | ~100 words | Stakeholders |
| **Executive summary** | One page | ~500 words | Management |
| **Full synthesis** | Complete document | Variable | Implementers |
| **Appendix** | Supporting evidence | Variable | Auditors |

**Process:**
1. Write the TITLE first — if you can't title it, you haven't synthesized
2. Then thesis — what's the single most important insight?
3. Then abstract — what are the 3-5 key findings?
4. Each level must be SELF-CONTAINED — readable without the level below
5. **Compression test:** Can someone at each level make appropriate decisions with just that level's information?

**Output:** `compressed_synthesis → {title, thesis, abstract, executive_summary, full, appendix}`

---

### 406 — Boundary Condition Mapping

**What:** Define WHERE the synthesis applies and where it doesn't. Every synthesis has scope limits — making them explicit prevents misapplication.

**Process:**
1. For each synthesis conclusion: under what conditions does it hold?
2. Define boundaries:
   - **Scale boundaries:** Works for N<1000 but not N>1M
   - **Context boundaries:** Works in cloud but not on-prem
   - **Temporal boundaries:** True now but may change when...
   - **Domain boundaries:** Works for data engineering but not ML engineering
   - **Organizational boundaries:** Works for small teams but not enterprises
3. For each boundary: what happens OUTSIDE the boundary? (Gradual degradation? Complete failure? Unknown?)
4. **Extrapolation warning:** Applying synthesis beyond its boundaries without validation is a common source of false coherence

**Output:** `boundaries[] → {conclusion, boundary_type, valid_range, outside_behavior, extrapolation_risk}`

---

### 407 — Synthesis Coherence Check

**What:** Test whether the integrated synthesis is internally consistent. Synthesis that contradicts itself is worse than no synthesis.

**Process:**
1. List all synthesis conclusions
2. For each pair: are they mutually compatible?
3. If contradictory:
   - Is the contradiction at different levels of analysis? (May be fine if acknowledged)
   - Is the contradiction at different scopes? (May be fine if bounded)
   - Is it genuine contradiction? → Must resolve or acknowledge as open question
4. Check logical consistency: does Conclusion A + Conclusion B imply anything that contradicts Conclusion C?
5. **Internal consistency is necessary but NOT sufficient.** A synthesis can be perfectly consistent and perfectly wrong (beautiful but false theory).

**Output:** `coherence_check → {contradictions, resolved, remaining, overall_coherence}`

---

## Phase 5: CRYSTALLIZE

*Goal: Transform integrated understanding into communicable, actionable form — models, principles, narratives, and recommendations.*

---

### 501 — Core Insight Distillation

**What:** Extract the 3-7 most important insights from the synthesis. These are the findings that CHANGE how someone should think or act.

**Insight Quality Criteria:**

| Criterion | Question |
|-----------|----------|
| **Novelty** | Is this genuinely new? Or restating what sources already said? |
| **Actionability** | Can someone DO something different based on this? |
| **Importance** | Does this insight MATTER for the synthesis question? |
| **Robustness** | Does this hold across multiple sources and methods? |
| **Surprise** | Does this challenge existing assumptions? (Surprise = high information value) |

**Process:**
1. List all synthesis findings
2. Score each on 5 criteria
3. Select top 3-7 as CORE insights
4. For each: write in ONE sentence
5. Order by: importance × actionability

**Output:** `core_insights[] → {insight, novelty, actionability, importance, robustness, surprise, one_sentence}`

---

### 502 — Mental Model Design

**What:** Construct one or more MENTAL MODELS that capture the synthesis in a form that can be internalized and applied. A good mental model enables someone to make correct predictions in new situations.

**Mental Model Types:**

| Type | Form | Best For |
|------|------|----------|
| **Visual diagram** | Boxes, arrows, flows | System structure and dynamics |
| **Matrix/grid** | 2×2 or N×M | Classification and trade-offs |
| **Hierarchy** | Tree structure | Decomposition and categorization |
| **Cycle** | Circular/spiral | Recurring processes and feedback |
| **Spectrum** | Linear scale | Continuous dimensions and positioning |
| **Formula** | Mathematical expression | Quantitative relationships |
| **Metaphor** | Analogy to familiar domain | Intuitive understanding |

**Process:**
1. What FORM best captures the synthesis? (The form shapes understanding)
2. Build the model: include ONLY essential elements (compression)
3. Test: can someone who hasn't seen the sources use this model to make correct predictions?
4. Test: does the model GENERALIZE beyond the specific cases in the sources?
5. Name the model: a good name makes it memorable and shareable

**Output:** `mental_models[] → {name, type, description, essential_elements, predictive_test, generalization_scope}`

---

### 503 — Principle Extraction

**What:** Derive GENERAL PRINCIPLES from the synthesis — rules that apply beyond the specific context of the sources. Principles are the most durable form of synthesized knowledge.

**Principle Quality:**
A good principle is:
- **General:** Applies to a class of situations, not just one
- **Predictive:** Makes testable claims about what will happen
- **Actionable:** Tells you what to DO (or avoid)
- **Memorable:** Short enough to remember
- **Falsifiable:** Can be proven wrong (Popper)

**Process:**
1. From core insights (#501): which generalize beyond the specific synthesis context?
2. Formulate as principles: "When [context], [action/observation] because [mechanism]"
3. Test: would this principle have been useful BEFORE the sources were collected? (If yes, it's genuinely general)
4. Define boundaries: where does this principle NOT apply?
5. Check for existing principles: is this a known principle under a different name?

**Example:**
```
From synthesis of 5 project post-mortems:
Insight: "Every project underestimated integration time"
Principle: "Integration effort is proportional to the SQUARE of the number of components,
           not the number of components. Budget accordingly."
Context: Multi-component system development
Mechanism: Each pair of components has a potential integration issue; pairs grow quadratically
Boundaries: Applies to tightly coupled systems; loosely coupled may be more linear
Falsifiable: Measure actual integration effort vs component count; plot should be quadratic
```

**Output:** `principles[] → {principle, context, mechanism, boundaries, falsifiable_by, novelty}`

---

### 504 — Narrative Construction

**What:** Build a coherent STORY from the synthesis. Humans think in narratives — a well-constructed narrative makes synthesis sticky and shareable.

**Narrative Elements:**

| Element | Purpose | Synthesis Mapping |
|---------|---------|-------------------|
| **Setting** | Context and background | Source landscape, domain context |
| **Characters** | Who/what is involved | Stakeholders, systems, concepts |
| **Tension** | Conflict or question | Dialectical tensions, contradictions |
| **Discovery** | What was learned | Emergent insights, resolved tensions |
| **Resolution** | How it comes together | Unified framework, principles |
| **Implication** | What happens next | Actionable conclusions, predictions |

**Narrative Fallacy Guard:**
Narratives are powerful but dangerous. They can make accidental patterns feel inevitable. For each narrative element, check:
- Is this SUPPORTED by evidence, or just a good story?
- Would a different narrative structure change the conclusion?
- Am I including this because it's TRUE or because it makes a satisfying story?

**Process:**
1. Build narrative following the elements
2. Ensure every narrative claim is traceable to evidence
3. Apply narrative fallacy guard
4. Write at appropriate level for audience (executive vs technical vs general)

**Output:** `narrative → {story, evidence_traceability, fallacy_check, audience_level}`

---

### 505 — Actionability Assessment

**What:** For each synthesis output, assess: what should someone DO differently based on this? Synthesis that doesn't lead to different action or understanding is academic.

**Actionability Dimensions:**

| Dimension | Question |
|-----------|----------|
| **Decisions** | Which decisions does this synthesis inform? |
| **Predictions** | What can we now predict that we couldn't before? |
| **Questions** | What NEW questions does this synthesis raise? |
| **Warnings** | What risks/pitfalls does this synthesis reveal? |
| **Opportunities** | What possibilities does this synthesis open? |
| **Changes** | What should we CHANGE based on this synthesis? |

**Process:**
1. For each core insight and principle: map to actionability dimensions
2. Prioritize: what's the SINGLE most important action?
3. Identify: what synthesis outputs feed into other Deep processes?
   - New options → Deep-Explore
   - Correctness concerns → Deep-Verify
   - Feasibility questions → Deep-Feasibility
   - New risks → Deep-Risk

**Output:** `actions[] → {insight_or_principle, dimension, recommended_action, priority, feeds_into_process}`

---

## META Methods

*Applied continuously. Validate the synthesis itself — is it genuine understanding or false coherence?*

---

### 601 — Apophenia Check

**What:** Test whether detected patterns (#306) are REAL or imposed by the synthesizer's pattern-seeking brain. Humans are pattern-completion machines — we see faces in clouds and causation in coincidence.

**Detection Methods:**
1. **Base rate test:** What's the probability of this pattern appearing by CHANCE?
2. **Prediction test:** If the pattern is real, what ELSE should be true? Check those predictions.
3. **Alternative explanation test:** Is there a simpler explanation that doesn't require the pattern?
4. **Independent observer test:** Would someone with different expertise see the same pattern?
5. **Removal test:** Remove one source from the synthesis. Does the pattern survive? If it depends on a single source, it's weak.

**Red Flags:**
- Pattern only visible after extensive "massaging" of data
- Pattern depends on specific framing or ordering of sources
- No one outside the synthesis team sees it
- Pattern conveniently confirms synthesizer's prior beliefs

**Output:** `pattern_validity[] → {pattern, base_rate, prediction_test, alternative_explanation, robustness, verdict}`

---

### 602 — Confirmation Bias Audit

**What:** Check whether the synthesis selectively weighted evidence that confirms a pre-existing view while downweighting evidence that contradicts it.

**Process:**
1. What was the synthesizer's PRIOR VIEW before starting?
2. Does the synthesis conclusion ALIGN with the prior view?
3. If yes: were counter-sources (#105) given adequate weight? Were divergences fully explored?
4. Perform **inversion test:** if someone with the OPPOSITE prior view looked at the same sources, would they reach the same synthesis? If not, bias is likely present.
5. Check source selection: were sources chosen to CONFIRM or to INVESTIGATE?

**Output:** `bias_audit → {prior_view, synthesis_aligns, counter_evidence_weight, inversion_test_result, bias_verdict}`

---

### 603 — Completeness Assessment

**What:** Evaluate whether the synthesis adequately covers the synthesis question. Incomplete synthesis is fine — as long as the gaps are acknowledged.

**Completeness Dimensions:**
- **Question coverage:** Does the synthesis address ALL aspects of the question?
- **Source utilization:** Were all collected sources actually used?
- **Contradiction resolution:** Were all divergences addressed?
- **Gap acknowledgment:** Are known gaps documented?
- **Level coverage:** Are all relevant levels of analysis included?

**Process:**
1. Score each dimension
2. For gaps: is the gap acknowledged in the synthesis output?
3. Overall: is the synthesis ADEQUATE for its intended purpose? (Complete enough, not perfect)
4. **Bonini's Paradox check:** If achieving completeness would require a synthesis as complex as reality, accept meaningful incompleteness.

**Output:** `completeness → {dimension_scores, acknowledged_gaps, adequate_for_purpose}`

---

### 604 — Falsifiability Check (Popper)

**What:** Verify that the synthesis produces claims that could, in principle, be proven wrong. A synthesis that explains everything and predicts nothing is narrative, not knowledge.

**Process:**
1. For each major synthesis conclusion: what evidence would DISPROVE it?
2. Is that evidence obtainable? (In principle? Practically?)
3. If no evidence could disprove it: the conclusion is unfalsifiable → downgrade to "perspective" or "narrative", not "finding"
4. For falsifiable conclusions: what's the cheapest/fastest way to test?
5. **Time-delayed falsification:** Some conclusions can only be tested over time. Note the timeline and set a review date.

**Output:** `falsifiability[] → {conclusion, disproof_evidence, obtainable, test_method, timeline}`

---

### 605 — Source Bias Propagation Check

**What:** Assess whether biases in individual sources have propagated into the synthesis. Even quality-assessed sources carry biases — and synthesis can AMPLIFY them if most sources share the same bias.

**Common Propagated Biases:**

| Bias | Mechanism | Check |
|------|-----------|-------|
| **Survivorship** | Only successful cases reported | Are failure cases represented? |
| **Publication** | Only positive results published | Are null results included? |
| **Selection** | Sources selected to confirm hypothesis | Were sources gathered systematically? |
| **Recency** | Recent sources overweighted | Are historical perspectives included? |
| **Authority** | High-status sources overweighted | Are practitioner perspectives included? |
| **Cultural** | Dominant culture's perspective assumed universal | Are diverse cultural perspectives represented? |
| **Methodological** | One method dominates | Are multiple methods represented? |

**Process:**
1. For each bias type: check whether the source set is affected
2. If bias detected: assess impact on synthesis conclusions
3. Adjust synthesis to acknowledge or correct for propagated bias

**Output:** `bias_propagation[] → {bias_type, affected, impact_on_synthesis, correction}`

---

### 606 — Novel Information Test (Shannon)

**What:** Rigorously test whether the synthesis contains GENUINE new information or is merely reorganizing what sources already said.

**Test:**
1. For each claimed synthesis insight:
   - Is it present in Source A? → Extraction from A
   - Is it present in Source B? → Extraction from B
   - Does it require COMBINING A and B? → Genuine synthesis
   - Does it come from the synthesizer's prior knowledge, not sources? → Added expertise (label it)
2. Count: how many insights are genuine synthesis vs extraction vs added?
3. A synthesis with 0% genuine novel insights is a SUMMARY, not a synthesis. Relabel it.
4. Target: at least 30% of key insights should be genuine synthesis (combining sources to produce new understanding)

**Output:** `novelty_test → {insight, source_test, classification, overall_novelty_ratio}`

---

### 607 — Synthesis Decay Monitoring

**What:** Synthesis conclusions are not permanent. Define what changes would invalidate the synthesis and require reassessment.

**Decay Triggers:**

| Trigger | Impact |
|---------|--------|
| **New contradicting source** | May invalidate core conclusions |
| **Source quality revision** | Changes evidence weights |
| **Context change** | May violate boundary conditions (#406) |
| **Time passage** | Temporal assumptions may expire |
| **Failed prediction** | Synthesis model is wrong in some way |
| **Paradigm shift in domain** | May invalidate framework assumptions |

**Process:**
1. For each core conclusion: what would change it?
2. Set monitoring cadence: when to re-evaluate?
3. Define KILL criteria: what evidence would completely invalidate the synthesis?
4. **Living synthesis:** Major syntheses should be versioned and updated, not treated as final documents

**Output:** `decay_monitors[] → {conclusion, trigger, check_cadence, kill_criteria}`

---

## Method Summary

| # | Phase | Method | Core Question |
|---|-------|--------|---------------|
| 001 | SCOPE | Synthesis Question Formulation | What exactly are we synthesizing and why? |
| 002 | SCOPE | Level-of-Analysis Selection | At what abstraction level? |
| 003 | SCOPE | Source Landscape Mapping | What types of knowledge exist and are missing? |
| 101 | ACQUIRE | Systematic Source Collection | Have we gathered comprehensively? |
| 102 | ACQUIRE | Source Quality Assessment | How reliable is each source? |
| 103 | ACQUIRE | Diversity Verification | Are multiple perspectives represented? |
| 104 | ACQUIRE | Tacit Knowledge Elicitation | What knowledge is undocumented? |
| 105 | ACQUIRE | Counter-Source Search | Have we sought disagreement? |
| 201 | DECOMPOSE | Atomic Claim Extraction | What exactly does each source claim? |
| 202 | DECOMPOSE | Concept Taxonomy Building | Are we using consistent terminology? |
| 203 | DECOMPOSE | Model Inventory | What frameworks do sources use? |
| 204 | DECOMPOSE | Evidence Grading | How strong is the evidence? |
| 205 | DECOMPOSE | Assumption Surfacing | What's implicit in each source? |
| 206 | DECOMPOSE | Knowledge Gap Identification | What's missing from the source set? |
| 301 | RELATE | Convergence-Divergence Mapping | Where do sources agree and disagree? |
| 302 | RELATE | Dialectical Tension Mapping | What thesis-antithesis pairs exist? |
| 303 | RELATE | Analogical Structure Mapping | What structural parallels exist cross-domain? |
| 304 | RELATE | Conceptual Blend Construction | What emerges when we blend mental spaces? |
| 305 | RELATE | Causal Chain Reconciliation | How do different causal explanations fit together? |
| 306 | RELATE | Pattern Detection Across Sources | What recurring patterns span sources? |
| 307 | RELATE | Level Alignment Check | Are we mixing abstraction levels correctly? |
| 308 | RELATE | Gap Significance Analysis | Are gaps random or systematic? |
| 401 | INTEGRATE | Dialectical Integration | How do we resolve productive tensions? |
| 402 | INTEGRATE | Framework Unification | Can we build one framework from many? |
| 403 | INTEGRATE | Emergence Detection | What's genuinely new in the combination? |
| 404 | INTEGRATE | Abductive Integration | What's the best explanation for all evidence? |
| 405 | INTEGRATE | Knowledge Compression | What's the shortest description that captures the essential? |
| 406 | INTEGRATE | Boundary Condition Mapping | Where does this synthesis apply and where not? |
| 407 | INTEGRATE | Synthesis Coherence Check | Is the synthesis internally consistent? |
| 501 | CRYSTALLIZE | Core Insight Distillation | What are the 3-7 most important findings? |
| 502 | CRYSTALLIZE | Mental Model Design | What model captures this for intuitive use? |
| 503 | CRYSTALLIZE | Principle Extraction | What general rules emerge? |
| 504 | CRYSTALLIZE | Narrative Construction | What's the story? |
| 505 | CRYSTALLIZE | Actionability Assessment | What should change based on this? |
| 601 | META | Apophenia Check | Are detected patterns real? |
| 602 | META | Confirmation Bias Audit | Did prior views distort the synthesis? |
| 603 | META | Completeness Assessment | Is the synthesis adequate? |
| 604 | META | Falsifiability Check | Can the synthesis be proven wrong? |
| 605 | META | Source Bias Propagation Check | Did source biases infect the synthesis? |
| 606 | META | Novel Information Test | Is this genuine synthesis or just summary? |
| 607 | META | Synthesis Decay Monitoring | When will this synthesis expire? |

**Total: 40 methods** (3 SCOPE + 5 ACQUIRE + 6 DECOMPOSE + 8 RELATE + 7 INTEGRATE + 5 CRYSTALLIZE + 7 META)

---

## Usage Guide

### When to Use Deep-Synthesis

| Trigger | Starting Phase | Depth |
|---------|---------------|-------|
| **Integrating research for a decision** | SCOPE → full cycle | Full |
| **Post-mortem across multiple incidents** | SCOPE → ACQUIRE → DECOMPOSE → RELATE → INTEGRATE | Standard |
| **Literature review** | SCOPE → ACQUIRE → DECOMPOSE → RELATE | Focus on RELATE |
| **Cross-team knowledge sharing** | ACQUIRE → DECOMPOSE → CRYSTALLIZE | Focus on CRYSTALLIZE |
| **Making sense of conflicting advice** | DECOMPOSE → RELATE → INTEGRATE | Focus on RELATE + INTEGRATE |
| **Synthesizing Deep Framework outputs** | All outputs as sources → RELATE → INTEGRATE → CRYSTALLIZE | Integration use case |
| **Domain knowledge building** | Full cycle | Full |

### Scaling Deep-Synthesis

| Context | Methods | Time |
|---------|---------|------|
| **Quick synthesis** | #001 + #201 + #301 + #401 + #501 | 1-2 hours |
| **Standard synthesis** | SCOPE + ACQUIRE + DECOMPOSE + RELATE + CRYSTALLIZE | Half day |
| **Rigorous synthesis** | Full cycle including INTEGRATE + META | 2-3 days |
| **Comprehensive knowledge synthesis** | Full cycle + multiple rounds + stakeholder review | 1-2 weeks |

### Integration with Other Deep Processes

**Synthesis OF process outputs (meta-integration):**
```
EXPLORE output ──┐
VERIFY output  ──┼──→ DEEP-SYNTHESIS → Unified understanding → Decision
FEASIBILITY output ┤
RISK output    ──┘
```

**Synthesis AS preparation:**
```
Domain knowledge ──→ DEEP-SYNTHESIS → Mental model → Feed into EXPLORE/VERIFY/FEASIBILITY/RISK
Research findings ──┘
```

**Synthesis FOR learning:**
```
Post-mortems ──┐
Retrospectives ┼──→ DEEP-SYNTHESIS → Principles → Organizational knowledge
Case studies  ──┘
```

---

## Appendix A: Synthesis Quality Rubric

| Criterion | Excellent | Good | Adequate | Poor |
|-----------|-----------|------|----------|------|
| **Novelty** | >50% genuine synthesis | 30-50% synthesis | 10-30% synthesis | <10% (it's a summary) |
| **Compression** | 5× shorter than sources | 3× shorter | 2× shorter | Same length (no compression) |
| **Coherence** | Internally consistent, no contradictions | Minor tensions acknowledged | Some unresolved contradictions | Contradicts itself |
| **Coverage** | All aspects of question addressed | Most addressed, gaps noted | Major gaps acknowledged | Significant gaps unacknowledged |
| **Falsifiability** | All key claims falsifiable | Most falsifiable | Some falsifiable | Unfalsifiable narrative |
| **Actionability** | Clear actions for multiple stakeholders | Clear primary action | Suggestive but vague | No actionable implications |
| **Bias control** | Counter-sources sought, biases checked | Some bias checks | Minimal bias awareness | No bias checking |
| **Level clarity** | Level explicit, cross-level noted | Level mostly clear | Level implicit | Levels mixed without acknowledgment |

## Appendix B: Synthesis Record Template

```
SYNTHESIS RECORD

Title:        [From #405 compression]
Date:         [When]
Question:     [From #001]
Level:        [From #002]
Synthesizer:  [Who]

SOURCES:
  Count: [N] sources across [M] types
  Quality: [A: N, B: N, C: N, D: N]
  Diversity: [Which dimensions covered]
  Gaps: [Acknowledged gaps]

CORE INSIGHTS:
  1. [Insight] — [Evidence grade] — [Novel/Extracted/Added]
  2. [Insight] — [Evidence grade] — [Novel/Extracted/Added]
  3. [Insight] — [Evidence grade] — [Novel/Extracted/Added]

KEY TENSIONS RESOLVED:
  1. [Thesis vs Antithesis → Synthesis via Strategy]

MENTAL MODEL:
  [Name]: [Brief description]

PRINCIPLES:
  1. [Principle] — Context: [When it applies] — Falsifiable by: [What would disprove]

BOUNDARIES:
  This synthesis applies to: [Scope]
  This synthesis does NOT apply to: [Exclusions]
  
ACTIONS:
  1. [Action] → feeds into [Process]

META:
  Novelty ratio: [Genuine synthesis %]
  Compression: [Sources length vs synthesis length]
  Bias checks: [Performed? Results?]
  Falsifiable claims: [N/total]
  
DECAY:
  Review by: [Date]
  Kill criteria: [What would invalidate this]
```
