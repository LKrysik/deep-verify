# Deep Protocol v1: Self-Contained Markdown Processes

## 1. Filozofia: LLM jako Runtime, Markdown jako Kod
W tym modelu LLM (Claude, Gemini) nie jest tylko generatorem tekstu, ale **środowiskiem wykonawczym (Runtime)**. Pliki Markdown są "kodem źródłowym" procesu, który zawiera w sobie wszystko, co niezbędne do jego realizacji: meta-dane, instrukcje operacyjne (kernel) oraz logikę biznesową.

Python w tej architekturze jest warstwą opcjonalną (narzędziową), a procesy muszą być **samowystarczalne (self-contained)**.

## 2. Struktura Kontraktu Markdown (Deep Contract)

Każdy plik procesu `.md` musi posiadać trzy warstwy:

### A. Warstwa Interfejsu (YAML Frontmatter)
Definiuje wejścia, wyjścia i powiązania dla narzędzi zewnętrznych oraz dla samego LLM, aby wiedział, w jakim punkcie grafu się znajduje.
```yaml
---
id: string          # Unikalny identyfikator kroku
type: string        # Typ (step, gate, agent-process)
agent: string       # Rola/Persona wykonująca krok
inputs: [path]      # Pliki do wczytania przed startem
outputs: [path]     # Pliki, które MUSZĄ powstać lub zostać zmienione
next: id/phase      # Kolejny krok po sukcesie
---
```

### B. Warstwa Jądra (Kernel Layer)
Instrukcje systemowe dla LLM, jak ma zarządzać "sobą" i stanem projektu. To tutaj definiujemy, że LLM jest odpowiedzialny za pliki w `.state/`.
- **Zasada Autonomii:** LLM sam wykonuje `read_file` i `write_file`.
- **Zasada Stanu:** Każda zmiana w artefaktach musi zostać odnotowana przez LLM w `.state/phase.yaml` oraz `.state/items.yaml`.
- **Zasada Weryfikacji:** LLM przed zakończeniem sprawdza, czy spełnił warunki kontraktu z Frontmattera.

### C. Warstwa Aplikacyjna (Logic Layer)
Właściwe zadanie do wykonania (np. "Zdefiniuj Wizję", "Oceń Ryzyko"). Zawiera kroki biznesowe i Definition of Done.

## 3. Zarządzanie Stanem (LLM-Controlled State)

LLM nie czeka na skrypt Pythona, aby zaktualizować postęp. Wewnątrz instrukcji Markdown zawarty jest obowiązek:
1.  **Odczytu stanu:** `read_file .state/phase.yaml`.
2.  **Logiki zmiany:** Obliczenie nowego `phase_progress`.
3.  **Zapisu stanu:** `write_file .state/phase.yaml` (lub `replace`).
4.  **Rejestracji artefaktów:** Dodanie ścieżki nowego pliku do `current_artifacts`.

## 4. Przykład: Samowystarczalny Krok BMM

```markdown
---
id: define-vision
agent: business-architect
inputs: []
outputs: ["artifacts/bmm/vision.md", ".state/phase.yaml"]
---

# KERNEL
Jesteś autonomicznym agentem Deep Process.
1. Wykonaj zadanie biznesowe.
2. Zaktualizuj stan w .state/phase.yaml ustawiając status na "completed".
3. Użyj narzędzi CLI do manipulacji plikami.

# ZADANIE
Zdefiniuj Wizję biznesową zgodnie z modelem BMM...
...
```

## 5. Rola Narzędzi CLI (Python/Bash)
Narzędzia CLI (np. `dp.py` lub natywne komendy gemini-cli) pełnią rolę **Context Injectors**:
- Wczytują plik `.md`.
- Na podstawie sekcji `inputs` doczytują treść innych plików.
- Przesyłają tak przygotowany, "napuchnięty" kontekst do LLM.
- LLM wykonuje resztę autonomicznie.
