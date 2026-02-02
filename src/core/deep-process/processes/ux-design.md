# Process: UX Design

> **ID:** ux-design
> **Version:** 1.0
> **Domain:** User Experience Design
> **Goal:** Create user-centered design through research, iteration, and testing

---

## METADATA

```yaml
id: ux-design
version: "1.0"
domain: user-experience

phases:
  - research
  - personas
  - journeys
  - wireframes
  - prototype
  - testing

integrations:
  figma:
    supported: true
    via: mcp  # If Figma MCP available
  miro:
    supported: true
    via: mcp
```

---

## ENFORCEMENT

> **WAŻNE:** Przed wykonaniem CZEGOKOLWIEK przeczytaj `engine/enforcer.md`

### Reguły specyficzne dla UX

```yaml
rules:
  - rule: "No wireframes without personas"
    check: "At least 1 persona must exist before wireframes"
    on_violation: BLOCK

  - rule: "No prototype without approved wireframes"
    check: "Wireframes must have status: approved"
    on_violation: BLOCK

  - rule: "User testing required"
    check: "At least 3 user tests before final"
    on_violation: WARN

  - rule: "Accessibility check"
    check: "WCAG compliance verified"
    on_violation: WARN
```

---

## PHASE 1: RESEARCH

### Purpose
Zrozumieć użytkowników, ich potrzeby, bóle i kontekst użycia.

### Entry Conditions
```yaml
requires:
  state:
    - "Project initialized"
  artifacts:
    - "artifacts/idea.md OR artifacts/prd.md"  # Context about product
```

### Steps

#### Step 1.1: Define Research Goals

```yaml
id: define-research-goals
name: "Define what we need to learn"

requires:
  artifacts:
    - "artifacts/idea.md"

produces:
  artifacts:
    - path: "artifacts/ux/research-plan.md"

instructions: |
  1. Review product idea/PRD
  2. Identify key unknowns about users:
     - Who are they?
     - What are their goals?
     - What frustrates them?
     - What context do they use product in?
  3. Define research questions (5-10)
  4. Choose research methods:
     - User interviews
     - Surveys
     - Competitor analysis
     - Analytics review
  5. Create research-plan.md

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.3"
```

#### Step 1.2: Conduct Research

```yaml
id: conduct-research
name: "Execute research activities"

requires:
  artifacts:
    - "artifacts/ux/research-plan.md"

produces:
  artifacts:
    - path: "artifacts/ux/research-findings.md"

instructions: |
  1. For each research method in plan:
     a. Execute (interviews, surveys, etc.)
     b. Document raw findings
  2. Synthesize findings:
     - Common themes
     - Pain points
     - Opportunities
     - Surprises
  3. Create research-findings.md

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.7"
```

#### Step 1.3: Competitor Analysis

```yaml
id: competitor-analysis
name: "Analyze competitor UX"

produces:
  artifacts:
    - path: "artifacts/ux/competitor-analysis.md"

instructions: |
  1. Identify 3-5 competitors
  2. For each competitor:
     - Screenshot key screens
     - Note UX patterns used
     - Identify strengths/weaknesses
  3. Summarize:
     - Best practices to adopt
     - Mistakes to avoid
     - Differentiation opportunities
```

### Exit Gate: research_to_personas

```yaml
gate:
  name: research_to_personas
  threshold: 0.70

  criteria:
    - name: "Research conducted"
      weight: 0.30
      check: "Research findings documented"

    - name: "User needs identified"
      weight: 0.30
      check: "At least 5 user needs/pain points documented"

    - name: "Context understood"
      weight: 0.20
      check: "Usage context documented"

    - name: "Competitors analyzed"
      weight: 0.20
      check: "At least 3 competitors analyzed"
```

---

## PHASE 2: PERSONAS

### Purpose
Stworzyć reprezentatywne persony użytkowników na podstawie research.

### Entry Conditions
```yaml
requires:
  gates:
    - "research_to_personas: passed"
  artifacts:
    - "artifacts/ux/research-findings.md"
```

### Steps

#### Step 2.1: Create Personas

```yaml
id: create-personas
name: "Define user personas"

requires:
  artifacts:
    - "artifacts/ux/research-findings.md"

produces:
  artifacts:
    - path: "artifacts/ux/personas/PERSONA-XXX.yaml"

instructions: |
  1. Cluster research findings into user types
  2. For each user type (2-4 personas):
     a. Generate ID: PERSONA-{sequence}
     b. Create persona file with:
        - Name and photo (stock)
        - Demographics
        - Goals
        - Frustrations
        - Behaviors
        - Quote (representative)
        - Scenario
  3. Identify primary persona
  4. Update state

schema: |
  # artifacts/ux/personas/PERSONA-XXX.yaml
  id: PERSONA-001
  name: "Anna Developer"
  type: primary  # primary | secondary

  demographics:
    age: 32
    occupation: "Senior Software Engineer"
    location: "Warsaw, Poland"
    tech_savviness: high

  goals:
    - "Ship quality code faster"
    - "Reduce time on repetitive tasks"
    - "Learn new technologies"

  frustrations:
    - "Too many context switches"
    - "Outdated documentation"
    - "Slow build times"

  behaviors:
    - "Uses CLI over GUI when possible"
    - "Reads docs before asking colleagues"
    - "Prefers keyboard shortcuts"

  quote: "I don't want another tool, I want fewer tools that work better together."

  scenario: |
    Anna starts her day reviewing PRs. She needs to understand
    changes quickly and provide meaningful feedback. She's
    frustrated when commits lack context or tests.

state_updates:
  - file: ".state/items.yaml"
    action: "append personas"
```

### Exit Gate: personas_to_journeys

```yaml
gate:
  name: personas_to_journeys
  threshold: 0.75

  criteria:
    - name: "Personas created"
      weight: 0.40
      check: "At least 2 personas exist"

    - name: "Primary persona identified"
      weight: 0.30
      check: "One persona marked as primary"

    - name: "Goals defined"
      weight: 0.30
      check: "Each persona has at least 3 goals"
```

---

## PHASE 3: JOURNEYS

### Purpose
Zmapować podróże użytkowników przez produkt.

### Entry Conditions
```yaml
requires:
  gates:
    - "personas_to_journeys: passed"
  artifacts:
    - "artifacts/ux/personas/*.yaml"
```

### Steps

#### Step 3.1: Map User Journeys

```yaml
id: map-journeys
name: "Create user journey maps"

requires:
  artifacts:
    - "artifacts/ux/personas/*.yaml"

produces:
  artifacts:
    - path: "artifacts/ux/journeys/JOURNEY-XXX.md"

instructions: |
  1. For primary persona, map main journeys:
     - Identify key scenarios (3-5)
     - For each scenario:
       a. Define stages (Awareness → Consideration → Use → Retention)
       b. Map touchpoints
       c. Identify emotions at each stage
       d. Note pain points and opportunities
  2. Create journey map document
  3. Optionally: Create visual in Miro/Figma

schema: |
  # artifacts/ux/journeys/JOURNEY-XXX.md

  # Journey: First Time Setup

  **Persona:** Anna Developer (PERSONA-001)
  **Scenario:** Setting up the tool for the first time

  ## Stages

  ### 1. Awareness
  - **Touchpoint:** Landing page
  - **Action:** Reads about features
  - **Emotion:** 😐 Curious but skeptical
  - **Pain point:** Too much marketing speak
  - **Opportunity:** Show real examples

  ### 2. Installation
  - **Touchpoint:** CLI / Package manager
  - **Action:** Runs install command
  - **Emotion:** 😊 Satisfied (if quick)
  - **Pain point:** Dependency issues
  - **Opportunity:** One-liner install

  [... more stages ...]

  ## Key Insights
  - First 5 minutes are critical
  - Error messages must be actionable
```

### Exit Gate: journeys_to_wireframes

```yaml
gate:
  name: journeys_to_wireframes
  threshold: 0.70

  criteria:
    - name: "Journeys mapped"
      weight: 0.40
      check: "At least 3 journeys documented"

    - name: "Pain points identified"
      weight: 0.30
      check: "Pain points noted at each stage"

    - name: "Opportunities noted"
      weight: 0.30
      check: "Improvement opportunities identified"
```

---

## PHASE 4: WIREFRAMES

### Purpose
Stworzyć szkice interfejsu rozwiązujące problemy z journey maps.

### Entry Conditions
```yaml
requires:
  gates:
    - "journeys_to_wireframes: passed"
  artifacts:
    - "artifacts/ux/journeys/*.md"
```

### Steps

#### Step 4.1: Create Wireframes

```yaml
id: create-wireframes
name: "Design low-fidelity wireframes"

requires:
  artifacts:
    - "artifacts/ux/journeys/*.md"

produces:
  artifacts:
    - path: "artifacts/ux/wireframes/WIREFRAME-XXX.md"
    - path: "artifacts/ux/wireframes/*.png"  # If using tool

instructions: |
  1. For each key screen in journeys:
     a. Sketch layout (paper or digital)
     b. Focus on:
        - Information hierarchy
        - User flow
        - Key interactions
     c. Do NOT focus on:
        - Colors
        - Exact fonts
        - Visual polish
  2. Document each wireframe:
     - Screen name
     - Purpose
     - Key elements
     - User actions
     - Notes/questions
  3. Get stakeholder feedback
  4. Iterate based on feedback

schema: |
  # artifacts/ux/wireframes/WIREFRAME-XXX.md

  # Wireframe: Dashboard

  **ID:** WIREFRAME-001
  **Journey:** First Time Setup
  **Stage:** Post-onboarding

  ## Purpose
  Show user their project status at a glance.

  ## Layout
  ```
  ┌─────────────────────────────────────────┐
  │  [Logo]           [User] [Settings]     │
  ├─────────────────────────────────────────┤
  │  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
  │  │ Active  │  │ Pending │  │ Done    │ │
  │  │   12    │  │    5    │  │   47    │ │
  │  └─────────┘  └─────────┘  └─────────┘ │
  ├─────────────────────────────────────────┤
  │  Recent Activity                        │
  │  ┌─────────────────────────────────┐   │
  │  │ • Task completed: Auth module   │   │
  │  │ • New comment on PR #42         │   │
  │  └─────────────────────────────────┘   │
  └─────────────────────────────────────────┘
  ```

  ## Key Elements
  1. Status cards - quick overview
  2. Activity feed - recent updates
  3. Quick actions - primary CTA

  ## User Actions
  - Click card → filter by status
  - Click activity → go to item

  ## Questions
  - Should we show notifications here?
  - How many activity items to show?

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: based on wireframes completed"
```

#### Step 4.2: Review Wireframes

```yaml
id: review-wireframes
name: "Get feedback and iterate"

requires:
  artifacts:
    - "artifacts/ux/wireframes/*.md"

produces:
  state:
    - "wireframe.status: approved | needs_revision"

instructions: |
  1. Present wireframes to stakeholders
  2. Collect feedback on:
     - Flow clarity
     - Missing elements
     - Priority of information
  3. Update wireframes based on feedback
  4. Mark as approved when ready
```

### Exit Gate: wireframes_to_prototype

```yaml
gate:
  name: wireframes_to_prototype
  threshold: 0.75

  criteria:
    - name: "Key screens wireframed"
      weight: 0.40
      check: "All journey touchpoints have wireframes"

    - name: "Feedback incorporated"
      weight: 0.30
      check: "Stakeholder feedback addressed"

    - name: "Wireframes approved"
      weight: 0.30
      check: "Key wireframes marked approved"
```

---

## PHASE 5: PROTOTYPE

### Purpose
Stworzyć interaktywny prototyp do testowania.

### Entry Conditions
```yaml
requires:
  gates:
    - "wireframes_to_prototype: passed"
  artifacts:
    - "artifacts/ux/wireframes/*.md (approved)"
```

### Steps

#### Step 5.1: Create Prototype

```yaml
id: create-prototype
name: "Build interactive prototype"

requires:
  artifacts:
    - "artifacts/ux/wireframes/*.md"

produces:
  artifacts:
    - path: "artifacts/ux/prototype/README.md"
    - external: "Figma/Sketch/Adobe XD link"

instructions: |
  1. Choose prototyping tool:
     - Figma (recommended)
     - Sketch + InVision
     - Adobe XD
     - HTML/CSS (for complex interactions)
  2. Build screens from wireframes:
     - Add visual design (colors, fonts)
     - Add interactions (clicks, transitions)
     - Create realistic content
  3. Link screens into flows
  4. Document prototype:
     - Tool used
     - Link to prototype
     - Flows covered
     - Known limitations

prototype_doc: |
  # Prototype: {Project Name}

  **Tool:** Figma
  **Link:** https://figma.com/file/...
  **Last Updated:** 2026-02-01

  ## Flows Covered
  1. Onboarding (JOURNEY-001)
  2. Daily workflow (JOURNEY-002)
  3. Settings configuration (JOURNEY-003)

  ## How to Use
  1. Open Figma link
  2. Click "Present" (play button)
  3. Follow blue hotspots

  ## Known Limitations
  - Search is not interactive
  - Only happy path implemented
```

### Exit Gate: prototype_to_testing

```yaml
gate:
  name: prototype_to_testing
  threshold: 0.70

  criteria:
    - name: "Prototype exists"
      weight: 0.40
      check: "Interactive prototype link documented"

    - name: "Key flows work"
      weight: 0.40
      check: "All journey flows navigable"

    - name: "Visual design applied"
      weight: 0.20
      check: "Not wireframe-level, has visual polish"
```

---

## PHASE 6: TESTING

### Purpose
Przetestować prototyp z prawdziwymi użytkownikami.

### Entry Conditions
```yaml
requires:
  gates:
    - "prototype_to_testing: passed"
  artifacts:
    - "artifacts/ux/prototype/README.md"
```

### Steps

#### Step 6.1: Plan User Tests

```yaml
id: plan-user-tests
name: "Create testing plan"

produces:
  artifacts:
    - path: "artifacts/ux/testing/test-plan.md"

instructions: |
  1. Define test objectives:
     - What do we want to learn?
     - What decisions depend on this?
  2. Create test tasks (5-8):
     - "Find the settings page"
     - "Complete the onboarding"
  3. Define success metrics:
     - Task completion rate
     - Time to complete
     - Error rate
     - Satisfaction score
  4. Recruit participants (5-8 people)
     - Match primary persona
  5. Document in test-plan.md
```

#### Step 6.2: Conduct User Tests

```yaml
id: conduct-user-tests
name: "Run usability tests"

requires:
  artifacts:
    - "artifacts/ux/testing/test-plan.md"

produces:
  artifacts:
    - path: "artifacts/ux/testing/sessions/SESSION-XXX.md"

instructions: |
  1. For each participant:
     a. Introduction (explain process, get consent)
     b. Background questions
     c. Task scenarios
     d. Think-aloud protocol
     e. Post-test questions (SUS, NPS)
     f. Thank and compensate
  2. Document each session:
     - Participant info
     - Task completion (yes/no/partial)
     - Time per task
     - Observations
     - Quotes
     - Issues found
```

#### Step 6.3: Analyze and Report

```yaml
id: analyze-tests
name: "Synthesize test results"

requires:
  artifacts:
    - "artifacts/ux/testing/sessions/*.md"

produces:
  artifacts:
    - path: "artifacts/ux/testing/report.md"

instructions: |
  1. Aggregate data:
     - Task success rates
     - Average times
     - SUS/NPS scores
  2. Identify issues:
     - Critical (blocked task)
     - Major (significant struggle)
     - Minor (confusion, not blocking)
  3. Prioritize fixes:
     - Impact × Frequency
  4. Recommend next steps:
     - Fixes needed
     - Another round of testing?
     - Ready for development?
  5. Create report.md

report_template: |
  # Usability Test Report

  **Date:** 2026-02-01
  **Participants:** 6
  **Prototype:** v1.2

  ## Summary
  - Overall SUS Score: 72 (Good)
  - Task Success Rate: 85%
  - Key Issue: Onboarding flow confusing

  ## Task Results
  | Task | Success | Avg Time | Issues |
  |------|---------|----------|--------|
  | Complete onboarding | 67% | 4m 30s | 3 |
  | Find settings | 100% | 15s | 0 |
  | Create project | 83% | 2m | 1 |

  ## Critical Issues
  1. **Step 3 of onboarding unclear**
     - 4/6 users confused
     - Recommendation: Add helper text

  ## Recommendations
  1. Fix onboarding step 3
  2. Add progress indicator
  3. Test again with 3 users
```

### Exit Gate: testing_complete

```yaml
gate:
  name: testing_complete
  threshold: 0.80

  criteria:
    - name: "Tests conducted"
      weight: 0.30
      check: "At least 5 user tests completed"

    - name: "Issues documented"
      weight: 0.25
      check: "All issues logged with severity"

    - name: "Success rate acceptable"
      weight: 0.25
      check: "Task success rate >= 80%"

    - name: "Report complete"
      weight: 0.20
      check: "Test report with recommendations exists"
```

---

## ARTIFACTS SUMMARY

| Artifact | Phase | Purpose |
|----------|-------|---------|
| research-plan.md | Research | What to learn |
| research-findings.md | Research | What we learned |
| competitor-analysis.md | Research | Competition review |
| personas/PERSONA-XXX.yaml | Personas | User representations |
| journeys/JOURNEY-XXX.md | Journeys | User flow maps |
| wireframes/WIREFRAME-XXX.md | Wireframes | Screen sketches |
| prototype/README.md | Prototype | Interactive demo |
| testing/test-plan.md | Testing | Test setup |
| testing/sessions/SESSION-XXX.md | Testing | Individual tests |
| testing/report.md | Testing | Final analysis |

---

## STATE TRANSITIONS

```
┌──────────┐     0.70      ┌──────────┐     0.75      ┌──────────┐
│ RESEARCH │──────────────▶│ PERSONAS │──────────────▶│ JOURNEYS │
└──────────┘               └──────────┘               └──────────┘
                                                            │
                                                        0.70│
                                                            ▼
┌──────────┐     0.80      ┌───────────┐    0.70     ┌───────────┐
│ TESTING  │◀──────────────│ PROTOTYPE │◀────────────│ WIREFRAMES│
└──────────┘               └───────────┘             └───────────┘
     │
     │ 0.80
     ▼
┌──────────┐
│   DONE   │
└──────────┘
```

---

## QUICK REFERENCE

| User says | Action |
|-----------|--------|
| "Start UX process" | Enter Research phase |
| "Create personas" | Execute create-personas step |
| "Map user journey" | Execute map-journeys step |
| "Create wireframe for X" | Execute create-wireframes step |
| "Build prototype" | Execute create-prototype step |
| "Run user test" | Execute conduct-user-tests step |
