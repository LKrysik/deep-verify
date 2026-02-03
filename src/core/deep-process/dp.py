#!/usr/bin/env python3
"""
Deep Process CLI
Version: 1.0

Usage:
    python dp.py init <process> <name>    - Create new project
    python dp.py list                      - List all projects
    python dp.py status                    - Show active project status
    python dp.py switch <project-id>       - Switch active project
    python dp.py resume                    - Resume active project (show context)
    python dp.py processes                 - List available processes
"""

import sys
import argparse
from pathlib import Path

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent))

from engine.project_manager import ProjectManager
from engine.session import SessionManager


def get_root() -> Path:
    """Get project root (4 levels up from this file)."""
    return Path(__file__).parent.parent.parent.parent


def cmd_init(args):
    """Initialize a new project."""
    root = get_root()
    pm = ProjectManager(root)

    project_path = pm.create_project(
        project_id=args.name.lower().replace(' ', '-'),
        project_name=args.name,
        process_id=args.process,
        set_active=True
    )

    if project_path:
        print(f"\n Project created at: {project_path}")
        print(f"\n Next: Run 'python dp.py resume' to start working")


def cmd_list(args):
    """List all projects."""
    root = get_root()
    pm = ProjectManager(root)

    projects = pm.list_projects()

    if not projects:
        print("\n No projects found.")
        print(" Create one with: python dp.py init <process> <name>")
        return

    print("\n PROJECTS")
    print(" " + "=" * 60)

    for p in projects:
        active_marker = " *" if p.is_active else "  "
        print(f"{active_marker} {p.id}")
        print(f"     Name: {p.name}")
        print(f"     Process: {p.process_id}")
        print(f"     Created: {p.created_at[:10]}")
        print()


def cmd_status(args):
    """Show active project status."""
    root = get_root()
    pm = ProjectManager(root)

    project = pm.get_active_project()
    if not project:
        print("\n No active project.")
        print(" Use 'python dp.py switch <id>' or 'python dp.py init <process> <name>'")
        return

    session = SessionManager.from_project_path(project.path)
    ctx = session.load_context()

    print()
    print("+" + "=" * 62 + "+")
    print(f"| PROJECT: {ctx.project_name:<51} |")
    print("+" + "=" * 62 + "+")
    print(f"| Process: {ctx.process_id:<52} |")
    print(f"| Phase: {(ctx.current_phase or 'Not started'):<54} |")

    # Progress bar
    progress_pct = int(ctx.phase_progress * 100)
    bar_filled = int(ctx.phase_progress * 20)
    bar = "" * bar_filled + "" * (20 - bar_filled)
    print(f"| Progress: [{bar}] {progress_pct:>3}%{' ' * 24} |")

    # Blockers
    if ctx.blocking_items:
        print("|" + "-" * 62 + "|")
        print(f"| BLOCKERS: {len(ctx.blocking_items):<51} |")
        for b in ctx.blocking_items[:3]:
            print(f"|   - {b.get('title', 'Unknown')[:54]:<55} |")

    # Last action
    if ctx.last_action:
        print("|" + "-" * 62 + "|")
        print(f"| Last: {ctx.last_action.get('name', 'Unknown'):<55} |")

    print("+" + "=" * 62 + "+")
    print()


def cmd_switch(args):
    """Switch active project."""
    root = get_root()
    pm = ProjectManager(root)

    if pm.set_active(args.project_id):
        print(f"\n Switched to: {args.project_id}")
        cmd_status(args)


def cmd_resume(args):
    """Resume working on active project."""
    root = get_root()
    pm = ProjectManager(root)

    project = pm.get_active_project()
    if not project:
        print("\n No active project.")
        print(" Use 'python dp.py init <process> <name>' to create one")
        return

    session = SessionManager.from_project_path(project.path)
    ctx = session.load_context()

    print()
    print("+" + "=" * 62 + "+")
    print(f"|{'RESUMING PROJECT':^62}|")
    print("+" + "=" * 62 + "+")
    print(f"| Name: {ctx.project_name:<55} |")
    print(f"| Process: {ctx.process_id:<52} |")
    print(f"| Phase: {(ctx.current_phase or 'Not started'):<54} |")
    print("+" + "-" * 62 + "+")

    if ctx.current_phase:
        print(f"|{'CONTEXT FOR LLM':^62}|")
        print("+" + "-" * 62 + "+")
        print(f"| Load process definition from:                                |")
        print(f"|   src/core/deep-process/processes/{ctx.process_id}/process.yaml  |")
        print(f"|                                                              |")
        print(f"| Current state at:                                            |")
        print(f"|   projects/{project.id}/.state/                         |")
        print("+" + "=" * 62 + "+")
    else:
        print(f"|{'READY TO START':^62}|")
        print("+" + "-" * 62 + "+")
        print(f"| To begin, load the process definition and start phase 1.    |")
        print("+" + "=" * 62 + "+")

    print()


def cmd_processes(args):
    """List available processes."""
    root = get_root()
    processes_dir = root / "src" / "core" / "deep-process" / "processes"

    print("\n AVAILABLE PROCESSES")
    print(" " + "=" * 40)

    if not processes_dir.exists():
        print(" No processes found.")
        return

    for item in sorted(processes_dir.iterdir()):
        if item.is_dir():
            manifest = item / "process.yaml"
            if manifest.exists():
                import yaml
                try:
                    data = yaml.safe_load(manifest.read_text(encoding='utf-8'))
                    print(f"\n   {item.name}")
                    print(f"   {data.get('description', 'No description')[:50]}")
                except:
                    print(f"\n   {item.name}")
            else:
                # Check for workflow.md (legacy format)
                workflow = item / "workflow.md"
                if workflow.exists():
                    print(f"\n   {item.name} (workflow.md format)")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Deep Process CLI - Manage process-driven projects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python dp.py init deep-explore "My Decision Analysis"
    python dp.py list
    python dp.py status
    python dp.py switch my-decision-analysis
    python dp.py resume
    python dp.py processes
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # init
    init_parser = subparsers.add_parser('init', help='Create new project')
    init_parser.add_argument('process', help='Process ID (e.g., deep-explore, bmm)')
    init_parser.add_argument('name', help='Project name')
    init_parser.set_defaults(func=cmd_init)

    # list
    list_parser = subparsers.add_parser('list', help='List all projects')
    list_parser.set_defaults(func=cmd_list)

    # status
    status_parser = subparsers.add_parser('status', help='Show active project status')
    status_parser.set_defaults(func=cmd_status)

    # switch
    switch_parser = subparsers.add_parser('switch', help='Switch active project')
    switch_parser.add_argument('project_id', help='Project ID to switch to')
    switch_parser.set_defaults(func=cmd_switch)

    # resume
    resume_parser = subparsers.add_parser('resume', help='Resume active project')
    resume_parser.set_defaults(func=cmd_resume)

    # processes
    processes_parser = subparsers.add_parser('processes', help='List available processes')
    processes_parser.set_defaults(func=cmd_processes)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
