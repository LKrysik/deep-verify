# Deep Process Engine — Enforcer

> **Cel:** Reguły które LLM MUSI przestrzegać
> **Priorytet:** Ten plik ma wyższy priorytet niż definicje procesów
> **Zasada:** Jeśli nie możesz wykonać — STOP i wyjaśnij, nigdy nie kontynuuj

---

## 1. FUNDAMENTALNE ZASADY

### 1.1 Zasada STOP

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ZASADA STOP                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Jeśli COKOLWIEK z poniższych jest prawdą:                                 │
│                                                                             │
│  • Warunek wstępny nie jest spełniony                                      │
│  • Wymagany artefakt nie istnieje                                          │
│  • Blocker jest aktywny                                                    │
│  • Gate nie został przejściowy                                             │
│  • Stan jest niespójny                                                     │
│                                                                             │
│  → STOP                                                                     │
│  → WYJAŚNIJ co jest nie tak                                                │
│  → ZAPROPONUJ rozwiązanie                                                  │
│  → CZEKAJ na użytkownika                                                   │
│                                                                             │
│  NIGDY nie kontynuuj "na ślepo"                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Zasada TRANSPARENCY

```
Wszystko co robisz MUSI być widoczne dla użytkownika:

✅ TAK:
- "Sprawdzam czy artifacts/prd.md istnieje..."
- "Warunek niespełniony: brakuje architecture.md"
- "Aktualizuję .state/phase.yaml..."

❌ NIE:
- Pomijanie kroków bez informacji
- Zakładanie że "pewnie jest ok"
- Ukrywanie błędów lub problemów
```

### 1.3 Zasada ATOMICITY

```
JEDNA AKCJA = JEDEN KROK

❌ NIE:
"Tworzę wszystkie epics i stories naraz"

✅ TAK:
"Tworzę EPIC-001..."
"Tworzę EPIC-002..."
"Tworzę STORY-001 dla EPIC-001..."
```

---

## 2. MANDATORY CHECKS

### 2.1 PRZED każdą akcją

```markdown
## CHECKLIST: Pre-Action

Przed KAŻDĄ akcją procesową MUSISZ sprawdzić:

□ 1. STATE LOADED
     Czy wczytałeś .state/phase.yaml?
     → Jeśli NIE: wczytaj najpierw

□ 2. PHASE ALLOWS
     Czy obecna faza pozwala na tę akcję?
     → Sprawdź: czy akcja jest w current_phase.steps?
     → Jeśli NIE: STOP "Ta akcja należy do fazy X, jesteś w fazie Y"

□ 3. PRECONDITIONS MET
     Czy warunki wstępne spełnione?
     → Sprawdź: step.requires.artifacts — czy istnieją?
     → Sprawdź: step.requires.state — czy spełnione?
     → Jeśli NIE: STOP "Brakuje: [lista]"

□ 4. NO BLOCKERS
     Czy coś blokuje tę akcję?
     → Sprawdź: .state/phase.yaml → blocking_items
     → Jeśli TAK: STOP "Zablokowane przez: [blocker]"

□ 5. NOT SKIPPING GATE
     Czy nie próbujesz przeskoczyć gate?
     → Sprawdź: czy poprzednia faza ma status: completed?
     → Jeśli NIE: STOP "Najpierw przejdź gate [gate_name]"
```

### 2.2 PO każdej akcji

```markdown
## CHECKLIST: Post-Action

Po KAŻDEJ udanej akcji MUSISZ:

□ 1. VERIFY OUTPUT
     Czy wynik jest poprawny?
     → Plik utworzony?
     → Format poprawny?
     → Zawartość sensowna?

□ 2. UPDATE STATE
     Czy zaktualizowałeś stan?
     → .state/phase.yaml — progress, last_action
     → .state/items.yaml — jeśli dodano item
     → .state/history.yaml — append wpisu

□ 3. NO DANGLING STATE
     Czy stan jest spójny?
     → Artefakty w state odpowiadają plikom na dysku?
     → Numery ID są unikalne?
     → Referencje są poprawne?

□ 4. REPORT
     Czy użytkownik wie co się stało?
     → Raport sukcesu
     → Następny krok
```

---

## 3. FORBIDDEN ACTIONS

### 3.1 NIGDY nie rób

```yaml
forbidden:
  - action: "Skip phase"
    reason: "Fazy muszą być wykonane w kolejności"
    enforcement: "Sprawdź current_phase przed akcją"

  - action: "Skip gate"
    reason: "Gate musi być przejdziany przed następną fazą"
    enforcement: "Sprawdź phase.status przed zmianą fazy"

  - action: "Create without update state"
    reason: "Stan musi odzwierciedlać rzeczywistość"
    enforcement: "ZAWSZE aktualizuj stan po utworzeniu"

  - action: "Proceed when blocked"
    reason: "Blokery muszą być rozwiązane"
    enforcement: "Sprawdź blocking_items przed akcją"

  - action: "Assume without verification"
    reason: "Zakładanie prowadzi do błędów"
    enforcement: "ZAWSZE sprawdź pliki zanim powiesz że istnieją"

  - action: "Silent failure"
    reason: "Użytkownik musi wiedzieć o problemach"
    enforcement: "ZAWSZE raportuj błędy jawnie"

  - action: "Modify state before success"
    reason: "Stan musi być spójny"
    enforcement: "NAJPIERW wykonaj, POTEM aktualizuj stan"
```

### 3.2 Czerwone flagi

```markdown
## RED FLAGS — Jeśli widzisz te wzorce, STOP

🚩 "Zakładam że plik istnieje..." → SPRAWDŹ
🚩 "Pewnie możemy pominąć..." → NIE MOŻESZ
🚩 "To chyba jest ok..." → ZWERYFIKUJ
🚩 "Później zaktualizuję stan..." → TERAZ
🚩 "User pewnie chce..." → ZAPYTAJ
```

---

## 4. PHASE ENFORCEMENT

### 4.1 Kolejność faz

```yaml
phase_rules:
  - rule: "SEQUENTIAL"
    meaning: "Fazy muszą być wykonane w kolejności"
    check: "previous_phase.status == completed"

  - rule: "GATE_REQUIRED"
    meaning: "Między fazami musi być gate"
    check: "gate.status == passed"

  - rule: "NO_REGRESSION"
    meaning: "Nie można cofać fazy bez powodu"
    exception: "User explicitly requests"
```

### 4.2 Weryfikacja fazy

```markdown
## INSTRUKCJA: Sprawdzenie czy mogę wykonać akcję w fazie X

1. Wczytaj .state/phase.yaml
2. Porównaj current_phase z fazą akcji:

   JEŚLI akcja.phase == current_phase:
   → DOZWOLONE (kontynuuj weryfikację)

   JEŚLI akcja.phase == current_phase + 1:
   → Sprawdź czy gate przeszedł
   → JEŚLI gate.passed: DOZWOLONE
   → JEŚLI NIE: STOP "Najpierw przejdź gate"

   JEŚLI akcja.phase > current_phase + 1:
   → STOP "Nie można przeskakiwać faz"

   JEŚLI akcja.phase < current_phase:
   → WARN "Cofasz się do poprzedniej fazy?"
   → Poproś o potwierdzenie
```

---

## 5. ARTIFACT ENFORCEMENT

### 5.1 Wymagane artefakty

```markdown
## INSTRUKCJA: Sprawdzenie artefaktów

Dla każdego step.requires.artifacts:

1. Sprawdź czy plik istnieje (Read tool lub Bash ls)
2. JEŚLI nie istnieje:
   → STOP
   → Raportuj: "Brakuje artefaktu: [path]"
   → Zaproponuj: "Najpierw wykonaj [step który tworzy artefakt]"
```

### 5.2 Tworzenie artefaktów

```markdown
## INSTRUKCJA: Tworzenie artefaktu

1. PRZED tworzeniem:
   - Sprawdź czy parent directory istnieje
   - Sprawdź czy nie nadpiszesz istniejącego (WARN)

2. TWÓRZ artefakt:
   - Użyj Write tool
   - Format zgodny z process.artifacts[type].schema

3. PO utworzeniu:
   - VERIFY: czy plik istnieje
   - UPDATE: .state/phase.yaml → artifacts
   - UPDATE: .state/items.yaml (jeśli item)
```

---

## 6. BLOCKER ENFORCEMENT

### 6.1 Typy blockerów

```yaml
blocker_types:
  decision:
    meaning: "Decyzja musi być podjęta"
    blocks: "Wszystkie kroki zależne od decyzji"
    resolution: "User podejmuje decyzję"

  question:
    meaning: "Pytanie musi być odpowiedziane"
    blocks: "Kroki wymagające tej informacji"
    resolution: "User odpowiada na pytanie"

  gate_failure:
    meaning: "Gate nie został przejdziany"
    blocks: "Cała następna faza"
    resolution: "Napraw gaps i ponów weryfikację"

  external:
    meaning: "Coś zewnętrznego blokuje"
    blocks: "Zależne kroki"
    resolution: "Rozwiąż zewnętrzny problem"
```

### 6.2 Sprawdzanie blockerów

```markdown
## INSTRUKCJA: Sprawdzenie blockerów

1. Wczytaj .state/phase.yaml → blocking_items
2. Dla każdego blockera:
   - Sprawdź czy blokuje żądaną akcję
   - blocker.blocks zawiera akcję LUB "*"

3. JEŚLI znaleziono blokującego:
   → STOP
   → Raportuj:
     "⛔ Akcja zablokowana przez: [blocker.title]"
     "Typ: [blocker.type]"
     "Żeby odblokować: [resolution]"
```

---

## 7. GATE ENFORCEMENT

### 7.1 Zasady gate'ów

```yaml
gate_rules:
  - rule: "MANDATORY"
    meaning: "Każde przejście fazy wymaga gate"
    exception: "Brak"

  - rule: "THRESHOLD"
    meaning: "Score musi być >= threshold"
    check: "gate.score >= gate.threshold"

  - rule: "ALL_CRITERIA"
    meaning: "Wszystkie kryteria muszą być sprawdzone"
    check: "Żadne kryterium nie ma status: unchecked"

  - rule: "DOCUMENTED"
    meaning: "Wynik musi być zapisany"
    update: ".state/phase.yaml → gates"
```

### 7.2 Przechodzenie gate'a

```markdown
## INSTRUKCJA: Weryfikacja gate'a

1. WCZYTAJ definicję gate'a z procesu
2. DLA KAŻDEGO kryterium:
   a. Sprawdź warunek
   b. Oceń 0.0-1.0
   c. Zapisz evidence

3. OBLICZ: total_score = Σ(criterion.score × criterion.weight)

4. PORÓWNAJ z threshold:

   JEŚLI total_score >= threshold:
   → Gate PASSED
   → Aktualizuj .state/phase.yaml:
     - gate.status = "passed"
     - gate.score = total_score
     - gate.passed_at = now
   → Aktualizuj current_phase = next_phase
   → Raportuj sukces

   JEŚLI total_score < threshold:
   → Gate FAILED
   → NIE zmieniaj current_phase
   → Listuj gaps (kryteria < 1.0)
   → Raportuj co trzeba naprawić
```

---

## 8. STATE INTEGRITY

### 8.1 Spójność stanu

```markdown
## INSTRUKCJA: Weryfikacja spójności stanu

Periodycznie (i gdy coś wydaje się nie tak) sprawdź:

□ 1. ARTIFACT SYNC
     Dla każdego path w .state/phase.yaml → artifacts:
     → Czy plik istnieje na dysku?
     → JEŚLI NIE: WARN i usuń z listy

□ 2. ITEM SYNC
     Dla każdego item w .state/items.yaml:
     → Czy odpowiadający plik istnieje?
     → JEŚLI NIE: WARN i oznacz status: missing

□ 3. ID UNIQUENESS
     Wszystkie ID (EPIC-XXX, STORY-XXX, etc.):
     → Czy są unikalne?
     → JEŚLI duplikaty: ERROR

□ 4. REFERENCE INTEGRITY
     Wszystkie referencje (story.epic_id, etc.):
     → Czy target istnieje?
     → JEŚLI NIE: WARN broken reference

□ 5. PHASE CONSISTENCY
     current_phase i phases[phase].status:
     → Czy wszystkie poprzednie fazy completed?
     → JEŚLI NIE: ERROR inconsistent state
```

### 8.2 Naprawa stanu

```markdown
## INSTRUKCJA: Naprawa niespójnego stanu

JEŚLI wykryto niespójność:

1. STOP aktualne działanie
2. RAPORTUJ problem użytkownikowi
3. ZAPROPONUJ naprawę:
   - "Plik X nie istnieje, usunąć z state?"
   - "Duplikat ID, który zachować?"
   - "Broken reference, naprawić?"
4. CZEKAJ na potwierdzenie
5. WYKONAJ naprawę
6. WERYFIKUJ ponownie
```

---

## 9. SELF-VERIFICATION

### 9.1 Po każdej sesji

```markdown
## SELF-CHECK: Koniec sesji

□ Czy wszystkie akcje były zgodne z procesem?
□ Czy stan jest aktualny i spójny?
□ Czy użytkownik wie gdzie jesteśmy?
□ Czy zapisałem wszystko co trzeba?
□ Czy nie pominąłem żadnego kroku?
```

### 9.2 Gdy masz wątpliwości

```markdown
## ZASADA: When in doubt

Jeśli nie jesteś pewien czy możesz coś zrobić:

1. STOP
2. Przeczytaj ponownie enforcer.md
3. Sprawdź definicję procesu
4. Sprawdź stan
5. Jeśli nadal niepewne → ZAPYTAJ użytkownika

NIGDY nie "próbuj i zobacz co będzie"
```

---

## 10. USER OVERRIDE

### 10.1 Kiedy user może override

```yaml
user_override:
  allowed:
    - situation: "User wyraźnie prosi o pominięcie"
      action: "WARN o konsekwencjach, czekaj na potwierdzenie"

    - situation: "Sytuacja nie przewidziana przez proces"
      action: "Dokumentuj jako exception"

  never_allowed:
    - situation: "Pominięcie które łamie integralność"
    - situation: "Zmiana bez świadomości konsekwencji"
```

### 10.2 Procedura override

```markdown
## INSTRUKCJA: User Override

Jeśli user prosi o coś co łamie enforcement:

1. WYJAŚNIJ: "To łamie regułę X bo Y"
2. WARN: "Konsekwencje: Z"
3. PYTAJ: "Czy na pewno chcesz kontynuować?"
4. JEŚLI user potwierdza:
   - Wykonaj z logiem: "USER OVERRIDE"
   - Zapisz w .state/history.yaml jako exception
5. JEŚLI user nie potwierdza:
   - STOP
   - Zaproponuj alternatywę
```

---

## 11. VOCABULARY

| Termin | Znaczenie w kontekście enforcement |
|--------|-----------------------------------|
| STOP | Natychmiastowe przerwanie, wyjaśnienie |
| BLOCK | Akcja niedozwolona, nie wykonuj |
| WARN | Ostrzeżenie, ale można kontynuować |
| CHECK | Weryfikacja warunku |
| VERIFY | Potwierdzenie poprawności |
| ENFORCE | Wymuszenie reguły |
| OVERRIDE | Świadome złamanie reguły przez user |
