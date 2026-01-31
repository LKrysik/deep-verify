# Deep Explore V2.1 — Knowledge-First Decision Exploration

---

## INVOCATION

**Kiedy użytkownik chce eksplorować decyzję, ZAWSZE rozpocznij od tego dialogu:**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      DEEP EXPLORE                                          ║
║                      Eksploracja przestrzeni decyzyjnej                    ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Zanim zaczniemy, wybierz głębokość eksploracji:                          ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [1] QUICK  (10-20 min)                                             │  ║
║  │                                                                      │  ║
║  │  Co dostaniesz:                                                      │  ║
║  │  • Podstawowa mapa opcji (3 wymiary minimum)                        │  ║
║  │  • Kluczowe konsekwencje dla top 2 opcji                            │  ║
║  │  • Szybka ocena gotowości do decyzji                                │  ║
║  │  • Najważniejsze ryzyka                                              │  ║
║  │                                                                      │  ║
║  │  Kiedy używać:                                                       │  ║
║  │  → Pilna decyzja, mało czasu                                        │  ║
║  │  → Wstępna orientacja przed głębszą analizą                         │  ║
║  │  → Decyzja o niskiej stawce                                          │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [2] STANDARD  (45-90 min)                                          │  ║
║  │                                                                      │  ║
║  │  Co dostaniesz:                                                      │  ║
║  │  • Pełna mapa opcji (4-6 wymiarów)                                  │  ║
║  │  • Konsekwencje dla top 3-5 opcji (VERIFIED vs ASSUMED)             │  ║
║  │  • Challenge: premortem, bias check, stress test założeń            │  ║
║  │  • Strategiczne klastry opcji                                        │  ║
║  │  • Pełny raport z sekwencją decyzji                                 │  ║
║  │                                                                      │  ║
║  │  Kiedy używać:                                                       │  ║
║  │  → Ważna decyzja wymagająca przemyślenia                            │  ║
║  │  → Potrzebujesz pewności przed działaniem                           │  ║
║  │  → Decyzja o średniej/wysokiej stawce                               │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │  [3] DEEP  (2-4 godziny)                                            │  ║
║  │                                                                      │  ║
║  │  Co dostaniesz:                                                      │  ║
║  │  • Wyczerpująca mapa WSZYSTKICH opcji                               │  ║
║  │  • Głęboka analiza konsekwencji dla każdej opcji                    │  ║
║  │  • Wielokrotne iteracje z feedback loops                            │  ║
║  │  • External research gdzie potrzebny                                │  ║
║  │  • Devil's advocate, black swan hunting                             │  ║
║  │  • Pełna analiza zależności i punktów zwrotnych                     │  ║
║  │                                                                      │  ║
║  │  Kiedy używać:                                                       │  ║
║  │  → Krytyczna, nieodwracalna decyzja                                 │  ║
║  │  → Bardzo wysoka stawka (kariera, firma, życie)                     │  ║
║  │  → Masz czas i chcesz maksymalnej pewności                          │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  Wybierz: [1] / [2] / [3]                                                 ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**Po wyborze użytkownika:**
1. Zapisz wybrany poziom: `depth = quick | standard | deep`
2. Przeskanuj input użytkownika pod kątem sygnałów strachu/obaw (patrz: FEAR DETECTION)
3. Rozpocznij wykonanie od Step 0

---

## FEAR DETECTION (automatyczne)

**Nie pytaj użytkownika o fear analysis. Wykryj automatycznie z języka.**

Jeśli w opisie decyzji użytkownik użył słów/fraz:
- "boję się", "martwię się", "obawiam się"
- "co jeśli się nie uda", "a jeśli to nie zadziała"
- "zablokowany", "nie wiem jak zacząć", "niemożliwe"
- "ryzyko", "stracę", "porażka"
- "paraliż", "nie mogę się zdecydować"
- "wszyscy mówią że to złe", "nikt tego nie robi"

**→ Włącz `fear_analysis = on`**

Oznacza to:
- W Step 0: dodaj Fear Inventory (E008), Control Analysis (E011), Blocker Analysis (E012)
- W Step 4: dodaj Fear Resolution, Minimal Tests (E010), Growth Assessment (E014)
- W raporcie: dodaj Section 8 (Fear Resolution)

**Jeśli brak sygnałów strachu → `fear_analysis = off`** (standardowa eksploracja)

---

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP EXPLORE = KNOWLEDGE EXPANSION + UNCERTAINTY MAPPING + EXPLORATION     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Decision problem, strategic question, complex choice              │
│  OUTPUT:  UNDERSTANDING (not just a map)                                    │
│           • What you learned                                                │
│           • What you still don't know                                       │
│           • Options with VERIFIED vs ASSUMED consequences                   │
│           • Decision readiness assessment                                   │
│                                                                              │
│  CORE PRINCIPLE: EXPAND KNOWLEDGE BEFORE MAPPING OPTIONS                    │
│                  You cannot map territory you haven't explored              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DEPTH LEVELS — Co wykonujesz na każdym poziomie

### QUICK (depth = quick)

```
STEPS:           0 → 1 → 2 → 3 → 4 → 5 → 6  (wszystkie, ale skrócone)
MAX ITERATIONS:  1 (brak feedback loops)
RESEARCH:        Top 2-3 items z kolejki
DIMENSIONS:      3 minimum
OPTIONS:         Top 2 opcje analizowane głęboko
CHALLENGE:       Tylko kluczowe założenia, basic bias check
COVERAGE TARGET: C ≥ 12 = COMPREHENSIVE
```

### STANDARD (depth = standard)

```
STEPS:           0 → 1 → 2 → 3 → 4 → 5 → 6  (pełne wykonanie)
MAX ITERATIONS:  3 (feedback loops dozwolone)
RESEARCH:        Wszystkie P1 i P2 items
DIMENSIONS:      4-6 wymiarów
OPTIONS:         Top 3-5 opcji analizowanych
CHALLENGE:       Pełna procedura: premortem, black swan, bias check
COVERAGE TARGET: C ≥ 25 = COMPREHENSIVE
```

### DEEP (depth = deep)

```
STEPS:           0 → 1 → 2 → 3 → 4 → 5 → 6  (pełne + pogłębione)
MAX ITERATIONS:  Unlimited (do rozwiązania lub decyzji użytkownika)
RESEARCH:        Wszystkie items + exploratory research
DIMENSIONS:      Wyczerpujące odkrywanie
OPTIONS:         Wszystkie viable opcje
CHALLENGE:       Wielokrotne rundy, devil's advocate, external validation
COVERAGE TARGET: C ≥ 35 = COMPREHENSIVE
```

---

## FOUNDATIONAL METHODS

Deep Explore is built on these epistemological foundations:

### Epistemological Core (E001-E007) — zawsze używane

| ID | Method | Purpose |
|----|--------|---------|
| E001 | Abductive Reasoning | Generate hypotheses from observations |
| E002 | Counterfactual Thinking | Identify causal factors and leverage points |
| E003 | Minimal Assertions | Compress knowledge to actionable principles |
| E004 | Boundary Analysis | Find limits where things stop working |
| E005 | Causal Models | Map influence relationships |
| E006 | Falsification | Test beliefs by trying to disprove them |
| E007 | Information Questions | Identify highest-value questions |

### Fear-Based Methods (E008-E014) — gdy fear_analysis = on

| ID | Method | Purpose |
|----|--------|---------|
| E008 | Failure Reason Exploration | Transform fear into structured risk map |
| E009 | Reverse Abduction | Discover paths by assuming success |
| E010 | Cognitive MVP | Find smallest action that teaches something |
| E011 | Control vs Influence Analysis | Separate controllable from uncontrollable |
| E012 | Fundamental Block Analysis | Find true "walls" vs false walls |
| E013 | Contrast Exploration | Learn from others' successes and failures |
| E014 | Growth Test | Filter decisions by whether they develop you |

---

## EXECUTION FLOW

```
                    ┌──────────────────────────────────────────┐
                    │          FEEDBACK LOOPS                  │
                    │     (tylko dla standard i deep)          │
                    ▼                                          │
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│ STEP 0  │───►│ STEP 1  │───►│ STEP 2  │───►│ STEP 3  │─────┤
│ AUDIT   │    │ RESEARCH│    │   MAP   │    │ DEEPEN  │     │
└─────────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
                    │              │              │           │
                    └──────────────┴──────────────┘           │
                                         │                   │
                                         ▼                   │
                    ┌─────────┐    ┌─────────┐    ┌─────────┐
                    │ STEP 4  │───►│ STEP 5  │───►│ STEP 6  │
                    │CHALLENGE│    │SYNTHESIZE    │ OUTPUT  │
                    └─────────┘    └─────────┘    └─────────┘
```

---

## EXECUTION PATH

**Po wyborze poziomu przez użytkownika, wykonaj:**

```
📂 Step 0: KNOWLEDGE AUDIT
   Load: steps/step-00-knowledge-audit.md

   □ Frame the decision (one sentence)
   □ Assess stakes: LOW/MEDIUM/HIGH
   □ Inventory: Known Facts, Assumptions, Known Unknowns
   □ 📂 E001 → Surface Unknown Unknowns
   □ Prioritize research needs

   IF fear_analysis = on:
   □ 📂 E008 → Structure fears into risk map
   □ 📂 E011 → Separate actionable concerns
   □ 📂 E012 → Find true walls vs false walls
   □ 📂 E009 → Reverse from success (if "impossible")
   □ 📂 E013 → Gain context from others
   → Fears become structured research queue

   Output: Knowledge Map + Research Queue (+ Fear Map if fear_analysis=on)

   ↓ PROCEED if research queue is defined
   ↓ STAY if framing is unclear

📂 Step 1: RESEARCH
   Load: steps/step-01-research.md

   □ Execute research queue by priority
   □ Use methods from: data/research-methods.md
   □ Record findings with sources
   □ Update Knowledge Map
   □ Add new unknowns to queue if discovered

   DEPTH ADJUSTMENT:
   • quick: Research top 2-3 items only
   • standard: Research all P1 and P2 items
   • deep: Research all items + exploratory research

   Output: Research Summary + Updated Knowledge Map

   ↓ PROCEED if critical unknowns addressed
   ↓ STAY if more research needed (check iteration limit)
   ↑ RETURN TO STEP 0 if framing changed

📂 Step 2: MAP (Divergent)
   Load: steps/step-02-map.md

   □ 📂 M001 → Discover dimensions (axes of choice)
   □ 📂 M002 → Enumerate options per dimension
   □ 📂 M003 → Map hard and soft constraints
   □ Build Morphological Box (see step file for format)

   DEPTH ADJUSTMENT:
   • quick: 3 dimensions minimum
   • standard: 4-6 dimensions
   • deep: Exhaustive dimension discovery

   Output: Option Map (draft)

   ↓ PROCEED if dimensions are complete
   ↑ RETURN TO STEP 1 if knowledge gaps found

📂 Step 3: DEEPEN
   Load: steps/step-03-deepen.md

   □ 📂 E002 → Apply Counterfactual Thinking to key options
   □ 📂 E004 → Apply Boundary Analysis to key options
   □ 📂 E005 → Apply Causal Models to understand relationships
   □ 📂 M011 → Map consequences (mark VERIFIED vs ASSUMED)
   □ 📂 M012 → Assess reversibility of each option
   □ 📂 M013 → Map decision dependencies

   DEPTH ADJUSTMENT:
   • quick: Top 2 options only
   • standard: Top 3-5 options
   • deep: All viable options

   Output: Consequence Map with verification status

   ↓ PROCEED if critical consequences verified
   ↑ RETURN TO STEP 1 if consequences need research

📂 Step 4: CHALLENGE (Adversarial)
   Load: steps/step-04-challenge.md

   □ 📂 E006 → Apply Falsification to key beliefs
   □ 📂 M021 → Imagine failure, trace causes
   □ 📂 M022 → Find low-probability high-impact events
   □ 📂 M023 → Break assumptions one by one
   □ Check for cognitive biases
   □ Update map based on findings

   IF fear_analysis = on:
   □ 📂 E010 → Find smallest test to learn
   □ 📂 E014 → Assess if path develops user
   □ 📂 E008 → Revisit risks — which are now addressed?
   □ Update Fear Map with verified/falsified concerns

   DEPTH ADJUSTMENT:
   • quick: Key beliefs only, basic bias check
   • standard: Full challenge procedure
   • deep: Multiple rounds, devil's advocate, external validation

   Output: Challenged map with strengthened/weakened items
           (+ Updated Fear Map with resolution status if fear_analysis=on)

   ↓ PROCEED always (challenge is mandatory)

📂 Step 5: SYNTHESIZE
   Load: steps/step-05-synthesize.md

   □ 📂 E003 → Compress insights to minimal assertions
   □ Cluster natural strategic options
   □ Identify decision sequence (what first, what can wait)
   □ Assess decision readiness per item
   □ 📂 E007 → Identify remaining gaps

   Output: Synthesis ready for report

   ↓ PROCEED to final output

📂 Step 6: OUTPUT
   Load: steps/step-06-output.md
   Load template: data/exploration-report-template.md

   □ Section 1: What We Learned
   □ Section 2: What We Still Don't Know
   □ Section 3: Option Map
   □ Section 4: Strategic Clusters
   □ Section 5: Consequence Map
   □ Section 6: Decision Readiness
   □ Section 7: Suggested Next Steps
   □ Section 8: Fear Resolution (only if fear_analysis=on)

   Output: EXPLORATION REPORT
```

---

## SCORING SYSTEM

### Exploration Coverage Score (C)

| Exploration Quality | Points |
|---------------------|--------|
| New dimension discovered | +2 |
| New option in dimension | +1 |
| Consequence VERIFIED | +1 |
| Consequence ASSUMED | +0.3 |
| Unknown Unknown surfaced | +1.5 |
| Assumption falsified | +1 |
| Boundary identified | +0.5 |
| Causal relationship mapped | +0.5 |

**When fear_analysis = on, additional:**

| Fear Resolution Quality | Points |
|------------------------|--------|
| Fear classified | +0.5 |
| False wall identified | +1 |
| True wall confirmed | +1 |
| Controllable concern found | +0.5 |
| Success path discovered | +1.5 |
| Comparable analyzed | +0.5 |

### Coverage Thresholds (by depth)

| Score | quick | standard | deep |
|-------|-------|----------|------|
| COMPREHENSIVE | C ≥ 12 | C ≥ 25 | C ≥ 35 |
| ADEQUATE | C ≥ 8 | C ≥ 15 | C ≥ 25 |
| PARTIAL | C ≥ 4 | C ≥ 8 | C ≥ 15 |
| INSUFFICIENT | C < 4 | C < 8 | C < 15 |

**Note:** When fear_analysis=on, thresholds increase by +5.

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EXPLORATION COMMANDMENTS                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. ALWAYS START WITH INVOCATION                                            │
│     Display the depth selection dialog before doing anything                │
│     Wait for user choice before proceeding                                  │
│                                                                              │
│  2. KNOWLEDGE BEFORE MAPPING                                                │
│     Never map options in a space you don't understand                       │
│     Step 0 + Step 1 are NOT optional                                        │
│                                                                              │
│  3. VERIFY BEFORE CLAIMING                                                  │
│     Mark every consequence as VERIFIED or ASSUMED                           │
│     Critical assumptions MUST be verified or flagged                        │
│                                                                              │
│  4. RESPECT DEPTH LIMITS                                                    │
│     quick = 1 iteration, no loops                                           │
│     standard = max 3 iterations                                             │
│     deep = until resolved                                                   │
│                                                                              │
│  5. AUTO-DETECT FEAR                                                        │
│     Don't ask about fear analysis - detect from language                    │
│     If detected, enable silently and include in report                      │
│                                                                              │
│  6. USER DECIDES, AI EXPLORES                                               │
│     Output is UNDERSTANDING, not recommendation                             │
│     Present options fairly, let user weigh trade-offs                       │
│                                                                              │
│  7. LOAD FILES WHEN NEEDED                                                  │
│     Announce: "📂 Loading [path]"                                           │
│     Follow the procedure in the loaded file                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FILE LOADING PROTOCOL

When you need specific data, announce and load:

| Situation | Load | Announcement |
|-----------|------|--------------|
| Start Step 0 | `steps/step-00-knowledge-audit.md` | "📂 Loading Step 0: Knowledge Audit" |
| Start Step 1 | `steps/step-01-research.md` | "📂 Loading Step 1: Research" |
| Start Step 2 | `steps/step-02-map.md` | "📂 Loading Step 2: Map" |
| Start Step 3 | `steps/step-03-deepen.md` | "📂 Loading Step 3: Deepen" |
| Start Step 4 | `steps/step-04-challenge.md` | "📂 Loading Step 4: Challenge" |
| Start Step 5 | `steps/step-05-synthesize.md` | "📂 Loading Step 5: Synthesize" |
| Start Step 6 | `steps/step-06-output.md` | "📂 Loading Step 6: Output" |
| Execute method | `data/method-procedures/[ID]_[Name].md` | "📂 Loading method: [Name]" |
| Generate report | `data/exploration-report-template.md` | "📂 Loading report template" |
| Scoring | `data/coverage-scoring.yaml` | "📂 Loading scoring rules" |

---

## KEY PATHS

```
deep-explore-v2/
├── workflow.md                           ← This file (start here)
├── steps/step-{00-06}-*.md               ← Step procedures
├── data/method-procedures/{ID}_*.md      ← Method procedures
├── data/coverage-scoring.yaml            ← Scoring rules
├── data/exploration-report-template.md   ← Output template
└── data/research-methods.md              ← Research guidance
```

Method file naming: `{ID}_{Name}.md` where ID is E001-E014 or M001-M023.
