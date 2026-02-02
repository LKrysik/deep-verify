"""
BMAD Contract Parser

Parse YAML frontmatter from markdown files.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import re

try:
    import yaml
except ImportError:
    raise ImportError("PyYAML is required. Install with: pip install pyyaml")


@dataclass
class WorkflowContract:
    """Workflow contract parsed from markdown frontmatter."""

    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    output_contract: Optional[str] = None
    next_success: Optional[str] = None
    next_failure: Optional[str] = None
    status: Optional[str] = None
    file_path: Optional[Path] = None

    # Additional fields from original BMAD
    web_bundle: Optional[bool] = None

    @property
    def has_next(self) -> bool:
        """Check if workflow has any next steps defined."""
        return self.next_success is not None or self.next_failure is not None


@dataclass
class OutputContract:
    """Output contract (schema) parsed from markdown frontmatter."""

    contract: str
    version: Optional[str] = None
    required_fields: list[str] = field(default_factory=list)
    required_sections: list[str] = field(default_factory=list)
    file_path: Optional[Path] = None


def parse_frontmatter(filepath: Path) -> dict | None:
    """
    Extract YAML frontmatter from markdown file.

    Args:
        filepath: Path to markdown file

    Returns:
        Parsed YAML as dict, or None if no frontmatter found

    Example:
        >>> data = parse_frontmatter(Path("workflow.md"))
        >>> print(data.get('id'))
        'my-workflow'
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except (FileNotFoundError, PermissionError) as e:
        raise FileNotFoundError(f"Cannot read file: {filepath}") from e

    # Check for frontmatter
    if not content.startswith('---'):
        return None

    # Find closing ---
    # Skip first 3 chars (opening ---) and find next ---
    try:
        # Use regex to handle --- that might have trailing whitespace
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None

        frontmatter_text = match.group(1)
        return yaml.safe_load(frontmatter_text)

    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in frontmatter of {filepath}: {e}")


def parse_workflow(filepath: Path) -> WorkflowContract | None:
    """
    Parse workflow contract from markdown file.

    Args:
        filepath: Path to workflow markdown file

    Returns:
        WorkflowContract if valid contract found, None otherwise

    Example:
        >>> workflow = parse_workflow(Path("create-story.md"))
        >>> print(workflow.id)
        'create-story'
        >>> print(workflow.next_success)
        'validate-story'
    """
    data = parse_frontmatter(filepath)

    if not data:
        return None

    # Check for required field
    if 'id' not in data and 'name' not in data:
        return None

    # Extract 'next' structure
    next_data = data.get('next', {})
    if isinstance(next_data, str):
        # Simple case: next: workflow-id
        next_success = next_data
        next_failure = None
    elif isinstance(next_data, dict):
        next_success = next_data.get('success')
        next_failure = next_data.get('failure')
    else:
        next_success = None
        next_failure = None

    # Use 'name' as fallback for 'id' (backward compat with existing BMAD)
    workflow_id = data.get('id') or data.get('name')

    return WorkflowContract(
        id=workflow_id,
        name=data.get('name'),
        description=data.get('description'),
        inputs=data.get('inputs', []) or [],
        outputs=data.get('outputs', []) or [],
        output_contract=data.get('output_contract'),
        next_success=next_success,
        next_failure=next_failure,
        status=data.get('status'),
        file_path=filepath,
        web_bundle=data.get('web_bundle'),
    )


def parse_output_contract(filepath: Path) -> OutputContract | None:
    """
    Parse output contract schema from markdown file.

    Args:
        filepath: Path to contract schema file

    Returns:
        OutputContract if valid contract found, None otherwise

    Example:
        >>> contract = parse_output_contract(Path("contracts/story.md"))
        >>> print(contract.required_fields)
        ['id', 'epic', 'status']
    """
    data = parse_frontmatter(filepath)

    if not data:
        return None

    # Check for required field
    if 'contract' not in data:
        return None

    return OutputContract(
        contract=data['contract'],
        version=data.get('version'),
        required_fields=data.get('required_fields', []) or [],
        required_sections=data.get('required_sections', []) or [],
        file_path=filepath,
    )


def parse_all_workflows(directory: Path) -> dict[str, WorkflowContract]:
    """
    Parse all workflow contracts from a directory (recursive).

    Args:
        directory: Path to workflows directory

    Returns:
        Dict mapping workflow ID to WorkflowContract
    """
    workflows = {}

    for md_file in directory.rglob('*.md'):
        workflow = parse_workflow(md_file)
        if workflow:
            workflows[workflow.id] = workflow

    return workflows


def parse_all_contracts(directory: Path) -> dict[str, OutputContract]:
    """
    Parse all output contracts from a directory.

    Args:
        directory: Path to contracts directory

    Returns:
        Dict mapping contract name to OutputContract
    """
    contracts = {}

    for md_file in directory.rglob('*.md'):
        contract = parse_output_contract(md_file)
        if contract:
            contracts[contract.contract] = contract

    return contracts
