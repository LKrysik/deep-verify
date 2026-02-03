# Specyfikacja Techniczna Procesu: Deep Feasibility

> **Wersja:** 1.0
> **Domena:** Ocena Wykonalności i Ryzyka Projektowego
> **Status:** Specyfikacja Implementacyjna dla Deep Process Engine

---

## 1. Przegląd i Cel

**Deep Feasibility** to systematyczny proces oceny wykonalności inicjatyw, projektów lub decyzji technologicznych. W przeciwieństwie do prostych analiz "na oko", proces ten wymusza rygorystyczne sprawdzenie ograniczeń, wielowymiarową ocenę oraz walidację zewnętrzną przed podjęciem decyzji o alokacji zasobów.

### Cel w Deep Process Engine
Zintegrowanie logiki `Deep Feasibility V1.0` z silnikiem procesowym (`deep-process`), aby umożliwić Agentowi AI:
1.  **Autonomiczne prowadzenie oceny** krok po kroku.
2.  **Zarządzanie stanem** wiedzy o ograniczeniach i ryzykach.
3.  **Wymuszanie rygoru** (np. zakaz ignorowania twardych ograniczeń).
4.  **Generowanie artefaktów** zgodnych ze standardem projektu.

---

## 2. Architektura Procesu

Proces zostanie zdefiniowany jako `deep-feasibility` w strukturze Deep Process.

### 2.1 Struktura Katalogów
```text
src/core/deep-process/processes/deep-feasibility/
├── process.yaml                # Główna definicja procesu
├── schemas/                    # Schematy danych (YAML)
│   ├── constraint.schema.yaml
│   ├── dimension.schema.yaml
│   └── report.schema.yaml
└── phases/                     # Definicje kroków
    ├── 1-frame/
    ├── 2-constrain/
    ├── 3-assess/
    ├── 4-validate/
    └── 5-decide/
```

### 2.2 Integracja z Cyklem Życia
*   **Wejście:** Artefakt `idea.md` (z Project Management), `option.md` (z Deep Explore) lub `architecture.md`.
*   **Wyjście:** `feasibility-report.md`, `decision-record.md`, zaktualizowane `unknowns.yaml`.
*   **Trigger:** Przed fazą "Execution" w Project Management lub jako samodzielna sesja decyzyjna.

---

## 3. Definicja Procesu (`process.yaml`)

```yaml
id: deep-feasibility
version: "1.0"
domain: strategic-assessment
description: "Systematyczna ocena wykonalności w oparciu o ograniczenia i 10 wymiarów"

config:
  depth_levels:
    - id: quick
      name: "Szybka Ocena (30-60 min)"
      phases: [frame, constrain, assess, decide]
    - id: standard
      name: "Standardowa Ocena (Pół dnia)"
      phases: [frame, constrain, assess, validate, decide]
    - id: critical
      name: "Ocena Krytyczna (Wiele dni)"
      phases: [all]

phases:
  - id: frame
    name: "1. Frame (Ramy Problemu)"
    path: phases/1-frame
    entry_point: 1.1-classify-domain.md

  - id: constrain
    name: "2. Constrain (Mapa Ograniczeń)"
    path: phases/2-constrain
    entry_point: 2.1-map-constraints.md

  - id: assess
    name: "3. Assess (Ocena Wymiarowa)"
    path: phases/3-assess
    entry_point: 3.1-score-dimensions.md

  - id: validate
    name: "4. Validate (Weryfikacja Zewnętrzna)"
    path: phases/4-validate
    entry_point: 4.1-reference-class.md

  - id: decide
    name: "5. Decide (Decyzja i Raport)"
    path: phases/5-decide
    entry_point: 5.1-generate-report.md
```

---

## 4. Szczegółowy Opis Faz i Kroków

### Faza 1: FRAME (Ustalenie Ram)
**Cel:** Zrozumieć naturę problemu przed próbą jego oceny.

*   **Krok 1.1: Classify Domain (Cynefin)**
    *   *Akcja:* Analiza opisu problemu pod kątem sygnałów złożoności (niepewność, nowość).
    *   *Wyjście:* `artifacts/feasibility/frame.yaml` (domena: Simple, Complicated, Complex, Chaotic).
    *   *Logika:* Jeśli domena to "Complex" → włącz tryb `probe_mode` (zamiast analitycznej oceny, wymagane są eksperymenty).

*   **Krok 1.2: Define Scope**
    *   *Akcja:* Ustalenie co JEST, a co NIE JEST oceniane.
    *   *Wyjście:* Aktualizacja `frame.yaml` o sekcje `scope_in` i `scope_out`.

### Faza 2: CONSTRAIN (Mapowanie Ograniczeń)
**Cel:** Zidentyfikować twarde ograniczenia, które mogą natychmiast zabić projekt (Fail Fast).

*   **Krok 2.1: Map Constraints**
    *   *Akcja:* Skanowanie pod kątem ograniczeń fizycznych, prawnych, zasobowych.
    *   *Narzędzie:* Metoda #101 (Hardness Spectrum).
    *   *Wyjście:* `artifacts/feasibility/constraints.yaml`.
    *   *Schema:* Lista ograniczeń z poziomem twardości (H0-H5).
    *   *Logika Stopu:* Wykrycie ograniczenia **H5 (Niemożliwe)** → Natychmiastowe przerwanie procesu i rekomendacja NO-GO.

*   **Krok 2.2: Check Contradictions (TRIZ)**
    *   *Akcja:* Szukanie sprzeczności (np. "musi być szybkie ALE tanie").
    *   *Wyjście:* Lista sprzeczności w `constraints.yaml`.

### Faza 3: ASSESS (Ocena Wymiarowa)
**Cel:** Szczegółowa ocena w 10 wymiarach wykonalności.

*   **Krok 3.1: Score Dimensions**
    *   *Akcja:* Ocena 1-5 dla każdego z 10 wymiarów (Techniczna, Ekonomiczna, Prawna, Operacyjna, Czasowa, Skalowania, etc.).
    *   *Wyjście:* `artifacts/feasibility/assessment.yaml`.
    *   *Zasada:* **Weakest Link** – ogólna wykonalność = wynik najsłabszego wymiaru.

*   **Krok 3.2: Identify Binding Constraint**
    *   *Akcja:* Wskazanie wymiaru, który najbardziej blokuje sukces.

### Faza 4: VALIDATE (Weryfikacja)
**Cel:** Usunięcie optymizmu planistycznego (bias).

*   **Krok 4.1: Reference Class Forecasting**
    *   *Akcja:* Znalezienie podobnych projektów z przeszłości i ich wyników.
    *   *Wyjście:* `artifacts/feasibility/validation.yaml` (Base rates).

*   **Krok 4.2: Pre-mortem**
    *   *Akcja:* Symulacja porażki ("Jest rok po wdrożeniu, projekt upadł. Dlaczego?").

### Faza 5: DECIDE (Decyzja)
**Cel:** Synteza i rekomendacja.

*   **Krok 5.1: Generate Report**
    *   *Akcja:* Agregacja wszystkich danych w czytelny raport.
    *   *Wyjście:* `artifacts/feasibility/feasibility-report.md`.

*   **Krok 5.2: Decision Record**
    *   *Akcja:* Formalny zapis: GO / NO-GO / CONDITIONAL / INVESTIGATE.
    *   *Wyjście:* Wpis do `.state/decisions.yaml`.

---

## 5. Schematy Danych (YAML)

### 5.1 `constraints.yaml`
```yaml
constraints:
  - id: CST-001
    description: "Budżet maksymalny 50k PLN"
    hardness: H4 (Sztywne) # H0-H5
    source: "Sponsor"
    status: active
```

### 5.2 `assessment.yaml`
```yaml
dimensions:
  technical:
    score: 4
    confidence: high
    evidence: "Mamy doświadczony zespół"
  economic:
    score: 2
    confidence: medium
    evidence: "Ryzyko przekroczenia budżetu"
    blockers: ["CST-001"]

overall_score: 2 # Minimum z wymiarów
binding_constraint: economic
```

---

## 6. Egzekwowanie Reguł (Enforcement)

Silnik `deep-process` będzie wymuszał następujące reguły (zdefiniowane w `enforcer.md` dla tego procesu):

1.  **Zasada H5 (Impossibility):** Jeśli zidentyfikowano ograniczenie H5, proces NIE MOŻE przejść do fazy Assess. Musi zakończyć się NO-GO lub wrócić do redefinicji (Frame).
2.  **Zasada Cynefin:** Jeśli domena to "Complex", nie wolno używać standardowej estymacji czasu/kosztów (wymuszenie trybu eksperymentalnego).
3.  **Zasada Referencji:** W trybie Standard/Critical, krok 4.1 (Reference Class) jest obowiązkowy. Nie można polegać tylko na "wewnętrznym przeczuciu".
4.  **Zasada "Najsłabsze Ogniwo":** Raport końcowy musi eksponować najniższy wynik wymiaru jako główny wskaźnik ryzyka, a nie średnią.

---

## 7. Sposób Wykonywania (Instrukcja dla Agenta)

Gdy użytkownik wywoła: `python dp.py init deep-feasibility "Ocena Migracji Chmury"`

1.  **Inicjalizacja:** Agent tworzy strukturę katalogów i pliki stanu.
2.  **Pętla Wykonania:**
    *   Agent odczytuje `phases/1-frame/1.1-classify-domain.md`.
    *   Pyta użytkownika o opis migracji.
    *   Klasyfikuje domenę (np. "Complicated").
    *   Zapisuje wynik w `artifacts`.
    *   Aktualizuje `.state/phase.yaml`.
3.  **Bramki (Gates):**
    *   Przed wejściem w fazę `Decide`, Agent sprawdza, czy wszystkie krytyczne wymiary zostały ocenione.
4.  **Raportowanie:**
    *   Na koniec generuje plik Markdown z podsumowaniem, gotowy do przedstawienia interesariuszom.

## 8. Wartość Biznesowa

Wdrożenie tej specyfikacji w `deep-process` zapewnia:
*   **Powtarzalność:** Każda ocena wykonalności ma tę samą strukturę.
*   **Bezpieczeństwo:** Agent nie pozwoli "zapomnieć" o ograniczeniach prawnych czy budżetowych.
*   **Transparentność:** Jasno widać, dlaczego podjęto decyzję NO-GO (np. przez twarde ograniczenie H5).
*   **Oszczędność:** Szybka identyfikacja "Killer Constraints" w fazie 2 oszczędza czas na szczegółową analizę w fazie 3.
