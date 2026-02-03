"""
Deep Process Engine - Project Manager
Version: 1.0

Manages multiple projects with projects/{id}/ structure.
"""

import yaml
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field


@dataclass
class ProjectInfo:
    """Basic project information."""
    id: str
    name: str
    process_id: str
    created_at: str
    path: Path
    is_active: bool = False


class ProjectManager:
    """
    Manages multiple projects in projects/{id}/ structure.

    Structure:
    projects/
    ├── project-alpha/
    │   ├── .state/
    │   │   ├── process.yaml
    │   │   ├── phase.yaml
    │   │   ├── items.yaml
    │   │   ├── decisions.yaml
    │   │   ├── unknowns.yaml
    │   │   └── history.yaml
    │   └── artifacts/
    ├── project-beta/
    │   └── ...
    └── .active (file containing active project id)
    """

    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.projects_dir = root_path / "projects"
        self.active_file = self.projects_dir / ".active"

        # Ensure projects directory exists
        self.projects_dir.mkdir(parents=True, exist_ok=True)

    def list_projects(self) -> List[ProjectInfo]:
        """List all projects."""
        projects = []
        active_id = self._get_active_id()

        for item in self.projects_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                state_file = item / ".state" / "process.yaml"
                if state_file.exists():
                    try:
                        data = yaml.safe_load(state_file.read_text(encoding='utf-8'))
                        projects.append(ProjectInfo(
                            id=item.name,
                            name=data.get('project', {}).get('name', item.name),
                            process_id=data.get('process_id', 'unknown'),
                            created_at=data.get('project', {}).get('created_at', 'unknown'),
                            path=item,
                            is_active=(item.name == active_id)
                        ))
                    except Exception:
                        pass

        return sorted(projects, key=lambda p: p.created_at, reverse=True)

    def create_project(
        self,
        project_id: str,
        project_name: str,
        process_id: str,
        set_active: bool = True
    ) -> Optional[Path]:
        """
        Create a new project with initial state.

        Args:
            project_id: Unique identifier (used as folder name)
            project_name: Human-readable name
            process_id: Which process to use (e.g., 'deep-explore', 'bmm')
            set_active: Whether to make this the active project

        Returns:
            Path to the new project, or None if failed
        """
        # Sanitize project_id
        project_id = self._sanitize_id(project_id)
        project_path = self.projects_dir / project_id

        if project_path.exists():
            print(f"Project '{project_id}' already exists")
            return None

        try:
            # Create directory structure
            state_dir = project_path / ".state"
            artifacts_dir = project_path / "artifacts"

            state_dir.mkdir(parents=True)
            artifacts_dir.mkdir(parents=True)
            (artifacts_dir / "epics").mkdir()
            (artifacts_dir / "stories").mkdir()

            now = datetime.now().isoformat()

            # Create process.yaml
            process_state = {
                'process_id': process_id,
                'process_version': '1.0',
                'project': {
                    'id': project_id,
                    'name': project_name,
                    'created_at': now,
                },
                'integrations': {
                    'azure_devops': {'enabled': False},
                    'github': {'enabled': False},
                },
                'settings': {
                    'auto_verify_gate': True,
                    'require_confirmation': True,
                }
            }
            self._write_yaml(state_dir / "process.yaml", process_state)

            # Create phase.yaml
            phase_state = {
                'current_phase': None,  # Will be set when process starts
                'phase_started_at': None,
                'phase_progress': 0.0,
                'phases_history': [],
                'current_artifacts': [],
                'blocking_items': [],
            }
            self._write_yaml(state_dir / "phase.yaml", phase_state)

            # Create items.yaml
            items_state = {
                'sequences': {
                    'epic': 1,
                    'story': 1,
                    'task': 1,
                    'sprint': 1,
                },
                'epics': [],
                'stories': [],
                'sprints': [],
                'tasks': [],
            }
            self._write_yaml(state_dir / "items.yaml", items_state)

            # Create decisions.yaml
            decisions_state = {
                'sequences': {'decision': 1},
                'decisions': [],
            }
            self._write_yaml(state_dir / "decisions.yaml", decisions_state)

            # Create unknowns.yaml
            unknowns_state = {
                'sequences': {'unknown': 1},
                'unknowns': [],
            }
            self._write_yaml(state_dir / "unknowns.yaml", unknowns_state)

            # Create history.yaml
            history_state = {
                'entries': [{
                    'id': 1,
                    'action': 'project-created',
                    'at': now,
                    'details': {
                        'project_name': project_name,
                        'process_id': process_id,
                    }
                }]
            }
            self._write_yaml(state_dir / "history.yaml", history_state)

            # Set as active if requested
            if set_active:
                self.set_active(project_id)

            print(f"Created project: {project_name} ({project_id})")
            return project_path

        except Exception as e:
            print(f"Error creating project: {e}")
            # Cleanup on failure
            if project_path.exists():
                shutil.rmtree(project_path)
            return None

    def get_project(self, project_id: str) -> Optional[ProjectInfo]:
        """Get a specific project by ID."""
        project_path = self.projects_dir / project_id
        if not project_path.exists():
            return None

        state_file = project_path / ".state" / "process.yaml"
        if not state_file.exists():
            return None

        try:
            data = yaml.safe_load(state_file.read_text(encoding='utf-8'))
            return ProjectInfo(
                id=project_id,
                name=data.get('project', {}).get('name', project_id),
                process_id=data.get('process_id', 'unknown'),
                created_at=data.get('project', {}).get('created_at', 'unknown'),
                path=project_path,
                is_active=(project_id == self._get_active_id())
            )
        except Exception:
            return None

    def get_active_project(self) -> Optional[ProjectInfo]:
        """Get the currently active project."""
        active_id = self._get_active_id()
        if active_id:
            return self.get_project(active_id)
        return None

    def set_active(self, project_id: str) -> bool:
        """Set a project as active."""
        project_path = self.projects_dir / project_id
        if not project_path.exists():
            print(f"Project '{project_id}' not found")
            return False

        self.active_file.write_text(project_id, encoding='utf-8')
        print(f"Active project: {project_id}")
        return True

    def delete_project(self, project_id: str, confirm: bool = False) -> bool:
        """Delete a project (requires confirmation)."""
        if not confirm:
            print("Deletion requires confirm=True")
            return False

        project_path = self.projects_dir / project_id
        if not project_path.exists():
            print(f"Project '{project_id}' not found")
            return False

        # Clear active if this was active
        if self._get_active_id() == project_id:
            self.active_file.unlink(missing_ok=True)

        shutil.rmtree(project_path)
        print(f"Deleted project: {project_id}")
        return True

    def get_project_state_path(self, project_id: str = None) -> Optional[Path]:
        """Get the .state/ path for a project (active if not specified)."""
        if project_id is None:
            project_id = self._get_active_id()

        if project_id is None:
            return None

        state_path = self.projects_dir / project_id / ".state"
        return state_path if state_path.exists() else None

    def _get_active_id(self) -> Optional[str]:
        """Get the ID of the active project."""
        if self.active_file.exists():
            return self.active_file.read_text(encoding='utf-8').strip()
        return None

    def _sanitize_id(self, project_id: str) -> str:
        """Sanitize project ID for use as folder name."""
        # Replace spaces with hyphens, remove special chars
        sanitized = project_id.lower().replace(' ', '-')
        sanitized = ''.join(c for c in sanitized if c.isalnum() or c == '-')
        return sanitized

    def _write_yaml(self, path: Path, data: Dict[str, Any]):
        """Write data to YAML file."""
        path.write_text(
            yaml.dump(data, default_flow_style=False, allow_unicode=True),
            encoding='utf-8'
        )


# Convenience function for quick access
def get_project_manager(root_path: Path = None) -> ProjectManager:
    """Get a ProjectManager instance."""
    if root_path is None:
        root_path = Path.cwd()
    return ProjectManager(root_path)
