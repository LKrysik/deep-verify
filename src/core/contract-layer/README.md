# Python-LLM Contract Layer

Warstwa kontraktu między Pythonem a LLM - wspólny mianownik w realizacji zadań.

## Kluczowa zasada

**Kontrakt jest CZĘŚCIĄ markdown, nie obok niego.**

```markdown
---
id: analyze-config
input: [config_file]
output: [report]
depends_on: []
---

Otwórz plik {config_file} i przeanalizuj...
```

| Czytelnik | Co widzi | Jak używa |
|-----------|----------|-----------|
| LLM | Cały plik | Kontrakt = instrukcja |
| Python | YAML header | Struktura, graf, status |

## Dwa tryby działania

### Tryb 1: LLM samodzielnie

```
MARKDOWN + KONTRAKT → LLM → wykonanie
```

LLM czyta cały plik jako instrukcję i wykonuje samodzielnie.

### Tryb 2: Python + LLM

```
Python → czyta YAML → orchestruje → LLM wykonuje
```

Python dodaje: kolejność, wizualizację, automatyzację.

## Schemat kontraktu

```yaml
---
# WYMAGANE
id: string              # unikalny identyfikator

# OPCJONALNE
type: task | process    # domyślnie: task
input: [string]         # parametry wejściowe
output: [string]        # nazwy wyników
depends_on: [id]        # zależności
---
```

**Zasada prostoty:** Kontrakt musi być minimalny. Złożoność +50-70% = system traci stabilność.

## Struktura katalogów

```
contract-layer/
├── processes/              # Procesy z kontraktami
│   └── code-review/       # Przykład: proces code review
│       ├── 01-analyze-changes.md
│       ├── 02-check-quality.md
│       ├── 03-check-security.md
│       └── 04-generate-verdict.md
│
├── tools/                  # Narzędzia Python
│   └── visualizer.py      # Wizualizacja grafu i statusu
│
├── integration-deep-process.md  # Integracja z Deep Process Engine
└── README.md              # Ten plik
```

## Użycie

### Wizualizacja

```bash
python tools/visualizer.py processes/code-review/
```

Output:
```
============================================================
  CONTRACT LAYER - DASHBOARD
============================================================

  Tasks: 4 total | 0 done | 0 running | 4 pending
  Progress: [░░░░] 0/4

  DEPENDENCY GRAPH:
  ----------------------------------------
  [analyze-changes]
    → [check-quality]
    → [check-security]
      → [generate-verdict]

  TASKS:
  ----------------------------------------
  ○ analyze-changes
  ○ check-quality ← [analyze-changes]
  ○ check-security ← [analyze-changes]
  ○ generate-verdict ← [check-quality, check-security]

============================================================
```

### Wykonanie przez LLM (samodzielnie)

Daj LLM plik markdown - wykona go jako instrukcję.

### Wykonanie przez Python + LLM

```python
from orchestrator import Orchestrator

orch = Orchestrator(
    processes_dir="processes/code-review",
    output_dir=".output"
)

results = orch.run(llm_executor=my_llm_function)
```

## Integracja z Deep Process Engine

Contract Layer integruje się z Deep Process Engine:

| Deep Process | Contract Layer |
|--------------|----------------|
| Phase | Zestaw procesów (katalog) |
| Gate | Proces walidacyjny |
| Story | Może być wykonana jako proces |
| Task | Pojedyncze zadanie z kontraktem |

Szczegóły: [integration-deep-process.md](integration-deep-process.md)

## Dynamiczne zadania (spawn)

LLM może generować nowe zadania w trakcie wykonania:

```markdown
[odpowiedź LLM]

Znalazłem problem bezpieczeństwa.

~~~spawn
---
id: fix-security-issue
input: [vulnerability]
output: [patch]
depends_on: [check-security]
---

Napraw znalezioną lukę...
~~~
```

Python wykrywa `spawn` i dodaje nowe zadanie do grafu.

## Zasady

1. **Jeden plik = jedna prawda** - kontrakt i treść razem
2. **Minimalizm** - tylko niezbędne pola w kontrakcie
3. **LLM-native** - kontrakt jest częścią instrukcji dla LLM
4. **Python-optional** - LLM może działać samodzielnie
5. **Determinizm** - Python czyta tylko strukturę YAML
