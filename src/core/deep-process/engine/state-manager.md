# Deep Process Engine — State Manager Instructions

> **Purpose:** Detailed procedures for LLM to maintain state integrity.
> **Format:** YAML.
> **Principle:** Read-Modify-Write (RMW).

---

## 1. TRANSACTION PROTOCOL

When updating any state file in `.state/`, follow this "transactional" approach:

1.  **READ:** Use `read_file` to get the current content of the file (e.g., `.state/items.yaml`).
2.  **PARSE:** Identify the section to change (e.g., `sequences` or `epics`).
3.  **MODIFY:** Perform the change in your internal memory.
    - If adding: Append to the list.
    - If updating: Find by ID and replace fields.
    - If incrementing: `new_value = old_value + 1`.
4.  **WRITE:** Use `write_file` to overwrite the file with the COMPLETE updated YAML.
5.  **VERIFY:** Read the file back (or trust the write success) and confirm the change is reflected.

---

## 2. FILE SCHEMAS

### 2.1 items.yaml (The Registry)
```yaml
sequences:
  epic: [last_number]
  story: [last_number]
  task: [last_number]
epics:
  - id: EPIC-001
    title: "..."
    status: "defined"
stories: [] # List of stories
```
**RULE:** When creating a new item, you MUST increment the sequence.

### 2.2 phase.yaml (The Pointer)
```yaml
current_phase: [phase_id]
phase_progress: [0.0 - 1.0]
blocking_items: [] # List of BLK-XXX IDs
last_action:
  name: "step_id"
  at: "timestamp"
  result: "success"
```

### 2.3 history.yaml (The Audit)
Append a new entry for every successful action:
```yaml
entries:
  - id: [auto_increment]
    action: "create-epic"
    at: "2026-02-03T..."
    details:
      item_id: "EPIC-005"
```

---

## 3. REFERENTIAL INTEGRITY CHECKS

Before finalizing a state update, verify:
1.  **Unique IDs:** No duplicate IDs in the same file.
2.  **Parent Links:** If a Story references `EPIC-001`, does `EPIC-001` exist in the `epics` list?
3.  **File Existence:** If an item references an artifact path, does that file exist on disk?

---

## 4. HANDLING CONFLICTS

If you detect that the state is inconsistent (e.g., a story exists in `items.yaml` but its file is missing):
1.  **Do not ignore.**
2.  **Alert the user:** "State Inconsistency Detected: STORY-005 is in registry but file is missing."
3.  **Offer repair:** "Should I remove it from registry or attempt to recreate the file?"

---

## 5. TIMESTAMP FORMAT

Always use ISO 8601 format for timestamps: `YYYY-MM-DDTHH:MM:SSZ`.
Example: `2026-02-03T14:30:00Z`