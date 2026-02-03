# Step 01: SENSE Phase

## Purpose
Analyze current system state and present actionable status to Operator.

## Trigger
- System startup (after bootstrap)
- Explicit `pm` or `deep-process` command
- After any state change

## Execution

### Phase 1.1: Load State

```
📂 Loading .deep-process/state.json
📂 Loading .deep-process/registry.json
```

Read and parse:
- All nodes and their statuses
- All edges (dependencies)
- Current saga (if active)
- Active processes

### Phase 1.2: Scan for Issues

Query the graph for issues:

```markdown
## Issue Detection

### STALE Nodes (require update)
{for each node where dp_status = "STALE"}
  - {node.dp_id}: {node.path}
    Reason: Parent {changed_parent} modified at {timestamp}
{end}

### BLOCKED Nodes (cannot proceed)
{for each node where dp_status = "BLOCKED"}
  - {node.dp_id}: Blocked by {blocker_id}
{end}

### AWAITING_USER_INPUT (Decision Points)
{for each node where dp_status = "AWAITING_USER_INPUT"}
  - {node.dp_id}: {node.question.prompt}
{end}

### FAILED Nodes (validation failed)
{for each node where dp_status = "FAILED"}
  - {node.dp_id}: Failed at {timestamp}
{end}
```

### Phase 1.3: Build Topology Summary

Compute graph metrics:

```markdown
## Topology Summary

| Metric | Value |
|--------|-------|
| Total nodes | {count} |
| COMMITTED | {count} |
| STALE | {count} |
| BLOCKED | {count} |
| NOW (in progress) | {count} |
| Decision Points pending | {count} |
| Max depth | {depth} |
| Orphan nodes | {count} |
```

### Phase 1.4: Display Status Menu

Present to Operator:

```
═══════════════════════════════════════════════════════════════
  DEEP-PROCESS v3.6 — Semantic Reality Engine
═══════════════════════════════════════════════════════════════

Active Process: {process_name} ({process_id})

Status Summary:
  ✅ COMMITTED: {count}
  🔄 STALE: {count}
  🚫 BLOCKED: {count}
  ⏳ AWAITING INPUT: {count}
  ❌ FAILED: {count}

{if STALE > 0}
⚠️  {STALE} artifacts need update due to parent changes.
{end}

{if AWAITING_USER_INPUT > 0}
🔔 {count} decisions require your input.
{end}

{if FAILED > 0}
❌ {count} artifacts failed validation - review required.
{end}

Available Actions:
[1] Update STALE artifacts
[2] Review Decision Points
[3] View FAILED artifacts
[4] New artifact
[5] Switch process
[A] Run full audit
[Q] Quit

Enter choice:
```

## Decision Logic

### If STALE nodes exist:
- Prioritize by dependency order (leaves first)
- Offer bulk update or selective update

### If Decision Points exist:
- Show in order of blocking impact
- Most blockers first

### If FAILED nodes exist:
- Show failure reasons
- Offer to return to NOW for revision

## State Update

SENSE phase is read-only. No state update unless user takes action.

## Output

The SENSE phase produces:
1. **Status display** for Operator
2. **Issue list** prioritized by severity
3. **Recommended actions** based on state

## Next Steps

Based on Operator choice:
- **Update STALE** → Step 02: PLAN
- **Decision Points** → Present DP, await input
- **New artifact** → Step 02: PLAN
- **Audit** → Invoke Validator Agent on full graph

## Example Output

```
═══════════════════════════════════════════════════════════════
  DEEP-PROCESS v3.6 — Semantic Reality Engine
═══════════════════════════════════════════════════════════════

Active Process: feature-auth (PROC-DEV-001)

Status Summary:
  ✅ COMMITTED: 5
  🔄 STALE: 2
  🚫 BLOCKED: 1
  ⏳ AWAITING INPUT: 1
  ❌ FAILED: 0

⚠️  2 artifacts need update:
    - EPIC-AUTH (depends on ARCH-001, modified 2h ago)
    - TASK-LOGIN (depends on EPIC-AUTH)

🔔 1 decision requires your input:
    - DP-003: OAuth vs SAML for enterprise SSO

Available Actions:
[1] Update STALE artifacts
[2] Review Decision Point DP-003
[4] New artifact
[A] Run full audit

Enter choice:
```
