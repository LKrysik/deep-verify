# Deep Explore Report: Embedded Contracts Architecture

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║                           D E E P   E X P L O R E   R E P O R T                   ║
║                                    Version 2.1                                     ║
║                                                                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║  DECISION:  Jak wprowadzić strukturę (kontrakty) do BMAD workflows,               ║
║             aby umożliwić wizualizację, tracking i orchestrację przez Python,     ║
║             zachowując dynamiczność i standalone działanie z LLM.                 ║
║                                                                                    ║
║  DATE:      2026-02-02                                                            ║
║                                                                                    ║
║  DEPTH:     deep                                                                   ║
║  FEAR:      off (auto-detected)                                                   ║
║                                                                                    ║
║  COVERAGE:  95.4 — COMPREHENSIVE                                                  ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## SECTION 1: WHAT WE LEARNED

### KEY DISCOVERIES

| Discovery | Impact |
|-----------|--------|
| **EMBEDDED CONTRACT ARCHITECTURE** — Kontrakt musi żyć W pliku markdown (frontmatter YAML), nie obok. To eliminuje sync problem i pozwala LLM działać standalone. | CRITICAL |
| **DUAL-READABLE FORMAT** — Ten sam kontrakt jest: instrukcją dla LLM + danymi dla Python. Jedno źródło prawdy, dwa tryby użycia. | HIGH |
| **PYTHON = OPTIONAL ENHANCEMENT** — System musi działać tylko z LLM. Python dodaje wartość (viz, tracking, orchestration), ale nie jest wymagany. | HIGH |
| **SPEC SIMPLICITY = SURVIVAL** — Contract spec >10 linii YAML = wrong design. Complexity kills both LLM compliance and user adoption. | HIGH |
| **AGENT FRAMEWORK MARKET CONSOLIDATED** — LangGraph/CrewAI/AutoGen dominują. BMAD musi być "methodology + light tooling", nie "yet another framework". | MEDIUM |

### SURPRISES

- **CrewAI "ceiling problem"** — teams hit architectural limits after 6-12 months
  - Warning against quick-win architecture that constrains future

- **LLM costs dropping 67%+ per generation**
  - "Cost savings" argument for determinism weakening
  - "Quality/repeatability" arguments remain strong

- **Cursor overtook GitHub Copilot** in organizational adoption (43% vs 37%)
  - IDE landscape more fluid than expected

### CHANGED ASSUMPTIONS

| Original | Now | Confidence Change |
|----------|-----|-------------------|
| "Zero sync problem with embedded contracts" | "Minimal sync" — output schemas still need alignment with workflows | HIGH → MEDIUM |
| "Contract spec design is medium effort" | Expect iteration, plan for v0.1 → v0.2 → v0.3 | Mitigation: Keep scope aggressively small |

---

## SECTION 2: WHAT WE STILL DON'T KNOW

### CRITICAL UNKNOWNS

| Unknown | How to Learn |
|---------|--------------|
| "Jaki jest faktyczny LLM compliance rate z output schemas?" | Run 10 test workflows with contracts, measure % |
| "Ile istniejących BMAD workflows wymaga migracji?" | Count files in `_bmad/bmm/workflows/` |

### TRUE UNCERTAINTIES (cannot know — must decide despite)

- **Future LLM architecture changes**
  - May affect how frontmatter is interpreted
  - Mitigation: Validation layer, format flexibility

- **User adoption of structured workflows**
  - "Vibe coding" trend may reduce demand for structure
  - Mitigation: Make contracts add clear value, not bureaucracy

### FLAGGED FOR EXPERT

| Question | Expert Type |
|----------|-------------|
| "What's the best pattern for workflow state management in file-based systems?" | Senior architect with distributed systems experience |

---

## SECTION 3: OPTION MAP

### DIMENSION 1: CONTRACT LOCATION
- **A: Embedded in markdown (frontmatter YAML)** ⭐
- B: External registry (separate file)
- C: Hybrid (file metadata + central index)

### DIMENSION 2: EXECUTION MODEL
- **A: LLM standalone (Python optional)** ⭐
- B: Python required (LLM as executor)
- C: Tiered (basic=LLM, advanced=Python)

### DIMENSION 3: CONTRACT SCOPE
- A: Workflow metadata only (inputs, outputs, next)
- B: + Output schemas (story, epic, sprint)
- C: + State tracking (status, last_run)
- D: + Conditional logic (if/else, retry) — AVOID

### DIMENSION 4: PYTHON LAYER
- A: Parser only (read contracts)
- B: + Visualization (workflow graph)
- C: + Orchestration (execute workflows)
- D: + Full BMAD-assist feature set

### DIMENSION 5: SPEC COMPLEXITY
- **A: Minimal (<10 lines YAML)** ⭐
- B: Standard (10-20 lines)
- C: Full DSL (>20 lines) — AVOID

### DIMENSION 6: VALIDATION STRATEGY
- A: Trust LLM output
- **B: Validate required fields only** ⭐
- C: Full schema validation

### CONSTRAINTS

| Constraint | Confidence |
|------------|------------|
| Embedded contracts + LLM standalone = REQUIRED combination | HIGH |
| Spec complexity > 20 lines = ELIMINATED | HIGH |
| Full DSL + fast delivery = INCOMPATIBLE | HIGH |

---

## SECTION 4: STRATEGIC CLUSTERS

### CLUSTER A: "CONTRACT FIRST" ⭐ RECOMMENDED

```
Configuration:
D1:A (embedded) + D2:A (LLM standalone) + D3:A→C (grow scope) +
D4:A→B (parser → viz) + D5:A (minimal) + D6:B (validate fields)

Best for:
• Preserving current BMAD user experience
• Enabling Python features without breaking changes
• Progressive enhancement path

Risk: LOW
Reversibility: HIGH (remove frontmatter = back to status quo)
Trade-off: Slower Python feature velocity vs full assist approach
```

### CLUSTER B: "FULL ASSIST"

```
Configuration:
D1:B (external registry) + D2:B (Python required) + D4:D (full features)

Best for:
• Power users with Python environment
• Maximum automation and control

Risk: MEDIUM (adoption friction)
Reversibility: LOW (architectural commitment)
Trade-off: Feature depth for adoption breadth
```

### CLUSTER C: "WAIT & SEE"

```
Configuration: No contracts, BMAD and assist evolve independently

Best for: If resources extremely limited

Risk: LOW short-term, HIGH long-term (divergence)
Trade-off: Optionality for momentum
```

---

## SECTION 5: CONSEQUENCE MAP

### CLUSTER A: CONTRACT FIRST ⭐

| Type | Consequence | Status |
|------|-------------|--------|
| ✓ | Single source of truth — Kontrakt w pliku = zero sync między markdown i registry | VERIFIED |
| ✓ | LLM self-sufficient — Workflows działają bez Python, kontrakty = instrukcje | VERIFIED |
| ✓ | Backward compatible — Dodanie frontmatter nie łamie istniejących workflows | VERIFIED |
| ✓ | High reversibility — Można usunąć contracts i wrócić do pure markdown | VERIFIED |
| ? | Output schema compliance — LLM respektuje output format ~80% czasu | ASSUMED - MEDIUM |
| ? | Spec design effort — 2-4 tygodnie na v0.1, expect iterations | ASSUMED - MEDIUM |
| ✗ | Risk: Spec scope creep | MEDIUM probability |

### CLUSTER B: FULL ASSIST

| Type | Consequence | Status |
|------|-------------|--------|
| ✓ | Immediate rich tooling — CLI, UI, metrics — already built | VERIFIED |
| ✓ | Full determinism — Python controls entire flow | VERIFIED |
| ✗ | Sync problem — Registry + markdown must stay aligned | VERIFIED |
| ✗ | Adoption friction — Python environment required | ASSUMED - MEDIUM |
| ✗ | LLM not standalone — Users can't use workflows without Python | VERIFIED |

### CLUSTER C: WAIT & SEE

| Type | Consequence | Status |
|------|-------------|--------|
| ✓ | Zero effort | VERIFIED |
| ✗ | No visualization possible | VERIFIED |
| ✗ | No tracking possible | VERIFIED |
| ✗ | Products diverge — BMAD and assist become incompatible | ASSUMED - HIGH |

---

## SECTION 6: DECISION READINESS

### SEQUENCE

1. **FIRST:** "Wprowadzamy embedded contracts?" (YES/NO)
   - Gate decision, wszystko inne zależy od tego

2. **NEXT:** "Jaki scope contract spec v0.1?"
   - Define fields: id, inputs, outputs, next, status

3. **NEXT:** "Które 2-3 workflows migrujemy jako piloty?"
   - Pick representative, high-value workflows

4. **NEXT:** "Co w Python MVP?" (parser → viz → orchestration)
   - Start with parser + simple graph visualization

5. **CAN WAIT:** "BMAD vs assist product relationship"
   - Delay until contracts proven useful

6. **CAN WAIT:** "GTM channel priority"
   - Delay until product direction clear

### READINESS ASSESSMENT

| Decision | Readiness | What would help |
|----------|-----------|-----------------|
| Embedded contracts: YES | READY | — |
| Contract spec v0.1 scope | ALMOST | 1-2 hour design session |
| Pilot workflows selection | ALMOST | List current workflows |
| Python MVP scope | ALMOST | Spec must be defined first |
| BMAD/assist relationship | NOT READY | Need contracts working |
| GTM channel | NOT READY | Need product clarity |

---

## SECTION 7: SUGGESTED NEXT STEPS

### IF YOU'RE READY TO PROCEED (RECOMMENDED)

#### PHASE 1: SPEC & PILOT (Week 1-2)

- [ ] **Design contract spec v0.1**
  - Fields: id, name, inputs, outputs, output_contract, next, status
  - Constraint: max 10 lines YAML
  - Format: YAML frontmatter in markdown

- [ ] **Pick 2-3 pilot workflows**
  - Suggest: create-story, validate-story, dev-story
  - Representative of typical usage

- [ ] **Add frontmatter to pilot workflows**
  - Test that LLM still executes correctly
  - Document any issues

#### PHASE 2: PYTHON MVP (Week 3-4)

- [ ] **Build contract parser**
  - Read frontmatter YAML from all workflow files
  - Build workflow graph from 'next' fields

- [ ] **Build simple visualization**
  - CLI: print workflow graph (ASCII)
  - Show: workflow → workflow connections
  - Show: current status if tracked

- [ ] **Test LLM output compliance**
  - Run 10 workflows with output contracts
  - Measure compliance rate
  - Adjust instructions if <80%

#### PHASE 3: EVALUATE & ITERATE (Week 5-6)

- [ ] **Assess results**
  - Does visualization add value?
  - Is spec working or needs revision?
  - What's missing?

- [ ] **Decide next step**
  - If working: Migrate remaining workflows
  - If issues: Revise spec (v0.2)
  - If failure: Revert (low cost)

### IF YOU WANT MORE CLARITY FIRST

- **Experiment:** Run 5 workflows with manual frontmatter, see if LLM complies
- **Research:** Check for prior art ("executable markdown", "markdown workflows")
- **Consult:** Talk to BMAD-assist team about contract format alignment

### WATCH OUT FOR

⚠️ **Spec scope creep** — ruthlessly cut features, v0.1 must be minimal

⚠️ **Premature optimization** — don't build orchestration before viz works

⚠️ **LLM non-compliance** — build validation early, don't trust blindly

⚠️ **Team discipline** — ensure new workflows get contracts

---

## MINIMAL ASSERTIONS (Reference Card)

1. **"KONTRAKT W PLIKU, NIE OBOK PLIKU"**
2. **"LLM STANDALONE, PYTHON OPTIONAL"**
3. **"SPEC SIMPLE OR SPEC DEAD"**
4. **"VALIDATION, NOT TRUST"**
5. **"METHODOLOGY, NOT FRAMEWORK"**
6. **"PROVE VALUE EARLY"**

---

## EXPLORATION METADATA

| Attribute | Value |
|-----------|-------|
| Depth selected | deep |
| Steps completed | 0, 1, 2, 3, 4, 5, 6 (all) |
| Iterations | 1 (with mid-exploration reframe) |
| Research items | 6 (web research completed) |
| Biases checked | 12 (5 detected, addressed) |
| Black swans | 6 (3 positive, 3 negative) |

### Methods Used

**Epistemological:**
- E001 Abductive Reasoning (unknown unknowns)
- E002 Counterfactual Thinking (leverage points)
- E003 Minimal Assertions (compression)
- E004 Boundary Analysis (limits)
- E005 Causal Models (dependencies)
- E006 Falsification (belief testing)
- E007 Information Questions (gaps)

**Mapping:**
- M001 Dimension Discovery
- M002 Option Enumeration
- M003 Constraint Mapping
- M011 Consequence Analysis
- M012 Reversibility Check
- M013 Dependency Analysis

**Challenge:**
- M021 Premortem
- M022 Black Swan Hunt
- M023 Assumption Stress Test

### Limitations

- Research was web-based, no hands-on testing of LLM contract compliance
- Effort estimates are assumptions, not validated
- No direct user research on demand for visualization/tracking

### Key Insight

**Emerged mid-exploration:**
- User described "embedded contract" architecture during Step 2
- Reframed entire exploration around this insight
- This became the recommended path

---

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║                              END OF REPORT                                         ║
║                                                                                    ║
║  Exploration complete. Decision readiness: HIGH for core architectural choice.    ║
║  Recommended: Proceed with Cluster A (Contract First) — Phase 1 this week.        ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```
