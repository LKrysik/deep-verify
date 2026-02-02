"""
Deep Process Engine - Menu Generator
Version: 0.1
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from .core import DeepProcessEngine

@dataclass
class MenuOption:
    id: str
    label: str
    type: str # action, navigation, info
    context: Dict[str, Any] = None

class MenuGenerator:
    def __init__(self, engine: DeepProcessEngine):
        self.engine = engine

    def generate_menu(self) -> List[MenuOption]:
        options = []

        # 1. Check if project is initialized
        if not self.engine.active_process:
            available = self.engine.loader.list_available_processes()
            for proc_id in available:
                options.append(MenuOption(
                    id=f"init:{proc_id}",
                    label=f"Initialize new project with '{proc_id}' process",
                    type="action"
                ))
            return options

        # 2. Get Next Step Recommendation
        next_step = self.engine.get_next_step()
        if next_step:
            options.append(MenuOption(
                id=f"exec:{next_step.id}",
                label=f"▶ EXECUTE NEXT: {next_step.name}",
                type="action",
                context={"contract": next_step}
            ))

        # 3. Global Actions
        options.append(MenuOption(id="status", label="Show Project Status", type="info"))
        options.append(MenuOption(id="unknowns", label="Check for Unknowns", type="info"))
        
        return options
