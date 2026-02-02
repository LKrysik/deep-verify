# Process: Project Management

> **ID:** project-management
> **Version:** 1.0
> **Domain:** Software Development Project Management
> **Goal:** Transform idea into working, tested software through structured phases

---

## METADATA

```yaml
id: project-management
version: "1.0"
domain: software-development

phases:
  - ideation
  - specification
  - architecture
  - planning
  - execution
  - verification

integrations:
  azure_devops:
    supported: true
    work_item_mapping:
      epic: Feature
      story: "User Story"
      task: Task
      sprint: Iteration
  github:
    supported: true
    mapping:
      epic: Milestone
      story: Issue
      sprint: Project
```

---

## ENFORCEMENT

> **WAŻNE:** Przed wykonaniem CZEGOKOLWIEK przeczytaj `engine/enforcer.md`

### Reguły specyficzne dla tego procesu

```yaml
rules:
  - rule: "No story without epic"
    check: "story.epic_id must exist in epics"
    on_violation: BLOCK

  - rule: "No sprint without stories"
    check: "sprint.stories.length > 0"
    on_violation: BLOCK

  - rule: "Sprint capacity required"
    check: "sprint.capacity must be set before adding stories"
    on_violation: BLOCK

  - rule: "Story points required for sprint"
    check: "All stories in sprint must have points"
    on_violation: WARN

  - rule: "Blocked stories cannot be in active sprint"
    check: "story.status != blocked for all sprint.stories"
    on_violation: BLOCK
```

---

## PHASE 1: IDEATION

### Purpose
Skrystalizować surowy pomysł w jasny problem statement z zdefiniowanym użytkownikiem i kryteriami sukcesu.

### Entry Conditions
```yaml
requires:
  state:
    - "Project initialized (.state/process.yaml exists)"
```

### Steps

#### Step 1.1: Capture Idea

```yaml
id: capture-idea
name: "Capture and crystallize idea"
operation: deep-challenge  # lub manual

requires:
  input:
    - "User's raw idea or problem description"

produces:
  artifacts:
    - path: "artifacts/idea.md"
      type: document
      schema: schemas/idea.schema.yaml

instructions: |
  1. Collect user's raw idea
  2. Ask probing questions:
     - What problem does this solve?
     - Who experiences this problem?
     - What does success look like?
     - What is NOT in scope?
  3. Create artifacts/idea.md with:
     - Problem statement (one sentence)
     - Target user (specific persona)
     - Success criteria (measurable)
     - Scope boundaries (in/out)
  4. Update state

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "current_artifacts: append 'artifacts/idea.md'"
      - "phase_progress: 0.5"
      - "last_action: 'capture-idea'"
```

#### Step 1.2: Identify Unknowns

```yaml
id: identify-unknowns
name: "Identify what we don't know"

requires:
  artifacts:
    - "artifacts/idea.md"

produces:
  state:
    - "unknowns in .state/unknowns.yaml"

instructions: |
  1. Review idea.md
  2. Ask:
     - What are we assuming without evidence?
     - What could surprise us?
     - What expertise might we be missing?
  3. For each unknown:
     - Add to .state/unknowns.yaml
     - Classify: technical | user | market | feasibility
     - Set priority: high | medium | low

state_updates:
  - file: ".state/unknowns.yaml"
    action: "append discovered unknowns"
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.8"
```

### Exit Gate: idea_to_spec

```yaml
gate:
  name: idea_to_spec
  threshold: 0.70

  criteria:
    - name: "Problem clarity"
      weight: 0.25
      check: "Problem statement is one clear sentence"
      evidence: "artifacts/idea.md section: Problem Statement"

    - name: "User defined"
      weight: 0.20
      check: "Target user is specific (not 'everyone')"
      evidence: "artifacts/idea.md section: Target User"

    - name: "Success criteria"
      weight: 0.20
      check: "At least 2 measurable criteria exist"
      evidence: "artifacts/idea.md section: Success Criteria"

    - name: "Scope bounded"
      weight: 0.20
      check: "IN and OUT scope lists exist"
      evidence: "artifacts/idea.md section: Scope"

    - name: "Unknowns identified"
      weight: 0.15
      check: "Critical unknowns are listed"
      evidence: ".state/unknowns.yaml has entries"

  on_pass:
    - "Advance to specification phase"
    - "Update .state/phase.yaml"

  on_fail:
    - "List gaps"
    - "Recommend: Re-run capture-idea with focus on gaps"
```

---

## PHASE 2: SPECIFICATION

### Purpose
Zdefiniować kompletne wymagania funkcjonalne i niefunkcjonalne.

### Entry Conditions
```yaml
requires:
  gates:
    - "idea_to_spec: passed"
  artifacts:
    - "artifacts/idea.md"
```

### Steps

#### Step 2.1: Create PRD

```yaml
id: create-prd
name: "Create Product Requirements Document"
operation: deep-requirements  # lub manual

requires:
  artifacts:
    - "artifacts/idea.md"

produces:
  artifacts:
    - path: "artifacts/prd.md"
      type: document

instructions: |
  1. Read artifacts/idea.md
  2. Define functional requirements (FR-XXX):
     - Each requirement testable
     - Each has acceptance criteria
  3. Define non-functional requirements (NFR-XXX):
     - Performance
     - Security
     - Scalability
     - Usability
  4. Prioritize requirements (MoSCoW)
  5. Create artifacts/prd.md

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "current_artifacts: append 'artifacts/prd.md'"
      - "phase_progress: 0.7"
```

#### Step 2.2: Validate Requirements

```yaml
id: validate-requirements
name: "Check for conflicts and completeness"

requires:
  artifacts:
    - "artifacts/prd.md"

produces:
  state:
    - "validation result"
    - "discovered unknowns (if any)"

instructions: |
  1. Check for conflicting requirements
  2. Check NFR coverage (all categories)
  3. Check all FRs have acceptance criteria
  4. Identify any new unknowns
  5. Update state

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: spec_to_arch

```yaml
gate:
  name: spec_to_arch
  threshold: 0.85

  criteria:
    - name: "Requirements complete"
      weight: 0.25
      check: "All FRs have acceptance criteria"

    - name: "NFRs defined"
      weight: 0.20
      check: "Performance, security, scalability addressed"

    - name: "No conflicts"
      weight: 0.20
      check: "No conflicting requirements"

    - name: "Priorities set"
      weight: 0.15
      check: "MoSCoW prioritization done"

    - name: "Dependencies identified"
      weight: 0.10
      check: "External dependencies listed"

    - name: "Risks documented"
      weight: 0.10
      check: "Major risks identified"
```

---

## PHASE 3: ARCHITECTURE

### Purpose
Zaprojektować system który spełni wymagania.

### Entry Conditions
```yaml
requires:
  gates:
    - "spec_to_arch: passed"
  artifacts:
    - "artifacts/prd.md"
```

### Steps

#### Step 3.1: Design Architecture

```yaml
id: design-architecture
name: "Create system architecture"
operation: deep-architecture  # lub manual

requires:
  artifacts:
    - "artifacts/prd.md"

produces:
  artifacts:
    - path: "artifacts/architecture.md"
      type: document

instructions: |
  1. Read PRD
  2. Design:
     - High-level components
     - Data model
     - API contracts
     - Integration points
  3. Create artifacts/architecture.md
  4. Identify architectural decisions needed

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "current_artifacts: append 'artifacts/architecture.md'"
      - "phase_progress: 0.5"
```

#### Step 3.2: Make Architectural Decisions

```yaml
id: architectural-decisions
name: "Document and decide on ADRs"

requires:
  artifacts:
    - "artifacts/architecture.md"

produces:
  artifacts:
    - "artifacts/decisions/ADR-XXX.yaml"
  state:
    - "decisions in .state/decisions.yaml"

instructions: |
  1. For each decision needed:
     a. Create ADR file with options
     b. Analyze trade-offs
     c. Get user decision (or recommend)
     d. Update .state/decisions.yaml
  2. All blocking decisions must be resolved

state_updates:
  - file: ".state/decisions.yaml"
    action: "append new decisions"
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: based on decisions resolved"
```

### Exit Gate: arch_to_planning

```yaml
gate:
  name: arch_to_planning
  threshold: 0.80

  criteria:
    - name: "Requirements covered"
      weight: 0.25
      check: "All requirements have architectural home"

    - name: "Decisions resolved"
      weight: 0.25
      check: "No blocking decisions pending"

    - name: "Interfaces defined"
      weight: 0.20
      check: "Component interfaces documented"

    - name: "Data model complete"
      weight: 0.15
      check: "Entities and relationships defined"

    - name: "Deployment defined"
      weight: 0.15
      check: "Deployment strategy documented"
```

---

## PHASE 4: PLANNING

### Purpose
Podzielić pracę na epics, stories i zaplanować sprint.

### Entry Conditions
```yaml
requires:
  gates:
    - "arch_to_planning: passed"
  artifacts:
    - "artifacts/prd.md"
    - "artifacts/architecture.md"
```

### Steps

#### Step 4.1: Create Epics

```yaml
id: create-epics
name: "Define epics from requirements"

requires:
  artifacts:
    - "artifacts/prd.md"
    - "artifacts/architecture.md"

produces:
  artifacts:
    - "artifacts/epics/EPIC-XXX.yaml"
  state:
    - "epics in .state/items.yaml"

instructions: |
  1. Group related requirements into epics
  2. For each epic:
     a. Generate ID: EPIC-{sequence}
     b. Create artifacts/epics/EPIC-XXX.yaml:
        - title
        - description
        - requirements covered
        - acceptance criteria
     c. Add to .state/items.yaml
  3. If Azure DevOps enabled:
     - Create Feature work item
     - Store azure_devops_id

schema: |
  # artifacts/epics/EPIC-XXX.yaml
  id: EPIC-001
  title: "User Authentication"
  description: "Complete authentication system"
  requirements: [FR-001, FR-002, FR-003]
  acceptance_criteria:
    - "Users can register"
    - "Users can login"
    - "Password reset works"
  status: defined
  created_at: 2026-02-01T10:00:00Z

state_updates:
  - file: ".state/items.yaml"
    action: "append epics"
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.3"

integration:
  azure_devops: |
    az boards work-item create \
      --type "Feature" \
      --title "{epic.title}" \
      --description "{epic.description}"
```

#### Step 4.2: Create Stories

```yaml
id: create-stories
name: "Break epics into stories"

requires:
  state:
    - "At least 1 epic exists"

produces:
  artifacts:
    - "artifacts/stories/STORY-XXX.yaml"
  state:
    - "stories in .state/items.yaml"

instructions: |
  1. For each epic:
     a. Break into user stories (INVEST criteria)
     b. For each story:
        - Generate ID: STORY-{sequence}
        - Create artifacts/stories/STORY-XXX.yaml
        - Estimate points (Fibonacci: 1,2,3,5,8,13)
        - Add to .state/items.yaml
        - Link to epic
  2. If Azure DevOps enabled:
     - Create User Story work item
     - Set parent to epic

schema: |
  # artifacts/stories/STORY-XXX.yaml
  id: STORY-001
  epic_id: EPIC-001
  title: "User can register with email"
  description: "As a new user, I want to register with email and password"
  acceptance_criteria:
    - criterion: "Valid email required"
      testable: true
    - criterion: "Password min 8 chars"
      testable: true
    - criterion: "Confirmation email sent"
      testable: true
  points: 3
  priority: must_have
  status: draft
  created_at: 2026-02-01T10:30:00Z

state_updates:
  - file: ".state/items.yaml"
    updates:
      - "stories: append new story"
      - "epics[epic_id].stories: append story_id"
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.6"
```

#### Step 4.3: Plan Sprint

```yaml
id: plan-sprint
name: "Create and populate sprint"

requires:
  state:
    - "Stories exist with points"
    - "No critical blocking decisions"

produces:
  artifacts:
    - "artifacts/sprints/SPRINT-XXX.yaml"
  state:
    - "sprint in .state/items.yaml"

instructions: |
  1. Ask user for sprint parameters:
     - Duration (default: 2 weeks)
     - Capacity (story points)
     - Sprint goal
  2. Create sprint:
     - Generate ID: SPRINT-{sequence}
     - Set start_date, end_date
  3. Add stories to sprint:
     - Prioritize by MoSCoW + dependencies
     - Stop when capacity reached
     - Mark remaining as backlog
  4. Verify: no blocked stories in sprint
  5. Create artifacts/sprints/SPRINT-XXX.yaml

schema: |
  # artifacts/sprints/SPRINT-XXX.yaml
  id: SPRINT-001
  name: "Sprint 1 - Foundation"
  goal: "Basic authentication working"
  start_date: 2026-02-03
  end_date: 2026-02-14
  capacity: 20
  committed_points: 18
  stories:
    - id: STORY-001
      points: 3
    - id: STORY-002
      points: 5
    - id: STORY-003
      points: 5
    - id: STORY-004
      points: 5
  status: planned
  created_at: 2026-02-01T11:00:00Z

state_updates:
  - file: ".state/items.yaml"
    updates:
      - "sprints: append new sprint"
      - "stories[id].sprint_id: set for each story in sprint"
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 1.0"
```

### Exit Gate: planning_to_execution

```yaml
gate:
  name: planning_to_execution
  threshold: 0.80

  criteria:
    - name: "Epics defined"
      weight: 0.20
      check: "At least 1 epic exists"

    - name: "Stories defined"
      weight: 0.25
      check: "All epics have at least 1 story"

    - name: "Stories estimated"
      weight: 0.15
      check: "All stories have points"

    - name: "Sprint planned"
      weight: 0.25
      check: "Active sprint exists with stories"

    - name: "No blockers"
      weight: 0.15
      check: "No blocking decisions for sprint stories"
```

---

## PHASE 5: EXECUTION

### Purpose
Implementować stories w sprincie.

### Entry Conditions
```yaml
requires:
  gates:
    - "planning_to_execution: passed"
  state:
    - "Sprint with status: planned or active"
```

### Steps

#### Step 5.1: Start Sprint

```yaml
id: start-sprint
name: "Activate sprint"

requires:
  state:
    - "Sprint exists with status: planned"

produces:
  state:
    - "Sprint status: active"

instructions: |
  1. Update sprint status to 'active'
  2. Update sprint start_date to now (if not set)
  3. Set all sprint stories to 'ready'

state_updates:
  - file: ".state/items.yaml"
    updates:
      - "sprints[id].status: 'active'"
      - "stories[sprint_stories].status: 'ready'"
```

#### Step 5.2: Develop Story

```yaml
id: develop-story
name: "Implement a story"
operation: deep-develop  # lub manual

requires:
  state:
    - "Story with status: ready"
    - "Sprint is active"

produces:
  artifacts:
    - "src/** (code)"
    - "tests/** (tests)"
  state:
    - "Story status: in_progress → done"

instructions: |
  1. Select next story (by priority in sprint)
  2. Update story status: in_progress
  3. Implement:
     - Write code
     - Write tests
     - Ensure acceptance criteria met
  4. Update story status: done
  5. Update sprint progress

state_updates:
  - file: ".state/items.yaml"
    updates:
      - "stories[id].status: 'done'"
      - "stories[id].completed_at: now"
```

#### Step 5.3: Review Story

```yaml
id: review-story
name: "Code review"

requires:
  state:
    - "Story with status: done (code complete)"

produces:
  state:
    - "Story status: reviewed"

instructions: |
  1. Review code for:
     - Correctness
     - Code quality
     - Test coverage
     - Security
  2. If issues found:
     - Document issues
     - Set story back to in_progress
  3. If approved:
     - Set story status: reviewed
```

### Exit Gate: execution_to_verification

```yaml
gate:
  name: execution_to_verification
  threshold: 0.90

  criteria:
    - name: "Sprint stories done"
      weight: 0.40
      check: "All sprint stories have status: done or reviewed"

    - name: "Tests pass"
      weight: 0.30
      check: "All tests passing"

    - name: "No critical bugs"
      weight: 0.20
      check: "No known critical bugs"

    - name: "Code reviewed"
      weight: 0.10
      check: "All stories reviewed"
```

---

## PHASE 6: VERIFICATION

### Purpose
Zweryfikować że sprint goal osiągnięty i jakość wystarczająca.

### Entry Conditions
```yaml
requires:
  gates:
    - "execution_to_verification: passed"
```

### Steps

#### Step 6.1: Verify Acceptance Criteria

```yaml
id: verify-acceptance
name: "Check all acceptance criteria"

requires:
  state:
    - "All sprint stories done"

produces:
  state:
    - "Verification results"

instructions: |
  1. For each story in sprint:
     a. For each acceptance criterion:
        - Verify it's met
        - Document evidence
     b. Mark story: verified or failed
  2. Calculate verification score
```

#### Step 6.2: Sprint Retrospective

```yaml
id: sprint-retro
name: "Conduct sprint retrospective"

produces:
  artifacts:
    - "artifacts/retros/SPRINT-XXX-retro.md"

instructions: |
  1. Document:
     - What went well
     - What could improve
     - Action items for next sprint
  2. Save to artifacts/retros/
  3. Update sprint status: completed
```

### Exit Gate: sprint_complete

```yaml
gate:
  name: sprint_complete
  threshold: 0.85

  criteria:
    - name: "Acceptance criteria met"
      weight: 0.40
      check: "All stories verified"

    - name: "Sprint goal achieved"
      weight: 0.30
      check: "Sprint goal is met"

    - name: "Quality sufficient"
      weight: 0.20
      check: "Test coverage >= 80%"

    - name: "Retro completed"
      weight: 0.10
      check: "Retrospective document exists"
```

---

## ARTIFACTS SUMMARY

| Artifact | Phase | Schema |
|----------|-------|--------|
| artifacts/idea.md | Ideation | schemas/idea.schema.yaml |
| artifacts/prd.md | Specification | schemas/prd.schema.yaml |
| artifacts/architecture.md | Architecture | schemas/architecture.schema.yaml |
| artifacts/decisions/ADR-XXX.yaml | Architecture | schemas/adr.schema.yaml |
| artifacts/epics/EPIC-XXX.yaml | Planning | schemas/epic.schema.yaml |
| artifacts/stories/STORY-XXX.yaml | Planning | schemas/story.schema.yaml |
| artifacts/sprints/SPRINT-XXX.yaml | Planning | schemas/sprint.schema.yaml |
| artifacts/retros/SPRINT-XXX-retro.md | Verification | - |

---

## INTEGRATIONS

### Azure DevOps

```yaml
azure_devops:
  when_enabled: true

  on_epic_create: |
    az boards work-item create \
      --org "https://dev.azure.com/{org}" \
      --project "{project}" \
      --type "Feature" \
      --title "{epic.title}" \
      --description "{epic.description}"
    # Store returned ID in epic.azure_devops_id

  on_story_create: |
    az boards work-item create \
      --type "User Story" \
      --title "{story.title}" \
      --description "{story.description}" \
      --parent "{epic.azure_devops_id}"
    # Store returned ID in story.azure_devops_id

  on_sprint_create: |
    # Sprints map to Iterations in Azure DevOps
    # Usually pre-configured, just assign stories

  on_story_status_change: |
    az boards work-item update \
      --id "{story.azure_devops_id}" \
      --state "{mapped_state}"
```

### GitHub

```yaml
github:
  when_enabled: true

  on_epic_create: |
    gh api repos/{owner}/{repo}/milestones \
      -f title="{epic.title}" \
      -f description="{epic.description}"

  on_story_create: |
    gh issue create \
      --title "{story.title}" \
      --body "{story.description}" \
      --milestone "{epic.github_milestone}"
```

---

## STATE TRANSITIONS

```
┌──────────┐     gate      ┌──────────────┐     gate      ┌──────────────┐
│ IDEATION │──────0.70────▶│ SPECIFICATION│──────0.85────▶│ ARCHITECTURE │
└──────────┘               └──────────────┘               └──────────────┘
                                                                  │
                                                              gate 0.80
                                                                  │
┌──────────────┐    gate     ┌───────────┐     gate      ┌───────▼──────┐
│ VERIFICATION │◀───0.90─────│ EXECUTION │◀─────0.80─────│   PLANNING   │
└──────────────┘             └───────────┘               └──────────────┘
        │
    gate 0.85
        │
        ▼
   ┌─────────┐
   │  DONE   │ (or next sprint)
   └─────────┘
```

---

## QUICK REFERENCE

### Common Commands

| User says | Action |
|-----------|--------|
| "Start new project" | Initialize, enter Ideation |
| "Define requirements" | Execute PRD step |
| "Create epics" | Execute create-epics step |
| "Plan sprint" | Execute plan-sprint step |
| "Start sprint" | Activate sprint |
| "Work on next story" | develop-story step |
| "Check gate" | Verify current gate |
| "Show status" | Display dashboard |

### Status Flow (Story)

```
draft → ready → in_progress → done → reviewed → verified
                     ↑______________|  (if issues found)
```

### Status Flow (Sprint)

```
planned → active → completed
```
