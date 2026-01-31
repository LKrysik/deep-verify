# M021: Premortem

## Purpose

Imagine failure and trace its causes before it happens.

## Core Question

```
"It's [time later]. We chose [X]. It failed. What went wrong?"
```

## Procedure

### 1. Set the Scene

```
OPTION: [what we're analyzing]
TIMEFRAME: [how far in future]
SCENARIO: "We chose [option]. It failed badly."
```

### 2. Generate Failure Causes

```
Write as if failure already happened:

"The project failed because..."

CAUSES:
1. [cause] - category: [technical/market/execution/external]
2. [cause] - category: [technical/market/execution/external]
3. [cause] - category: [technical/market/execution/external]
4. [cause] - category: [technical/market/execution/external]
5. [cause] - category: [technical/market/execution/external]

Force at least 5 causes.
```

### 3. Assess Preventability

```
For each cause:

CAUSE: [description]

Could we have seen this coming? [Y/N]
If YES → add to risk list
If NO → note as true uncertainty

What would have prevented it?
[prevention measure]
```

### 4. Assess Survivability

```
IF FAILURE HAPPENS:

Can we recover? [Y/N]
What's the worst case? [description]
Is worst case survivable? [Y/N]
```

### 5. Extract Mitigations

```
PREVENTABLE RISKS → MITIGATION PLAN:
• [risk] → [mitigation]
• [risk] → [mitigation]

UNPREVENTABLE → CONTINGENCY:
• [risk] → [what to do if it happens]
```

## Output

```
PREMORTEM: [option]

FAILURE CAUSES:
┌────────────────────────┬──────────────┬──────────────────┐
│ Cause                  │ Preventable? │ Mitigation       │
├────────────────────────┼──────────────┼──────────────────┤
│ [cause 1]              │ YES          │ [action]         │
│ [cause 2]              │ NO           │ [contingency]    │
└────────────────────────┴──────────────┴──────────────────┘

WORST CASE: [description]
SURVIVABLE: [Y/N]
```
