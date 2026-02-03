# Step 05: SYNC Phase

## Purpose
Commit validated artifact to file system and update graph state.

## Trigger
- VALIDATE phase returned COMMITTED verdict
- VALIDATE phase returned CONDITIONAL and Operator approved

## Execution

### Phase 5.1: Operator Confirmation

Present final artifact to Operator:

```markdown
## Sync Confirmation

**Artifact:** {dp_id}
**Path:** {file_path}
**Verdict:** {COMMITTED / CONDITIONAL}

### Content Preview

```yaml
{YAML header}
```

{First 20 lines of content}
...

### Semantic Hash

{list of facts}

### Validation Summary

- Anti-bias: ✅
- Coherence: ✅
- Hash verification: ✅

{if CONDITIONAL}
**Warnings documented:**
- {warning_1}
- {warning_2}
{end}

**Write to file system?** [Y/n]
```

### Phase 5.2: File Write

Upon confirmation, write artifact:

```markdown
## File Write

Writing to: {file_path}

{if file exists}
  Creating backup: .deep-process/backups/{dp_id}_{timestamp}.md
  Backup created ✅
{end}

Writing artifact...
Write complete ✅

Verifying write...
Checksum: {hash}
Verification: ✅
```

### Phase 5.3: State Update

Update state.json with committed artifact:

```markdown
## State Update

### Node Update

```json
{
  "dp_id": "{dp_id}",
  "dp_status": "COMMITTED",
  "modified_at": "{timestamp}",
  "semantic_hash": [{facts}]
}
```

### Edge Verification

Checking declared dependencies exist:
{for each in depends_on}
  - {path}: ✅ exists
{end}

### Dependent Flagging

Finding nodes that depend on {dp_id}:
{for each dependent}
  - {dependent.dp_id}: Flagging as STALE
{end}
```

### Phase 5.4: Transaction Commit

Close the saga transaction:

```markdown
## Transaction Commit

```json
{
  "saga_id": "{saga_id}",
  "status": "COMMITTED",
  "started_at": "{start_time}",
  "completed_at": "{now}",
  "operations": [
    {"type": "CREATE/UPDATE", "target": "{dp_id}", "path": "{path}"}
  ]
}
```

Transaction logged ✅
```

### Phase 5.5: Propagation

Flag dependents as STALE:

```markdown
## Propagation

### Nodes depending on {dp_id}:

{for each dependent}
| Node | Dependency Type | New Status |
|------|-----------------|------------|
| {dep.dp_id} | {dep.type} | STALE |
{end}

Total flagged: {count}
```

## State Update Block

```
[UPDATE_STATE]
{
  "saga_id": "{saga_id}",
  "operations": [
    {
      "type": "COMMIT",
      "target": "{dp_id}",
      "path": "{file_path}",
      "backup_path": "{backup_path}"
    }
  ],
  "flag_stale": ["{dep_1}", "{dep_2}"]
}
[/UPDATE_STATE]
```

## Output

The SYNC phase produces:
1. **Written artifact** in file system
2. **Backup** of previous version (if update)
3. **Updated state.json** with new status
4. **STALE flags** on dependent nodes

## Completion Display

```
═══════════════════════════════════════════════════════════════
  SYNC COMPLETE
═══════════════════════════════════════════════════════════════

Artifact committed: {dp_id}
Path: {file_path}
Status: COMMITTED

{if dependents_flagged > 0}
⚠️  {count} dependent artifacts flagged as STALE:
{for each}
   - {dependent.dp_id}
{end}

Run [U] Update to refresh stale artifacts.
{end}

Transaction: {saga_id} COMMITTED

Returning to main menu...
```

## Error Handling

| Error | Cause | Recovery |
|-------|-------|----------|
| Write failed | Disk full / permissions | Retry or escalate |
| State update failed | Concurrent modification | Reload state, retry |
| Backup failed | Cannot create backup | Warn, allow proceed |

### Rollback Protocol

If SYNC fails after partial write:

```markdown
## Rollback Required

Error at: {error_point}

Rolling back:
1. Restore from backup: {backup_path}
2. Revert state.json to pre-SYNC
3. Clear STALE flags set during SYNC

Rollback complete. Artifact in previous state.

Returning to VALIDATE phase...
```

## Next Step

After successful SYNC:
- Return to **Step 01: SENSE** for next action
- System is ready for next operation

## Saga Pattern Compliance

The SYNC phase ensures:
1. **Atomicity:** All-or-nothing commit
2. **Backup:** Previous version preserved
3. **State consistency:** Graph updated atomically
4. **Propagation:** Dependents notified via STALE

If any step fails, the entire SYNC rolls back.
