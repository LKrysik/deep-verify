"""
Deep Process Engine - Process Loader
Version: 0.1
"""

import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class PhaseDefinition:
    id: str
    name: str
    path: Path
    entry_point: str

@dataclass
class ProcessDefinition:
    id: str
    version: str
    domain: str
    description: str
    phases: Dict[str, PhaseDefinition] = field(default_factory=dict)
    root_path: Path = field(default=Path("."))

class ProcessLoader:
    """Loads process definitions from the file system."""

    def __init__(self, processes_root: Path):
        self.processes_root = processes_root

    def load_process(self, process_id: str) -> Optional[ProcessDefinition]:
        """Loads a specific process by ID."""
        process_dir = self.processes_root / process_id
        manifest_path = process_dir / "process.yaml"

        if not manifest_path.exists():
            print(f"Process manifest not found: {manifest_path}")
            return None

        try:
            data = yaml.safe_load(manifest_path.read_text(encoding='utf-8'))
            
            process = ProcessDefinition(
                id=data['id'],
                version=data.get('version', '1.0'),
                domain=data.get('domain', 'unknown'),
                description=data.get('description', ''),
                root_path=process_dir
            )

            for phase_data in data.get('phases', []):
                phase = PhaseDefinition(
                    id=phase_data['id'],
                    name=phase_data['name'],
                    path=process_dir / phase_data['path'],
                    entry_point=phase_data.get('entry_point')
                )
                process.phases[phase.id] = phase

            return process

        except Exception as e:
            print(f"Error loading process {process_id}: {e}")
            return None

    def list_available_processes(self) -> List[str]:
        """Scans the root directory for available processes."""
        processes = []
        if not self.processes_root.exists():
            return []
            
        for item in self.processes_root.iterdir():
            if item.is_dir() and (item / "process.yaml").exists():
                processes.append(item.name)
        return processes
