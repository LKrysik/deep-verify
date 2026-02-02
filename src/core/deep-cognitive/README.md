# Deep Cognitive

Ten katalog zawiera pliki definiujące **"architekturę poznawczą"** dla agenta AI, którego zadaniem jest prowadzenie projektów programistycznych. Można to rozumieć jako **system operacyjny dla dewelopera AI**.

## Główne Cele

1.  **Strukturyzacja Procesu:** Prowadzi projekt przez zdefiniowane fazy:
    `Pomysł` → `Specyfikacja` → `Architektura` → `Implementacja` → `Testowanie` → `Ukończenie`.

2.  **Zarządzanie Stanem:** Utrzymuje centralny, spójny stan projektu w pliku `.deep/project-state.yaml`. Dzięki temu agent zawsze wie, na jakim etapie jest praca, co blokuje postęp i jakie decyzje zostały podjęte.

3.  **Aktywne Odkrywanie Niewiadomych:** Posiada wbudowany mechanizm (`meta-cognitive/unknown-detector.yaml`) do proaktywnego wyszukiwania "niewiadomych niewiadomych" (unknown unknowns). Jego celem jest identyfikacja ryzyk, ukrytych założeń i luk w wiedzy, zanim staną się one problemem.

4.  **Weryfikacja Jakości:** Na końcu każdej fazy znajdują się "bramki weryfikacyjne" (obsługiwane przez operację `deep-verify`), które sprawdzają, czy artefakty (np. dokumentacja, specyfikacja) są wystarczająco dojrzałe i spójne, aby bezpiecznie przejść do następnego etapu.

5.  **Automatyzacja i Wsparcie Decyzji:** Agent, korzystając z "planera" (`meta-cognitive/planner-rules.yaml`), autonomicznie sugeruje kolejne kroki i operacje. Wszystkie ważne decyzje architektoniczne są zapisywane w ustrukturyzowany sposób jako `Architecture Decision Records` (ADR).

## Struktura Katalogu

-   `workflow.md`: Główny dokument opisujący całościowy przepływ pracy i interakcje.
-   `.deep/`: Katalog przechowujący stan "na żywo" projektu, w tym zadania, pamięć agenta i ślady jego rozumowania.
-   `meta-cognitive/`: "Mózg" systemu, zawierający logikę planowania, orkiestracji sesji i wykrywania niewiadomych.
-   `operations/`: Konkretne "umiejętności" lub procesy, które agent może wykonywać, np. `deep-challenge` (klaryfikacja pomysłu) czy `deep-verify` (weryfikacja bramki).

W skrócie, **Deep Cognitive** to zaawansowana metodyka, która narzuca rygor i dyscyplinę w procesie tworzenia oprogramowania przy pomocy AI, minimalizując ryzyko i zwiększając przewidywalność projektu.
