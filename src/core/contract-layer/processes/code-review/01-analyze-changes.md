---
id: analyze-changes
type: task
input: [diff_file, context_files]
output: [change_summary]
depends_on: []
---

# Analiza zmian w kodzie

Przeczytaj plik diff ({diff_file}) zawierający zmiany do review.

Dla każdej zmiany określ:
- Który plik został zmieniony
- Jaki typ zmiany (nowa funkcja, bugfix, refactor, config)
- Zakres zmiany (ile linii, ile funkcji)
- Powiązane pliki które mogą być affected

Jeśli potrzebujesz kontekstu, przeczytaj pliki z {context_files}.

Przygotuj podsumowanie zmian w formacie:

```
## Podsumowanie zmian

### Pliki zmienione: N

| Plik | Typ zmiany | Zakres | Ryzyko |
|------|------------|--------|--------|
| ... | ... | ... | low/medium/high |

### Główne obszary zmian:
- ...

### Potencjalne ryzyka:
- ...
```
