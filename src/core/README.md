# Deep Tools — Verification & Development Workflows for LLM CLI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   ██████╗ ███████╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗      █║
│   ██╔══██╗██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║      █║
│   ██║  ██║█████╗  █████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║      █║
│   ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝        ██║   ██║   ██║██║   ██║██║      █║
│   ██████╔╝███████╗███████╗██║            ██║   ╚██████╔╝╚██████╔╝███████╗ █║
│   ╚═════╝ ╚══════╝╚══════╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ █║
│                                                                              │
│   Rigorous verification + intelligent development for any LLM CLI           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## What Are Deep Tools?

Deep Tools are **structured workflows** that run on any LLM CLI (Claude, Gemini, Ollama, etc.) to provide:

- **Deep Verify (DV)** — Rigorous verification of any artifact with evidence-based scoring
- **Deep Develop (DD)** — Intelligent development with context-aware planning and execution

These are not applications — they're **methodologies encoded as prompts** that transform your LLM into a verification engine or intelligent development assistant.

---

## Quick Start

### Deep Verify — Check if something is correct

```bash
# Quick check
claude "QV this code" < myfile.py

# Full verification
claude "DV this PRD" < product-requirements.md

# Deep verification with domain patterns
claude "DV --domain medical-research" < clinical-trial-protocol.md
```

### Deep Develop — Build something new

```bash
# Quick generation
claude "DD --light: Write a retry decorator with exponential backoff"

# Standard development with context
claude "DD: Add authentication to the API" --scope src/api/

# Deep development with verification
claude "DD --heavy --verify: Implement event sourcing for orders"
```

---

## The Two Workflows

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                          DEEP TOOLS ECOSYSTEM                               │
│                                                                              │
│  ┌─────────────────────────────┐     ┌─────────────────────────────┐       │
│  │                             │     │                             │       │
│  │      DEEP VERIFY (DV)       │     │      DEEP DEVELOP (DD)      │       │
│  │                             │     │                             │       │
│  │  "Is this correct?"         │     │  "How do I build this?"     │       │
│  │                             │     │                             │       │
│  │  INPUT:  Artifact           │     │  INPUT:  Task/Problem       │       │
│  │  OUTPUT: Verdict + Report   │     │  OUTPUT: Solution + Code    │       │
│  │                             │     │                             │       │
│  │  Phases:                    │     │  Phases:                    │       │
│  │  1. Pattern Scan           │     │  1. Context Gathering       │       │
│  │  2. Targeted Analysis      │     │  2. Analysis                │       │
│  │  3. Adversarial Review     │     │  3. Planning                │       │
│  │  4. Verdict                │     │  4. Execution               │       │
│  │  5. Report                 │     │  5. Verification (→ DV)     │       │
│  │                             │     │  6. Output                  │       │
│  └─────────────────────────────┘     └──────────────┬──────────────┘       │
│                 ▲                                    │                      │
│                 │                                    │                      │
│                 └────────────────────────────────────┘                      │
│                           DV validates DD output                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Deep Verify

**Purpose:** Validate any artifact (code, docs, designs, claims) with rigorous, evidence-based analysis.

### Key Features

| Feature | Description |
|---------|-------------|
| **Evidence-based scoring** | Quantified findings with S score |
| **Pattern library** | Known impossibilities and contradictions |
| **Adversarial review** | Challenge your own findings |
| **Multiple modes** | QV (quick), SV (standard), DV (deep) |
| **Domain support** | Medical, microservices, PRD, etc. |

### Verdicts

| Score | Verdict | Action |
|-------|---------|--------|
| S ≥ 6 | REJECT | Artifact has fatal flaws |
| S ≤ -3 | ACCEPT | Artifact appears sound |
| -3 < S < 6 | UNCERTAIN | Cannot determine |
| + ESCALATE | ESCALATE | Needs human expert |

### Example Output

```
═══════════════════════════════════════════════════════════════
VERIFICATION REPORT
═══════════════════════════════════════════════════════════════

VERDICT: REJECT
CONFIDENCE: HIGH
EVIDENCE SCORE: S = 7

KEY FINDINGS:

[F1] CRITICAL — CAP Theorem Violation
     Quote: "Our system provides strong consistency, high
            availability, and handles network partitions"
     Pattern: DC-004 (CAP Violation)
     Method: #153 Theoretical Impossibility Check

...
```

**Full documentation:** [deep-verify/workflow.md](deep-verify/workflow.md)

---

## Deep Develop

**Purpose:** Build new artifacts with context-aware planning and automatic verification.

### Key Features

| Feature | Description |
|---------|-------------|
| **Complexity modes** | Light, Medium, Heavy |
| **Context gathering** | Understands your codebase |
| **Pattern matching** | Follows existing conventions |
| **Plan approval** | Review before execution (Heavy) |
| **DV integration** | Auto-verify generated code |

### Modes

| Mode | When to Use | Time |
|------|-------------|------|
| **Light** | Simple, well-defined tasks | Seconds |
| **Medium** | Tasks requiring context | 30s-2min |
| **Heavy** | Complex, multi-step work | 2-10min |

### Domains

- **Code** — backend, frontend, data-engineering, devops
- **Documentation** — technical, user docs, runbooks
- **Book** — fiction, non-fiction, technical writing
- **API** — REST, GraphQL, gRPC design
- **Data** — analysis, pipelines, modeling

### Example Output

```
═══════════════════════════════════════════════════════════════
DEEP DEVELOP RESULT
═══════════════════════════════════════════════════════════════

TASK: Add Redis caching to user service
MODE: MEDIUM

ANALYSIS:
• Found existing caching pattern in product service
• User service has 3 cacheable functions

PLAN:
1. Create cache utilities
2. Add caching decorators
3. Implement invalidation

CHANGES:
📄 CREATE: src/services/user/cache.py
📝 MODIFY: src/services/user/repository.py

VERIFICATION: ACCEPT (S = -2.5)
```

**Full documentation:** [deep-develop/workflow.md](deep-develop/workflow.md)

---

## Directory Structure

```
src/core/
├── README.md                   ← YOU ARE HERE
│
├── deep-verify/                # Verification workflow
│   ├── workflow.md             # Main workflow documentation
│   ├── data/
│   │   ├── pattern-library.yaml        # Known patterns
│   │   ├── pattern-libraries/          # Domain-specific patterns
│   │   ├── method-procedures/          # 18 verification methods
│   │   ├── report-template.md          # Output format
│   │   ├── severity-scoring.yaml       # Scoring rules
│   │   ├── method-clusters.yaml        # Method selection
│   │   └── calibration.yaml            # Accuracy tracking
│   └── steps/                  # Detailed phase guides
│
└── deep-develop/               # Development workflow
    ├── workflow.md             # Main workflow documentation
    ├── data/
    │   ├── domains/            # Domain configurations
    │   ├── methods/            # Analysis/planning methods
    │   └── templates/          # Output templates
    └── examples/               # Usage examples
```

---

## CLI Integration

### Supported CLIs

| CLI | Trigger Pattern |
|-----|-----------------|
| Claude CLI | `claude "DV ..." < file` |
| Gemini CLI | `gemini "DV ..." < file` |
| Ollama | `ollama run model "DV ..."` |
| Any LLM CLI | Works with prompt piping |

### Common Options

```bash
# Mode selection
--quick, -q          # Quick verification (QV)
--full               # Standard verification (SV)
--deep, --heavy      # Deep verification/development

# Context
--context file.py    # Add specific files
--context-level project  # Include project context

# Domain
--domain medical     # Use medical patterns
--domain microservices   # Use distributed systems patterns

# Output
--output json        # JSON output for CI/CD
--verify             # Run DV on DD output
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Deep Verify PR
on: [pull_request]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Verify Changes
        run: |
          for file in $(git diff --name-only origin/main); do
            claude "DV --output json" < "$file" >> results.json
          done

      - name: Check for Critical Issues
        run: |
          if jq -e '.[] | select(.verdict == "REJECT")' results.json; then
            exit 1
          fi
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

for file in $(git diff --cached --name-only); do
  result=$(claude "QV --output json" < "$file")
  if echo "$result" | jq -e '.verdict == "REJECT"' > /dev/null; then
    echo "❌ $file failed verification"
    exit 1
  fi
done
```

---

## Customization

### Project Configuration

Create `.deep-tools/config.json`:

```json
{
  "verify": {
    "defaultMode": "standard",
    "patterns": ["core", "microservices"],
    "autoVerify": true
  },
  "develop": {
    "defaultMode": "medium",
    "domain": "code",
    "subDomain": "backend",
    "context": {
      "alwaysInclude": ["src/config.py"]
    }
  }
}
```

### Custom Patterns

Add patterns to `.deep-tools/patterns/`:

```yaml
# custom-patterns.yaml
my_patterns:
  NO_PRINT_IN_PROD:
    id: CUSTOM-001
    name: "No print() in Production"
    signals: ["print("]
    severity: WARNING
    check: "Is print() used outside debug/test files?"
```

---

## Philosophy

### Why These Tools Exist

1. **LLMs are powerful but need structure** — Raw prompting lacks rigor
2. **Evidence matters** — Every claim should be backed by quotes
3. **Adversarial thinking catches errors** — Always challenge your findings
4. **Context is king** — Understand before creating
5. **Integration beats isolation** — DV and DD work together

### Design Principles

- **CLI-first** — Works with any LLM CLI, no special tools needed
- **Modular** — Methods and patterns are separate files
- **Extensible** — Add your own patterns and domains
- **Transparent** — Score calculations and reasoning are visible
- **Practical** — Multiple modes for different needs

---

## Version

- **Deep Verify:** V3.0
- **Deep Develop:** V1.0
- **Last Updated:** 2025-01-30

---

## License

These workflows are designed to be used with your LLM of choice. No warranties provided — verify important findings with domain experts.
