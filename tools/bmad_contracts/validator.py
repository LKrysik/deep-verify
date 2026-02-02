"""
BMAD Contract Validator

Validate workflow outputs against contracts.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import re

from .parser import (
    parse_frontmatter,
    parse_output_contract,
    parse_all_contracts,
    OutputContract,
    WorkflowContract,
)


@dataclass
class ValidationError:
    """A single validation error."""

    file: Path
    error_type: str  # 'missing_field', 'missing_section', 'invalid_value', etc.
    message: str
    field: Optional[str] = None

    def __str__(self) -> str:
        return f"[{self.error_type}] {self.file}: {self.message}"


def validate_output(
    output_file: Path,
    contract: OutputContract,
) -> list[ValidationError]:
    """
    Validate output file against contract schema.

    Args:
        output_file: Path to the output markdown file
        contract: OutputContract to validate against

    Returns:
        List of ValidationError objects (empty if valid)

    Example:
        >>> contract = parse_output_contract(Path("contracts/story.md"))
        >>> errors = validate_output(Path("docs/stories/US-001.md"), contract)
        >>> if errors:
        ...     for e in errors:
        ...         print(e)
    """
    errors = []

    # Check file exists
    if not output_file.exists():
        errors.append(ValidationError(
            file=output_file,
            error_type="file_not_found",
            message=f"Output file does not exist",
        ))
        return errors

    # Parse output frontmatter
    try:
        data = parse_frontmatter(output_file)
    except ValueError as e:
        errors.append(ValidationError(
            file=output_file,
            error_type="invalid_yaml",
            message=str(e),
        ))
        return errors

    if data is None:
        errors.append(ValidationError(
            file=output_file,
            error_type="missing_frontmatter",
            message="File has no YAML frontmatter",
        ))
        return errors

    # Check required fields
    for field_name in contract.required_fields:
        if field_name not in data:
            errors.append(ValidationError(
                file=output_file,
                error_type="missing_field",
                message=f"Missing required field: {field_name}",
                field=field_name,
            ))
        elif data[field_name] is None or data[field_name] == "":
            errors.append(ValidationError(
                file=output_file,
                error_type="empty_field",
                message=f"Required field is empty: {field_name}",
                field=field_name,
            ))

    # Check required sections
    try:
        content = output_file.read_text(encoding='utf-8')
    except Exception as e:
        errors.append(ValidationError(
            file=output_file,
            error_type="read_error",
            message=f"Cannot read file content: {e}",
        ))
        return errors

    for section_name in contract.required_sections:
        # Look for ## Section Name (case-insensitive for flexibility)
        pattern = rf'^##\s+{re.escape(section_name)}\s*$'
        if not re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
            errors.append(ValidationError(
                file=output_file,
                error_type="missing_section",
                message=f"Missing required section: ## {section_name}",
                field=section_name,
            ))

    return errors


def validate_output_by_name(
    output_file: Path,
    contract_name: str,
    contracts_dir: Path,
) -> list[ValidationError]:
    """
    Validate output file against named contract.

    Args:
        output_file: Path to the output markdown file
        contract_name: Name of the contract to validate against
        contracts_dir: Path to directory containing contract files

    Returns:
        List of ValidationError objects
    """
    # Find contract file
    contracts = parse_all_contracts(contracts_dir)

    if contract_name not in contracts:
        return [ValidationError(
            file=output_file,
            error_type="contract_not_found",
            message=f"Contract '{contract_name}' not found in {contracts_dir}",
        )]

    return validate_output(output_file, contracts[contract_name])


def validate_workflow_references(
    graph: dict[str, WorkflowContract],
) -> list[ValidationError]:
    """
    Validate that all workflow references point to existing workflows.

    Args:
        graph: Workflow graph from build_workflow_graph

    Returns:
        List of ValidationError objects
    """
    errors = []

    for wf_id, workflow in graph.items():
        # Check next.success reference
        if workflow.next_success:
            if workflow.next_success != "retry" and workflow.next_success not in graph:
                errors.append(ValidationError(
                    file=workflow.file_path or Path(wf_id),
                    error_type="broken_reference",
                    message=f"next.success references non-existent workflow: {workflow.next_success}",
                    field="next.success",
                ))

        # Check next.failure reference
        if workflow.next_failure:
            if workflow.next_failure != "retry" and workflow.next_failure not in graph:
                errors.append(ValidationError(
                    file=workflow.file_path or Path(wf_id),
                    error_type="broken_reference",
                    message=f"next.failure references non-existent workflow: {workflow.next_failure}",
                    field="next.failure",
                ))

    return errors


def validate_workflow_contracts(
    graph: dict[str, WorkflowContract],
    contracts_dir: Path,
) -> list[ValidationError]:
    """
    Validate that all output_contract references point to existing contracts.

    Args:
        graph: Workflow graph
        contracts_dir: Path to contracts directory

    Returns:
        List of ValidationError objects
    """
    errors = []

    # Load all contracts
    contracts = parse_all_contracts(contracts_dir)

    for wf_id, workflow in graph.items():
        if workflow.output_contract:
            if workflow.output_contract not in contracts:
                errors.append(ValidationError(
                    file=workflow.file_path or Path(wf_id),
                    error_type="contract_not_found",
                    message=f"output_contract references non-existent contract: {workflow.output_contract}",
                    field="output_contract",
                ))

    return errors


def validate_all(
    workflows_dir: Path,
    contracts_dir: Path,
    outputs_dir: Optional[Path] = None,
) -> dict[str, list[ValidationError]]:
    """
    Run all validations on workflows, contracts, and optionally outputs.

    Args:
        workflows_dir: Path to workflows directory
        contracts_dir: Path to contracts directory
        outputs_dir: Optional path to outputs directory

    Returns:
        Dict with 'workflows', 'references', 'contracts', 'outputs' keys
    """
    from .graph import build_workflow_graph

    results = {
        'workflows': [],
        'references': [],
        'contracts': [],
        'outputs': [],
    }

    # Build graph
    graph = build_workflow_graph(workflows_dir)

    # Validate workflow references
    results['references'] = validate_workflow_references(graph)

    # Validate contract references
    results['contracts'] = validate_workflow_contracts(graph, contracts_dir)

    # Validate outputs if directory provided
    if outputs_dir and outputs_dir.exists():
        contracts = parse_all_contracts(contracts_dir)

        for output_file in outputs_dir.rglob('*.md'):
            # Try to determine which contract applies
            data = parse_frontmatter(output_file)
            if data:
                # Look for contract hint in frontmatter
                contract_name = data.get('contract') or data.get('output_contract')
                if contract_name and contract_name in contracts:
                    errors = validate_output(output_file, contracts[contract_name])
                    results['outputs'].extend(errors)

    return results
