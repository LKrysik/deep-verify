# Deep Process Engine

> **Wersja:** 1.0
> **Cel:** Meta-framework do definiowania i wykonywania procesów przez agenta AI.
> **Filozofia:** Agent AI podąża za procesem, stan jest śledzony automatycznie, a niewiadome są aktywnie odkrywane.

---

## Przeznaczenie

`Deep Process` to generyczny silnik wykonawczy, który umożliwia agentowi AI (LLM) niezawodne przeprowadzanie złożonych, wieloetapowych procesów. Działa jak system operacyjny, który dostarcza reguły, zarządza stanem i wykonuje kroki zdefiniowane w plikach procesów.

W przeciwieństwie do specyficznych metodyk, ten silnik może uruchomić dowolny proces, który jest zdefiniowany zgodnie z jego architekturą.

---

## Dostępne Procesy

| Proces | Domena | Fazy | Zastosowanie |
|---|---|---|---|
| [project-management](processes/project-management.md) | Zarządzanie projektem | 6 | Budowa oprogramowania z epikami i historyjkami |
| [ux-design](processes/ux-design.md) | Projektowanie UX | 6 | Projektowanie doświadczeń użytkownika |
| [code-documentation](processes/code-documentation.md) | Dokumentacja | 5 | Dokumentowanie istniejącej bazy kodu |
| [custom-template](processes/custom-template.md) | Dowolna | N | Tworzenie własnego, niestandardowego procesu |

---

## Architektura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DEEP PROCESS ENGINE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ENGINE (Jak wykonywać)               PROCESSES (Co wykonywać)              │
│  ├── executor.md                      ├── project-management.md             │
│  ├── enforcer.md                      ├── ux-design.md                      │
│  ├── state-manager.md                 ├── code-documentation.md             │
│  ├── unknown-detector.md              └── custom-template.md                │
│  └── integrations/                                                          │
│      ├── azure-devops.md              SCHEMAS (Walidacja)                   │
│      └── github.md                    ├── epic.schema.yaml                  │
│                                       ├── story.schema.yaml                 │
│                                       └── sprint.schema.yaml                │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STATE (.state/)                      ARTIFACTS (artifacts/)                │
│  ├── process.yaml (konfiguracja)      ├── idea.md                           │
│  ├── phase.yaml (gdzie jesteśmy)      ├── prd.md                            │
│  ├── items.yaml (epiki, historyjki)   ├── epics/*.yaml                      │
│  ├── decisions.yaml (decyzje)         ├── stories/*.yaml                    │
│  ├── unknowns.yaml (niewiadome)       └── ...                               │
│  └── history.yaml (audyt)                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Kluczowe Koncepty

### 1. Fazy i Bramki (Phases and Gates)

Każdy proces jest podzielony na uporządkowane fazy. Nie można ich pomijać. Pomiędzy fazami znajdują się **bramki** (gates) z kryteriami weryfikacji, które trzeba spełnić, aby przejść dalej.

```
Faza 1 ──[Bramka, próg: 0.70]──▶ Faza 2 ──[Bramka, próg: 0.85]──▶ Faza 3
```

### 2. Śledzenie Stanu (State Tracking)

Cały stan projektu jest jawnie przechowywany w plikach YAML w katalogu `.state/`. Agent AI automatycznie odczytuje i aktualizuje te pliki, dzięki czemu praca może być wznawiana, a postęp jest zawsze widoczny.

### 3. Egzekwowanie Reguł (Enforcement)

Agent AI **musi** przestrzegać reguł zdefiniowanych w pliku `engine/enforcer.md`. Gwarantuje to, że proces jest wykonywany poprawnie – bez pomijania kroków, ignorowania blokerów czy naruszania zależności.

### 4. Wykrywanie Niewiadomych (Unknown Unknowns)

Silnik, za pomocą `engine/unknown-detector.md`, aktywnie skanuje artefakty w poszukiwaniu ukrytych założeń, luk w logice i potencjalnych ryzyk, o których zespół mógł nie pomyśleć.

### 5. Integracje

System może opcjonalnie synchronizować postęp prac z zewnętrznymi narzędziami, takimi jak Azure DevOps czy GitHub, co pozwala na płynną integrację z istniejącymi przepływami pracy.

---

## Jak to działa?

1.  **Inicjalizacja:** Użytkownik wybiera proces (np. `project-management`), a system tworzy początkowy stan w katalogu `.state/`.
2.  **Pętla Wykonania:**
    a. Agent odczytuje aktualny stan i definicję procesu.
    b. Na podstawie reguł i stanu, rekomenduje następny krok.
    c. Po potwierdzeniu przez użytkownika, wykonuje krok, ściśle przestrzegając reguł z `enforcer.md`.
    d. Po wykonaniu kroku aktualizuje pliki stanu.
    e. Prezentuje użytkownikowi podsumowanie i nową rekomendację.
3.  **Weryfikacja:** Przed przejściem do kolejnej fazy, uruchamiana jest procedura weryfikacji (bramka), która ocenia, czy dotychczasowe artefakty spełniają określone kryteria jakości.

Dzięki takiemu podejściu, `Deep Process` przekształca LLM z narzędzia do generowania tekstu w niezawodnego partnera do realizacji skomplikowanych zadań.