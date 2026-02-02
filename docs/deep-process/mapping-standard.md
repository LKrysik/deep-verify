# Standard Mapowania Procesów na Deep Process v2

> **Cel:** Instrukcja jak przekształcić dowolny proces biznesowy (Agile, Waterfall, UX, tworzenie dokumentacji) na format zrozumiały dla silnika Deep Process oraz możliwy do wykonania samodzielnie przez LLM.

---

## 1. Filozofia: Atomowość i Samowystarczalność

Każdy proces musi zostać rozbity na **Atomowe Kroki**.
*   **Atomowy Krok:** To najmniejsza sensowna jednostka pracy, która daje wymierny rezultat (artefakt). Np. "Stwórz User Story" to atom. "Stwórz system" to nie atom.
*   **Samowystarczalność:** Plik kroku musi zawierać WSZYSTKIE informacje potrzebne do jego wykonania. Nie może polegać na "wiedzy plemiennej" lub zewnętrznych dokumentach, których nie ma w `inputs`.

---

## 2. Struktura Katalogów

Każdy proces to osobny katalog w `src/core/deep-process/processes/`.

```
nazwa-procesu/
├── process.yaml            # Manifest główny (Metadane procesu)
├── schemas/                # Schematy artefaktów (Output Contracts)
│   ├── artifact_type_A.yaml
│   └── artifact_type_B.yaml
└── phases/                 # Fazy procesu
    ├── 1-nazwa-fazy/
    │   ├── 1.1-nazwa-kroku.md
    │   └── 1.2-nazwa-kroku.md
    └── 2-nazwa-fazy/
        └── ...
```

---

## 3. Szablon Pliku Kroku (.md)

Każdy plik kroku MUSI mieć taką strukturę. To jest nasz **Standard**.

```markdown
---
# KONTRAKT DLA SILNIKA (I METADANE DLA LLM)
id: unikalne-id-kroku
name: "Czytelna nazwa kroku dla człowieka"
type: step  # step | gate | loop
inputs:
  - artifacts/sciezka/do/wejscia.md
outputs:
  - artifacts/sciezka/do/wyjscia.md
output_contract: nazwa_schematu  # np. 'story', 'epic'
context_menu: "Gdzie to pokazać w menu?" # np. "Active Epics" (opcjonalne)
---

# {Nazwa Kroku}

## Cel
Jedno zdanie: Po co to robimy?

## Kontekst
Opis sytuacji. LLM musi wiedzieć, w jakiej roli występuje (np. "Jesteś Product Ownerem").

## Instrukcje
Krok po kroku, co należy zrobić.
1. Przeanalizuj wejście...
2. Zastanów się nad...
3. Wygeneruj...

## Interakcja z Użytkownikiem
Jasne wytyczne, kiedy LLM ma się zatrzymać i o co zapytać.
*   "Zanim wygenerujesz plik, zapytaj użytkownika o priorytety."
*   "Jeśli brakuje informacji X, poproś użytkownika o jej uzupełnienie."

## Kryteria Weryfikacji (Quality Gate)
Lista kontrolna, którą LLM ma sprawdzić przed uznaniem zadania za gotowe.
- [ ] Czy format jest zgodny ze schematem?
- [ ] Czy wszystkie sekcje są wypełnione?
- [ ] Czy język jest zrozumiały?

## Wymagania Wyjściowe
Ścisłe techniczne wymagania co do formatu pliku wynikowego (np. "Musi być valid YAML").
```

---

## 4. Procedura Mapowania (Jak to robić?)

Jeśli masz nowy proces (np. "Tworzenie UX"), wykonaj te kroki:

1.  **Dekompozycja:** Wypisz na kartce wszystkie czynności.
2.  **Grupowanie:** Podziel czynności na Fazy (np. Research, Design, Test).
3.  **Atomizacja:** Każdą czynność zamień na jeden plik `.md` wg szablonu powyżej.
4.  **Definicja Przepływu:** Ustal, co jest wejściem (`inputs`), a co wyjściem (`outputs`) każdego kroku. To połączy kropki.
5.  **Definicja Kontraktów:** Stwórz pliki `.yaml` w katalogu `schemas/`, opisujące jak mają wyglądać wyniki (np. `persona.schema.yaml`).

---

## 5. Obsługa Wariantów

*   **Warianty:** Jeśli krok może być wykonany na różne sposoby (np. "Szybki szkic" vs "Pełna makieta"), stwórz dwa osobne pliki kroków lub obsłuż to wewnątrz jednego pliku w sekcji "Instrukcje" (np. "Jeśli użytkownik chce szybko...").
*   **Decyzje:** Jeśli krok wymaga decyzji (Bramka), użyj typu `type: gate` w kontrakcie.

---

## 6. Rozszerzalność

Jeśli potrzebujesz specjalnej obsługi (np. uruchomienie skryptu Python):
1.  Dodaj nowe pole do YAML w kontrakcie (np. `validator: scripts/check_ux.py`).
2.  Silnik (jeśli go używasz) może to obsłużyć.
3.  Samodzielny LLM to zignoruje (co jest bezpieczne).
