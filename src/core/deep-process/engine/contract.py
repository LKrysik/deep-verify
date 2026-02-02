"""
Deep Process Engine - Contract Parser
Version: 0.1
"""

import yaml
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass
class WorkflowContract:
    id: str
    name: Optional[str] = None
    type: str = "step"  # step, gate, process
    context_menu: Optional[str] = None  # NEW: Trigger for dynamic menu
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    output_contract: Optional[str] = None
    next_success: Optional[str] = None
    next_failure: Optional[str] = None
    status: str = "pending"
    file_path: Optional[Path] = None
    raw_content: Optional[str] = None  # The markdown content instructions

class ContractParser:
    """Parses YAML frontmatter from markdown files."""

    # Regex to capture YAML frontmatter between --- lines
    FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

    @staticmethod
    def parse(file_path: Path) -> Optional[WorkflowContract]:
        try:
            content = file_path.read_text(encoding='utf-8')
            match = ContractParser.FRONTMATTER_PATTERN.match(content)
            
            if not match:
                return None

            yaml_content = match.group(1)
            data = yaml.safe_load(yaml_content)
            
            if not isinstance(data, dict) or 'id' not in data:
                return None

            # Handle 'next' field structure
            next_data = data.get('next', {})
            if isinstance(next_data, str):
                # Handle legacy/simple format if any
                next_success = next_data
                next_failure = None
            else:
                next_success = next_data.get('success')
                next_failure = next_data.get('failure')

            return WorkflowContract(
                id=data['id'],
                name=data.get('name'),
                type=data.get('type', 'step'),
                context_menu=data.get('context_menu'), # NEW
                inputs=data.get('inputs', []),
                outputs=data.get('outputs', []),
                output_contract=data.get('output_contract'),
                next_success=next_success,
                next_failure=next_failure,
                status=data.get('status', 'pending'),
                file_path=file_path,
                raw_content=content[match.end():] # Everything after frontmatter
            )

        except Exception as e:
            print(f"Error parsing contract from {file_path}: {e}")
            return None
