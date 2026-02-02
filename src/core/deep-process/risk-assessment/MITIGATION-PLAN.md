# Deep Process Engine — Mitigation Implementation Plan
> **Version:** 1.0
> **Created:** 2026-02-02
> **Based on:** Deep Risk Assessment v1.0

---

## Executive Summary

This plan addresses **18 CRITICAL-tier risks** and **4 NON_ERGODIC risks** through **39 mitigations** organized into three priority waves.

| Priority | Risks Addressed | Mitigations | Focus |
|----------|-----------------|-------------|-------|
| P0 — Immediate | 4 NON_ERGODIC | M1-M9 | Survival |
| P1 — High | 6 CRITICAL | M10-M18 | Core stability |
| P2 — Medium | 8 HIGH | M19-M39 | Robustness |

---

## P0 — IMMEDIATE PRIORITY (NON_ERGODIC Risks)

> **Rationale:** These risks are potentially "game over" if they materialize.
> Standard cost-benefit analysis does not apply — survival must be ensured first.

### M7: Auto-Backup Before Every State Modification

| Attribute | Value |
|-----------|-------|
| **Addresses** | R115 State Corruption No Backup |
| **Risk Score** | 75 → 15 (80% reduction) |
| **Type** | Prevent + Recover |

**Implementation:**
```python
# In state-manager operations

def save_state(self, state: Dict[str, Any]):
    """Saves state with automatic backup."""
    # 1. Create backup before any modification
    backup_dir = self.state_dir / "backups"
    backup_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    backup_path = backup_dir / f"backup_{timestamp}"
    backup_path.mkdir()

    # 2. Copy all current state files
    for state_file in self.state_dir.glob("*.yaml"):
        shutil.copy2(state_file, backup_path / state_file.name)

    # 3. Write metadata
    (backup_path / "meta.yaml").write_text(yaml.dump({
        "created_at": timestamp,
        "reason": "auto_backup_before_modification",
        "files": [f.name for f in self.state_dir.glob("*.yaml")]
    }))

    # 4. Now perform the actual write
    self._write_state_files(state)

    # 5. Prune old backups (keep last 100 or 30 days)
    self._prune_backups(max_count=100, max_age_days=30)
```

**Files to Modify:**
- `engine/core.py` — Add backup logic to `_save_state()`
- Create `engine/backup_manager.py` — Backup utilities

**Acceptance Criteria:**
- [ ] Backup created before every state modification
- [ ] Backup includes all .state/*.yaml files
- [ ] Backup metadata includes timestamp and reason
- [ ] Old backups automatically pruned
- [ ] Recovery tested from backup

---

### M8: Integrity Checksums for All State Files

| Attribute | Value |
|-----------|-------|
| **Addresses** | R115 State Corruption |
| **Risk Score** | Part of R115 mitigation |
| **Type** | Detect |

**Implementation:**
```python
# Add to state files: checksum validation

import hashlib

def compute_checksum(file_path: Path) -> str:
    """Compute SHA-256 checksum of file."""
    return hashlib.sha256(file_path.read_bytes()).hexdigest()

def validate_state_integrity(state_dir: Path) -> Dict[str, Any]:
    """Validate all state files against stored checksums."""
    checksum_file = state_dir / "checksums.yaml"

    if not checksum_file.exists():
        return {"valid": True, "message": "No checksums yet"}

    stored = yaml.safe_load(checksum_file.read_text())
    errors = []

    for filename, expected_hash in stored.items():
        file_path = state_dir / filename
        if not file_path.exists():
            errors.append(f"Missing: {filename}")
            continue

        actual_hash = compute_checksum(file_path)
        if actual_hash != expected_hash:
            errors.append(f"Corrupted: {filename}")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }

def update_checksums(state_dir: Path):
    """Update checksum file after state modification."""
    checksums = {}
    for state_file in state_dir.glob("*.yaml"):
        if state_file.name != "checksums.yaml":
            checksums[state_file.name] = compute_checksum(state_file)

    (state_dir / "checksums.yaml").write_text(yaml.dump(checksums))
```

**Files to Modify:**
- `engine/core.py` — Add checksum validation on load
- `engine/core.py` — Update checksums after save

**Acceptance Criteria:**
- [ ] Checksums computed for all state files
- [ ] Validation runs on every state load
- [ ] Checksum mismatch raises clear error
- [ ] Checksums updated after successful writes

---

### M4-M6: Verification Checkpoints for LLM Output

| Attribute | Value |
|-----------|-------|
| **Addresses** | R114 LLM Hallucination No Safeguard |
| **Risk Score** | 100 → 40 (60% reduction) |
| **Type** | Detect |

**Implementation:**

```python
# M4: Verification checkpoints after critical operations

class VerificationCheckpoint:
    """Verification checkpoint for LLM-generated content."""

    CRITICAL_OPERATIONS = [
        "create_epic",
        "create_story",
        "pass_gate",
        "change_phase",
        "make_decision"
    ]

    @classmethod
    def verify(cls, operation: str, content: Dict, context: Dict) -> Dict:
        """Run verification checks on operation output."""
        if operation not in cls.CRITICAL_OPERATIONS:
            return {"verified": True, "checks": []}

        checks = []

        # Check 1: Required fields present
        required = cls._get_required_fields(operation)
        for field in required:
            if field not in content:
                checks.append({
                    "check": "required_field",
                    "field": field,
                    "passed": False,
                    "message": f"Missing required field: {field}"
                })

        # Check 2: References valid
        refs = cls._extract_references(content)
        for ref_type, ref_id in refs:
            if not cls._reference_exists(ref_type, ref_id, context):
                checks.append({
                    "check": "reference_valid",
                    "ref": f"{ref_type}:{ref_id}",
                    "passed": False,
                    "message": f"Reference not found: {ref_id}"
                })

        # Check 3: Consistency with existing state
        inconsistencies = cls._check_consistency(content, context)
        for inc in inconsistencies:
            checks.append({
                "check": "consistency",
                "passed": False,
                "message": inc
            })

        all_passed = all(c.get("passed", True) for c in checks)

        return {
            "verified": all_passed,
            "checks": checks,
            "requires_confirmation": not all_passed
        }
```

```python
# M5: User confirmation gates

class UserConfirmationGate:
    """Requires user confirmation for high-impact operations."""

    def request_confirmation(self, operation: str, summary: str) -> bool:
        """Present operation summary and request confirmation."""
        print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  VERIFICATION REQUIRED                                         ║
╠═══════════════════════════════════════════════════════════════╣
║  Operation: {operation:<50}║
║  Summary: {summary:<52}║
║                                                                ║
║  Please verify this is correct before proceeding.             ║
║                                                                ║
║  [Y] Confirm and proceed                                       ║
║  [N] Cancel and revise                                         ║
║  [D] Show details                                              ║
╚═══════════════════════════════════════════════════════════════╝
        """)
        # In CLI implementation, this would await user input
        return True  # Placeholder
```

```python
# M6: Fact-checking prompts

FACT_CHECK_PROMPT = """
Before finalizing this output, verify:

1. REFERENCES: All IDs mentioned (EPIC-XXX, STORY-XXX) actually exist
2. CONSISTENCY: This doesn't contradict earlier decisions in .state/decisions.yaml
3. COMPLETENESS: All required fields are filled with meaningful content
4. ACCURACY: Any facts mentioned are from the provided context, not assumed

If any verification fails, explicitly note the issue.
"""
```

**Files to Modify:**
- Create `engine/verification.py` — Verification checkpoints
- `engine/executor_impl.py` — Add verification after operations
- `engine/enforcer.md` — Add verification rules

**Acceptance Criteria:**
- [ ] Verification runs after all critical operations
- [ ] Verification failures clearly reported
- [ ] User confirmation required for flagged outputs
- [ ] Fact-checking prompt included in critical operations

---

### M1-M3: Provider Abstraction Layer

| Attribute | Value |
|-----------|-------|
| **Addresses** | R152 LLM Provider Dependency |
| **Risk Score** | 125 → 50 (60% reduction) |
| **Type** | Prevent (diversify) |

**Implementation:**

```python
# M1: Provider abstraction interface

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class LLMProvider(ABC):
    """Abstract interface for LLM providers."""

    @abstractmethod
    def complete(self, prompt: str, **kwargs) -> str:
        """Generate completion for prompt."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if provider is currently available."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Return provider name."""
        pass

class ClaudeProvider(LLMProvider):
    """Claude/Anthropic provider implementation."""

    def complete(self, prompt: str, **kwargs) -> str:
        # Implementation for Claude API
        pass

    def is_available(self) -> bool:
        # Health check
        pass

    def get_name(self) -> str:
        return "claude"

class ProviderManager:
    """Manages multiple LLM providers with fallback."""

    def __init__(self):
        self.providers: List[LLMProvider] = []
        self.primary: Optional[LLMProvider] = None

    def register(self, provider: LLMProvider, primary: bool = False):
        """Register a provider."""
        self.providers.append(provider)
        if primary:
            self.primary = provider

    def get_available(self) -> Optional[LLMProvider]:
        """Get first available provider, preferring primary."""
        if self.primary and self.primary.is_available():
            return self.primary

        for provider in self.providers:
            if provider.is_available():
                return provider

        return None
```

```python
# M2: Offline mode for state

class OfflineMode:
    """Allows state viewing and basic operations without LLM."""

    OFFLINE_OPERATIONS = [
        "view_state",
        "view_items",
        "view_history",
        "backup_state",
        "restore_state",
        "export_artifacts"
    ]

    def is_allowed(self, operation: str) -> bool:
        """Check if operation is allowed in offline mode."""
        return operation in self.OFFLINE_OPERATIONS

    def execute(self, operation: str, *args, **kwargs):
        """Execute offline-safe operation."""
        if not self.is_allowed(operation):
            raise OfflineModeError(
                f"Operation '{operation}' requires LLM. "
                f"Available offline: {self.OFFLINE_OPERATIONS}"
            )
        # Execute read-only operation
```

**Files to Modify:**
- Create `engine/providers/` — Provider abstraction
- Create `engine/providers/base.py` — Abstract interface
- Create `engine/providers/claude.py` — Claude implementation
- Create `engine/offline.py` — Offline mode

**Acceptance Criteria:**
- [ ] Provider interface defined
- [ ] Claude provider implemented
- [ ] Provider health checks work
- [ ] Offline mode allows state viewing
- [ ] Clear error when no provider available

---

## P1 — HIGH PRIORITY (CRITICAL Tier Risks)

### M10-M11: Concurrent Access Protection

| Attribute | Value |
|-----------|-------|
| **Addresses** | R125 No Concurrent Access Protection |
| **Risk Score** | 80 → 20 (75% reduction) |
| **Type** | Prevent |

**Implementation:**

```python
# M10: File locking mechanism

import fcntl  # Unix
import msvcrt  # Windows
import os

class StateLock:
    """File-based locking for state directory."""

    def __init__(self, state_dir: Path):
        self.lock_file = state_dir / ".lock"
        self.lock_handle = None

    def acquire(self, timeout: int = 30) -> bool:
        """Acquire exclusive lock on state directory."""
        self.lock_handle = open(self.lock_file, 'w')

        try:
            if os.name == 'nt':  # Windows
                msvcrt.locking(self.lock_handle.fileno(),
                              msvcrt.LK_NBLCK, 1)
            else:  # Unix
                fcntl.flock(self.lock_handle.fileno(),
                           fcntl.LOCK_EX | fcntl.LOCK_NB)

            # Write session info to lock file
            self.lock_handle.write(f"session_id: {os.getpid()}\n")
            self.lock_handle.write(f"acquired: {datetime.now().isoformat()}\n")
            self.lock_handle.flush()
            return True

        except (IOError, OSError):
            # Lock held by another process
            self.lock_handle.close()
            return False

    def release(self):
        """Release lock."""
        if self.lock_handle:
            try:
                if os.name == 'nt':
                    msvcrt.locking(self.lock_handle.fileno(),
                                  msvcrt.LK_UNLCK, 1)
                else:
                    fcntl.flock(self.lock_handle.fileno(),
                               fcntl.LOCK_UN)
            finally:
                self.lock_handle.close()
                self.lock_file.unlink(missing_ok=True)
```

```python
# M11: Multi-session warning

def check_existing_session(state_dir: Path) -> Optional[Dict]:
    """Check if another session is active."""
    lock_file = state_dir / ".lock"

    if lock_file.exists():
        content = lock_file.read_text()
        return yaml.safe_load(content)

    return None

def warn_concurrent_session(session_info: Dict):
    """Warn user about concurrent session."""
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  ⚠️  WARNING: ANOTHER SESSION MAY BE ACTIVE                   ║
╠═══════════════════════════════════════════════════════════════╣
║  Session ID: {session_info.get('session_id', 'unknown'):<46}║
║  Started: {session_info.get('acquired', 'unknown'):<49}║
║                                                                ║
║  Running multiple sessions on the same project may cause      ║
║  data corruption. Please close other sessions first.          ║
║                                                                ║
║  [F] Force continue (DANGEROUS)                                ║
║  [Q] Quit and use other session                                ║
╚═══════════════════════════════════════════════════════════════╝
    """)
```

**Files to Modify:**
- Create `engine/locking.py` — Lock management
- `engine/core.py` — Acquire lock on init, release on exit

**Acceptance Criteria:**
- [ ] Lock acquired when session starts
- [ ] Lock released when session ends
- [ ] Clear warning if lock held by another session
- [ ] Force option with explicit acknowledgment

---

### M12-M13: Referential Integrity Validation

| Attribute | Value |
|-----------|-------|
| **Addresses** | R124 Referential Integrity Not Enforced |
| **Risk Score** | 80 → 16 (80% reduction) |
| **Type** | Detect |

**Implementation:**

```python
# M12: Validate references on load

class ReferenceValidator:
    """Validates referential integrity of state."""

    REFERENCE_MAPPINGS = {
        "story.epic_id": "epics",
        "story.sprint_id": "sprints",
        "story.blocked_by": "decisions",
        "blocker.ref": ["decisions", "unknowns"],
    }

    def validate(self, state: Dict) -> Dict:
        """Validate all references in state."""
        errors = []
        warnings = []

        # Check story references
        for story in state.get("items", {}).get("stories", []):
            epic_id = story.get("epic_id")
            if epic_id:
                epic_exists = any(
                    e["id"] == epic_id
                    for e in state.get("items", {}).get("epics", [])
                )
                if not epic_exists:
                    errors.append(
                        f"Story {story['id']} references non-existent epic {epic_id}"
                    )

        # Check artifact file references
        for artifact_path in state.get("phase", {}).get("current_artifacts", []):
            if not Path(artifact_path).exists():
                warnings.append(
                    f"Artifact file missing: {artifact_path}"
                )

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
```

**Files to Modify:**
- Create `engine/integrity.py` — Reference validation
- `engine/core.py` — Run validation on load_state()

**Acceptance Criteria:**
- [ ] All reference types validated
- [ ] Clear error messages for broken references
- [ ] Warnings for missing artifact files
- [ ] Validation runs on every state load

---

### M14-M15: Single Schema Source

| Attribute | Value |
|-----------|-------|
| **Addresses** | R091 Schema Drift |
| **Risk Score** | 80 → 12 (85% reduction) |
| **Type** | Prevent |

**Implementation:**

```python
# M14: Load schemas from YAML files, not hardcode

class SchemaLoader:
    """Loads schemas from YAML files."""

    def __init__(self, schema_dir: Path):
        self.schema_dir = schema_dir
        self._cache = {}

    def get_schema(self, name: str) -> Dict:
        """Load schema from YAML file."""
        if name not in self._cache:
            schema_path = self.schema_dir / f"{name}.schema.yaml"
            if not schema_path.exists():
                raise SchemaNotFoundError(f"Schema not found: {name}")

            self._cache[name] = yaml.safe_load(schema_path.read_text())

        return self._cache[name]

    def get_required_fields(self, name: str) -> List[str]:
        """Extract required fields from schema."""
        schema = self.get_schema(name)
        return schema.get("required", [])
```

```python
# M15: Schema validation in CI

# tests/test_schemas.py

def test_validator_uses_yaml_schemas():
    """Ensure validator uses YAML schema files, not hardcoded."""
    loader = SchemaLoader(Path("schemas"))
    validator = OutputValidator(Path("."))

    for schema_name in ["epic", "story", "sprint"]:
        yaml_required = set(loader.get_required_fields(schema_name))
        validator_required = set(validator._get_required_fields(schema_name))

        assert yaml_required == validator_required, \
            f"Schema mismatch for {schema_name}: " \
            f"YAML has {yaml_required}, validator has {validator_required}"
```

**Files to Modify:**
- Create `engine/schema_loader.py` — Schema loader
- `engine/validator.py` — Use SchemaLoader instead of hardcoded
- Create `tests/test_schemas.py` — Schema validation tests

**Acceptance Criteria:**
- [ ] Validator loads schemas from YAML files
- [ ] No hardcoded schema definitions
- [ ] Test ensures YAML and validator match
- [ ] CI fails if schemas diverge

---

## P2 — MEDIUM PRIORITY (HIGH Tier Risks)

### M16-M18: Override Controls

| Addresses | R077 USER_OVERRIDE Abuse |
|-----------|--------------------------|
| **Risk Score** | 80 → 24 (70% reduction) |

**Implementation Summary:**
- M16: Log all overrides to `.state/overrides.yaml`
- M17: Limit overrides to 5/day per project
- M18: Require text justification for each override

---

### M19-M20: Session Context Enhancement

| Addresses | R094 Session Context Loss |
|-----------|---------------------------|
| **Risk Score** | 75 → 30 (60% reduction) |

**Implementation Summary:**
- M19: Save reasoning context to `.state/context.yaml`
- M20: Generate resumption summary on session start

---

### M21-M22: Drift Detection

| Addresses | R017 State Drift Accumulation |
|-----------|-------------------------------|
| **Risk Score** | 75 → 20 (73% reduction) |

**Implementation Summary:**
- M21: Periodic integrity scan (configurable interval)
- M22: Alert when drift metrics exceed threshold

---

### M23: Transactional State Updates

| Addresses | R005 State File Coupling |
|-----------|--------------------------|
| **Risk Score** | 64 → 16 (75% reduction) |

**Implementation Summary:**
- Write to temp files first
- Atomic rename after all writes succeed
- Rollback on any failure

---

### M24-M25: Enforcer Hardening

| Addresses | R006 Enforcer Bypass Cascade |
|-----------|------------------------------|
| **Risk Score** | 60 → 20 (67% reduction) |

**Implementation Summary:**
- M24: Hash enforcer.md content, verify before execution
- M25: Test suite for critical enforcement rules

---

### M26-M28: Prompt Injection Defense

| Addresses | R033 Prompt Injection |
|-----------|----------------------|
| **Risk Score** | 60 → 24 (60% reduction) |

**Implementation Summary:**
- M26: Sanitize artifact content before including in prompts
- M27: Separate artifact context from instruction context
- M28: Blocklist known injection patterns

---

### M29-M30: Rule Conflict Detection

| Addresses | R092 Rule Interpretation Conflicts |
|-----------|-------------------------------------|
| **Risk Score** | 60 → 15 (75% reduction) |

**Implementation Summary:**
- M29: Add priority field to rules in enforcer.md
- M30: Static analysis tool to detect conflicting rules

---

### M31-M32: Error Logging

| Addresses | R127 Silent Contract Parsing |
|-----------|------------------------------|
| **Risk Score** | 60 → 12 (80% reduction) |

**Implementation Summary:**
- M31: Explicit logging for all parsing failures
- M32: Test edge cases for frontmatter parsing

---

### M33-M34: Integration Reconciliation

| Addresses | R095 Integration Conflict |
|-----------|--------------------------|
| **Risk Score** | 60 → 20 (67% reduction) |

**Implementation Summary:**
- M33: Detect conflicts before sync
- M34: Generate reconciliation report

---

### M35-M36: History Management

| Addresses | R128 History Unbounded Growth |
|-----------|------------------------------|
| **Risk Score** | 60 → 15 (75% reduction) |

**Implementation Summary:**
- M35: Archive history older than 30 days
- M36: Track context utilization, warn at 80%

---

### M37-M38: Test Coverage

| Addresses | R140 No Regression Tests |
|-----------|--------------------------|
| **Risk Score** | 60 → 15 (75% reduction) |

**Implementation Summary:**
- M37: Core functionality test suite
- M38: CI/CD pipeline with test gate

---

### M39: Multi-Provider Support

| Addresses | R046 Provider Shutdown |
|-----------|------------------------|
| **Risk Score** | 50 → 25 (50% reduction) |

**Implementation Summary:**
- Build on M1 provider abstraction
- Allow user to configure backup providers

---

## Implementation Schedule

```
Week 1-2: P0 Priority (NON_ERGODIC)
├── M7: Auto-backup
├── M8: Integrity checksums
├── M4-M6: Verification checkpoints
└── M1-M3: Provider abstraction (foundation)

Week 3-4: P1 Priority (CRITICAL)
├── M10-M11: Concurrent access protection
├── M12-M13: Referential integrity
└── M14-M15: Schema unification

Week 5-6: P2 Priority (HIGH)
├── M16-M18: Override controls
├── M21-M22: Drift detection
├── M24-M25: Enforcer hardening
└── M31-M32: Error logging

Week 7-8: P2 Continued
├── M23: Transactional updates
├── M26-M28: Prompt injection defense
├── M33-M34: Integration reconciliation
└── M35-M38: History management + tests
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| NON_ERGODIC residual | 0 unmitigated | Count of unmitigated NON_ERGODIC risks |
| CRITICAL coverage | 100% | % of CRITICAL risks with active mitigation |
| Silent failure rate | 0 | Count of failures without error messages |
| Backup success rate | 100% | % of operations with successful backup |
| Test coverage | >80% | Code coverage of core modules |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial plan |

