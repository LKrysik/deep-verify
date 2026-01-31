# Deep Develop V1.0 — Solution Development Workflow for LLM CLI

## CORE PHILOSOPHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP = ANALYZE + PLAN + EXECUTE + VERIFY                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT:   Task/problem to solve + project context                          │
│  OUTPUT:  Solution (code, documentation, design) + verification report     │
│                                                                              │
│  PRINCIPLE: CONTEXT IS KING                                                 │
│             Understand existing patterns before creating new ones           │
│                                                                              │
│  EXECUTION: Designed for LLM CLI (Claude, Gemini, Ollama, etc.)           │
│             Multi-step process with checkpoints                             │
│                                                                              │
│  INTEGRATION: Uses Deep Verify for quality assurance                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DEEP VERIFY vs DEEP DEVELOP

| Aspect | Deep Verify | Deep Develop |
|--------|-------------|--------------|
| **Goal** | Validate existing artifacts | Create new artifacts |
| **Input** | Artifact to check | Problem/task to solve |
| **Output** | Verification report | Solution + optional report |
| **Question** | "Is this correct?" | "How do I build this?" |
| **Process** | Single-pass analysis | Multi-step development |
| **Timing** | After creation | Before/during creation |

---

## COMPLEXITY MODES

### Light Mode — Quick Generation
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LIGHT MODE                                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  For: Simple, well-defined tasks                                            │
│  Time: Seconds                                                               │
│  Cost: Low (1 LLM call)                                                     │
│                                                                              │
│  Flow:                                                                       │
│  [Task] → [Minimal Context] → [Generate] → [Output]                        │
│                                                                              │
│  Examples:                                                                   │
│  • "Write a sort function"                                                  │
│  • "Fix this syntax error"                                                  │
│  • "Add a docstring to this function"                                      │
│                                                                              │
│  Triggers: `DD --light`, `DD -l`, `quick`                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Medium Mode — Standard Development
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MEDIUM MODE                                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  For: Tasks requiring context and planning                                  │
│  Time: 30 seconds - 2 minutes                                               │
│  Cost: Medium (2-5 LLM calls)                                               │
│                                                                              │
│  Flow:                                                                       │
│  [Task] → [Gather Context] → [Analyze] → [Plan] → [Execute] → [Output]    │
│                                                                              │
│  Examples:                                                                   │
│  • "Add a new API endpoint"                                                 │
│  • "Write tests for this module"                                            │
│  • "Refactor this function for readability"                                │
│                                                                              │
│  Triggers: `DD`, `DD --medium`, default                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Heavy Mode — Deep Development
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HEAVY MODE                                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  For: Complex tasks requiring deep analysis                                 │
│  Time: 2-10 minutes                                                          │
│  Cost: High (5-20+ LLM calls)                                               │
│                                                                              │
│  Flow:                                                                       │
│  [Task] → [Deep Context] → [Multi-angle Analysis] → [Options] →            │
│  [Detailed Plan] → [Phased Execution] → [Verification] → [Iteration]      │
│                                                                              │
│  Examples:                                                                   │
│  • "Design a caching layer for the user service"                           │
│  • "Implement authentication system"                                        │
│  • "Write Chapter 5 of the book following the outline"                     │
│                                                                              │
│  Triggers: `DD --heavy`, `DD -h`, `DD --deep`                              │
│                                                                              │
│  Features:                                                                   │
│  • User checkpoint before execution (approve plan)                         │
│  • Phased execution with verification after each phase                     │
│  • Deep Verify integration on output                                        │
│  • Rollback capability if issues detected                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## EXECUTION FLOW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP FLOW                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  1. INPUT                                                            │   │
│  │     • Task description in natural language                          │   │
│  │     • Mode: light / medium / heavy (or auto-detect)                │   │
│  │     • Domain: code / documentation / book / api / data              │   │
│  │     • Scope: files / folders / project                             │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  2. CONTEXT GATHERING                                                │   │
│  │     LIGHT:  Active file only                                        │   │
│  │     MEDIUM: Scope + imports + related files + config                │   │
│  │     HEAVY:  Project + git history + documentation                   │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  3. ANALYSIS (skip for LIGHT)                                        │   │
│  │     • Identify existing patterns in codebase                        │   │
│  │     • Map dependencies and impact                                   │   │
│  │     • Detect conventions to follow                                  │   │
│  │     • HEAVY: Evaluate trade-offs between approaches                │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  4. PLANNING (skip for LIGHT)                                        │   │
│  │     MEDIUM: Simple step-by-step plan                                │   │
│  │     HEAVY:  Phased plan with checkpoints                            │   │
│  │             ★ USER CHECKPOINT: Approve plan before execution        │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  5. EXECUTION                                                        │   │
│  │     LIGHT:  Single generation                                       │   │
│  │     MEDIUM: Execute plan steps                                      │   │
│  │     HEAVY:  Execute phase by phase with verification                │   │
│  │             Checkpoint between phases if configured                 │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  6. VERIFICATION (MEDIUM/HEAVY)                                      │   │
│  │     • Syntax check (for code)                                       │   │
│  │     • Deep Verify integration                                       │   │
│  │     • Consistency check with existing code                          │   │
│  │     If issues → auto-fix or flag for user                          │   │
│  └──────────────────────────────┬──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  7. OUTPUT                                                           │   │
│  │     • Generated artifacts (code, docs, etc.)                        │   │
│  │     • Execution summary                                              │   │
│  │     • Verification results (if enabled)                             │   │
│  │     • Options: [Apply] [Edit] [Iterate] [New Task]                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DOMAINS

### Code Domain
```
Sub-domains: backend, frontend, data-engineering, devops, mobile

Methods:
• Pattern detection — Find and follow existing patterns
• Dependency analysis — Understand what's connected
• Type inference — Maintain type consistency
• Test generation — Create tests alongside code

Context sources:
• Source files
• Package manifests (package.json, pyproject.toml, etc.)
• Config files
• Existing tests
• Git history
```

### Documentation Domain
```
Sub-domains: technical-docs, user-docs, api-docs, runbooks

Methods:
• Structure analysis — Match existing documentation style
• Terminology extraction — Use consistent terms
• Cross-reference checking — Ensure links are valid
• Readability scoring — Maintain accessibility

Context sources:
• Existing documentation
• Code (for technical docs)
• Style guides
• Glossaries
```

### Book Domain
```
Sub-domains: fiction, non-fiction, technical-book

Methods:
• Outline management — Follow chapter structure
• Character/concept tracking — Maintain consistency
• Narrative flow — Ensure logical progression
• Word count management — Hit targets

Context sources:
• Previous chapters
• Character sheets / concept definitions
• Plot outline / book structure
• Style samples
• Research notes
```

### API Domain
```
Sub-domains: rest-api, graphql, grpc, event-driven

Methods:
• Schema validation — Ensure valid schemas
• Contract analysis — Check breaking changes
• Consistency checking — Match existing endpoints
• SDK generation — Create client code

Context sources:
• OpenAPI/Swagger specs
• Existing endpoints
• Client implementations
• API guidelines
```

### Data Domain
```
Sub-domains: analysis, modeling, pipeline

Methods:
• Schema inference — Understand data structure
• Data profiling — Know what you're working with
• Query optimization — Write efficient queries
• Lineage tracking — Understand data flow

Context sources:
• Data schemas
• Sample data
• Existing queries
• Pipeline definitions
```

---

## ANALYSIS METHODS

### Decomposition
```
Purpose: Break complex tasks into smaller parts
Used in: MEDIUM, HEAVY
How: Identify sub-tasks, order by dependency, size appropriately
```

### Context Mapping
```
Purpose: Find relevant files/code for the task
Used in: MEDIUM, HEAVY
How: Analyze imports, search for related patterns, trace dependencies
```

### Pattern Recognition
```
Purpose: Detect and follow existing patterns
Used in: All modes
How: Look for repeated structures, naming conventions, architectural choices
```

### Impact Analysis
```
Purpose: Understand what the change affects
Used in: HEAVY
How: Map consumers of changed code, identify breaking changes
```

### Trade-off Evaluation
```
Purpose: Compare different approaches
Used in: HEAVY
How: List options, analyze pros/cons, recommend with reasoning
```

---

## CLI INVOCATION

### Basic Usage
```bash
# Light mode — quick generation
claude "DD --light: Write a function to parse JSON safely"

# Medium mode — standard development
claude "DD: Add Redis caching to the user service" \
  --scope src/services/user/

# Heavy mode — deep development
claude "DD --heavy: Implement OAuth2 authentication" \
  --scope src/auth/ \
  --verify
```

### With Context Files
```bash
# Include specific context
claude "DD: Add validation to this form" \
  --context src/forms/base.py src/validators/

# Include project context
claude "DD: Refactor to use dependency injection" \
  --context-level project
```

### Plan-Only Mode
```bash
# Generate plan without execution
claude "DD --plan-only: Migrate database to PostgreSQL"

# Execute a saved plan
claude "DD --execute-plan migration-plan.json"
```

### With Verification
```bash
# Auto-verify output with Deep Verify
claude "DD --verify: Add error handling to API endpoints"

# Specify verification mode
claude "DD --verify=full: Implement payment processing"
```

---

## OUTPUT FORMAT

### Standard Output
```
═══════════════════════════════════════════════════════════════
DEEP DEVELOP RESULT
═══════════════════════════════════════════════════════════════

TASK: Add Redis caching to user service
MODE: MEDIUM
DOMAIN: code/backend

───────────────────────────────────────────────────────────────
ANALYSIS
───────────────────────────────────────────────────────────────

Context gathered:
• Found existing Redis connection in src/config/redis.py
• Caching pattern used in src/services/product/cache.py
• User service has 3 cacheable functions

Pattern detected: Decorator-based caching with TTL

───────────────────────────────────────────────────────────────
PLAN
───────────────────────────────────────────────────────────────

1. Create cache utilities following existing pattern
2. Add caching to get_user()
3. Add caching to get_user_by_email()
4. Add cache invalidation to update_user()

───────────────────────────────────────────────────────────────
CHANGES
───────────────────────────────────────────────────────────────

📄 CREATE: src/services/user/cache.py
----------------------------------------
[generated code here]

📝 MODIFY: src/services/user/repository.py
----------------------------------------
[diff here]

───────────────────────────────────────────────────────────────
VERIFICATION (if --verify)
───────────────────────────────────────────────────────────────

Deep Verify Result: ACCEPT
Score: S = -2.5
No critical issues found.

═══════════════════════════════════════════════════════════════
```

### JSON Output (for CI/CD)
```bash
claude "DD --output json: Add logging" | jq .
```

```json
{
  "success": true,
  "task": "Add logging",
  "mode": "medium",
  "domain": "code",
  "outputs": [
    {
      "type": "create",
      "path": "src/logging/config.py",
      "content": "..."
    },
    {
      "type": "modify",
      "path": "src/main.py",
      "diff": "..."
    }
  ],
  "verification": {
    "verdict": "ACCEPT",
    "score": -2.5,
    "findings": []
  },
  "metadata": {
    "duration": 45,
    "llm_calls": 3,
    "context_files": 5
  }
}
```

---

## INTEGRATION WITH DEEP VERIFY

Deep Develop uses Deep Verify to ensure quality:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  VERIFY INTEGRATION                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  WHEN --verify is enabled:                                                  │
│                                                                              │
│  1. After EXECUTION completes                                               │
│     → Run Deep Verify QV on generated code                                  │
│                                                                              │
│  2. If findings detected:                                                    │
│     MINOR → Include in output, continue                                     │
│     IMPORTANT → Flag, offer auto-fix                                        │
│     CRITICAL → Auto-fix or block application                               │
│                                                                              │
│  3. Auto-fix flow:                                                          │
│     → Analyze finding                                                        │
│     → Generate fix                                                           │
│     → Re-verify                                                              │
│     → If still issues → flag for user                                       │
│                                                                              │
│  HEAVY mode with --verify=full:                                             │
│     → Run Deep Verify SV (full process)                                     │
│     → Check for pattern violations                                          │
│     → Adversarial review of generated code                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## CONTINUATION & ITERATION

```bash
# Continue from previous result
claude "DD --continue: Now add tests for the caching layer"

# Iterate on output
claude "DD --iterate: Make the cache TTL configurable"

# Fix issues
claude "DD --fix: Address the race condition mentioned in verification"
```

---

## CONFIGURATION

### Project-Level Config
```json
// .deep-develop/config.json
{
  "domain": {
    "type": "code",
    "subType": "data-engineering"
  },
  "defaultMode": "medium",
  "autoVerify": true,
  "context": {
    "alwaysInclude": [
      "src/config/settings.py",
      "src/utils/common.py"
    ],
    "exclude": [
      "**/*.test.py",
      "**/fixtures/**"
    ]
  },
  "savedPrompts": {
    "new-pipeline": "Create a new data pipeline for {description}",
    "add-tests": "Add tests for {target} following existing patterns"
  }
}
```

---

## DIRECTORY STRUCTURE

```
deep-develop/
├── workflow.md                 ← YOU ARE HERE
├── data/
│   ├── domains/
│   │   ├── code.yaml           # Code domain methods and patterns
│   │   ├── documentation.yaml  # Documentation domain
│   │   ├── book.yaml           # Book writing domain
│   │   ├── api.yaml            # API design domain
│   │   └── data.yaml           # Data domain
│   ├── methods/
│   │   ├── analysis.yaml       # Analysis methods
│   │   ├── planning.yaml       # Planning methods
│   │   └── execution.yaml      # Execution methods
│   └── templates/
│       ├── output-text.md      # Text output template
│       └── output-json.json    # JSON output template
└── examples/
    ├── light-mode.md           # Light mode examples
    ├── medium-mode.md          # Medium mode examples
    └── heavy-mode.md           # Heavy mode examples
```

---

## BEST PRACTICES

### When to Use Each Mode

| Situation | Mode | Why |
|-----------|------|-----|
| Quick fix, simple function | Light | No planning needed |
| New feature in existing pattern | Medium | Need context, but straightforward |
| New architecture component | Heavy | Requires analysis and phased approach |
| Bug fix with known solution | Light | Direct execution |
| Refactoring with dependencies | Heavy | Impact analysis needed |
| Documentation update | Medium | Consistency checking needed |
| Full chapter/section writing | Heavy | Structure and consistency critical |

### Getting Good Results

1. **Be specific** — "Add Redis caching with 5-min TTL" > "Add caching"
2. **Provide context** — Include related files when asking
3. **Use appropriate mode** — Don't use Heavy for simple tasks
4. **Enable verification** — Catch issues before they ship
5. **Iterate** — Use `--continue` for complex multi-step work

---

## VERSION HISTORY

- **V1.0** — Initial release, CLI-focused workflow
