"""
Deep Process Engine - Core
Version: 0.1
"""

from pathlib import Path
from typing import Optional, Dict, Any
import yaml

from .loader import ProcessLoader, ProcessDefinition
from .contract import ContractParser, WorkflowContract

class DeepProcessEngine:
    def __init__(self, project_root: Path = Path(".")):
        self.project_root = project_root
        self.processes_root = project_root / "src/core/deep-process/processes"
        self.state_dir = project_root / ".state"
        
        self.loader = ProcessLoader(self.processes_root)
        self.active_process: Optional[ProcessDefinition] = None
        self.current_state: Dict[str, Any] = {}

    def initialize_project(self, process_id: str, project_name: str) -> bool:
        """Initializes a new project with the given process."""
        process = self.loader.load_process(process_id)
        if not process:
            return False

        self.state_dir.mkdir(parents=True, exist_ok=True)
        
        # Create initial state
        state = {
            "project": {
                "name": project_name,
                "process_id": process_id
            },
            "current_phase": list(process.phases.keys())[0], # Default to first phase
            "phase_progress": 0.0
        }
        
        self._save_state(state)
        self.active_process = process
        return True

    def load_state(self) -> bool:
        """Loads existing project state."""
        state_path = self.state_dir / "process.yaml" # Simplified for MVP
        if not state_path.exists():
            return False
            
        try:
            self.current_state = yaml.safe_load(state_path.read_text(encoding='utf-8'))
            process_id = self.current_state.get("project", {}).get("process_id")
            if process_id:
                self.active_process = self.loader.load_process(process_id)
            return True
        except Exception:
            return False

    def get_next_step(self) -> Optional[WorkflowContract]:
        """Determines the next step based on current state."""
        if not self.active_process:
            return None

        current_phase_id = self.current_state.get("current_phase")
        if not current_phase_id:
            return None

        phase = self.active_process.phases.get(current_phase_id)
        if not phase:
            return None

        # Logic to determine step:
        # 1. If no history, assume entry point of current phase
        # 2. (In future) Check history/status to find next pending step
        
        # MVP: Just return entry point
        entry_point_path = phase.path / phase.entry_point
        return ContractParser.parse(entry_point_path)

    def _save_state(self, state: Dict[str, Any]):
        """Saves state to disk."""
        (self.state_dir / "process.yaml").write_text(yaml.dump(state), encoding='utf-8')
        self.current_state = state

# Usage Example:
# engine = DeepProcessEngine()
# engine.initialize_project("project-management", "My New App")
# next_step = engine.get_next_step()
# print(f"Next step: {next_step.name}")
