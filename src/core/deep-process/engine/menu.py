"""
Deep Process Engine - Menu Generator
Version: 0.2 (Context Aware)
"""

from typing import List, Dict, Any
from pathlib import Path
from dataclasses import dataclass
from .core import DeepProcessEngine
from .contract import ContractParser

@dataclass
class MenuOption:
    id: str
    label: str
    type: str # action, navigation, info, header
    context: Dict[str, Any] = None

class MenuGenerator:
    def __init__(self, engine: DeepProcessEngine):
        self.engine = engine

    def generate_menu(self) -> List[MenuOption]:
        options = []

        # 1. Initialization Check
        if not self.engine.active_process:
            available = self.engine.loader.list_available_processes()
            for proc_id in available:
                options.append(MenuOption(
                    id=f"init:{proc_id}",
                    label=f"Initialize new project with '{proc_id}' process",
                    type="action"
                ))
            return options

        # 2. Scan Process for Contextual Actions
        # Strategy: Iterate over all phases and steps in the active process
        # If a step has 'context_menu', scan for matching artifacts
        
        process = self.engine.active_process
        for phase_id, phase_def in process.phases.items():
            # Scan directory for .md files
            if not phase_def.path.exists():
                continue
                
            for step_file in phase_def.path.glob("*.md"):
                contract = ContractParser.parse(step_file)
                if not contract:
                    continue
                
                # Case A: Static Steps (Entry Points)
                # If it's the entry point of current phase, show it
                is_current_entry = (phase_id == self.engine.current_state.get("current_phase") 
                                   and step_file.name == phase_def.entry_point)
                
                if is_current_entry:
                     options.append(MenuOption(
                        id=f"exec:{contract.id}",
                        label=f"▶ EXECUTE NEXT: {contract.name}",
                        type="action",
                        context={"contract": contract}
                    ))

                # Case B: Contextual Steps (e.g., "Active Epics")
                if contract.context_menu == "Active Epics":
                    self._add_epic_actions(options, contract)
                elif contract.context_menu == "Active Stories":
                    # self._add_story_actions(options, contract)
                    pass

        # 3. Global Actions
        options.append(MenuOption(id="sep1", label="--- Global ---", type="header"))
        options.append(MenuOption(id="status", label="Show Project Status", type="info"))
        options.append(MenuOption(id="unknowns", label="Check for Unknowns", type="info"))
        
        return options

    def _add_epic_actions(self, options: List[MenuOption], contract: Any):
        """Scans artifacts/epics/ and adds actions for each."""
        epics_dir = self.engine.project_root / "artifacts" / "epics"
        if not epics_dir.exists():
            return

        epics = list(epics_dir.glob("*.yaml")) + list(epics_dir.glob("*.md"))
        if not epics:
            return

        options.append(MenuOption(id="sep_epics", label=f"--- {contract.name} ---", type="header"))
        
        for epic_file in epics:
            epic_id = epic_file.stem # e.g. EPIC-001
            
            # Create a specialized contract for this instance
            # We inject the specific file path into inputs
            
            options.append(MenuOption(
                id=f"exec:{contract.id}:{epic_id}",
                label=f"  ↳ For {epic_id}",
                type="action",
                context={
                    "contract": contract, 
                    "variables": {"epic_id": epic_id} # Variable injection
                }
            ))