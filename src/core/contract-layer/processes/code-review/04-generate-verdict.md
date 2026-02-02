---
id: generate-verdict
type: task
input: [change_summary, quality_report, security_report]
output: [final_verdict]
depends_on: [check-quality, check-security]
---

# Wygeneruj werdykt review

Na podstawie wszystkich raportów przygotuj finalny werdykt.

## Dane wejściowe
- Podsumowanie zmian: {change_summary}
- Raport jakości: {quality_report}
- Raport bezpieczeństwa: {security_report}

## Werdykt

Określ jeden z:
- **APPROVE** - można mergować
- **APPROVE WITH COMMENTS** - można mergować, ale są sugestie
- **REQUEST CHANGES** - wymagane poprawki przed merge
- **REJECT** - fundamentalne problemy, wymaga przeprojektowania

## Format werdyktu

```markdown
# Code Review Verdict

## Status: [APPROVE/REQUEST CHANGES/REJECT]

## Podsumowanie
(2-3 zdania o ogólnej jakości zmian)

## Statystyki
- Plików zmienionych: N
- Problemów krytycznych: N
- Problemów major: N
- Problemów minor: N

## Wymagane poprawki (jeśli REQUEST CHANGES)
1. ...
2. ...

## Sugestie (opcjonalne)
1. ...
2. ...

## Pochwały (co jest dobrze zrobione)
1. ...
```
