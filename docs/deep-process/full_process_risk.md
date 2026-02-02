# Deep Risk Report: Analiza Ryzyka dla Zunifikowanego Silnika Procesowego

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║                         D E E P   R I S K   R E P O R T                            ║
║                                    Wersja 1.0                                      ║
║                                                                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                    ║
║  OCENIANY PROJEKT:   Implementacja Zunifikowanego Silnika Procesowego v2.0         ║
║  GŁĘBOKOŚĆ:          Standard                                                      ║
║  DATA:               2026-02-02                                                      ║
║                                                                                    ║
║  KLUCZOWE WNIOSKI:                                                                 ║
║  - Identyfikowalne ryzyka techniczne i użytkowe.                                   ║
║  - Brak fundamentalnych, niemożliwych do zaadresowania zagrożeń.                  ║
║  - Kluczem do sukcesu jest zarządzanie interakcją z LLM i złożonością systemu.     ║
║                                                                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Podsumowanie Zarządcze

Analiza ryzyka dla projektu zunifikowanego silnika procesowego potwierdza, że projekt jest obarczony umiarkowanym, zarządzalnym ryzykiem. Najważniejsze zidentyfikowane zagrożenia koncentrują się wokół **niezawodności interakcji z LLM** oraz **potencjalnego wzrostu złożoności** samego silnika.

Zaproponowano konkretne strategie mitygacji dla każdego z kluczowych ryzyk. Przy ich wdrożeniu, poziom ryzyka resztkowego jest akceptowalny, co pozwala na kontynuację projektu zgodnie z przedstawionym planem.

---

## 2. Charakterystyka Systemu i Geneza Ryzyka (GROUND)

*   **Charakter Systemu (wg Perrowa): Złożony i Średnio Sprzężony.**
    System ma wiele komponentów (silnik, procesy, kontrakty, artefakty), co czyni go złożonym. Sprzężenie jest umiarkowane – błąd w jednym kontrakcie procesu nie powinien wpływać na inny, ale błąd w silniku może wpłynąć na wszystko. Taki system jest podatny na nieoczekiwane, kaskadowe awarie.

*   **Główne Źródła Ryzyka (Risk Genesis):**
    1.  **Ryzyko Strukturalne:** Zależność od sztywnego formatu kontraktów YAML – błędy w definicji mogą być trudne do zdiagnozowania.
    2.  **Ryzyko Emergentne:** Nieliniowe i nieprzewidywalne zachowanie LLM, które może generować niepoprawne, choć składniowo poprawne, artefakty.
    3.  **Ryzyko Integracyjne:** Ryzyko na styku `Pętli Zarządzania` i `Pętli Wykonania`.

---

## 3. Rejestr Zidentyfikowanych Ryzyk (IDENTIFY & QUANTIFY)

| ID | Ryzyko | Opis | P | I | V | D | R | **Score** |
|:---|:---|:---|:-:|:-:|:-:|:-:|:-:|:---:|
| **R-01** | **Niezgodność LLM** | Agent LLM generuje artefakty, które nie przechodzą walidacji z `Output Contract`. | 4 | 3 | 5 | 2 | 2 | **60** |
| **R-02** | **Rozrost Złożoności** | Silnik staje się zbyt skomplikowany przez dodawanie logiki dla "specjalnych przypadków", tracąc swoją generyczność. | 3 | 4 | 2 | 3 | 4 | **48** |
| **R-03** | **Degradacja Wydajności** | Dynamiczne skanowanie setek plików przy każdym kroku powoduje, że system staje się powolny i nieużywalny. | 2 | 4 | 2 | 4 | 3 | **32** |
| **R-04** | **Zła Użyteczność** | Zbyt duża liczba opcji w menu lub biurokracja związana z kontraktami zniechęca użytkownika do korzystania z systemu. | 3 | 5 | 2 | 2 | 3 | **75** |
| **R-05** | **Kaskada Błędów** | Błąd w jednym z plików kontraktu (np. literówka w `id`) powoduje serię trudnych do zdiagnozowania błędów w całym grafie zależności. | 3 | 4 | 4 | 3 | 3 | **48** |

*Legenda: P - Prawdopodobieństwo, I - Wpływ, V - Prędkość, D - Wykrywalność, R - Odwracalność (1-5). Score = P × I × max(V, D, R).*

---

## 4. Mapa Interakcji Ryzyk (INTERACT)

*   **Kaskada:** `R-01 (Niezgodność LLM)` → Prowadzi do ciągłych nieudanych prób, co zwiększa frustrację użytkownika i bezpośrednio wywołuje `R-04 (Zła Użyteczność)`.
*   **Korelacja Pozytywna:** `R-02 (Rozrost Złożoności)` jest silnie skorelowany z `R-03 (Degradacja Wydajności)`. Bardziej złożony kod ma tendencję do wolniejszego działania.

---

## 5. Portfolio Mitygacji (MITIGATE)

| ID | Ryzyko | Strategia (4T) | Działania Mitygujące |
|:---|:---|:---|:---|
| **R-01** | **Niezgodność LLM** | **Treat (Ogranicz)** | 1. Implementacja pętli `walidacja -> feedback -> retry` dla LLM. <br> 2. Wzbogacenie szablonów promptów o jednoznaczne instrukcje formatowania i przykłady (few-shot). |
| **R-02** | **Rozrost Złożoności** | **Terminate (Unikaj)** | 1. Ustanowienie twardej zasady architektonicznej: "Silnik jest generyczny, nowa funkcjonalność to nowy proces, a nie wyjątek w silniku". <br> 2. Regularne przeglądy kodu silnika pod kątem "zapachów" specjalizacji. |
| **R-03** | **Degradacja Wydajności** | **Tolerate/Treat (Toleruj/Ogranicz)** | 1. **Toleruj na początku:** Zaakceptuj, że dla małej liczby procesów problem nie wystąpi. <br> 2. **Ogranicz w przyszłości:** Zaplanuj implementację warstwy cache'ującej dla sparsowanych kontraktów. Cache będzie unieważniany tylko przy zmianie plików. |
| **R-04** | **Zła Użyteczność** | **Treat (Ogranicz)** | 1. Zaprojektuj `MenuGenerator` tak, by tworzył menu hierarchiczne (np. "Akcje Globalne", "Akcje Kontekstowe"). <br> 2. Ogranicz liczbę opcji na jednym poziomie menu do 5-7, z opcją "Pokaż więcej...". |
| **R-05** | **Kaskada Błędów** | **Treat (Ogranicz)** | 1. Stwórz narzędzie **"Linter Procesów"**, które przed uruchomieniem waliduje cały katalog procesu pod kątem spójności (np. czy wszystkie `next` wskazują na istniejące `id`, brak cykli). |

**Sprawdzenie Efektu Kobry (#407):** Żadna z powyższych mitygacji nie wprowadza nowych, poważniejszych ryzyk. Np. pętla `retry` (R-01) może zwiększyć koszt użycia API, ale jest to ryzyko akceptowalne w porównaniu do ryzyka niedziałającego systemu.

---

## 6. System Monitorowania (MONITOR)

Należy wdrożyć system monitorowania, który będzie śledził wczesne wskaźniki ostrzegawcze (leading indicators):

*   **Dla R-01 (Niezgodność LLM):**
    *   **Wskaźnik:** `Validation Failure Rate (%)`.
    *   **Próg:** Jeśli > 20% zadań wymaga `retry`, uruchom alert w celu przeglądu i poprawy szablonów promptów.
*   **Dla R-03 (Wydajność):**
    *   **Wskaźnik:** `Menu Generation Time (ms)`.
    *   **Próg:** Jeśli > 500ms, uruchom alert sygnalizujący potrzebę implementacji cache.
*   **Dla R-04 (Użyteczność):**
    *   **Wskaźnik:** Oceny z ankiet `System Usability Scale (SUS)` zbierane od użytkowników.
    *   **Próg:** Jeśli wynik SUS spadnie poniżej 70, uruchom alert w celu przeglądu i uproszczenia interfejsu/menu.

---

## 7. Podsumowanie Ryzyka Resztkowego

Po zastosowaniu mitygacji, profil ryzyka projektu jest akceptowalny. Największe ryzyko resztkowe pozostaje w obszarze **niezawodności LLM (R-01)**, ponieważ jest to czynnik częściowo zewnętrzny. Jednak dzięki zaplanowanym mechanizmom walidacji i ponawiania, jego wpływ jest ograniczony do potencjalnie wyższych kosztów i dłuższego czasu wykonania zadania, a nie do błędnego wyniku.
