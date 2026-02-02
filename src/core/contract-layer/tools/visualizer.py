"""
Contract Layer - Visualizer

Wizualizacja grafu zależności i statusu zadań.
Czyta kontrakty z plików markdown i generuje dashboard.
"""

import os
import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    id: str
    type: str = "task"
    input: list[str] = field(default_factory=list)
    output: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    source_file: Optional[Path] = None
    status: str = "pending"  # pending, running, completed, failed


class ContractReader:
    """Czyta kontrakty z YAML front matter"""

    FRONT_MATTER = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)

    def read_directory(self, path: Path) -> dict[str, Task]:
        """Czyta wszystkie pliki .md z katalogu"""
        tasks = {}
        for md_file in Path(path).rglob("*.md"):
            task = self.read_file(md_file)
            if task:
                tasks[task.id] = task
        return tasks

    def read_file(self, filepath: Path) -> Optional[Task]:
        """Czyta pojedynczy plik"""
        content = filepath.read_text(encoding='utf-8')
        match = self.FRONT_MATTER.match(content)
        if not match:
            return None

        try:
            contract = yaml.safe_load(match.group(1))
            if not contract or 'id' not in contract:
                return None

            return Task(
                id=contract['id'],
                type=contract.get('type', 'task'),
                input=contract.get('input', []),
                output=contract.get('output', []),
                depends_on=contract.get('depends_on', []),
                source_file=filepath
            )
        except yaml.YAMLError:
            return None


class Visualizer:
    """Generuje wizualizację grafu i statusu"""

    def __init__(self, tasks: dict[str, Task]):
        self.tasks = tasks

    def print_dashboard(self) -> None:
        """Wyświetla dashboard w terminalu"""
        print("\n" + "=" * 60)
        print("  CONTRACT LAYER - DASHBOARD")
        print("=" * 60)

        # Stats
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks.values() if t.status == "completed")
        running = sum(1 for t in self.tasks.values() if t.status == "running")
        pending = sum(1 for t in self.tasks.values() if t.status == "pending")

        print(f"\n  Tasks: {total} total | {completed} done | {running} running | {pending} pending")
        print(f"  Progress: [{'#' * completed}{'.' * (total - completed)}] {completed}/{total}")

        # Graph
        print("\n  DEPENDENCY GRAPH:")
        print("  " + "-" * 40)
        self._print_graph()

        # Task list
        print("\n  TASKS:")
        print("  " + "-" * 40)
        for task in self._topological_order():
            status_icon = {"pending": "[ ]", "running": "[~]", "completed": "[x]", "failed": "[!]"}
            icon = status_icon.get(task.status, "?")
            deps = f" <- [{', '.join(task.depends_on)}]" if task.depends_on else ""
            print(f"  {icon} {task.id}{deps}")

        print("\n" + "=" * 60)

    def _print_graph(self) -> None:
        """Wyświetla graf ASCII"""
        order = self._topological_order()
        levels = self._calculate_levels()

        for task in order:
            level = levels.get(task.id, 0)
            indent = "  " * level
            arrow = "-> " if level > 0 else ""
            print(f"  {indent}{arrow}[{task.id}]")

    def _topological_order(self) -> list[Task]:
        """Zwraca zadania w kolejności topologicznej"""
        visited = set()
        order = []

        def visit(task_id):
            if task_id in visited or task_id not in self.tasks:
                return
            visited.add(task_id)
            task = self.tasks[task_id]
            for dep in task.depends_on:
                visit(dep)
            order.append(task)

        for task_id in self.tasks:
            visit(task_id)

        return order

    def _calculate_levels(self) -> dict[str, int]:
        """Oblicza poziom każdego zadania (dla wizualizacji)"""
        levels = {}

        def get_level(task_id):
            if task_id in levels:
                return levels[task_id]
            if task_id not in self.tasks:
                return 0

            task = self.tasks[task_id]
            if not task.depends_on:
                levels[task_id] = 0
            else:
                levels[task_id] = 1 + max(get_level(dep) for dep in task.depends_on)

            return levels[task_id]

        for task_id in self.tasks:
            get_level(task_id)

        return levels

    def generate_mermaid(self) -> str:
        """Generuje diagram Mermaid"""
        lines = ["graph TD"]

        for task in self.tasks.values():
            # Node
            status_style = {
                "pending": ":::pending",
                "running": ":::running",
                "completed": ":::completed",
                "failed": ":::failed"
            }
            style = status_style.get(task.status, "")
            lines.append(f"    {task.id}[{task.id}]{style}")

            # Edges
            for dep in task.depends_on:
                if dep in self.tasks:
                    lines.append(f"    {dep} --> {task.id}")

        # Styles
        lines.extend([
            "",
            "    classDef pending fill:#f9f9f9,stroke:#999",
            "    classDef running fill:#fff3cd,stroke:#ffc107",
            "    classDef completed fill:#d4edda,stroke:#28a745",
            "    classDef failed fill:#f8d7da,stroke:#dc3545"
        ])

        return "\n".join(lines)


def main():
    """Demo"""
    import sys

    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        # Default: current directory
        path = Path(".")

    print(f"Scanning: {path.absolute()}")

    reader = ContractReader()
    tasks = reader.read_directory(path)

    if not tasks:
        print("No tasks with contracts found.")
        return

    viz = Visualizer(tasks)
    viz.print_dashboard()

    # Generate mermaid
    mermaid = viz.generate_mermaid()
    print("\nMERMAID DIAGRAM:")
    print("-" * 40)
    print(mermaid)


if __name__ == "__main__":
    main()
