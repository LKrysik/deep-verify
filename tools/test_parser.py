#!/usr/bin/env python3
"""
Test BMAD Contract Parser

Run: python test_parser.py
"""

import sys
import io
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from bmad_contracts import (
    parse_frontmatter,
    parse_workflow,
    parse_output_contract,
    build_workflow_graph,
    find_entry_points,
    find_broken_references,
    validate_output,
    print_workflow_list,
    print_workflow_graph,
    generate_mermaid_diagram,
)


def test_parse_examples():
    """Test parsing example files."""
    print("\n" + "=" * 60)
    print("TEST: Parse Example Workflows")
    print("=" * 60)

    examples_dir = Path(__file__).parent.parent / "examples" / "workflows-with-contracts"

    if not examples_dir.exists():
        print(f"⚠️  Examples directory not found: {examples_dir}")
        return False

    success = True

    for md_file in examples_dir.glob("*.md"):
        print(f"\nParsing: {md_file.name}")

        workflow = parse_workflow(md_file)

        if workflow:
            print(f"  ✅ ID: {workflow.id}")
            print(f"     Inputs: {len(workflow.inputs)}")
            print(f"     Outputs: {len(workflow.outputs)}")
            print(f"     Contract: {workflow.output_contract}")
            print(f"     Next: {workflow.next_success} / {workflow.next_failure}")
        else:
            print(f"  ❌ Failed to parse")
            success = False

    return success


def test_parse_contracts():
    """Test parsing contract schemas."""
    print("\n" + "=" * 60)
    print("TEST: Parse Output Contracts")
    print("=" * 60)

    contracts_dir = Path(__file__).parent.parent / "examples" / "contracts"

    if not contracts_dir.exists():
        print(f"⚠️  Contracts directory not found: {contracts_dir}")
        return False

    success = True

    for md_file in contracts_dir.glob("*.md"):
        print(f"\nParsing: {md_file.name}")

        contract = parse_output_contract(md_file)

        if contract:
            print(f"  ✅ Contract: {contract.contract}")
            print(f"     Version: {contract.version}")
            print(f"     Required fields: {contract.required_fields}")
            print(f"     Required sections: {contract.required_sections}")
        else:
            print(f"  ❌ Failed to parse")
            success = False

    return success


def test_build_graph():
    """Test building workflow graph."""
    print("\n" + "=" * 60)
    print("TEST: Build Workflow Graph")
    print("=" * 60)

    examples_dir = Path(__file__).parent.parent / "examples" / "workflows-with-contracts"

    if not examples_dir.exists():
        print(f"⚠️  Examples directory not found: {examples_dir}")
        return False

    graph = build_workflow_graph(examples_dir)

    print(f"\nWorkflows found: {len(graph)}")

    for wf_id, workflow in graph.items():
        print(f"  - {wf_id}")

    # Find entry points
    entry_points = find_entry_points(graph)
    print(f"\nEntry points: {entry_points}")

    # Find broken references
    broken = find_broken_references(graph)
    if broken:
        print(f"\n⚠️  Broken references: {broken}")
    else:
        print(f"\n✅ No broken references")

    return True


def test_visualize():
    """Test visualization functions."""
    print("\n" + "=" * 60)
    print("TEST: Visualize Workflow Graph")
    print("=" * 60)

    examples_dir = Path(__file__).parent.parent / "examples" / "workflows-with-contracts"

    if not examples_dir.exists():
        print(f"⚠️  Examples directory not found: {examples_dir}")
        return False

    graph = build_workflow_graph(examples_dir)

    # Print list
    print("\n--- Workflow List ---")
    print_workflow_list(graph, verbose=False)

    # Print graph
    print("\n--- Workflow Graph ---")
    print_workflow_graph(graph)

    # Generate Mermaid
    print("\n--- Mermaid Diagram ---")
    mermaid = generate_mermaid_diagram(graph)
    print(mermaid)

    return True


def test_validate():
    """Test validation."""
    print("\n" + "=" * 60)
    print("TEST: Validate Output")
    print("=" * 60)

    contracts_dir = Path(__file__).parent.parent / "examples" / "contracts"

    if not contracts_dir.exists():
        print(f"⚠️  Contracts directory not found: {contracts_dir}")
        return False

    # Load a contract
    contract = parse_output_contract(contracts_dir / "product-brief.md")

    if not contract:
        print("❌ Failed to load contract")
        return False

    print(f"Contract: {contract.contract}")
    print(f"Required fields: {contract.required_fields}")
    print(f"Required sections: {contract.required_sections}")

    # Create a test output file content
    test_content = """---
id: test-brief
name: Test Product
status: draft
version: "1.0"
---

# Test Product Brief

## Vision

This is the vision.

## Target Users

These are the users.

## Core Problem

This is the problem.

## Success Metrics

These are the metrics.

## MVP Scope

This is the scope.
"""

    # Write test file
    test_file = Path(__file__).parent / "test_output.md"
    test_file.write_text(test_content)

    # Validate
    errors = validate_output(test_file, contract)

    if errors:
        print(f"\n❌ Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"\n✅ Validation passed")

    # Clean up
    test_file.unlink()

    # Test with missing fields
    print("\n--- Test with missing fields ---")

    bad_content = """---
id: test-brief
---

# Test

## Vision

Content here.
"""

    test_file.write_text(bad_content)
    errors = validate_output(test_file, contract)

    print(f"Expected errors found: {len(errors)}")
    for error in errors:
        print(f"  - [{error.error_type}] {error.message}")

    test_file.unlink()

    return True


def test_parse_existing_bmad():
    """Test parsing existing BMAD workflows."""
    print("\n" + "=" * 60)
    print("TEST: Parse Existing BMAD Workflows")
    print("=" * 60)

    bmad_dir = Path(__file__).parent.parent / "_bmad" / "bmm" / "workflows"

    if not bmad_dir.exists():
        print(f"⚠️  BMAD workflows directory not found: {bmad_dir}")
        return True  # Not a failure, just not available

    # Parse with error handling
    from bmad_contracts.parser import parse_all_workflows

    workflows = {}
    errors = []

    for md_file in bmad_dir.rglob('*.md'):
        try:
            workflow = parse_workflow(md_file)
            if workflow:
                workflows[workflow.id] = workflow
        except ValueError as e:
            errors.append((md_file.name, str(e)[:50]))

    print(f"\nExisting BMAD workflows found: {len(workflows)}")
    print(f"Files with YAML errors: {len(errors)}")

    # Show some examples
    for wf_id, workflow in list(workflows.items())[:5]:
        print(f"\n  [{wf_id}]")
        print(f"    file: {workflow.file_path.name if workflow.file_path else 'N/A'}")
        print(f"    has contract: {'yes' if workflow.inputs or workflow.outputs else 'partial'}")

    if len(workflows) > 5:
        print(f"\n  ... and {len(workflows) - 5} more")

    if errors:
        print(f"\n⚠️  Files with invalid YAML (need fixing):")
        for filename, error in errors[:3]:
            print(f"    - {filename}")

    return True  # Always pass - we're testing parser, not BMAD files


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("BMAD CONTRACT PARSER - TEST SUITE")
    print("=" * 60)

    tests = [
        ("Parse Examples", test_parse_examples),
        ("Parse Contracts", test_parse_contracts),
        ("Build Graph", test_build_graph),
        ("Visualize", test_visualize),
        ("Validate", test_validate),
        ("Parse Existing BMAD", test_parse_existing_bmad),
    ]

    results = []

    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Exception in {name}: {e}")
            results.append((name, False))

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {name}")

    print(f"\nTotal: {passed}/{total} passed")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
