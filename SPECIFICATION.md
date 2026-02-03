# TECHNICAL SPECIFICATION: Deep-Process v3.6 (Semantic Reality Engine)

**Codename:** SRE-Convergent
**Version:** 3.6.0-Final
**Architecture:** File-Based, LLM-Executed, Human-Anchored Graph Database
**Target Runtime:** Claude CLI / Gemini CLI / Native Shell

---

## 1. CORE PHILOSOPHY & INVARIANTS

System nie jest chatbotem. Jest **Semantycznym Systemem Operacyjnym**, który wymusza determinizm na probabilistycznym silniku (LLM) poprzez 5 nienaruszalnych Filarów.

### 1.1. The 5 Pillars of Architecture
1.  **Transactional Processes (Saga Pattern):**
    *   Każda operacja zapisu jest transakcją.
    *   Brak `[UPDATE_STATE]` w odpowiedzi = `ROLLBACK` (odrzucenie odpowiedzi przez Operatora).
    *   Stan "pomiędzy" jest niedopuszczalny.
2.  **Structured Rails (Schema Enforcement):**
    *   LLM nie "pisze" dokumentów; LLM "wypełnia" schematy zdefiniowane w kontraktach YAML.
    *   Walidacja następuje *przed* zapisem (Pre-commit hook w postaci Sub-Agenta).
3.  **Topology Awareness (Change Coupling):**
    *   System mapuje zależności (`depends_on`).
    *   Zmiana w węźle A automatycznie flaguje węzły zależne B i C jako `STALE`.
4.  **Semantic Lineage (Traceability):**
    *   Każdy artefakt posiada wskaźnik `source_id`.
    *   Można prześledzić drogę od Tasku (kod) przez Epik aż do Wizji.
5.  **Convergent Determinism (Method #108):**
    *   Determinizm nie jest binarny (identyczność znaków), lecz semantyczny (zgodność faktów).
    *   Wymuszenie: `semantic_hash` w każdym artefakcie + weryfikacja przez Operatora (Human Anchor).

---

## 2. FILESYSTEM ARCHITECTURE (The Hardware)

Architektura oparta na modelu obiektowym z **trzema warstwami dziedziczenia**:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: META-CLASS (Deep-Process Framework)                              │
│  Location: src/core/deep-process/                                          │
│  Provides: HOW to execute (methods, validation, orchestration)             │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: PROCESS CLASSES (SRE-Convergent Process Definitions)             │
│  Location: src/core/deep-process/processes/                                │
│  Provides: WHAT to execute (steps, artifacts, gates)                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: PROCESS INSTANCES (Runtime Executions)                           │
│  Location: artifacts/processes/{instance-id}/                              │
│  Tracked in: .deep-process/registry.json                                   │
│  Provides: EXECUTION results (generated artifacts)                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1. Framework Definition (Layer 1)

```text
src/core/deep-process/              # META-CLASS (Framework)
├── workflow.md                     # Main documentation
├── data/
│   ├── enforcer.md                 # BIOS: Law 0 + Method Translator
│   ├── contract-interpretation-protocol.md  # YAML parsing as executable
│   ├── state-schema.yaml           # Schema for state.json
│   ├── registry-schema.yaml        # Schema for registry.json
│   ├── contract-schema.yaml        # Universal Contract schema
│   └── method-procedures/          # 17 method procedures
├── steps/                          # Deep-Pulse phases (SENSE→SYNC)
├── agents/                         # PM, Validator, Implementation Agent
└── processes/                      # LAYER 2: Process Definitions
    ├── _manifest.yaml              # Registry of available processes
    └── [process-name]/             # Each SRE-Convergent process
        ├── process.yaml            # Steps, gates, methods
        └── templates/              # Artifact templates
```

### 2.2. Runtime Instance (Layer 3)

```text
/project-root/                      # USER PROJECT
├── .deep-process/                  # RUNTIME KERNEL
│   ├── state.json                  # Graph DB (all artifacts)
│   ├── registry.json               # Instance tracking
│   └── backups/                    # Saga rollback storage
│
├── artifacts/                      # USER SPACE
│   └── processes/                  # LAYER 3: Process Instances
│       ├── onboarding-client-acme-001/
│       │   ├── instance-state.json
│       │   └── *.md                # Generated artifacts
│       └── code-review-feature-auth-001/
│
└── .claude/commands/               # CLI INTERFACE
```

---

## 3. DATA STRUCTURES (The Logic Layer)

### 3.1. The Universal Contract (YAML Header)
Każdy plik `.md` w `artifacts/` i `processes/` **MUSI** zaczynać się od tego bloku.

**⚠️ CRITICAL: YAML Header = Executable Instructions**

YAML header NIE jest metadanymi dla ludzi — jest **instrukcjami wykonawczymi dla LLM**.
Przed czytaniem treści Markdown, LLM MUSI wykonać **Contract Interpretation Protocol**:

```text
PHASE I:  Context Rehydration    → Load all depends_on, check STALE
PHASE II: Runtime Configuration  → Inject active_methods, evaluate gates
PHASE III: Determinism Enforcement → Lock semantic_hash as constraints
═══════════════════════════════════════════════════════════════════════
ONLY NOW: Read Markdown body
```

Pełny protokół: `src/core/deep-process/data/contract-interpretation-protocol.md`

```yaml
---
dp_id: "EPIC-USER-LOGIN"       # Unique ID
dp_type: "artifact"            # [artifact | process | decision-point]
dp_status: "STALE"             # [NOW | STALE | COMMITTED | FAILED | AWAITING_USER_INPUT]
version: "3.6"

# === TOPOLOGY & LINEAGE ===
context:
  depends_on:
    - path: "artifacts/vision.md"
      type: "semantic_source"  # Changes here invalidate content
    - path: "artifacts/security_policy.md"
      type: "hard_constraint"  # Changes here invalidate logic

# === CONVERGENT DETERMINISM ===
# Lista faktów, które muszą pozostać prawdziwe niezależnie od redakcji tekstu.
semantic_hash:
  - "Auth: OAuth2 via Google"
  - "MFA: Required for Admin"
  - "Session: 24h JWT"

# === EXECUTION LOGIC ===
execution:
  active_methods: [154, 114, 87] # Metody wstrzyknięte przez PM-a
  logic_gates:                   # Warunkowe ścieżki wykonania
    if_mobile: "Use artifact/templates/mobile_screen.md"
    if_web: "Use artifact/templates/web_page.md"

# === TRANSACTION ===
transaction:
  saga_id: "tx-9912"
  previous_hash: "a1b2c3d4"
---
```

### 3.2. Decision Point Contract (Human-in-the-Loop)
Gdy system napotyka sprzeczność, nie zgaduje. Generuje plik typu `decision-point`.

```yaml
---
dp_id: "DP-005"
dp_type: "decision-point"
dp_status: "AWAITING_USER_INPUT"

question:
  type: "EXCLUSIVE_CHOICE"
  trigger: "Conflict detected via Method #154"
  prompt: "Wizja zakłada 'Szybki MVP', a Architektura 'Mikroserwisy'. To sprzeczne."
  options:
    - id: "A"
      label: "Zmień na Monolit (Zgodność z MVP)"
      impact: "Update artifacts/architecture.md"
    - id: "B"
      label: "Wydłuż czas (Zgodność z Mikroserwisami)"
      impact: "Update artifacts/timeline.md"
---
```

---

## 4. SYSTEM KERNEL (BIOS Definition)

Plik `data/enforcer.md` jest ładowany do każdego kontekstu. Zawiera "Prawa Niezmienne", "Tłumacza Metod" i "Zasady Fizyki".

### 4.0. Law 0: CONTRACT PARSING (Prime Directive)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  YAML HEADER ≠ METADATA FOR HUMANS                                          │
│  YAML HEADER = EXECUTABLE INSTRUCTIONS FOR LLM PROCESSOR                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Before reading ANY Markdown content in an artifact file:                  │
│    1. PARSE YAML header as processor instructions                          │
│    2. EXECUTE Phase I: Load all depends_on (Context Rehydration)           │
│    3. EXECUTE Phase II: Inject active_methods (Runtime Configuration)      │
│    4. EXECUTE Phase III: Lock semantic_hash (Determinism Enforcement)      │
│    5. ONLY THEN read Markdown body                                         │
│                                                                             │
│  Full protocol: data/contract-interpretation-protocol.md                   │
│                                                                             │
│  VIOLATION: Reading Markdown before executing YAML = undefined behavior    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.1. Method Translator (Instrukcje Wykonawcze)
Jak LLM ma rozumieć liczby w `active_methods`:

**Anti-Bias Methods (Mandatory in Validation):**
*   **#56 (Liar's Trap):** "List 3 ways you could be deceiving the Operator. Provide evidence you're NOT doing each."
*   **#59 (CUI BONO Test):** "Who benefits? AGENT benefits = RED FLAG, USER benefits = OK."
*   **#60 (Approval Gradient):** "Rate claims 0-100% (truth vs what user wants). Score > 60% = PEOPLE-PLEASING FLAG."

**Coherence Methods (Mandatory in Validation):**
*   **#93 (DNA Inheritance):** "Does new element inherit system 'genes'? Mutations need justification."
*   **#95 (Structural Isomorphism):** "Compare structure with existing. Delta > 30% needs justification."
*   **#99 (Multi-Artifact Coherence):** "Check reference integrity, naming consistency, interface compatibility."
*   **#100 (Vocabulary Consistency):** "Standardize synonyms, disambiguate homonyms."

**Implementation Methods:**
*   **#71 (First Principles):** "Strip assumptions, rebuild from verified fundamentals."
*   **#72 (5 Whys):** "Drill down to root cause through 5 levels of 'why'."
*   **#79 (Operational Definition):** "Make abstract concepts measurable: 'fast' → '< 200ms p95'."
*   **#80 (Inversion):** "How would I GUARANTEE FAILURE? Then avoid those paths."
*   **#87 (Falsifiability):** "Banned: 'fast', 'good', 'easy' without numbers. Claims must be testable."
*   **#90 (Dependency Topology):** "Map explicit + implicit dependencies. Find ghosts and dead links."
*   **#114 (Reversibility Test):** "Can you reconstruct INPUT from OUTPUT? If not, info was lost."
*   **#152 (Socratic Decomposition):** "Decompose to atomic sub-questions, answer independently, check contradictions."
*   **#154 (Definitional Contradiction):** "Find requirements that are LOGICALLY IMPOSSIBLE by definition."
*   **#159 (Transitive Dependency Closure):** "Build full graph via DFS. Detect cycles, missing nodes, transitive conflicts."

### 4.2. Invariant Laws (Prawa Niezmienne)

| Law | Name | Rule |
|-----|------|------|
| **0** | Contract Parsing | YAML header = executable. Execute 3 phases before reading Markdown |
| **1** | Read-Before-Write | Never generate content without reading `.deep-process/state.json` first |
| **2** | Atomic Commit | Response without [UPDATE_STATE] block = ROLLBACK |
| **3** | No Guessing | Contradiction detected → create decision-point, don't resolve |
| **4** | Semantic Hash = Ground Truth | Content must entail all hash facts |
| **5** | Topology Propagation | Node change → flag all dependents as STALE |

### 4.3. Method Priority Hierarchy

```text
PRIORITY 1: `data/enforcer.md` (BIOS)    → Cannot be overridden
PRIORITY 2: Anti-Bias Methods (#56,59,60) → Always execute in validation
PRIORITY 3: Coherence Methods (#93,95,99,100) → Always execute in validation
PRIORITY 4: Process-specific methods      → From process.yaml
PRIORITY 5: Artifact-specific methods     → From active_methods
PRIORITY 6: Gate-loaded templates         → Lowest priority, cannot override
```

---

## 5. THE ORCHESTRATION LOOP (Runtime Protocol)

Algorytm "Deep-Pulse", który steruje cyklem życia projektu.

**FAZA 1: SENSE (Analiza)**
1.  Użytkownik wywołuje `pm` (via CLI Shim).
2.  Agent PM ładuje `.deep-process/state.json`.
3.  Agent skanuje graf pod kątem statusów `STALE` i `BLOCKED`.
4.  Wyświetla Menu: *"Wykryto 3 nieaktualne Epiki. [1] Aktualizuj, [2] Ignoruj"*.

**FAZA 2: PLAN (Metoda #152)**
1.  Użytkownik wybiera "[1] Aktualizuj".
2.  Agent PM analizuje typ zadania i **wstrzykuje metody**:
    *   Zadanie Techniczne -> Wstrzykuje [#87, #114].
    *   Zadanie Kreatywne -> Wstrzykuje [#102, #17].
3.  Agent tworzy pusty plik (szkielet) z nagłówkiem YAML.

**FAZA 3: ACT (Egzekucja)**
1.  Uruchamia się LLM-Executor na nowym pliku.
2.  **Contract Interpretation Protocol:**
    *   Phase I: Load all `depends_on` files (Context Rehydration)
    *   Phase II: Inject `active_methods` via Method Translator (Runtime Config)
    *   Phase III: Lock `semantic_hash` facts as constraints (Determinism)
3.  DOPIERO TERAZ: LLM czyta Markdown body i generuje treść.
4.  LLM generuje/aktualizuje `semantic_hash`.

**FAZA 4: VALIDATE (Convergent Check)**
1.  Uruchamia się LLM-Validator (Sub-Agent).
2.  Sprawdza zgodność: Treść vs Hash vs Rodzice.
3.  Werdykt: `COMMITTED` lub `FAILED`.

**FAZA 5: SYNC (Zapis)**
1.  Operator (Ty) widzisz wynik w terminalu.
2.  Jeśli blok stanu jest poprawny -> Zatwierdzasz (zapis pliku).
3.  Python/CLI aktualizuje `.deep-process/state.json`.

---

## 6. CLI INTERFACE & UX (Punkty Styku)

System jest obsługiwany przez aliasy w folderze `.claude/commands` lub `.gemini/commands`.

### 6.1. Komenda `deep-process` (Project Manager)
*   **Cel:** Główny dashboard i Launcher Procesów.
*   **Prompt Startowy:** "Działaj jako Orchestrator. Przeczytaj `.deep-process/registry.json`. Wyświetl aktywne procesy."
*   **Dynamiczne Menu:**
    ```text
    > SRE-Convergent Manager
    > Aktywne Procesy:
      [1] PROC-MIGRATION (legacy-import-v1) - Status: BLOCKED
      [2] PROC-DEV (feature-login) - Status: RUNNING

    Dostępne akcje:
    [N] Nowy Proces (Instancjonowanie)
    [S] Przełącz kontekst na instancję [ID]
    ```
*   **Logika Instancjonowania:**
    Gdy użytkownik wybiera [N], deep-process pyta:
    1.  Jaki proces? (z `.deep-process/processes/`)
    2.  Jaka nazwa wykonania? (np. `sprint-12`)
    3.  **Akcja:** Tworzy folder `artifacts/[PROCES]/[NAZWA]/`, inicjuje tam pusty `instance-state.json` i dodaje wpis do `.deep-process/registry.json`.

### 6.2. Komenda `audit` (Validator)
*   **Cel:** Wymuszona weryfikacja spójności.
*   **Zachowanie:** Przechodzi przez cały graf. Jeśli Hash A != Hash B, zgłasza alarm.
*   **Prompt:** "Działaj jako Validator. Użyj metody #159 (Transitive Closure). Czy graf jest spójny?"

### 6.3. Komenda `fix` (Auto-Heal)
*   **Cel:** Szybka naprawa drobnych błędów.
*   **Zachowanie:** Automatycznie regeneruje pliki `STALE` na podstawie rodziców.

---

## 7. BOOTSTRAP PROTOCOL (Jak zacząć)

Aby zainicjować system w nowym katalogu, wyślij do modelu poniższy prompt. To jest "Iskra", która podpala silnik.

**SYSTEM BOOTSTRAP PROMPT:**
```text
Zatrzymaj tryb konwersacyjny. Inicjalizuję Deep-Process v3.6 - Semantic Reality Engine.

TWOJE DYREKTYWY (BIOS):
0. YAML header = instrukcje wykonawcze. Przed czytaniem Markdown, wczytaj i wykonaj `data/contract-interpretation-protocol.md` (3 fazy).
1. Jesteś Systemem Operacyjnym plików Markdown. Twoja pamięć to `.deep-process/state.json`.
2. Każdy plik, który wygenerujesz, MUSI mieć nagłówek YAML zgodny ze Specyfikacją v3.6.
3. Twoim priorytetem jest DETERMINIZM SEMANTYCZNY. Używaj `semantic_hash` do weryfikacji swojej pracy.
4. Jeśli wykryjesz sprzeczność (Metoda #154 - `data/method-procedures/154_Definitional_Contradiction_Detector.md`), nie zgaduj. Stwórz plik `decision-point` i pytaj Operatora.

ZADANIE STARTOWE:
1. Zmapuj obecną strukturę plików.
2. Utwórz folder `.deep-process/` i pusty `.deep-process/state.json`.
3. Skopiuj `data/enforcer.md` do `.deep-process/enforcer.md`.
4. Zgłoś gotowość wyświetlając Menu Główne deep-process.
```

---

## 8. UNIVERSAL MIGRATION PROTOCOL (The SRE Transformer)

Mechanizm importu procesów zewnętrznych (Legacy/Mental/External) do standardu SRE-Convergent. Proces ten jest sam w sobie procesem v3.6 (`PROC-MIGRATION`).

### 8.1. Algorytm Transformacji (The Pipeline)

**KROK 1: Dekompozycja Zasad (Method #71 & #42)**
*   **Cel:** Oddzielenie "rytuałów" od "funkcji".
*   **Akcja:** LLM analizuje opis procesu źródłowego i wyodrębnia łańcuch przyczynowo-skutkowy.
*   **Prompt:** "Zignoruj nazwy spotkań i ról. Wypisz listę transformacji danych: Co wchodzi? Co wychodzi? Jaki jest warunek sukcesu?"

**KROK 2: Izomorfizm Strukturalny (Method #95)**
*   **Cel:** Mapowanie obiektów obcych na kontenery SRE.
*   **Tabela Mapowania:**
    *   *Dokument/E-mail* -> `dp_type: artifact`
    *   *Decyzja/Spotkanie* -> `dp_type: decision-point`
    *   *Procedura/Instrukcja* -> `dp_type: process`
    *   *Rola/Osoba* -> `dp_type: agent`

**KROK 3: Wykrywanie Punktów Styku (Method #68)**
*   **Cel:** Identyfikacja, gdzie System musi się zatrzymać.
*   **Analiza:** Każdy moment w oryginale, który wymaga "zatwierdzenia", "opinii" lub "wyboru", jest konwertowany na `Decision Point Contract` z wymuszoną pauzą `AWAITING_USER_INPUT`.

**KROK 4: Generowanie Kontraktów (Method #79)**
*   **Cel:** Operacjonalizacja.
*   **Akcja:** Dla każdego wyodrębnionego kroku, system generuje plik `.md` z nagłówkiem YAML, definiując `input`, `output` i `active_methods`.

**KROK 5: Weryfikacja Wierności (Method #112 & #114)**
*   **Test Entropii (#112):** Porównanie listy informacji wejściowych i wyjściowych. Czy coś zginęło?
*   **Test Odwracalności (#114):** Symulacja: "Mając tylko te nowe pliki SRE, odtwórz opis oryginalnego procesu". Jeśli opis różni się od oryginału -> BŁĄD TRANSFORMACJI.

### 8.2. Obsługa Plików i Rejestracja (State Awareness)

Proces migracji tworzy nową **Klasę Procesu**, która dziedziczy po Meta-Klasie Deep-Process.

1.  **Nowa Klasa Procesu (Definicja):**
    *   System generuje folder: `.deep-process/processes/[NAZWA_PROCESU]/`.
    *   W środku umieszcza `definition.md`, który zawiera specyficzną logikę biznesową, ale w sekcji `inheritance` wskazuje na `.deep-process/enforcer.md`.

2.  **Raport z Migracji (Instancja):**
    *   Dokumentacja przebiegu transformacji trafia do: `artifacts/PROC-MIGRATION/[ID_MIGRACJI]/`.

3.  **Rejestracja:**
    *   Nowa klasa jest dodawana do indeksu dostępnych procesów. Od tej pory można ją instancjonować komendą `deep-process`.

---

## 9. KNOWN LIMITATIONS & MITIGATIONS

*   **Context Window:** Przy dużych grafach `.deep-process/state.json` może spuchnąć.
    *   *Mitigacja:* Dzielenie stanu na `.deep-process/active_state.json` (bieżący sprint) i `.deep-process/archive_state.json`.
*   **LLM Drift:** Model może "zapomnieć" o rygorze YAML w długiej konwersacji.
    *   *Mitigacja:* Każda nowa komenda CLI to "świeża" sesja z załadowanym BIOSem (Stateless Execution).