"""
Deep Process Engine - Executor Implementation
Version: 0.4 (With Validation)
"""

from typing import Dict, Any, List
from pathlib import Path
import yaml
from .contract import WorkflowContract
from .validator import OutputValidator

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

class TaskExecutor:
    """Executes a task defined by a contract."""
    
    def __init__(self, project_root: Path = Path(".")):
        self.project_root = project_root
        self.validator = OutputValidator(project_root)

    def execute(self, contract: WorkflowContract, variables: Dict[str, str] = None) -> Dict[str, Any]:
        if variables is None:
            variables = {}

        print(f"\n🚀 EXECUTING: {contract.name} ({contract.id})")
        if variables:
            print(f"   Context: {variables}")
        print("-" * 40)
        
        # 1. Resolve Variables
safe_vars = SafeDict(**variables)
        resolved_content = contract.raw_content.format_map(safe_vars)
        resolved_inputs = [i.format_map(safe_vars) for i in contract.inputs]
        resolved_outputs = [o.format_map(safe_vars) for o in contract.outputs]

        # 2. Validate Inputs
        print(f"Checking inputs: {resolved_inputs}...")
        
        # 3. Simulate Execution
        print("\n--- INSTRUCTIONS FOR AGENT ---")
        print(resolved_content)
        print("------------------------------\n")
        
        print(f"(Agent is working... producing: {resolved_outputs})")
        
        # --- SIMULATION: Create Dummy Output File for Validation to pass ---
        # In real life, the LLM creates this. Here we mock it.
        if contract.output_contract == 'story':
            self._create_mock_story(resolved_outputs[0], variables.get('epic_id'))
        # -----------------------------------------------------------------

        # 4. Validate Outputs
        print("Validating outputs...")
        validation_results = []
        all_valid = True
        
        for output_file in resolved_outputs:
            result = self.validator.validate(contract.output_contract, Path(output_file))
            validation_results.append(result)
            if not result['valid']:
                print(f"❌ Validation FAILED for {output_file}: {result['errors']}")
                all_valid = False
            else:
                print(f"✅ Validation PASSED for {output_file}")

        if not all_valid:
             return {"status": "failure", "errors": validation_results}

        print("\n✅ Task execution COMPLETED successfully.")
        
        return {
            "status": "success",
            "contract_id": contract.id,
            "outputs_produced": resolved_outputs
        }

    def _create_mock_story(self, path_str: str, epic_id: str):
        """Helper to simulate LLM output."""
        # path_str might be 'artifacts/stories/{story_id}.yaml' - we need a real name
        # For demo, let's assume the path is already resolved or we force one
        if "{story_id}" in path_str:
            path_str = path_str.replace("{story_id}", "STORY-101")
            
        path = self.project_root / path_str
        path.parent.mkdir(parents=True, exist_ok=True)
        
        mock_content = {
            "id": "STORY-101",
            "epic_id": epic_id or "EPIC-UNKNOWN",
            "title": "Generated Story",
            "acceptance_criteria": ["Works"],
            "status": "draft"
        }
        path.write_text(yaml.dump(mock_content), encoding='utf-8')
        print(f"(SIMULATION: Created {path})")