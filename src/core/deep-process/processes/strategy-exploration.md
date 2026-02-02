# Process: Strategy Exploration

> **ID:** strategy-exploration
> **Version:** 1.0
> **Domain:** Strategic Management & Decision Making
> **Goal:** Transform a complex problem or a high-stakes question into a well-understood decision space, a clear choice, and an actionable plan.

---

## METADATA

```yaml
id: strategy-exploration
version: "1.0"
domain: strategic-management

phases:
  - framing
  - exploration
  - decision
  - planning
  - review
```

---

## ENFORCEMENT

> **WAŻNE:** Przed wykonaniem CZEGOKOLWIEK przeczytaj `engine/enforcer.md`

### Reguły specyficzne dla tego procesu

```yaml
rules:
  - rule: "No exploration without a clear problem"
    check: "artifacts/strategy/problem-definition.md must exist before exploration phase"
    on_violation: BLOCK

  - rule: "No decision without an exploration report"
    check: "artifacts/strategy/exploration-report.md must exist before decision phase"
    on_violation: BLOCK

  - rule: "No plan without a decision"
    check: "artifacts/strategy/decision-record.md must exist before planning phase"
    on_violation: BLOCK
```

---

## PHASE 1: FRAMING

### Purpose
Precyzyjnie zdefiniować problem decyzyjny, pytanie strategiczne oraz określić wagę (stawkę) decyzji.

### Entry Conditions
```yaml
requires:
  state:
    - "Project initialized"
```

### Steps

#### Step 1.1: Define Problem

```yaml
id: define-problem
name: "Define the strategic problem"

produces:
  artifacts:
    - path: "artifacts/strategy/problem-definition.md"

instructions: |
  1. Wezwij użytkownika do opisania problemu, pytania lub decyzji do podjęcia.
  2. Użyj pytań sondujących, aby skrystalizować problem w jedno, klarowne zdanie.
     - "Jaka jest najważniejsza decyzja, którą musimy podjąć?"
     - "Co się stanie, jeśli nie podejmiemy tej decyzji?"
     - "Jak będzie wyglądał sukces?"
  3. Określ wagę (stawkę) decyzji: Niska, Średnia, Wysoka.
  4. Zapisz wszystko w `artifacts/strategy/problem-definition.md`.

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: framing_to_exploration

```yaml
gate:
  name: framing_to_exploration
  threshold: 0.80

  criteria:
    - name: "Problem clearly stated"
      weight: 0.60
      check: "Problem statement is a single, unambiguous sentence."

    - name: "Stakes assessed"
      weight: 0.40
      check: "Decision stakes (Low/Medium/High) are documented."
```

---

## PHASE 2: EXPLORATION

### Purpose
Systematycznie zbadać przestrzeń decyzyjną, zmapować opcje, konsekwencje i niewiadome przy użyciu metodologii **Deep Explore**.

### Entry Conditions
```yaml
requires:
  gates:
    - "framing_to_exploration: passed"
  artifacts:
    - "artifacts/strategy/problem-definition.md"
```

### Steps

#### Step 2.1: Run Deep Explore

```yaml
id: run-deep-explore
name: "Execute the Deep Explore process"
operation: deep-explore # This is the core of this process

requires:
  artifacts:
    - "artifacts/strategy/problem-definition.md"

produces:
  artifacts:
    - path: "artifacts/strategy/exploration-report.md"

instructions: |
  1. **Uruchom proces `@src/core/deep-explore/workflow.md`**.
  2. Wczytaj `problem-definition.md` jako główne wejście (decyzja do eksploracji).
  3. Wybierz głębokość eksploracji (Quick/Standard/Deep) na podstawie stawki określonej w poprzedniej fazie. Dla stawki Średniej/Wysokiej, użyj minimum "Standard".
  4. Postępuj zgodnie ze wszystkimi krokami `deep-explore`: Knowledge Audit -> Research -> Map -> Deepen -> Challenge -> Synthesize.
  5. Wygeneruj kompletny `EXPLORATION REPORT` i zapisz go jako `artifacts/strategy/exploration-report.md`.

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: exploration_to_decision

```yaml
gate:
  name: exploration_to_decision
  threshold: 0.75

  criteria:
    - name: "Exploration report exists"
      weight: 0.50
      check: "artifacts/strategy/exploration-report.md exists."

    - name: "Exploration coverage is adequate"
      weight: 0.50
      check: "Report coverage score is 'ADEQUATE' or 'COMPREHENSIVE'."
```

---

## PHASE 3: DECISION

### Purpose
Przeanalizować wyniki eksploracji i podjąć formalną, udokumentowaną decyzję.

### Entry Conditions
```yaml
requires:
  gates:
    - "exploration_to_decision: passed"
  artifacts:
    - "artifacts/strategy/exploration-report.md"
```

### Steps

#### Step 3.1: Make and Document Decision

```yaml
id: make-decision
name: "Make and document the final decision"

requires:
  artifacts:
    - "artifacts/strategy/exploration-report.md"

produces:
  artifacts:
    - path: "artifacts/strategy/decision-record.md"
  state:
    - "decisions in .state/decisions.yaml"

instructions: |
  1. Zaprezentuj użytkownikowi kluczowe wnioski z raportu eksploracji, w szczególności "Strategic Clusters" i "Consequence Map".
  2. Poproś o podjęcie ostatecznej decyzji.
  3. Stwórz `decision-record.md`, dokumentując:
     - Wybraną opcję.
     - Kluczowe uzasadnienie (rationale) oparte na raporcie.
     - Główne odrzucone opcje i powody ich odrzucenia.
     - Zidentyfikowane ryzyka i plan ich mitygacji.
  4. Dodaj wpis do `.state/decisions.yaml`.

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: decision_to_planning

```yaml
gate:
  name: decision_to_planning
  threshold: 0.80
  criteria:
    - name: "Decision is documented"
      weight: 0.50
      check: "decision-record.md exists and is complete."
    - name: "Rationale is clear"
      weight: 0.50
      check: "Rationale links back to findings from the exploration report."
```

---

## PHASE 4: PLANNING

### Purpose
Przekształcić podjętą decyzję w konkretny, wysokopoziomowy plan działania.

### Entry Conditions
```yaml
requires:
  gates:
    - "decision_to_planning: passed"
  artifacts:
    - "artifacts/strategy/decision-record.md"
```

### Steps

#### Step 4.1: Create Action Plan

```yaml
id: create-action-plan
name: "Create a high-level action plan"

requires:
  artifacts:
    - "artifacts/strategy/decision-record.md"

produces:
  artifacts:
    - path: "artifacts/strategy/action-plan.md"

instructions: |
  1. Na podstawie `decision-record.md`, zidentyfikuj główne strumienie pracy lub kolejne kroki.
  2. Utwórz plan działania w `action-plan.md`, zawierający:
     - Listę głównych zadań, epików lub projektów do uruchomienia.
     - Proponowaną kolejność i zależności.
     - Wskaźniki sukcesu (KPIs) do monitorowania postępów.
     - Wstępne oszacowanie zasobów (jeśli możliwe).

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: planning_to_review

```yaml
gate:
  name: planning_to_review
  threshold: 0.70
  criteria:
    - name: "Action plan exists"
      weight: 0.50
      check: "action-plan.md exists."
    - name: "Plan is aligned with decision"
      weight: 0.50
      check: "All items in the action plan directly support the documented decision."
```

---

## PHASE 5: REVIEW

### Purpose
Przeprowadzić ostateczny przegląd spójności całego procesu strategicznego przed przekazaniem do wykonania.

### Entry Conditions
```yaml
requires:
  gates:
    - "planning_to_review: passed"
```

### Steps

#### Step 5.1: Final Review

```yaml
id: final-review
name: "Final consistency review"

requires:
  artifacts:
    - "artifacts/strategy/problem-definition.md"
    - "artifacts/strategy/exploration-report.md"
    - "artifacts/strategy/decision-record.md"
    - "artifacts/strategy/action-plan.md"

instructions: |
  1. Sprawdź, czy istnieje logiczna ciągłość między wszystkimi artefaktami.
     - Czy `decision-record.md` faktycznie odpowiada na pytanie z `problem-definition.md`?
     - Czy `action-plan.md` jest realistyczną implementacją podjętej decyzji?
     - Czy kluczowe ryzyka z `exploration-report.md` są zaadresowane w planie?
  2. Zgłoś wszelkie niespójności. Jeśli wszystko jest w porządku, zakończ proces.
```

### Exit Gate: process_complete

```yaml
gate:
  name: process_complete
  threshold: 0.90
  criteria:
    - name: "All artifacts are consistent"
      weight: 1.00
      check: "A full audit trail from problem to plan is clear and logical."
```

---

## ARTIFACTS SUMMARY

| Artifact | Phase | Purpose |
|---|---|---|
| problem-definition.md | Framing | Zdefiniowanie problemu i stawki |
| exploration-report.md | Exploration | Szczegółowa mapa przestrzeni decyzyjnej |
| decision-record.md | Decision | Formalne udokumentowanie wyboru i uzasadnienia |
| action-plan.md | Planning | Konkretne następne kroki |
