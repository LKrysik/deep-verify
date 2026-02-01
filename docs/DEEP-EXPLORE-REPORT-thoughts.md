
# DEEP EXPLORE: Exploration Report
## On the subject of a unified workflow system from `thoughts.md`

---

- **Decision Problem:** How to design a comprehensive, unified, and controllable system for managing the entire lifecycle of a complex project using an LLM, integrating deterministic processes with adaptive frameworks.
- **Exploration Depth:** DEEP
- **Date:** 2026-02-01

---

### **Section 1: What We Learned (Key Insights)**

The exploration process transformed the initial problem into a concrete architectural solution. The most critical insights are:

1.  **The Core Problem is DAG Management:** The user's desire for a traceable, dynamic "plan" is a classic Directed Acyclic Graph (DAG) problem. Framing it this way unlocks decades of established solutions from software engineering.

2.  **LLMs are Executors, Not Orchestrators:** The biggest risk identified is asking an LLM to manage the state and logic of a complex, evolving plan. The LLM excels at executing well-defined, contextual tasks (a single step), but is not reliable as a stateful orchestrator. The architecture must reflect this.

3.  **Use Existing Tools for Core Problems:** Building a custom DAG orchestrator is a difficult and unnecessary task. Battle-tested tools like **DVC (Data Version Control)** already provide the exact functionality needed: defining a DAG in a YAML file, tracking file-based dependencies, and executing commands.

4.  **A Hybrid Architecture is the Solution:** The most robust architecture is a hybrid that combines the strengths of the user's existing `BMAD` framework with the reliability of a tool like DVC.

5.  **Change Management Requires a Formal Process:** Dynamic adaptation shouldn't mean "live editing the plan." It should be a formal process of "re-planning," where a dedicated workflow (`deep-plan`) generates a new, version-controlled definition of the plan (`dvc.yaml`), which is then reviewed and committed.

### **Section 2: What We Still Don't Know (Implementation Gaps)**

The exploration successfully answered the foundational strategic questions. The remaining gaps are now concrete engineering tasks, not unknowns:

1.  **`run_bmad.py` Wrapper Script:** The design and implementation of the command-line wrapper that can invoke any `BMAD` workflow with the correct `agent` context.
2.  **`deep-plan` Workflow Design:** The detailed prompts and logic for the conversational workflow that will guide a user in modifying the `dvc.yaml` file.
3.  **`BMAD` Interactivity Refactor:** A strategy is needed for handling `BMAD` workflows that require user interaction. They likely need to be refactored to take all inputs as command-line arguments to work with DVC.
4.  **YAML Schema Definition:** A formal, documented schema for the `dvc.yaml` file, defining how `BMAD` concepts like `agent` are represented.

### **Section 3: Option Map**

The exploration revealed a clear spectrum of architectural choices, with the DVC-BMAD Hybrid emerging as the strongest.

| Dimension | Option A: `BMAD` Native | Option B: **DVC-BMAD Hybrid (Recommended)** | Option C: Custom Symbolic (`thoughts.md`) |
| :--- | :--- | :--- | :--- |
| **Plan Definition** | Implicitly in `nextStep:` links | Explicitly in `dvc.yaml` | Custom symbolic language file |
| **Orchestrator** | LLM following steps | `dvc repro` CLI | Custom LLM-based interpreter |
| **Reliability** | High (for linear tasks) | **Very High** | Low (brittle, ambiguous) |
| **Flexibility** | Low | **Medium** (via formal replanning) | High (but chaotic) |
| **Traceability** | Low (must read all files) | **Very High** (via `git diff dvc.yaml`) | Medium (if notation is clear) |
| **Effort to Build** | Already exists | Medium (new scripts needed) | High (custom parser + orchestrator) |

### **Section 4: Strategic Clusters**

The options cluster into two main strategic approaches:

1.  **LLM-as-Orchestrator (High Risk, High "Magic"):** This cluster includes the original idea from `thoughts.md`. It aims for a natural language, fluid interface where the LLM understands and manages the plan directly. Our exploration revealed this to be brittle and unreliable due to the limitations of LLMs in state management.

2.  **LLM-as-Executor (Low Risk, High Reliability):** This cluster, which includes the recommended DVC-BMAD Hybrid, treats the LLM as a powerful tool to be called by a traditional, deterministic orchestrator. The LLM does the complex cognitive work within a task, but the plan's structure and state are managed by a reliable, external tool. This is the professional software engineering approach.

### **Section 5: Consequence Map (for DVC-BMAD Hybrid)**

- **Positive Consequences:**
  - **Reliability:** The system will execute predictably. Dependency checks are handled by a robust tool.
  - **Auditability:** Every change to the plan is a Git commit. `git blame` on `dvc.yaml` will show who changed what, when, and why.
  - **Modularity:** The system is composed of discrete, testable parts (the DVC file, the wrapper script, the `BMAD` workflows).
  - **Reusability:** Core `BMAD` assets are preserved and leveraged.

- **Negative Consequences (Trade-offs):**
  - **Increased Formality:** The process is more rigid than a simple conversation with an LLM. There is more "ceremony."
  - **Learning Curve:** Users must understand the basics of DVC and the `dvc.yaml` structure.
  - **New Components to Build:** The `run_bmad.py` wrapper and the `deep-plan` workflow must be created.

### **Section 6: Decision Readiness**

The decision to **adopt the DVC-BMAD Hybrid Model architecture** is assessed as **READY**. The exploration has been exhaustive, the risks of alternatives are well-understood, and the proposed path is a clear, robust, and feasible synthesis of all the insights gathered.

### **Section 7: Suggested Next Steps**

1.  **Prototype the `run_bmad.py` wrapper.** Create a simple Python script that can take a workflow name and agent name as arguments and correctly execute a single `BMAD` workflow.
2.  **Create a sample `dvc.yaml` file by hand.** Manually define a simple, two-step pipeline (e.g., `create-prd` -> `deep-risk`) to serve as a tangible target.
3.  **Run the pipeline.** Use the `dvc repro` command to execute the manually-created `dvc.yaml` via the `run_bmad.py` wrapper. This will validate the core mechanics of the architecture.
4.  **Begin designing the `deep-plan` workflow.** Start outlining the conversational steps and logic needed to guide a user through the process of generating or modifying the `dvc.yaml` file.
5.  **Archive the Symbolic Notation Idea.** The custom notation from `thoughts.md` was a valuable catalyst for this exploration, but the research has shown it is not a viable path. It should be archived as a research artifact.
