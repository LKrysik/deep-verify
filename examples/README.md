# BMAD Contract Examples

Przykładowe workflows i contracts zgodne ze specyfikacją v0.1.

---

## Struktura

```
examples/
├── README.md                           ← Ten plik
├── workflows-with-contracts/           ← Workflows z embedded contracts
│   ├── create-product-brief.md
│   ├── create-prd.md
│   └── create-architecture.md
└── contracts/                          ← Output schemas
    ├── product-brief.md
    ├── prd.md
    └── architecture.md
```

---

## Workflow Graph

```
┌─────────────────────────┐
│  create-product-brief   │
│  ─────────────────────  │
│  inputs:  config.yaml   │
│  outputs: product-brief │
└───────────┬─────────────┘
            │ success
            ▼
┌─────────────────────────┐
│      create-prd         │
│  ─────────────────────  │
│  inputs:  product-brief │
│  outputs: prd.md        │
└───────────┬─────────────┘
            │ success
            ▼
┌─────────────────────────┐
│  create-architecture    │
│  ─────────────────────  │
│  inputs:  prd.md        │
│  outputs: architecture  │
└───────────┬─────────────┘
            │ success
            ▼
      [create-epics]
           ...
```

---

## Contract Format

### Workflow Contract (w pliku workflow)

```yaml
---
# === BMAD CONTRACT v0.1 ===
id: workflow-id                    # REQUIRED
name: Human Readable Name
inputs:
  - path/to/input1.md
  - path/to/input2.md
outputs:
  - path/to/output.md
output_contract: contract-name     # schema for output validation
next:
  success: next-workflow-id
  failure: retry | other-workflow
status: pending | done
---
```

### Output Contract (w pliku contracts/)

```yaml
---
contract: contract-name            # REQUIRED
version: "0.1"
required_fields:
  - field1
  - field2
required_sections:
  - Section Name 1
  - Section Name 2
---
```

---

## Jak używać

### LLM Standalone (bez Python)

1. LLM czyta workflow file
2. LLM widzi `inputs:` → wie jakie pliki załadować
3. LLM widzi `output_contract:` → wie jaki format outputu
4. LLM widzi `next:` → wie co dalej po zakończeniu

```
User: "Execute create-product-brief"

LLM reads: workflows-with-contracts/create-product-brief.md
LLM sees: output_contract: product-brief
LLM reads: contracts/product-brief.md
LLM knows: output must have frontmatter with id, name, status, version
LLM knows: output must have sections: Vision, Target Users, Core Problem...
LLM creates output following contract
LLM sees: next.success: create-prd
LLM tells user: "Product brief created. Next: create-prd"
```

### Python Orchestration

```python
from pathlib import Path
import yaml

def parse_contract(filepath: Path) -> dict:
    content = filepath.read_text()
    if not content.startswith('---'):
        return {}
    end = content.index('---', 3)
    return yaml.safe_load(content[3:end])

# Build workflow graph
workflows = {}
for f in Path('workflows-with-contracts').glob('*.md'):
    contract = parse_contract(f)
    if 'id' in contract:
        workflows[contract['id']] = contract

# Visualize
for wf_id, wf in workflows.items():
    print(f"[{wf_id}]")
    print(f"  inputs: {wf.get('inputs', [])}")
    print(f"  outputs: {wf.get('outputs', [])}")
    if wf.get('next'):
        print(f"  next.success: {wf['next'].get('success')}")
        print(f"  next.failure: {wf['next'].get('failure')}")
```

Output:
```
[create-product-brief]
  inputs: ['{project-root}/_bmad/bmm/config.yaml']
  outputs: ['{output_folder}/product-brief.md']
  next.success: create-prd
  next.failure: retry

[create-prd]
  inputs: ['{output_folder}/product-brief.md', ...]
  outputs: ['{output_folder}/prd.md']
  next.success: create-architecture
  next.failure: retry

[create-architecture]
  inputs: ['{output_folder}/prd.md', ...]
  outputs: ['{output_folder}/architecture.md']
  next.success: create-epics-and-stories
  next.failure: retry
```

---

## Validation

### Validate workflow output

```python
def validate_output(output_path: Path, contract_path: Path) -> list[str]:
    errors = []

    # Load contract
    contract = parse_contract(contract_path)

    # Load output
    output = parse_contract(output_path)
    output_content = output_path.read_text()

    # Check required fields
    for field in contract.get('required_fields', []):
        if field not in output:
            errors.append(f"Missing field: {field}")

    # Check required sections
    for section in contract.get('required_sections', []):
        if f"## {section}" not in output_content:
            errors.append(f"Missing section: ## {section}")

    return errors

# Example
errors = validate_output(
    Path('docs/product-brief.md'),
    Path('examples/contracts/product-brief.md')
)
if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
else:
    print("Validation passed!")
```

---

## Migracja istniejących workflows

Aby dodać contract do istniejącego workflow:

1. **Dodaj contract fields na początku frontmatter:**

```yaml
---
# === BMAD CONTRACT v0.1 ===
id: my-workflow
name: My Workflow
inputs:
  - input/path.md
outputs:
  - output/path.md
output_contract: my-contract
next:
  success: next-workflow
  failure: retry
status: pending

# === EXISTING FIELDS ===
description: Original description...
web_bundle: true
---
```

2. **Dodaj OUTPUT REQUIREMENTS section na końcu:**

```markdown
---

## OUTPUT REQUIREMENTS

Your output MUST follow the `my-contract` contract:

1. Save to: `{outputs[0]}`
2. Include YAML frontmatter with required fields
3. Include required sections

Failure to follow this format will cause validation errors.
```

3. **Stwórz contract file w contracts/:**

```yaml
---
contract: my-contract
version: "0.1"
required_fields:
  - id
  - status
required_sections:
  - Overview
---
```

---

## Checklist

- [x] 3 example workflows with contracts
- [x] 3 output contracts (schemas)
- [x] Workflow graph visualization
- [x] Python parsing example
- [x] Validation example
- [x] Migration guide

---

## Related Documents

- [Contract Spec v0.1](../contract-spec-v0.1.md)
- [Deep Explore Report](../deep-explore-report-embedded-contracts.md)
