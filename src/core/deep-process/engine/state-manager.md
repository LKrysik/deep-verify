# Deep Process Engine — State Manager

> **Cel:** Jak zarządzać stanem projektu w `.state/`
> **Zasada:** Single Source of Truth — stan w plikach jest jedyną prawdą
> **Format:** YAML dla czytelności i łatwego parsowania

---

## 1. STRUKTURA `.state/`

### 1.1 Pliki stanu

```
.state/
├── process.yaml      # Konfiguracja procesu
├── phase.yaml        # Obecna faza i postęp
├── items.yaml        # Work items (epics, stories, tasks)
├── decisions.yaml    # Podjęte decyzje
├── unknowns.yaml     # Odkryte niewiadome
└── history.yaml      # Historia akcji (audit trail)
```

### 1.2 Odpowiedzialności plików

| Plik | Odpowiada za | Kiedy aktualizować |
|------|--------------|-------------------|
| process.yaml | Który proces, config, integracje | Inicjalizacja, zmiana config |
| phase.yaml | Gdzie jesteśmy, blokery, gates | Każda akcja |
| items.yaml | Epics, stories, sprints, tasks | Tworzenie/zmiana items |
| decisions.yaml | ADRs, podjęte decyzje | Podjęcie decyzji |
| unknowns.yaml | Unknown unknowns | Odkrycie, adresowanie |
| history.yaml | Co robiliśmy | Każda akcja |

---

## 2. SCHEMATY PLIKÓW

### 2.1 process.yaml

```yaml
# .state/process.yaml — Konfiguracja procesu

# Identyfikacja
process_id: project-management    # ID procesu
process_version: "1.0"            # Wersja procesu
process_path: processes/project-management.md

# Projekt
project:
  name: "MyApp"
  description: "Habit tracking application"
  created_at: 2026-02-01T10:00:00Z
  created_by: user

# Integracje
integrations:
  azure_devops:
    enabled: true
    organization: myorg
    project: MyApp
    sync_on_create: true
  github:
    enabled: false
  mcp:
    enabled: false

# Ustawienia
settings:
  auto_verify_gate: true          # Automatycznie sprawdzaj gate przy progress > 85%
  require_confirmation: true       # Wymagaj potwierdzenia przed zmianami
  strict_enforcement: true         # Ścisłe egzekwowanie reguł
```

### 2.2 phase.yaml

```yaml
# .state/phase.yaml — Obecny stan fazy

# Obecna faza
current_phase: planning
phase_started_at: 2026-02-01T14:00:00Z
phase_progress: 0.65              # 0.0 - 1.0

# Ostatnia akcja
last_action:
  name: "create-story"
  at: 2026-02-01T15:30:00Z
  result: success

# Historia faz
phases_history:
  - phase: ideation
    status: completed
    started_at: 2026-02-01T10:00:00Z
    completed_at: 2026-02-01T11:30:00Z
    gate_score: 0.82

  - phase: specification
    status: completed
    started_at: 2026-02-01T11:30:00Z
    completed_at: 2026-02-01T13:00:00Z
    gate_score: 0.91

  - phase: architecture
    status: completed
    started_at: 2026-02-01T13:00:00Z
    completed_at: 2026-02-01T14:00:00Z
    gate_score: 0.85

  - phase: planning
    status: in_progress
    started_at: 2026-02-01T14:00:00Z

# Artefakty obecnej fazy
current_artifacts:
  - artifacts/epics/EPIC-001.yaml
  - artifacts/epics/EPIC-002.yaml
  - artifacts/stories/STORY-001.yaml
  - artifacts/stories/STORY-002.yaml

# Blokery
blocking_items:
  - id: BLK-001
    type: decision
    ref: DEC-003
    title: "Wybór bazy danych"
    blocks: [STORY-004, STORY-006]
    created_at: 2026-02-01T14:30:00Z

# Następny gate
next_gate:
  name: planning_to_execution
  threshold: 0.80
  criteria:
    - name: "All epics defined"
      status: done
      score: 1.0
    - name: "All stories defined"
      status: done
      score: 1.0
    - name: "Sprint planned"
      status: pending
      score: 0.0
    - name: "No blocking decisions"
      status: blocked
      score: 0.0
  current_score: 0.50
```

### 2.3 items.yaml

```yaml
# .state/items.yaml — Work items

# Sequence counters
sequences:
  epic: 3
  story: 7
  task: 1
  sprint: 1

# Epics
epics:
  - id: EPIC-001
    title: "User Authentication"
    description: "Complete auth system with login, register, password reset"
    status: defined           # defined | in_progress | done
    stories: [STORY-001, STORY-002, STORY-003]
    created_at: 2026-02-01T14:10:00Z
    azure_devops_id: 12345    # jeśli zsynchronizowane

  - id: EPIC-002
    title: "Habit Tracking Core"
    description: "Basic habit CRUD and daily tracking"
    status: in_progress
    stories: [STORY-004, STORY-005, STORY-006]
    created_at: 2026-02-01T14:20:00Z

# Stories
stories:
  - id: STORY-001
    epic_id: EPIC-001
    title: "User can register with email"
    description: "As a new user, I want to register with email and password"
    status: ready             # draft | ready | in_progress | done | blocked
    points: 3
    sprint_id: SPRINT-001
    acceptance_criteria:
      - "Email validation"
      - "Password requirements"
      - "Confirmation email sent"
    created_at: 2026-02-01T14:15:00Z
    azure_devops_id: 12346

  - id: STORY-004
    epic_id: EPIC-002
    title: "User can create habit"
    description: "As a user, I want to create a new habit to track"
    status: blocked
    blocked_by: DEC-003       # Czeka na decyzję o bazie
    points: 5
    created_at: 2026-02-01T14:25:00Z

# Sprints
sprints:
  - id: SPRINT-001
    name: "Sprint 1 - Foundation"
    goal: "Basic authentication working"
    start_date: 2026-02-03
    end_date: 2026-02-14
    status: planned           # planned | active | completed
    stories: [STORY-001, STORY-002]
    capacity: 20
    committed_points: 8
    created_at: 2026-02-01T15:00:00Z

# Tasks (if using tasks within stories)
tasks: []
```

### 2.4 decisions.yaml

```yaml
# .state/decisions.yaml — Decyzje

# Sequence
sequences:
  decision: 4

# Decyzje
decisions:
  - id: DEC-001
    title: "Frontend framework"
    status: accepted          # pending | accepted | rejected | superseded
    decision: "React Native"
    rationale: "Cross-platform, team experience"
    options_considered:
      - name: "React Native"
        chosen: true
      - name: "Flutter"
        chosen: false
        reason: "Less team experience"
    decided_at: 2026-02-01T11:00:00Z
    decided_by: user
    phase: ideation

  - id: DEC-003
    title: "Database choice"
    status: pending
    options_considered:
      - name: "PostgreSQL + Supabase"
      - name: "MongoDB Atlas"
      - name: "SQLite + custom sync"
    blocking:
      - STORY-004
      - STORY-006
    created_at: 2026-02-01T14:30:00Z
    needed_by: 2026-02-02T00:00:00Z  # Kiedy decyzja jest potrzebna
```

### 2.5 unknowns.yaml

```yaml
# .state/unknowns.yaml — Unknown unknowns

# Sequence
sequences:
  unknown: 3

# Unknowns
unknowns:
  - id: UNK-001
    description: "Offline sync strategy unclear"
    type: technical           # technical | user | market | feasibility
    priority: high
    status: addressed         # discovered | exploring | addressed | accepted_risk
    discovered_at: 2026-02-01T12:00:00Z
    discovered_during: specification
    discovered_via: unknown-detector
    addressed_in: architecture.md
    addressed_at: 2026-02-01T13:30:00Z

  - id: UNK-002
    description: "No rate limiting in requirements"
    type: technical
    priority: medium
    status: discovered
    discovered_at: 2026-02-01T14:00:00Z
    discovered_during: architecture
    suggested_action: "Add rate limiting requirements to PRD"
```

### 2.6 history.yaml

```yaml
# .state/history.yaml — Audit trail

# Historia akcji
entries:
  - id: 1
    action: "init-project"
    at: 2026-02-01T10:00:00Z
    details:
      project_name: "MyApp"
      process: "project-management"

  - id: 2
    action: "execute-step"
    step: "capture-idea"
    phase: ideation
    at: 2026-02-01T10:15:00Z
    result: success
    artifacts_created: [artifacts/idea.md]

  - id: 3
    action: "verify-gate"
    gate: "idea_to_spec"
    at: 2026-02-01T11:30:00Z
    result: passed
    score: 0.82

  - id: 4
    action: "create-epic"
    at: 2026-02-01T14:10:00Z
    result: success
    item_created: EPIC-001

  # ... kolejne wpisy
```

---

## 3. OPERACJE NA STANIE

### 3.1 Wczytywanie stanu

```markdown
## INSTRUKCJA: Wczytywanie stanu

1. Użyj Read tool na każdy plik .state/*.yaml
2. Parsuj YAML do struktury w pamięci
3. Zbuduj kontekst:

context = {
  process: process.yaml content,
  phase: phase.yaml content,
  items: items.yaml content,
  decisions: decisions.yaml content,
  unknowns: unknowns.yaml content
}

4. VERIFY: czy pliki są spójne (brak broken references)
```

### 3.2 Aktualizacja stanu

```markdown
## INSTRUKCJA: Aktualizacja stanu

ZASADA: Read-Modify-Write

1. READ: Wczytaj aktualny plik
2. MODIFY: Zmień tylko potrzebne pola
3. WRITE: Zapisz cały plik

PRZYKŁAD: Dodanie epic

1. Read .state/items.yaml
2. Modify:
   - sequences.epic += 1
   - epics.append(new_epic)
3. Write całe items.yaml
```

### 3.3 Atomowość aktualizacji

```markdown
## ZASADA: Atomic Updates

ZAWSZE aktualizuj w kolejności:

1. Najpierw artefakt (np. artifacts/epics/EPIC-001.yaml)
2. Potem items.yaml (dodaj referencję)
3. Potem phase.yaml (update progress, last_action)
4. Na końcu history.yaml (append entry)

JEŚLI którykolwiek krok FAIL:
- NIE kontynuuj
- RAPORTUJ błąd
- ROLLBACK jeśli możliwe (usuń częściowe zmiany)
```

---

## 4. GENEROWANIE ID

### 4.1 Wzorzec ID

```yaml
id_patterns:
  epic: "EPIC-{sequence:03d}"      # EPIC-001, EPIC-002
  story: "STORY-{sequence:03d}"   # STORY-001, STORY-002
  task: "TASK-{sequence:03d}"     # TASK-001, TASK-002
  sprint: "SPRINT-{sequence:03d}" # SPRINT-001
  decision: "DEC-{sequence:03d}"  # DEC-001
  unknown: "UNK-{sequence:03d}"   # UNK-001
  blocker: "BLK-{sequence:03d}"   # BLK-001
```

### 4.2 Procedura generowania

```markdown
## INSTRUKCJA: Generowanie nowego ID

1. Wczytaj .state/items.yaml (lub odpowiedni plik)
2. Odczytaj sequences.{type}
3. Nowy ID = pattern z sequences.{type}
4. Inkrementuj sequences.{type}
5. Zapisz zaktualizowany plik

PRZYKŁAD: Nowy Epic

sequences.epic = 3
new_id = "EPIC-003"
sequences.epic = 4  # zapisz
```

---

## 5. SPRAWDZANIE REFERENCJI

### 5.1 Typy referencji

```yaml
references:
  story.epic_id: "Must exist in epics"
  story.sprint_id: "Must exist in sprints (if set)"
  story.blocked_by: "Must exist in decisions"
  blocker.ref: "Must exist in decisions/unknowns"
  epic.stories: "All must exist in stories"
```

### 5.2 Weryfikacja referencji

```markdown
## INSTRUKCJA: Weryfikacja integralności referencji

Dla każdego typu referencji:

1. Pobierz wszystkie referencje danego typu
2. Dla każdej referencji:
   - Sprawdź czy target istnieje
   - JEŚLI NIE: dodaj do listy błędów

3. Raportuj:
   - Jeśli błędy: lista broken references
   - Jeśli ok: "Integrity check passed"
```

---

## 6. SYNCHRONIZACJA Z INTEGRACJAMI

### 6.1 Kiedy synchronizować

```yaml
sync_triggers:
  - event: "Item created"
    condition: "integrations.{type}.sync_on_create == true"
    action: "Create in external system, store external_id"

  - event: "Item updated"
    condition: "item.external_id exists"
    action: "Update in external system"

  - event: "Manual sync requested"
    action: "Full sync all items with external_ids"
```

### 6.2 Przechowywanie external IDs

```yaml
# W items.yaml, każdy item może mieć:
- id: EPIC-001
  azure_devops_id: 12345    # Azure DevOps Work Item ID
  github_issue_id: 67       # GitHub Issue number
  # etc.
```

---

## 7. BACKUP I RECOVERY

### 7.1 Kiedy tworzyć backup

```yaml
backup_triggers:
  - event: "Before phase change"
  - event: "Before gate verification"
  - event: "User explicitly requests"
  - event: "Before risky operation"
```

### 7.2 Struktura backup

```markdown
## INSTRUKCJA: Backup stanu

1. Utwórz katalog: .state/backups/{timestamp}/
2. Skopiuj wszystkie pliki .state/*.yaml
3. Zapisz metadata:

.state/backups/{timestamp}/meta.yaml:
  created_at: {timestamp}
  reason: "Before phase change to execution"
  phase_at_backup: planning
```

### 7.3 Recovery

```markdown
## INSTRUKCJA: Przywracanie stanu

1. Listuj dostępne backupy: .state/backups/*/
2. Pokaż użytkownikowi z metadata
3. User wybiera backup
4. WARN: "To nadpisze obecny stan"
5. Jeśli potwierdzone:
   - Skopiuj pliki z backupu do .state/
   - Zapisz w history: "State restored from backup"
```

---

## 8. WALIDACJA STANU

### 8.1 Schema validation

```markdown
## INSTRUKCJA: Walidacja schematu

Dla każdego pliku .state/*.yaml:

1. Sprawdź required fields
2. Sprawdź typy danych
3. Sprawdź enumy (np. status values)
4. Sprawdź formaty (np. daty ISO)

JEŚLI błąd walidacji:
- WARN użytkownika
- Zaproponuj naprawę
```

### 8.2 Business rules validation

```markdown
## INSTRUKCJA: Walidacja reguł biznesowych

1. Wszystkie story muszą mieć epic_id
2. Sprint nie może mieć stories z różnych epiców (soft rule)
3. Blocked story nie może być w active sprint
4. Completed phase musi mieć gate_score
5. current_phase musi być ostatnią non-completed fazą
```

---

## 9. INICJALIZACJA STANU

### 9.1 Dla nowego projektu

```markdown
## INSTRUKCJA: Inicjalizacja nowego projektu

1. Utwórz katalog .state/

2. Utwórz process.yaml:
   process_id: {user_choice}
   process_version: "1.0"
   project.name: {user_input}
   project.created_at: {now}
   integrations: {user_config}

3. Utwórz phase.yaml:
   current_phase: {first_phase_from_process}
   phase_started_at: {now}
   phase_progress: 0.0
   phases_history: []
   blocking_items: []

4. Utwórz items.yaml:
   sequences: {epic: 1, story: 1, ...}
   epics: []
   stories: []
   sprints: []

5. Utwórz decisions.yaml:
   sequences: {decision: 1}
   decisions: []

6. Utwórz unknowns.yaml:
   sequences: {unknown: 1}
   unknowns: []

7. Utwórz history.yaml:
   entries:
     - id: 1
       action: "init-project"
       at: {now}
```

---

## 10. VOCABULARY

| Termin | Znaczenie |
|--------|-----------|
| State | Cały katalog .state/ |
| Phase state | Plik phase.yaml |
| Items | Epics, stories, sprints, tasks |
| Sequence | Licznik do generowania ID |
| Reference | Powiązanie między elementami |
| External ID | ID w zewnętrznym systemie |
| Backup | Kopia stanu w danym momencie |
