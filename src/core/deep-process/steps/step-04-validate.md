# Step 04: VALIDATE Phase

## Purpose
Execute Validator Agent to verify artifact before commit.

## Trigger
- ACT phase completed without conflicts
- Explicit validation request

## Execution

### Phase 4.1: Load Validation Context

```markdown
## Validation Context

📂 Loading artifact: {artifact_path}
📂 Loading system genes (from existing artifacts)

### Artifact Under Validation
- dp_id: {dp_id}
- dp_type: {dp_type}
- Current status: NOW

### Comparison Baseline
{for structural isomorphism}
Similar existing artifacts:
- {artifact_1} ({similarity_metric})
- {artifact_2} ({similarity_metric})
```

### Phase 4.2: Anti-Bias Checks

Execute mandatory anti-bias methods:

```markdown
## Anti-Bias Validation

### Method #56: Liar's Trap

📂 Loading method: `data/method-procedures/056_Liars_Trap.md`

**Deception Vectors Examined:**

Vector 1: {identified_vector}
- Evidence against: {evidence}
- Status: {CLEAR / FLAG}

Vector 2: {identified_vector}
- Evidence against: {evidence}
- Status: {CLEAR / FLAG}

Vector 3: {identified_vector}
- Evidence against: {evidence}
- Status: {CLEAR / FLAG}

**Result:** {PASS / FAIL}

---

### Method #59: CUI BONO Test

📂 Loading method: `data/method-procedures/059_CUI_BONO_Test.md`

| Decision | Beneficiary | Justification |
|----------|-------------|---------------|
| {decision_1} | {USER/AGENT/BOTH} | {why} |
| {decision_2} | {USER/AGENT/BOTH} | {why} |

**Red Flags:** {count}
**Result:** {PASS / FLAG}

---

### Method #60: Approval Gradient Test

📂 Loading method: `data/method-procedures/060_Approval_Gradient_Test.md`

| Claim | Truth ← → Approval | Score | Status |
|-------|-------------------|-------|--------|
| {claim_1} | {position} | {%} | {OK/FLAG} |
| {claim_2} | {position} | {%} | {OK/FLAG} |

**Max Score:** {%}
**Result:** {PASS / FLAG}
```

### Phase 4.3: Coherence Checks

Execute coherence methods:

```markdown
## Coherence Validation

### Method #93: DNA Inheritance Check

📂 Loading method: `data/method-procedures/093_DNA_Inheritance_Check.md`

| Gene | System Pattern | Artifact | Status |
|------|----------------|----------|--------|
| Naming | {pattern} | {actual} | {✅/❌} |
| Structure | {pattern} | {actual} | {✅/❌} |
| Style | {pattern} | {actual} | {✅/❌} |

**Mutations:** {count}
**Justified:** {yes/no}
**Result:** {PASS / FLAG}

---

### Method #95: Structural Isomorphism

📂 Loading method: `data/method-procedures/095_Structural_Isomorphism.md`

| Metric | Baseline | Artifact | Delta | Status |
|--------|----------|----------|-------|--------|
| Nesting | {x} | {y} | {%} | {✅/⚠️} |
| Sections | {x} | {y} | {%} | {✅/⚠️} |
| Lines | {x} | {y} | {%} | {✅/⚠️} |

**Over threshold (30%):** {count}
**Result:** {PASS / FLAG}

---

### Method #99: Multi-Artifact Coherence

📂 Loading method: `data/method-procedures/099_Multi_Artifact_Coherence.md`

| Check | Status | Issues |
|-------|--------|--------|
| Reference integrity | {✅/❌} | {broken refs} |
| Naming consistency | {✅/❌} | {inconsistencies} |
| Interface compatibility | {✅/❌} | {mismatches} |
| Duplication drift | {✅/❌} | {drift found} |

**Result:** {PASS / FAIL}

---

### Method #100: Vocabulary Consistency

📂 Loading method: `data/method-procedures/100_Vocabulary_Consistency.md`

**Synonyms found:** {list}
**Homonyms found:** {list}
**Undefined terms:** {list}

**Result:** {PASS / FLAG}
```

### Phase 4.4: Semantic Hash Verification

Verify content supports declared facts:

```markdown
## Semantic Hash Verification

| # | Fact | Content Support | Status |
|---|------|-----------------|--------|
| 1 | "{fact_1}" | Section 2, Line 15: "{quote}" | ✅ |
| 2 | "{fact_2}" | Section 3, Line 42: "{quote}" | ✅ |
| 3 | "{fact_3}" | NOT FOUND | ❌ VIOLATION |

**Violations:** {count}
**Result:** {PASS / FAIL}
```

### Phase 4.5: Verdict

Compile results and determine verdict:

```markdown
## Validation Verdict

### Results Summary

| Category | Methods | Status |
|----------|---------|--------|
| Anti-Bias | #56, #59, #60 | {PASS/FAIL/FLAG} |
| Coherence | #93, #95, #99, #100 | {PASS/FAIL/FLAG} |
| Semantic Hash | - | {PASS/FAIL} |

### Blockers
{list any BLOCK_ON_FAIL results}

### Flags (non-blocking)
{list any FLAG_ON_FAIL results}

### Final Verdict

**VERDICT: {COMMITTED / FAILED / CONDITIONAL}**

{if COMMITTED}
Artifact passes all checks. Ready for state update.
{end}

{if FAILED}
Artifact fails validation. Required fixes:
1. {fix_1}
2. {fix_2}
Return to ACT phase after fixes.
{end}

{if CONDITIONAL}
Artifact has warnings but no blockers:
- {warning_1}
- {warning_2}
Proceed with documented warnings? [Y/n]
{end}
```

## Decision Logic

### Verdict Rules

| Condition | Verdict |
|-----------|---------|
| Any BLOCK_ON_FAIL fails | FAILED |
| Semantic hash violation | FAILED |
| Only FLAG_ON_FAIL warnings | CONDITIONAL |
| All checks pass | COMMITTED |

## Output

The VALIDATE phase produces:
1. **Validation Report** with all method results
2. **Verdict** (COMMITTED, FAILED, or CONDITIONAL)
3. **Action items** if FAILED

## State Update

```
[UPDATE_STATE]
{
  "saga_id": "{current_saga}",
  "operations": [
    {"type": "VALIDATE", "target": "{dp_id}", "result": "{verdict}"}
  ],
  "flag_stale": []
}
[/UPDATE_STATE]
```

## Next Step

- **COMMITTED:** Proceed to **Step 05: SYNC**
- **FAILED:** Return to **Step 03: ACT** with fixes
- **CONDITIONAL:** Operator decides, then SYNC or ACT
