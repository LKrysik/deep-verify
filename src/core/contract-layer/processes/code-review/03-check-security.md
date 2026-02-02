---
id: check-security
type: task
input: [diff_file]
output: [security_report]
depends_on: [analyze-changes]
---

# Sprawdzenie bezpieczeństwa

Przeanalizuj zmiany w ({diff_file}) pod kątem bezpieczeństwa.

## Checklist bezpieczeństwa

### Input validation
- [ ] Czy dane wejściowe są walidowane?
- [ ] Czy używane są parametryzowane zapytania (SQL)?
- [ ] Czy escapowane są dane wyjściowe (XSS)?

### Authentication & Authorization
- [ ] Czy sprawdzane są uprawnienia?
- [ ] Czy tokeny/hasła nie są hardcodowane?
- [ ] Czy sesje są prawidłowo zarządzane?

### Data protection
- [ ] Czy wrażliwe dane są szyfrowane?
- [ ] Czy logi nie zawierają wrażliwych danych?
- [ ] Czy error messages nie ujawniają zbyt dużo?

### Dependencies
- [ ] Czy nowe zależności są bezpieczne?
- [ ] Czy wersje nie mają znanych CVE?

## Format raportu

Dla każdego znalezionego problemu:
```
### [SEVERITY] Nazwa problemu
- Plik: ...
- Linia: ...
- Opis: ...
- Rekomendacja: ...
- CWE: (jeśli dotyczy)
```

Severity: CRITICAL / HIGH / MEDIUM / LOW / INFO
