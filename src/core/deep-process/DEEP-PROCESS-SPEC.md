# Deep Process Specification (LLM-As-Engine)

> **Wersja:** 2.0
> **Filozofia:** "LLM is the CPU, Context is the RAM, Files are the HDD."
> **Kluczowa zasada:** Każdy krok procesu jest samowystarczalny (Self-Contained).

---

## 1. Architektura Systemu

W tym podejściu odwracamy tradycyjną zależność. To nie kod Python steruje LLM-em, ale **LLM steruje procesem**, posiłkując się plikami definicji.

```mermaid
graph TD
    subgraph "Storage (Long-term Memory)"
        ProcessDef[Process Definition<br/>(Map of Steps)]
        Contract[Step Contract<br/>(Self-Contained Prompt)]
        State[.state/ YAMLs<br/>(Project Context)]
    end

    subgraph "Execution Engine (The CPU)"
        LLM((LLM Agent))
    end

    subgraph "Tools (Optional Deterministic Ops)"
        Python[Python Scripts]
        CLI[System CLI]
        API[External APIs]
    end

    ProcessDef -->|Next Step ID| LLM
    State -->|Context Injection| LLM
    Contract -->|Instructions & Schema| LLM
    
    LLM -->|Update| State
    LLM -->|Create| Artifacts[Project Artifacts]
    LLM -.->|Invoke| Python
```

### 1.1 Kluczowe Zmiany w Podejściu
1.  **Samowystarczalność Kontraktu:** Plik kroku (`.md`) zawiera **wszystko**, co jest potrzebne do jego wykonania. Nie wymaga zewnętrznej logiki biznesowej w Pythonie.
2.  **Stan jako Jedyna Prawda:** LLM jest odpowiedzialny za czytanie i **aktualizowanie** stanu (`.state/`). Python nie robi tego "za plecami" modelu (chyba że jako wywołane narzędzie).
3.  **Język Naturalny jako Kod:** Instrukcje w kontrakcie są kodem wykonywalnym dla LLM. Muszą być precyzyjne, atomowe i testowalne.

---

## 2. Struktura Kontraktu (The Unit of Work)

Kontrakt to pojedynczy plik Markdown, który po wczytaniu staje się **kompletnym promptem** dla Agenta.

### Format Pliku: `processes/{process}/phases/{phase}/{step}.md`

```markdown
---
id: create-story
type: step
name: "Break Down Epic into Stories"
# Kontekst wejściowy (LLM musi to przeczytać przed startem)
inputs:
  - artifacts/epics/{epic_id}.yaml
  - .state/items.yaml
# Oczekiwane wyjście (LLM musi to wygenerować)
outputs:
  - artifacts/stories/STORY-*.yaml
# Opcjonalne narzędzia, które LLM ma prawo uruchomić
tools:
  - name: "validate_yaml"
    command: "python tools/validate.py --schema schemas/story.schema.yaml"
next:
  success: verify-stories
  failure: retry
---

# Context & Role
Jesteś **Product Ownerem**. Twoim celem jest rozbicie dużego Epika na małe, niezależne Historyjki (User Stories).

# Input Data
<!-- LLM wstawia tu treść plików z sekcji 'inputs' -->
{inputs_content}

# Instructions (The Algorithm)
Wykonaj następujące kroki, jeden po drugim:

1.  **Analiza:** Przeanalizuj plik Epika. Zrozum "Acceptance Criteria".
2.  **Dekompozycja:** Rozbij Epik na 3-5 mniejszych zadań zgodnie z zasadą INVEST.
3.  **Generowanie ID:** Sprawdź w `.state/items.yaml` ostatni numer sekwencji dla 'story'. Wygeneruj nowe ID (np. STORY-004, STORY-005).
4.  **Tworzenie Plików:** Dla każdej historyjki utwórz nowy plik w `artifacts/stories/` używając poniższego schematu.
5.  **Aktualizacja Stanu:** Dopisz nowe historyjki do `.state/items.yaml` i zaktualizuj sekwencję.

# Output Schema (Strict JSON/YAML)
Każdy plik wyjściowy MUSI być zgodny z tym formatem. Nie dodawaj komentarzy markdown.

```yaml
id: "STORY-{NNN}"
epic_id: "{epic_id}"
title: "Jako [rola] chcę [coś] aby [korzyść]"
points: [Fibonacci number]
status: "draft"
```

# Validation Rules
Przed zakończeniem sprawdź:
- [ ] Czy ID są unikalne?
- [ ] Czy pliki YAML są poprawne składniowo?
- [ ] Czy `epic_id` zgadza się z plikiem wejściowym?
```

---

## 3. Zarządzanie Stanem (State Management)

Ponieważ LLM jest silnikiem, musi on **świadomie** zarządzać swoją pamięcią długotrwałą.

### 3.1 Pliki Stanu (`.state/`)
LLM ma obowiązek aktualizować te pliki po każdej udanej operacji.

*   `process.yaml`: Konfiguracja statyczna.
*   `phase.yaml`: "Instruction Pointer" - gdzie jestem w procesie.
*   `items.yaml`: "Heap" - baza obiektów (ID, nazwy, statusy).
*   `history.yaml`: "Log" - co zrobiłem (audit trail).

### 3.2 Protokół Aktualizacji Stanu (Instrukcja dla LLM)
W każdym kontrakcie (lub w globalnym `enforcer.md`) zaszyta jest instrukcja:

> "Po wygenerowaniu artefaktów, MUSISZ zaktualizować `.state/items.yaml`. Jeśli tego nie zrobisz, system 'zapomni' o stworzonych plikach."

---

## 4. Przepływ Sterowania (Control Flow)

### 4.1 Pętla Wykonawcza (The Loop)

Użytkownik (lub lekki skrypt Python CLI) pełni rolę "zegara" (Clock), który popycha cykl do przodu, ale to LLM podejmuje decyzje.

1.  **FETCH:**
    *   System czyta `.state/phase.yaml`.
    *   System identyfikuje `current_step`.
    *   System ładuje plik kontraktu (np. `create-stories.md`).
2.  **PREPARE:**
    *   System wczytuje pliki zdefiniowane w `inputs` kontraktu.
    *   System skleja: `Enforcer Rules` + `Contract` + `Input Content`.
3.  **EXECUTE (LLM):**
    *   LLM przetwarza instrukcje.
    *   LLM używa narzędzi (np. `write_file`, `search_file`).
    *   LLM generuje wynik.
4.  **COMMIT:**
    *   LLM (lub narzędzie) aktualizuje `.state/phase.yaml` (postęp).
    *   LLM decyduje o przejściu do `next: success` lub `failure`.

### 4.2 Bramki (Gates) jako Kroki Weryfikacyjne
Bramka to specjalny rodzaj Kontraktu, gdzie jedynym zadaniem jest ocena.

*   **Input:** Artefakty z poprzedniej fazy.
*   **Instruction:** "Porównaj artefakty z kryteriami X, Y, Z. Oblicz wynik 0-1."
*   **Output:** Aktualizacja `.state/phase.yaml` -> `gate_status: passed/failed`.

---

## 5. Rola Narzędzi Deterministycznych (Optional Tools)

Kod (Python/Bash) jest traktowany jako **rozszerzenie możliwości LLM**, a nie nadrzędny sterownik.

### Kiedy używać kodu?
1.  **Operacje Masowe:** "Przenieś 100 plików".
2.  **Ścisła Walidacja:** "Sprawdź czy YAML parsuje się bez błędów" (LLM może to przeoczyć).
3.  **Zewnętrzne API:** "Wyślij ticket do Jiry".
4.  **Obliczenia:** "Zlicz statystyki wyrazów".

### Definicja Narzędzia w Kontrakcie
```yaml
tools:
  - name: "git_commit"
    description: "Zapisz zmiany w repozytorium"
    command_template: "git add . && git commit -m '{message}'"
```
LLM decyduje *kiedy* i *czy* wywołać to narzędzie, wypełniając `message` na podstawie kontekstu.

---

## 6. Enforcer (Global System Instructions)

Aby LLM działał stabilnie jako silnik, potrzebuje "BIOSu" – zestawu nadrzędnych instrukcji wstrzykiwanych do każdej sesji.

---

## 7. Wdrażanie Nowych Procesów

Aby dodać nowy proces (np. `code-review`), użytkownik tworzy tylko pliki Markdown:

1.  `processes/code-review/process.yaml` (Definicja faz).
2.  `processes/code-review/phases/1-analyze/1.1-read-code.md` (Kontrakt).
3.  `processes/code-review/phases/1-analyze/1.2-critique.md` (Kontrakt).

Nie trzeba pisać ani linijki kodu Python w silniku (`src/core/deep-process/engine/`), aby nowy proces zadziałał. To zapewnia pełną skalowalność i elastyczność.
