"""
BMAD Workflow Graph Builder

Build and analyze workflow dependency graphs.
"""

from pathlib import Path
from typing import Iterator

from .parser import WorkflowContract, parse_workflow, parse_all_workflows


def build_workflow_graph(
    directory: Path,
    pattern: str = "**/*.md"
) -> dict[str, WorkflowContract]:
    """
    Build graph of all workflows from directory.

    Args:
        directory: Path to workflows directory
        pattern: Glob pattern for finding workflow files

    Returns:
        Dict mapping workflow ID to WorkflowContract

    Example:
        >>> graph = build_workflow_graph(Path("workflows/"))
        >>> for wf_id, wf in graph.items():
        ...     print(f"{wf_id} -> {wf.next_success}")
    """
    return parse_all_workflows(directory)


def get_workflow_sequence(
    graph: dict[str, WorkflowContract],
    start_id: str,
    follow: str = "success"
) -> list[str]:
    """
    Get linear sequence of workflows from start following success/failure path.

    Args:
        graph: Workflow graph from build_workflow_graph
        start_id: ID of workflow to start from
        follow: Which path to follow ('success' or 'failure')

    Returns:
        List of workflow IDs in sequence

    Example:
        >>> sequence = get_workflow_sequence(graph, "create-product-brief")
        >>> print(sequence)
        ['create-product-brief', 'create-prd', 'create-architecture', ...]
    """
    sequence = []
    current = start_id
    visited = set()

    while current and current not in visited:
        if current not in graph:
            # Reference to workflow not in graph
            sequence.append(f"{current} (not found)")
            break

        visited.add(current)
        sequence.append(current)

        workflow = graph[current]
        if follow == "success":
            current = workflow.next_success
        else:
            current = workflow.next_failure

        # Handle 'retry' as special case
        if current == "retry":
            sequence.append("(retry)")
            break

    return sequence


def find_entry_points(graph: dict[str, WorkflowContract]) -> list[str]:
    """
    Find workflows that are not referenced by any other workflow.
    These are potential entry points / starting workflows.

    Args:
        graph: Workflow graph

    Returns:
        List of workflow IDs that are entry points
    """
    # Collect all referenced workflow IDs
    referenced = set()
    for workflow in graph.values():
        if workflow.next_success and workflow.next_success != "retry":
            referenced.add(workflow.next_success)
        if workflow.next_failure and workflow.next_failure != "retry":
            referenced.add(workflow.next_failure)

    # Find workflows not referenced
    entry_points = [
        wf_id for wf_id in graph.keys()
        if wf_id not in referenced
    ]

    return sorted(entry_points)


def find_orphan_workflows(graph: dict[str, WorkflowContract]) -> list[str]:
    """
    Find workflows that have no next steps and are not referenced.

    Args:
        graph: Workflow graph

    Returns:
        List of orphan workflow IDs
    """
    # Collect all referenced workflow IDs
    referenced = set()
    for workflow in graph.values():
        if workflow.next_success and workflow.next_success != "retry":
            referenced.add(workflow.next_success)
        if workflow.next_failure and workflow.next_failure != "retry":
            referenced.add(workflow.next_failure)

    # Find workflows with no next that are not referenced
    orphans = [
        wf_id for wf_id, wf in graph.items()
        if not wf.has_next and wf_id not in referenced
    ]

    return sorted(orphans)


def find_broken_references(graph: dict[str, WorkflowContract]) -> list[tuple[str, str]]:
    """
    Find workflow references that point to non-existent workflows.

    Args:
        graph: Workflow graph

    Returns:
        List of tuples (source_workflow, missing_target)
    """
    broken = []

    for wf_id, workflow in graph.items():
        if workflow.next_success:
            if workflow.next_success != "retry" and workflow.next_success not in graph:
                broken.append((wf_id, workflow.next_success))

        if workflow.next_failure:
            if workflow.next_failure != "retry" and workflow.next_failure not in graph:
                broken.append((wf_id, workflow.next_failure))

    return broken


def get_workflow_dependencies(
    graph: dict[str, WorkflowContract],
    workflow_id: str
) -> dict[str, list[str]]:
    """
    Get dependencies for a specific workflow.

    Args:
        graph: Workflow graph
        workflow_id: ID of workflow to analyze

    Returns:
        Dict with 'inputs', 'outputs', 'depends_on', 'blocks'
    """
    if workflow_id not in graph:
        return {}

    workflow = graph[workflow_id]

    # Find workflows that lead to this one
    depends_on = [
        wf_id for wf_id, wf in graph.items()
        if wf.next_success == workflow_id or wf.next_failure == workflow_id
    ]

    # Find workflows this one leads to
    blocks = []
    if workflow.next_success and workflow.next_success != "retry":
        blocks.append(workflow.next_success)
    if workflow.next_failure and workflow.next_failure != "retry":
        if workflow.next_failure not in blocks:
            blocks.append(workflow.next_failure)

    return {
        'inputs': workflow.inputs,
        'outputs': workflow.outputs,
        'depends_on': depends_on,
        'blocks': blocks,
    }


def topological_sort(graph: dict[str, WorkflowContract]) -> list[str]:
    """
    Return workflows in topological order (dependencies first).

    Args:
        graph: Workflow graph

    Returns:
        List of workflow IDs in topological order
    """
    # Build adjacency list (reversed - from target to source)
    in_degree = {wf_id: 0 for wf_id in graph}

    for workflow in graph.values():
        if workflow.next_success and workflow.next_success in graph:
            in_degree[workflow.next_success] += 1
        if workflow.next_failure and workflow.next_failure in graph:
            if workflow.next_failure != workflow.next_success:
                in_degree[workflow.next_failure] += 1

    # Start with nodes that have no incoming edges
    queue = [wf_id for wf_id, degree in in_degree.items() if degree == 0]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        workflow = graph[current]

        for next_id in [workflow.next_success, workflow.next_failure]:
            if next_id and next_id in in_degree and next_id != "retry":
                in_degree[next_id] -= 1
                if in_degree[next_id] == 0:
                    queue.append(next_id)

    return result
