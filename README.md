# Deep Verify V3.0

**Deep Verify** is a rigorous, universal verification workflow designed for LLM CLIs. It transforms the verification of software artifacts—from code and documentation to architecture and product requirements—into a structured, evidence-based process.

Unlike standard "reviews" which can be subjective, Deep Verify uses a **Pattern Intelligence** engine and a quantitative **Evidence Score** to provide objective verdicts.

## 🚀 Why Deep Verify?

In the era of AI-generated content and complex systems, verification is the critical bottleneck. Deep Verify provides a systematic protocol to detect:
- **Theoretical Impossibilities:** Violations of known theorems (CAP, FLP, etc.).
- **Definitional Contradictions:** Mutually exclusive requirements hiding in plain sight.
- **Hidden Assumptions:** Ungrounded claims and invisible dependencies.
- **Structural Flaws:** Circular logic, topological holes, and unhandled failure modes.

**Core Principle:** `NO QUOTE = NO FINDING`. Every critique must be grounded in exact text from the artifact.

## 🛠️ How It Works

Deep Verify operates in **Phases**, moving from broad scanning to targeted adversarial attacks.

### The 6-Step Workflow

1.  **Phase 0: Setup**
    Assess stakes (Low/Medium/High) and mitigate bias using *Blind Mode* or *Forced Alternative Mode*.
2.  **Phase 1: Pattern Scan**
    Rapidly identify "Red Flags" using mandatory Tier 1 methods and the **Pattern Library**.
3.  **Phase 2: Targeted Analysis**
    Deep dives based on specific signals. For example, detecting "absolute claims" triggers the *Theoretical Impossibility Check*.
4.  **Phase 3: Adversarial Validation (MANDATORY)**
    We attack our own findings. Using prompts like "Survivorship Bias" and "Hidden Context," we attempt to weaken our critique. Only findings that survive are reported.
5.  **Phase 4: Verdict**
    A quantitative **Evidence Score (S)** determines the outcome: `ACCEPT`, `REJECT`, or `UNCERTAIN`.
6.  **Phase 5: Report**
    Generation of a structured, actionable report with specific recommendations.

## 🧰 Core Methods

Deep Verify utilizes a library of cognitive and analytical methods. Below are 10 key methods (sourced from `@methods/methods.csv`) that drive the verification engine:

### Tier 1: Mandatory Scan
1.  **#71 First Principles Analysis**
    *   **Goal:** Strip away assumptions to rebuild from fundamental truths.
    *   **Action:** Identifies the 3-5 core claims and asks: "What must be fundamentally true for this to work?" Checks consistency with physics, math, and regulations.
2.  **#100 Vocabulary Consistency**
    *   **Goal:** Ensure semantic precision.
    *   **Action:** Scans for *synonyms* (confusion: same concept, different words) and *homonyms* (contradiction: same word, different meanings).
3.  **#17 Abstraction Laddering**
    *   **Goal:** Check vertical coherence.
    *   **Action:** Moves up (Why?) and down (How?) levels of abstraction to find "orphaned" details or "gap" promises with no implementation.

### Tier 2: Targeted Analysis
4.  **#153 Theoretical Impossibility Check**
    *   **Goal:** Prevent violations of known limits.
    *   **Action:** Checks claims against theorems like CAP, FLP, Halting Problem, or Rice's Theorem. *Example: Claiming "perfect consensus" in an async network.*
5.  **#154 Definitional Contradiction Detector**
    *   **Goal:** Find mutually exclusive requirements.
    *   **Action:** Expands requirements into `MEANS`, `IMPLIES`, and `EXCLUDES`. If `R1.EXCLUDES` overlaps with `R2.MEANS`, a contradiction exists.
6.  **#85 Grounding Check**
    *   **Goal:** Verify evidence quality.
    *   **Action:** Classifies every claim's evidence as *Explicit*, *Implicit*, or *Missing*. Applies the **CUI BONO** test to ungrounded claims.
7.  **#116 Strange Loop Detection**
    *   **Goal:** Identify circular reasoning.
    *   **Action:** Maps justification graphs to find cycles (e.g., A is secure because B; B is secure because A).
8.  **#109 Contraposition Inversion**
    *   **Goal:** Reveal hidden failure modes.
    *   **Action:** Inverts claims ("If A then B" → "If not B then not A") to check if failure conditions are addressed.
9.  **#165 Constructive Counterexample**
    *   **Goal:** Demonstrate actual failure.
    *   **Action:** Actively attempts to construct a specific input or scenario that breaks a claimed property, moving beyond theoretical risk to proven failure.

### Tier 3: Adversarial
10. **#63 Challenge from Critical Perspective**
    *   **Goal:** Overcome confirmation bias.
    *   **Action:** Adopts a hostile "Devil's Advocate" persona to steel-man the opposite view. Required for all high-severity findings.

## 🚦 Usage

Deep Verify is designed to be invoked via your LLM CLI environment.

**Quick Verify (QV)** — *Fast Triage (2-5 min)*
Use for low-stakes artifacts or initial scans.
```bash
# Example
verify --quick < artifact.md
```

**Standard Verify (DV)** — *Full Rigor (15-30 min)*
The default mode for code reviews, architectural decisions, and specs.
```bash
# Example
verify --full < artifact.md
```

## 📊 Scoring System

The **Evidence Score (S)** is calculated dynamically:

| Severity | Points | Description |
| :--- | :--- | :--- |
| **CRITICAL** | `+3` | Fundamental flaw or theorem violation. Alone justifies REJECT. |
| **IMPORTANT** | `+1` | Significant issue. 2-3 together justify REJECT. |
| **MINOR** | `+0.3` | Style/clarity issue. Only matters in aggregate. |
| **Clean Pass** | `-0.5` | Method executed and found no issues. |

**Verdict Thresholds:**
*   **REJECT:** `S ≥ 6`
*   **ACCEPT:** `S ≤ -3`
*   **UNCERTAIN:** `-3 < S < 6`

## 📁 Repository Structure

*   `src/core/deep-verify/workflow.md` — The Master Protocol.
*   `src/core/deep-verify/data/` — Configuration, Pattern Libraries, and Scoring Rules.
*   `src/core/deep-verify/steps/` — The step-by-step prompts used by the agent.
*   `src/core/deep-verify/methods/` — Documentation of all analytical methods.

---
*Documentation generated by Deep Verify Agent.*
