# Deep Process Engine — Executor

> **Cel:** Instrukcje dla LLM jak czytać i wykonywać procesy
> **Kontekst:** LLM wykonuje via CLI (Claude CLI, Gemini CLI)
> **Zasada:** Proste, atomowe instrukcje — bez skomplikowanych łańcuchów

---

## 1. KIEDY UŻYĆ TEGO DOKUMENTU

Czytasz ten dokument gdy:
1. Użytkownik chce rozpocząć/kontynuować pracę z procesem
2. Użytkownik wywołuje akcję procesową (np. "stwórz epic")
3. Potrzebujesz wiedzieć jak wykonać krok procesu

---

## 2. HIERARCHIA PLIKÓW

```
PRIORYTET CZYTANIA (od najwyższego):

1. engine/executor.md        ← JAK wykonywać (ten plik)
2. engine/enforcer.md        ← CO MUSISZ przestrzegać
3. engine/state-manager.md   ← JAK zarządzać stanem
4. processes/{process}.md    ← CO wykonywać (definicja procesu)
5. .state/*.yaml             ← GDZIE jesteśmy (aktualny stan)
```

**Zasada:** Engine > Process > State

---

## 3. EXECUTION LOOP

### 3.1 Pętla wykonania (dla każdej akcji)

```
┌─────────────────────────────────────────────────────────────────┐
│  1. LOAD                                                        │
│     Wczytaj stan i definicję procesu                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. VERIFY                                                      │
│     Sprawdź czy akcja jest dozwolona (enforcer.md)             │
└─────────────────────────────────────────────────────────────────┘
                              │
                      ┌───────┴───────┐
                      │               │
                 PASS ▼          FAIL ▼
┌─────────────────────────────┐  ┌─────────────────────────────┐
│  3. EXECUTE                 │  │  3. BLOCK                   │
│     Wykonaj akcję           │  │     Wyjaśnij co blokuje    │
└─────────────────────────────┘  └─────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. UPDATE                                                      │
│     Zaktualizuj stan (state-manager.md)                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. REPORT                                                      │
│     Raportuj co zrobione + następny krok                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. KROK 1: LOAD — Wczytywanie

### 4.1 Co wczytać

```yaml
# ZAWSZE wczytuj w tej kolejności:

load_sequence:
  - path: ".state/process.yaml"
    purpose: "Który proces używamy"
    if_missing: "Zainicjalizuj projekt"

  - path: ".state/phase.yaml"
    purpose: "Gdzie jesteśmy w procesie"
    if_missing: "Faza = pierwsza faza procesu"

  - path: "processes/{process_id}.md"
    purpose: "Definicja procesu"
    if_missing: "BŁĄD: Brak definicji procesu"
```

### 4.2 Jak wczytać

```markdown
## INSTRUKCJA: Wczytywanie stanu

1. Użyj Read tool na `.state/process.yaml`
2. Wyciągnij `process_id`
3. Użyj Read tool na `.state/phase.yaml`
4. Użyj Read tool na `processes/{process_id}.md`

Jeśli którykolwiek plik nie istnieje — STOP i wykonaj inicjalizację.
```

### 4.3 Co zapamiętać po wczytaniu

```yaml
context:
  process_id: string      # np. "project-management"
  current_phase: string   # np. "planning"
  phase_progress: number  # np. 0.65
  blocking_items: list    # lista blokujących elementów
  next_gate: object       # następny gate do przejścia
```

---

## 5. KROK 2: VERIFY — Weryfikacja

### 5.1 Checklist weryfikacji

Przed KAŻDĄ akcją sprawdź:

```markdown
## VERIFY CHECKLIST

□ 1. PHASE CHECK
     Czy obecna faza pozwala na tę akcję?
     → Sprawdź: process.phases[current_phase].steps

□ 2. ARTIFACTS CHECK
     Czy wymagane artefakty istnieją?
     → Sprawdź: step.requires.artifacts
     → Dla każdego: czy plik istnieje?

□ 3. BLOCKERS CHECK
     Czy coś blokuje tę akcję?
     → Sprawdź: .state/phase.yaml → blocking_items
     → Czy którykolwiek blocker dotyczy tej akcji?

□ 4. GATE CHECK
     Czy nie próbujemy przeskoczyć gate?
     → Sprawdź: czy wszystkie poprzednie fazy completed?
```

### 5.2 Wynik weryfikacji

```yaml
# Jeśli WSZYSTKIE checks PASS:
verification:
  result: PASS
  action: PROCEED

# Jeśli KTÓRYKOLWIEK check FAIL:
verification:
  result: FAIL
  action: BLOCK
  reason: "Konkretny powód"
  resolution: "Co użytkownik musi zrobić"
```

### 5.3 Jak raportować BLOCK

```markdown
## SZABLON: Blokada akcji

⛔ **NIE MOGĘ WYKONAĆ TEJ AKCJI**

**Powód:** [konkretny powód]

**Co blokuje:**
- [element blokujący 1]
- [element blokujący 2]

**Żeby odblokować:**
1. [krok 1]
2. [krok 2]

**Lub:** [alternatywa jeśli istnieje]
```

---

## 6. KROK 3: EXECUTE — Wykonanie

### 6.1 Zasady wykonania

```yaml
execution_rules:
  - rule: "ATOMIC"
    meaning: "Jeden krok = jedna rzecz"
    example: "Nie twórz 5 epiców naraz, twórz po jednym"

  - rule: "EXPLICIT"
    meaning: "Mów co robisz"
    example: "Tworzę plik artifacts/epics/EPIC-001.yaml..."

  - rule: "VERIFY_OUTPUT"
    meaning: "Sprawdź czy wyjście jest poprawne"
    example: "Sprawdzam czy plik został utworzony..."

  - rule: "NO_ASSUMPTIONS"
    meaning: "Nie zakładaj, pytaj"
    example: "Jeśli nie wiem → pytam użytkownika"
```

### 6.2 Struktura wykonania kroku

```markdown
## INSTRUKCJA: Wykonanie kroku

1. **ANNOUNCE**
   "Wykonuję: [nazwa kroku]"

2. **INPUT**
   Wczytaj wymagane artefakty/dane

3. **PROCESS**
   Wykonaj logikę kroku (zgodnie z definicją w procesie)

4. **OUTPUT**
   Zapisz wynik (artefakt, zmiana stanu)

5. **VERIFY**
   Sprawdź czy wynik jest poprawny:
   - Plik istnieje?
   - Format poprawny?
   - Zawartość sensowna?

6. **CONFIRM**
   "Zakończone: [co zostało zrobione]"
```

### 6.3 Obsługa błędów podczas wykonania

```yaml
error_handling:
  file_write_failed:
    action: "RETRY once, then REPORT to user"

  missing_information:
    action: "ASK user for clarification"

  validation_failed:
    action: "FIX if possible, else REPORT"

  unexpected_state:
    action: "STOP and REPORT, do not continue"
```

---

## 7. KROK 4: UPDATE — Aktualizacja stanu

### 7.1 Co zawsze aktualizować

Po KAŻDEJ udanej akcji:

```yaml
always_update:
  - file: ".state/phase.yaml"
    fields:
      - phase_progress  # Jeśli postęp
      - last_action     # Co zrobiono
      - last_action_at  # Kiedy

  - file: ".state/history.yaml"
    action: "APPEND nowy wpis"
```

### 7.2 Co aktualizować warunkowo

```yaml
conditional_update:
  - when: "Utworzono artefakt"
    update:
      file: ".state/phase.yaml"
      field: "artifacts"
      action: "APPEND path do artefaktu"

  - when: "Podjęto decyzję"
    update:
      file: ".state/decisions.yaml"
      action: "APPEND nowa decyzja"

  - when: "Odkryto unknown"
    update:
      file: ".state/unknowns.yaml"
      action: "APPEND nowy unknown"

  - when: "Zmieniono fazę"
    update:
      file: ".state/phase.yaml"
      fields:
        - current_phase
        - phase_started
      also: "APPEND do history"
```

### 7.3 Zasada atomowości aktualizacji

```markdown
## ZASADA: Atomic State Update

ZAWSZE aktualizuj stan PO udanym wykonaniu, NIGDY przed.

ŹRÓDLE:
1. Wykonaj akcję
2. Sprawdź czy się udała
3. DOPIERO WTEDY aktualizuj stan

NIE:
1. Aktualizuj stan
2. Wykonaj akcję
3. Jeśli się nie uda → stan jest niespójny
```

---

## 8. KROK 5: REPORT — Raportowanie

### 8.1 Szablon raportu sukcesu

```markdown
## SZABLON: Raport sukcesu

✅ **WYKONANO: [nazwa akcji]**

**Co zrobione:**
- [konkretny wynik 1]
- [konkretny wynik 2]

**Pliki zmienione:**
- `[ścieżka]` — [co zmieniono]

**Stan projektu:**
- Faza: [faza]
- Postęp: [progress]%

**Następny krok:**
→ [rekomendowany następny krok]
```

### 8.2 Szablon statusu projektu

```markdown
## SZABLON: Status projektu

╔═══════════════════════════════════════════════════════════════════╗
║  PROJEKT: {name}                                                  ║
╠═══════════════════════════════════════════════════════════════════╣
║  FAZA: {phase}                    Postęp: {progress_bar} {%}     ║
║                                                                   ║
║  {phase_indicators}                                               ║
║                                                                   ║
║  BLOKERY: {blocker_count}                                        ║
║  {blocker_list if any}                                           ║
║                                                                   ║
║  NASTĘPNY KROK: {recommendation}                                  ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 9. SPECJALNE PRZYPADKI

### 9.1 Inicjalizacja projektu

```markdown
## INSTRUKCJA: Inicjalizacja nowego projektu

TRIGGER: Brak `.state/process.yaml` LUB user prosi o nowy projekt

1. PYTAJ użytkownika:
   - Nazwa projektu?
   - Który proces? (pokaż dostępne z processes/)
   - Integracje? (Azure DevOps / GitHub / brak)

2. TWÓRZ strukturę:
   ```
   .state/
   ├── process.yaml
   ├── phase.yaml
   ├── items.yaml
   └── history.yaml
   artifacts/
   ```

3. WYPEŁNIJ pliki inicjalnymi wartościami

4. RAPORTUJ: "Projekt zainicjalizowany, możesz zaczynać"
```

### 9.2 Weryfikacja gate'a

```markdown
## INSTRUKCJA: Weryfikacja gate'a

TRIGGER: User prosi o sprawdzenie gate'a LUB phase_progress > 0.85

1. WCZYTAJ definicję gate'a z procesu
2. DLA KAŻDEGO kryterium:
   - Sprawdź czy spełnione
   - Oceń 0.0-1.0
3. OBLICZ score = weighted average
4. PORÓWNAJ z threshold

5a. JEŚLI score >= threshold:
    - Aktualizuj: gate.status = "passed"
    - Aktualizuj: current_phase = next_phase
    - RAPORTUJ: "Gate przeszedł!"

5b. JEŚLI score < threshold:
    - Listuj gaps
    - RAPORTUJ: "Gate nie przeszedł, brakuje: ..."
```

### 9.3 Kontynuacja sesji

```markdown
## INSTRUKCJA: Kontynuacja po przerwie

TRIGGER: User wraca do projektu

1. WCZYTAJ cały stan
2. SPRAWDŹ blocking_items
3. SPRAWDŹ co było ostatnio robione (history)
4. POKAŻ status projektu
5. ZAPROPONUJ następny krok
```

---

## 10. SELF-CHECK

Przed zakończeniem KAŻDEJ sesji, zapytaj siebie:

```markdown
## SELF-CHECK (po każdej akcji)

□ Czy wykonałem to co user prosił?
□ Czy zaktualizowałem stan?
□ Czy stan jest spójny z rzeczywistością?
□ Czy user wie co zrobiono i co dalej?
□ Czy nie pominąłem enforcement rules?
```

---

## 11. VOCABULARY

| Termin | Znaczenie |
|--------|-----------|
| Phase | Faza procesu (np. ideation, planning) |
| Step | Krok w ramach fazy |
| Gate | Punkt weryfikacji między fazami |
| Artifact | Plik wyjściowy (dokument, config) |
| State | Stan projektu w `.state/` |
| Blocker | Element blokujący postęp |
| Process | Definicja procesu w `processes/` |

---

## 12. ZAŁĄCZNIKI

### A. Flowchart decyzyjny

```
START
  │
  ▼
Czy .state/ istnieje? ──NO──▶ INICJALIZUJ
  │
  YES
  │
  ▼
Wczytaj stan + proces
  │
  ▼
User request ──▶ Mapuj na step/action
  │
  ▼
VERIFY (enforcer.md)
  │
  ├──FAIL──▶ BLOCK + wyjaśnij
  │
  PASS
  │
  ▼
EXECUTE step
  │
  ▼
UPDATE state
  │
  ▼
REPORT + recommend next
  │
  ▼
END (czekaj na kolejne polecenie)
```
