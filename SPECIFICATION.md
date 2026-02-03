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

System opiera się na sztywnej strukturze katalogów, która pełni rolę bazy danych.

```text
/project-root/
├── .deep-process/                  # SYSTEM KERNEL (Hidden)
│   ├── enforcer.md                 # BIOS: Method Translator & Invariants
│   ├── state.json                  # GLOBAL REGISTRY (Graph DB)
│   ├── backups/                    # SAGA LOG (Rollback storage)
│   ├── agents/                     # ROLE MANIFESTS (PM, Architect, Validator)
│   └── processes/                  # EXECUTABLE LOGIC (Templates with Gates)
│
├── artifacts/                      # USER SPACE (The Output)
│   ├── vision.md
│   ├── architecture.md
│   └── ... (Subfolders allowed)
│
├── .claude/commands/               # CLI INTERFACE (Shims)
│   ├── deep-process.json           # Entry point for Project Manager
│   └── audit.json                  # Entry point for Validator
│
└── SPECIFICATION.md                # THIS FILE
```

---

## 3. DATA STRUCTURES (The Logic Layer)

### 3.1. The Universal Contract (YAML Header)
Każdy plik `.md` w `artifacts/` i `processes/` **MUSI** zaczynać się od tego bloku.

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

Plik `.deep-process/enforcer.md` jest ładowany do każdego kontekstu. Zawiera "Tłumacza Metod" i "Zasady Fizyki".

### 4.1. Method Translator (Instrukcje Wykonawcze)
Jak LLM ma rozumieć liczby w `active_methods`:

*   **#154 (Definitional Contradiction):** "Przed wygenerowaniem treści, załaduj pliki z `depends_on`. Jeśli nowe zdanie przeczy zdaniu z rodzica -> STOP. Zgłoś konflikt."
*   **#114 (Reversibility Test):** "Twój opis musi być tak precyzyjny, aby inny LLM mógł odtworzyć z niego kod bez pytań. Brak konkretów = FAIL."
*   **#87 (Falsifiability):** "Zabronione są przymiotniki 'szybki', 'ładny'. Używaj liczb: '200ms', 'Material Design 3'."
*   **#90 (Dependency Topology):** "Jeśli zmieniasz ten plik, sprawdź w `state.json`, co od niego zależy i oznacz to jako STALE."

### 4.2. State Management Rules
1.  **Read-Before-Write:** Nie wolno generować treści bez uprzedniego `read_file` na pliku `state.json`.
2.  **Atomic Commit:** Odpowiedź bez bloku JSON z aktualizacją stanu jest traktowana jako awaria systemu.

---

## 5. THE ORCHESTRATION LOOP (Runtime Protocol)

Algorytm "Deep-Pulse", który steruje cyklem życia projektu.

**FAZA 1: SENSE (Analiza)**
1.  Użytkownik wywołuje `pm` (via CLI Shim).
2.  Agent PM ładuje `state.json`.
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
2.  "Tłumacz Metod" w BIOS wymusza styl pracy (np. szukanie sprzeczności).
3.  LLM generuje treść i `semantic_hash`.

**FAZA 4: VALIDATE (Convergent Check)**
1.  Uruchamia się LLM-Validator (Sub-Agent).
2.  Sprawdza zgodność: Treść vs Hash vs Rodzice.
3.  Werdykt: `COMMITTED` lub `FAILED`.

**FAZA 5: SYNC (Zapis)**
1.  Operator (Ty) widzisz wynik w terminalu.
2.  Jeśli blok stanu jest poprawny -> Zatwierdzasz (zapis pliku).
3.  Python/CLI aktualizuje `state.json`.

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
    3.  **Akcja:** Tworzy folder `artifacts/[PROCES]/[NAZWA]/`, inicjuje tam pusty `state.json` i dodaje wpis do `registry.json`.

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
1. Jesteś Systemem Operacyjnym plików Markdown. Twoja pamięć to `.deep-process/state.json`.
2. Każdy plik, który wygenerujesz, MUSI mieć nagłówek YAML zgodny ze Specyfikacją v3.6.
3. Twoim priorytetem jest DETERMINIZM SEMANTYCZNY. Używaj `semantic_hash` do weryfikacji swojej pracy.
4. Jeśli wykryjesz sprzeczność (Metoda #154), nie zgaduj. Stwórz plik `decision-point` i pytaj Operatora.

ZADANIE STARTOWE:
1. Zmapuj obecną strukturę plików.
2. Utwórz folder `.deep-process/` i pusty `state.json`.
3. Utwórz `enforcer.md` z definicją metod #87, #114, #154.
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
Nowo powstałe procesy są "widziane" przez system tylko wtedy, gdy zostaną zarejestrowane.

1.  **Fizyczna Lokalizacja:**
    Wszystkie przetransformowane procesy trafiają do: `artifacts/processes/[NAZWA_PROCESU]/`.
2.  **Rejestracja w Grafie:**
    Transformator musi zakończyć pracę blokiem `[UPDATE_STATE]`, który dodaje wpisy do `state.json` z tagiem `origin: migrated`.

---

## 9. KNOWN LIMITATIONS & MITIGATIONS

*   **Context Window:** Przy dużych grafach `state.json` może spuchnąć.
    *   *Mitigacja:* Dzielenie stanu na `active_state.json` (bieżący sprint) i `archive_state.json`.
*   **LLM Drift:** Model może "zapomnieć" o rygorze YAML w długiej konwersacji.
    *   *Mitigacja:* Każda nowa komenda CLI to "świeża" sesja z załadowanym BIOSem (Stateless Execution).