# Integracja: Contract Layer + Deep Process Engine

## Jak się łączą

```
┌─────────────────────────────────────────────────────────────────┐
│                     DEEP PROCESS ENGINE                         │
│                                                                 │
│  Fazy → Gates → Unknowns → Decisions → Items                   │
│                                                                 │
│  Zarządza CZYM (epiki, story, sprinty)                         │
│  Zarządza KIEDY (fazy, gates, przejścia)                       │
│  Zarządza RYZYKIEM (unknowns, decisions)                       │
│                                                                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ używa
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CONTRACT LAYER                              │
│                                                                 │
│  Markdown + Kontrakt = atomowe zadania                         │
│                                                                 │
│  Zarządza JAK (wykonanie zadań przez LLM)                      │
│  Zarządza PRZEPŁYWEM (zależności między zadaniami)             │
│  Zarządza OUTPUTEM (wyniki zadań)                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Mapowanie

| Deep Process | Contract Layer |
|--------------|----------------|
| Phase | Zestaw procesów (katalog) |
| Gate | Proces walidacyjny z kontraktem |
| Story | Może być wykonana jako proces |
| Task | Pojedyncze zadanie z kontraktem |
| Unknown | Może generować nowe zadania (spawn) |

## Przykład: Gate jako proces z kontraktem

```markdown
---
id: gate-idea-to-spec
type: process
input: [idea_document, unknowns_list]
output: [gate_result]
depends_on: []
---

# Gate: Ideation → Specification

Oceń czy projekt jest gotowy do przejścia z fazy ideation do specification.

## Kryteria (wszystkie muszą być spełnione)

### 1. Problem clarity (waga: 0.25)
- [ ] Problem jest jasno zdefiniowany
- [ ] Znamy kogo dotyka problem
- [ ] Znamy skalę problemu

### 2. User defined (waga: 0.25)
- [ ] Zdefiniowani użytkownicy docelowi
- [ ] Znamy ich potrzeby
- [ ] Znamy ich ograniczenia

### 3. Success criteria (waga: 0.20)
- [ ] Zdefiniowane mierzalne kryteria sukcesu
- [ ] Wiadomo jak będziemy mierzyć

### 4. Scope bounded (waga: 0.15)
- [ ] Scope jest ograniczony
- [ ] Wiadomo co NIE jest w scope

### 5. Unknowns identified (waga: 0.15)
- [ ] Lista unknowns jest kompletna
- [ ] Każdy unknown ma plan eksploracji

## Output

```yaml
gate_result:
  passed: true/false
  score: 0.0-1.0
  threshold: 0.70
  criteria:
    - name: "Problem clarity"
      score: 0.0-1.0
      notes: "..."
    ...
  recommendation: "proceed/iterate/stop"
  blockers: []
```
```

## Integracja w .state/

### Rozszerzenie phase.yaml

```yaml
current_phase: ideation
phase_started_at: 2026-02-02T10:00:00Z

# NOWE: Powiązanie z procesami Contract Layer
phase_processes:
  - id: capture-idea
    source: processes/ideation/capture-idea.md
    status: completed
    output: artifacts/idea.md
  - id: identify-unknowns
    source: processes/ideation/identify-unknowns.md
    status: in_progress
    output: null

next_gate:
  name: idea_to_spec
  process: processes/gates/gate-idea-to-spec.md  # NOWE
  threshold: 0.70
```

### Rozszerzenie items.yaml

```yaml
stories:
  - id: STORY-001
    title: "Implement login"
    status: ready
    # NOWE: Powiązanie z procesem wykonania
    execution:
      process: processes/dev/implement-story.md
      status: pending
      output: null
```

## Flow wykonania

```
1. Deep Process określa CO trzeba zrobić (story, task)
2. Story/Task ma powiązany proces z Contract Layer
3. Python/LLM wykonuje proces (markdown + kontrakt)
4. Output wraca do Deep Process (.state/ update)
5. Deep Process decyduje o następnym kroku
```

## Przykład: Wykonanie Story przez Contract Layer

```python
# Deep Process wie że STORY-001 jest ready
story = deep_process.get_next_ready_story()

# Pobierz powiązany proces
process_file = story.execution.process

# Contract Layer wykonuje
result = contract_layer.execute(process_file, input={
    "story": story,
    "codebase": "./src"
})

# Update Deep Process state
deep_process.update_story(story.id, {
    "status": "done",
    "execution": {
        "status": "completed",
        "output": result.output
    }
})
```
