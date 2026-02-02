"""
BMAD Workflow Visualizer

Visualize workflow graphs in various formats.
"""

from pathlib import Path
from typing import Optional

from .parser import WorkflowContract
from .graph import find_entry_points, get_workflow_sequence


def print_workflow_list(
    graph: dict[str, WorkflowContract],
    verbose: bool = False,
) -> None:
    """
    Print list of all workflows.

    Args:
        graph: Workflow graph
        verbose: If True, print additional details
    """
    print(f"\nWorkflows ({len(graph)} total):")
    print("=" * 50)

    for wf_id in sorted(graph.keys()):
        workflow = graph[wf_id]

        if verbose:
            print(f"\n[{wf_id}]")
            if workflow.name and workflow.name != wf_id:
                print(f"  name: {workflow.name}")
            if workflow.description:
                desc = workflow.description[:60] + "..." if len(workflow.description) > 60 else workflow.description
                print(f"  desc: {desc}")
            if workflow.inputs:
                print(f"  inputs: {workflow.inputs}")
            if workflow.outputs:
                print(f"  outputs: {workflow.outputs}")
            if workflow.output_contract:
                print(f"  contract: {workflow.output_contract}")
            if workflow.next_success:
                print(f"  next.success: {workflow.next_success}")
            if workflow.next_failure:
                print(f"  next.failure: {workflow.next_failure}")
            if workflow.file_path:
                print(f"  file: {workflow.file_path}")
        else:
            status = workflow.status or ""
            status_icon = "✓" if status == "done" else "○"
            next_info = f" → {workflow.next_success}" if workflow.next_success else ""
            print(f"  {status_icon} {wf_id}{next_info}")


def print_workflow_graph(
    graph: dict[str, WorkflowContract],
    start_from: Optional[str] = None,
) -> None:
    """
    Print ASCII visualization of workflow graph.

    Args:
        graph: Workflow graph
        start_from: Optional workflow ID to start from
    """
    print("\nWorkflow Graph:")
    print("=" * 50)

    if start_from:
        # Print sequence from starting point
        sequence = get_workflow_sequence(graph, start_from)
        _print_sequence(graph, sequence)
    else:
        # Find entry points and print from each
        entry_points = find_entry_points(graph)

        if not entry_points:
            print("No entry points found (all workflows are referenced by others)")
            return

        for entry in entry_points:
            print(f"\nStarting from: {entry}")
            print("-" * 30)
            sequence = get_workflow_sequence(graph, entry)
            _print_sequence(graph, sequence)


def _print_sequence(
    graph: dict[str, WorkflowContract],
    sequence: list[str],
    indent: int = 0,
) -> None:
    """Print a workflow sequence with ASCII art."""
    prefix = "  " * indent

    for i, wf_id in enumerate(sequence):
        is_last = i == len(sequence) - 1

        if wf_id.startswith("("):
            # Special marker like "(retry)" or "(not found)"
            print(f"{prefix}    └── {wf_id}")
            continue

        workflow = graph.get(wf_id)

        # Box drawing
        print(f"{prefix}┌─{'─' * (len(wf_id) + 2)}─┐")
        print(f"{prefix}│ {wf_id} │")
        print(f"{prefix}└─{'─' * (len(wf_id) + 2)}─┘")

        if workflow:
            # Show inputs/outputs
            if workflow.inputs:
                inputs_str = ", ".join(str(i).split("/")[-1] for i in workflow.inputs[:2])
                if len(workflow.inputs) > 2:
                    inputs_str += f" (+{len(workflow.inputs) - 2})"
                print(f"{prefix}  in:  {inputs_str}")

            if workflow.outputs:
                outputs_str = ", ".join(str(o).split("/")[-1] for o in workflow.outputs[:2])
                if len(workflow.outputs) > 2:
                    outputs_str += f" (+{len(workflow.outputs) - 2})"
                print(f"{prefix}  out: {outputs_str}")

            # Show failure path if different
            if workflow.next_failure and workflow.next_failure != "retry":
                print(f"{prefix}  (failure → {workflow.next_failure})")

        # Arrow to next
        if not is_last:
            print(f"{prefix}    │")
            print(f"{prefix}    ▼")


def generate_mermaid_diagram(
    graph: dict[str, WorkflowContract],
    direction: str = "TD",
) -> str:
    """
    Generate Mermaid diagram code for workflow graph.

    Args:
        graph: Workflow graph
        direction: Diagram direction (TD=top-down, LR=left-right)

    Returns:
        Mermaid diagram code as string

    Example:
        >>> mermaid = generate_mermaid_diagram(graph)
        >>> print(mermaid)
        ```mermaid
        graph TD
            create-product-brief --> create-prd
            ...
        ```
    """
    lines = [
        "```mermaid",
        f"graph {direction}",
    ]

    # Add nodes with labels
    for wf_id, workflow in graph.items():
        # Sanitize ID for Mermaid (replace dashes with underscores)
        safe_id = wf_id.replace("-", "_")
        label = workflow.name or wf_id
        lines.append(f"    {safe_id}[\"{label}\"]")

    lines.append("")

    # Add edges
    for wf_id, workflow in graph.items():
        safe_id = wf_id.replace("-", "_")

        if workflow.next_success:
            if workflow.next_success == "retry":
                lines.append(f"    {safe_id} -->|retry| {safe_id}")
            elif workflow.next_success in graph:
                safe_target = workflow.next_success.replace("-", "_")
                lines.append(f"    {safe_id} -->|success| {safe_target}")

        if workflow.next_failure and workflow.next_failure != workflow.next_success:
            if workflow.next_failure == "retry":
                lines.append(f"    {safe_id} -.->|retry| {safe_id}")
            elif workflow.next_failure in graph:
                safe_target = workflow.next_failure.replace("-", "_")
                lines.append(f"    {safe_id} -.->|failure| {safe_target}")

    lines.append("```")

    return "\n".join(lines)


def generate_ascii_tree(
    graph: dict[str, WorkflowContract],
    start_id: str,
    visited: Optional[set] = None,
    prefix: str = "",
    is_last: bool = True,
) -> str:
    """
    Generate ASCII tree representation of workflow graph.

    Args:
        graph: Workflow graph
        start_id: Starting workflow ID
        visited: Set of visited IDs (for cycle detection)
        prefix: Line prefix for indentation
        is_last: Whether this is the last child

    Returns:
        ASCII tree as string
    """
    if visited is None:
        visited = set()

    lines = []

    # Cycle detection
    if start_id in visited:
        return f"{prefix}{'└── ' if is_last else '├── '}(cycle: {start_id})\n"

    visited.add(start_id)

    # Current node
    connector = "└── " if is_last else "├── "
    workflow = graph.get(start_id)

    if workflow:
        status_icon = "✓" if workflow.status == "done" else "○"
        lines.append(f"{prefix}{connector}{status_icon} {start_id}")

        # Child prefix
        child_prefix = prefix + ("    " if is_last else "│   ")

        # Add children (success and failure paths)
        children = []
        if workflow.next_success and workflow.next_success != "retry":
            children.append(("success", workflow.next_success))
        if workflow.next_failure and workflow.next_failure != "retry":
            if workflow.next_failure != workflow.next_success:
                children.append(("failure", workflow.next_failure))

        for i, (path_type, child_id) in enumerate(children):
            is_last_child = i == len(children) - 1
            lines.append(generate_ascii_tree(
                graph,
                child_id,
                visited.copy(),  # Copy to allow parallel paths
                child_prefix,
                is_last_child,
            ))
    else:
        lines.append(f"{prefix}{connector}✗ {start_id} (not found)")

    return "".join(lines)


def print_status_summary(graph: dict[str, WorkflowContract]) -> None:
    """Print summary of workflow statuses."""
    total = len(graph)
    done = sum(1 for wf in graph.values() if wf.status == "done")
    pending = sum(1 for wf in graph.values() if wf.status == "pending")
    no_status = total - done - pending

    print("\nStatus Summary:")
    print("=" * 30)
    print(f"  Total workflows: {total}")
    print(f"  Done:           {done}")
    print(f"  Pending:        {pending}")
    print(f"  No status:      {no_status}")

    if total > 0:
        progress = (done / total) * 100
        bar_width = 20
        filled = int(bar_width * done / total)
        bar = "█" * filled + "░" * (bar_width - filled)
        print(f"\n  Progress: [{bar}] {progress:.0f}%")
