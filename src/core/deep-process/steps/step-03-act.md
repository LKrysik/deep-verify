# Step 03: ACT Phase

## Purpose
Execute content generation with Implementation Agent, applying injected methods.

## Trigger
- Plan phase completed and confirmed
- Skeleton file created with YAML header

## Execution

### Phase 3.1: Load Context

```markdown
## Context Loading

📂 Loading `data/enforcer.md` (BIOS)
📂 Loading skeleton: {artifact_path}

### Dependencies
{for each dependency in depends_on}
📂 Loading {dependency.path}
   Type: {dependency.type}
   Status: {dependency.status}
   Semantic Hash:
   {for each fact in dependency.semantic_hash}
     - "{fact}"
   {end}
{end}
```

### Phase 3.2: Method Execution

Apply each injected method sequentially:

```markdown
## Method Execution

### Method #{method_1}: {name_1}

📂 Loading method procedure: {file}

**Execution:**
{method-specific output following procedure template}

**Findings:**
- {finding_1}
- {finding_2}

---

### Method #{method_2}: {name_2}

📂 Loading method procedure: {file}

**Execution:**
{method-specific output}

**Findings:**
- {finding_1}

---

{repeat for all methods}
```

### Phase 3.3: Content Generation

Generate content informed by method outputs:

```markdown
## Content Generation

### Constraints from Methods

| Method | Constraint | Applied How |
|--------|------------|-------------|
| #87 | All claims must be falsifiable | Each claim has test criteria |
| #114 | Reasoning must be reversible | Sources cited for all decisions |
| #154 | No definitional contradictions | Requirements cross-checked |

### Content Sections

{Generate actual content for each section in skeleton}

## Overview

{Generated overview that:
- Addresses all parent semantic_hash facts
- Incorporates method findings
- Avoids banned words without quantification
}

## Details

{Generated details that:
- Follow method constraints
- Include specific, measurable claims
- Cite dependencies where relevant
}
```

### Phase 3.4: Semantic Hash Generation

Extract facts from generated content:

```markdown
## Semantic Hash Generation

### Extracted Facts

From content, the following facts MUST remain true:

1. "{Category}: {Specific fact}"
   - Source: Section {X}, Line {Y}
   - Falsifiable: Yes, test by {method}

2. "{Category}: {Specific fact}"
   - Source: Section {X}
   - Falsifiable: Yes, test by {method}

3. "{Category}: {Specific fact}"
   - Source: {location}
   - Falsifiable: Yes

### Semantic Hash (for YAML)

```yaml
semantic_hash:
  - "{fact_1}"
  - "{fact_2}"
  - "{fact_3}"
```
```

### Phase 3.5: Self-Validation

Quick validation before passing to Validator:

```markdown
## Self-Validation Checklist

### #114 Reversibility Check
[ ] All conclusions trace back to sources
[ ] No "obvious" or "everyone knows" statements
[ ] Calculations shown, not just results

### #87 Falsifiability Check
[ ] No banned words without quantification
[ ] Each claim has disproof criteria
[ ] No unfalsifiable claims

### Conflict Scan
[ ] No contradictions with parent hashes
[ ] No definitional impossibilities (#154)
[ ] Dependencies don't conflict

### Result
{PASS → proceed to VALIDATE}
{CONFLICT DETECTED → create Decision Point, HALT}
```

### Phase 3.6: Handle Conflicts

If conflict detected:

```markdown
## Conflict Detected

**Method:** #{detecting_method}
**Type:** {contradiction_type}

### Conflicting Elements

**Element A:** (from {source_a})
> "{quoted_text_a}"

**Element B:** (from {source_b})
> "{quoted_text_b}"

### Analysis
{Why these conflict}

### Action
Creating Decision Point: DP-{sequence}

---

{Generate Decision Point artifact}

---

**STATUS:** HALTED - Awaiting user input on DP-{sequence}
```

## Output

The ACT phase produces:
1. **Completed artifact** with content and semantic_hash
2. **Method execution records** for audit trail
3. **Decision Points** if conflicts detected

## State Update

```
[UPDATE_STATE]
{
  "saga_id": "{current_saga}",
  "operations": [
    {"type": "UPDATE", "target": "{dp_id}", "path": "{path}"}
  ],
  "flag_stale": []
}
[/UPDATE_STATE]
```

## Next Step

- **If no conflicts:** Proceed to **Step 04: VALIDATE**
- **If conflict:** Wait for Decision Point resolution, then re-run ACT
