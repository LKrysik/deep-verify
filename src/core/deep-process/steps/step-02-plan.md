# Step 02: PLAN Phase

## Purpose
Analyze task type, inject appropriate methods, and create artifact skeleton.

## Trigger
- Operator selects "Update STALE" or "New artifact" from SENSE menu
- Migration process initiated

## Execution

### Phase 2.1: Task Analysis

Determine task type through analysis:

```markdown
## Task Analysis

**Task:** {user_provided_description}

### Type Detection

| Indicator | Present? | Task Type |
|-----------|----------|-----------|
| Code, API, technical design | {yes/no} | Technical |
| Vision, brainstorming, exploration | {yes/no} | Creative |
| External process import | {yes/no} | Migration |
| Quality, verification | {yes/no} | Validation |

**Detected Type:** {type}
```

### Phase 2.2: Method Injection

Based on task type, select methods:

```markdown
## Method Injection

**Task Type:** {detected_type}

### Injected Methods

| # | Method | Purpose |
|---|--------|---------|
{for technical}
| 87 | Falsifiability Check | Ensure claims are testable |
| 114 | Reversibility Test | Verify reasoning traceability |
| 154 | Definitional Contradiction | Detect impossible requirements |
{end}

{for creative}
| 71 | First Principles Analysis | Strip assumptions |
| 79 | Operational Definition | Make concepts measurable |
| 152 | Socratic Decomposition | Break into atomic questions |
{end}

{for migration}
| 90 | Dependency Topology Mapping | Find hidden couplings |
| 159 | Transitive Dependency Closure | Build full graph |
| 100 | Vocabulary Consistency | Standardize terms |
{end}

### Validation Methods (Always Applied)
| 56 | Liar's Trap | Anti-bias |
| 59 | CUI BONO Test | Anti-bias |
| 60 | Approval Gradient | Anti-bias |
| 93 | DNA Inheritance | Coherence |
| 95 | Structural Isomorphism | Coherence |
| 99 | Multi-Artifact Coherence | Coherence |
| 100 | Vocabulary Consistency | Coherence |
```

### Phase 2.3: Dependency Resolution

Identify what must be loaded:

```markdown
## Dependency Resolution

### For STALE Update

**Target:** {dp_id}
**Changed Parent:** {parent_id}

Dependencies to load:
{for each in depends_on}
  📂 {path} ({type})
{end}

### For New Artifact

**Probable dependencies based on type:**
{suggest dependencies based on artifact type}
```

### Phase 2.4: Skeleton Creation

Generate artifact skeleton with YAML header:

```markdown
## Skeleton Generation

**File:** artifacts/{path}/{name}.md

---
dp_id: "{TYPE}-{NAME}"
dp_type: "artifact"
dp_status: "NOW"
version: "3.6"

context:
  depends_on:
    - path: "{dependency_1}"
      type: "semantic_source"
    - path: "{dependency_2}"
      type: "hard_constraint"

semantic_hash:
  - "PLACEHOLDER: Replace with actual facts"

execution:
  active_methods: [{injected_methods}]
  logic_gates: {}

transaction:
  saga_id: "{new_saga_id}"
  previous_hash: "{hash_if_update}"
---

# {Title}

## Overview

{Content to be generated in ACT phase}

## Details

{Details section}
```

### Phase 2.5: Confirmation

Present plan to Operator:

```
═══════════════════════════════════════════════════════════════
  PLAN PHASE — Ready to Execute
═══════════════════════════════════════════════════════════════

Task: {description}
Type: {detected_type}

Methods to apply:
  • #{method_1}: {name_1}
  • #{method_2}: {name_2}
  • #{method_3}: {name_3}

Dependencies to load:
  • {dep_1}
  • {dep_2}

Output file: {path}

Proceed? [Y/n]
```

## Decision Logic

### Task Type Heuristics

| Signal | Type |
|--------|------|
| Contains "implement", "build", "code", "API" | Technical |
| Contains "design", "explore", "vision", "brainstorm" | Creative |
| Contains "import", "migrate", "transform", "convert" | Migration |
| Contains "verify", "audit", "check", "validate" | Validation |

### Method Selection Override

Operator can override method selection:
```
Default methods for {type}: [{default_methods}]
Add methods? (comma-separated numbers, or Enter to accept):
Remove methods? (comma-separated numbers, or Enter to skip):
```

## State Update

Update state with new artifact in NOW status:

```
[UPDATE_STATE]
{
  "saga_id": "{new_saga_id}",
  "operations": [
    {"type": "CREATE", "target": "{dp_id}", "path": "{path}"}
  ],
  "flag_stale": []
}
[/UPDATE_STATE]
```

## Output

The PLAN phase produces:
1. **Artifact skeleton** with YAML header
2. **Method list** for Implementation Agent
3. **Dependency list** to load in ACT phase

## Next Step

Proceed to **Step 03: ACT** with:
- Skeleton file path
- Injected methods
- Dependency paths
