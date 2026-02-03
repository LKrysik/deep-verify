# Deep Verify V3.0

**Deep Verify** is a rigorous, universal verification workflow designed for **LLM CLIs (e.g., Gemini CLI, Claude CLI)**. It transforms the verification of software artifacts—from code and documentation to architecture and product requirements—into a structured, evidence-based process.

Unlike standard "reviews" which can be subjective, Deep Verify uses a **Pattern Intelligence** engine and a quantitative **Evidence Score** to provide objective verdicts.

## ⚠️ Prerequisites: LLM Required

**This is NOT a standard executable.** Deep Verify is a **Prompt Engineering Workflow**.

To use it, you must have a Large Language Model (LLM) agent capable of reading files and following complex instructions, such as:
*   **Gemini CLI**
*   **Claude CLI**
*   **Ollama** (with a capable model)

The "software" here is a set of rigorous protocols (`workflow.md`) and data files that guide the LLM's reasoning process.

## 🚀 Execution Instructions

To "run" Deep Verify, you must instruct your LLM agent to execute the master workflow file against your target artifact.

**Command Structure:**
> "Execute the process defined in `src/core/deep-verify/workflow.md` to verify [TARGET_FILE]. Pay special attention to [specific aspect if needed]."

**Examples:**

*   **Standard Verification:**
    ```text
    @gemini run src/core/deep-verify/workflow.md on src/auth_service.py
    ```
*   **With Context:**
    ```text
    @claude please verify docs/api_spec.md using the deep-verify workflow in src/core/deep-verify/workflow.md. Check specifically for data consistency.
    ```

*Note: The `verify --quick` or `verify --full` commands mentioned in shorthand are conceptual triggers for the LLM agent, not shell commands.*

---

## 🧠 Core Intelligence Components

Deep Verify relies on specific data files to drive its decision-making. These are not just config files; they are the "brain" of the verification engine.

### 1. Pattern Library (`data/pattern-library.yaml`)
*   **Purpose:** The single source of truth for **Known Impossibilities**. It contains specific patterns that always indicate a flaw (e.g., claiming "Perfect Forward Secrecy" while also having "Key Escrow").
*   **Function:** During Phase 1 (Pattern Scan), the agent checks findings against this library.
*   **Impact:** A match here grants a `+1` score bonus and allows for an **Early Exit (REJECT)**, saving time on obviously flawed artifacts.
*   **Customization:** You can merge domain-specific libraries (e.g., `microservices.yaml`, `medical-research.yaml`) into this file during setup.

### 2. Pattern Update Protocol (`data/pattern-update-protocol.yaml`)
*   **Purpose:** The "Immune System" for the pattern library. It dictates how new patterns are discovered and verified.
*   **Why it matters:** Prevents the library from becoming cluttered with opinions. Only findings grounded in **Theorems**, **Definitions**, **Regulations**, or **Statistics** can enter the library.
*   **Usage:** If the agent finds a Critical issue with no existing pattern match, it may suggest running **Phase 6: Pattern Candidate Evaluation**, which follows this protocol.

### 3. Decision Thresholds (`data/decision-thresholds.yaml`)
*   **Purpose:** The "Judge and Jury." This file defines the exact logic for verdicts.
*   **Configuration:** You can adjust the **Evidence Score (S)** thresholds here.
    *   **Default:** `REJECT if S ≥ 6`, `ACCEPT if S ≤ -3`.
    *   **Stakes Assessment:** Configures how "High Stakes" projects handle uncertainty (e.g., disabling early acceptance).
    *   **Escalation:** Defines triggers that force a human review (e.g., "Methods strongly disagree").

### 4. Report Template (`data/report-template.md`)
*   **Purpose:** Ensures consistent, actionable output.
*   **Function:** The agent fills this template in Phase 5. It forces the agent to:
    *   Cite exact quotes for every finding.
    *   Show the math behind the Evidence Score.
    *   List exactly what was *not* checked.
    *   Provide specific recommendations based on the verdict.

---

## 🛠️ The 6-Step Workflow

Deep Verify operates in **Phases**, moving from broad scanning to targeted adversarial attacks.

1.  **Phase 0: Setup** — Assess stakes and mitigate bias (Blind Mode).
2.  **Phase 1: Pattern Scan** — Rapidly identify "Red Flags" using Tier 1 methods.
3.  **Phase 2: Targeted Analysis** — Deep dives based on specific signals (e.g., "absolute claims" triggers *Theoretical Impossibility Check*).
4.  **Phase 3: Adversarial Validation (MANDATORY)** — We attack our own findings. Only findings that survive scrutiny are reported.
5.  **Phase 4: Verdict** — Calculate Evidence Score (S) and determine outcome.
6.  **Phase 5: Report** — Generate the final artifact.

## 🧰 Key Methods (Sample)

Deep Verify utilizes a library of cognitive methods (sourced from `@methods/methods.csv`):

*   **#71 First Principles Analysis:** Strips away assumptions to rebuild from fundamental truths.
*   **#153 Theoretical Impossibility Check:** Checks claims against known theorems (CAP, FLP, Rice's).
*   **#154 Definitional Contradiction Detector:** Expands terms to find mutually exclusive requirements.
*   **#85 Grounding Check:** Verifies if claims have explicit evidence or are ungrounded assertions.
*   **#116 Strange Loop Detection:** Maps justification graphs to find circular reasoning.
*   **#109 Contraposition Inversion:** Inverts claims to reveal unhandled failure modes.
*   **#165 Constructive Counterexample:** Actively attempts to break a claimed property.
*   **#100 Vocabulary Consistency:** Scans for synonyms (confusion) and homonyms (contradiction).
*   **#17 Abstraction Laddering:** Checks coherence between high-level goals and low-level details.
*   **#63 Challenge from Critical Perspective:** The "Devil's Advocate" phase to steel-man the opposing view.

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