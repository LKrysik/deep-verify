# Process: Code Documentation

> **ID:** code-documentation
> **Version:** 1.0
> **Domain:** Technical Documentation
> **Goal:** Create comprehensive, maintainable documentation for codebases

---

## METADATA

```yaml
id: code-documentation
version: "1.0"
domain: technical-documentation

phases:
  - scan
  - analyze
  - document
  - review
  - publish

integrations:
  github:
    supported: true
    pages: true  # GitHub Pages publishing
  mkdocs:
    supported: true
  docusaurus:
    supported: true
```

---

## ENFORCEMENT

> **WAŻNE:** Przed wykonaniem CZEGOKOLWIEK przeczytaj `engine/enforcer.md`

### Reguły specyficzne dla dokumentacji

```yaml
rules:
  - rule: "No documentation without analysis"
    check: "codebase-map.yaml must exist before documenting"
    on_violation: BLOCK

  - rule: "API docs require examples"
    check: "Each API endpoint must have at least 1 example"
    on_violation: WARN

  - rule: "No orphan docs"
    check: "All docs must be linked in index"
    on_violation: WARN

  - rule: "Review before publish"
    check: "All docs must have status: reviewed before publishing"
    on_violation: BLOCK
```

---

## PHASE 1: SCAN

### Purpose
Przeskanować codebase i stworzyć mapę struktury.

### Entry Conditions
```yaml
requires:
  state:
    - "Project initialized"
  access:
    - "Read access to source code"
```

### Steps

#### Step 1.1: Identify Codebase Structure

```yaml
id: scan-structure
name: "Map codebase structure"

produces:
  artifacts:
    - path: "artifacts/docs/codebase-map.yaml"

instructions: |
  1. Scan directory structure:
     ```bash
     find . -type f -name "*.ts" -o -name "*.js" -o -name "*.py" | head -100
     ```
  2. Identify:
     - Main directories (src, lib, tests, etc.)
     - Entry points (main.*, index.*, app.*)
     - Config files
     - Existing docs
  3. Create codebase-map.yaml

schema: |
  # artifacts/docs/codebase-map.yaml

  project:
    name: "MyProject"
    language: typescript
    framework: express
    scanned_at: 2026-02-01T10:00:00Z

  structure:
    directories:
      - path: src/
        purpose: "Main source code"
        modules: 12
        files: 48

      - path: src/api/
        purpose: "REST API endpoints"
        modules: 5
        files: 15

      - path: src/services/
        purpose: "Business logic"
        modules: 7
        files: 21

      - path: tests/
        purpose: "Test files"
        files: 32

    entry_points:
      - path: src/index.ts
        type: main

    config_files:
      - package.json
      - tsconfig.json
      - .env.example

    existing_docs:
      - README.md
      - docs/  # if exists

  stats:
    total_files: 156
    total_lines: 12500
    languages:
      - typescript: 80%
      - javascript: 15%
      - json: 5%

state_updates:
  - file: ".state/phase.yaml"
    updates:
      - "phase_progress: 0.5"
```

#### Step 1.2: Identify Documentation Targets

```yaml
id: identify-targets
name: "List what needs documenting"

requires:
  artifacts:
    - "artifacts/docs/codebase-map.yaml"

produces:
  artifacts:
    - path: "artifacts/docs/doc-targets.yaml"

instructions: |
  1. Based on codebase-map, identify:
     - Public APIs (need API docs)
     - Core modules (need architecture docs)
     - Complex functions (need inline docs)
     - Config options (need config reference)
     - Setup process (need getting started)
  2. Prioritize by:
     - User-facing vs internal
     - Complexity
     - Frequency of questions
  3. Create doc-targets.yaml

schema: |
  # artifacts/docs/doc-targets.yaml

  targets:
    high_priority:
      - type: api
        path: src/api/
        description: "REST API endpoints"
        estimated_pages: 10

      - type: getting_started
        description: "Installation and setup"
        estimated_pages: 2

    medium_priority:
      - type: architecture
        path: src/
        description: "System architecture overview"
        estimated_pages: 3

      - type: config
        description: "Configuration reference"
        estimated_pages: 2

    low_priority:
      - type: internal
        path: src/utils/
        description: "Internal utilities"
        estimated_pages: 5
```

### Exit Gate: scan_to_analyze

```yaml
gate:
  name: scan_to_analyze
  threshold: 0.70

  criteria:
    - name: "Codebase mapped"
      weight: 0.40
      check: "codebase-map.yaml exists and complete"

    - name: "Targets identified"
      weight: 0.30
      check: "doc-targets.yaml lists at least 3 targets"

    - name: "Priorities set"
      weight: 0.30
      check: "Targets have priority levels"
```

---

## PHASE 2: ANALYZE

### Purpose
Głęboko zanalizować moduły przed dokumentowaniem.

### Entry Conditions
```yaml
requires:
  gates:
    - "scan_to_analyze: passed"
  artifacts:
    - "artifacts/docs/codebase-map.yaml"
    - "artifacts/docs/doc-targets.yaml"
```

### Steps

#### Step 2.1: Analyze API Endpoints

```yaml
id: analyze-api
name: "Extract API structure"

requires:
  artifacts:
    - "artifacts/docs/doc-targets.yaml"

produces:
  artifacts:
    - path: "artifacts/docs/api/API-XXX.yaml"

instructions: |
  1. For each API file:
     a. Extract endpoints (GET, POST, etc.)
     b. Extract request parameters
     c. Extract response format
     d. Extract error codes
     e. Find existing examples in tests
  2. Create API definition file

schema: |
  # artifacts/docs/api/API-001.yaml

  id: API-001
  name: "Users API"
  base_path: /api/v1/users
  source_file: src/api/users.ts

  endpoints:
    - method: GET
      path: /
      summary: "List all users"
      parameters:
        - name: limit
          in: query
          type: integer
          default: 20
        - name: offset
          in: query
          type: integer
          default: 0
      response:
        200:
          description: "List of users"
          schema: User[]
        401:
          description: "Unauthorized"

    - method: POST
      path: /
      summary: "Create new user"
      body:
        required: true
        schema:
          email: string (required)
          name: string (required)
          password: string (required)
      response:
        201:
          description: "User created"
          schema: User
        400:
          description: "Validation error"
```

#### Step 2.2: Analyze Architecture

```yaml
id: analyze-architecture
name: "Document system architecture"

produces:
  artifacts:
    - path: "artifacts/docs/architecture/overview.md"
    - path: "artifacts/docs/architecture/modules/"

instructions: |
  1. Identify architectural patterns:
     - Layers (API, Service, Data)
     - Design patterns used
     - Data flow
  2. For each major module:
     - Purpose
     - Dependencies
     - Public interface
     - Key concepts
  3. Create architecture documentation

template: |
  # Architecture Overview

  ## System Layers

  ```
  ┌─────────────────────────────────────────┐
  │           API Layer (routes)            │
  │  - Express routes                       │
  │  - Request validation                   │
  │  - Response formatting                  │
  ├─────────────────────────────────────────┤
  │         Service Layer (business)        │
  │  - Business logic                       │
  │  - Orchestration                        │
  ├─────────────────────────────────────────┤
  │          Data Layer (models)            │
  │  - Database access                      │
  │  - Data transformation                  │
  └─────────────────────────────────────────┘
  ```

  ## Key Modules

  ### Authentication (src/auth/)
  Handles user authentication and authorization.

  **Key concepts:**
  - JWT tokens for stateless auth
  - Refresh token rotation
  - Role-based access control

  ### Users (src/users/)
  User management and profiles.
```

#### Step 2.3: Extract Config Reference

```yaml
id: analyze-config
name: "Document configuration options"

produces:
  artifacts:
    - path: "artifacts/docs/config-reference.md"

instructions: |
  1. Find all config sources:
     - .env variables
     - Config files
     - CLI arguments
  2. For each option:
     - Name
     - Type
     - Default value
     - Description
     - Example
  3. Create config-reference.md

template: |
  # Configuration Reference

  ## Environment Variables

  | Variable | Type | Default | Description |
  |----------|------|---------|-------------|
  | `PORT` | number | 3000 | Server port |
  | `DATABASE_URL` | string | - | PostgreSQL connection string |
  | `JWT_SECRET` | string | - | Secret for JWT signing |
  | `LOG_LEVEL` | string | info | Logging level (debug/info/warn/error) |

  ## Example .env

  ```env
  PORT=3000
  DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
  JWT_SECRET=your-secret-here
  LOG_LEVEL=debug
  ```
```

### Exit Gate: analyze_to_document

```yaml
gate:
  name: analyze_to_document
  threshold: 0.75

  criteria:
    - name: "API analyzed"
      weight: 0.35
      check: "All API endpoints documented in API-*.yaml"

    - name: "Architecture documented"
      weight: 0.35
      check: "Architecture overview exists"

    - name: "Config documented"
      weight: 0.30
      check: "Config reference exists"
```

---

## PHASE 3: DOCUMENT

### Purpose
Stworzyć właściwą dokumentację dla użytkowników.

### Entry Conditions
```yaml
requires:
  gates:
    - "analyze_to_document: passed"
  artifacts:
    - "artifacts/docs/api/*.yaml"
    - "artifacts/docs/architecture/"
```

### Steps

#### Step 3.1: Create Getting Started

```yaml
id: create-getting-started
name: "Write getting started guide"

produces:
  artifacts:
    - path: "docs/getting-started.md"

instructions: |
  1. Write installation steps
  2. Write quick start example
  3. Write first API call example
  4. Link to deeper docs
  5. Audience: new user, 5-10 minutes to first success

template: |
  # Getting Started

  ## Prerequisites

  - Node.js 18+
  - PostgreSQL 14+

  ## Installation

  ```bash
  # Clone repository
  git clone https://github.com/org/repo.git
  cd repo

  # Install dependencies
  npm install

  # Configure environment
  cp .env.example .env
  # Edit .env with your values

  # Run migrations
  npm run db:migrate

  # Start server
  npm start
  ```

  ## Your First API Call

  ```bash
  # Create a user
  curl -X POST http://localhost:3000/api/v1/users \
    -H "Content-Type: application/json" \
    -d '{"email": "test@example.com", "name": "Test User", "password": "secret123"}'
  ```

  ## Next Steps

  - [API Reference](./api/) - Full API documentation
  - [Architecture](./architecture/) - System design
  - [Configuration](./config-reference.md) - All config options
```

#### Step 3.2: Generate API Documentation

```yaml
id: generate-api-docs
name: "Create API reference from analysis"

requires:
  artifacts:
    - "artifacts/docs/api/*.yaml"

produces:
  artifacts:
    - path: "docs/api/*.md"

instructions: |
  1. For each API-*.yaml:
     a. Convert to readable markdown
     b. Add examples for each endpoint
     c. Add error handling section
     d. Link to related endpoints
  2. Create index page

template: |
  # Users API

  Base URL: `/api/v1/users`

  ## List Users

  ```http
  GET /api/v1/users
  ```

  **Query Parameters:**

  | Parameter | Type | Default | Description |
  |-----------|------|---------|-------------|
  | limit | integer | 20 | Max results |
  | offset | integer | 0 | Skip results |

  **Example Request:**

  ```bash
  curl http://localhost:3000/api/v1/users?limit=10
  ```

  **Example Response:**

  ```json
  {
    "data": [
      {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe"
      }
    ],
    "pagination": {
      "total": 100,
      "limit": 10,
      "offset": 0
    }
  }
  ```

  **Error Responses:**

  | Code | Description |
  |------|-------------|
  | 401 | Unauthorized - missing or invalid token |
  | 500 | Server error |
```

#### Step 3.3: Create Module Documentation

```yaml
id: create-module-docs
name: "Document individual modules"

requires:
  artifacts:
    - "artifacts/docs/architecture/"

produces:
  artifacts:
    - path: "docs/modules/*.md"

instructions: |
  1. For each major module:
     a. Purpose and responsibility
     b. Public API (functions, classes)
     c. Dependencies
     d. Usage examples
     e. Common patterns
  2. Link modules together
```

#### Step 3.4: Create Index/Navigation

```yaml
id: create-index
name: "Create documentation index"

produces:
  artifacts:
    - path: "docs/index.md"
    - path: "docs/_sidebar.md"  # If using docsify
    - path: "mkdocs.yml"  # If using mkdocs

instructions: |
  1. List all documentation pages
  2. Organize into categories
  3. Create navigation structure
  4. Add search keywords

template: |
  # Documentation

  ## Quick Links

  - [Getting Started](./getting-started.md)
  - [API Reference](./api/)
  - [Configuration](./config-reference.md)

  ## Guides

  - [Architecture Overview](./architecture/overview.md)
  - [Authentication Guide](./guides/authentication.md)
  - [Deployment Guide](./guides/deployment.md)

  ## Reference

  - [API Reference](./api/)
  - [Configuration](./config-reference.md)
  - [Error Codes](./reference/errors.md)

  ## Contributing

  - [Development Setup](./contributing/setup.md)
  - [Code Style](./contributing/style.md)
```

### Exit Gate: document_to_review

```yaml
gate:
  name: document_to_review
  threshold: 0.80

  criteria:
    - name: "Getting started exists"
      weight: 0.25
      check: "docs/getting-started.md complete"

    - name: "API docs complete"
      weight: 0.30
      check: "All API endpoints documented with examples"

    - name: "Architecture documented"
      weight: 0.20
      check: "Architecture overview in docs/"

    - name: "Index/navigation exists"
      weight: 0.15
      check: "docs/index.md with links to all pages"

    - name: "No broken links"
      weight: 0.10
      check: "All internal links valid"
```

---

## PHASE 4: REVIEW

### Purpose
Przejrzeć dokumentację pod kątem jakości i dokładności.

### Entry Conditions
```yaml
requires:
  gates:
    - "document_to_review: passed"
  artifacts:
    - "docs/*.md"
```

### Steps

#### Step 4.1: Technical Review

```yaml
id: technical-review
name: "Verify technical accuracy"

instructions: |
  1. For each code example:
     - Does it actually work?
     - Is the output correct?
     - Are error cases shown?
  2. For each API endpoint:
     - Are parameters correct?
     - Are responses accurate?
  3. For architecture docs:
     - Does it match actual code?
  4. Mark issues found

checklist: |
  ## Technical Review Checklist

  □ All code examples tested and working
  □ API request/response examples accurate
  □ Configuration options match .env.example
  □ Architecture diagrams match code
  □ Version numbers current
  □ Links to external resources valid
```

#### Step 4.2: Editorial Review

```yaml
id: editorial-review
name: "Review writing quality"

instructions: |
  1. Check for:
     - Clarity (can a new user understand?)
     - Consistency (same terms throughout?)
     - Completeness (no missing steps?)
     - Conciseness (no unnecessary words?)
  2. Check formatting:
     - Headers hierarchy correct
     - Code blocks formatted
     - Lists used appropriately
  3. Check navigation:
     - Logical flow
     - Cross-references work

checklist: |
  ## Editorial Review Checklist

  □ Clear, jargon-free language
  □ Consistent terminology
  □ Step-by-step instructions complete
  □ Headers follow hierarchy (h1 > h2 > h3)
  □ Code blocks have language tags
  □ No typos or grammar errors
```

#### Step 4.3: User Test Documentation

```yaml
id: user-test-docs
name: "Test docs with real user"

instructions: |
  1. Find someone unfamiliar with codebase
  2. Ask them to:
     - Set up project using Getting Started
     - Make first API call
     - Find answer to specific question
  3. Observe:
     - Where do they get stuck?
     - What's confusing?
     - What's missing?
  4. Update docs based on feedback
```

### Exit Gate: review_to_publish

```yaml
gate:
  name: review_to_publish
  threshold: 0.85

  criteria:
    - name: "Technical review passed"
      weight: 0.35
      check: "All examples tested and working"

    - name: "Editorial review passed"
      weight: 0.25
      check: "Writing quality checklist complete"

    - name: "User tested"
      weight: 0.25
      check: "At least 1 user successfully followed docs"

    - name: "No blocking issues"
      weight: 0.15
      check: "All critical issues resolved"
```

---

## PHASE 5: PUBLISH

### Purpose
Opublikować dokumentację w dostępnym miejscu.

### Entry Conditions
```yaml
requires:
  gates:
    - "review_to_publish: passed"
```

### Steps

#### Step 5.1: Choose Publishing Platform

```yaml
id: choose-platform
name: "Select documentation platform"

instructions: |
  1. Options:
     - GitHub Pages (free, simple)
     - GitBook (hosted, nice UI)
     - Read the Docs (versioning)
     - Self-hosted (full control)
  2. Consider:
     - Team preferences
     - Versioning needs
     - Search requirements
     - Cost
  3. Configure chosen platform
```

#### Step 5.2: Deploy Documentation

```yaml
id: deploy-docs
name: "Publish to chosen platform"

instructions: |
  For GitHub Pages:
  ```bash
  # Using mkdocs
  mkdocs gh-deploy

  # Or manual
  git subtree push --prefix docs origin gh-pages
  ```

  For Netlify/Vercel:
  - Connect repository
  - Set build command
  - Deploy

  Verify:
  - Site is accessible
  - All pages load
  - Search works (if applicable)
  - Mobile responsive
```

#### Step 5.3: Set Up Maintenance

```yaml
id: setup-maintenance
name: "Establish update process"

produces:
  artifacts:
    - path: "docs/CONTRIBUTING.md"

instructions: |
  1. Document update process:
     - How to update docs
     - Review requirements
     - Deploy process
  2. Set up automation:
     - CI check for broken links
     - Auto-deploy on merge
  3. Assign ownership:
     - Who reviews doc changes?
     - How often to audit?
```

### Exit Gate: publish_complete

```yaml
gate:
  name: publish_complete
  threshold: 0.80

  criteria:
    - name: "Docs published"
      weight: 0.40
      check: "Documentation accessible at public URL"

    - name: "Verified accessible"
      weight: 0.30
      check: "All pages load correctly"

    - name: "Maintenance documented"
      weight: 0.30
      check: "Update process documented"
```

---

## ARTIFACTS SUMMARY

| Artifact | Phase | Purpose |
|----------|-------|---------|
| codebase-map.yaml | Scan | Structure overview |
| doc-targets.yaml | Scan | What to document |
| api/API-XXX.yaml | Analyze | API definitions |
| architecture/overview.md | Analyze | System design |
| config-reference.md | Analyze/Document | Config options |
| docs/getting-started.md | Document | Quick start |
| docs/api/*.md | Document | API reference |
| docs/index.md | Document | Navigation |
| CONTRIBUTING.md | Publish | Maintenance guide |

---

## STATE TRANSITIONS

```
┌──────┐     0.70      ┌─────────┐     0.75      ┌──────────┐
│ SCAN │──────────────▶│ ANALYZE │──────────────▶│ DOCUMENT │
└──────┘               └─────────┘               └──────────┘
                                                      │
                                                  0.80│
                                                      ▼
┌─────────┐     0.80      ┌────────┐
│ PUBLISH │◀──────────────│ REVIEW │
└─────────┘               └────────┘
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
| "Document this codebase" | Start Scan phase |
| "Analyze the API" | Execute analyze-api step |
| "Write getting started" | Execute create-getting-started step |
| "Review the docs" | Enter Review phase |
| "Publish documentation" | Execute deploy-docs step |
