# Deep Explore Report: BMM Process Mapping Audit

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                           D E E P   E X P L O R E   R E P O R T                   ║
║                                    Wersja 3.0 (BMM Audit)                          ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  CEL:       Audyt i kompletne zmapowanie procesu BMM (Business Motivation Model)   ║
║             na architekturę Deep Process v2, przy użyciu metod kolaboracyjnych.    ║
║  METODY:    #4, #5, #6, #7, #8 (z methods.csv)                                     ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Sekcja 1: Zastosowanie Metod (Insights)

### Metoda 4: User Persona Focus Group
*   **Project Manager:** "Widzę wizję, ale gdzie są *Cele (Goals)* i *Strategie (Strategies)*? BMM to nie tylko wizja. Gdzie śledzę KPI?"
    *   **Wniosek:** Brakuje fazy `Strategy` i `Tactics` oraz artefaktów dla celów mierzalnych.
*   **Tech Lead:** "Fajnie, że jest wizja biznesowa, ale jak to się ma do architektury? Gdzie jest punkt styku, w którym Cele BMM zamieniają się w Wymagania Techniczne?"
    *   **Wniosek:** Brakuje jawnego kroku transformacji `BMM -> PRD`.
*   **Scrum Master:** "Proces wygląda na liniowy. BMM jest żywy. Co jeśli zmienia się strategia w trakcie sprintu?"
    *   **Wniosek:** Potrzebna jest pętla zwrotna (Loop) `Assess Impact of Change`, dostępna w menu kontekstowym.

### Metoda 5: Time Traveler Council
*   **Future-You:** "Patrzę na zakończony projekt. Mamy kod, ale nie wiemy *dlaczego* podjęliśmy pewne decyzje. `vision.md` to za mało. Brakuje `decision-log` połączonego z celami BMM."
    *   **Wniosek:** Każda decyzja architektoniczna powinna mieć link do `BMM Goal`, który wspiera.

### Metoda 6: Cross-Functional War Room
*   **Konflikt:** PM chce "Szybko", Tech Lead chce "Solidnie". BMM ma to rozwiązywać przez `Influencers` (Czynniki Wpływu) i `Assessments`.
    *   **Wniosek:** Brakuje kluczowego elementu BMM: `SWOT Analysis` (lub podobnej oceny wpływów), która uzasadnia wybory.

### Metoda 7: Mentor and Apprentice
*   **Pytanie Juniora:** "Szefie, w katalogu `1-definition` jest tylko `vision.md`. Gdzie mam wpisać, że konkurencja właśnie wypuściła X?"
    *   **Mentor:** "Och, zapomnieliśmy o `External Influencers`. Musimy dodać ten krok."

### Metoda 8: Good Cop / Bad Cop
*   **Bad Cop:** "Ten proces to wydmuszka. To nie jest BMM, to tylko plik tekstowy z życzeniami. Gdzie jest rygor? Gdzie `Ends` vs `Means`?"
*   **Good Cop:** "Struktura katalogów jest dobra. Mechanizm kontraktów pozwala nam to naprawić. Wystarczy dodać odpowiednie kroki i schematy."

---

## Sekcja 2: Zidentyfikowane Luki (Gaps)

Na podstawie audytu, obecne mapowanie BMM jest **niekompletne** w ok. 80%.

1.  **Brakujące Fazy:**
    *   **Assessment:** Analiza SWOT, Influencers (Wewnętrzne/Zewnętrzne).
    *   **Strategy:** Definicja Strategii i Taktyk (Means).
    *   **Goals:** Definicja Celów i Celów Operacyjnych (Ends).
2.  **Brakujące Artefakty (Schemas):**
    *   `goal.schema.yaml`
    *   `strategy.schema.yaml`
    *   `influencer.schema.yaml`
    *   `assessment.schema.yaml`
3.  **Brakujące Relacje:**
    *   Brak mapowania `Strategy -> Epic`. To jest "most" między biznesem a deweloperką.

---

## Sekcja 3: Kompletna Mapa BMM na Deep Process (Target State)

### Struktura Katalogów (Poprawiona)

```
processes/bmm/
├── process.yaml
├── schemas/
│   ├── vision.schema.yaml
│   ├── goal.schema.yaml        # NEW
│   ├── strategy.schema.yaml    # NEW
│   ├── influencer.schema.yaml  # NEW
│   └── assessment.schema.yaml  # NEW
├── phases/
│   ├── 1-ends/                 # Definicja "CO" (Wizja + Cele)
│   │   ├── 1.1-define-vision.md
│   │   └── 1.2-define-goals.md # NEW
│   ├── 2-means/                # Definicja "JAK" (Misja + Strategie)
│   │   ├── 2.1-define-mission.md
│   │   └── 2.2-define-strategies.md # NEW
│   ├── 3-assessment/           # Ocena Wpływów
│   │   ├── 3.1-identify-influencers.md # NEW
│   │   └── 3.2-swot-analysis.md # NEW
│   └── 4-realization/          # Most do IT
│       └── 4.1-map-strategy-to-epics.md # NEW
└── menus/
    └── main.yaml               # Z akcjami kontekstowymi dla każdego artefaktu
```

### Kluczowe Kontrakty (Przykłady)

**Krok 4.1: Map Strategy to Epics**
*   **Input:** `artifacts/bmm/strategies/*.md`
*   **Output:** `artifacts/epics/*.yaml`
*   **Context Menu:** "Active Strategies" -> "Create Epic from Strategy"
*   **Cel:** To jest punkt, w którym abstrakcyjny BMM zamienia się w konkretne zadanie dla zespołu dev.

---

## Sekcja 4: Plan Naprawczy

1.  **Rozszerzenie Schematów:** Stworzyć brakujące pliki YAML w `schemas/`.
2.  **Uzupełnienie Faz:** Stworzyć brakujące pliki `.md` w strukturze faz.
3.  **Aktualizacja Menu:** Dodać sekcje dla Celów i Strategii w `menus/main.yaml`.
4.  **Weryfikacja:** Uruchomić `verify` na nowej strukturze.
