# Step 00: Bootstrap Protocol

## Purpose
Initialize Deep-Process v3.6 system in a new project directory.

## Prerequisites
- Empty or existing project directory
- LLM CLI available (Claude, Gemini, or compatible)

## Execution

### Phase 1: Directory Structure Creation

Create the system kernel:

```
📁 Create .deep-process/
   ├── state.json          # Initialize with `data/state-schema.yaml`
   ├── registry.json       # Initialize with `data/registry-schema.yaml`
   ├── enforcer.md         # Copy from `data/enforcer.md`
   ├── backups/            # Create empty directory
   ├── agents/             # Copy from `agents/`
   │   ├── pm-agent.yaml
   │   ├── validator-agent.yaml
   │   └── implementation-agent.yaml
   └── processes/          # Create empty directory

📁 Create artifacts/
   └── (initially empty, will hold output)

📁 Create .claude/commands/ (or .gemini/commands/)
   ├── deep-process.json   # CLI shim
   └── audit.json          # CLI shim
```

### Phase 2: State Initialization

Initialize `.deep-process/state.json`:

```json
{
  "version": "3.6",
  "initialized_at": "{ISO_TIMESTAMP}",
  "last_modified": "{ISO_TIMESTAMP}",
  "current_saga": null,
  "nodes": {},
  "edges": [],
  "transactions": []
}
```

Initialize `.deep-process/registry.json`:

```json
{
  "version": "3.6",
  "processes": [],
  "active_process": null
}
```

### Phase 3: Load BIOS (Enforcer)

Copy enforcer content to `.deep-process/enforcer.md`:
- Method Translator definitions
- Invariant Laws
- Response Protocol

### Phase 4: Verification

Verify initialization:

```markdown
## Bootstrap Verification Checklist

[ ] .deep-process/state.json exists and is valid JSON
[ ] .deep-process/registry.json exists and is valid JSON
[ ] .deep-process/enforcer.md exists
[ ] .deep-process/agents/ contains all 3 agent files
[ ] artifacts/ directory exists
[ ] CLI shims created (if applicable)
```

### Phase 5: Display Main Menu

After successful bootstrap, display:

```
═══════════════════════════════════════════════════════════════
  DEEP-PROCESS v3.6 — Semantic Reality Engine
  Status: INITIALIZED
═══════════════════════════════════════════════════════════════

System ready. No active processes.

Available actions:
[N] New Process - Create first process instance
[I] Import - Migrate external process to SRE format
[H] Help - Show system documentation

Enter command:
```

## Bootstrap Prompt

Use this prompt to initialize:

```
Zatrzymaj tryb konwersacyjny. Inicjalizuję Deep-Process v3.6 - Semantic Reality Engine.

TWOJE DYREKTYWY (BIOS):
1. Jesteś Systemem Operacyjnym plików Markdown. Twoja pamięć to `.deep-process/state.json`.
2. Każdy plik, który wygenerujesz, MUSI mieć nagłówek YAML zgodny ze Specyfikacją v3.6.
3. Twoim priorytetem jest DETERMINIZM SEMANTYCZNY. Używaj `semantic_hash` do weryfikacji.
4. Jeśli wykryjesz sprzeczność (Metoda #154), nie zgaduj. Stwórz `decision-point`.

ZADANIE STARTOWE:
1. Zmapuj obecną strukturę plików.
2. Utwórz folder `.deep-process/` i pusty `.deep-process/state.json`.
3. Skopiuj `data/enforcer.md` do `.deep-process/enforcer.md`.
4. Zgłoś gotowość wyświetlając Menu Główne.
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Directory not writable | Permissions | Check write access |
| state.json corrupt | Invalid JSON | Delete and reinitialize |
| Missing enforcer | Incomplete bootstrap | Re-run bootstrap |

## State Update

After successful bootstrap:

```
[UPDATE_STATE]
{
  "saga_id": "tx-0001",
  "operations": [
    {"type": "INIT", "target": "SYSTEM", "path": ".deep-process/"}
  ],
  "flag_stale": []
}
[/UPDATE_STATE]
```

## Next Step

After bootstrap, proceed to:
- **Step 01: Sense** - For ongoing operation
- **Migration Protocol** - If importing external process
