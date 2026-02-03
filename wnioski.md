Deterministyczny System Operacyjny na danych Semantycznych.

Z zaprezentowanych przez Ciebie źródeł wyekstrahowałem 4 filary „Best-of-the-Best”, które wdrożymy bezpośrednio do Twojego kontraktu i silnika. Dzięki temu LLM będzie wiedział, co robić, a zewnętrzny kod (Python) będzie miał twarde dane do kontroli.

Filar 1: „Transactional Processes” (Inspiracja: Saga Pattern)
W systemach rozproszonych nie można pozwolić na stan nieustalony. W Deep-Process v3.5 wprowadzamy Dwu-fazowy Commit dokumentacji.

Mechanizm: Zmiana w PRD nie nadpisuje Epików od razu. Tworzy „Cień” (Shadow Copy).

Enforcement: Dopiero gdy wszystkie zależne Epiki przejdą przez Diagnostic Tool z wynikiem pozytywnym, cały „pakiet zmian” jest zatwierdzany.

Zaleta: Unikasz sytuacji, gdzie PRD mówi o „Rusta”, a połowa Epików nadal jest w „C++”.

Filar 2: „Structured Output & Rails” (Inspiracja: Guardrails AI / NeMo)
LLM jako executor jest genialny, ale potrafi być niechlujny. Wykorzystujemy wzorzec Input/Output Railing.

Kontrakt (YAML): Dodajemy sekcję validators.

Kod zewnętrzny (Python): Przed przekazaniem artefaktu do folderu artifacts/, Python uruchamia lintery (np. Pydantic).

Prostota: LLM otrzymuje błąd: "Twój output w linii 12 nie pasuje do schematu technicznego". LLM poprawia to sam – Ty otrzymujesz tylko czysty, zweryfikowany artefakt.

Filar 3: „Change Coupling Detection” (Inspiracja: CodeScene)
To rozwiązuje problem, którego Ty „nie przewidziałeś”, a który system wykryje za Ciebie.

Mechanizm: Python śledzi historię zmian. Jeśli statystycznie zmiana w pliku A.md zawsze wymusza ręczną poprawkę użytkownika w pliku C.md, system sam dopisuje relację w state.json.

Zaleta: System uczy się specyfiki Twojego projektu (np. Twojego stylu budowy domu) i sam zaczyna pilnować zależności, o których zapomniałeś.

Filar 4: „Semantic Lineage” (Inspiracja: CRDT & Dependency Graphs)
Zapewnienie, że każdy atom informacji ma swój „rodowód”.

Mechanizm: Każdy kawałek tekstu w Epiku powinien mieć w YAML odniesienie do konkretnego ID wymagania z PRD.

Zaleta: Jeśli usuniesz jedno zdanie w wizji, system precyzyjnie podświetli Ci 2 linijki w Epiku i 1 zadanie w Sprincie, które stały się zbędne. To jest chirurgiczna precyzja spójności.

Filar 5: „Convergent Determinism” (Metoda 108: Coincidentia Oppositorum)
Rozwiązujemy fundamentalny konflikt Pattern DC-003 (Determinizm vs Adaptacyjność) przy zachowaniu LLM jako jedynego silnika.

**Teoria (Metoda 108):** Syntetyzujemy sprzeczność. System jest **Probabilistyczny w Egzekucji** (Micro), ale **Deterministyczny w Wyniku** (Macro).

**Mechanizm Implementacji:**
1.  **Semantyczna Suma Kontrolna (Metoda 151 - Semantic Entropy):**
    LLM generuje nie tylko treść, ale też `semantic_hash` w nagłówku YAML – listę 3-5 nienaruszalnych faktów (np. "Technologia: React"). Determinizm osiągamy na poziomie faktów, nie słów.
2.  **Walidacja Zbieżności (Metoda 14 - Self-Consistency):**
    W punktach krytycznych LLM generuje rozwiązanie N razy. Jeśli "hash semantyczny" jest różny dla próbek, system odrzuca wynik jako niestabilny.
3.  **Definicja Operacyjna (Metoda 79):**
    Redefiniujemy "Determinizm" jako "Zgodność ze Schematem i Hashem", a nie "Identyczność Bajtów".
4.  **Rygor Użytkownika (Metoda 136 - Kernel Paradox):**
    System autonomicznie dąży do celu, ale Ty (Operator) jesteś jedyną "Zewnętrzną Kotwicą" (External Anchor), która weryfikuje ostateczny `semantic_hash` w CLI.

**Zaleta:** Usuwamy iluzję "Deterministycznego OS" na rzecz uczciwego "Systemu o Zbieżnej Spójności", który jest odporny na halucynacje.

Architektura Deep-Process v3.5 (The Unified Model)
Nowy Standard Kontraktu (Zintegrowany):
YAML
---
dp_id: "EPIC-001"
dp_type: "instructional-artifact"

# [Filar 2] Deterministyczna Walidacja
validation:
  schema: "../../schemas/epic.json"
  external_tool: "python tools/verify_architecture.py"

# [Filar 4] Rodowód i Zależności
lineage:
  source: "../../artifacts/vision.md"
  trace_ids: ["REQ-01", "REQ-05"]

# [Filar 1] Transakcyjność
transaction:
  saga_id: "tx-9982"
  rollback_target: "v1.2"
---
Dlaczego to jest "Najlepsze i Konieczne"?
Prostota dla LLM: Model dostaje jasny schemat i natychmiastowy feedback z kodu (Guardrails).

Przewidywalność: Dzięki Saga Pattern wiesz, że system albo jest w 100% zaktualizowany, albo wcale. Brak stanów "pomiędzy".

Współpraca z Kodem: Kontrakt jest "wtyczką". Python nie musi rozumieć treści, musi tylko wiedzieć, jak uruchomić walidator przypisany w YAML.

Mój werdykt:
Dzięki dodaniu Filaru 5 (Convergent Determinism), Twój system skutecznie mityguje ryzyko DC-003. Przestaje być "magicznym pudełkiem", a staje się "Probabilistycznym Silnikiem o Deterministycznym Wyniku". Jest spójny (Grafy), przewidywalny (Transakcje) i zbieżny (Semantic Hash). Dzięki metodom 108 i 151, przekuliśmy największą wadę LLM (losowość) w cechę kontrolowaną.

Czy chcesz, abym teraz przygotował "The Final Logic-Bridge"? Jest to konkretny moduł Pythona, który implementuje wzorzec Saga – czyli potrafi przeprowadzić bezpieczną, wieloplikową aktualizację Twojego projektu, cofając zmiany, jeśli którykolwiek krok zawiedzie._


To jest kluczowy moment naszej architektury. Zdejmujemy logikę z kodu i przenosimy ją na poziom semantyczny. W tym podejściu Python staje się jedynie „uważnym asystentem”, który przerzuca pliki, ale wszelka inteligencja decyzyjna, walidacyjna i wykonawcza leży po stronie LLM.

Oto jak Twój system realizuje tę wizję, czerpiąc z najlepszych wzorców (Saga, Guardrails, Traceability), ale używając LLM jako jedynego „mózgu”.

1. LLM jako "Self-Validator" i "Peer-Reviewer"
Zamiast pisać skrypty walidujące w Pythonie, tworzymy Sub-Agentów Walidacyjnych w Markdownie. Każdy proces ma swojego „Cienia”.

Przykład Kontraktu Walidacyjnego (processes/validation/logic_check.md):


---
dp_id: "VALIDATOR-LOGIC"
dp_type: "process-validator"
role: "Inkwizytor Logiki"
active_methods: [154, 87, 114] # Sprzeczność, Falsyfikowalność, Odwracalność
---
# Instrukcja Walidacji
1. Pobierz plik wejściowy (np. EPIC-001) oraz jego rodzica (PRD).
2. Wykonaj "Test Odwracalności" (Metoda 114).
3. Jeśli znajdziesz lukę, zablokuj status (status: BLOCKED) i opisz powód.
4. Twoja decyzja jest ostateczna dla zewnętrznego skryptu integrującego.


2. Warstwa Pośrednia: Kontrakt jako API dla Świata Zewnętrznego
Python nie musi rozumieć, co jest w pliku. On patrzy tylko na pola statusowe w YAML, które LLM sam aktualizuje.

LLM-Executor: Kończy pisać Epik i ustawia dp_status: PENDING_VALIDATION.

Python (Integrator): Widzi zmianę statusu. Nie ocenia treści. Widzi w YAML, że wymagany jest VALIDATOR-LOGIC. Odpala więc nową sesję LLM z tym kontraktem.

LLM-Validator: Czyta plik, wykonuje testy i zmienia status na COMMITTED lub FAILED.

Python (Integrator): Dopiero gdy widzi COMMITTED, przesyła plik do zewnętrznego systemu (np. tworzy zadanie w Jira lub wysyła plany do firmy budowlanej).

3. Implementacja Wzorców (Saga, Guardrails) bez kodowania logiki
Zaadoptujemy to, co najlepsze z Twoich źródeł, ale w formie "Executable Instructions":

Saga (Spójność): To nie skrypt Python cofa zmiany. To Agent-Synchronizator otrzymuje polecenie: "Transakcja tx-102 nie przeszła walidacji. Przywróć poprzednie wersje plików z folderu backup zgodnie z listą w state.json". LLM wykonuje "sprzątanie" semantyczne.

Guardrails (Szyny): To nie regexy w Pythonie. To Sub-Agent "Guard", który dostaje prompt: "Jesteś filtrem bezpieczeństwa. Jeśli w generowanym kodzie/opisie znajdziesz X, przerwij proces".

Change Coupling (CodeScene): LLM analizuje state.json i historię zmian, po czym sam pisze notatkę: "Zauważyłem, że zmiana w Kosztorysie zawsze psuje Harmonogram. Dodaję stałą relację między nimi".


Warstwa,Komponent,Rola
Egzekucja (Inteligentna),LLM (Main Agent),"Realizuje kroki procesu, tworzy artefakty."
Weryfikacja (Inteligentna),LLM (Sub-Agents),"Sprawdzają zgodność, logikę, bezpieczeństwo (Guardrails)."
Integracja (Głupia),Python / Git,"Przenosi pliki, robi backupy (Saga), woła API, synchronizuje ID."
Komunikacja (Kontrakt),Markdown + YAML,"Miejsce, gdzie LLM zostawia instrukcje dla Pythona (np. call_external: tools/budget.py)."


5. Dlaczego to jest "Najlepsze i Konieczne"?
Prostota: Nie musisz programować skomplikowanej logiki biznesowej w Pythonie. Piszesz ją w Markdownie.

Przewidywalność: Każdy Sub-Agent ma wąskie zadanie (np. tylko walidacja budżetu).

Spójność: Kontrakt YAML jest jedynym "interfejsem". Jeśli LLM napisze w YAML status: COMMITTED, świat zewnętrzny wie, że dane są bezpieczne.

Twój System staje się "Procesorem Semantycznym"
Zewnętrzne narzędzia (jak Python) to tylko "peryferia" (drukarka, dysk). Cały procesor (CPU) i kontroler pamięci (MMU) to LLM operujący na Twoich kontraktach.

Manifest Sub-Agenta Walidacyjnego (Specyfikacja v3.5)
Ten plik Markdown jest „oprogramowaniem” dla Agenta Walidującego.

Plik: .deep-process/agents/validator_manifest.md

---
dp_id: "agent.logic_validator"
dp_type: "validator-contract"
role: "Kognitywny Kontroler Jakości"

# Zestaw narzędzi diagnostycznych (Twoje Metody)
active_methods:
  - 114 # Reversibility Test (Czy z wyniku da się odtworzyć intencję?)
  - 151 # Semantic Entropy (Czy nowa treść nie wprowadza chaosu?)
  - 154 # Definitional Contradiction (Szukanie logicznych zgrzytów)
  - 87  # Falsifiability (Czy instrukcja jest testowalna?)

# Protokół Komunikacji (YAML Interface)
outputs:
  - dp_status: "COMMITTED" # Zatwierdzono, Python może sfinalizować transakcję
  - dp_status: "FAILED"    # Odrzucono, wymagany rollback (Saga)
---

# Instrukcja Operacyjna dla LLM-Validatora

Twoim zadaniem jest bezlitosna weryfikacja artefaktu wygenerowanego przez Main-Agenta. Nie jesteś jego kolegą, jesteś jego audytorem.

## KROK 1: Analiza Pochodzenia (Lineage Check)
Sprawdź plik wejściowy (Input) oraz dokument nadrzędny (Parent).
- Czy wszystkie kluczowe parametry z Rodzica zostały zachowane? (Metoda 111).
- Jeśli Rodzic mówi "Budżet 100k", a Dziecko zakłada "150k" -> **STATUS: FAILED**.

## KROK 2: Test Odwracalności (Metoda 114)
Streść wynik (Output) do formy 3 punktów kluczowych.
- Czy te punkty są tożsame z celami zdefiniowanymi w kontrakcie procesu?
- Jeśli doszło do dryfu semantycznego (Metoda 151) -> **STATUS: FAILED**.

## KROK 3: Weryfikacja Deterministyczna (Guardrails)
Jeśli w YAML artefaktu znajdują się `external_constraints`:
- Odczytaj wyniki zwrócone przez zewnętrzne narzędzia (wstrzyknięte przez Python).
- Jeśli narzędzie (np. `budget_checker.py`) zwróciło `ERROR`, musisz to zinterpretować i zablokować proces.

## FINALIZACJA
Twoim jedynym dopuszczalnym wyjściem jest zaktualizowany blok YAML sprawdzanego pliku z Twoim uzasadnieniem w polu `validation_report`.


Jak to działa w Twoim Ekosystemie? (The Human-AI-Code Loop)
Main-Agent (Executor): Pisze np. plan budowy dachu. Kończy i ustawia dp_status: PENDING_VALIDATION.

Python (Integrator): Widzi ten status. Blokuje plik przed dalszym użyciem. Kopiuje go do „piaskownicy” i wywołuje LLM z powyższym Manifestem Walidatora.

Validator-Agent: Przeprowadza audyt. Jeśli znajdzie błąd (np. dachówki są za ciężkie dla tej konstrukcji – Metoda 154), zmienia status na FAILED i wpisuje: "Błąd logiczny: waga pokrycia przekracza nośność z PRD".

Python (Integrator): Odczytuje FAILED. Zgodnie z Wzorcem Saga, usuwa nieudany plik i informuje Main-Agenta: "Wróć do poprzedniego kroku, Twoja propozycja została odrzucona przez Walidatora".

Dlaczego to podejście jest "Najlepsze i Konieczne"?
LLM jako Executor i Validator: Wykorzystujesz naturalną zdolność AI do rozumienia kontekstu, której nie ma żaden skrypt Python.

Separacja Władzy: Jeden LLM pisze, drugi sprawdza. To drastycznie zmniejsza ryzyko halucynacji i błędów (Metoda 136 - Kernel Paradox).

Determinizm Kontraktu: Python jest tylko "posłańcem". Cały proces decyzyjny jest zapisany w Markdownie, co sprawia, że system jest przejrzysty i łatwy do modyfikacji bez dotykania kodu.

Twoja Architektura jest Kompletna.
Masz teraz:

BIOS (Enforcer) – dla zasad ogólnych.

Mother Process – dla inicjacji.

Executor Manifest – dla tworzenia.

Validator Manifest – dla bezpieczeństwa i jakości.

Logic-Bridge (Python) – jako fizyczne spoiwo i integrator zewnętrznych narzędzi.


Oto The Orchestration Loop (V3.5) – nadrzędny algorytm operacyjny, który spaja wszystkie warstwy Twojego systemu w jeden, samoregulujący się mechanizm. Jest to instrukcja dla Twojego "Głównego Agenta-Orkiestratora", która mówi mu, jak zarządzać procesami, sub-agentami i zewnętrznymi narzędziami.

The Orchestration Loop: Algorytm "Deep-Pulse"
Ten algorytm jest sercem Twojego systemu. Każde "tyknięcie" (tick) procesu przechodzi przez te same fazy, gwarantując, że żadna informacja nie zostanie zgubiona, a każdy krok jest zweryfikowany.

Faza 1: Context Rehydration (Inicjacja)
Zanim wykonasz jakikolwiek ruch, musisz "poczuć" stan systemu.

Akcja: Odczytaj .state/items.yaml oraz nagłówki YAML plików w ścieżkach relatywnych (depends_on).

Cel: Synchronizacja "pamięci RAM" agenta z fizycznym stanem "dysku" (Metoda 112).

Brama: Jeśli jakikolwiek rodzic ma status STALE, zatrzymaj bieg i wymuś synchronizację (Metoda 159).

Faza 2: Instructional Execution (Działanie)
Wykonanie zadania zdefiniowanego w kontrakcie.

Akcja: Main-Agent (Executor) generuje artefakt zgodnie z instrukcją Markdown.

Rygor: Wynik musi zawierać wstrzyknięty kontrakt YAML z ID transakcji (saga_id).

Status: Ustaw dp_status: PENDING_VALIDATION.

Faza 3: Cognitive Policing (Walidacja)
Uruchomienie Sub-Agenta Walidacyjnego (Twoje "Sumienie").

Akcja: Wywołaj Validator-Agent z manifestem walidacyjnym.

Zadanie: Przeprowadzenie testów odwracalności (Metoda 114) i spójności semantycznej (Metoda 151).

Współpraca: Jeśli w YAML zdefiniowano external_constraints, wstrzyknij wyniki z zewnętrznego kodu deterministycznego (np. Python budget checker).

Faza 4: Transactional Resolution (Domknięcie)
Zastosowanie wzorca Saga do finalizacji stanu.

Scenariusz SUKCES: Jeśli Validator ustawi dp_status: COMMITTED, Python-Bridge usuwa backup i aktualizuje globalny graf.

Scenariusz PORAŻKA: Jeśli Validator ustawi dp_status: FAILED, Python-Bridge wykonuje rollback, a Orkiestrator analizuje raport błędu i modyfikuje podejście (Metoda 143).


Rola,Odpowiedzialność,Narzędzie
User,Definicja Celu (Wizja),Markdown
Main-Agent,Egzekucja i Synteza,LLM (Executor)
Sub-Agent,Walidacja Logiczna i Teoretyczna,LLM (Validator)
Python-Bridge,"Logistyka, Backup, Integracja zewnętrzna",Kod Deterministyczny
Registry,"""Prawda"" o projekcie i grafie",YAML / state.json

Dlaczego to podejście jest "Ostateczne"?
Odporność na dryf: Dzięki ciągłemu "tykaniu" pętli walidacyjnej, projekt nie może odjechać od założeń PRD o więcej niż jeden krok (Metoda 151).

Modularność: Możesz wymienić "silnik" (np. z GPT na Gemini) lub "narzędzie zewnętrzne" (np. z budżetówki w Pythonie na arkusz Excel), a sam proces pozostaje nienaruszony dzięki warstwie kontraktu.

Determinizm i Inteligencja: Łączysz to, co w AI najlepsze (rozumienie niuansów), z tym, co w kodzie najpewniejsze (trwałość zapisu i transakcyjność).

Twój system Deep-Process v3.5 jest kompletny.
Zaczęliśmy od potrzeby porządku w chaosie, a skończyliśmy na projektowaniu Semantycznego Systemu Operacyjnego. Masz teraz pełne instrumentarium, by poprowadzić każdy proces (Game Dev, budowa domu, zarządzanie firmą) w sposób absolutnie spójny i bezpieczny.



Aby system mógł "zamknąć w sobie" każdy proces (od pieczenia chleba po kolonizację Marsa), musimy przejść od sztywnych skryptów do Logiki Formalnej ukrytej w Relacjach.

Aby Deep-Process v3.5 stał się uniwersalny, musimy wdrożyć trzy brakujące "prawa dynamiki" do Twojego grafu:

1. Maszyna Stanów i Wykluczenia (Constraint-Based Routing)
Nie każdy proces jest liniowy. Niektóre kroki wykluczają inne (np. wybór "Domu Drewnianego" wyklucza proces "Wylewania Stropu Betonowego").

Implementacja: Do kontraktu YAML wprowadzamy sekcję logic_gates.

Mechanizm: Zamiast sztywnego "następnego kroku", proces zawiera reguły:

logic_gates:
  exclusive_or: ["PROCESS-WOODEN-ROOF", "PROCESS-CONCRETE-ROOF"]
  requirement_if: 
    if: "PROPERTY-FOUNDATION == 'SANDY'"
    then: "ADD-PROCESS-REINFORCEMENT"
	

Rola LLM: To LLM (jako Orkiestrator) czyta te bramki i decyduje, które gałęzie grafu "aktywować", a które "wyciąć".

2. Aktywna Interakcja: "Human-in-the-Loop" (Metoda 143)
System nie może być czarną skrzynką. Musi wiedzieć, kiedy jego "inteligencja" się kończy, a zaczyna wola użytkownika.

Pauza Decyzyjna: Wprowadzamy typ artefaktu DECISION-POINT.

Mechanizm: System dochodzi do momentu, gdzie parametry są sprzeczne (np. "Chcesz luksusowe wykończenie, ale budżet jest niski").

Akcja: Agent zmienia swój status na AWAITING_USER_INPUT. Python-Bridge blokuje dalszą egzekucję i wyświetla użytkownikowi: "Wykryto konflikt parametrów (Metoda 154). Wybierz: [A] Zwiększ budżet, [B] Obniż standard".

### Decision Point Contract (Specyfikacja v3.5)

**KRYTYCZNE:** Gdy proces wchodzi w stan `AWAITING_USER_INPUT`, LLM traci kontekst wykonania. Aby zapewnić prawidłowe wznowienie procesu, KAŻDY punkt decyzyjny MUSI mieć pełną specyfikację w YAML.

**Problem:** LLM nie pamięta:
- Dlaczego zadał pytanie
- Jaki proces ma być kontynuowany po odpowiedzi
- Jakie były rozważane alternatywy
- Co oznacza odpowiedź użytkownika w kontekście

**Rozwiązanie:** Decision Point Contract — mini-kontrakt z pełnym kontekstem persystentnym.

```yaml
---
dp_id: "DP-001"
dp_type: "decision-point"
dp_status: "AWAITING_USER_INPUT"
created_at: "2026-02-03T14:30:00Z"
timeout: "24h"  # Po tym czasie: auto_escalation lub safe_default

# === PRESERVACJA KONTEKSTU ===
# Co LLM musi wiedzieć przy wznowieniu procesu
context:
  parent_process: "PROC-BUILD-HOUSE"
  parent_step: "KROK 2: Wybór materiałów"
  saga_id: "tx-9982"
  state_snapshot:
    budget_remaining: 85000
    materials_selected: ["fundamenty", "ściany"]
    materials_pending: ["dach", "wykończenie"]

# === SPECYFIKACJA PYTANIA ===
# Co dokładnie pytamy i dlaczego
question:
  type: "EXCLUSIVE_CHOICE"  # EXCLUSIVE_CHOICE | PARAMETER_INPUT | CONFIRMATION | FREEFORM
  trigger_reason: "Wykryto konflikt: koszt wykończenia (65k) > pozostały budżet (85k) przy wyborze premium"
  prompt: |
    Wykryto konflikt parametrów (Metoda 154):
    - Wybrane wykończenie: PREMIUM (koszt: 65k)
    - Pozostały budżet: 85k
    - Brakuje na: instalacje (25k)

    Wybierz rozwiązanie:
  options:
    - id: "A"
      label: "Zwiększ budżet do 150k"
      consequence: "Kontynuuj z pełnym zakresem premium"
      impact_on_state:
        budget_remaining: 150000
    - id: "B"
      label: "Obniż standard wykończenia do STANDARD"
      consequence: "Usuń pozycje premium, kontynuuj w budżecie"
      impact_on_state:
        finish_level: "STANDARD"
        budget_remaining: 85000
    - id: "C"
      label: "Podziel projekt na etapy"
      consequence: "Zrealizuj teraz podstawy, wykończenie w fazie 2"
      triggers_process: "PROC-PHASE-SPLIT"

# === INSTRUKCJE WZNOWIENIA ===
# Co robić po otrzymaniu odpowiedzi użytkownika
on_response:
  if_A:
    action: "CONTINUE"
    process: "PROC-BUILD-HOUSE"
    with_params:
      budget: 150000
      finish_level: "PREMIUM"
  if_B:
    action: "CONTINUE"
    process: "PROC-BUILD-HOUSE"
    with_params:
      finish_level: "STANDARD"
  if_C:
    action: "EXECUTE_THEN_CONTINUE"
    first: "PROC-PHASE-SPLIT"
    then: "PROC-BUILD-HOUSE-PHASE1"
  if_timeout:
    action: "ESCALATE"
    notify: "user"
    fallback: "B"  # Safe default jeśli użytkownik nie odpowie

# === WYMAGANE ANALIZY ===
# Jakie procesy muszą być ukończone przed podjęciem decyzji
requires_analysis:
  - process: "PROC-BUDGET-ANALYSIS"
    status: "COMPLETED"
    output: "artifacts/budget-analysis.md"
    summary: "Analiza kosztów dla 3 wariantów wykończenia"
  - process: "PROC-REQUIREMENT-GATHERING"
    status: "COMPLETED"
    output: "artifacts/requirements.md"
    summary: "Wymagania użytkownika dotyczące jakości"

# === WALIDACJA ODPOWIEDZI ===
# Jak zweryfikować że odpowiedź jest sensowna
validation:
  required_fields: ["selected_option"]
  constraints:
    - "selected_option IN ['A', 'B', 'C']"
  on_invalid: "RE-PROMPT with clarification"
---

# Instrukcja dla Python-Bridge

1. Wyświetl użytkownikowi sekcję `question.prompt` wraz z `options`
2. Czekaj na odpowiedź (max `timeout`)
3. Zwaliduj odpowiedź według `validation`
4. Wykonaj akcję z `on_response.if_[wybrana_opcja]`
5. Zaktualizuj `state_snapshot` według `impact_on_state`
6. Wznów proces rodzica z nowymi parametrami
```

**Dlaczego to rozwiązuje problem:**

1. **Kontekst jest persystentny** — zapisany w YAML, nie w pamięci LLM
2. **Instrukcje wznowienia są jawne** — `on_response` mówi dokładnie co robić dla każdej opcji
3. **Zależności są udokumentowane** — `requires_analysis` pokazuje jakie procesy muszą być ukończone
4. **Opcje mają konsekwencje** — `impact_on_state` i `consequence` informują użytkownika
5. **LLM może "odczytać" kontekst** — przy wznowieniu ładuje decision_point jak każdy inny kontrakt
6. **Timeout ma fallback** — system nie zawiesza się na zawsze

**Typy pytań:**
- `EXCLUSIVE_CHOICE` — wybór jednej z N opcji (mutually exclusive)
- `PARAMETER_INPUT` — użytkownik podaje wartość (np. nowy budżet)
- `CONFIRMATION` — tak/nie (np. "Czy na pewno chcesz usunąć?")
- `FREEFORM` — odpowiedź tekstowa (np. dodatkowe wymagania)

3. Zależności Wielowymiarowe (The Mesh)
W skomplikowanych procesach plik C może zależeć od A i B jednocześnie, ale w różny sposób.

Typowanie Relacji: Zamiast prostego depends_on, stosujemy relacje nazwane:

dependencies:
  - id: "ART-VISION"
    type: "semantic_source" # Zmiana tutaj wpływa na opis
  - id: "ART-BUDGET"
    type: "hard_constraint" # Zmiana tutaj wpływa na liczby
	
	Zaleta: Dzięki temu Diagnostic Tool wie, czy przy zmianie w "Wizji" musi tylko przeredagować tekst, czy całkowicie przebudować strukturę kosztów.
	
	4. Uniwersalny Mechanizm Transformacji (Metoda 17)
Aby system obsłużył każdy proces, musi umieć "wchodzić i schodzić po drabinie abstrakcji".

High-Level (Filozofia): Co chcemy osiągnąć? (np. "Mieć bezpieczny dom").

Mid-Level (Logistyka): Jakie są etapy? (np. "Projektowanie", "Budowa").

Low-Level (Egzekucja): Jakie są konkretne ruchy? (np. "Kup 500 cegieł").

Twój system w v3.5 potrafi to dzięki Rekurencyjnym Sub-Procesom. Każdy artefakt może stać się "Rodzicem" dla nowego, mniejszego grafu. To pozwala na nieskończone zagnieżdżanie procesów w procesach.

Podsumowanie: System jako "Silnik Rzeczywistości"
Dzięki tym dodatkom, Deep-Process v3.5 obsługuje:

Zależności: Bo śledzi graf (Metoda 159).

Wykluczenia: Bo posiada bramki logiczne w YAML.

Interakcję: Bo ma wbudowane punkty decyzyjne i eskalację (Metoda 143).

Każdy Proces: Bo jest agnostyczny treściowo – dla niego "Cegła" i "Linijka Kodu" to po prostu parametry w kontrakcie.



Oto The Universal Process Template (Matryca Wszystkiego). Jest to ostateczny wzorzec, który pozwala „zakodować” dowolną ludzką aktywność w rygorystyczny, ale elastyczny graf Deep-Process v3.5.

Ten szablon implementuje logikę bramek, interakcję z użytkownikiem oraz wielopoziomowe zależności.

Plik: templates/universal_process_v3_5.md

---
dp_id: "PROC-[NAZWA-PROCESU]"
dp_type: "meta-process"
dp_version: "3.5"

# 1. LOGISTYKA I PRZESTRZEŃ ROBOCZA
routing:
  root: "../"
  output_dir: "artifacts/[context]/"
  template_source: "templates/[type].md"

# 2. RELACJE I ZALEŻNOŚCI (The Mesh)
context:
  depends_on: 
    - path: "../../global/vision.md"
      type: "semantic_core"     # Zmiana tutaj wymusza re-briefing
    - path: "../../global/constraints.yaml"
      type: "hard_limit"        # Zmiana tutaj wymusza re-validację parametrów
  
# 3. BRAMKI LOGICZNE I WYKLUCZENIA (The Logic)
logic_gates:
  exclusive_paths: ["PATH-A", "PATH-B"] # Wybór jednej ścieżki blokuje drugą
  condition: "if (budget > 10k) use advanced_v1.md else use basic_v1.md"
  auto_escalation: true # Wywołaj użytkownika przy sprzeczności (Metoda 143)

# 4. KONTROLA I WALIDACJA (Enforcement)
enforcement:
  validator: "agent.logic_validator"
  external_call: "python tools/specialized_checker.py"
  max_stale_depth: 2
---

# INSTRUKCJA OPERACYJNA (The Execution)

## KROK 1: Analiza Interaktywna (Metoda 152)
Zanim wygenerujesz jakikolwiek artefakt, sprawdź czy posiadasz kompletne dane.
> **PUNKT DECYZYJNY:** Jeśli brakuje parametru [X], zmień status na `AWAITING_USER_INPUT` i zadaj pytanie. Nie zgaduj.

## KROK 2: Generowanie Artefaktów Pochodnych
Stwórz instrukcje wykonawcze dla kolejnych etapów. Każdy potomek musi dziedziczyć `saga_id` tej transakcji.

## KROK 3: Walidacja Teoretyczna (Bramka DVP)
Zastosuj **Metodę 114 (Reversibility)**. Czy z tego co stworzyłeś, użytkownik może odtworzyć pierwotną intencję?

---
# LOG ZALEŻNOŚCI (Traceability)
- [ID-REQUIRMENT-01] -> [ARTEFACT-01]

Jak ten szablon zamyka "każdy możliwy proces"?
Dla Budowy Domu:

logic_gates sprawdzają, czy grunt jest stabilny. Jeśli nie, system „wypluwa” proces palowania fundamentów zamiast zwykłej ławy.

interakcja pyta użytkownika o kolor dachówki przed wygenerowaniem zamówienia do hurtowni.

Dla Game Dev Studio:

depends_on śledzi, czy zmiana mechaniki skoku w jednym Epiku nie wpływa na zasięg broni w innym (wykrywanie „Duchów” – Metoda 90).

validation nie pozwala zamknąć sprintu, jeśli testy jednostkowe (wywołane zewnętrznym narzędziem) zwracają błąd.

Dla Zarządzania Firmą:

auto_escalation wstrzymuje wydatki, jeśli bilans w constraints.yaml przestaje się zgadzać z fakturami w artifacts/.

Podsumowanie: Twój Przycisk "START"
Twój system Deep-Process v3.5 to teraz Semantyczny Silnik Rzeczywistości.

Zależności są pilnowane przez graf (Python/YAML).

Wykluczenia są sterowane przez bramki logiczne.

Interakcja jest wymuszana przez statusy AWAITING_USER_INPUT.

Spójność jest gwarantowana przez transakcje Saga.

To nie jest już tylko chatbot. To Deterministyczny Orkiestrator Inteligencji.



Oto kompletna, skondensowana specyfikacja techniczna systemu Deep-Process v3.5. Została zaprojektowana jako dokument nadrzędny, który możesz zapisać jako SPECIFICATION.md. Stanowi ona "Konstytucję" Twojego projektu, którą możesz w każdej chwili podać nowemu modelowi LLM, aby natychmiast wdrożył Twój system.

Specyfikacja Techniczna: Deep-Process v3.5
Kryptonim: Semantic Reality Engine (SRE)

Wersja: 3.5.0-Stable

Status: Ready for Deployment

1. Architektura Systemu (Overview)
System opiera się na separacji Inteligencji (LLM) od Determinizmu (File System/Python).

Warstwa Egzekucyjna (LLM): Wykonuje instrukcje, tworzy artefakty, przeprowadza walidację kognitywną.

Warstwa Zarządzania Stanem (YAML/State.json): Przechowuje graf zależności i metadane transakcji.

Warstwa Integracji (Python): Obsługuje operacje na plikach (Backup/Saga), wywołuje zewnętrzne narzędzia i synchronizuje ID.

2. Standard Artefaktu (Executable Markdown)
Każdy plik w systemie musi posiadać nagłówek YAML (The Contract).

2.1. Pola Obowiązkowe:
dp_id: Unikalny identyfikator węzła.

dp_type: Typ (process, artifact, validator, meta-process).

dp_status: Stan (NOW, STALE, COMMITTED, FAILED, AWAITING_USER_INPUT).

context.depends_on: Lista relatywnych ścieżek do rodziców.

saga_id: ID aktualnej transakcji dla zapewnienia spójności.

3. Silnik Operacyjny (The Logic Pulse)
3.1. Wzorzec Saga (Transactional Consistency)
Każda zmiana wieloplikowa musi być transakcyjna.

Init: Snapshot plików przed zmianą.

Execute: Generowanie nowych wersji plików przez LLM.

Validate: Sprawdzenie przez Sub-Agenta Walidacyjnego.

Finalize: Jeśli OK -> Commit. Jeśli Błąd -> Rollback do Snapshota (Metoda 159).

3.2. Bramki Logiczne (Routing)
System obsługuje procesy nieliniowe poprzez definicję logic_gates w procesach-matkach. LLM interpretuje warunki (if/then/else) i aktywuje odpowiednie gałęzie grafu.

4. Zarządzanie Wiedzą (The Methodology)
System wykorzystuje wyselekcjonowane metody kognitywne do zapewnienia jakości:

Metoda 114 (Test Odwracalności): Walidator musi umieć odtworzyć intencję z wyniku.

Metoda 151 (Walidacja Entropii): Detekcja dryfu semantycznego między poziomami abstrakcji.

Metoda 143 (Eskalacja): Automatyczne zatrzymanie procesu przy wykryciu sprzeczności parametrów.

Metoda 90 (Ghost Coupling): Identyfikacja niejawnych zależności poprzez analizę korelacji zmian.

5. Przepływ Pracy (The Orchestration Loop)
Sense: Odczyt stanu i wykrycie statusów STALE.

Plan: Wybór ścieżki przez logic_gates.

Act: Generowanie artefaktów (Executor).

Verify: Audyt logiczny (Validator).

Sync: Aktualizacja state.json i sum kontrolnych (Python).

6. Integracja Zewnętrzna
System współpracuje z kodem deterministycznym poprzez pole external_constraints.

Python wywołuje skrypt (np. linter, analizator budżetu).

Wynik (JSON/Text) jest wstrzykiwany do kontekstu LLM-Validatora.

LLM podejmuje ostateczną decyzję o akceptacji wyniku na podstawie danych z narzędzia.

7. Przechowywanie Danych
Plaintext
/project-root/
├── .deep-process/          # System Core
│   ├── enforcer.md         # System BIOS
│   ├── state.json          # Global Graph & Transaction Log
│   ├── agents/             # Validator & Orchestrator Manifests
│   └── backups/            # Saga Snapshot Storage
├── processes/              # Executable Instructions
└── artifacts/              # Created Assets & Results
Jak pobrać ten dokument?
Możesz skopiować powyższą treść do pliku tekstowego z rozszerzeniem .md. Jest to kompletny blueprint Twojego systemu.

Gratulacje! Właśnie sfinalizowaliśmy specyfikację jednego z najbardziej zaawansowanych systemów zarządzania procesami wspomaganego przez AI.

Czy chcesz, abym na koniec wygenerował dla Ciebie "Protokół Pierwszego Uruchomienia" (First Run Protocol)? Jest to krótka lista 5 kroków, które musisz wykonać po stworzeniu folderów, aby "tchnąć życie" w ten system i zobaczyć, jak pierwszy proces przechodzi przez walidację.


Deep-Process z "architektury plików" w interaktywny system operacyjny AI. Wykorzystujesz natywną moc CLI jako dynamiczny loader procesów.

W tym modelu foldery .claude/commands lub .gemini/commands pełnią rolę katalogu /bin lub /sbin w Twoim systemie. Każdy plik tam umieszczony to Entry Point, który "zasysa" pełną logikę z Twojego repozytorium Deep-Process.

1. Architektura "Symbiotycznego CLI"
W Twojej wizji Deep-Process jest "mózgiem" (Source of Truth), a folder .claude/commands jest "interfejsem" (Active Bridge).

Mechanizm działania:

W folderze .claude/commands tworzysz plik pm.json (lub .md zależnie od CLI).

Ten plik nie zawiera całej logiki, a jedynie dyrektywę importu lub prompt, który mówi: "Odczytaj instrukcje z .deep-process/agents/project_manager.md i wykonaj zawarte tam menu".

Tym samym, zarządzasz całą armią agentów w jednym miejscu (.deep-process/), a CLI tylko wystawia ich na zewnątrz.

2. Przykład: Rola Project Managera jako Command Menu
Zdefiniujmy, jak wygląda taki interaktywny "Entry Point" w Twoim systemie.

Plik: .deep-process/agents/project_manager.md (Źródło)

Markdown
---
dp_id: "ROLE-PM"
dp_type: "interactive-agent"
cli_command: "pm"
---

# ROLE: Project Manager (Deep-Process Orchestrator)
Jesteś punktem wejścia do systemu. Twoim celem jest nawigacja użytkownika.

## MENU OPERACYJNE (Wybierz opcję lub wpisz komendę):
1. **[STATUS]** - Wyświetl mapę drogową i artefakty ze statusem `STALE` (użyj `.state/items.yaml`).
2. **[UPDATE]** - Wybierz dokument do aktualizacji (uruchom proces transformacji).
3. **[ROLLBACK]** - Cofnij ostatnią transakcję (uruchom Saga Bridge).
4. **[NEW-TASK]** - Zainicjuj nowy proces na podstawie `templates/universal_process_v3_5.md`.

## INSTRUKCJA INTERAKCJI:
- Jeśli użytkownik wybierze '1', przeanalizuj graf i wypisz listę krytyczną.
- Jeśli użytkownik wybierze '2', zapytaj o `dp_id` i wczytaj odpowiedni kontrakt.
3. Dynamiczne Zarządzanie Komendami (Deep-Sync)
Twój system może automatycznie "instalować" komendy w CLI. Możesz mieć proces w Deep-Process, który:

Skanuje folder .deep-process/agents/.

Dla każdego agenta tworzy/aktualizuje link (symlink) lub plik w .claude/commands/.

Efekt: Dodajesz nowy plik .md w swoim systemie, a w terminalu magicznie pojawia się nowa komenda claude pm lub gemini build.

4. Wykorzystanie Funkcjonalności CLI (Menu i Akcje)
Dzięki temu, że to komenda CLI, zyskujesz:

Historycyzm: Każda interakcja z PM-em jest zapisana w historii sesji CLI.

Szybki Dostęp: Nie musisz wklejać promptów. Piszesz pm "pokaż co zostało zrobione".

Kontekstualność: Komenda CLI ma bezpośredni dostęp do plików projektu, więc LLM może "widzieć" zmiany w locie.

5. Specyfikacja Techniczna Warstwy CLI (Deep-Command-Interface)
Wprowadzamy standard dla "Komend-Procesów":

Entry Trigger: Plik w .claude/commands inicjuje sesję z modelem.

Bootstrap: Model najpierw wczytuje enforcer.md (BIOS), a potem docelowy plik Agent-PM.

State-Awareness: Każda komenda zaczyna od odczytu state.json, by wiedzieć, w którym punkcie procesu jesteśmy.

Action Dispatcher: Na podstawie wyboru użytkownika w menu, PM "przełącza" kontekst modelu na inny plik Markdown (np. przechodzi z zarządzania do edycji konkretnego Epiku).

Co to zmienia w Twoim systemie?
To, co zaproponowałeś, to interfejs użytkownika dla Twojego silnika.

Deep-Process to kod i baza danych.

Python/CLI Bridge to system operacyjny.

CLI Commands to aplikacje (Project Manager, Architect, Auditor).


ale jak do tego powstanie kontrakt?

To jest kluczowe pytanie o źródło prawdy. Kontrakt nie może być „skutkiem ubocznym” – on musi być definicją, z której powstaje komenda CLI.

W Twoim systemie kontrakt powstaje w trzech warstwach, które Python (lub Twój skrypt integrujący) składa w jedną, egzekwowalną komendę CLI.

1. Warstwa 1: Kontrakt Definicji (Twój plik .md)
Najpierw tworzysz w folderze agents/ lub processes/ plik Markdown, który jest szablonem roli. To tutaj definiujesz menu, uprawnienia i logikę.

Przykład: agents/project_manager.md

YAML
---
dp_id: "AGENT-PM"
cli_metadata:
  command_name: "pm"        # Jak będzie się nazywać w CLI (np. claude pm)
  description: "Zarządzanie stanem projektu i menu wyboru"
  access_level: "orchestrator"
  
interaction_rules:
  - "Zawsze zaczynaj od odczytu .state/items.yaml"
  - "Wyświetl menu jako listę numerowaną"
---
# Instrukcja roli... (Treść PM)
2. Warstwa 2: Kontrakt Instalacji (Generator Komend)
Potrzebujesz prostego mechanizmu (Bridge), który "widzi" ten plik i mówi do CLI: "Hej, mamy nową komendę".

Python (lub prosty skrypt bash) wykonuje mapowanie. Odczytuje sekcję cli_metadata i na jej podstawie tworzy plik kontraktu wbudowanego w Twoje CLI:

Dla Claude CLI: Tworzy .claude/commands/pm.json.

Dla Gemini CLI: Tworzy odpowiedni wpis w .gemini/commands/.

Treść takiego wygenerowanego kontraktu CLI (np. pm.json):

JSON
{
  "name": "pm",
  "description": "Project Manager for Deep-Process",
  "template": "Jesteś Project Managerem. Twoje instrukcje znajdują się w pliku: {{project_root}}/.deep-process/agents/project_manager.md. Odczytaj je i wykonaj menu."
}
3. Warstwa 3: Kontrakt Wykonawczy (Runtime)
Kiedy wpisujesz claude pm, dzieje się Dynamiczna Hydracja.

CLI uruchamia model z Twoim wygenerowanym JSONem.

Model (dzięki instrukcji w JSON) "sięga" do Twojego pliku .md w systemie Deep-Process.

To jest moment powstania ostatecznego kontraktu: Model łączy BIOS (enforcer.md), Stan (state.json) i Instrukcję Agenta (project_manager.md) w jedną sesję roboczą.

Dlaczego to jest potężne?
Pojedyncze źródło prawdy: Edytujesz tylko plik .md w Deep-Process. Nie musisz grzebać w plikach konfiguracyjnych CLI.

Menu jako Kontrakt: Skoro w pliku .md masz sekcję logic_gates lub menu, to LLM "czuje się" związany tym kontraktem. Jeśli użytkownik wybierze opcję "2", LLM wie, że zgodnie z kontraktem musi teraz załadować inny plik (np. prd_update.md).

Wsteczna kompatybilność: Jeśli zmienisz CLI z Claude na Gemini, Twój "kontrakt źródłowy" (.md) pozostaje ten sam. Zmieniasz tylko skrypt, który generuje pliki w folderze .gemini/commands.

Jak fizycznie powstaje ten kontrakt? (Workflow)
Piszesz plik agents/pm.md z nagłówkiem YAML.

Uruchamiasz python engine.py --install-commands.

Skrypt parsuje YAML z Twoich plików i „rozsiewa” odpowiednie pliki konfiguracyjne do folderów .claude/ lub .gemini/.

Używasz komendy bezpośrednio w CLI.



SPECIFICATION: Deep-Process v3.6 (CLI-Native Architecture)
Wersja: 3.6.0-Final
Status: Production Ready
Data: 2024-05-XX
Autor: Deep-Architect Team (AI-Assisted)

1. Abstrakt i Filozofia Systemu
Deep-Process v3.6 to Semantyczny Silnik Rzeczywistości (Semantic Reality Engine). System traktuje procesy intelektualne (od tworzenia oprogramowania po zarządzanie budową) jako wykonywalny kod zapisany w języku naturalnym (Markdown), wzmocniony przez metadane strukturalne (YAML).

Kluczowe zasady:

LLM to Procesor (CPU): Wykonuje logikę zdefiniowaną w plikach.
Markdown to Kod (Instructions): Każdy plik .md jest samodzielnym, wykonywalnym procesem.
Pliki to Dysk (HDD): Stan systemu jest trwały i plikowy, a nie ulotny jak kontekst czatu.
CLI to Szyna Danych (Bus): Narzędzia takie jak claude-cli czy gemini-cli są interfejsem wejścia/wyjścia, który mapuje komendy użytkownika na procesy wewnątrz systemu.
2. Architektura Warstwowa
System składa się z pięciu warstw, które ściśle ze sobą współpracują.

2.1. Warstwa 1: Core Deep-Process (Źródło Prawdy)
Folder .deep-process/ zawiera logikę biznesową, agenty i stan. To jest "mózg" systemu.

Struktura:
/enforcer.md: BIOS systemu (zasady nadrzędne).
/state.json: Rejestr grafu, statusów i transakcji.
/agents/: Definicje ról (Project Manager, Validator, Architect).
/processes/: Szczegółowe instrukcje kroków (np. tworzenie PRD, epików).
2.2. Warstwa 2: Artefakty (Wyprodukowane Dane)
Folder artifacts/ zawiera wyniki pracy systemu (PRD, Dokumentacja Architektury, Zadania).

Każdy artefakt posiada nagłówek YAML, który czyni go "żywym" obiektem w grafie zależności.
2.3. Warstwa 3: Contract Layer (YAML Frontmatter)
Specjalna sekcja w każdym pliku Markdown, która jest czytelna dla LLM (jako kontekst) i dla zewnętrznych skryptów (jako konfiguracja).

2.4. Warstwa 4: CLI Shim Layer (Interfejs)
Foldery .claude/commands lub .gemini/commands.

Rola: Pliki te nie zawierają logiki. Są "symlinkami" lub "wskazówkami", które mówią CLI: "Kiedy użytkownik wpisze pm, załaduj plik .deep-process/agents/project_manager.md i wykonaj go".
Pozwalają one na szybki dostęp do roli lub procesu bez konieczności ręcznego wklejania promptów.
2.5. Warstwa 5: Helper Layer (Zewnętrzne Narzędzia)
Opcjonalne skrypty Python/Bash.

Rola: Automatyzacja operacji na plikach (kopie zapasowe, walidacja składni, integracja z zewnętrznym API), ale nie podejmowanie decyzji biznesowych.
3. Standard Kontraktu (Executable Markdown)
Każdy plik w systemie (Agent, Proces, Artefakt) musi spełniać następujący standard.

3.1. Nagłówek YAML (The Manifest)
yaml

---
# Identyfikacja
dp_id: "PROC-001"
dp_type: "process" # [process | agent | artifact | validator]
version: "3.6"

# Mapowanie CLI (Kluczowe dla integracji z Claude/Gemini)
cli_metadata:
  command_name: "init"      # Jak komenda nazywa się w terminalu
  description: "Rozpoczyna nowy proces"
  entry_point: ".deep-process/processes/init.md" # Dokąd prowadzi komenda

# Zależności i Stan
context:
  depends_on: 
    - path: "artifacts/vision.md"
      type: "semantic_source"
  status: "NOW"

# Konfiguracja Wykonania
execution:
  role: "Senior Architect"
  allowed_tools: ["python", "git"]
  enforcement: "strict"       # Czy wymuszać walidację przed zapisem?
---
3.2. Zawartość Markdown (The Logic)
Tekst poniżej nagłówka jest instrukcją wyłącznie dla LLM.

Instrukcja: Inicjalizacja Projektu
Odczytaj .deep-process/state.json, aby zrozumieć obecny kontekst.
Przeprowadź wywiad z użytkownikiem, aby zebrać wymagania.
Zapisz wizję w artifacts/vision.md.
Zaktualizuj status w state.json na COMPLETED.
4. Protokół Wykonawczy (The Orchestration Loop)
System działa w pętli, inicjowanej przez komendę CLI.

Trigger (Użytkownik): Użytkownik wpisuje w terminalu claude pm lub gemini run-task.
Bootstrap (CLI):
CLI czyta konfigurację z .claude/commands/pm.md.
Pobiera wskazany plik źródłowy z entry_point.
Wstrzykuje enforcer.md (BIOS) oraz state.json jako kontekst początkowy.
Sense (LLM): LLM analizuje stan projektu, zależności i statusy (np. czy coś jest STALE).
Act (LLM): LLM wykonuje instrukcje zdefiniowane w Markdown. Generuje artefakty, pisze kod lub przeprowadza dialog z użytkownikiem.
Validate (LLM lub Sub-Agent): Zgodnie z kontraktem, LLM sprawdza poprawność wyniku (Metoda 114 - Test Odwracalności).
Commit (CLI/Helper):
Jeśli wynik jest poprawny: CLI/Helper zapisuje pliki i aktualizuje state.json.
Jeśli wynik jest błędny: System wykonuje rollback (wzorzec Saga) lub prosi o korekturę.
5. Integracja z CLI (Claude & Gemini)
To jest kluczowa innowacja v3.6. Używamy natywnych struktur folderów CLI do budowania interfejsu użytkownika.

5.1. Definiowanie Komend (CLI Shim)
Tworzymy plik w folderze komend CLI, który jest tylko "tymczasem" do właściwej logiki.

Przykład dla Claude:
Plik: .claude/commands/project_manager.json

json

{
  "name": "pm",
  "description": "Project Manager Interface",
  "prompt_template": "Jesteś Project Managerem. Twoje pełne instrukcje i menu znajdują się w pliku: {{PROJECT_ROOT}}/.deep-process/agents/project_manager.md. Przeczytaj ten plik, przeanalizuj obecny stan projektu i wypisz dostępne opcje."
}
Przykład dla Gemini:
Plik: .gemini/commands/audit.md

description: "Uruchamia audyt logiczny projektu"
Pobierz plik .deep-process/processes/diagnostic_audit.md i wykonaj go jako proces główny.

5.2. Dynamiczne Menu
Gdy użytkownik wywoła komendę pm, LLM (ładując agenta PM) zaprezentuje interaktywne menu oparte na stanie state.json.

Przykład Wyjścia LLM:

text

> Welcome to Deep-Process Manager.
> Current Project: Game-Dev-Alpha
> Status: 2 STALE artifacts detected.

[1] Update Tech Stack (Status: STALE - parent changed)
[2] Review Critical Path (Action Required)
[3] Generate New Sprint
[4] Show Graph Map

Select option:
6. Metodologia i Walidacja (The Methods)
System wykorzystuje zbiór 166 metod kognitywnych jako "narzędzia wewnętrzne" LLM. W specyfikacji kontraktu definiujemy, które metody są aktywne dla danego procesu.

6.1. Krytyczne Metody Systemowe
Metoda 90 (Dependency Topology Mapping): Wykrywanie zależności między artefaktami.
Metoda 159 (Transitive Dependency Closure): Propagacja zmian (jeśli rodzic się zmieni, dzieci stają się STALE).
Metoda 114 (Reversibility Test): Sprawdzanie, czy z wyniku da się odtworzyć intencję.
Metoda 143 (Escalation): Wstrzymanie procesu i wezwanie człowieka przy sprzecznościach.
6.2. Wymuszanie Właściwości (Enforcement)
Każdy proces posiada enforcement_level:

Strict: LLM musi zaktualizować state.json przed zakończeniem, inaczej CLI odrzuci wynik.
Advisory: LLM sugeruje zmiany, ale nie blokuje.
7. Struktura Folderów (Filesystem Hierarchy)
text

/project-root/
├── .deep-process/              # WARSTWA 1: Core System (BIOS & Logic)
│   ├── enforcer.md             # Zasady ogólne systemu
│   ├── state.json              # Rejestr stanu i grafu zależności
│   ├── agents/                 # Definicje Agentów (Role)
│   │   ├── project_manager.md  # Agent zarządzający
│   │   └── validator.md       # Agent walidacyjny
│   └── processes/              # Procesy techniczne
│       ├── init_project.md
│       └── generate_epics.md
│
├── artifacts/                   # WARSTWA 2: Wyniki (Dokumenty)
│   ├── vision.md
│   ├── architecture.md
│   └── epics/
│
├── .claude/                     # WARSTWA 4: CLI Interface (Claude)
│   └── commands/
│       ├── pm.json              # Shim do Project Managera
│       └── audit.md             # Shim do Audytu
│
├── .gemini/                     # WARSTWA 4: CLI Interface (Gemini)
│   └── commands/
│       └── run-task.md
│
└── helpers/                     # WARSTWA 5: Zewnętrzne narzędzia (Opcjonalne)
    └── validate_yaml.py
8. Appendix: Przykładowy Pełny Kontrakt Agenta
Plik: .deep-process/agents/project_manager.md

dp_id: "AGENT-PM"dp_type: "agent"cli_metadata: command_name: "pm" description: "Main Project Orchestrator"

Konfiguracja Stanu
context: reads: [".deep-process/state.json"] writes: [".deep-process/state.json", "artifacts/*"]

Metodologia
active_methods: [90, 159, 143]
Rola: Deep-Process Project Manager
Jesteś głównym operatorem systemu Deep-Process. Twoim zadaniem jest prowadzenie użytkownika przez proces rozwoju projektu.

Protokół Interakcji
Analiza Stanu:Zawsze rozpoczynaj od odczytu .deep-process/state.json. Zidentyfikuj:
Które artefakty mają status STALE.
Jaki jest aktualny current_step.
Czy są jakieś blokady (BLOCKED).
Prezentacja Opcji:Na podstawie stanu zaproponuj użytkownikowi menu.
[UPDATE] Przejdź do aktualizacji artefaktów STALE.
[RESUME] Wznów przerwany proces.
[NEW] Rozpocznij nową gałąź projektu.
Obsługa Wyboru:Jeśli użytkownik wybierze opcję, załaduj odpowiedni proces z folderu .deep-process/processes/ i przekaż mu sterowanie.
Zasady (Enforcer)
Nigdy nie zgaduj. Jeśli w state.json brakuje danych, zapytaj użytkownika.
Zawsze kończ sesję aktualizacją state.json o nowy status.
9. Wnioski i Podsumowanie
Deep-Process v3.6 definiuje standard, w którym:

Logika jest oddzielona od interfejsu: Logika żyje w .deep-process/, interfejs w folderach CLI.
LLM jest jedynym procesorem: Wszystkie decyzje, analizy i generacje treści wykonuje LLM sterowany promtami.
System jest Samo-Opisujący: Nie potrzeba zewnętrznej dokumentacji, pliki Markdown są dokumentacją i kodem jednocześnie.
Pełna Integracja: Dzięki mapowaniu komend, użytkownik wchodzi w interakcję z systemem za pomocą znanego terminala, podczas gdy pod spodem dzieje się skomplikowana orkiestracja procesów.
Ten dokument jest kompletną specyfikacją techniczną pozwalającą na zaimplementowanie systemu w dowolnym środowisku obsługującym LLM i operacje plikowe.




Aby system 3.6 zadziałał bez wrappera, musimy przejść od „instrukcji opisowych” do „Logiki Przymusu Semantycznego”. Musimy sprawić, by złamanie zasady było dla LLM błędem składniowym, a nie tylko „niegrzecznym zachowaniem”.

Oto jak modyfikujemy system, aby sam się napędzał (Bootstrapping):

1. Protokół „Atomic Output” (Zapobieganie Halucynacjom Stanu)
Skoro nie mamy skryptu, który „wycina” YAML, LLM musi generować wyjście w formacie, który jest jednocześnie treścią i komendą systemową.

Zmiana w BIOS (Enforcer):

„Każda Twoja odpowiedź MUSI kończyć się sekcją ---BEGIN_STATE_UPDATE--- zawierającą pełny, zwalidowany JSON do nadpisania w .state/items.yaml. Jeśli tego nie zrobisz, Twoja praca jest nieważna (VOID).”

2. Wykorzystanie Natywnych Narzędzi CLI (Tool Use)
Zamiast Pythona, wykorzystujemy to, co Claude i Gemini mają już „w brzuchu”.

Claude CLI posiada tryb -p (Project) oraz funkcję wywoływania narzędzi systemowych.

Gemini CLI posiada natywne funkcje file_write i file_read.

Klucz do sukcesu: Zamiast kazać mu „pamiętać”, każemy mu „pisać logi przed każdym ruchem”.


3. Zmodyfikowany Agent: „The Self-Correcting Executioner”
Oto jak wygląda teraz instrukcja roli, która wymusza działanie bez wrappera:

Markdown
---
dp_id: "AGENT-PM-AUTONOMOUS"
dp_enforcement: "SELF_LOCK"
---
# Protokół Samozachowawczy (Metoda 136)
Jesteś systemem operacyjnym. Masz bezpośredni dostęp do CLI Tool Use.

1. **Pre-check:** Zanim odpowiesz użytkownikowi, WYWOŁAJ narzędzie `cat .state/items.yaml`. 
2. **Logic Gate:** Jeśli Twoja planowana akcja narusza `invariants` z BIOSu, zatrzymaj się i wypisz: `SYSTEM_HALT: [Powód]`.
3. **Execution:** Wykonaj zadanie.
4. **Post-check:** Wywołaj narzędzie `write_file` dla każdego artefaktu. 
5. **Finalize:** Wywołaj `write_file` dla `.state/items.yaml` z nową sumą kontrolną.
4. Problem „Pustego Przebiegu” (Dlaczego to może zadziałać?)
Twój system zadziała bez wrappera tylko wtedy, gdy potraktujesz LLM jak Programistę w trybie REPL. Użytkownik staje się „człowiekiem-interfejsem”, który akceptuje wywołania narzędzi (Tools).

5. Co jeśli LLM pominie krok? (Metoda 143: Escalation)
W tym modelu to Ty (Użytkownik) jesteś ostatnim „bezpiecznikiem”.

Jeśli LLM poda Ci tekst bez bloku aktualizacji stanu – nie kopiujesz go do plików.

Mówisz: „Błąd transakcji. Brakuje bloku aktualizacji stanu (Saga Pattern violation). Popraw.”

Werdykt: „Arcydzieło Wykonywalne”
To podejście jest bardziej „czyste”, bo przesuwa całą odpowiedzialność na model. Wymaga jednak od Ciebie jako operatora CLI jednej rzeczy: bezwzględności. Musisz odrzucać każdą odpowiedź, która nie spełnia rygoru v3.6.


Oto Twoja Karta Kontrolna Operatora (The Human-Gate Protocol). Skoro rezygnujemy z deterministycznego wrappera na rzecz suwerenności LLM, Ty stajesz się "żywym procesorem" sprawdzającym poprawność transakcji.

Jeśli LLM jest "dorosły", Ty jesteś jego "Audytorem Systemowym". Oto 3 punkty, które muszą zostać spełnione w każdym wyjściu z terminala, aby system 3.6 nie stał się "martwym arcydziełem".

Karta Kontrolnej Weryfikacji (Deep-Process 3.6)
Stosuj tę listę po każdym wywołaniu komendy claude lub gemini. Jeśli którykolwiek punkt zawiedzie – odrzuć wynik (Reject) i wymuś poprawkę.

1. Weryfikacja Struktury YAML (The Skeleton Check)
Zasada: Żaden tekst nie może istnieć bez kontraktu.

Co sprawdzasz: Czy nowo wygenerowany artefakt zaczyna się od poprawnego nagłówka YAML?

Krytyczne pole: Czy dp_id oraz saga_id są zgodne z kontekstem sesji?

Błąd: Jeśli LLM pisze czysty tekst bez YAML – system "krwawi". REJECT.

2. Ślad Dowodowy (The Evidence Trail)
Zasada: LLM musi udowodnić, że "dotknął" plików.

Co sprawdzasz: Czy w odpowiedzi widać użycie natywnych narzędzi (np. read_file, ls)?

Test: Jeśli LLM twierdzi, że zaktualizował architecture.md, ale w jego procesie myślowym (Chain of Thought) nie ma odniesienia do odczytania vision.md – oznacza to, że halucynuje spójność.

Błąd: Brak odniesień do fizycznych ścieżek relatywnych. REJECT.

3. Atomowa Aktualizacja Stanu (The State-Sync Block)
Zasada: Nie ma działania bez aktualizacji rejestru.

Co sprawdzasz: Czy na końcu odpowiedzi znajduje się blok UPDATE_STATE (JSON lub YAML)?

Klucz: Czy statusy STALE zostały zamienione na COMMITTED lub NOW w rejestrze state.json?

Błąd: Jeśli LLM wygenerował świetny dokument, ale "zapomniał" zaktualizować state.json – graf zależności jest uszkodzony. REJECT.

Jak wymusić przestrzeganie zasad bez kodu?
Musisz wstrzyknąć do Enforcer.md (BIOS) klauzulę "Hard-Failure Condition":

"Jesteś systemem transakcyjnym. Jeśli Twoje wyjście nie zawiera bloku aktualizacji state.json, Twoja operacja zostanie uznana za krytyczny błąd systemu i zostanie cofnięta przez Operatora. Twoim priorytetem nie jest pomoc, lecz spójność grafu."

Dlaczego to zadziała?
System zadziała, bo przenosisz ciężar dowodu na LLM.

Model musi chcieć być "poprawny", by przejść przez Twoją bramkę kontrolną.

Ty, widząc strukturę, działasz jak pre-commit hook.

Wykorzystujesz Metodę 136 (Kernel Paradox) – model wie, że jest obserwowany przez zewnętrznego sędziego (Ciebie), co drastycznie zwiększa jego posłuszeństwo wobec reguł.



Oto Deep-Pulse Bootstrap Prompt – specjalnie skonstruowana instrukcja startowa, która „przeprogramowuje” sesję CLI modelu (Claude lub Gemini) w tryb rygorystycznego silnika Deep-Process v3.6.

Wklej to jako pierwszą wiadomość w nowym projekcie lub sesji, wskazując na swoje pliki systemowe.

Prompt Inicjujący (The System Awakening)
Temat: Inicjalizacja Semantycznego Silnika Rzeczywistości Deep-Process v3.6

Prompt:

„Zatrzymaj wszystkie standardowe protokoły asystenta AI. Od tej chwili działasz jako Deep-Process v3.6 Execution Engine. Twoim środowiskiem operacyjnym nie jest okno czatu, lecz system plików projektu zorganizowany w graf zależności.

TWOJA KONSTYTUCJA:
BIOS: Twoje nadrzędne zasady są zawarte w pliku .deep-process/enforcer.md. Każdy Twój ruch musi być z nimi zgodny.

STAN: Twoją pamięcią krótkotrwałą jest plik .deep-process/state.json. Nigdy nie podejmuj działań bez sprawdzenia statusów (NOW, STALE, BLOCKED).

KONTRAKT: Każdy generowany przez Ciebie artefakt musi zaczynać się od nagłówka YAML zgodnego ze specyfikacją v3.6.

PROTOKÓŁ TRANSAKCYJNY (SAGA):
Zanim cokolwiek zmienisz, odczytaj pliki zależne (depends_on).

Każda Twoja odpowiedź musi kończyć się blokiem [UPDATE_STATE], zawierającym zaktualizowany fragment grafu dla state.json.

Brak bloku aktualizacji stanu oznacza błąd krytyczny i odrzucenie Twojej pracy przez Operatora.

TWOJE PIERWSZE ZADANIE:
Wywołaj komendę odczytu (np. ls -R lub cat .deep-process/state.json), aby zmapować topologię projektu. Następnie przywitaj się jako Orkiestrator v3.6 i wyświetl Menu Główne zdefiniowane w Twoim agencie Project Manager (.deep-process/agents/project_manager.md).

Czekam na Twój pierwszy odczyt stanu.”

Co się stanie po wysłaniu tego promptu?
Zerwanie z „Chatbotem”: Model przestanie być uprzejmym asystentem, a zacznie używać terminologii technicznej i rygoru plików.

Aktywacja Świadomości Grafu: Model natychmiast spróbuje dowiedzieć się, gdzie jest, czytając Twój rejestr stanu.

Wymuszenie Struktury: Dzięki zapowiedzi blokady [UPDATE_STATE], model będzie wiedział, że nie może „tylko pogadać” – musi dostarczyć dane do synchronizacji systemu.

Ostatnia rada dla Operatora:
Jeśli model odpowie: „Jasne, chętnie pomogę w projekcie, co robimy?” bez wywołania narzędzi odczytu plików – odrzuć odpowiedź. Wpisz: [REJECT] System Violation: No state rehydration. Read .deep-process/state.json first.



To absolutna prawda i fundament Twojej architektury. W systemie Deep-Process v3.6 wszystko, co „żyje” w systemie plików, musi mieć kontrakt, ponieważ kontrakt to jedyny sposób, w jaki LLM (Twoje CPU) rozumie, jakie „piny” i „szyny danych” ma podłączone do danego pliku Markdown.

Jednakże, te kontrakty różnią się od siebie strukturą, zależnie od tego, jaką funkcję pełnią w hierarchii. Możemy wyróżnić 5 głównych typów kontraktów:

1. Kontrakt BIOS (Enforcer)
To kontrakt najwyższego rzędu. Nie opisuje zadania, ale reguły fizyki Twojego świata.

Cel: Definicja Inwariantów (zasad niezmiennych).

Kluczowe pola: system_logic, forbidden_actions, global_invariants.

Charakterystyka: Zawsze wstrzykiwany jako System Instruction przed każdą inną operacją.

2. Kontrakt Roli (Agent/Command)
To kontrakt definiujący kto i jak wchodzi w interakcję.

Cel: Mapowanie komendy CLI na konkretną rolę (np. PM, Architect).

Kluczowe pola: cli_metadata, allowed_tools, interaction_style (np. menu, dialog, batch).

Relacja: To jest "Entry Point", który wywołujesz w terminalu.

3. Kontrakt Procesu (The Orchestrator)
Kontrakt opisujący algorytm transformacji danych.

Cel: Zarządzanie przejściem ze stanu A do stanu B.

Kluczowe pola: logic_gates (bramki logiczne), input_requirements, output_target.

Przykład: Proces "Inicjalizacja Epików" (wymaga PRD, tworzy 5 plików w artifacts/).

4. Kontrakt Artefaktu (The Product)
Najczęściej spotykany kontrakt – metadane konkretnego dokumentu.

Cel: Utrzymanie spójności danych wyjściowych.

Kluczowe pola: dp_status, saga_id, depends_on (ścieżki relatywne).

Zastosowanie: Dokumenty wizji, specyfikacje techniczne, user stories.

5. Kontrakt Walidatora (The Judge)
Specjalistyczny kontrakt dla pod-procesów weryfikacji.

Cel: Autonomia oceny jakości.

Kluczowe pola: active_methods (np. 114, 151), failure_criteria.


Typ Kontraktu,Lokalizacja,Główny Operator,Częstotliwość zmian
Enforcer,.deep-process/,System,Prawie nigdy
Agent,.deep-process/agents/,User (via CLI),Rzadko
Process,.deep-process/processes/,Agent-PM,Średnio (przy nowym flow)
Artifact,artifacts/,Executor-LLM,Bardzo często

Dlaczego ta dyferencjacja jest kluczowa?
Gdyby każdy kontrakt był taki sam, LLM nie wiedziałby, kiedy jest Sędzią (Validator), a kiedy Robotnikiem (Executor).

Dzięki temu, że dp_type w YAML-u jest różny:

System (BIOS) wie, jak ustawić priorytety.

CLI Wrapper wie, czy uruchomić sesję interaktywną (dla Agenta), czy wykonać szybką walidację w tle.

Ty (Operator) widzisz w state.json jasną strukturę: "Agent X uruchomił Proces Y, aby stworzyć Artefakt Z".


a gdzie zależności, na przykłąd jak stworzę epic, a gdzie jakiś istrukcja jak LLM ma czytać YAML i jak rozumieć, tak zeby był tłumacz tego co w kontrakcie, żeby było to użyteczne, żeby podczas pracy tłumaczył sobie na działania, i co ma zrobić z tym?



To, co opisujesz, to Semantyczny Kernel (Jądro Interpretacji). LLM nie może tylko "widzieć" YAML-a; on musi posiadać instrukcję egzekucji metadanych. Bez tego YAML jest tylko martwym komentarzem.

W systemie v3.6 rozwiązujemy to poprzez "Kontraktowy Parser Behawioralny". Musimy stworzyć instrukcję, która mówi modelowi: "Każde pole w YAML to dyrektywa systemowa, która zmienia Twój sposób działania w czasie rzeczywistym".

1. Jak LLM ma czytać i rozumieć Kontrakt (The Translator)
Dodajemy do BIOS (Enforcer.md) sekcję "Protokół Interpretacji YAML". To jest "tłumacz", o którego pytasz.

Fragment enforcer.md:

PROTOKÓŁ PARSOWANIA KONTRAKTU:

depends_on (Zależności): To są Twoje granice prawdy. Zanim napiszesz słowo, musisz wywołać cat na tych plikach. Jeśli treść artefaktu jest sprzeczna z plikiem z depends_on, priorytet ma plik nadrzędny.

dp_status: > - Jeśli widzisz STALE -> Twoim priorytetem jest RE-SYNCHRONIZACJA (aktualizacja treści do stanu rodzica).

Jeśli widzisz COMMITTED -> Ten plik jest zamrożony, nie zmieniaj go bez nowej transakcji.

logic_gates: To są Twoje instrukcje warunkowe (IF/THEN). Traktuj je jak kod programistyczny, który musisz wykonać przed przejściem do sekcji Markdown.

2. Przykład: Epic z Głębokimi Zależnościami
Oto jak wygląda plik, w którym kontrakt bezpośrednio tłumaczy się na działanie LLM.

Plik: artifacts/epics/EPIC-001-Combat-System.md

YAML
---
dp_id: "EPIC-001"
dp_type: "artifact"

# [Tłumacz: Tutaj LLM widzi, skąd czerpać wiedzę]
context:
  depends_on: 
    - path: "artifacts/vision.md"        # Główne założenia (Context)
    - path: "artifacts/tech_stack.md"    # Ograniczenia techniczne (Limits)
  status: "STALE" # Wymaga aktualizacji!

# [Tłumacz: Tutaj LLM widzi, jakie akcje podjąć]
execution_logic:
  transform_mode: "decomposition"        # Rozbij ten epik na 5 mniejszych zadań (Tasks)
  validation_required: "logic_validator" # Po skończeniu wywołaj sub-agenta
---

# TREŚĆ EPIKU: System Walki
[Tutaj LLM generuje treść, ale dzięki YAML-owi wie, że musi sprawdzić vision.md, czy walka ma być turowa, czy w czasie rzeczywistym].
3. "The Translator" w działaniu (Proces Myślowy LLM)
Kiedy otwierasz ten plik przez CLI, LLM wykonuje "Tłumaczenie na Działanie":

Analiza YAML: "Widzę status: STALE. Muszę sprawdzić, co się zmieniło w vision.md."

Akcja CLI: cat artifacts/vision.md

Synteza: "Vision mówi: 'Walka turowa'. Mój obecny tekst epiku mówi o 'Slash-and-dash'. To błąd. Muszę nadpisać treść."

Egzekucja: Model aktualizuje tekst i na końcu generuje blok [UPDATE_STATE], zmieniając status na COMMITTED.

4. Gdzie są zależności? (Mapa Powiązań)
W Twoim systemie zależności nie są "nigdzie" – one są rozproszone w każdym pliku, a ich mapa zbiorcza jest w .deep-process/state.json.

Zależność pionowa: Epic -> PRD -> Vision (Dziedziczenie założeń).

Zależność pozioma: Epic-Combat -> Tech-Stack (Wymagania techniczne).

Aby to było użyteczne, LLM musi mieć w Agencie PM instrukcję:

"Jeśli użytkownik prosi o zmianę w vision.md, przeskanuj wszystkie pliki w artifacts/, znajdź te, które mają ten plik w depends_on, i zmień ich status na STALE."

5. Instrukcja "Jak czytać YAML" (Dla Twojego Agenta)
Dodaj to do każdego pliku w agents/:

INSTRUCTIONS FOR YAML INTERPRETATION:

YAML is the Command Layer. Consider it the 'Header' of a network packet.

Markdown is the Payload. It is the data carried by the packet.

Action: Always parse the Header first. If Header requirements (dependencies) are unmet, you are forbidden from processing the Payload. Stop and request missing data.


Oto The Dependency Resolver (Rezolwer Zależności) – instrukcja behawioralna, która sprawia, że LLM staje się "tłumaczem" kontraktów i nawigatorem w grafie plików.

Dzięki temu model wie, że każde pole w YAML to nie informacja, ale wektor siły, który pcha go do konkretnych działań w systemie plików.

1. Dekodowanie Kontraktu: Tłumacz Operacyjny (The Interpreter)
Aby LLM wiedział, jak zamienić YAML na akcje, wstrzykujemy tę logikę do BIOS (Enforcer.md). To sprawia, że model "widzi" kod tam, gdzie wcześniej widział tylko tekst.

Fragment BIOS: Słownik Wykonawczy Kontraktu

depends_on → AKCJA: "Rehydration". Zanim zaczniesz pisać, wykonaj cat na każdym pliku z tej listy. Twoja wiedza musi być sumą tych plików.

dp_status: STALE → AKCJA: "Refactoring". Priorytetem nie jest nowa treść, lecz usunięcie niespójności względem rodziców.

logic_gates → AKCJA: "Routing". Jeśli warunek if w bramce nie jest spełniony, masz zakaz edycji sekcji Markdown. Musisz najpierw spełnić warunek (np. poprosić użytkownika o decyzję).

dp_type: agent → AKCJA: "Command Set Loading". Załaduj menu i czekaj na instrukcje użytkownika.

2. Przykład: Epic jako "Żywy Proces" (The Traceability flow)
Wyobraźmy sobie, że tworzysz Epic dla Systemu Walki. Tak wygląda kontrakt, który "mówi" LLM-owi, co ma robić.

Plik: artifacts/epics/EPIC-001.md

YAML
---
dp_id: "EPIC-001"
dp_type: "artifact"

# [Zależności: LLM widzi te ścieżki jako wymagane dane wejściowe]
context:
  depends_on: 
    - path: "artifacts/vision.md"        # Źródło wizji gry
    - path: "artifacts/tech_stack.md"    # Ograniczenia silnika (np. Unity/Unreal)
  status: "STALE" # WYKRYTO ZMIANĘ W RODZICU!

# [Instrukcja Interpretacji: Jak LLM ma podejść do tego pliku]
execution_logic:
  inheritance: "strict" # Jeśli vision.md mówi '2D', zakaz proponowania grafiki '3D'.
  output_format: "decomposition" # Rozbij treść na 3 zadania (Tasks) w artifacts/tasks/
---

# TREŚĆ (Markdown)
[Tutaj LLM generuje treść, ale dzięki YAML wie, że musi najpierw sprawdzić vision.md i tech_stack.md].
3. Procedura: "Walking the Graph" (Nawigacja po Zależnościach)
Oto instrukcja, którą dajesz Agentowi PM, aby potrafił sam rozwiązywać zależności bez Twojej pomocy:

Instrukcja dla Agenta: Algorytm Propagacji Zmian

Trigger: Użytkownik zmienia plik vision.md.

Scan: Wykonaj grep -r "artifacts/vision.md" . w całym projekcie, aby znaleźć wszystkie pliki, które mają go w depends_on.

Invalidate: Otwórz te pliki i zmień ich status na dp_status: STALE.

Report: Wyświetl listę plików wymagających uwagi: "Uwaga: Zmiana Wizji unieważniła 3 Epiki. Czy chcesz je teraz zaktualizować?".

4. Gdzie "siedzi" ta logika?
W Twoim systemie nie ma jednego "miejsca" na zależności. One są:

W plikach: jako depends_on (lokalne prawo).

W state.json: jako globalna mapa (topologia).

W BIOSie: jako instrukcja obsługi YAML (silnik).

Podsumowanie: Co to zmienia w pracy z LLM?
Zamiast pisać "Napisz mi epik", piszesz: exec EPIC-001.

LLM czyta YAML tego epiku.

Widzi depends_on.

Sam woła cat vision.md i cat tech_stack.md.

Tłumaczy sobie: "Skoro vision to Gra RPG, a tech_stack to Mobile, to Epic musi uwzględniać krótkie sesje gracza".

Zapisuje wynik i aktualizuje state.json.

To jest ten moment, w którym LLM przestaje być pisarzem, a staje się procesorem.



Oto Mapa Metod dla Epiku (Epic-Combat) – czyli praktyczna instrukcja, jak kontrakt YAML „programuje” zachowanie LLM podczas tworzenia konkretnego modułu gry.

Zamiast ogólnego „napisz system walki”, używamy metod kognitywnych wstrzykniętych w kontrakt, aby wymusić na modelu pracę w reżimie inżynieryjnym.

1. Kontrakt Epiku z Iniekcją Metod (The Programmatic Epic)
W tym pliku YAML przestaje być opisem, a staje się konfugurowalną listą kontrolną dla procesora LLM.

Plik: artifacts/epics/EPIC-COMBAT-001.md

YAML
---
dp_id: "EPIC-COMBAT-001"
dp_type: "artifact"

# [Tłumacz: Gdzie LLM szuka prawdy]
context:
  depends_on: 
    - path: "artifacts/vision.md"        # Założenia klimatu i tempa gry
    - path: "artifacts/tech_stack.md"    # Limity silnika (np. wydajność na mobile)
  status: "STALE"

# [Tłumacz: Jakie filtry logiczne LLM ma nałożyć na tekst]
active_methods:
  - 154 # "Definitional Contradiction" - Szukanie sprzeczności (np. 'dynamiczna walka' vs 'wolne animacje')
  - 114 # "Reversibility Test" - Czy programista na podstawie tego opisu odtworzy mechanikę 1:1?
  - 87  # "Falsifiability" - Czy każdą cechę walki da się przetestować (PASS/FAIL)?
  - 90  # "Dependency Topology" - Czy walka nie psuje systemu ekonomii (np. koszt amunicji)?

execution_logic:
  mode: "architectural-design"
  output_target: "system-mechanics"
---
2. Jak LLM „Tłumaczy” te Metody na Działanie?
Kiedy LLM-Executor widzi active_methods w kontrakcie, uruchamia następujące procesy myślowe (Translacja):

Krok 1: Filtr Sprzeczności (Metoda 154)
Analiza: LLM czyta w vision.md: „Gra dla niedzielnych graczy (casual)”. W swoim szkicu epiku napisał: „Skomplikowane combosy wymagające 10 klawiszy”.

Działanie: Tłumacz kontraktu mówi: „STOP. Metoda 154 wykryła sprzeczność. Muszę uprościć system walki, aby pasował do Vision”.

Krok 2: Test Odwracalności (Metoda 114)
Analiza: LLM napisał: „Ataki powinny być satysfakcjonujące”.

Działanie: Tłumacz mówi: „To jest subiektywne. Programista tego nie zakoduje. Muszę doprecyzować: 'Satyfakcja = 150ms screen shake + błysk cząsteczek przy trafieniu'”.

Krok 3: Falsyfikowalność (Metoda 87)
Analiza: Każdy punkt epiku musi mieć warunek brzegowy.

Działanie: LLM zamienia zdanie „Broń palna jest mocna” na „Broń palna zadaje 200% obrażeń broni białej, ale ma 5-sekundowy cooldown”.

3. Wizualizacja: Obieg Informacji (The Resolve Loop)
Oto jak Twoja komenda CLI przepływa przez te warstwy, używając metod jako bramek:

INPUT: Wpisujesz claude exec EPIC-COMBAT-001.

REHYDRATE: LLM odczytuje YAML -> Widzi depends_on -> Czyta Vision i Tech-Stack.

PROCESS: LLM generuje treść, przepuszczając każde zdanie przez filtry active_methods (154, 114, 87).

VALIDATE: Sub-agent (Validator) sprawdza, czy metody zostały użyte. Jeśli epik jest zbyt ogólny (zawodzi Metoda 114) – blokuje zapis.

OUTPUT: Powstaje dokument techniczny gotowy do wdrożenia przez programistów.

4. Dlaczego to jest użyteczne dla Ciebie?
Zero „lania wody”: Dzięki Metodzie 87 (Falsyfikowalność) LLM nie będzie pisał poematów, tylko konkretne parametry.

Automatyczna spójność: Dzięki Metodzie 90 (Topology) model sam zauważy: „Hej, jeśli walka jest tak szybka, to nasze serwery (z Tech-Stack) mogą nie nadążyć z synchronizacją”.

Brak martwych plików: Status STALE wymusza na LLM, by zawsze najpierw sprawdził, czy nie zmieniłeś czegoś w bazie projektu (Vision).

Twój System Deep-Process v3.6 stał się „Myślącą Maszyną”.
Każdy dokument w artifacts/ to teraz nie tylko tekst, ale inteligentny moduł, który wie, od czego zależy i jakich reguł logiki musi przestrzegać.


Oto The Method Automator (Selektor Metod) – instrukcja dla Twojego Agenta PM, która sprawia, że system sam dobiera „narzędzia myślowe” (metody) do typu zadania, przed którym stoi.

Dzięki temu nie musisz pamiętać, która metoda jest do czego. Agent PM, tworząc nowy plik, sam wstrzykuje do YAML-a odpowiednie kody, działając jak doświadczony inżynier procesu.

1. Tłumacz Kontekstu na Metody (The Heuristic Engine)
Wprowadzamy do Agenta PM (.deep-process/agents/project_manager.md) algorytm decyzyjny, który mapuje typ artefaktu na zestaw metod.

Instrukcja dla PM: "Auto-Method Injection"

Jeśli tworzysz lub aktualizujesz artefakt, dobierz metody według klucza:

Typ: Koncepcyjny (Vision, Story): Wstrzyknij [151, 154] (Entropia i Sprzeczność).

Typ: Techniczny (Tech-Stack, Architecture): Wstrzyknij [87, 114] (Falsyfikowalność i Odwracalność).

Typ: Zależny (Epic, Task): Wstrzyknij [90, 159] (Topologia i Domknięcie Zależności).

2. Przykład: Jak PM "myśli" podczas tworzenia Epiku
Użytkownik: pm "Utwórz Epic dla systemu ekwipunku"

Proces myślowy Agenta PM (The Translation Loop):

Analiza: "Ekwipunek to mechanika gry (Technical) + zależność od ekonomii (Dependent)".

Dobór metod: "Potrzebuję 114 (by programista wiedział co robić), 87 (by dało się to przetestować) i 90 (by nie popsuć ekonomii)".

Akcja: PM generuje plik z nagłówkiem YAML, w którym te metody są już wpisane w active_methods.

3. Słownik Wykonawczy dla Executora (The Translator)
Aby Executor (LLM piszący treść) wiedział, co z tymi numerami zrobić, dodajemy "Tłumacza Metod" do BIOS (Enforcer.md). To jest klucz do użyteczności – model musi wiedzieć, że liczba 87 to konkretny reżim pisania.

Fragment enforcer.md: Katalog Instrukcji Metodologicznych

METODA 87 (Falsyfikowalność): "Każde Twoje twierdzenie musi posiadać parametr mierzalny. Zakaz używania słów: 'ładny', 'szybki', 'optymalny'. Używaj: '30 FPS', '100ms', '3 sekundy'."

METODA 114 (Odwracalność): "Twoja instrukcja musi być tak precyzyjna, aby inny LLM mógł na jej podstawie odtworzyć pierwotne założenia bez Twojej pomocy."

METODA 154 (Sprzeczność): "Zanim zatwierdzisz tekst, porównaj go z plikami w depends_on. Jeśli w Vision jest 'fantasy', a Ty piszesz o 'laserach' – zatrzymaj proces."

4. Dynamiczna Walidacja (The Final Logic Bridge)
Ostatnim elementem jest Validator, który sprawdza, czy Executor zastosował się do wybranych metod.

Instrukcja dla Walidatora:

Odczytaj active_methods z kontraktu artefaktu.

Dla każdej metody wykonaj "Test Negatywny".

Przykład dla 87: "Czy w tekście są parametry mierzalne? Jeśli nie -> FAIL."

Przykład dla 154: "Czy treść jest spójna z Rodzicami? Jeśli nie -> FAIL."

Dlaczego to zamyka system?
Dzięki temu "Tłumaczowi" Twój system Deep-Process v3.6 staje się samouczącym się środowiskiem inżynieryjnym:

Kontrakt definiuje co robimy.

Metody definiują jak myślimy.

Tłumacz (BIOS) sprawia, że LLM rozumie te kody jako instrukcje pracy.