# Python-LLM Contract Layer

## Kluczowa zasada

**Kontrakt jest CZĘŚCIĄ markdown, nie obok niego.**

```markdown
---
id: analyze-config
input: [config_file]
output: [report]
depends_on: []
---

Otwórz plik {config_file} i przeanalizuj zgodność z best practices...
```

**Jeden plik, jedna prawda, dwa odczyty:**

| Czytelnik | Co widzi | Jak używa |
|-----------|----------|-----------|
| LLM | Cały plik | Kontrakt = instrukcja (co, skąd, dokąd) |
| Python | YAML header | Struktura (graf, kolejność, status) |

**LLM może działać samodzielnie** - bez Pythona. Kontrakt jest zrozumiały dla LLM jako część instrukcji.

**Python jest opcjonalny** - do orchestracji wielu zadań, wizualizacji, automatyzacji.

---

## Problem (historyczny kontekst)

Dwa światy które trudno pogodzić:

| MARKDOWN (LLM) | PYTHON |
|----------------|--------|
| Elastyczny, luźny zapis | Deterministyczny, strukturalny |
| "Otwórz plik, przeanalizuj, oceń" | `steps[0].status == "done"` |
| Łatwo zmienić - dopisz tekst | Wymaga parsowania |
| LLM rozumie kontekst | Kod potrzebuje schematu |

**Próby rozwiązania które NIE działają:**
- Parsować markdown → niedeterministyczne, LLM zgaduje
- Narzucić strukturę w markdown → tracimy elastyczność
- Dwa pliki (md + yaml) → rozjadą się, trudne w utrzymaniu

## Rozwiązanie: Atomowe zadania + Kontrakt na granicy

```
┌─────────────────────────────────────────────────────────────┐
│                      ŚWIAT LLM                              │
│                                                             │
│   Markdown jest ATOMOWY dla Pythona                         │
│   Python nie wie co jest w środku                           │
│   Python tylko ZLECA wykonanie                              │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │  analyze-config.md                                  │   │
│   │                                                     │   │
│   │  "Otwórz plik config.yaml, przeczytaj ustawienia,  │   │
│   │   przeanalizuj zgodność z best practices,          │   │
│   │   oceń ryzyko, przygotuj rekomendacje..."          │   │
│   │                                                     │   │
│   │  (Python tego NIE CZYTA)                           │   │
│   └─────────────────────────────────────────────────────┘   │
│                              │                              │
└──────────────────────────────┼──────────────────────────────┘
                               │
                               │ GRANICA
                               │ Tu powstaje KONTRAKT
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     ŚWIAT PYTHON                            │
│                                                             │
│   Python czyta TYLKO kontrakt - strukturalny, przewidywalny │
│                                                             │
│   ```yaml                                                   │
│   contract:                                                 │
│     task: analyze-config                                    │
│     source: analyze-config.md                               │
│     status: completed                                       │
│     output:                                                 │
│       type: report                                          │
│       file: reports/config-analysis.md                      │
│     next:                                                   │
│       - task: implement-fixes                               │
│         source: implement-fixes.md                          │
│   ```                                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Zasady

### 1. Markdown jest atomowy
- Python traktuje markdown jak czarną skrzynkę
- Nie próbuje parsować, analizować, rozumieć
- Tylko: "wykonaj ten.md" → "oto wynik"

### 2. Kontrakt powstaje na GRANICY
Kiedy LLM musi przekazać coś do Pythona:
- Generuje zadania do wykonania
- Zwraca wyniki które Python ma przetworzyć
- Tworzy kolejne kroki do orchestracji

### 3. LLM jest odpowiedzialny za kontrakt
- LLM czyta luźny markdown
- LLM wykonuje zadanie
- LLM **tworzy kontrakt** gdy wynik ma trafić do Pythona
- Kontrakt ma ustalony schemat (Python wie jak czytać)

### 4. Elastyczność zostaje zachowana
- Markdown piszesz po ludzku, bez ograniczeń
- Zmiany w markdown nie wymagają zmian w kontrakcie
- Kontrakt jest generowany dynamicznie przez LLM

## Schemat kontraktu

```yaml
# Minimalny kontrakt
contract:
  version: 1

  # Co zostało wykonane
  task:
    id: string
    source: path/to/markdown.md  # atomowe zadanie
    status: pending | running | completed | failed

  # Wejście (opcjonalne)
  input:
    - name: string
      value: any

  # Wyjście (gdy status=completed)
  output:
    type: report | data | artifact | tasks
    value: any

  # Następne zadania (gdy output.type=tasks)
  next:
    - task_id: string
      source: path/to/next.md
      depends_on: [task_ids]
      priority: number
```

## Przykłady użycia

### Python zleca wykonanie markdown
```python
# Python
result = llm.execute("processes/analyze-config.md", input={"file": "config.yaml"})

# LLM wykonuje markdown (atomowo)
# LLM zwraca kontrakt:
# {
#   "task": {"id": "analyze-1", "source": "...", "status": "completed"},
#   "output": {"type": "report", "value": "...analiza..."}
# }
```

### LLM generuje kolejne zadania
```python
# LLM po analizie decyduje że trzeba coś naprawić
# Generuje kontrakt z next:

# {
#   "task": {"id": "analyze-1", "status": "completed"},
#   "output": {"type": "tasks"},
#   "next": [
#     {"task_id": "fix-1", "source": "processes/fix-security.md"},
#     {"task_id": "fix-2", "source": "processes/fix-performance.md"}
#   ]
# }

# Python widzi next i może:
# - wyświetlić użytkownikowi
# - automatycznie zlecić wykonanie
# - zmienić kolejność
# - odrzucić niektóre
```

### Python orchestruje workflow
```python
def execute_workflow(entry_point_md):
    queue = [{"source": entry_point_md}]

    while queue:
        task = queue.pop(0)
        contract = llm.execute(task["source"])

        # Python śledzi postęp
        update_dashboard(contract)

        # Python decyduje o kolejnych krokach
        if contract.get("next"):
            for next_task in contract["next"]:
                if should_execute(next_task):  # Python może filtrować
                    queue.append(next_task)
```

## Korzyści

| Aspekt | Rozwiązanie |
|--------|-------------|
| Elastyczność markdown | ✓ Piszesz po ludzku, bez struktury |
| Python ma wgląd | ✓ Przez kontrakt, nie przez parsowanie markdown |
| Determinizm | ✓ Schemat kontraktu jest stały |
| Orchestracja | ✓ Python może zarządzać kolejnością, filtrować |
| Wizualizacja | ✓ Python czyta kontrakty i wyświetla dashboard |
| Raportowanie | ✓ Historia kontraktów = historia wykonania |

## Rozwiązanie: YAML Front Matter

Zamiast osobnych kontraktów - **nagłówek YAML w pliku markdown**:

```markdown
---
# KONTRAKT (Python czyta tę sekcję)
id: analyze-config
type: task
input:
  - name: config_file
    type: path
output:
  - name: report
    type: markdown
depends_on: []
---

# TREŚĆ (LLM wykonuje tę część)

Otwórz plik {config_file}, przeczytaj ustawienia,
przeanalizuj zgodność z best practices,
oceń ryzyko i przygotuj rekomendacje...

(tu piszesz po ludzku, elastycznie, bez ograniczeń)
```

### Dlaczego to działa

| Aspekt | Rozwiązanie |
|--------|-------------|
| Jeden plik | Kontrakt + treść razem - nie rozjadą się |
| Dual-read | Python czyta strukturę, LLM czyta instrukcję |
| LLM-native | Kontrakt jest częścią instrukcji dla LLM |
| Python-optional | LLM może działać samodzielnie bez orchestratora |
| Standard | YAML front matter to powszechny wzorzec (Jekyll, Hugo, Obsidian) |

### LLM czyta kontrakt jako instrukcję

```markdown
---
id: analyze-config
input: [config_file]      ← LLM: "mam użyć config_file"
output: [report]          ← LLM: "mam stworzyć report"
depends_on: [load-data]   ← LLM: "load-data musi być wcześniej"
---

Otwórz plik {config_file}...   ← LLM: wykonuję
```

LLM widzi CAŁY plik i rozumie kontekst:
- Co to za zadanie
- Czego potrzebuje
- Co ma wyprodukować
- Od czego zależy

**Kontrakt to nie metadane - to część instrukcji.**

### Dwa tryby działania

**TRYB 1: LLM samodzielnie (bez Pythona)**

```
┌─────────────────────────────────────────┐
│         MARKDOWN + KONTRAKT             │
│                                         │
│  ---                                    │
│  id: analyze-config                     │
│  input: [config_file]                   │
│  output: [report]                       │
│  ---                                    │
│                                         │
│  Otwórz {config_file}...                │
└─────────────────────────────────────────┘
                  │
                  ▼
            ┌───────────┐
            │    LLM    │  Czyta CAŁY plik
            │           │  Kontrakt = część instrukcji
            │           │  Wykonuje samodzielnie
            └───────────┘
```

**TRYB 2: Python jako orchestrator (opcjonalny)**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   PYTHON    │────▶│  MARKDOWN   │────▶│     LLM     │
│ (opcjonalny)│     │ + KONTRAKT  │     │             │
│             │     │             │     │ Czyta CAŁY  │
│ Czyta YAML  │     │ ---         │     │ plik jako   │
│ Buduje graf │     │ kontrakt    │     │ instrukcję  │
│ Orchestruje │     │ ---         │     │             │
│ Wizualizuje │     │ treść...    │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
```

**Kluczowe:**
- LLM zawsze czyta CAŁY plik (kontrakt + treść)
- Kontrakt jest instrukcją dla LLM, nie tylko metadanymi
- Python czyta tylko YAML (struktura)
- Python jest OPCJONALNY - dodaje orchestrację, wizualizację

## KRYTYCZNE: Próg złożoności

```
⚠️  STABILITY BASIN WARNING

Kontrakt musi być PROSTY.
Złożoność kontraktu +50-70% = system traci stabilność.

✓ DOBRY kontrakt:              ✗ ZŁY kontrakt:

---                            ---
id: task-1                     id: task-1
input: [config_file]           input:
output: [report]                 - name: config_file
depends_on: []                     type: path
---                                validation: [...]
                               output:
                                 - name: report
                                   type: markdown
                                   schema: {...}
                               depends_on:
                                 hard: [task-0]
                                 soft: [task-x]
                               retry_policy:
                                 max_attempts: 3
                                 backoff: exponential
                               error_handling:
                                 on_fail: [...]
                               validation:
                                 pre: [...]
                                 post: [...]
                               ---

Prosty kontrakt = stabilny system
Złożony kontrakt = kaskada problemów przy każdej zmianie
```

### Minimalistyczny schemat kontraktu

```yaml
---
# WYMAGANE
id: string              # unikalny identyfikator
type: task | process    # atomowe zadanie lub orchestracja

# OPCJONALNE (tylko gdy potrzebne)
input: [string]         # lista nazw parametrów wejściowych
output: [string]        # lista nazw wyników
depends_on: [id]        # lista ID zadań które muszą być wcześniej
---
```

**Zasada:** Dodawaj pola tylko gdy są NIEZBĘDNE. Domyślnie - minimum.

## Rozwiązania otwartych pytań

### 1. Jak obsługiwać wyniki LLM?

**Rozwiązanie: Konwencja katalogów + automatyczne nazewnictwo**

```
.output/
  {task_id}/
    {output_name}.md

Przykład:
.output/
  analyze-config/
    report.md
  fix-security/
    patch.md
    notes.md
```

- Python kontroluje GDZIE (struktura katalogów)
- LLM kontroluje CO (treść)
- Przewidywalna lokalizacja = łatwe do odczytu

### 2. Jak obsługiwać dynamiczne zadania?

**Rozwiązanie: Blok `spawn` w odpowiedzi LLM**

Gdy LLM odkryje że trzeba wykonać dodatkowe zadanie:

```markdown
[odpowiedź LLM]

Podczas analizy znalazłem krytyczną lukę bezpieczeństwa.
Wymagana natychmiastowa naprawa.

~~~spawn
---
id: fix-security-issue
type: task
input: [vulnerability_report]
output: [patch]
priority: high
---

Na podstawie raportu {vulnerability_report} przygotuj patch
który naprawi znalezioną lukę...
~~~
```

- Python parsuje odpowiedź LLM
- Wykrywa blok `spawn`
- Tworzy nowy plik markdown z kontraktem
- Dodaje do kolejki wykonania

### 3. Wersjonowanie kontraktów?

**Rozwiązanie: Minimalizm eliminuje problem**

```yaml
# Schemat jest tak prosty że nie wymaga wersjonowania
---
id: string
type: task | process
input: [string]      # opcjonalne
output: [string]     # opcjonalne
depends_on: [string] # opcjonalne
---
```

- 5 pól = brak potrzeby wersji
- Nowe pola = zawsze opcjonalne z domyślną wartością
- Backward compatibility przez prostotę, nie przez mechanizm wersji

**Zasada:** Jeśli potrzebujesz wersjonowania kontraktu, kontrakt jest za złożony.

## Architektura - podsumowanie

```
┌─────────────────────────────────────────────────────────────────┐
│                      PYTHON ORCHESTRATOR                        │
│                                                                 │
│  1. Skanuje katalog processes/ → znajduje pliki .md             │
│  2. Parsuje YAML front matter → buduje graf zależności          │
│  3. Wykonuje w kolejności (topological sort)                    │
│  4. Dla każdego zadania:                                        │
│     a) Czyta markdown                                           │
│     b) Zleca LLM wykonanie                                      │
│     c) Parsuje odpowiedź (szuka bloków spawn)                   │
│     d) Zapisuje output do .output/{id}/                         │
│     e) Jeśli spawn → tworzy nowe zadanie → dodaje do grafu      │
│  5. Raportuje postęp                                            │
└─────────────────────────────────────────────────────────────────┘

Pliki:
  processes/
    analyze-config.md     # zadanie z kontraktem
    generate-report.md    # zadanie z kontraktem
    ...

  .output/
    analyze-config/
      report.md           # wynik LLM
    generate-report/
      final-report.md     # wynik LLM

  .state/
    execution.yaml        # stan wykonania (który task done/pending)
```
