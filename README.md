# Deep Verify V3.0

**Deep Verify** is a rigorous, universal verification workflow designed for **LLM CLIs (e.g., Gemini CLI, Claude CLI)**. It transforms the verification of software artifacts—from code and documentation to architecture and product requirements—into a structured, evidence-based process.

Unlike standard "reviews" which can be subjective, Deep Verify uses a **Pattern Intelligence** engine and a quantitative **Evidence Score** to provide objective verdicts.

## ⚠️ Prerequisites: LLM Required

**This is NOT a standard executable.** Deep Verify is a **Prompt Engineering Workflow**.

To use it, you must have a Large Language Model (LLM) agent capable of reading files and following complex instructions, such as **Gemini CLI**, **Claude CLI**, or **Ollama** (with a capable model).

## 🚀 How to Use (Execution)

The simplest way to run Deep Verify is using the built-in CLI command shortcut.

### 1. Command Shortcut (Simplest)
Just type the command followed by the path to the artifact you want to verify:
*   **`/deep-verify [TARGET_FILE]`**

Example: `/deep-verify src/auth_service.py`

### 2. Manual Invocation
Alternatively, you can instruct your LLM agent to execute the master workflow file directly:
*   `@gemini run src/core/deep-verify/workflow.md on src/auth_service.py`
*   `@claude please verify docs/api_spec.md using src/core/deep-verify/workflow.md.`

---

## 🛠️ The 6-Phase Workflow

1.  **Phase 0: Setup** — Interactive configuration. Assess stakes (Low/Med/High), mitigate bias (Blind Mode), and select execution mode.
2.  **Phase 1: Pattern Scan** — Rapidly identify "Red Flags" using Tier 1 methods.
3.  **Phase 2: Targeted Analysis** — Deep dives based on Phase 1 signals (e.g., "Absolute Claims" trigger "Theoretical Impossibility Check").
4.  **Phase 3: Adversarial Validation (MANDATORY)** — Critical attack on findings ("Devil's Advocate") to ensure they survive scrutiny.
5.  **Phase 4: Verdict** — Final calculation of the Evidence Score (S).
6.  **Phase 5: Report** — Generation of a standardized report with actionable recommendations.
7.  **Phase 6: Pattern Candidate** — (Deep Mode Only) Evaluation of new impossibility patterns for the library.

---

## 🧠 Core Intelligence Components

*   **Pattern Library (`data/pattern-library.yaml`):** The single source of truth for **Known Impossibilities**. Matches grant score bonuses and enable Early Exit (REJECT).
*   **Pattern Update Protocol (`data/pattern-update-protocol.yaml`):** The "Immune System" for the library. Ensures only findings grounded in theorems, definitions, or regulations become patterns.
*   **Decision Thresholds (`data/decision-thresholds.yaml`):** Defines verdict logic (e.g., `REJECT if S ≥ 6`). Configures stakes assessment and escalation triggers.
*   **Report Template (`data/report-template.md`):** Standardizes output, requiring exact quotes, score math, and explicit "not checked" sections.

---

## 🌐 Supported Domains

Deep Verify includes specialized pattern libraries for specific domains:

*   **Core:** Universal impossibilities (Theorems, Logical Contradictions).
*   **Agile Process:** Sprint planning, user stories, and estimation gaming.
*   **Documentation:** API consistency, code examples, and versioning.
*   **Fiction:** Narrative consistency, time travel logic, and world-building rules.
*   **IaC:** Infrastructure as Code (Terraform/CloudFormation) state and drift issues.
*   **Medical Research:** Clinical trials, FDA/HIPAA compliance, and statistical validity.
*   **Microservices:** Distributed systems, CAP theorem, and API contracts.
*   **PRD:** Product requirements, scope creep, and stakeholder conflicts.

---

## 🧰 Method Catalog

Deep Verify employs **18 specialized methods** grouped by tier and function:

### Tier 1: Mandatory Scan (Phase 1)
*   **#71 First Principles Analysis:** Rebuild from fundamental truths to verify core claims.
*   **#100 Vocabulary Consistency:** Scan for synonyms (confusion) and homonyms (contradiction).
*   **#17 Abstraction Laddering:** Check coherence between high-level goals and implementation details.

### Tier 2: Targeted Analysis (Phase 2)
*   **#78 Assumption Excavation:** Surface and stress-test hidden assumptions.
*   **#84 Coherence Check:** Verify internal consistency across document sections.
*   **#85 Grounding Check:** Verify if claims have explicit evidence or are ungrounded assertions.
*   **#86 Topological Hole Detection:** Find structural gaps (dead ends, sinks) in the system graph.
*   **#87 Falsifiability Check:** Verify claims can be tested or are unfalsifiable by theorem.
*   **#109 Contraposition Inversion:** Invert claims to reveal unhandled failure modes.
*   **#116 Strange Loop Detection:** Identify circular reasoning in justification graphs.
*   **#130 Assumption Torture:** Test assumption sensitivity (10%, 50%, 100% error).
*   **#153 Theoretical Impossibility Check:** Check claims against known theorems (CAP, FLP, Rice's).
*   **#154 Definitional Contradiction Detector:** Find requirements that are mutually exclusive by definition.
*   **#159 Transitive Dependency Closure:** Find indirect dependency cycles and conflicts.
*   **#162 Theory-Dependence Verification:** Verify theoretical claims have proper backing.
*   **#163 Existence Proof Demand:** Challenge unproven capability claims.
*   **#165 Constructive Counterexample:** Actively attempt to break a claimed property with a specific scenario.

### Tier 3: Adversarial (Phase 3)
*   **#63 Challenge from Critical Perspective:** Adversarial "Devil's Advocate" review to find weaknesses.

---

## 📊 Scoring System

| Severity | Points | Description |
| :--- | :--- | :--- |
| **CRITICAL** | `+3` | Fundamental flaw. Alone justifies REJECT. |
| **IMPORTANT** | `+1` | Significant issue. 2-3 together justify REJECT. |
| **MINOR** | `+0.3` | Style/clarity issue. |
| **Clean Pass** | `-0.5` | Method executed and found no issues. |

**Verdict:** `REJECT` if S ≥ 6 | `ACCEPT` if S ≤ -3 | `UNCERTAIN` otherwise.

---
*Documentation generated by Deep Verify Agent.*