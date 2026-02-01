# Deep Process Engine — Idea Document

> **Status:** Idea / Conceptual Design
> **Data:** 2026-02-01
> **Autor:** Współpraca człowiek + AI
> **Cel:** Meta-framework do definiowania i egzekwowania procesów przez LLM via CLI

---

## 1. Problem Statement

### Co chcemy osiągnąć

Stworzyć **uniwersalny silnik procesów** który:
1. Pozwala szybko definiować dowolne procesy (project management, UX, dokumentacja, cokolwiek)
2. LLM przestrzega procesu ściśle — nie "interpretuje", tylko wykonuje
3. Automatycznie śledzi stan — nigdy nie zastanawiamy się "gdzie jesteśmy"
4. Odkrywa "unknown unknowns" — rzeczy o których nie wiemy że nie wiemy
5. Integruje się z zewnętrznymi systemami (Azure DevOps, MCP, GitHub)
6. Jest skalowalny — od prostego workflow do enterprise

### Dlaczego istniejące rozwiązania nie wystarczają

| Problem | BMAD | Nasze rozwiązanie |
|---------|------|-------------------|
| Adaptowalność | Sztywne workflow'y | Generyczny engine + definicje procesów |
| State tracking | Brak centralnego stanu | Explicit `.state/` z weryfikacją |
| Enforcement | LLM "stara się" przestrzegać | Twarde reguły + blokowanie |
| Integracje | Brak | Adapter layer (Azure DevOps, MCP) |
| Unknown unknowns | Brak | Aktywne wykrywanie |

---

## 2. Kluczowe Decyzje Architektoniczne

### Decyzja 1: LLM wykonuje proces via CLI, nie "silnik" w kodzie

**Kontekst:**
- Używamy Claude CLI, Gemini CLI, podobnych narzędzi
- LLM ma dostęp do systemu plików, Bash, MCP tools
- Nie chcemy pisać kodu który "uruchamia" LLM

**Decyzja:**
Process Engine to **zbiór plików** (markdown + YAML) które LLM czyta i wykonuje, nie kod TypeScript/Python.

**Konsekwencje:**
- ✅ Proste — nie trzeba nic instalować
- ✅ Portable — działa z każdym LLM CLI
- ✅ Debugowalne — wszystko w plikach tekstowych
- ❌ Enforcement zależy od "posłuszeństwa" LLM
- ❌ Brak runtime validation (ale można obejść przez Bash scripts)

**Dlaczego tak:**
```
USER: "stwórz epic dla funkcji logowania"
         │
         ▼
┌─────────────────────────────────────────┐
│  LLM (Claude CLI)                       │
│                                         │
│  1. Czyta: processes/project-mgmt.md    │
│  2. Czyta: .state/project.yaml          │
│  3. Sprawdza: "czy mogę to zrobić?"     │
│  4. Jeśli tak → wykonuje                │
│  5. Aktualizuje: .state/                │
│  6. Opcjonalnie: az devops sync         │
└─────────────────────────────────────────┘
```

### Decyzja 2: Separacja Engine vs Process Definitions

**Kontekst:**
Chcemy móc szybko tworzyć nowe procesy bez przepisywania core logic.

**Decyzja:**
```
deep-process/
├── engine/                    # STAŁE — jak wykonywać procesy
│   ├── executor.md            # Instrukcje dla LLM jak czytać/wykonywać
│   ├── state-manager.md       # Jak zarządzać stanem
│   ├── enforcer.md            # Reguły enforcement
│   └── integrations/          # Adaptery do zewnętrznych systemów
│
└── processes/                 # ZMIENNE — co wykonywać
    ├── project-management.md
    ├── ux-design.md
    ├── code-documentation.md
    └── custom.md
```

**Konsekwencje:**
- ✅ Jeden engine, wiele procesów
- ✅ Łatwo dodać nowy proces — tylko nowy plik
- ✅ Można wersjonować procesy niezależnie
- ✅ Można dzielić się procesami (library)

### Decyzja 3: State jako pliki YAML w `.state/`

**Kontekst:**
LLM potrzebuje wiedzieć gdzie jesteśmy, co zrobione, co blokuje.

**Decyzja:**
```
.state/
├── process.yaml      # Który proces używamy
├── phase.yaml        # Obecna faza i progress
├── items.yaml        # Work items (epics, stories, tasks)
├── decisions.yaml    # Podjęte decyzje
├── unknowns.yaml     # Odkryte niewiadome
└── history.yaml      # Co robiliśmy (audit trail)
```

**Dlaczego YAML a nie JSON/MD:**
- Czytelny dla człowieka i LLM
- Łatwy do parsowania
- Wsparcie dla komentarzy
- Standardowy format

**Przykład `.state/phase.yaml`:**
```yaml
process: project-management
version: "1.0"

current_phase: planning
phase_progress: 0.65

phases_completed:
  - ideation: { score: 0.82, completed_at: "2026-02-01T10:00:00Z" }
  - specification: { score: 0.91, completed_at: "2026-02-01T14:00:00Z" }

blocking_items:
  - type: decision
    id: DEC-003
    title: "Wybór bazy danych"
    blocks: [STORY-004, STORY-006]

next_gate:
  name: planning_to_execution
  threshold: 0.80
  current_readiness: 0.65
```

### Decyzja 4: Enforcement przez instrukcje + state checking

**Kontekst:**
LLM musi przestrzegać procesu. Nie możemy "zmusić" LLM kodem, ale możemy:
1. Dać jasne instrukcje
2. Kazać sprawdzać stan przed akcją
3. Blokować akcje gdy warunki nie spełnione

**Decyzja:**
Każdy proces ma sekcję `## ENFORCEMENT` z regułami które LLM MUSI przestrzegać.

**Przykład:**
```markdown
## ENFORCEMENT

### BEFORE ANY ACTION

You MUST read `.state/phase.yaml` and verify:

1. **Phase check:** Current phase allows this action
2. **Artifacts check:** All required artifacts exist
3. **Blockers check:** No blocking items prevent this

If ANY check fails:
- STOP immediately
- Explain what failed
- Suggest how to unblock

### NEVER

- Skip phases
- Create artifacts without updating state
- Proceed when gate threshold not met
- Ignore blocking items
```

### Decyzja 5: Integracje przez Tools (Bash, MCP)

**Kontekst:**
Chcemy integrować z Azure DevOps, GitHub, MCP servers.

**Decyzja:**
LLM używa dostępnych tools:
- **Bash** → `az devops`, `gh`, curl do API
- **MCP** → dedykowane MCP tools jeśli dostępne
- **Adaptery** → pliki instrukcji jak mapować dane

**Przykład integracji Azure DevOps:**
```markdown
## INTEGRATION: Azure DevOps

When `integrations.azure_devops.enabled: true` in process config:

### After creating Epic:
```bash
az boards work-item create \
  --title "{epic.title}" \
  --type "Feature" \
  --description "{epic.description}" \
  --project "{config.azure.project}"
```

### After creating Story:
```bash
az boards work-item create \
  --title "{story.title}" \
  --type "User Story" \
  --parent "{story.epic_id}" \
  --project "{config.azure.project}"
```

Store Azure DevOps IDs in `.state/items.yaml` for sync.
```

---

## 3. Jak to działa — Flow

### 3.1 Inicjalizacja projektu

```
USER: "rozpocznij nowy projekt"
         │
         ▼
LLM:
  1. Sprawdza czy istnieje .state/
  2. Jeśli nie → pyta o:
     - Nazwa projektu
     - Który proces? (project-management / ux-design / custom)
     - Integracje? (Azure DevOps / GitHub / none)
  3. Tworzy strukturę:

     project/
     ├── .state/
     │   ├── process.yaml    # Wybrany proces
     │   ├── phase.yaml      # Faza: ideation
     │   └── items.yaml      # Puste
     ├── artifacts/          # Puste
     └── .process → link do process definition
```

### 3.2 Wykonanie kroku

```
USER: "stwórz epic dla modułu autoryzacji"
         │
         ▼
LLM:
  1. LOAD: Czyta process definition
  2. LOAD: Czyta .state/phase.yaml

  3. VERIFY:
     - Czy obecna faza pozwala na tworzenie epiców?
     - Czy wymagane artefakty istnieją (prd.md, architecture.md)?
     - Czy nie ma blockerów?

  4. IF verification fails:
     → STOP
     → Explain: "Nie mogę stworzyć epica bo..."
     → Suggest: "Najpierw musisz..."

  5. IF verification passes:
     → EXECUTE: Tworzy epic w artifacts/epics/EPIC-001.yaml
     → UPDATE: .state/items.yaml
     → UPDATE: .state/phase.yaml (progress)
     → INTEGRATE: (jeśli włączone) az devops create...

  6. REPORT: Co zrobione, jaki następny krok
```

### 3.3 Weryfikacja gate'a

```
USER: "sprawdź czy możemy przejść do execution"
         │
         ▼
LLM:
  1. LOAD: Gate definition z procesu
  2. CHECK: Każde kryterium
     - Wszystkie stories zdefiniowane? ✓
     - Sprint zaplanowany? ✗
     - Brak blocking decisions? ✓

  3. CALCULATE: Score (np. 0.67)
  4. COMPARE: Score vs threshold (0.80)

  5. IF score < threshold:
     → BLOCK: "Gate nie przeszedł"
     → GAPS: Lista co brakuje
     → SUGGEST: "Zaplanuj sprint żeby przejść"

  6. IF score >= threshold:
     → PASS: "Gate przeszedł!"
     → ADVANCE: Update phase.yaml → execution
     → NEXT: "Możesz zacząć development"
```

---

## 4. Struktura plików

### 4.1 Process Definition (np. `processes/project-management.md`)

```markdown
# Process: Project Management

> Version: 1.0
> Domain: project-management
> Author: ...

## METADATA

```yaml
id: project-management
version: "1.0"

phases:
  - ideation
  - specification
  - architecture
  - planning
  - execution
  - verification

integrations:
  azure_devops:
    enabled: configurable
    work_item_mapping:
      epic: Feature
      story: User Story
      task: Task
```

## ENFORCEMENT

[Reguły które LLM MUSI przestrzegać]

## PHASE: Ideation

### Entry Conditions
- Project initialized

### Steps

#### Step: Capture Idea
**Operation:** deep-challenge
**Produces:** artifacts/idea.md

#### Step: Verify Idea
**Operation:** deep-verify
**Requires:** artifacts/idea.md
**Gate:** clarity >= 0.70

### Exit Gate
- Clarity score >= 0.70
- Problem statement defined
- Target user defined
- Scope bounded

## PHASE: Planning

### Entry Conditions
- Specification completed
- Architecture completed

### Steps

#### Step: Create Epics
**Requires:**
- artifacts/prd.md
- artifacts/architecture.md
**Produces:** artifacts/epics/*.yaml

[...itd...]
```

### 4.2 State files

#### `.state/process.yaml`
```yaml
# Który proces używamy
process_id: project-management
process_version: "1.0"
process_path: processes/project-management.md

project:
  name: "MyApp"
  created: 2026-02-01
  description: "Habit tracking application"

integrations:
  azure_devops:
    enabled: true
    organization: myorg
    project: MyApp
```

#### `.state/phase.yaml`
```yaml
current_phase: planning
phase_started: 2026-02-01T14:00:00Z
phase_progress: 0.65

history:
  - phase: ideation
    status: completed
    score: 0.82
    started: 2026-02-01T10:00:00Z
    completed: 2026-02-01T11:30:00Z

  - phase: specification
    status: completed
    score: 0.91
    started: 2026-02-01T11:30:00Z
    completed: 2026-02-01T13:00:00Z

blocking_items:
  - type: decision
    id: DEC-003
    title: "Database choice"
    created: 2026-02-01T14:30:00Z
    blocks: [STORY-004, STORY-006]

next_gate:
  name: planning_to_execution
  threshold: 0.80
  criteria_status:
    - criterion: "All epics defined"
      status: done
    - criterion: "All stories defined"
      status: done
    - criterion: "Sprint planned"
      status: pending
    - criterion: "No blocking decisions"
      status: blocked
```

#### `.state/items.yaml`
```yaml
epics:
  - id: EPIC-001
    title: "User Authentication"
    status: defined
    stories: [STORY-001, STORY-002, STORY-003]
    azure_devops_id: 12345  # If synced

  - id: EPIC-002
    title: "Habit Tracking"
    status: in_progress
    stories: [STORY-004, STORY-005]

stories:
  - id: STORY-001
    epic: EPIC-001
    title: "User can register with email"
    status: ready
    points: 3
    sprint: SPRINT-001
    azure_devops_id: 12346

  - id: STORY-004
    epic: EPIC-002
    title: "User can create habit"
    status: blocked
    blocked_by: DEC-003
    points: 5

sprints:
  - id: SPRINT-001
    name: "Sprint 1"
    goal: "Basic authentication"
    start: 2026-02-03
    end: 2026-02-14
    stories: [STORY-001, STORY-002]
    status: planned
```

---

## 5. Uruchamianie

### 5.1 Przez Claude CLI

```bash
# Inicjalizacja
claude "Zainicjalizuj projekt z procesem project-management"

# Wykonanie kroku
claude "Stwórz epic dla modułu autoryzacji"

# Sprawdzenie stanu
claude "Pokaż gdzie jesteśmy w projekcie"

# Weryfikacja gate'a
claude "Sprawdź czy możemy przejść do execution"

# Integracja
claude "Zsynchronizuj z Azure DevOps"
```

### 5.2 Przez skill (jeśli zarejestrowany)

```bash
/deep-process init --process=project-management
/deep-process status
/deep-process create-epic "Moduł autoryzacji"
/deep-process verify-gate planning_to_execution
```

### 5.3 LLM wie co robić bo:

1. **Ma dostęp do process definition** — czyta `processes/project-management.md`
2. **Ma dostęp do stanu** — czyta `.state/*.yaml`
3. **Ma jasne instrukcje** — sekcja ENFORCEMENT mówi co MUSI zrobić
4. **Sprawdza warunki** — przed każdą akcją weryfikuje
5. **Aktualizuje stan** — po każdej akcji zapisuje

---

## 6. Adaptowalność — przykłady procesów

### 6.1 Project Management (epics, stories, sprints)

```
Phases: ideation → specification → architecture → planning → execution → verification
Artifacts: idea.md, prd.md, architecture.md, epics/, stories/, sprint.yaml
Integrations: Azure DevOps, GitHub Projects
```

### 6.2 UX Design

```
Phases: research → personas → journeys → wireframes → prototype → testing
Artifacts: research.md, personas/, journeys/, wireframes/, prototype-notes.md
Integrations: Figma (przez MCP), user-testing tools
```

### 6.3 Code Documentation

```
Phases: scan → analyze → document → review → publish
Artifacts: codebase-map.yaml, modules/, api-docs/, architecture-diagrams/
Integrations: GitHub, docs hosting
```

### 6.4 Custom Process

```yaml
# processes/custom.md - User defines:

phases:
  - name: discovery
    steps: [...]
  - name: design
    steps: [...]
  - name: build
    steps: [...]

# LLM follows the same engine rules, just different phases/steps
```

---

## 7. Integracja z zewnętrznymi systemami

### 7.1 Azure DevOps

**Jak działa:**
```markdown
## INTEGRATION: Azure DevOps

### Configuration
In `.state/process.yaml`:
```yaml
integrations:
  azure_devops:
    enabled: true
    organization: myorg
    project: MyProject
    area_path: "MyProject\\Team"
```

### Sync Operations

After creating Epic:
```bash
az boards work-item create \
  --org "https://dev.azure.com/{org}" \
  --project "{project}" \
  --type "Feature" \
  --title "{epic.title}" \
  --description "{epic.description}"
```
Store returned ID in `.state/items.yaml`.

After creating Story:
```bash
az boards work-item create \
  --type "User Story" \
  --title "{story.title}" \
  --parent "{epic.azure_id}"
```

### Sync Status
Read from Azure DevOps and update local state.
```

### 7.2 MCP Server

**Jak działa:**
```markdown
## INTEGRATION: MCP

If MCP tools available, prefer them over Bash:

- `mcp_azure_create_work_item` instead of `az boards`
- `mcp_github_create_issue` instead of `gh issue`

MCP provides:
- Better error handling
- Structured responses
- Authentication management
```

### 7.3 GitHub

**Jak działa:**
```bash
# Create issue for story
gh issue create \
  --title "{story.title}" \
  --body "{story.description}" \
  --label "user-story"

# Create project board
gh project item-add {project_number} --url {issue_url}
```

---

## 8. Enforcement — jak LLM przestrzega procesu

### 8.1 Explicit Instructions

Każdy process definition zawiera:

```markdown
## ENFORCEMENT

### MANDATORY CHECKS (before ANY action)

1. Read `.state/phase.yaml`
2. Verify current phase allows requested action
3. Verify all required artifacts exist
4. Verify no blocking items

### IF CHECK FAILS

- Do NOT proceed
- Explain exactly what failed
- List what needs to happen first
- Wait for user to address

### NEVER

- Skip phases
- Ignore gate thresholds
- Create items without updating state
- Proceed when blocked
```

### 8.2 State as Contract

Stan jest "kontraktem" — LLM nie może go zignorować:

```yaml
# .state/phase.yaml mówi:
current_phase: specification
blocking_items:
  - type: decision
    id: DEC-001
    blocks: [any_architecture_work]

# LLM MUSI to uszanować:
# - Nie może zacząć architecture bo phase = specification
# - Nawet gdyby mógł, DEC-001 blokuje
```

### 8.3 Verification Points

Wbudowane punkty weryfikacji:

```
1. BEFORE step   → Check preconditions
2. DURING step   → Validate outputs
3. AFTER step    → Update state correctly
4. AT gate       → Meet threshold or block
```

---

## 9. Unknown Unknowns — aktywne odkrywanie

### 9.1 Mechanism

Po każdej operacji, LLM sprawdza:

```markdown
## UNKNOWN DETECTION

After each step, check:

1. **Missing NFRs:** Are performance, security, scalability addressed?
2. **Missing edge cases:** What if X fails?
3. **Implicit assumptions:** What are we assuming without evidence?
4. **Forgotten items:** Auth? Logging? Error handling? Backup?

If unknown discovered:
1. Add to `.state/unknowns.yaml`
2. Notify user
3. Suggest how to address
```

### 9.2 State

```yaml
# .state/unknowns.yaml

discovered:
  - id: UNK-001
    description: "Nie rozważono zachowania offline"
    discovered_at: 2026-02-01T14:00:00Z
    discovered_during: specification
    discovered_via: unknown-detector
    priority: high
    status: open
    suggested_action: "Dodaj wymagania offline do PRD"

  - id: UNK-002
    description: "Brak strategii rate limiting"
    discovered_at: 2026-02-01T15:30:00Z
    priority: medium
    status: addressed
    addressed_in: architecture.md
```

---

## 10. Różnice vs BMAD

| Aspekt | BMAD | Deep Process |
|--------|------|--------------|
| **Struktura** | Osobne workflow'y per task | Jeden engine + process definitions |
| **State** | Brak centralnego stanu | `.state/` z pełnym śledzeniem |
| **Enforcement** | LLM "stara się" | Explicit rules + verification |
| **Adaptowalność** | Trzeba modyfikować workflow'y | Nowy plik process definition |
| **Integracje** | Brak | Adapter layer |
| **Unknown unknowns** | Brak | Aktywne wykrywanie |
| **Reusability** | Copy-paste | Library of processes |

---

## 11. Roadmap implementacji

### Phase 1: Core Engine
- [ ] `engine/executor.md` — jak LLM wykonuje procesy
- [ ] `engine/state-manager.md` — jak zarządzać stanem
- [ ] `engine/enforcer.md` — reguły enforcement
- [ ] `.state/` schema definition

### Phase 2: First Process
- [ ] `processes/project-management.md` — pełny proces PM
- [ ] Schemas dla epic, story, sprint
- [ ] Gate definitions

### Phase 3: Integrations
- [ ] Azure DevOps adapter
- [ ] GitHub adapter
- [ ] MCP integration template

### Phase 4: Additional Processes
- [ ] `processes/ux-design.md`
- [ ] `processes/code-documentation.md`
- [ ] Custom process template

### Phase 5: Polish
- [ ] Unknown detector rules
- [ ] Dashboard / status views
- [ ] Multi-agent support (przyszłość)

---

## 12. Open Questions

1. **Skill registration:** Czy procesy rejestrować jako BMAD skills czy osobny system?

2. **Process inheritance:** Czy proces może dziedziczyć z innego? (np. ux-design extends base-process)

3. **Multi-project:** Jak zarządzać gdy pracujemy nad wieloma projektami?

4. **Versioning:** Jak wersjonować procesy i migrować stan?

5. **Rollback:** Jak cofnąć zmiany gdy coś pójdzie nie tak?

6. **Collaboration:** Jak obsłużyć gdy wielu ludzi pracuje?

---

## 13. Appendix: Kluczowe wymagania od użytkownika

Zebrane z konwersacji:

1. **Generyczny silnik** — jeden core, wiele procesów
2. **Łatwa adaptacja** — szybko zdefiniować nowy proces (PM, UX, dokumentacja, cokolwiek)
3. **LLM-enforceable** — agent MUSI przestrzegać procesu
4. **Integrowalny** — Azure DevOps, MCP, inne systemy
5. **Skalowalny** — od prostego workflow do enterprise
6. **CLI-native** — działa z Claude CLI, Gemini CLI, innymi
7. **Unknown unknowns** — aktywne odkrywanie czego nie wiemy
8. **State tracking** — zawsze wiadomo gdzie jesteśmy
9. **Verification gates** — nie można przejść dalej bez spełnienia kryteriów

---

## 14. References

- **Deep Cognitive Architecture:** `docs/deep/architecture.md`
- **BMAD Workflows:** `_bmad/bmm/workflows/`
- **CoALA Paper:** https://arxiv.org/abs/2309.02427
- **ADR Guide:** https://adr.github.io/
