chciałbym żeby moje rozwiązanie , program (deep verify) do wykonywania weryfikacji kodu i pomagania w pisaniu kodu było dostępne jako wtyczka visual studio code, ale także jako npm do instalacji jako CLI, żeby w VSC inne aplikacje mogły to wywoływać (jakies api dla VSC), ale chciałbym żeby moc to integrować z LiteLLM a take żeby było dostępne i żeby z azure devops w pipeline można było wywołać mój kod  (deep verify) żeby uruchomiona była weryfikacja , ale wiąże się to z konfiguracją do LiteLLM który będzie wykonywał zapytanie do AI, 

pytanie tylko czy lepiej żeby LiteLLM miał tą możliwośc realizacji całośc, 
czyli Azure DevOps wysyła kod jaki ma weryfikować LiteLLM, i być moze litelmm posiada te moje algorytmy weryfikacyjne i generuje raport w oparciu o odpowiedź LLM , 

załączyłem obecnie jak wygląda mój algorytm, jest to prompt który wykonywany jest przez wskazanie w prompcie do LLM żeby przeczytał plik workflow.md i wykonał instrukcje na jakimś artefakcie, tekście itd, 

tak samo by działało w visual studio code, tylko tam zainstalowany na przykład gemini cli, albo claude cli by był używany przez moją wtyczkę żeby przesyłać do danego AI, 

w LiteLMM gdyby możliwe było realizowanie tego żeby na przyklad generować weryfikację na żądanie ale żeby było to wbudowane w LiteLMM, do tego chciałbym żeby możliwe było generowanie raportów comliance (żeby spełnić oczekiwania europa ai act lub inne na przykład dla branż jak zgodność z innymi wymogami) ale dla klientów enterprise, 

a do tego chciałbym żeby dla firm przedstawiać ofertę premium / enterprise ready, 
ale chciałbym żebyśmy zrobili brainstorming , bo mam metodę weryfikacyjną którą można rozwinąć jako wspomagajacą lepsze znajdywanie rozwiazań, do generowania raportów zgodności kodu z wymogami i regulacjami


Deep Verify - Brainstorming Architektury i Strategii Produktowej
Świetny projekt! Masz solidną metodologię weryfikacyjną. Przemyślmy to systematycznie.
🎯 Kluczowa decyzja architektoniczna
Nie wbudowuj logiki w LiteLLM - to byłby błąd. Oto dlaczego:
❌ Opcja A: Logika w LiteLLM
   - LiteLLM to proxy, nie silnik biznesowy
   - Trudne w utrzymaniu (fork LiteLLM?)
   - Vendor lock-in do jednego proxy

✅ Opcja B: Deep Verify jako osobny silnik
   - LiteLLM tylko jako transport do LLM
   - Można wymienić na OpenRouter, bezpośrednie API
   - Logika weryfikacyjna jest Twoją własnością intelektualną
🏗️ Proponowana architektura
┌─────────────────────────────────────────────────────────────────┐
│                        KLIENCI                                  │
├──────────┬──────────┬──────────┬──────────┬────────────────────┤
│  VSCode  │   CLI    │  Azure   │   API    │  GitHub Actions    │
│Extension │  (npm)   │ DevOps   │  REST    │     / GitLab CI    │
└────┬─────┴────┬─────┴────┬─────┴────┬─────┴─────────┬──────────┘
     │          │          │          │               │
     └──────────┴──────────┴──────────┴───────────────┘
                           │
              ┌────────────▼────────────┐
              │   DEEP VERIFY CORE      │
              │   ──────────────────    │
              │ • Workflow Engine       │
              │ • Pattern Library       │
              │ • Scoring System        │
              │ • Report Generator      │
              │ • Compliance Modules    │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   LLM ADAPTER LAYER     │
              │   ──────────────────    │
              │ • LiteLLM               │
              │ • OpenRouter            │
              │ • Direct APIs           │
              │ • Local (Ollama)        │
              └────────────┬────────────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
┌────▼────┐          ┌─────▼─────┐         ┌────▼────┐
│ Claude  │          │   GPT-4   │         │ Gemini  │
└─────────┘          └───────────┘         └─────────┘
📦 Struktura pakietów
deep-verify/
├── packages/
│   ├── @deep-verify/core          # Silnik główny (TypeScript)
│   │   ├── workflow/              # Engine wykonujący kroki
│   │   ├── patterns/              # Pattern Library
│   │   ├── scoring/               # System scoringu
│   │   ├── methods/               # 165 metod weryfikacyjnych
│   │   └── reports/               # Generatory raportów
│   │
│   ├── @deep-verify/cli           # CLI (npm install -g)
│   ├── @deep-verify/vscode        # Extension VSCode
│   ├── @deep-verify/azure-devops  # Azure DevOps Task
│   ├── @deep-verify/github-action # GitHub Action
│   │
│   ├── @deep-verify/compliance    # 💰 ENTERPRISE
│   │   ├── eu-ai-act/
│   │   ├── soc2/
│   │   ├── hipaa/
│   │   └── custom/
│   │
│   └── @deep-verify/server        # 💰 Self-hosted API server
│
└── llm-adapters/
    ├── litellm/
    ├── openrouter/
    └── direct/
💡 Model biznesowy - 3 tiary
TierNazwaCenaFunkcje🆓CommunityFree/OSSCLI, podstawowe patterns, własny LLM API key💼Pro$29/miesVSCode Extension, więcej patterns, priorytetowe wsparcie🏢EnterpriseCustomSelf-hosted, compliance reports, SLA, dedicated support, custom patterns
🔄 Jak to działa w praktyce
Scenariusz 1: Developer w VSCode
typescript// Użytkownik klika "Verify with Deep Verify" na pliku

// 1. Extension zbiera kontekst
const artifact = vscode.window.activeTextEditor.document.getText();

// 2. Wywołuje Core
const result = await deepVerify.run({
  artifact,
  stakes: 'MEDIUM',
  llmProvider: 'litellm',  // lub 'claude', 'openai'
  llmConfig: {
    baseUrl: 'http://localhost:4000',  // LiteLLM proxy
    model: 'claude-sonnet-4-20250514'
  }
});

// 3. Wyświetla raport w panelu
vscode.window.showWebviewPanel(result.report);
Scenariusz 2: Azure DevOps Pipeline
yaml# azure-pipelines.yml
trigger:
  - main

stages:
  - stage: Verify
    jobs:
      - job: DeepVerify
        steps:
          - task: DeepVerify@1
            inputs:
              artifactPath: '$(Build.SourcesDirectory)/src/**/*.ts'
              stakes: 'HIGH'
              llmEndpoint: '$(LITELLM_ENDPOINT)'
              llmApiKey: '$(LITELLM_API_KEY)'
              llmModel: 'azure/gpt-4'
              complianceModules: 
                - 'eu-ai-act'
                - 'soc2'
              failOnReject: true
              reportFormat: 'junit,sarif,html'
Scenariusz 3: Enterprise Compliance Report
typescript// Generowanie raportu zgodności EU AI Act

const complianceReport = await deepVerify.compliance.generate({
  artifacts: ['./src/**/*.py'],
  framework: 'eu-ai-act',
  riskCategory: 'high-risk',  // Art. 6 EU AI Act
  
  checks: [
    'transparency-requirements',      // Art. 13
    'human-oversight',                // Art. 14
    'accuracy-robustness-security',   // Art. 15
    'data-governance',                // Art. 10
    'risk-management-system',         // Art. 9
  ],
  
  outputFormat: 'pdf',
  includeEvidence: true,
  signedTimestamp: true  // Dla audytu
});
```

## 🚀 Roadmap sugerowany
```
Q1 2025: MVP
├── @deep-verify/core (TypeScript)
├── @deep-verify/cli (npm)
└── Podstawowa dokumentacja

Q2 2025: Developer Experience
├── @deep-verify/vscode
├── GitHub Action
└── Marketplace presence

Q3 2025: Enterprise
├── @deep-verify/compliance
├── Self-hosted server
├── Azure DevOps Task
└── First enterprise pilots

Q4 2025: Scale
├── Custom pattern marketplace
├── Team collaboration features
└── Analytics dashboard
🤔 Pytania do rozstrzygnięcia
Zanim przejdziemy dalej, chciałbym zrozumieć Twoje preferencje:
💎 Rozszerzenie metody weryfikacyjnej
Patrząc na Twój obecny workflow, widzę potencjał rozbudowy w kilku kierunkach:
1. Specialized Pattern Libraries
yaml# Branżowe biblioteki wzorców
pattern-libraries/
├── general/           # Obecna - uniwersalna
├── fintech/           # Regulacje finansowe (MiFID II, PSD2)
├── healthcare/        # HIPAA, HL7 FHIR compliance
├── automotive/        # ISO 26262, ASPICE
├── ai-systems/        # EU AI Act, NIST AI RMF
└── security/          # OWASP, CWE patterns
```

### 2. **Multi-artifact verification**

Nie tylko pojedyncze pliki, ale relacje między nimi:
```
Artifact A (spec) ←→ Artifact B (code) ←→ Artifact C (tests)
         ↓                    ↓                   ↓
    Spójność           Implementacja         Pokrycie
```

### 3. **Continuous Verification**
```
PR Created → Deep Verify → Comments inline → Approve/Request changes
                ↓
         Pattern matches saved
                ↓
         Organization learns
Twoje odpowiedzi na pytania powyżej pomogą mi doprecyzować rekomendacje techniczne i biznesowe!


Rozumiem teraz pełniej Twoją wizję. To nie jest tylko narzędzie do weryfikacji - to zmiana paradygmatu pracy z AI-generated code. Zróbmy głębszy brainstorming.
🎯 Problem który rozwiązujesz
DZIŚ: Chaos z AI-generated code
────────────────────────────────────────────────────────────

Developer ──► "Napisz mi endpoint" ──► AI ──► KOD
                                              │
                                              ▼
                                         ¯\_(ツ)_/¯
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
                    ▼                         ▼                         ▼
              Czy działa?            Czy jest bezpieczny?        Czy jest zgodny
                  🤷                        🤷                    z architekturą?
                                                                      🤷
                    │                         │                         │
                    └─────────────────────────┼─────────────────────────┘
                                              │
                                              ▼
                                    MERGE TO MAIN 🙈
                                              │
                                              ▼
                              6 miesięcy później: audit 💀
🌟 Twoja wizja: Governed AI Development
JUTRO: AI Development z Governance wbudowanym w DNA
────────────────────────────────────────────────────────────

                         ┌──────────────────────────────────┐
                         │      CONTEXT LAYER               │
                         │  ┌────────────────────────────┐  │
                         │  │ • Architecture decisions   │  │
                         │  │ • Coding standards         │  │
                         │  │ • Security policies        │  │
                         │  │ • Compliance requirements  │  │
                         │  │ • Team patterns            │  │
                         │  └────────────────────────────┘  │
                         └──────────────┬───────────────────┘
                                        │
                                        ▼
Developer ──► "Napisz mi endpoint" ──► AI + CONTEXT ──► KOD
                                                         │
                         ┌───────────────────────────────┘
                         │
                         ▼
              ┌──────────────────────────────────────────────┐
              │            VERIFICATION LAYER                │
              │  ┌────────────────────────────────────────┐  │
              │  │ ✓ Deep Verify (logika/spójność)       │  │
              │  │ ✓ Architecture Alignment              │  │
              │  │ ✓ Security Scan                       │  │
              │  │ ✓ Compliance Check (EU AI Act, etc)   │  │
              │  │ ✓ Style/Standards                     │  │
              │  └────────────────────────────────────────┘  │
              └──────────────────────┬───────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
                    ▼                                 ▼
              ┌──────────┐                     ┌──────────────┐
              │ ✅ PASS  │                     │ ⚠️ ISSUES    │
              │  + Report│                     │  + Guidance  │
              └────┬─────┘                     └──────┬───────┘
                   │                                  │
                   ▼                                  ▼
            Auto-approve                      Developer fixes
            (with audit trail)                (with AI assistance)
                   │                                  │
                   └──────────────┬───────────────────┘
                                  │
                                  ▼
                         ┌───────────────┐
                         │  MERGE ✓     │
                         │  Full trace   │
                         │  Compliant    │
                         │  Auditable    │
                         └───────────────┘
🏗️ Ekosystem: "Governed AI Development Platform"
Proponuję nazwę roboczą dla całości: "Aegis" (tarcza ochronna) lub "Sentinel" - ale Deep Verify może być flagowym produktem.
┌─────────────────────────────────────────────────────────────────────────┐
│                           AEGIS PLATFORM                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐         │
│  │   PRE-FLIGHT    │  │   IN-FLIGHT     │  │  POST-FLIGHT    │         │
│  │   ───────────   │  │   ──────────    │  │  ───────────    │         │
│  │                 │  │                 │  │                 │         │
│  │ Context Loader  │  │ Deep Verify     │  │ Audit Trail     │         │
│  │ • Architecture  │  │ • Verification  │  │ • What was gen  │         │
│  │ • Standards     │  │ • Scoring       │  │ • What passed   │         │
│  │ • Compliance    │  │ • Patterns      │  │ • Who approved  │         │
│  │   requirements  │  │                 │  │ • Evidence      │         │
│  │                 │  │ Compliance      │  │                 │         │
│  │ Prompt Enhance  │  │ • EU AI Act     │  │ Reports         │         │
│  │ • Add context   │  │ • SOC2          │  │ • Compliance    │         │
│  │ • Add rules     │  │ • HIPAA         │  │ • Governance    │         │
│  │ • Add examples  │  │ • Custom        │  │ • Analytics     │         │
│  │                 │  │                 │  │                 │         │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘         │
│           │                    │                    │                   │
│           └────────────────────┼────────────────────┘                   │
│                                │                                        │
│                    ┌───────────▼───────────┐                           │
│                    │    KNOWLEDGE BASE     │                           │
│                    │    ──────────────     │                           │
│                    │ • Pattern Library     │                           │
│                    │ • Org Architecture    │                           │
│                    │ • Compliance Rules    │                           │
│                    │ • Historical Data     │                           │
│                    │ • Team Learnings      │                           │
│                    └───────────────────────┘                           │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                          INTEGRATIONS                                   │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐    │
│  │ VSCode │ │  CLI   │ │ Azure  │ │ GitHub │ │ GitLab │ │ Slack  │    │
│  │        │ │        │ │ DevOps │ │Actions │ │   CI   │ │ Teams  │    │
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
👥 User Journeys
Journey 1: Developer (codzienne kodowanie)
┌────────────────────────────────────────────────────────────────────────┐
│  DEVELOPER EXPERIENCE                                                   │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1. WRITE                                                               │
│     ┌─────────────────────────────────────────────────────────┐        │
│     │  VSCode + Aegis Extension                                │        │
│     │                                                          │        │
│     │  > "Create user authentication endpoint with JWT"        │        │
│     │                                                          │        │
│     │  [Aegis Context Injection]                               │        │
│     │  + Your org uses: Express.js, PostgreSQL                 │        │
│     │  + Security policy: bcrypt, rate limiting required       │        │
│     │  + Compliance: GDPR - no plain text passwords            │        │
│     │  + Architecture: /api/v1/* pattern, DTO validation       │        │
│     │                                                          │        │
│     │  AI generates with FULL CONTEXT ──────────────────────►  │        │
│     └─────────────────────────────────────────────────────────┘        │
│                              │                                          │
│                              ▼                                          │
│  2. VERIFY (automatycznie lub on-demand)                               │
│     ┌─────────────────────────────────────────────────────────┐        │
│     │  Deep Verify Results                    [Panel w VSCode] │        │
│     │  ──────────────────────────────────────────────────────  │        │
│     │                                                          │        │
│     │  ✅ Logic & Coherence      Score: -2.5 (SOUND)           │        │
│     │  ✅ Architecture Aligned   Matches: /api/v1/* ✓          │        │
│     │  ⚠️ Security              Issue: Missing rate limit      │        │
│     │  ✅ GDPR Compliance        No PII exposure               │        │
│     │  ✅ Code Standards         ESLint: 0 errors              │        │
│     │                                                          │        │
│     │  [Fix Security Issue] [Accept with caveat] [Reject]      │        │
│     └─────────────────────────────────────────────────────────┘        │
│                              │                                          │
│                              ▼                                          │
│  3. FIX (AI-assisted)                                                  │
│     ┌─────────────────────────────────────────────────────────┐        │
│     │  "Add rate limiting as per security policy"              │        │
│     │                                                          │        │
│     │  AI knows exactly what's needed ─────────────────────►   │        │
│     │  + Your rate limit config: 100 req/min                   │        │
│     │  + Your middleware pattern: express-rate-limit           │        │
│     └─────────────────────────────────────────────────────────┘        │
│                              │                                          │
│                              ▼                                          │
│  4. COMMIT (with evidence)                                             │
│     ┌─────────────────────────────────────────────────────────┐        │
│     │  git commit -m "Add auth endpoint"                       │        │
│     │                                                          │        │
│     │  [Aegis auto-attaches]                                   │        │
│     │  • Verification report hash                              │        │
│     │  • Compliance attestation                                │        │
│     │  • AI interaction trace                                  │        │
│     └─────────────────────────────────────────────────────────┘        │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
Journey 2: Team Lead / Architect (PR Review)
┌────────────────────────────────────────────────────────────────────────┐
│  PR REVIEW EXPERIENCE                                                   │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PR #1234: Add user authentication                                      │
│  ──────────────────────────────────────────────────────────────────    │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────┐       │
│  │  AEGIS VERIFICATION SUMMARY                    [Auto-added] │       │
│  │  ═══════════════════════════════════════════════════════    │       │
│  │                                                             │       │
│  │  Overall: ✅ APPROVED FOR MERGE                             │       │
│  │                                                             │       │
│  │  ┌──────────────────┬──────────────────┬─────────────────┐ │       │
│  │  │ Deep Verify      │ Architecture     │ Compliance      │ │       │
│  │  │ Score: -2.5 ✅   │ Aligned ✅       │ GDPR ✅         │ │       │
│  │  │ Patterns: 0      │ Deviations: 0    │ SOC2 ✅         │ │       │
│  │  │ Confidence: HIGH │                  │                 │ │       │
│  │  └──────────────────┴──────────────────┴─────────────────┘ │       │
│  │                                                             │       │
│  │  AI-Generated Code: 73%                                     │       │
│  │  Verification Coverage: 100%                                │       │
│  │  Human Review Required: Security-sensitive (policy)         │       │
│  │                                                             │       │
│  │  [View Full Report] [View AI Traces] [Approve] [Request]    │       │
│  └─────────────────────────────────────────────────────────────┘       │
│                                                                         │
│  Files changed: 5                                                       │
│  ├── src/api/auth/login.ts      [AI: 100%] [Verified ✅]               │
│  ├── src/api/auth/register.ts   [AI: 85%]  [Verified ✅]               │
│  ├── src/middleware/rateLimit.ts [AI: 100%] [Verified ✅]              │
│  ├── tests/auth.test.ts          [AI: 60%]  [Verified ✅]              │
│  └── docs/api/auth.md            [AI: 100%] [Not verified - docs]      │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
Journey 3: Compliance Officer / CISO (Audit)
┌────────────────────────────────────────────────────────────────────────┐
│  COMPLIANCE DASHBOARD                                                   │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  EU AI Act Compliance Status                    Period: Q1 2025        │
│  ══════════════════════════════════════════════════════════════════    │
│                                                                         │
│  Risk Category: HIGH-RISK AI SYSTEM (Art. 6)                           │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────┐        │
│  │  REQUIREMENTS MATRIX                                        │        │
│  │  ────────────────────────────────────────────────────────   │        │
│  │                                                             │        │
│  │  Art. 9  Risk Management      ████████████░░  87% ⚠️       │        │
│  │  Art. 10 Data Governance      ██████████████  100% ✅       │        │
│  │  Art. 11 Technical Docs       ████████████░░  92% ⚠️       │        │
│  │  Art. 12 Record-keeping       ██████████████  100% ✅       │        │
│  │  Art. 13 Transparency         ██████████████  100% ✅       │        │
│  │  Art. 14 Human Oversight      ████████████░░  95% ⚠️       │        │
│  │  Art. 15 Accuracy/Robustness  ██████████████  100% ✅       │        │
│  │                                                             │        │
│  └────────────────────────────────────────────────────────────┘        │
│                                                                         │
│  AI-Generated Code Governance                                          │
│  ┌────────────────────────────────────────────────────────────┐        │
│  │                                                             │        │
│  │  Total commits this quarter:        1,247                   │        │
│  │  Commits with AI-generated code:    834 (67%)               │        │
│  │  Verified before merge:             834 (100%) ✅           │        │
│  │  Rejected by verification:          127 (15%)               │        │
│  │  Manual review triggered:           89 (11%)                │        │
│  │                                                             │        │
│  │  [Download Audit Report] [Export Evidence] [Schedule Audit] │        │
│  └────────────────────────────────────────────────────────────┘        │
│                                                                         │
│  Recent Compliance Events                                              │
│  ┌────────────────────────────────────────────────────────────┐        │
│  │  🔴 Jan 28: PR #1456 rejected - PII exposure risk          │        │
│  │  🟡 Jan 25: PR #1440 manual review - new AI model used     │        │
│  │  🟢 Jan 24: Quarterly audit passed                          │        │
│  │  🟢 Jan 20: Architecture deviation auto-blocked             │        │
│  └────────────────────────────────────────────────────────────┘        │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
🔑 Kluczowe komponenty do zbudowania
PRIORYTET 1: Core Engine (bez tego nic nie działa)
────────────────────────────────────────────────────
├── Deep Verify Core        ← Masz już algorytm!
├── Context Loader          ← Zbiera kontekst organizacji
├── LLM Adapter Layer       ← Abstrahuje od providera
└── Report Generator        ← Standardowe formaty

PRIORYTET 2: Developer Experience
────────────────────────────────────────────────────
├── VSCode Extension        ← Tu jest adoption
├── CLI                     ← Dla CI/CD i power users
└── Git hooks               ← Pre-commit verification

PRIORYTET 3: Enterprise & Compliance
────────────────────────────────────────────────────
├── Compliance Modules      ← EU AI Act, SOC2, HIPAA
├── Audit Trail Storage     ← Evidence dla audytorów
├── Dashboard               ← Visibility dla leadership
└── Azure DevOps Task       ← Enterprise CI/CD
🤔 Strategiczne pytania
Chciałbym lepiej zrozumieć Twoje możliwości i preferencje:
📊 Dlaczego timing jest idealny
TRENDY RYNKOWE 2025
────────────────────────────────────────────────────

1. EU AI Act wchodzi w życie
   • Sierpień 2025: Zakaz niedozwolonych praktyk
   • Sierpień 2026: Obowiązki dla high-risk AI
   • Firmy TERAZ szukają rozwiązań compliance
   
2. AI-generated code eksploduje
   • GitHub Copilot: 50M+ developerów
   • Cursor, Windsurf, Claude Code: rosnąca adopcja
   • Problem: KTO WERYFIKUJE ten kod?

3. Enterprise "AI Governance" to nowy buzzword
   • Gartner, Forrester piszą raporty
   • CISO/CIO potrzebują narzędzi
   • Budżety są, rozwiązań brak

4. Konkurencja jest słaba
   • SonarQube, Snyk = static analysis (nie AI-aware)
   • Cursor, Copilot = generation (nie verification)  
   • BRAK: AI-native verification + compliance
Twoje odpowiedzi pomogą mi przygotować konkretny plan implementacji i strategię go-to-market!