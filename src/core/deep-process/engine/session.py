"""
Deep Process Engine - Session Manager
Version: 1.0

Manages the current working session within a project.
Handles state loading, updating, and persistence.
"""

import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass


@dataclass
class SessionContext:
    """Current session context."""
    project_id: str
    project_name: str
    process_id: str
    current_phase: Optional[str]
    phase_progress: float
    blocking_items: List[Dict]
    last_action: Optional[Dict]


class SessionManager:
    """
    Manages session state within a project.

    Provides:
    - State loading and caching
    - State updates with history tracking
    - Context for LLM execution
    """

    def __init__(self, state_dir: Path):
        self.state_dir = state_dir
        self._cache: Dict[str, Any] = {}
        self._dirty: set = set()

    @classmethod
    def from_project_path(cls, project_path: Path) -> 'SessionManager':
        """Create session from project path."""
        return cls(project_path / ".state")

    def load_context(self) -> Optional[SessionContext]:
        """Load current session context."""
        process = self.get_state('process')
        phase = self.get_state('phase')

        if not process:
            return None

        return SessionContext(
            project_id=process.get('project', {}).get('id', 'unknown'),
            project_name=process.get('project', {}).get('name', 'Unknown'),
            process_id=process.get('process_id', 'unknown'),
            current_phase=phase.get('current_phase') if phase else None,
            phase_progress=phase.get('phase_progress', 0.0) if phase else 0.0,
            blocking_items=phase.get('blocking_items', []) if phase else [],
            last_action=phase.get('last_action') if phase else None,
        )

    def get_state(self, state_type: str) -> Optional[Dict]:
        """
        Get state data by type.

        Args:
            state_type: One of 'process', 'phase', 'items', 'decisions', 'unknowns', 'history'
        """
        if state_type in self._cache:
            return self._cache[state_type]

        file_path = self.state_dir / f"{state_type}.yaml"
        if not file_path.exists():
            return None

        try:
            data = yaml.safe_load(file_path.read_text(encoding='utf-8'))
            self._cache[state_type] = data
            return data
        except Exception as e:
            print(f"Error loading {state_type}: {e}")
            return None

    def update_state(self, state_type: str, updates: Dict[str, Any], merge: bool = True):
        """
        Update state data.

        Args:
            state_type: Which state file to update
            updates: Data to update
            merge: If True, merge with existing; if False, replace
        """
        current = self.get_state(state_type) or {}

        if merge:
            self._deep_merge(current, updates)
        else:
            current = updates

        self._cache[state_type] = current
        self._dirty.add(state_type)

    def set_phase(self, phase_id: str, progress: float = 0.0):
        """Set current phase."""
        now = datetime.now().isoformat()

        phase_data = self.get_state('phase') or {}

        # Record previous phase if transitioning
        if phase_data.get('current_phase') and phase_data['current_phase'] != phase_id:
            history = phase_data.get('phases_history', [])
            history.append({
                'phase': phase_data['current_phase'],
                'status': 'completed',
                'started_at': phase_data.get('phase_started_at'),
                'completed_at': now,
            })
            phase_data['phases_history'] = history

        phase_data['current_phase'] = phase_id
        phase_data['phase_started_at'] = now
        phase_data['phase_progress'] = progress

        self._cache['phase'] = phase_data
        self._dirty.add('phase')

        self._add_history_entry('phase-changed', {'phase': phase_id})

    def update_progress(self, progress: float):
        """Update phase progress (0.0 - 1.0)."""
        phase_data = self.get_state('phase') or {}
        phase_data['phase_progress'] = min(1.0, max(0.0, progress))
        self._cache['phase'] = phase_data
        self._dirty.add('phase')

    def record_action(self, action_name: str, details: Dict = None):
        """Record an action in history."""
        now = datetime.now().isoformat()

        # Update last_action in phase
        phase_data = self.get_state('phase') or {}
        phase_data['last_action'] = {
            'name': action_name,
            'at': now,
            'result': 'success',
        }
        self._cache['phase'] = phase_data
        self._dirty.add('phase')

        # Add to history
        self._add_history_entry(action_name, details or {})

    def add_blocker(self, blocker_type: str, ref: str, title: str, blocks: List[str] = None):
        """Add a blocking item."""
        phase_data = self.get_state('phase') or {}
        blockers = phase_data.get('blocking_items', [])

        blocker_id = f"BLK-{len(blockers) + 1:03d}"
        blockers.append({
            'id': blocker_id,
            'type': blocker_type,
            'ref': ref,
            'title': title,
            'blocks': blocks or [],
            'created_at': datetime.now().isoformat(),
        })

        phase_data['blocking_items'] = blockers
        self._cache['phase'] = phase_data
        self._dirty.add('phase')

        return blocker_id

    def remove_blocker(self, blocker_id: str):
        """Remove a blocking item."""
        phase_data = self.get_state('phase') or {}
        blockers = phase_data.get('blocking_items', [])
        phase_data['blocking_items'] = [b for b in blockers if b['id'] != blocker_id]
        self._cache['phase'] = phase_data
        self._dirty.add('phase')

    def add_decision(self, title: str, decision: str, rationale: str, options: List[Dict] = None):
        """Record a decision."""
        decisions_data = self.get_state('decisions') or {'sequences': {'decision': 1}, 'decisions': []}

        dec_id = f"DEC-{decisions_data['sequences']['decision']:03d}"
        decisions_data['sequences']['decision'] += 1

        decisions_data['decisions'].append({
            'id': dec_id,
            'title': title,
            'status': 'accepted',
            'decision': decision,
            'rationale': rationale,
            'options_considered': options or [],
            'decided_at': datetime.now().isoformat(),
        })

        self._cache['decisions'] = decisions_data
        self._dirty.add('decisions')

        self._add_history_entry('decision-made', {'decision_id': dec_id, 'title': title})
        return dec_id

    def add_unknown(self, description: str, unknown_type: str = 'technical', priority: str = 'medium'):
        """Record an unknown."""
        unknowns_data = self.get_state('unknowns') or {'sequences': {'unknown': 1}, 'unknowns': []}

        unk_id = f"UNK-{unknowns_data['sequences']['unknown']:03d}"
        unknowns_data['sequences']['unknown'] += 1

        unknowns_data['unknowns'].append({
            'id': unk_id,
            'description': description,
            'type': unknown_type,
            'priority': priority,
            'status': 'discovered',
            'discovered_at': datetime.now().isoformat(),
        })

        self._cache['unknowns'] = unknowns_data
        self._dirty.add('unknowns')

        self._add_history_entry('unknown-discovered', {'unknown_id': unk_id})
        return unk_id

    def save(self):
        """Persist all dirty state to disk."""
        for state_type in self._dirty:
            if state_type in self._cache:
                file_path = self.state_dir / f"{state_type}.yaml"
                file_path.write_text(
                    yaml.dump(self._cache[state_type], default_flow_style=False, allow_unicode=True),
                    encoding='utf-8'
                )
        self._dirty.clear()

    def _add_history_entry(self, action: str, details: Dict):
        """Add entry to history."""
        history_data = self.get_state('history') or {'entries': []}
        entries = history_data.get('entries', [])

        new_id = max([e.get('id', 0) for e in entries], default=0) + 1
        entries.append({
            'id': new_id,
            'action': action,
            'at': datetime.now().isoformat(),
            'details': details,
        })

        history_data['entries'] = entries
        self._cache['history'] = history_data
        self._dirty.add('history')

    def _deep_merge(self, base: Dict, updates: Dict):
        """Deep merge updates into base dict."""
        for key, value in updates.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value
