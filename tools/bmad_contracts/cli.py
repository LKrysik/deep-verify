#!/usr/bin/env python3
"""
BMAD Contract CLI

Command-line interface for parsing, validating, and visualizing BMAD contracts.

Usage:
    bmad-contracts list [--dir PATH] [--verbose]
    bmad-contracts graph [--dir PATH] [--start WORKFLOW]
    bmad-contracts validate OUTPUT_FILE --contract CONTRACT
    bmad-contracts check [--workflows PATH] [--contracts PATH]
    bmad-contracts mermaid [--dir PATH]
"""

import argparse
import sys
from pathlib import Path

from .parser import parse_workflow, parse_output_contract, parse_all_workflows, parse_all_contracts
from .graph import build_workflow_graph, find_entry_points, find_broken_references
from .validator import validate_output, validate_output_by_name, validate_all, ValidationError
from .visualizer import (
    print_workflow_list,
    print_workflow_graph,
    print_status_summary,
    generate_mermaid_diagram,
)


def cmd_list(args: argparse.Namespace) -> int:
    """List all workflows."""
    workflows_dir = Path(args.dir)

    if not workflows_dir.exists():
        print(f"Error: Directory not found: {workflows_dir}", file=sys.stderr)
        return 1

    graph = build_workflow_graph(workflows_dir)

    if not graph:
        print(f"No workflows found in {workflows_dir}")
        return 0

    print_workflow_list(graph, verbose=args.verbose)

    if args.verbose:
        print_status_summary(graph)

    return 0


def cmd_graph(args: argparse.Namespace) -> int:
    """Show workflow graph."""
    workflows_dir = Path(args.dir)

    if not workflows_dir.exists():
        print(f"Error: Directory not found: {workflows_dir}", file=sys.stderr)
        return 1

    graph = build_workflow_graph(workflows_dir)

    if not graph:
        print(f"No workflows found in {workflows_dir}")
        return 0

    print_workflow_graph(graph, start_from=args.start)

    # Show entry points
    entry_points = find_entry_points(graph)
    if entry_points:
        print(f"\nEntry points: {', '.join(entry_points)}")

    # Show broken references
    broken = find_broken_references(graph)
    if broken:
        print(f"\n⚠️  Broken references:")
        for source, target in broken:
            print(f"  {source} → {target} (not found)")

    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """Validate output against contract."""
    output_file = Path(args.output_file)

    if not output_file.exists():
        print(f"Error: Output file not found: {output_file}", file=sys.stderr)
        return 1

    # Load contract
    if args.contract_file:
        contract_path = Path(args.contract_file)
        if not contract_path.exists():
            print(f"Error: Contract file not found: {contract_path}", file=sys.stderr)
            return 1

        contract = parse_output_contract(contract_path)
        if not contract:
            print(f"Error: Invalid contract file: {contract_path}", file=sys.stderr)
            return 1

        errors = validate_output(output_file, contract)
    else:
        # Use contract name and contracts directory
        contracts_dir = Path(args.contracts_dir)
        if not contracts_dir.exists():
            print(f"Error: Contracts directory not found: {contracts_dir}", file=sys.stderr)
            return 1

        errors = validate_output_by_name(output_file, args.contract, contracts_dir)

    if errors:
        print(f"\n❌ Validation failed for {output_file}:")
        for error in errors:
            print(f"  - [{error.error_type}] {error.message}")
        return 1
    else:
        print(f"\n✅ Validation passed for {output_file}")
        return 0


def cmd_check(args: argparse.Namespace) -> int:
    """Run all validation checks."""
    workflows_dir = Path(args.workflows)
    contracts_dir = Path(args.contracts)

    if not workflows_dir.exists():
        print(f"Error: Workflows directory not found: {workflows_dir}", file=sys.stderr)
        return 1

    if not contracts_dir.exists():
        print(f"Error: Contracts directory not found: {contracts_dir}", file=sys.stderr)
        return 1

    outputs_dir = Path(args.outputs) if args.outputs else None

    results = validate_all(workflows_dir, contracts_dir, outputs_dir)

    total_errors = sum(len(errors) for errors in results.values())

    print("\nValidation Results:")
    print("=" * 50)

    for category, errors in results.items():
        status = "✅" if not errors else "❌"
        print(f"\n{status} {category.title()}: {len(errors)} errors")
        for error in errors[:5]:  # Show max 5 errors per category
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more")

    print(f"\n{'=' * 50}")
    print(f"Total errors: {total_errors}")

    return 0 if total_errors == 0 else 1


def cmd_mermaid(args: argparse.Namespace) -> int:
    """Generate Mermaid diagram."""
    workflows_dir = Path(args.dir)

    if not workflows_dir.exists():
        print(f"Error: Directory not found: {workflows_dir}", file=sys.stderr)
        return 1

    graph = build_workflow_graph(workflows_dir)

    if not graph:
        print(f"No workflows found in {workflows_dir}")
        return 0

    mermaid = generate_mermaid_diagram(graph, direction=args.direction)
    print(mermaid)

    return 0


def cmd_info(args: argparse.Namespace) -> int:
    """Show info about a specific workflow."""
    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        return 1

    workflow = parse_workflow(file_path)

    if not workflow:
        print(f"Error: No valid workflow contract in {file_path}", file=sys.stderr)
        return 1

    print(f"\nWorkflow: {workflow.id}")
    print("=" * 50)

    if workflow.name:
        print(f"Name:        {workflow.name}")
    if workflow.description:
        print(f"Description: {workflow.description[:80]}...")
    if workflow.status:
        print(f"Status:      {workflow.status}")

    print(f"\nInputs:      {workflow.inputs or '(none)'}")
    print(f"Outputs:     {workflow.outputs or '(none)'}")

    if workflow.output_contract:
        print(f"Contract:    {workflow.output_contract}")

    print(f"\nNext:")
    print(f"  success:   {workflow.next_success or '(none)'}")
    print(f"  failure:   {workflow.next_failure or '(none)'}")

    print(f"\nFile:        {workflow.file_path}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="BMAD Contract Tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bmad-contracts list --dir workflows/
  bmad-contracts graph --dir workflows/ --start create-product-brief
  bmad-contracts validate docs/prd.md --contract prd --contracts-dir contracts/
  bmad-contracts check --workflows workflows/ --contracts contracts/
  bmad-contracts mermaid --dir workflows/
        """,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # list command
    list_parser = subparsers.add_parser("list", help="List all workflows")
    list_parser.add_argument("--dir", "-d", default=".", help="Workflows directory")
    list_parser.add_argument("--verbose", "-v", action="store_true", help="Show details")
    list_parser.set_defaults(func=cmd_list)

    # graph command
    graph_parser = subparsers.add_parser("graph", help="Show workflow graph")
    graph_parser.add_argument("--dir", "-d", default=".", help="Workflows directory")
    graph_parser.add_argument("--start", "-s", help="Starting workflow ID")
    graph_parser.set_defaults(func=cmd_graph)

    # validate command
    validate_parser = subparsers.add_parser("validate", help="Validate output against contract")
    validate_parser.add_argument("output_file", help="Output file to validate")
    validate_parser.add_argument("--contract", "-c", help="Contract name")
    validate_parser.add_argument("--contract-file", "-f", help="Contract file path")
    validate_parser.add_argument("--contracts-dir", default="contracts/", help="Contracts directory")
    validate_parser.set_defaults(func=cmd_validate)

    # check command
    check_parser = subparsers.add_parser("check", help="Run all validation checks")
    check_parser.add_argument("--workflows", "-w", default="workflows/", help="Workflows directory")
    check_parser.add_argument("--contracts", "-c", default="contracts/", help="Contracts directory")
    check_parser.add_argument("--outputs", "-o", help="Outputs directory (optional)")
    check_parser.set_defaults(func=cmd_check)

    # mermaid command
    mermaid_parser = subparsers.add_parser("mermaid", help="Generate Mermaid diagram")
    mermaid_parser.add_argument("--dir", "-d", default=".", help="Workflows directory")
    mermaid_parser.add_argument("--direction", default="TD", choices=["TD", "LR"], help="Diagram direction")
    mermaid_parser.set_defaults(func=cmd_mermaid)

    # info command
    info_parser = subparsers.add_parser("info", help="Show workflow info")
    info_parser.add_argument("file", help="Workflow file path")
    info_parser.set_defaults(func=cmd_info)

    args = parser.parse_args()

    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nInterrupted")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
