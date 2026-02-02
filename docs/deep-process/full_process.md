# Deep Explore Report: Architektura Zunifikowanego Silnika Procesowego

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║                           D E E P   E X P L O R E   R E P O R T                   ║
║                                    Wersja 2.1                                      ║
║                                                                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║  DECYZJA:   Jak zaprojektować zunifikowany silnik `deep-process`, który będzie     ║
║             elastycznie wykonywał dowolne procesy oparte na kontraktach (BMAD),   ║
║             zapewniając przy tym pełną kontrolę, obserwowalność i ciągłe          ║
║             prowadzenie użytkownika przez interaktywne menu.                      ║
║                                                                                    ║
║  DATA:      2026-02-02                                                            ║
║  GŁĘBOKOŚĆ: deep                                                                   ║
║  COVERAGE:  C ≥ 35 (COMPREHENSIVE)                                                 ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Sekcja 1: Czego się Nauczyliśmy (Audyt Wiedzy)

### Kluczowe Fakty
1.  **Dwa Systemy, Jeden Cel:** `deep-process` i `contract-layer`/`BMAD` rozwiązują ten sam problem na różnych poziomach abstrakcji. `deep-process` zarządza cyklem życia projektu, a `contract-layer` wykonaniem atomowych zadań.
2.  **Kontrakt jako Źródło Prawdy:** Specyfikacja `contract-spec-v0.1.md` jest dojrzałym standardem, który ma być podstawą. Osadzanie kontraktu w YAML frontmatter w pliku Markdown jest kluczowym założeniem.
3.  **Silnik musi być Generyczny:** `src/core/deep-process/` ma stać się uniwersalnym silnikiem zdolnym do uruchomienia *każdego* procesu, a nie tylko `project-management`.
4.  **Proces to Graf Zadań:** Proces nie musi być jednym plikiem. Obawa użytkownika jest słuszna – elastyczniejsza struktura (np. katalog z krokami) jest wymagana.
5.  **Interaktywność jest kluczowa:** Użytkownik nigdy nie może utknąć. System musi dynamicznie prezentować dostępne akcje w formie menu.

### Zmienione Założenia
*   **Z:** "Proces jest zdefiniowany w jednym pliku `.md`." -> **NA:** "Proces to **katalog** zawierający graf powiązanych ze sobą zadań (`.md` z kontraktami)."
*   **Z:** "Kroki w procesie są sztywną listą." -> **NA:** "Kroki definiują graf zależności (`next: success/failure`), co pozwala na elastyczne i rozgałęzione przepływy pracy."

---

## Sekcja 2: Czego Jeszcze Nie Wiemy (Kolejka Badawcza)

1.  **Odkrywanie Procesów i Akcji:** Jak silnik ma dynamicznie znajdować wszystkie dostępne procesy (np. `bmm`, `project-management`) i akcje kontekstowe (np. "zmień epic")?
2.  **Generowanie Menu Kontekstowego:** Jak dokładnie generować menu, które zależy od aktualnego stanu (np. wybranego artefaktu)?
3.  **Struktura Procesu w Katalogu:** Jaka powinna być dokładna i standardowa struktura katalogu dla procesu, aby silnik mógł ją zrozumieć?
4.  **Definicja "Agentów Akcji":** Czym jest "agent", który wykonuje akcję "zmień epic"? Czy to część silnika, czy też sam jest definiowalny jako proces?

---

## Sekcja 3: Mapa Opcji (Wymiary Projektu)

1.  **Struktura Definicji Procesu:**
    *   **A: Płaski Katalog:** Wszystkie pliki `.md` (kroki) w jednym katalogu. Proste, ale nieczytelne przy dużych procesach.
    *   **B: Katalogi z Manifestem:** Proces to katalog z podkatalogami na fazy i plikiem `process.yaml` definiującym metadane. ⭐ **Rekomendowane** dla czytelności i skalowalności.

2.  **Odkrywanie Dostępnych Akcji:**
    *   **A: Statyczna Rejestracja:** Wszystkie możliwe akcje i procesy są na stałe zakodowane w silniku.
    *   **B: Dynamiczne Skanowanie:** Silnik przy starcie skanuje katalogi `/processes` i `/artifacts` w poszukiwaniu kontraktów, dynamicznie budując listę dostępnych operacji. ⭐ **Rekomendowane** dla maksymalnej elastyczności.

3.  **Model Wykonania Zadań:**
    *   **A: Monolit:** Silnik `deep-process` sam wykonuje instrukcje z Markdown.
    *   **B: Delegacja:** `deep-process` jest orkiestratorem, a wykonanie zadania deleguje do wyspecjalizowanej warstwy wykonawczej (logika z `contract-layer`). ⭐ **Rekomendowane** dla czystości architektury.

4.  **Prezentacja Menu Użytkownikowi:**
    *   **A: Prosta Lista:** Wyświetla wszystkie znalezione akcje. Może być przytłaczająca.
    *   **B: Hierarchiczne Menu:** Grupuje akcje (np. Akcje Globalne, Akcje na Artefakcie, Dostępne Procesy). ⭐ **Rekomendowane** dla przejrzystości.

---

## Sekcja 4: Klastry Strategiczne (Proponowana Architektura)

### **Zunifikowany Silnik Procesowy v2.0 (Architektura Rekomendowana)**

System składa się z dwóch głównych pętli: **Pętli Zarządzania (Orchestration Loop)** i **Pętli Wykonania (Execution Loop)**.

#### **1. Struktura Plików**

Wprowadzamy standardową strukturę dla definicji procesów.

```
/processes/
├── code-review/
│   ├── process.yaml
│   ├── 01-analyze.md
│   └── 02-generate-report.md
├── project-management/
│   ├── process.yaml
│   ├── 1-ideation/
│   │   ├── 1.1-capture-idea.md
│   │   └── 1.2-identify-unknowns.md
│   ├── 2-specification/
│   │   └── ...
│   └── ...
└── bmm/
    ├── process.yaml
    └── ... (pliki .md z zadaniami dla LLM)
```
*   **`process.yaml` (Manifest):** Plik w głównym katalogu procesu, który go opisuje: `id`, `name`, `domain`, `entry_point` (pierwszy krok do uruchomienia).

#### **2. Pętla Zarządzania (Orchestration Loop) - serce `deep-process`**

To główna pętla interakcji z użytkownikiem.
1.  **Load State:** Wczytaj cały stan projektu z katalogu `.state/`.
2.  **Generate Menu:** Uruchom **Generator Menu**, który:
    a. Skanuje katalog `/processes` w poszukiwaniu plików `process.yaml`, aby znaleźć wszystkie **dostępne procesy** (np. "Uruchom proces: Zarządzanie Projektem").
    b. Skanuje katalog `/artifacts` i na podstawie **kontraktów wyjściowych** (np. `contract: epic`) oraz kontraktów procesów, które przyjmują te artefakty jako `input`, generuje **akcje kontekstowe** (np. "Zmień ten Epic", "Dodaj Story do tego Epica").
    c. Dodaje **akcje globalne** (np. "Pokaż status", "Sprawdź spójność stanu").
3.  **Present Menu:** Wyświetl użytkownikowi hierarchiczne, ponumerowane menu.
4.  **Get User Choice:** Poczekaj na wybór użytkownika.
5.  **Delegate to Executor:** Na podstawie wyboru, przygotuj odpowiednie zadanie (plik `.md` z kontraktem) i przekaż je do Pętli Wykonania.

#### **3. Pętla Wykonania (Execution Loop) - rola `contract-layer`**

Przyjmuje pojedyncze zadanie (`.md` z kontraktem) i wykonuje je.
1.  **Parse Contract:** Przeczytaj kontrakt zadania.
2.  **Verify Inputs:** Sprawdź, czy wszystkie pliki `input` istnieją.
3.  **Execute:** Przekaż całą zawartość pliku `.md` (kontrakt + instrukcje) do LLM w celu wykonania.
4.  **Receive Output:** Odbierz od LLM wygenerowany artefakt.
5.  **Validate Output:** Użyj **Walidatora Wyjść**, aby sprawdzić, czy artefakt jest zgodny ze swoim `output_contract`.
    *   **Success:** Zwróć ścieżkę do wyniku.
    *   **Failure:** Zwróć błąd walidacji. Silnik może zdecydować o ponowieniu (`retry`).
6.  **Update State:** Pętla Zarządzania, po otrzymaniu wyniku, aktualizuje stan w `.state/` (`items.yaml`, `phase.yaml`, `history.yaml`).

---

## Sekcja 5: Mapa Konsekwencji

*   **Elastyczność:** System staje się w pełni konfigurowalny. Każdy zestaw zadań dla LLM (jak `bmm`) można opakować w strukturę katalogu procesu i natychmiast udostępnić w silniku.
*   **Kontrolowalność:** Każdy element (proces, zadanie, artefakt) ma swój kontrakt. Pozwala to na automatyczną walidację na każdym kroku.
*   **Prowadzenie Użytkownika:** Dynamiczne menu eliminuje "ślepe zaułki". Użytkownik zawsze wie, co może zrobić dalej.
*   **Złożoność Implementacji:** Początkowa implementacja silnika (zwłaszcza dynamicznego generatora menu) jest bardziej złożona, ale ta inwestycja zwraca się w postaci skalowalności i łatwości dodawania nowych procesów.

---

## Sekcja 7: Sugerowane Następne Kroki (Plan Implementacji)

Plan implementacji nowego silnika `deep-process v2.0`.

#### **Faza 1: Ujednolicenie Kontraktów (Tydzień 1)**
1.  **Zadanie:** Przepisać istniejące definicje procesów w `src/core/deep-process/processes/` do nowej struktury katalogów (z plikiem `process.yaml`).
2.  **Zadanie:** Zaktualizować wszystkie pliki `.md` z krokami, aby zawierały kontrakty zgodne ze specyfikacją `contract-spec-v0.1.md`.
3.  **Cel:** Stworzenie spójnej, maszynowo-czytelnej bazy procesów.

#### **Faza 2: Budowa Rdzenia Silnika (Tydzień 2-3)**
1.  **Zadanie:** Zaimplementować w `src/core/deep-process/engine/` logikę **Pętli Zarządzania**.
2.  **Zadanie:** Stworzyć **Generator Menu**, który dynamicznie skanuje procesy i artefakty.
3.  **Zadanie:** Stworzyć **Walidator Wyjść**, który sprawdza zgodność artefaktów z kontraktami.
4.  **Cel:** Silnik potrafi wczytać stan, pokazać użytkownikowi poprawne menu i przyjąć od niego zadanie do wykonania.

#### **Faza 3: Integracja Warstwy Wykonawczej (Tydzień 4)**
1.  **Zadanie:** Zintegrować logikę `contract-layer` jako **Pętlę Wykonania**.
2.  **Zadanie:** Połączyć obie pętle: Pętla Zarządzania deleguje zadanie, Pętla Wykonania je realizuje, a wynik wraca do Pętli Zarządzania w celu aktualizacji stanu.
3.  **Cel:** Pierwsze, kompletne przejście od wyboru w menu, przez wykonanie zadania przez LLM, po aktualizację stanu.

---

## Sekcja 8: Minimalne Stwierdzenia

1.  **Proces to graf zadań w katalogu, nie jeden plik.**
2.  **Wszystko co wykonywalne, musi mieć kontrakt.**
3.  **Menu użytkownika jest generowane dynamicznie z kontraktów.**
4.  **Silnik orkiestruje, LLM wykonuje, kontrakty walidują.**
5.  **Nigdy nie zostawiaj użytkownika w ślepym zaułku.**
