# BMAD Contract Spec v0.1

**Version:** 0.1
**Date:** 2026-02-02
**Status:** Draft

---

## Design Principles

```
1. MAX 10 LINES — jeśli więcej, wrong design
2. YAML FRONTMATTER — standard markdown, LLM i Python czytają natywnie
3. LLM = INSTRUCTIONS — kontrakt mówi LLM co robić
4. PYTHON = DATA — kontrakt daje Python strukturę do parsowania
5. OPTIONAL FIELDS — tylko `id` wymagane, reszta opcjonalna
```

---

## Specification

### Workflow Contract (for workflow files)

```yaml
---
id: string                    # REQUIRED: unique identifier (kebab-case)
name: string                  # display name for humans
inputs: [path, ...]           # files/data needed to execute
outputs: [path, ...]          # files/data produced
output_contract: string       # schema name for output validation
next:                         # what happens after execution
  success: workflow-id        # on success, go here
  failure: workflow-id | retry # on failure, go here or retry
status: pending | done        # tracking (Python updates this)
---
```

### Output Contract (for artifact schemas)

```yaml
---
contract: string              # REQUIRED: schema identifier
version: string               # schema version
required_fields: [field, ...] # fields that MUST be in output frontmatter
required_sections: [name, ...]# markdown sections that MUST exist
---
```

---

## Field Reference

### Workflow Contract Fields

| Field | Type | Required | Used By | Description |
|-------|------|----------|---------|-------------|
| `id` | string | **YES** | Both | Unique identifier, kebab-case |
| `name` | string | no | LLM | Human-readable name |
| `inputs` | list | no | Both | Paths to required input files |
| `outputs` | list | no | Both | Paths where outputs are saved |
| `output_contract` | string | no | Both | Schema that output must follow |
| `next.success` | string | no | Both | Workflow to run on success |
| `next.failure` | string | no | Both | Workflow to run on failure, or "retry" |
| `status` | enum | no | Python | Execution tracking: `pending`, `done` |

### Output Contract Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `contract` | string | **YES** | Schema identifier |
| `version` | string | no | Schema version |
| `required_fields` | list | no | Fields that MUST be in output frontmatter |
| `required_sections` | list | no | Markdown sections that MUST exist |

---

## Examples

### Example 1: Simple Workflow

```yaml
---
id: create-story
name: Create User Story
inputs:
  - docs/epics/{epic_id}.md
  - docs/prd.md
outputs:
  - docs/stories/{epic_id}/{story_id}.md
output_contract: story
next:
  success: validate-story
  failure: retry
---

## Instructions

Create a user story from the epic. Follow INVEST criteria.

Your output MUST include YAML frontmatter following the `story` contract.
```

**Line count: 9 lines** ✓

---

### Example 2: Validation Workflow

```yaml
---
id: validate-story
name: Validate Story
inputs:
  - docs/stories/{epic_id}/{story_id}.md
outputs:
  - docs/stories/{epic_id}/{story_id}.md
next:
  success: dev-story
  failure: create-story
---

## Instructions

Validate the story against acceptance criteria and INVEST principles.
If valid, update status to `ready`. If invalid, explain issues.
```

**Line count: 8 lines** ✓

---

### Example 3: Development Workflow

```yaml
---
id: dev-story
name: Implement Story
inputs:
  - docs/stories/{epic_id}/{story_id}.md
  - docs/architecture.md
outputs:
  - src/**/*
next:
  success: code-review
  failure: retry
---

## Instructions

Implement the user story according to the acceptance criteria.
Follow architecture guidelines and project conventions.
```

**Line count: 8 lines** ✓

---

## Output Contracts

### Story Contract

**File:** `contracts/story.md`

```yaml
---
contract: story
version: "0.1"
required_fields:
  - id
  - epic
  - status
required_sections:
  - Description
  - Acceptance Criteria
---

## Story Contract

Stories created by BMAD workflows MUST follow this format.

### Required Frontmatter

| Field | Type | Values | Required |
|-------|------|--------|----------|
| id | string | e.g., "US-001" | YES |
| epic | string | parent epic ID | YES |
| status | enum | draft, ready, in-progress, done | YES |
| priority | enum | low, medium, high, critical | no |
| estimate | number | story points | no |
| depends_on | list | IDs of blocking stories | no |

### Required Sections

- `## Description` — User story format (As a... I want... So that...)
- `## Acceptance Criteria` — Testable criteria as checklist

### Example Valid Output

```markdown
---
id: US-001
epic: EPIC-03
status: draft
priority: high
estimate: 5
---

## Description

As a user, I want to reset my password so that I can regain access to my account.

## Acceptance Criteria

- [ ] User can request password reset via email
- [ ] Reset link expires after 24 hours
- [ ] User must create password meeting security requirements
```
```

---

### Epic Contract

**File:** `contracts/epic.md`

```yaml
---
contract: epic
version: "0.1"
required_fields:
  - id
  - name
  - status
required_sections:
  - Overview
  - Stories
---

## Epic Contract

### Required Frontmatter

| Field | Type | Values | Required |
|-------|------|--------|----------|
| id | string | e.g., "EPIC-01" | YES |
| name | string | epic name | YES |
| status | enum | draft, ready, in-progress, done | YES |
| priority | enum | low, medium, high, critical | no |

### Required Sections

- `## Overview` — What this epic accomplishes
- `## Stories` — List of stories in this epic

### Example Valid Output

```markdown
---
id: EPIC-03
name: User Authentication
status: draft
priority: high
---

## Overview

Implement complete user authentication system with login, logout, and password reset.

## Stories

- [ ] US-001: Password reset
- [ ] US-002: Login flow
- [ ] US-003: Logout flow
```
```

---

## Workflow Graph

Python can build this visualization from contracts:

```
                    ┌─────────────┐
                    │ create-prd  │
                    └──────┬──────┘
                           │ success
                           ▼
                    ┌─────────────┐
          ┌─────── │create-epics │
          │        └──────┬──────┘
          │               │ success
          │ failure       ▼
          │        ┌─────────────┐
          │   ┌───►│create-story │◄──┐
          │   │    └──────┬──────┘   │
          │   │           │ success  │ failure
          │   │           ▼          │
          │   │    ┌─────────────┐   │
          │   │    │validate-    │───┘
          │   │    │story        │
          │   │    └──────┬──────┘
          │   │           │ success
          │   │           ▼
          │   │    ┌─────────────┐
          │   │    │  dev-story  │
          │   │    └──────┬──────┘
          │   │           │ success
          │   │           ▼
          │   │    ┌─────────────┐
          └───┴────│ code-review │
                   └─────────────┘
```

---

## Python Implementation

### Contract Parser

```python
"""BMAD Contract Parser v0.1"""

import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class WorkflowContract:
    id: str
    name: Optional[str] = None
    inputs: list[str] = None
    outputs: list[str] = None
    output_contract: Optional[str] = None
    next_success: Optional[str] = None
    next_failure: Optional[str] = None
    status: Optional[str] = None
    file_path: Optional[Path] = None

@dataclass
class OutputContract:
    contract: str
    version: Optional[str] = None
    required_fields: list[str] = None
    required_sections: list[str] = None


def parse_frontmatter(filepath: Path) -> dict | None:
    """Extract YAML frontmatter from markdown file."""
    content = filepath.read_text(encoding='utf-8')

    if not content.startswith('---'):
        return None

    try:
        end = content.index('---', 3)
        frontmatter = content[3:end].strip()
        return yaml.safe_load(frontmatter)
    except (ValueError, yaml.YAMLError):
        return None


def parse_workflow(filepath: Path) -> WorkflowContract | None:
    """Parse workflow contract from markdown file."""
    data = parse_frontmatter(filepath)

    if not data or 'id' not in data:
        return None

    next_data = data.get('next', {})

    return WorkflowContract(
        id=data['id'],
        name=data.get('name'),
        inputs=data.get('inputs', []),
        outputs=data.get('outputs', []),
        output_contract=data.get('output_contract'),
        next_success=next_data.get('success'),
        next_failure=next_data.get('failure'),
        status=data.get('status'),
        file_path=filepath,
    )


def parse_output_contract(filepath: Path) -> OutputContract | None:
    """Parse output contract schema from markdown file."""
    data = parse_frontmatter(filepath)

    if not data or 'contract' not in data:
        return None

    return OutputContract(
        contract=data['contract'],
        version=data.get('version'),
        required_fields=data.get('required_fields', []),
        required_sections=data.get('required_sections', []),
    )
```

### Workflow Graph Builder

```python
def build_workflow_graph(workflows_dir: Path) -> dict[str, WorkflowContract]:
    """Build graph of all workflows from directory."""
    graph = {}

    for md_file in workflows_dir.glob('**/*.md'):
        workflow = parse_workflow(md_file)
        if workflow:
            graph[workflow.id] = workflow

    return graph


def get_workflow_sequence(graph: dict, start_id: str) -> list[str]:
    """Get linear sequence of workflows from start."""
    sequence = []
    current = start_id
    visited = set()

    while current and current not in visited:
        visited.add(current)
        sequence.append(current)

        workflow = graph.get(current)
        if workflow:
            current = workflow.next_success
        else:
            break

    return sequence


def print_workflow_graph(graph: dict):
    """Print ASCII visualization of workflow graph."""
    print("\nWorkflow Graph:")
    print("=" * 40)

    for wf_id, workflow in graph.items():
        print(f"\n[{wf_id}]")
        if workflow.next_success:
            print(f"  ├── success → {workflow.next_success}")
        if workflow.next_failure:
            print(f"  └── failure → {workflow.next_failure}")
```

### Output Validator

```python
def validate_output(
    output_file: Path,
    contract: OutputContract
) -> list[str]:
    """Validate output file against contract schema."""
    errors = []

    # Parse output frontmatter
    data = parse_frontmatter(output_file)

    if not data:
        return ["Missing YAML frontmatter"]

    # Check required fields
    for field in contract.required_fields or []:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Check required sections
    content = output_file.read_text(encoding='utf-8')
    for section in contract.required_sections or []:
        if f"## {section}" not in content:
            errors.append(f"Missing required section: ## {section}")

    return errors


def validate_all_outputs(
    outputs_dir: Path,
    contracts_dir: Path
) -> dict[str, list[str]]:
    """Validate all outputs against their contracts."""
    results = {}

    # Load all contracts
    contracts = {}
    for contract_file in contracts_dir.glob('*.md'):
        contract = parse_output_contract(contract_file)
        if contract:
            contracts[contract.contract] = contract

    # Validate outputs (would need mapping from output to contract)
    # This is simplified - real implementation would check output_contract field

    return results
```

### CLI Tool

```python
"""BMAD Contract CLI"""

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='BMAD Contract Tools')
    subparsers = parser.add_subparsers(dest='command')

    # List workflows
    list_parser = subparsers.add_parser('list', help='List all workflows')
    list_parser.add_argument('--dir', default='_bmad/bmm/workflows')

    # Show graph
    graph_parser = subparsers.add_parser('graph', help='Show workflow graph')
    graph_parser.add_argument('--dir', default='_bmad/bmm/workflows')

    # Validate
    validate_parser = subparsers.add_parser('validate', help='Validate outputs')
    validate_parser.add_argument('file', help='File to validate')
    validate_parser.add_argument('--contract', help='Contract to validate against')

    args = parser.parse_args()

    if args.command == 'list':
        graph = build_workflow_graph(Path(args.dir))
        for wf_id in sorted(graph.keys()):
            print(f"  {wf_id}")

    elif args.command == 'graph':
        graph = build_workflow_graph(Path(args.dir))
        print_workflow_graph(graph)

    elif args.command == 'validate':
        # Implementation here
        pass

if __name__ == '__main__':
    main()
```

---

## LLM Instruction Template

Add to end of each workflow that produces output:

```markdown
---

## Output Requirements

Your output MUST:
1. Begin with YAML frontmatter between `---` markers
2. Include all required fields: {list required_fields from contract}
3. Include all required sections: {list required_sections from contract}

Example structure:
```yaml
---
id: [unique-id]
{other required fields}
---

## {Required Section 1}
[content]

## {Required Section 2}
[content]
```

Failure to follow this format will cause validation errors.
```

---

## File Structure

```
project/
├── _bmad/
│   └── bmm/
│       ├── workflows/              # Workflow files with contracts
│       │   ├── 1-analysis/
│       │   │   ├── create-prd.md
│       │   │   └── research.md
│       │   ├── 2-planning/
│       │   │   ├── create-epics.md
│       │   │   └── create-story.md
│       │   ├── 3-development/
│       │   │   ├── dev-story.md
│       │   │   └── code-review.md
│       │   └── ...
│       │
│       └── contracts/              # Output schemas
│           ├── story.md
│           ├── epic.md
│           ├── prd.md
│           └── sprint.md
│
├── docs/                           # Generated outputs
│   ├── prd.md
│   ├── epics/
│   │   └── EPIC-01.md
│   └── stories/
│       └── EPIC-01/
│           └── US-001.md
│
└── tools/
    └── bmad-contracts/             # Python tools
        ├── parser.py
        ├── validator.py
        └── cli.py
```

---

## Validation Checklist

Before shipping v0.1:

- [ ] All workflow files have `id` field
- [ ] All `id` values are unique
- [ ] All `id` values are kebab-case
- [ ] All `next` references point to existing workflow IDs
- [ ] All `output_contract` references have corresponding schema in contracts/
- [ ] LLM compliance test: 10 runs, >80% valid outputs
- [ ] Python parser correctly parses all workflow files
- [ ] Python validator catches missing fields/sections
- [ ] CLI `list` command works
- [ ] CLI `graph` command renders correctly

---

## v0.1 Scope

### IN SCOPE ✓

- [x] Workflow identification (`id`, `name`)
- [x] Input/output paths with placeholders
- [x] Linear flow (`next.success`, `next.failure`)
- [x] Output contracts (required fields, sections)
- [x] Basic status tracking (`pending`, `done`)
- [x] Python parser
- [x] Output validation
- [x] CLI tools (list, graph, validate)

### OUT OF SCOPE (v0.2+) ✗

- [ ] Conditional logic (if/else in contracts)
- [ ] Loop/retry count configuration
- [ ] Parallel execution
- [ ] Variable interpolation beyond simple placeholders
- [ ] Contract versioning and migration
- [ ] Dependencies between workflows (beyond next)
- [ ] Execution history/logging
- [ ] Web UI visualization

---

## Migration Guide

### Adding Contract to Existing Workflow

1. Open workflow file
2. Add YAML frontmatter at the very top:

```yaml
---
id: my-workflow-name
---
```

3. Optionally add more fields as needed
4. Test that LLM still executes workflow correctly

### Creating New Workflow with Contract

1. Start with frontmatter template:

```yaml
---
id: new-workflow
name: Human Readable Name
inputs:
  - path/to/input.md
outputs:
  - path/to/output.md
output_contract: contract-name
next:
  success: next-workflow
  failure: retry
---
```

2. Add workflow instructions below
3. Add output requirements section at end

---

## Changelog

### v0.1 (2026-02-02)

- Initial specification
- Workflow contracts: id, name, inputs, outputs, output_contract, next, status
- Output contracts: contract, version, required_fields, required_sections
- Python parser and validator
- CLI tools

---

## References

- [Deep Explore Report](./deep-explore-report-embedded-contracts.md) — Decision exploration that led to this spec
- YAML Frontmatter: Standard markdown convention (Jekyll, Hugo, Obsidian)
- BMAD Method: Base methodology this extends
