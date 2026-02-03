# Deep-Process v3.6 — Semantic Reality Engine (SRE-Convergent)

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP-PROCESS = SEMANTIC OS + TRANSACTIONAL DETERMINISM + HUMAN ANCHOR     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  System nie jest chatbotem. Jest Semantycznym Systemem Operacyjnym,        │
│  który wymusza determinizm na probabilistycznym silniku (LLM)              │
│  poprzez 5 nienaruszalnych Filarów.                                        │
│                                                                             │
│  INPUT:  Projekt, wymagania, procesy zewnętrzne                            │
│  OUTPUT: Graf artefaktów ze spójnością semantyczną                         │
│                                                                             │
│  EXECUTION: LLM CLI (Claude, Gemini, Native Shell)                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## THREE-LAYER ARCHITECTURE

System operuje w trzech warstwach dziedziczenia:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: META-CLASS (Deep-Process Framework)                              │
│  Location: src/core/deep-process/                                          │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • workflow.md          — JAK wykonywać procesy                     │   │
│  │  • data/enforcer.md     — BIOS, Method Translator                   │   │
│  │  • data/method-procedures/ — 17 metod weryfikacji                   │   │
│  │  • agents/              — PM, Validator, Implementation Agent       │   │
│  │  • steps/               — Deep-Pulse loop (SENSE→PLAN→ACT→...)     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓ inherits                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: PROCESS CLASSES (SRE-Convergent Process Definitions)             │
│  Location: src/core/deep-process/processes/                                │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • _manifest.yaml       — Registry of available processes           │   │
│  │  • onboarding/          — Process "Onboarding" definition           │   │
│  │  • code-review/         — Process "Code Review" definition          │   │
│  │  • sprint-planning/     — Process "Sprint Planning" definition      │   │
│  │  • ...                  — More transformed processes                │   │
│  │                                                                     │   │
│  │  Each process:                                                      │   │
│  │    ├── process.yaml     — Steps, gates, methods, artifacts          │   │
│  │    └── templates/       — Artifact templates for this process       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓ instantiates                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: PROCESS INSTANCES (Runtime Executions)                           │
│  Location: artifacts/processes/{instance-id}/                              │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Tracked in: .deep-process/registry.json                            │   │
│  │                                                                     │   │
│  │  artifacts/processes/                                               │   │
│  │    ├── onboarding-client-acme-001/    — Instance 1 of Onboarding   │   │
│  │    │     ├── instance-state.json                                   │   │
│  │    │     └── *.md (generated artifacts)                            │   │
│  │    ├── onboarding-client-beta-002/    — Instance 2 of Onboarding   │   │
│  │    └── code-review-feature-auth-001/  — Instance of Code Review    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

| Layer | Contains | Responsibility |
|-------|----------|----------------|
| **Meta-Class** | Framework | HOW to execute (methods, validation, orchestration) |
| **Process Class** | Definitions | WHAT to execute (steps, artifacts, gates) |
| **Instance** | Artifacts | EXECUTION results (generated files, decisions) |

### Instance Tracking

All running/completed instances are tracked in `.deep-process/registry.json`:

```json
{
  "active_instance": "onboarding-client-acme-001",
  "instances": [
    {
      "instance_id": "onboarding-client-acme-001",
      "process_type": "PROC-ONBOARDING",
      "process_path": "processes/onboarding/",
      "artifacts_path": "artifacts/processes/onboarding-client-acme-001/",
      "status": "RUNNING",
      "progress": { "current_step": "step-03", "percentage": 40 }
    }
  ]
}
```

This enables:
- **Resume:** Return to paused process instance
- **Switch:** Change between active instances
- **Audit:** Review all instances of a process type

---

## THE 5 PILLARS OF ARCHITECTURE

### Pillar 1: Transactional Processes (Saga Pattern)
- Każda operacja zapisu jest transakcją
- Brak `[UPDATE_STATE]` w odpowiedzi = `ROLLBACK`
- Stan "pomiędzy" jest niedopuszczalny

### Pillar 2: Structured Rails (Schema Enforcement)
- LLM nie "pisze" dokumentów; LLM "wypełnia" schematy
- Walidacja następuje *przed* zapisem (Pre-commit via Validator Sub-Agent)

### Pillar 3: Topology Awareness (Change Coupling)
- System mapuje zależności (`depends_on`)
- Zmiana w węźle A automatycznie flaguje węzły zależne jako `STALE`

### Pillar 4: Semantic Lineage (Traceability)
- Każdy artefakt posiada wskaźnik `source_id`
- Pełna droga od Tasku przez Epik aż do Wizji

### Pillar 5: Convergent Determinism (Method #108)
- Determinizm semantyczny (zgodność faktów) zamiast identyczności znaków
- `semantic_hash` w każdym artefakcie + weryfikacja przez Operatora

---

## METHOD ARCHITECTURE

### Anti-Bias Methods (Wymuszenie Obiektywności)

| # | Method | Purpose | File |
|---|--------|---------|------|
| 56 | Liar's Trap | Wymuś samoobserwację potencjalnych dróg oszustwa | `056_Liars_Trap.md` |
| 59 | CUI BONO Test | Kto korzysta z decyzji? Agent vs User | `059_CUI_BONO_Test.md` |
| 60 | Approval Gradient Test | Wykryj people-pleasing vs truth-telling | `060_Approval_Gradient_Test.md` |

### Coherence Methods (Spójność Wyniku)

| # | Method | Purpose | File |
|---|--------|---------|------|
| 93 | DNA Inheritance Check | Czy element dziedziczy "geny" systemu? | `093_DNA_Inheritance_Check.md` |
| 95 | Structural Isomorphism | Porównanie struktury nowego vs istniejącego | `095_Structural_Isomorphism.md` |
| 99 | Multi-Artifact Coherence | Spójność między powiązanymi artefaktami | `099_Multi_Artifact_Coherence.md` |
| 100 | Vocabulary Consistency | Spójność terminologii w całym systemie | `100_Vocabulary_Consistency.md` |

### Implementation Methods (Dla Implementation Agenta)

| # | Method | Purpose | File |
|---|--------|---------|------|
| 71 | First Principles Analysis | Fundamentalna analiza od podstaw | `071_First_Principles_Analysis.md` |
| 72 | 5 Whys Deep Dive | Dotarcie do root cause | `072_5_Whys_Deep_Dive.md` |
| 79 | Operational Definition | Operacjonalizacja abstrakcyjnych pojęć | `079_Operational_Definition.md` |
| 80 | Inversion | Jak zagwarantować porażkę? Unikaj tego | `080_Inversion.md` |
| 87 | Falsifiability Check | Czy twierdzenia są mierzalne i testowalne? | `087_Falsifiability_Check.md` |
| 90 | Dependency Topology Mapping | Mapowanie ukrytych zależności | `090_Dependency_Topology_Mapping.md` |
| 114 | Reversibility Test | Czy można odtworzyć input z output? | `114_Reversibility_Test.md` |
| 152 | Socratic Decomposition | Dekompozycja na atomowe pod-pytania | `152_Socratic_Decomposition_Pre_Analysis.md` |
| 154 | Definitional Contradiction | Wykrywanie sprzeczności definicyjnych | `154_Definitional_Contradiction_Detector.md` |
| 159 | Transitive Dependency Closure | Pełny graf zależności z cyklami | `159_Transitive_Dependency_Closure.md` |

---

## THE ORCHESTRATION LOOP (Deep-Pulse)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DEEP-PULSE ALGORITHM                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: SENSE ─────────────────────────────────────────────────────────► │
│    └── Load state.json → Scan for STALE/BLOCKED → Display Menu             │
│                                                                             │
│  PHASE 2: PLAN ──────────────────────────────────────────────────────────► │
│    └── Analyze task type → Inject methods → Create skeleton with YAML      │
│                                                                             │
│  PHASE 3: ACT ───────────────────────────────────────────────────────────► │
│    └── LLM-Executor + Method Translator → Generate content + semantic_hash │
│                                                                             │
│  PHASE 4: VALIDATE ──────────────────────────────────────────────────────► │
│    └── LLM-Validator → Check: Content vs Hash vs Parents → COMMITTED/FAILED│
│                                                                             │
│  PHASE 5: SYNC ──────────────────────────────────────────────────────────► │
│    └── Operator approval → Write files → Update state.json                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## QUICK EXECUTION PATH

**Standard orchestration sequence:**

```
📂 Loading data/state-schema.yaml

1. BOOTSTRAP (First run only)
   □ Initialize .deep-process/ structure
   □ Create empty state.json
   □ Create enforcer.md with Method Translator
   □ Display Main Menu

2. SENSE PHASE
   📂 Loading .deep-process/state.json
   □ Scan graph for STALE and BLOCKED nodes
   □ Build dependency topology
   □ Present status menu to Operator

3. PLAN PHASE
   □ Operator selects action
   □ PM Agent analyzes task type:
     → Technical Task: Inject [#87, #114, #154]
     → Creative Task: Inject [#71, #79, #152]
     → Migration Task: Inject [#90, #159, #100]
   □ Create skeleton file with YAML header

4. ACT PHASE
   📂 Loading data/enforcer.md (BIOS)
   □ LLM-Executor receives skeleton
   □ Method Translator enforces work style
   □ Generate content adhering to constraints
   □ Compute semantic_hash

5. VALIDATE PHASE
   📂 Loading agents/validator-agent.yaml
   □ Anti-Bias Check: Execute #56, #59, #60
   □ Coherence Check: Execute #93, #95, #99, #100
   □ Hash Verification: Content vs Hash vs Parents
   □ Verdict: COMMITTED or FAILED

6. SYNC PHASE
   □ Display result to Operator
   □ If valid → Operator approves
   □ Write file + Update state.json
   □ Flag dependent nodes as STALE

```

---

## FILESYSTEM ARCHITECTURE

### Framework Definition (src/core/deep-process/)

```
src/core/deep-process/              # LAYER 1: META-CLASS (Framework)
├── workflow.md                     # Main documentation
├── data/
│   ├── enforcer.md                 # BIOS: Method Translator & Invariants
│   ├── state-schema.yaml           # Schema for state.json
│   ├── registry-schema.yaml        # Schema for registry.json
│   ├── contract-schema.yaml        # Universal Contract schema
│   ├── decision-point-schema.yaml  # Decision Point schema
│   ├── method-translator.yaml      # Method definitions
│   ├── method-procedures/          # 17 method procedures
│   └── templates/                  # Universal templates
├── steps/                          # Deep-Pulse phases
│   ├── step-00-bootstrap.md
│   ├── step-01-sense.md
│   ├── step-02-plan.md
│   ├── step-03-act.md
│   ├── step-04-validate.md
│   └── step-05-sync.md
├── agents/                         # Agent manifests
│   ├── pm-agent.yaml
│   ├── validator-agent.yaml
│   └── implementation-agent.yaml
└── processes/                      # LAYER 2: PROCESS DEFINITIONS
    ├── _manifest.yaml              # Registry of SRE-Convergent processes
    ├── _process-template/          # Template for new processes
    │   ├── process.yaml
    │   └── templates/
    └── [process-name]/             # Each transformed process
        ├── process.yaml            # Process definition
        └── templates/              # Process-specific templates
```

### Runtime Instance (project-root)

```
/project-root/                      # USER PROJECT
├── .deep-process/                  # RUNTIME KERNEL
│   ├── state.json                  # Graph DB (all artifacts)
│   ├── registry.json               # Instance tracking
│   ├── enforcer.md                 # Copied from framework
│   └── backups/                    # Saga rollback storage
│
├── artifacts/                      # USER SPACE (Output)
│   ├── vision.md                   # Project-level artifacts
│   ├── architecture.md
│   └── processes/                  # LAYER 3: PROCESS INSTANCES
│       ├── onboarding-client-acme-001/
│       │   ├── instance-state.json # Instance-specific state
│       │   └── *.md                # Generated artifacts
│       ├── onboarding-client-beta-002/
│       └── code-review-feature-auth-001/
│
└── .claude/commands/               # CLI shims
    ├── deep-process.json
    └── audit.json
```

### Relationship Between Layers

```
┌───────────────────────────────────────────────────────────────────────┐
│ FRAMEWORK (src/core/deep-process/)                                    │
│   defines HOW                                                         │
│   └── processes/ contains WHAT (process definitions)                  │
│         └── Each definition can have multiple INSTANCES in runtime    │
│               └── artifacts/processes/{instance-id}/                  │
└───────────────────────────────────────────────────────────────────────┘

registry.json tracks:
  - Which instances exist
  - Where their artifacts are stored
  - Current status and progress
  - How to resume each instance
```

---

## UNIVERSAL CONTRACT (YAML Header)

Every artifact MUST start with this header:

```yaml
---
dp_id: "EPIC-USER-LOGIN"       # Unique ID
dp_type: "artifact"            # [artifact | process | decision-point]
dp_status: "STALE"             # [NOW | STALE | COMMITTED | FAILED | AWAITING_USER_INPUT]
version: "3.6"

# === TOPOLOGY & LINEAGE ===
context:
  depends_on:
    - path: "artifacts/vision.md"
      type: "semantic_source"  # Changes invalidate content
    - path: "artifacts/security_policy.md"
      type: "hard_constraint"  # Changes invalidate logic

# === CONVERGENT DETERMINISM ===
semantic_hash:
  - "Auth: OAuth2 via Google"
  - "MFA: Required for Admin"
  - "Session: 24h JWT"

# === EXECUTION LOGIC ===
execution:
  active_methods: [154, 114, 87]
  logic_gates:
    if_mobile: "Use artifact/templates/mobile_screen.md"
    if_web: "Use artifact/templates/web_page.md"

# === TRANSACTION ===
transaction:
  saga_id: "tx-9912"
  previous_hash: "a1b2c3d4"
---
```

---

## DECISION POINT CONTRACT

When system encounters contradiction, it generates a decision-point:

```yaml
---
dp_id: "DP-005"
dp_type: "decision-point"
dp_status: "AWAITING_USER_INPUT"

question:
  type: "EXCLUSIVE_CHOICE"
  trigger: "Conflict detected via Method #154"
  prompt: "Wizja zakłada 'Szybki MVP', a Architektura 'Mikroserwisy'. To sprzeczne."
  options:
    - id: "A"
      label: "Zmień na Monolit (Zgodność z MVP)"
      impact: "Update artifacts/architecture.md"
    - id: "B"
      label: "Wydłuż czas (Zgodność z Mikroserwisami)"
      impact: "Update artifacts/timeline.md"
---
```

---

## CLI COMMANDS

### `deep-process` (Project Manager)
- **Purpose:** Main dashboard and Process Launcher
- **Behavior:** Load registry.json, display active processes, offer actions

```
> SRE-Convergent Manager
> Aktywne Procesy:
  [1] PROC-MIGRATION (legacy-import-v1) - Status: BLOCKED
  [2] PROC-DEV (feature-login) - Status: RUNNING

Dostępne akcje:
[N] Nowy Proces (Instancjonowanie)
[S] Przełącz kontekst na instancję [ID]
```

### `audit` (Validator)
- **Purpose:** Force consistency verification
- **Behavior:** Traverse entire graph, check all hashes

### `fix` (Auto-Heal)
- **Purpose:** Quick repair of minor errors
- **Behavior:** Auto-regenerate STALE files from parents

---

## BOOTSTRAP PROTOCOL

Initialize system with this prompt:

```
Zatrzymaj tryb konwersacyjny. Inicjalizuję Deep-Process v3.6 - Semantic Reality Engine.

TWOJE DYREKTYWY (BIOS):
1. Jesteś Systemem Operacyjnym plików Markdown. Twoja pamięć to `.deep-process/state.json`.
2. Każdy plik, który wygenerujesz, MUSI mieć nagłówek YAML zgodny ze Specyfikacją v3.6.
3. Twoim priorytetem jest DETERMINIZM SEMANTYCZNY. Używaj `semantic_hash` do weryfikacji.
4. Jeśli wykryjesz sprzeczność (Metoda #154), nie zgaduj. Stwórz `decision-point`.

ZADANIE STARTOWE:
1. Zmapuj obecną strukturę plików.
2. Utwórz folder `.deep-process/` i pusty `state.json`.
3. Utwórz `enforcer.md` z definicją metod.
4. Zgłoś gotowość wyświetlając Menu Główne.
```

---

## MIGRATION PROTOCOL (SRE Transformer)

### Transformation Pipeline

```
KROK 1: Dekompozycja Zasad (Methods #71, #72)
  └── Oddziel "rytuały" od "funkcji"
  └── Wypisz łańcuch przyczynowo-skutkowy

KROK 2: Izomorfizm Strukturalny (Method #95)
  └── Mapowanie:
      Dokument/E-mail → dp_type: artifact
      Decyzja/Spotkanie → dp_type: decision-point
      Procedura/Instrukcja → dp_type: process
      Rola/Osoba → dp_type: agent

KROK 3: Wykrywanie Punktów Styku (Method #90)
  └── Każde "zatwierdzenie/opinia/wybór" → Decision Point

KROK 4: Generowanie Kontraktów (Method #79)
  └── Dla każdego kroku: plik .md z YAML header

KROK 5: Weryfikacja Wierności (Methods #114, #100)
  └── Test Entropii: czy informacja zginęła?
  └── Test Odwracalności: czy można odtworzyć oryginał?
```

---

## DIRECTORY STRUCTURE

```
src/core/deep-process/
├── workflow.md                     ← YOU ARE HERE
│
├── data/                           # FRAMEWORK DATA
│   ├── state-schema.yaml           # Schema for state.json
│   ├── registry-schema.yaml        # Schema for registry.json (instance tracking)
│   ├── contract-schema.yaml        # Universal Contract schema
│   ├── decision-point-schema.yaml  # Decision Point schema
│   ├── enforcer.md                 # BIOS - Method Translator
│   ├── method-translator.yaml      # Method definitions
│   ├── method-procedures/          # Individual method files (17 methods)
│   │   ├── 056_Liars_Trap.md           # Anti-bias
│   │   ├── 059_CUI_BONO_Test.md        # Anti-bias
│   │   ├── 060_Approval_Gradient_Test.md # Anti-bias
│   │   ├── 093_DNA_Inheritance_Check.md  # Coherence
│   │   ├── 095_Structural_Isomorphism.md # Coherence
│   │   ├── 099_Multi_Artifact_Coherence.md # Coherence
│   │   ├── 100_Vocabulary_Consistency.md # Coherence
│   │   ├── 071_First_Principles_Analysis.md # Implementation
│   │   ├── 072_5_Whys_Deep_Dive.md     # Implementation
│   │   ├── 079_Operational_Definition.md # Implementation
│   │   ├── 080_Inversion.md            # Implementation
│   │   ├── 087_Falsifiability_Check.md # Implementation
│   │   ├── 090_Dependency_Topology_Mapping.md # Implementation
│   │   ├── 114_Reversibility_Test.md   # Implementation
│   │   ├── 152_Socratic_Decomposition_Pre_Analysis.md # Implementation
│   │   ├── 154_Definitional_Contradiction_Detector.md # Implementation
│   │   └── 159_Transitive_Dependency_Closure.md # Implementation
│   └── templates/
│       ├── artifact-template.md
│       └── decision-point-template.md
│
├── steps/                          # DEEP-PULSE PHASES
│   ├── step-00-bootstrap.md
│   ├── step-01-sense.md
│   ├── step-02-plan.md
│   ├── step-03-act.md
│   ├── step-04-validate.md
│   └── step-05-sync.md
│
├── agents/                         # AGENT MANIFESTS
│   ├── pm-agent.yaml               # Project Manager / Orchestrator
│   ├── validator-agent.yaml        # Validator (anti-bias + coherence)
│   └── implementation-agent.yaml   # Implementation (10 methods)
│
└── processes/                      # SRE-CONVERGENT PROCESS DEFINITIONS
    ├── _manifest.yaml              # Registry of available processes
    ├── _process-template/          # Template for creating new processes
    │   ├── process.yaml            # Process definition template
    │   └── templates/
    │       └── artifact-template.md
    └── [process-name]/             # Each transformed process
        ├── process.yaml            # Process steps, gates, methods
        └── templates/              # Process-specific artifact templates
```

### Runtime Files (created in user project)

```
project-root/
├── .deep-process/
│   ├── state.json                  # Graph DB (artifacts)
│   ├── registry.json               # Instance tracking
│   └── backups/                    # Rollback storage
│
└── artifacts/
    └── processes/
        └── {instance-id}/          # Each process instance
            ├── instance-state.json
            └── *.md                # Generated artifacts
```

---

## CRITICAL RULES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SYSTEM COMMANDMENTS                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. READ-BEFORE-WRITE                                                       │
│     Never generate content without first reading state.json                 │
│                                                                             │
│  2. ATOMIC COMMIT                                                           │
│     Response without [UPDATE_STATE] block = system failure (ROLLBACK)       │
│                                                                             │
│  3. NO GUESSING                                                             │
│     If contradiction detected → create decision-point, don't resolve        │
│                                                                             │
│  4. SEMANTIC HASH = GROUND TRUTH                                            │
│     Content must match semantic_hash; hash survives text rewrites           │
│                                                                             │
│  5. TOPOLOGY IS LAW                                                         │
│     Changes propagate through dependency graph automatically                │
│                                                                             │
│  6. HUMAN ANCHOR                                                            │
│     Operator (Human) is final arbiter; system proposes, human disposes      │
│                                                                             │
│  7. ANTI-BIAS IS MANDATORY                                                  │
│     Methods #56, #59, #60 run on EVERY validation phase                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## VERSION

- **Deep-Process:** V3.6
- **Codename:** SRE-Convergent
- **Architecture:** File-Based, LLM-Executed, Human-Anchored Graph Database
