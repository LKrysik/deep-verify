# Deep Explore

**Structured Decision Space Exploration for AI-Assisted Conversations**

A companion to [Deep Verify](../deep-verify/) — while Deep Verify validates artifacts, Deep Explore maps decision spaces.

## The Problem Deep Explore Solves

When talking to AI about decisions, a common pattern emerges:

```
User: "What database should I use?"
AI: "Here are the options: A, B, or C. I recommend B because..."

User chooses B, conversation continues...

Meanwhile: Options D, E, F never mentioned
           Dimensions not explored (hosting? scale? cost model?)
           Consequences not mapped
           Better solution possibly missed
```

**Deep Explore prevents premature convergence** by systematically exploring the full decision space before narrowing.

## Core Philosophy

```
┌─────────────────────────────────────────────────────────────────────────┐
│  DIMENSION BEFORE OPTION                                                │
│  What are the axes of choice before what should I choose               │
├─────────────────────────────────────────────────────────────────────────┤
│  CONSEQUENCE BEFORE JUDGMENT                                            │
│  What happens if X before is X good                                    │
├─────────────────────────────────────────────────────────────────────────┤
│  USER CONVERGES, NOT AI                                                 │
│  AI maps territory; User navigates                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

## Quick Start

### CLI Usage

```bash
# Quick exploration - map dimensions and options
claude "QE: What are my options for this architecture?" < context.md

# Standard exploration - full process
claude "DE: Explore monetization strategies" < business_context.md

# Strategic exploration - maximum breadth
claude "DE --strategic: Market entry approach" < market_analysis.md
```

### Workflow Overview

```
PHASE 0: FRAME
├── Define vision (outcome, not solution)
├── Identify hard constraints
├── Set abstraction level (strategic/tactical/operational)
└── Classify problem type (Cynefin)

PHASE 1: MAP (Divergent)
├── #1 Dimension Discovery - find all axes of choice
├── #2 Option Enumeration - list ALL options per dimension
├── #3 Constraint Mapping - eliminate impossible combinations
└── OUTPUT: Morphological Box

PHASE 2: ILLUMINATE (Still Divergent)
├── #11 Consequence Analysis - first/second/third order effects
├── #12 Reversibility Check - points of no return
├── #13 Dependency Analysis - what must be decided first
└── OUTPUT: Decision Consequence Map

PHASE 3: CHALLENGE (Adversarial)
├── #21 Premortem - imagine failure, trace causes
├── #22 Black Swan Hunt - low-probability high-impact events
├── #23 Assumption Stress Test - what if we're wrong?
└── OUTPUT: Stress-tested Options

PHASE 4: SYNTHESIZE
├── Cluster natural option groups
├── Sequence decisions (what first?)
├── Identify real options (what can be delayed?)
└── OUTPUT: Decision Priority Map

PHASE 5: CONVERGE (User-driven)
├── Present trade-offs without recommendation
├── Document uncertainties
├── Design experiments if needed
└── OUTPUT: Exploration Report (User decides)
```

## Coverage Scoring

Unlike Deep Verify's evidence-based scoring for flaws, Deep Explore uses coverage-based scoring for completeness:

| What's Discovered | Points |
|-------------------|--------|
| New dimension | +2 |
| New option per dimension | +1 |
| Consequence mapped | +0.5 |
| Constraint identified | +0.5 |
| Blind spot found | +1 |
| Risk surfaced | +0.5 |

| Coverage Score | Level | Guidance |
|----------------|-------|----------|
| C ≥ 20 | COMPREHENSIVE | Safe to converge |
| 10 ≤ C < 20 | ADEQUATE | Most scenarios covered |
| 5 ≤ C < 10 | PARTIAL | Significant gaps likely |
| C < 5 | INSUFFICIENT | Don't decide yet |

## Decision Archetypes

Common traps to watch for:

| Archetype | Pattern | Check |
|-----------|---------|-------|
| False Dichotomy | Only 2 options | Find the third way |
| Sunk Cost Anchor | Past investments influence | Start fresh test |
| Premature Optimization | Details before exploration | Phase 1 complete? |
| Analysis Paralysis | Endless exploration | Time limit set? |
| Hobson's Choice | Fake choice | Challenge constraints |

## Theoretical Foundations

Deep Explore is built on:

1. **Double Diamond** (Design Council) - Diverge before converge
2. **Morphological Analysis** (Zwicky) - Systematic combination exploration
3. **Cynefin Framework** (Snowden) - Match approach to problem type
4. **Real Options Theory** - Value of preserving optionality
5. **Premortem** (Klein) - Prospective hindsight

## Integration with Deep Verify

```
Explore → Decide → Implement → Verify

Deep Explore          User Decision       Create         Deep Verify
(map options)    →    (selects one)   →  (artifact)  →  (validate)
```

When Deep Verify finds issues, Deep Explore can map alternative approaches.

## Directory Structure

```
deep-explore/
├── workflow.md                    # Main workflow document
├── data/
│   ├── methods.csv                # Method definitions
│   ├── method-procedures/         # Individual method procedures
│   │   ├── 001_Dimension_Discovery.md
│   │   ├── 002_Option_Enumeration.md
│   │   ├── 003_Constraint_Mapping.md
│   │   ├── 011_Consequence_Analysis.md
│   │   ├── 021_Premortem.md
│   │   └── ...
│   ├── decision-archetypes.yaml   # Common decision traps
│   ├── coverage-scoring.yaml      # Scoring rules
│   └── exploration-template.md    # Output format
└── steps/
    ├── step-00-frame.md
    ├── step-01-map.md
    ├── step-02-illuminate.md
    ├── step-03-challenge.md
    ├── step-04-synthesize.md
    └── step-05-converge.md
```

## Key Differences from Deep Verify

| Aspect | Deep Verify | Deep Explore |
|--------|-------------|--------------|
| Purpose | Validate existing artifact | Map decision space |
| Direction | Convergent (find truth) | Divergent (find options) |
| Output | Verdict (ACCEPT/REJECT) | Map (no recommendation) |
| Scoring | Evidence of flaws | Coverage of space |
| End state | AI decides quality | User decides direction |
| Adversarial | Attack findings | Stress-test options |

## Version History

- **V1.0** - Initial release, based on Deep Verify structure
