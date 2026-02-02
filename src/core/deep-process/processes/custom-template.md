# Process: Custom Template

> **ID:** custom-{your-name}
> **Version:** 1.0
> **Domain:** {Your Domain}
> **Goal:** {What this process achieves}

---

## HOW TO USE THIS TEMPLATE

1. Copy this file to `processes/{your-process-name}.md`
2. Replace all `{placeholders}` with your values
3. Define your phases (3-7 recommended)
4. Define steps within each phase
5. Define gates between phases
6. Test with a real project

---

## METADATA

```yaml
id: {process-id}
version: "1.0"
domain: {your-domain}

phases:
  - {phase-1}
  - {phase-2}
  - {phase-3}
  # Add more as needed

integrations:
  # Define integrations if needed
  # Example:
  # tool_name:
  #   supported: true
  #   via: bash  # or mcp
```

---

## ENFORCEMENT

> **WAŻNE:** Przed wykonaniem CZEGOKOLWIEK przeczytaj `engine/enforcer.md`

### Reguły specyficzne dla tego procesu

```yaml
rules:
  - rule: "{Rule name}"
    check: "{What to check}"
    on_violation: BLOCK  # or WARN

  # Add more rules as needed
```

---

## PHASE 1: {PHASE_NAME}

### Purpose
{What this phase achieves - 1-2 sentences}

### Entry Conditions
```yaml
requires:
  state:
    - "Project initialized"
  artifacts:
    - "{required artifact if any}"
```

### Steps

#### Step 1.1: {Step Name}

```yaml
id: {step-id}
name: "{Step name}"

requires:
  artifacts:
    - "{required artifact}"

produces:
  artifacts:
    - path: "{output artifact path}"

instructions: |
  1. {First action}
  2. {Second action}
  3. {Third action}
  # Add more steps as needed

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: {progress after this step}"
```

#### Step 1.2: {Another Step}

```yaml
id: {step-id}
name: "{Step name}"

# ... follow same structure
```

### Exit Gate: {phase1}_to_{phase2}

```yaml
gate:
  name: {phase1}_to_{phase2}
  threshold: 0.70  # Adjust as needed (0.0 - 1.0)

  criteria:
    - name: "{Criterion 1}"
      weight: 0.30
      check: "{What to verify}"

    - name: "{Criterion 2}"
      weight: 0.30
      check: "{What to verify}"

    - name: "{Criterion 3}"
      weight: 0.40
      check: "{What to verify}"

  # Weights must sum to 1.0
```

---

## PHASE 2: {PHASE_NAME}

### Purpose
{What this phase achieves}

### Entry Conditions
```yaml
requires:
  gates:
    - "{previous_gate}: passed"
  artifacts:
    - "{required artifacts from previous phase}"
```

### Steps

#### Step 2.1: {Step Name}

```yaml
# ... follow same structure as Phase 1 steps
```

### Exit Gate: {phase2}_to_{phase3}

```yaml
# ... follow same structure as Phase 1 gate
```

---

## PHASE N: {FINAL_PHASE_NAME}

### Purpose
{What this phase achieves - typically verification/completion}

### Steps

#### Step N.1: {Final verification or output}

### Exit Gate: {process}_complete

```yaml
gate:
  name: {process}_complete
  threshold: 0.80

  criteria:
    - name: "All outputs produced"
      weight: 0.50
      check: "All expected artifacts exist"

    - name: "Quality verified"
      weight: 0.50
      check: "Quality criteria met"
```

---

## ARTIFACTS SUMMARY

| Artifact | Phase | Purpose |
|----------|-------|---------|
| {artifact-1} | {Phase} | {Purpose} |
| {artifact-2} | {Phase} | {Purpose} |
| {artifact-3} | {Phase} | {Purpose} |

---

## STATE TRANSITIONS

```
# Draw your phase flow diagram

┌──────────┐     {threshold}    ┌──────────┐
│ {PHASE1} │───────────────────▶│ {PHASE2} │
└──────────┘                    └──────────┘
                                     │
                              {threshold}
                                     ▼
┌──────────┐     {threshold}    ┌──────────┐
│ {PHASE4} │◀───────────────────│ {PHASE3} │
└──────────┘                    └──────────┘
```

---

## QUICK REFERENCE

| User says | Action |
|-----------|--------|
| "{trigger phrase 1}" | {Action} |
| "{trigger phrase 2}" | {Action} |
| "{trigger phrase 3}" | {Action} |

---

## EXAMPLES

### Example 1: {Scenario Name}

```
User: "{example user input}"

Process:
1. {What happens first}
2. {What happens next}
3. {Output}
```

---

## CHECKLIST: Is Your Process Complete?

- [ ] All phases defined with clear purpose
- [ ] Each phase has at least 1 step
- [ ] Each step has requires/produces
- [ ] Each step has clear instructions
- [ ] Gates between all phases
- [ ] Gate thresholds sum to 1.0
- [ ] Artifacts summary complete
- [ ] State transitions diagram done
- [ ] Quick reference filled in
- [ ] Enforcement rules defined
- [ ] Tested with real project
