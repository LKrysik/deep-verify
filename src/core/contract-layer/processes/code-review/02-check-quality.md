---
id: check-quality
type: task
input: [change_summary, diff_file]
output: [quality_report]
depends_on: [analyze-changes]
---

# Sprawdzenie jakości kodu

Na podstawie podsumowania zmian ({change_summary}) i diffa ({diff_file}), przeprowadź review jakości.

Sprawdź każdą zmianę pod kątem:

## 1. Czytelność
- Czy nazwy zmiennych/funkcji są jasne?
- Czy kod jest zrozumiały bez nadmiernych komentarzy?
- Czy struktura jest logiczna?

## 2. Poprawność
- Czy logika jest prawidłowa?
- Czy obsłużone są edge cases?
- Czy nie ma oczywistych bugów?

## 3. Spójność
- Czy styl jest zgodny z resztą projektu?
- Czy konwencje nazewnictwa są zachowane?
- Czy formatowanie jest spójne?

## 4. Wydajność
- Czy nie ma oczywistych problemów wydajnościowych?
- Czy pętle/algorytmy są optymalne?

Dla każdego problemu podaj:
- Plik i linię
- Opis problemu
- Sugerowaną poprawkę
- Priorytet (blocker/major/minor)
