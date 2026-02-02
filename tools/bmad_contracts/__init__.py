"""
BMAD Contract Parser v0.1

Parse, validate, and visualize BMAD workflow contracts.
"""

from .parser import (
    parse_frontmatter,
    parse_workflow,
    parse_output_contract,
    WorkflowContract,
    OutputContract,
)
from .graph import (
    build_workflow_graph,
    get_workflow_sequence,
    find_entry_points,
    find_orphan_workflows,
    find_broken_references,
)
from .validator import (
    validate_output,
    validate_workflow_references,
    ValidationError,
)
from .visualizer import (
    print_workflow_graph,
    print_workflow_list,
    generate_mermaid_diagram,
)

__version__ = "0.1.0"
__all__ = [
    # Parser
    "parse_frontmatter",
    "parse_workflow",
    "parse_output_contract",
    "WorkflowContract",
    "OutputContract",
    # Graph
    "build_workflow_graph",
    "get_workflow_sequence",
    "find_entry_points",
    "find_orphan_workflows",
    "find_broken_references",
    # Validator
    "validate_output",
    "validate_workflow_references",
    "ValidationError",
    # Visualizer
    "print_workflow_graph",
    "print_workflow_list",
    "generate_mermaid_diagram",
]
