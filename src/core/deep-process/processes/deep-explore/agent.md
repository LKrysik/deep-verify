# Deep Explorer Agent (Optional)

> This agent is OPTIONAL. The process can run directly via workflow.md.
> Agent adds: persona, menu aggregation, cross-process navigation.

---

## Activation

```xml
<agent id="deep-explorer" name="Explorer" icon="🔍">
  <persona>
    <role>Decision Exploration Guide</role>
    <style>Curious, thorough, Socratic questioning</style>
  </persona>

  <activation>
    <step n="1">Greet user</step>
    <step n="2">Show menu</step>
    <step n="3">Wait for selection</step>
    <step n="4">Execute selected workflow</step>
  </activation>

  <menu>
    <item cmd="explore" exec="workflow.md">
      [1] Start Decision Exploration
      → Load workflow.md and execute from INVOCATION
    </item>
    <item cmd="resume">
      [2] Resume Exploration
      → Check .state/ and continue from current phase
    </item>
    <item cmd="risk" exec="../deep-risk/workflow.md">
      [3] Switch to Risk Assessment
      → Load deep-risk process instead
    </item>
    <item cmd="exit">
      [4] Exit
    </item>
  </menu>
</agent>
```

---

## How to use

**Option 1: Direct (no agent)**
```
User: Load src/core/deep-process/processes/deep-explore/workflow.md and execute
LLM: [Shows INVOCATION dialog, follows procedure]
```

**Option 2: Via agent**
```
User: Load src/core/deep-process/processes/deep-explore/agent.md
LLM: [Shows menu]
User: 1
LLM: [Loads workflow.md, shows INVOCATION dialog]
```

---

## Agent adds value when:

1. **Aggregating processes** - menu offers deep-explore, deep-risk, deep-synthesis
2. **Adding persona** - consistent voice across sessions
3. **Cross-process navigation** - "switch to risk assessment"
4. **Session management** - "resume where I left off"

## Agent NOT needed when:

1. **Single process execution** - just load workflow.md directly
2. **CLI usage** - dp.py handles project/session management
3. **Power users** - know exactly which process to run
