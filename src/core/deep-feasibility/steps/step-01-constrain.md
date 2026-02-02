---
step: 1
name: "Constrain"
time_estimate: "30-60 minutes"
goal: "Identify hard vs soft limits, contradictions, structural blocks"
requires_completion: [0]
next_steps:
  DEFAULT: "steps/step-02-assess.md"
  H5_FOUND: "EARLY_EXIT — impossibility detected"
  SCOPE_CHANGE: "steps/step-00-frame.md"
data_dependencies:
  - "data/method-procedures/101-106*.md"
  - "data/constraint-patterns.yaml"
  - "data/theoretical-foundations.yaml"
outputs:
  - constraint_map
  - impossibility_flags
  - contradictions
  - variety_gap
---

# Phase 1: CONSTRAIN

## MANDATORY EXECUTION RULES

1. **EXECUTE ALL METHODS** (or depth-adjusted subset)
2. **H5 = STOP** — If impossible found, don't continue that path
3. **CHECK PATTERNS** — Load `data/constraint-patterns.yaml` for known impossibilities
4. **RECORD EVERYTHING** — Each constraint classified H0-H5

---

## 1.1 Constraint Hardness Spectrum (#101)

**Load:** `data/method-procedures/101_Constraint_Hardness_Spectrum.md`

**Purpose:** Classify every constraint from absolutely impossible to merely inconvenient. Prevents two errors:
1. Treating hard impossibilities as "challenges to overcome"
2. Treating soft difficulties as hard impossibilities

### The Hardness Spectrum

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONSTRAINT HARDNESS LEVELS                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  H5 — LOGICALLY IMPOSSIBLE                                                  │
│       Violates mathematics, logic, physics                                  │
│       Examples: Halting problem, perpetual motion, FLP consensus           │
│       Response: STOP. Redesign. This cannot be overcome with effort.       │
│                                                                              │
│  H4 — COMPUTATIONALLY INFEASIBLE                                            │
│       NP-hard at scale, no good approximation known                         │
│       Examples: Optimal scheduling for 10K variables, exact TSP             │
│       Response: Approximate, decompose, use heuristics                      │
│                                                                              │
│  H3 — STRUCTURALLY BLOCKED                                                  │
│       Organization or architecture prevents execution                       │
│       Examples: Conway misalignment, no decision authority                  │
│       Response: Restructure org OR change architecture to match             │
│                                                                              │
│  H2 — RESOURCE CONSTRAINED                                                  │
│       Lack of people, money, time, skills                                   │
│       Examples: Need 5 specialists, have 2; budget cut                      │
│       Response: Acquire, trade, defer, reduce scope                         │
│                                                                              │
│  H1 — PRACTICALLY DIFFICULT                                                 │
│       Doable but hard, risky, expensive                                     │
│       Examples: Migrate legacy system with no docs                          │
│       Response: Plan carefully, accept cost, manage risk                    │
│                                                                              │
│  H0 — INCONVENIENT                                                          │
│       Minor friction, easily overcome                                       │
│       Examples: Need to learn new API, different time zone                  │
│       Response: Just do it                                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Execution Process

1. **Gather constraints** from:
   - Deep-Explore outputs (if available)
   - Stakeholder requirements
   - Technical analysis
   - Regulatory environment
   - Resource inventory

2. **Classify each constraint:**

```
For each constraint:
  □ What level is it? (H0-H5)
  □ What's the evidence for this classification?
  □ Could we be misclassifying?
  □ What would change the classification?
```

3. **Check for misclassification risks:**

| Red Flag | Risk |
|----------|------|
| Team treating H5 as H2 | "If we just work harder..." — waste |
| Team treating H1 as H5 | "It's impossible" when just inconvenient — paralysis |
| No H4/H5 constraints found | Possible blind spot — are we seeing everything? |

### Record Constraints

```yaml
constraints:
  - constraint: "[Description]"
    hardness: "H5"  # H0-H5
    nature: "[Why this level]"
    evidence: "[Supporting evidence]"
    response_strategy: "[What to do about it]"
    misclassification_risk: "[What could we be wrong about]"
```

**EARLY EXIT:** If H5 found for a required capability → that path is infeasible. Recommend redesign or reframe.

---

## 1.2 Requisite Variety Audit (#102)

**Load:** `data/method-procedures/102_Requisite_Variety_Audit.md`

**Purpose:** Measure whether team/tools/process have enough VARIETY to control problem complexity. Based on Ashby's Law: controller must have at least as many response options as system has disturbance types.

### Execution Process

1. **Enumerate PROBLEM DIMENSIONS** — every independent axis of complexity:

```
□ Technologies involved (languages, platforms, services)
□ Domains required (data engineering, security, compliance, UX, business)
□ Integration points (APIs, databases, services, organizations)
□ Failure modes that must be handled
□ Stakeholder perspectives to satisfy
□ Regulatory requirements
□ Scale dimensions (data volume, users, transactions)
```

2. **Enumerate TEAM VARIETY** — response capabilities:

```
□ Skills present on team
□ Tools available and mastered
□ Decision authority held
□ Time available for learning
□ Access to external expertise
□ Organizational support
```

3. **Compare — for each problem dimension:**
   - Does team have corresponding capability?
   - If partial, how big is the gap?
   - Can gap be closed in available time?

### Calculate Variety Gap

```
Variety Gap = Problem Dimensions - Team Capabilities

If gap > 0:
  → Project is INFEASIBLE without acquiring missing variety
  → Options: hire, train, outsource, simplify problem, accept risk
```

### Record Variety Audit

```yaml
variety_audit:
  problem_dimensions:
    - dimension: "Databricks"
      covered: true
    - dimension: "EPR regulations"
      covered: false
      gap_closable: "Uncertain — need domain expert"

  team_capabilities:
    - capability: "Python"
      level: "strong"
    - capability: "Synapse"
      level: "partial"

  variety_gap:
    - "EPR regulations (missing)"
    - "Synapse optimization (partial)"

  feasibility_given_gap: "CONDITIONAL — need EPR expert"
```

---

## 1.3 TRIZ Contradiction Detection (#103)

**Load:** `data/method-procedures/103_TRIZ_Contradiction_Detection.md`

**Purpose:** Search for contradictions in requirements that signal fundamental design conflicts. Unresolved contradiction = infeasibility OR innovation opportunity.

### Types of Contradictions

**TECHNICAL CONTRADICTION:** Improving parameter X worsens parameter Y
- "Must be real-time AND process massive batches" (speed vs throughput)
- "Must be fully secure AND zero-friction UX" (security vs usability)
- "Must be highly available AND strongly consistent" (CAP theorem)

**PHYSICAL CONTRADICTION:** Element must have property A AND NOT-A simultaneously
- "Data must be encrypted AND queryable" (encrypted AND readable)
- "System must be simple AND handle all edge cases" (simple AND comprehensive)
- "Pipeline must be idempotent AND exactly-once" (retryable AND non-duplicating)

### Execution Process

1. **For each pair of requirements:** Does satisfying R1 conflict with R2?

2. **If yes:** Classify as technical or physical contradiction

3. **For technical contradictions** — try TRIZ separation principles:
   - Separation in TIME: "Real-time for latest, batch for historical"
   - Separation in SPACE: "Encrypt at rest, decrypt in secure enclave"
   - Separation in SCALE: "Simple API surface, complex internal logic"
   - Separation in CONDITION: "Available normally, consistent during writes"

4. **For physical contradictions:**
   - If no separation resolves it AND maps to a theorem (CAP, FLP) → H5 impossible
   - Hand off to Deep-Verify for confirmation

### Record Contradictions

```yaml
contradictions:
  - r1: "Must provide real-time updates"
    r2: "Must process 10M records/hour"
    type: "technical"
    triz_resolution_attempted: "Separation in time"
    resolved: true
    resolution_method: "Stream recent data, batch historical"

  - r1: "Strong consistency"
    r2: "High availability"
    r3: "Partition tolerance"
    type: "physical (CAP)"
    triz_resolution_attempted: "None applicable"
    resolved: false
    note: "H5 — CAP theorem. Must choose 2 of 3."
```

**IF unresolved contradiction maps to known theorem → flag as H5**

---

## 1.4 Conway Alignment Check (#104)

**Load:** `data/method-procedures/104_Conway_Alignment_Check.md`

**Purpose:** Assess whether required architecture is compatible with organizational structure. Misalignment = structural infeasibility (H3).

### Execution Process

1. **Map required system architecture:**
   - Components
   - Interfaces between components
   - Data flows
   - Decision points

2. **Map organizational structure:**
   - Teams
   - Reporting lines
   - Communication channels
   - Decision authority

3. **For each architectural interface:**
   - Does a corresponding org communication channel exist?
   - Is the channel adequate for the integration complexity?

### Alignment Assessment

| Architecture Needs | Org Has | Assessment |
|-------------------|---------|------------|
| Tight integration A↔B | Daily standups X↔Y | ALIGNED |
| Tight integration A↔B | Monthly reviews X↔Y | MISALIGNED |
| Loose coupling A→B | Async communication | ALIGNED |
| Shared ownership A+B | Siloed teams | MISALIGNED |

### Record Conway Check

```yaml
conway_check:
  - arch_interface: "Databricks pipeline ↔ Synapse reporting"
    org_channel: "Monthly review meetings"
    aligned: false
    resolution: "Either create daily sync OR redesign for loose coupling"

  - arch_interface: "Data ingestion → Storage"
    org_channel: "Same team"
    aligned: true
```

**IF misaligned AND cannot change org → must change architecture**

---

## 1.5 Regulatory Feasibility Scan (#105)

**Load:** `data/method-procedures/105_Regulatory_Feasibility_Scan.md`

**Purpose:** Determine whether project is LEGALLY PERMITTED. Regulatory constraints are often H5 — cannot be overcome by effort.

### Execution Process

1. **Identify all regulatory jurisdictions:**
   - Geographic (EU, US, specific countries)
   - Industry (HIPAA, PCI-DSS, SOX)
   - Domain (GDPR, CCPA, EPR)

2. **For each jurisdiction, map requirements:**

| Activity | Required | Permitted | Restricted | Prohibited |
|----------|----------|-----------|------------|------------|
| Data storage | □ | □ | □ | □ |
| Data transfer | □ | □ | □ | □ |
| Processing | □ | □ | □ | □ |
| Retention | □ | □ | □ | □ |

3. **Check for regulatory contradictions:**
   - Jurisdiction A requires X
   - Jurisdiction B prohibits X
   - → May need jurisdiction-specific design

4. **Assess regulatory stability:**
   - Is this regulation likely to change during project?
   - What's the risk of non-compliance?

### Record Regulatory Map

```yaml
regulatory_map:
  - regulation: "GDPR"
    jurisdiction: "EU"
    requirements:
      - "Data minimization"
      - "Right to erasure"
    prohibitions:
      - "Transfer to non-adequate countries without SCCs"
    status: "Must comply"
    stability: "Stable"

  - regulation: "EPR"
    jurisdiction: "EU"
    requirements:
      - "Packaging data reporting"
    status: "New requirement — evolving"
```

**IF prohibited activity is required → H5 infeasible**

---

## 1.6 Precedent Existence Check (#106)

**Load:** `data/method-procedures/106_Precedent_Existence_Check.md`

**Purpose:** Has anyone done something substantially similar before? Precedent = evidence of feasibility. No precedent = warning (not proof of infeasibility, but requires investigation).

### Execution Process

1. **Define core capability/outcome** being assessed

2. **Search for precedents:**
   - Same domain
   - Adjacent domains
   - Analogous problems

3. **Classify precedents:**

| Type | Evidence Strength | Example |
|------|------------------|---------|
| **Direct** | STRONG | Someone did essentially this |
| **Analogous** | Moderate | Similar in different domain |
| **Partial** | Each part exists | Components exist, combination novel |
| **None** | WARNING | Nobody has done this |

4. **For each precedent:**
   - What was their context? (team, timeline, budget, tools)
   - How does ours compare?
   - What can we learn from their experience?

### Record Precedents

```yaml
precedents:
  - capability: "Delta Lake for regulatory reporting"
    precedent_type: "direct"
    context: "Company X, similar team size, 6 months"
    comparison: "Our scope is larger but tech is same"
    evidence_strength: "strong"

  - capability: "ML-based data quality detection"
    precedent_type: "partial"
    context: "Components exist separately"
    comparison: "Novel combination for this domain"
    evidence_strength: "uncertain — needs probe"
```

**IF no precedent AND novel combination:**
→ Composition feasibility (#206) is the key question
→ Consider probe design (#303)

---

## 1.7 Depth Adjustments

### Quick Depth
Execute: #101, #102, #106 only
Skip: #103, #104, #105

### Standard+ Depths
Execute: All six methods

---

## 1.8 Update Frontmatter

After completing CONSTRAIN:

```yaml
constraints_found:
  - constraint: "..."
    hardness: "H3"
    resolution: "..."

variety_gap:
  gap_items: ["EPR regulations", "Synapse expertise"]
  gap_closable: "Conditional"

contradictions:
  - type: "technical"
    resolved: true

impossibility_flags:
  - "None"  # or list H5 constraints

steps_completed: [0, 1]
current_step: 2
```

---

## 1.9 Proceed to ASSESS

**Before loading Step 2, verify:**

- [ ] All constraints classified (H0-H5)
- [ ] Variety audit complete
- [ ] Contradictions checked (and resolved or flagged)
- [ ] Conway alignment assessed
- [ ] Regulatory scan complete (if applicable)
- [ ] Precedents checked
- [ ] No unaddressed H5 constraints blocking progress

**Next step:** Load `steps/step-02-assess.md`

**Navigation:**
- ↓ PROCEED if constraints mapped and no blocking H5
- ↓ EARLY EXIT if H5 found on required path → recommend redesign
- ↑ RETURN TO STEP 0 if scope needs refinement

---

## Output Checklist

Before proceeding, confirm:

- [ ] `constraints_found` populated with all constraints and hardness levels
- [ ] `variety_gap` calculated and documented
- [ ] `contradictions` list complete (resolved or flagged)
- [ ] `impossibility_flags` set (empty or with H5 items)
- [ ] Ready to assess 10 feasibility dimensions
