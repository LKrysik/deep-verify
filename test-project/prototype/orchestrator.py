"""
Python-LLM Contract Layer - Orchestrator Prototype

Python jako dyrygent:
- Czyta kontrakty (YAML front matter)
- Buduje graf zależności
- Zleca LLM wykonanie
- Parsuje wyniki (w tym spawn)
"""

import os
import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from collections import deque


@dataclass
class Task:
    """Reprezentacja zadania z kontraktem"""
    id: str
    type: str = "task"
    input: list[str] = field(default_factory=list)
    output: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    source_file: Optional[Path] = None
    content: str = ""  # treść markdown (dla LLM)
    status: str = "pending"  # pending, running, completed, failed


class ContractParser:
    """Parsuje YAML front matter z plików markdown"""

    FRONT_MATTER_PATTERN = re.compile(
        r'^---\s*\n(.*?)\n---\s*\n(.*)$',
        re.DOTALL
    )

    def parse_file(self, filepath: Path) -> Optional[Task]:
        """Parsuje plik markdown z kontraktem"""
        content = filepath.read_text(encoding='utf-8')
        return self.parse_content(content, filepath)

    def parse_content(self, content: str, source: Path = None) -> Optional[Task]:
        """Parsuje treść markdown z kontraktem"""
        match = self.FRONT_MATTER_PATTERN.match(content)
        if not match:
            return None

        yaml_content, markdown_content = match.groups()

        try:
            contract = yaml.safe_load(yaml_content)
        except yaml.YAMLError:
            return None

        if not contract or 'id' not in contract:
            return None

        return Task(
            id=contract['id'],
            type=contract.get('type', 'task'),
            input=contract.get('input', []),
            output=contract.get('output', []),
            depends_on=contract.get('depends_on', []),
            source_file=source,
            content=markdown_content.strip()
        )


class SpawnDetector:
    """Wykrywa bloki spawn w odpowiedzi LLM"""

    SPAWN_PATTERN = re.compile(
        r'~~~spawn\s*\n(.*?)~~~',
        re.DOTALL
    )

    def find_spawns(self, llm_response: str) -> list[str]:
        """Znajduje wszystkie bloki spawn w odpowiedzi"""
        return self.SPAWN_PATTERN.findall(llm_response)

    def extract_response_without_spawns(self, llm_response: str) -> str:
        """Usuwa bloki spawn z odpowiedzi"""
        return self.SPAWN_PATTERN.sub('', llm_response).strip()


class Orchestrator:
    """
    Główny orkiestrator - Python jako dyrygent

    Odpowiedzialności:
    - Skanuje katalog z zadaniami
    - Buduje graf zależności
    - Wykonuje zadania w kolejności
    - Obsługuje spawn (dynamiczne zadania)
    """

    def __init__(self, processes_dir: Path, output_dir: Path):
        self.processes_dir = Path(processes_dir)
        self.output_dir = Path(output_dir)
        self.parser = ContractParser()
        self.spawn_detector = SpawnDetector()
        self.tasks: dict[str, Task] = {}
        self.execution_order: list[str] = []

    def scan_tasks(self) -> None:
        """Skanuje katalog i ładuje wszystkie zadania"""
        self.tasks.clear()

        for md_file in self.processes_dir.glob("*.md"):
            task = self.parser.parse_file(md_file)
            if task:
                self.tasks[task.id] = task
                print(f"  Loaded: {task.id} (depends: {task.depends_on})")

    def build_execution_order(self) -> list[str]:
        """Buduje kolejność wykonania (topological sort)"""
        # Kahn's algorithm
        in_degree = {task_id: 0 for task_id in self.tasks}

        for task in self.tasks.values():
            for dep in task.depends_on:
                if dep in self.tasks:
                    in_degree[task.id] = in_degree.get(task.id, 0) + 1

        queue = deque([tid for tid, deg in in_degree.items() if deg == 0])
        order = []

        while queue:
            task_id = queue.popleft()
            order.append(task_id)

            for other_id, other_task in self.tasks.items():
                if task_id in other_task.depends_on:
                    in_degree[other_id] -= 1
                    if in_degree[other_id] == 0:
                        queue.append(other_id)

        self.execution_order = order
        return order

    def execute_task(self, task: Task, llm_executor) -> str:
        """
        Wykonuje pojedyncze zadanie

        Args:
            task: Zadanie do wykonania
            llm_executor: Funkcja która wysyła do LLM i zwraca odpowiedź
                          signature: (markdown_content: str) -> str

        Returns:
            Odpowiedź LLM (bez bloków spawn)
        """
        task.status = "running"
        print(f"  Executing: {task.id}")

        # Zlec LLM wykonanie
        llm_response = llm_executor(task.content)

        # Sprawdź czy są spawn
        spawns = self.spawn_detector.find_spawns(llm_response)
        for spawn_content in spawns:
            self._handle_spawn(spawn_content)

        # Wyczyść odpowiedź z bloków spawn
        clean_response = self.spawn_detector.extract_response_without_spawns(llm_response)

        # Zapisz output
        self._save_output(task, clean_response)

        task.status = "completed"
        return clean_response

    def _handle_spawn(self, spawn_content: str) -> None:
        """Obsługuje dynamicznie wygenerowane zadanie"""
        new_task = self.parser.parse_content(spawn_content)
        if new_task:
            # Zapisz jako nowy plik
            new_file = self.processes_dir / f"{new_task.id}.md"
            new_file.write_text(f"---\n{yaml.dump({'id': new_task.id, 'type': new_task.type, 'input': new_task.input, 'output': new_task.output, 'depends_on': new_task.depends_on})}---\n\n{new_task.content}", encoding='utf-8')

            # Dodaj do listy zadań
            self.tasks[new_task.id] = new_task
            print(f"  Spawned: {new_task.id}")

    def _save_output(self, task: Task, content: str) -> None:
        """Zapisuje output zadania"""
        task_output_dir = self.output_dir / task.id
        task_output_dir.mkdir(parents=True, exist_ok=True)

        output_file = task_output_dir / "result.md"
        output_file.write_text(content, encoding='utf-8')
        print(f"  Output: {output_file}")

    def run(self, llm_executor) -> dict[str, str]:
        """
        Uruchamia cały workflow

        Args:
            llm_executor: Funkcja wykonująca LLM

        Returns:
            Słownik {task_id: result}
        """
        print("\n=== SCAN ===")
        self.scan_tasks()

        print("\n=== BUILD ORDER ===")
        order = self.build_execution_order()
        print(f"  Order: {' -> '.join(order)}")

        print("\n=== EXECUTE ===")
        results = {}

        # Wykonuj w pętli (może się pojawić spawn)
        executed = set()
        while True:
            # Znajdź następne zadanie do wykonania
            next_task = None
            for task_id in self.tasks:
                if task_id in executed:
                    continue
                task = self.tasks[task_id]
                # Sprawdź czy wszystkie zależności wykonane
                if all(dep in executed for dep in task.depends_on):
                    next_task = task
                    break

            if not next_task:
                break

            result = self.execute_task(next_task, llm_executor)
            results[next_task.id] = result
            executed.add(next_task.id)

        print("\n=== DONE ===")
        print(f"  Executed: {len(executed)} tasks")

        return results


# ============================================================
# DEMO / TEST
# ============================================================

def mock_llm_executor(markdown_content: str) -> str:
    """
    Mock LLM - symuluje odpowiedź
    W prawdziwej implementacji: wywołanie API Claude/GPT/etc.
    """
    # Symulacja: zwróć echo + czasem spawn
    response = f"[LLM wykonał zadanie]\n\nTreść zadania była:\n{markdown_content[:100]}..."

    # Symulacja spawn - jeśli treść zawiera słowo "problem"
    if "problem" in markdown_content.lower():
        response += """

~~~spawn
---
id: investigate-problem
type: task
input: [problem_description]
output: [solution]
depends_on: []
---

Zbadaj znaleziony problem i zaproponuj rozwiązanie.
~~~
"""

    return response


if __name__ == "__main__":
    # Demo
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        processes = Path(tmpdir) / "processes"
        output = Path(tmpdir) / "output"
        processes.mkdir()

        # Stwórz przykładowe zadania
        (processes / "task-1.md").write_text("""---
id: analyze
type: task
input: [config_file]
output: [report]
depends_on: []
---

Przeanalizuj plik konfiguracyjny i znajdź problemy.
""", encoding='utf-8')

        (processes / "task-2.md").write_text("""---
id: generate-report
type: task
input: [report]
output: [final_report]
depends_on: [analyze]
---

Na podstawie analizy wygeneruj raport końcowy.
""", encoding='utf-8')

        # Uruchom orchestrator
        orch = Orchestrator(processes, output)
        results = orch.run(mock_llm_executor)

        print("\n=== RESULTS ===")
        for task_id, result in results.items():
            print(f"\n{task_id}:")
            print(result[:200])
