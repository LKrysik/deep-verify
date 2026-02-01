Deep Verify VS Code Extension — Rozszerzenie Specyfikacji
Dodatek: Konfiguracja Per Projekt i Pattern Library

17. Konfiguracja Per Projekt
17.1 Hierarchia Konfiguracji
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONFIGURATION HIERARCHY (od najniższego do najwyższego priorytetu)         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. DEFAULTS (wbudowane w rozszerzenie)                                     │
│     └── Bazowe ustawienia, działają "out of the box"                       │
│                                                                              │
│  2. GLOBAL USER CONFIG                                                       │
│     └── ~/.deepverify/config.json                                          │
│     └── Ustawienia użytkownika na wszystkie projekty                       │
│                                                                              │
│  3. GLOBAL PATTERNS                                                         │
│     └── ~/.deepverify/patterns/                                            │
│     └── Własne patterny dostępne we wszystkich projektach                  │
│                                                                              │
│  4. WORKSPACE CONFIG (VS Code)                                              │
│     └── .vscode/settings.json → "deepVerify.*"                             │
│     └── Standardowa konfiguracja VS Code per workspace                     │
│                                                                              │
│  5. PROJECT CONFIG (Deep Verify specific)                                   │
│     └── .deepverify/config.json                                            │
│     └── Pełna konfiguracja projektu                                        │
│                                                                              │
│  6. PROJECT PATTERNS                                                        │
│     └── .deepverify/patterns/                                              │
│     └── Patterny specyficzne dla projektu                                  │
│                                                                              │
│  Wyższy priorytet nadpisuje niższy.                                        │
│  Patterny się łączą (merge), nie nadpisują.                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
17.2 Struktura Katalogu .deepverify/
project-root/
├── .deepverify/
│   ├── config.json           # Główna konfiguracja projektu
│   ├── doc-mapping.json      # Mapowanie dokumentacja ↔ kod
│   ├── patterns/             # Patterny specyficzne dla projektu
│   │   ├── spark.yaml
│   │   ├── security.yaml
│   │   └── custom.yaml
│   ├── prompts/              # Własne prompty dla projektu
│   │   ├── code-review.md
│   │   ├── security-audit.md
│   │   └── performance.md
│   └── history/              # Lokalna historia weryfikacji (opcjonalne)
│       └── .gitignore        # history/ w .gitignore
├── src/
├── docs/
└── ...
17.3 Plik config.json — Pełna Struktura
json{
  "$schema": "https://deepverify.dev/schemas/config.json",
  "version": "1.0",

  "project": {
    "name": "My Spark Project",
    "type": "data-engineering",
    "languages": ["python", "sql"],
    "frameworks": ["spark", "databricks", "delta"]
  },

  "cli": {
    "default": "claude",
    "providers": {
      "claude": {
        "enabled": true,
        "model": "claude-sonnet-4-20250514",
        "timeout": 120
      },
      "gemini": {
        "enabled": true,
        "model": "gemini-pro"
      },
      "ollama": {
        "enabled": false,
        "model": "codellama"
      }
    }
  },

  "context": {
    "maxSize": "150KB",
    "autoInclude": {
      "imports": true,
      "sameDirectory": false,
      "configFiles": true,
      "typeDefinitions": true
    },
    "alwaysInclude": [
      "src/config.py",
      "src/types.py"
    ],
    "exclude": [
      "**/*.test.py",
      "**/fixtures/**",
      "legacy/**"
    ]
  },

  "documentation": {
    "mappingFile": "doc-mapping.json",
    "autoDetect": true,
    "roots": ["docs/", "README.md"]
  },

  "patterns": {
    "enabled": true,
    "global": true,
    "project": true,
    "files": [
      "patterns/spark.yaml",
      "patterns/security.yaml"
    ],
    "disabled": [
      "generic-style"
    ]
  },

  "prompts": {
    "default": "code-review",
    "files": {
      "code-review": "prompts/code-review.md",
      "security": "prompts/security-audit.md",
      "performance": "prompts/performance.md"
    }
  },

  "verification": {
    "defaultMode": "file-with-context",
    "autoTrigger": {
      "onSave": false,
      "onPreCommit": true
    },
    "severity": {
      "failOn": ["critical"],
      "warnOn": ["warning"]
    }
  },

  "ui": {
    "showInlineDecorations": true,
    "panelPosition": "bottom",
    "groupFindingsBy": "severity"
  },

  "history": {
    "enabled": true,
    "retention": "30d",
    "location": ".deepverify/history"
  }
}

18. Mapowanie Dokumentacja ↔ Kod
18.1 Cel
Szybkie porównywanie dokumentacji z kodem wymaga wiedzy który plik dokumentacji opisuje który kod. Mapowanie może być automatyczne (konwencje) lub ręczne (konfiguracja).
18.2 Plik doc-mapping.json
json{
  "$schema": "https://deepverify.dev/schemas/doc-mapping.json",
  "version": "1.0",

  "autoDetect": {
    "enabled": true,
    "conventions": [
      {
        "name": "readme-per-folder",
        "docPattern": "**/README.md",
        "codePattern": "**/*.{py,js,ts}",
        "scope": "same-directory"
      },
      {
        "name": "docs-folder",
        "docPattern": "docs/**/*.md",
        "codePattern": "src/**/*.py",
        "matching": "filename"
      }
    ]
  },

  "explicit": [
    {
      "doc": "docs/api-reference.md",
      "code": ["src/api/**/*.py"],
      "description": "API documentation"
    },
    {
      "doc": "docs/architecture.md",
      "code": ["src/core/**/*.py", "src/services/**/*.py"],
      "description": "Architecture overview"
    },
    {
      "doc": "docs/pipelines/etl.md",
      "code": ["src/pipelines/etl/*.py"],
      "description": "ETL pipeline documentation"
    },
    {
      "doc": "README.md",
      "code": ["src/main.py", "src/cli.py"],
      "sections": {
        "## Installation": ["setup.py", "requirements.txt"],
        "## Usage": ["src/cli.py"],
        "## API": ["src/api/"]
      }
    }
  ],

  "docstring": {
    "enabled": true,
    "verifyOnCodeChange": true,
    "languages": {
      "python": {
        "style": "google",
        "requireForPublic": true
      },
      "typescript": {
        "style": "tsdoc"
      }
    }
  },

  "ignore": [
    "docs/internal/**",
    "**/*.draft.md"
  ]
}
```

### 18.3 Automatyczne Wykrywanie Par

Wtyczka automatycznie proponuje mapowania na podstawie:

**Konwencja nazw:** `docs/pipeline.md` ↔ `src/pipeline.py`

**Lokalizacja:** `src/module/README.md` ↔ `src/module/*.py`

**Zawartość:** Parsuje linki i odniesienia w dokumentacji do plików kodu.

**Historia Git:** Pliki często commitowane razem mogą być powiązane.

### 18.4 UI dla Mapowania

W panelu bocznym Deep Verify pojawia się widok "Doc ↔ Code Mappings":
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DOC ↔ CODE MAPPINGS                                          [+ Add] [⟳]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  📄 README.md                                                               │
│  ├── 📁 src/main.py                                                        │
│  └── 📁 src/cli.py                                              [Compare]  │
│                                                                              │
│  📄 docs/api-reference.md                                                  │
│  └── 📁 src/api/** (12 files)                                   [Compare]  │
│                                                                              │
│  📄 docs/pipelines/etl.md                                                  │
│  └── 📁 src/pipelines/etl/** (5 files)                          [Compare]  │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│  SUGGESTED (auto-detected)                                                  │
│                                                                              │
│  📄 docs/config.md                                                         │
│  └── 📁 src/config.py                                   [Accept] [Ignore]  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 18.5 Quick Compare

Po skonfigurowaniu mapowania, użytkownik może:

**Z poziomu kodu:** Right-click na plik → "Compare with Documentation" → automatycznie otwiera powiązany doc i uruchamia porównanie.

**Z poziomu dokumentacji:** Right-click na .md → "Compare with Code" → otwiera powiązany kod.

**Skrót:** `Ctrl+Shift+D` na aktywnym pliku → porównaj z mapowanym odpowiednikiem.

---

## 19. Pattern Library

### 19.1 Koncepcja

Pattern Library to zbiór reguł/wzorców które wtyczka wykorzystuje do weryfikacji. Patterny nie zastępują LLM — wzbogacają prompt o specyficzne rzeczy do sprawdzenia.

### 19.2 Poziomy Pattern Library
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PATTERN LIBRARY LEVELS                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. BUILTIN PATTERNS                                                        │
│     └── Wbudowane w rozszerzenie                                           │
│     └── Podstawowe patterny dla popularnych języków/frameworków            │
│     └── Aktualizowane z rozszerzeniem                                      │
│     └── Lokalizacja: wewnątrz rozszerzenia                                 │
│                                                                              │
│  2. COMMUNITY PATTERNS (future)                                             │
│     └── Pobierane z registry                                               │
│     └── Tworzone przez społeczność                                         │
│     └── Lokalizacja: ~/.deepverify/community-patterns/                     │
│                                                                              │
│  3. GLOBAL USER PATTERNS                                                    │
│     └── Własne patterny użytkownika                                        │
│     └── Dostępne we wszystkich projektach                                  │
│     └── Lokalizacja: ~/.deepverify/patterns/                               │
│                                                                              │
│  4. PROJECT PATTERNS                                                        │
│     └── Specyficzne dla projektu                                           │
│     └── Commitowane do repo                                                │
│     └── Lokalizacja: .deepverify/patterns/                                 │
│                                                                              │
│  MERGE STRATEGY:                                                            │
│  Wszystkie poziomy są łączone. Project może disable'ować patterny          │
│  z wyższych poziomów przez "disabled" w config.                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
19.3 Format Pattern File (YAML)
yaml# .deepverify/patterns/spark.yaml

$schema: "https://deepverify.dev/schemas/pattern.yaml"
version: "1.0"

metadata:
  name: "Spark Patterns"
  description: "Patterns for Apache Spark code verification"
  author: "Your Name"
  tags: ["spark", "pyspark", "data-engineering"]
  languages: ["python"]
  frameworks: ["spark", "databricks"]

patterns:

  - id: "spark-broadcast-large-table"
    name: "Broadcast Join on Large Table"
    severity: "critical"
    description: |
      Detects use of broadcast() on potentially large tables.
      Broadcasting large tables causes OOM on executors.
    detect:
      type: "code-pattern"
      languages: ["python"]
      patterns:
        - "broadcast\\s*\\(\\s*\\w+\\s*\\)"
        - "\\.hint\\s*\\(\\s*['\"]broadcast['\"]"
    context:
      - "Check if the broadcasted table is known to be small (<10MB)"
      - "Look for table size hints in comments or variable names"
    suggestion: |
      Remove broadcast() for large tables. Use regular shuffle join instead.
      If the table is small, add a comment confirming the size.
    examples:
      bad: |
        df.join(broadcast(large_orders), "id")
      good: |
        # small_lookup is <1MB
        df.join(broadcast(small_lookup), "id")
        # or without broadcast
        df.join(large_orders, "id")
    references:
      - "https://spark.apache.org/docs/latest/sql-performance-tuning.html"

  - id: "spark-collect-unbounded"
    name: "Collect Without Limit"
    severity: "critical"
    description: |
      Using .collect() without .limit() can cause driver OOM
      if the DataFrame is large.
    detect:
      type: "code-pattern"
      patterns:
        - "\\.collect\\s*\\(\\s*\\)"
      exclude:
        - "\\.limit\\s*\\([^)]+\\)\\s*\\.collect"
        - "\\.take\\s*\\("
    suggestion: |
      Use .take(n), .limit(n).collect(), or ensure DataFrame is small.
    examples:
      bad: |
        results = large_df.collect()
      good: |
        results = large_df.limit(1000).collect()
        # or
        results = large_df.take(1000)

  - id: "spark-udf-vs-builtin"
    name: "UDF Instead of Built-in Function"
    severity: "warning"
    description: |
      Python UDFs are significantly slower than Spark built-in functions
      and prevent Catalyst optimization.
    detect:
      type: "semantic"
      check: |
        Look for @udf or F.udf decorators/functions where a Spark
        built-in function could achieve the same result.
    suggestion: |
      Replace UDF with equivalent Spark built-in function.
      Common replacements:
      - String manipulation: use F.concat, F.substring, F.regexp_replace
      - Math: use F.round, F.abs, F.ceil
      - Date/time: use F.date_format, F.datediff

  - id: "delta-merge-no-partition"
    name: "MERGE Without Partition Predicate"
    severity: "critical"
    description: |
      MERGE INTO without partition column in condition causes
      full table scan on every merge operation.
    detect:
      type: "sql-pattern"
      patterns:
        - "MERGE\\s+INTO"
      check: |
        Verify that ON clause includes the partition column.
        Common partition columns: date, year, month, region.
    suggestion: |
      Add partition column to MERGE condition.
      Example: MERGE INTO target USING source 
      ON target.id = source.id AND target.date = source.date

  - id: "databricks-hardcoded-catalog"
    name: "Hardcoded Catalog/Schema"
    severity: "warning"
    description: |
      Hardcoded catalog or schema names make code non-portable
      between environments (dev/staging/prod).
    detect:
      type: "code-pattern"
      patterns:
        - "USE\\s+CATALOG\\s+['\"]\\w+['\"]"
        - "USE\\s+SCHEMA\\s+['\"]\\w+['\"]"
        - "spark\\.catalog\\.setCurrentCatalog\\s*\\(['\"]\\w+['\"]\\)"
    exclude:
      - "# noqa: hardcoded-catalog"
      - "getArgument|dbutils\\.widgets"
    suggestion: |
      Use widgets, environment variables, or configuration:
      catalog = dbutils.widgets.get("catalog")
      spark.catalog.setCurrentCatalog(catalog)
```

### 19.4 Typy Detekcji w Patterns

**code-pattern:** Regex matching na kodzie. Szybkie, działa offline. Dla prostych wzorców.

**sql-pattern:** Parsuje SQL i sprawdza strukturę. Rozumie składnię SQL.

**semantic:** Opisowy check dla LLM. Wtyczka dołącza opis do prompta i LLM sprawdza.

**ast:** Parsuje AST (Abstract Syntax Tree) i sprawdza strukturę kodu. Dla złożonych wzorców.

### 19.5 Jak Patterny Są Używane
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PATTERN INTEGRATION FLOW                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. USER TRIGGERS VERIFICATION                                              │
│     └── "Verify File" on pipeline.py                                       │
│                                                                              │
│  2. WTYCZKA ŁADUJE RELEVANT PATTERNS                                        │
│     └── Filtruje po: language=python, framework=spark                      │
│     └── Wynik: 15 patterns applicable                                      │
│                                                                              │
│  3. PRE-CHECK (code-pattern, local)                                         │
│     └── Uruchamia regex patterns lokalnie                                  │
│     └── Znajduje: 2 potential matches                                      │
│                                                                              │
│  4. BUILD PROMPT                                                            │
│     └── Bazowy prompt weryfikacji                                          │
│     └── + lista patterns z opisami "Check for these specific issues..."   │
│     └── + pre-check findings "I detected possible X on line Y, verify"    │
│                                                                              │
│  5. SEND TO LLM                                                             │
│     └── LLM otrzymuje kod + wzbogacony prompt                              │
│     └── LLM weryfikuje z wiedzą o domain-specific patterns                │
│                                                                              │
│  6. PARSE RESPONSE                                                          │
│     └── Map findings do pattern IDs jeśli match                            │
│     └── Dodaj references i suggestions z pattern definition                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
19.6 Wbudowane Pattern Packs (Builtin)
yaml# Wbudowane w rozszerzenie

packs:
  - name: "python-core"
    description: "Core Python antipatterns"
    patterns: 12
    
  - name: "javascript-core"
    description: "Core JavaScript/TypeScript antipatterns"
    patterns: 15
    
  - name: "sql-core"
    description: "SQL antipatterns and performance issues"
    patterns: 10
    
  - name: "security-basic"
    description: "Basic security checks (injection, secrets)"
    patterns: 8
    
  - name: "async-patterns"
    description: "Async/await and concurrency issues"
    patterns: 7
```

### 19.7 Zarządzanie Patterns w UI

W Settings lub przez Command Palette:
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PATTERN LIBRARY MANAGER                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ENABLED PATTERNS                                                [+ Create]  │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  📦 BUILTIN                                                                 │
│  ├── ✓ python-core (12 patterns)                              [Disable]    │
│  ├── ✓ sql-core (10 patterns)                                 [Disable]    │
│  ├── ○ javascript-core (15 patterns)                          [Enable]     │
│  └── ✓ security-basic (8 patterns)                            [Disable]    │
│                                                                              │
│  📁 GLOBAL USER (~/.deepverify/patterns/)                                  │
│  ├── ✓ my-spark-patterns.yaml (5 patterns)           [Edit] [Disable]     │
│  └── ✓ company-standards.yaml (3 patterns)           [Edit] [Disable]     │
│                                                                              │
│  📁 PROJECT (.deepverify/patterns/)                                        │
│  ├── ✓ spark.yaml (8 patterns)                       [Edit] [Disable]     │
│  └── ✓ databricks.yaml (6 patterns)                  [Edit] [Disable]     │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│  TOTAL: 52 patterns enabled                                                 │
│                                                                              │
│  [Import Pattern Pack...] [Export Project Patterns]                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 19.8 Tworzenie Własnych Patterns

Command: `Deep Verify: Create New Pattern`

Wizard prowadzi przez:
1. Nazwa i opis
2. Severity (critical/warning/info)
3. Typ detekcji (code-pattern/semantic)
4. Dla code-pattern: regex lub przykład kodu do match
5. Suggestion i examples
6. Zapisz do global lub project

---

## 20. Inicjalizacja Projektu

### 20.1 Komenda Init

`Deep Verify: Initialize Project` tworzy strukturę `.deepverify/` z domyślną konfiguracją.
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  INITIALIZE DEEP VERIFY                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Project Type:                                                              │
│  ○ Data Engineering (Spark, Databricks, Airflow)                           │
│  ○ Backend (Python, Node.js, Go)                                           │
│  ○ Frontend (React, Vue, Angular)                                          │
│  ○ Full Stack                                                               │
│  ○ Custom                                                                   │
│                                                                              │
│  Options:                                                                    │
│  ☑ Create doc-mapping.json                                                 │
│  ☑ Include recommended patterns for project type                           │
│  ☑ Add .deepverify to .gitignore (history folder only)                    │
│  ☐ Enable pre-commit hook                                                  │
│                                                                              │
│  [Initialize]  [Cancel]                                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
20.2 Wykrywanie Typu Projektu
Wtyczka może auto-detect typ projektu na podstawie:

package.json → Node.js/Frontend
pyproject.toml, setup.py → Python
Obecność spark, databricks w dependencies → Data Engineering
Struktura folderów


21. Przykładowe Konfiguracje
21.1 Projekt Data Engineering (Spark/Databricks)
json// .deepverify/config.json
{
  "project": {
    "name": "ETL Pipelines",
    "type": "data-engineering",
    "languages": ["python", "sql"],
    "frameworks": ["spark", "databricks", "delta"]
  },
  "patterns": {
    "files": [
      "patterns/spark.yaml",
      "patterns/delta.yaml",
      "patterns/unity-catalog.yaml"
    ]
  },
  "documentation": {
    "roots": ["docs/", "notebooks/README.md"]
  },
  "context": {
    "alwaysInclude": [
      "src/config/settings.py",
      "src/utils/spark_utils.py"
    ]
  }
}
json// .deepverify/doc-mapping.json
{
  "explicit": [
    {
      "doc": "docs/pipelines/sales.md",
      "code": ["src/pipelines/sales/**/*.py"]
    },
    {
      "doc": "docs/data-models.md",
      "code": ["src/models/**/*.py", "src/schemas/**/*.sql"]
    }
  ]
}
21.2 Projekt Backend API
json// .deepverify/config.json
{
  "project": {
    "name": "User Service API",
    "type": "backend",
    "languages": ["python"],
    "frameworks": ["fastapi", "sqlalchemy"]
  },
  "patterns": {
    "files": [
      "patterns/api-security.yaml",
      "patterns/sqlalchemy.yaml"
    ]
  },
  "documentation": {
    "roots": ["docs/api/", "openapi.yaml"]
  },
  "prompts": {
    "files": {
      "api-review": "prompts/api-review.md",
      "security": "prompts/security-audit.md"
    }
  }
}
json// .deepverify/doc-mapping.json
{
  "explicit": [
    {
      "doc": "openapi.yaml",
      "code": ["src/api/routes/**/*.py"],
      "description": "OpenAPI spec should match route implementations"
    },
    {
      "doc": "docs/api/authentication.md",
      "code": ["src/auth/**/*.py"]
    }
  ],
  "docstring": {
    "enabled": true,
    "verifyOnCodeChange": true
  }
}
```

---

## 22. Command Palette — Pełna Lista
```
Deep Verify: Verify Selection
Deep Verify: Verify Selection with File Context
Deep Verify: Verify Selection with Project Context
Deep Verify: Verify File
Deep Verify: Verify File with Project Context
Deep Verify: Verify Selected Files
Deep Verify: Verify Folder
Deep Verify: Verify Uncommitted Changes
Deep Verify: Verify Staged Changes
Deep Verify: Compare with Documentation
Deep Verify: Compare with Mapped Documentation    ← używa doc-mapping
Deep Verify: Custom Prompt
Deep Verify: Run Saved Prompt...

Deep Verify: Select CLI Provider
Deep Verify: Refresh CLI Detection

Deep Verify: Initialize Project
Deep Verify: Open Project Config
Deep Verify: Edit Doc Mappings
Deep Verify: Manage Patterns
Deep Verify: Create New Pattern
Deep Verify: Import Pattern Pack

Deep Verify: Show Results Panel
Deep Verify: Clear Results
Deep Verify: Show History
```

---

## 23. Zaktualizowana Struktura Plików Rozszerzenia
```
deep-verify-vscode/
├── package.json
├── src/
│   ├── extension.ts
│   ├── commands/
│   │   ├── verify/
│   │   │   ├── selection.ts
│   │   │   ├── file.ts
│   │   │   ├── folder.ts
│   │   │   ├── git.ts
│   │   │   └── docCompare.ts
│   │   ├── config/
│   │   │   ├── init.ts
│   │   │   ├── openConfig.ts
│   │   │   └── editDocMapping.ts
│   │   ├── patterns/
│   │   │   ├── manage.ts
│   │   │   ├── create.ts
│   │   │   └── import.ts
│   │   └── prompts/
│   │       ├── custom.ts
│   │       └── saved.ts
│   ├── adapters/
│   │   ├── base.ts
│   │   ├── claude.ts
│   │   ├── gemini.ts
│   │   ├── ollama.ts
│   │   └── custom.ts
│   ├── config/
│   │   ├── loader.ts           # Ładuje hierarchię konfiguracji
│   │   ├── schema.ts           # TypeScript types dla config
│   │   ├── defaults.ts         # Domyślne wartości
│   │   └── validator.ts        # Walidacja config files
│   ├── patterns/
│   │   ├── loader.ts           # Ładuje i merguje patterns
│   │   ├── matcher.ts          # Pre-check regex matching
│   │   ├── promptBuilder.ts    # Buduje prompt z patterns
│   │   └── builtin/            # Wbudowane pattern packs
│   │       ├── python-core.yaml
│   │       ├── sql-core.yaml
│   │       └── security-basic.yaml
│   ├── docMapping/
│   │   ├── loader.ts
│   │   ├── autoDetect.ts
│   │   └── resolver.ts         # Resolve doc ↔ code pairs
│   ├── context/
│   │   ├── collector.ts
│   │   ├── imports.ts
│   │   ├── git.ts
│   │   └── limiter.ts          # Enforce context limits
│   ├── ui/
│   │   ├── resultsPanel.ts
│   │   ├── statusBar.ts
│   │   ├── decorations.ts
│   │   ├── docMappingView.ts   # Sidebar view
│   │   └── patternManager.ts   # Pattern management UI
│   ├── prompts/
│   │   ├── templates.ts
│   │   └── builder.ts
│   └── utils/
│       ├── parser.ts
│       ├── files.ts
│       └── logger.ts
├── schemas/                     # JSON schemas for config files
│   ├── config.json
│   ├── doc-mapping.json
│   └── pattern.json
├── resources/
└── test/

Czy ta rozszerzona specyfikacja pokrywa Twoje potrzeby? Mogę jeszcze bardziej rozwinąć któryś aspekt lub przejść do planowania implementacji.





Deep Verify VS Code Extension — Jak To Działa

Filozofia Narzędzia
Deep Verify to asystent weryfikacji wbudowany w edytor. Nie zastępuje programisty — daje mu drugie spojrzenie na kod w momencie gdy tego potrzebuje. Działa cicho w tle dopóki nie zostanie poproszony o pomoc, ale gdy już działa, dostarcza konkretne, actionable informacje zamiast ogólników.
Kluczowa zasada: zero konfiguracji na start, pełna kontrola gdy potrzebujesz. Nowy użytkownik instaluje wtyczkę, ma już Claude CLI, naciska Ctrl+Shift+V na zaznaczonym kodzie i dostaje wyniki. Zaawansowany użytkownik konfiguruje własne patterns, mapowania dokumentacji, automatyczne triggery.

Jak Ułatwia Pracę Deweloperom
Problem 1: "Napisałem kod z AI, ale czy on jest poprawny?"
Deweloper używa Copilot/Cursor/Claude do generowania kodu. Kod wygląda dobrze, kompiluje się, ale czy naprawdę robi to co powinien? Czy nie ma ukrytych bugów?
Rozwiązanie: Zaznacz wygenerowany kod, Ctrl+Shift+V, w 5 sekund masz analizę. Nie musisz kopiować do osobnego okna, nie musisz pisać prompta od zera. Wtyczka wie że to kod Python/Spark/SQL i wie jakie problemy szukać.
Problem 2: "Dokumentacja pewnie jest nieaktualna"
README mówi że funkcja przyjmuje 3 argumenty, ale kod ma ich 5. Docstring opisuje stare zachowanie. API spec nie zgadza się z implementacją.
Rozwiązanie: Skonfiguruj raz mapowanie doc↔kod. Potem jedno kliknięcie "Compare with Documentation" i masz listę rozbieżności. Możesz też włączyć automatyczne sprawdzanie przy zmianach.
Problem 3: "Przed commitem chcę mieć pewność"
Zrobiłeś zmiany, chcesz commitować, ale czy na pewno wszystko jest OK? Standardowy review to za dużo, ale żaden review to za mało.
Rozwiązanie: "Verify Uncommitted Changes" analizuje tylko to co zmieniłeś. Skupia się na nowym kodzie, nie na całym projekcie. Możesz też włączyć automatyczny trigger na pre-commit.
Problem 4: "Ten sam błąd popełniamy ciągle"
W zespole ciągle ktoś robi broadcast join na dużej tabeli, albo zapomina o partition predicate w MERGE. Code review łapie to za późno.
Rozwiązanie: Stwórz pattern dla tego błędu. Dodaj do repo w .deepverify/patterns/. Teraz każdy w zespole ma automatyczne sprawdzanie tego konkretnego problemu. Pattern zawiera nie tylko detekcję ale też wyjaśnienie i fix.
Problem 5: "Nowy w projekcie, nie znam konwencji"
Nowy deweloper nie zna wszystkich zasad projektu. Skąd ma wiedzieć że w tym projekcie zawsze używamy określonego stylu error handling?
Rozwiązanie: Patterns i prompts są w repo. Nowy deweloper instaluje wtyczkę, patterns ładują się automatycznie. Weryfikacja od razu mówi mu o konwencjach projektu których nie przestrzega.

Integracja z CLI
Dlaczego CLI a nie bezpośrednie API?
Wtyczka nie ma wbudowanych kluczy API ani bezpośredniej integracji z providerami AI. Zamiast tego używa CLI które użytkownik już ma zainstalowane i skonfigurowane.
Korzyści:
Użytkownik sam kontroluje koszty i rate limits — używa swojego konta Claude/Gemini, widzi zużycie w swoim dashboardzie.
Autentykacja jest już zrobiona — jeśli claude działa w terminalu, działa też we wtyczce.
Łatwe przełączanie między providerami — dziś Claude, jutro Gemini, pojutrze lokalny Ollama.
Brak vendor lock-in — wtyczka jest agnostyczna, nowy provider to tylko nowy adapter.
Prywatność — dane idą przez CLI które użytkownik kontroluje, nie przez serwery wtyczki.
Jak Wykrywane Jest CLI
Przy starcie VS Code wtyczka sprawdza w PATH:

claude --version
gemini --version
ollama --version

Dla każdego znalezionego CLI zapisuje że jest dostępne. W status barze pokazuje aktualnie wybrany provider. Jeśli nie znajdzie żadnego CLI, pokazuje komunikat z instrukcją instalacji.
Użytkownik może też zdefiniować własne CLI w ustawieniach — wystarczy podać komendę i sposób przekazania prompta.
Jak Wygląda Wywołanie
Gdy użytkownik triggeruje weryfikację:

Wtyczka zbiera kontekst (kod, pliki, patterns)
Buduje prompt z szablonu + kontekst + instrukcje z patterns
Zapisuje prompt do pliku tymczasowego
Wywołuje CLI: claude -p /tmp/dv-prompt-xxx.txt
Czeka na odpowiedź (z timeout i progress indicator)
Parsuje odpowiedź, wyciąga findings
Wyświetla wyniki w panelu

Dla użytkownika to jest transparentne — klika "Verify", widzi spinner, dostaje wyniki.

Kiedy Jest Wywoływane
Triggery Manualne (domyślne)
Skrót klawiszowy — Ctrl+Shift+V na zaznaczeniu lub aktywnym pliku.
Menu kontekstowe — Right-click → Deep Verify → wybór trybu.
Command Palette — Ctrl+Shift+P → "Deep Verify: ..."
Ikona w edytorze — Mała ikona na pasku tytułu pliku.
Panel boczny — Kliknięcie na plik w widoku Doc Mappings.
Triggery Automatyczne (opcjonalne, konfigurowalne)
On Save — Weryfikacja przy zapisie pliku. Domyślnie wyłączone bo może być wolne i kosztowne. Dla krytycznych plików można włączyć selektywnie.
On Pre-Commit — Git hook który uruchamia weryfikację przed commitem. Wtyczka może zarejestrować hook lub integrować się z istniejącym (husky, pre-commit).
On File Change — Dla par doc↔kod, gdy zmienia się kod, zaproponuj sprawdzenie czy dokumentacja jest aktualna.
On Branch Switch — Przy przełączeniu na branch z dużymi zmianami, zaproponuj weryfikację zmienionych plików.
Scheduled — Dla dużych projektów, nocna weryfikacja całego repo z raportem rano.
Triggery Kontekstowe (inteligentne)
Po paste — Gdy użytkownik wkleja duży blok kodu (np. z ChatGPT), wtyczka może zaproponować weryfikację.
Po generacji AI — Integracja z innymi rozszerzeniami (Copilot, Continue), po wygenerowaniu kodu zaproponuj weryfikację.
Przy otwarciu PR — Dla integracji z GitHub/GitLab, automatyczna weryfikacja zmian w PR.

Możliwości Podstawowe
Weryfikacja Kodu
Sprawdza kod pod kątem błędów logicznych, potencjalnych bugów, niespójności, złych praktyk. Nie jest linterem — nie sprawdza formatowania czy stylu. Szuka problemów semantycznych których narzędzia statyczne nie znajdą.
Weryfikacja z Kontekstem
Kod rzadko istnieje w izolacji. Funkcja wywołuje inne funkcje, używa typów z innych plików, zależy od konfiguracji. Wtyczka automatycznie zbiera relevantny kontekst aby LLM mógł zrozumieć szerszy obraz.
Porównanie Dokumentacji z Kodem
Dokumentacja szybko się dezaktualizuje. Wtyczka porównuje co dokumentacja mówi z tym co kod robi i raportuje rozbieżności.
Weryfikacja Zmian Git
Przed commitem lub pushem, sprawdź tylko to co się zmieniło. Szybsze i tańsze niż weryfikacja całego projektu.
Pattern-Based Verification
Predefiniowane reguły dla typowych problemów. Patterns są specyficzne dla języka/frameworka i zawierają nie tylko detekcję ale też wyjaśnienie i sugerowany fix.
Custom Prompts
Użytkownik może wpisać własne polecenie. "Sprawdź czy ten kod obsługuje wszystkie edge cases", "Znajdź potencjalne problemy z wydajnością", "Czy ta funkcja jest thread-safe?".

Możliwości Zaawansowane
Saved Prompts i Templates
Często używane prompty można zapisać i wywoływać jednym kliknięciem. Można je też współdzielić w zespole przez repo.
Project-Specific Configuration
Każdy projekt może mieć własną konfigurację: które patterns włączyć, jak mapować dokumentację, jakie pliki zawsze dołączać do kontekstu.
Hierarchia Patterns
Patterns z różnych poziomów (wbudowane, globalne użytkownika, projektowe) są mergowane. Projekt może wyłączyć patterns które nie mają sensu w jego kontekście.
Inline Decorations
Findings mogą być wyświetlane bezpośrednio w edytorze jako podkreślenia i ikony na marginesie, nie tylko w osobnym panelu.
History i Trends
Wtyczka może zapisywać historię weryfikacji lokalnie. Pozwala to zobaczyć czy jakość kodu się poprawia, które patterns najczęściej triggerują, które pliki mają najwięcej problemów.

Możliwości Których Jeszcze Nie Przewidziałeś
1. Verification Sessions (Multi-Turn)
Czasem jedna weryfikacja nie wystarczy. Chcesz dopytać o konkretny finding, poprosić o głębszą analizę, podyskutować o alternatywach.
Jak działa: Po weryfikacji możesz kliknąć "Continue" i zadać follow-up pytanie w kontekście poprzedniej analizy. Wtyczka utrzymuje sesję z CLI (jeśli CLI to wspiera) lub dołącza poprzednią wymianę do nowego prompta.
Przykład:
[Verification] → "CRITICAL: Possible race condition on line 45"
[User clicks "Ask More"] → "Wyjaśnij dokładniej ten race condition"
[Verification] → "Problem polega na tym że..."
[User] → "Jak to naprawić używając asyncio.Lock?"
[Verification] → "Oto propozycja fix..."
2. Comparative Verification
Porównaj dwie wersje tego samego kodu. Która jest lepsza? Co się zmieniło?
Jak działa: Zaznacz dwa pliki lub dwa commity i wybierz "Compare Versions". Wtyczka analizuje różnice i mówi która wersja jest lepsza i dlaczego.
Use cases:

Przed i po refactoringu — czy refactoring coś zepsuł?
Twój kod vs kod kolegi — code review assistance
Main vs feature branch — co wprowadziła ta zmiana?

3. Fix Suggestions with Preview
Nie tylko "tu jest bug" ale "oto naprawiony kod, chcesz zastosować?".
Jak działa: Przy każdym findingu z severity CRITICAL lub WARNING, wtyczka może wygenerować suggested fix. Użytkownik klika "Preview Fix", widzi diff, klika "Apply" i kod jest zmieniony.
Workflow:
[Finding] Broadcast join on large table (line 45)
[Suggestion] Remove broadcast()
[Preview Fix] → pokazuje diff
[Apply] → zmienia kod
[Undo] → git-like undo jeśli nie zadziałało
4. Learning Mode
Wtyczka może uczyć się z twoich decyzji.
Jak działa: Gdy dismissujesz finding jako false positive, wtyczka pyta dlaczego. Na podstawie tych odpowiedzi może:

Wyłączyć pattern który ciągle triggeruje false positives
Dostosować severity
Dodać exceptions do patterns

Feedback loop:
[Finding] UDF instead of built-in (line 23)
[User clicks "Dismiss - Not Applicable"]
[Wtyczka] "Dlaczego to nie dotyczy?"
[User] "Ta UDF robi coś czego built-in nie obsługuje"
[Wtyczka] Zapisuje że UDF z tym signature to exception
5. Team Insights (jeśli włączone)
Anonimowe statystyki z weryfikacji mogą być agregowane dla zespołu.
Jak działa: Opt-in feature. Wtyczka wysyła anonimowe dane (bez kodu!) do dashboardu zespołowego:

Które patterns najczęściej triggerują
Które pliki/moduły mają najwięcej findings
Trend jakości w czasie

Korzyści: Tech lead widzi że moduł X ma chroniczne problemy. Onboarding widzi że nowi ludzie robią błąd Y. Można priorytetyzować refactoring.
6. Integration with Test Results
Połącz weryfikację z wynikami testów.
Jak działa: Wtyczka czyta wyniki ostatniego test run. Jeśli test failuje, automatycznie dołącza test code i error message do kontekstu weryfikacji.
Przykład:
[Test fails] test_calculate_total AssertionError: expected 100, got 99.99
[User] "Verify" na calculate_total()
[Wtyczka] Dołącza failing test i error
[Verification] "Problem: floating point precision. Test expects integer but function returns float."
7. Documentation Generation
Nie tylko sprawdzaj dokumentację — generuj ją.
Jak działa: Na pliku bez dokumentacji, "Generate Documentation" tworzy docstringi, README sections, lub API docs na podstawie kodu.
Połączenie z weryfikacją: Po wygenerowaniu, automatycznie weryfikuje czy wygenerowana dokumentacja jest accurate.
8. Codebase Q&A
Zadawaj pytania o swój codebase.
Jak działa: "Ask about Codebase" pozwala zadać pytanie a wtyczka przeszukuje relevantne pliki i odpowiada z kontekstem.
Przykłady:

"Gdzie jest zdefiniowana funkcja process_payment?"
"Jak działa autentykacja w tym projekcie?"
"Jakie są wszystkie miejsca gdzie wywołujemy external API?"

Różnica od zwykłego search: Nie szuka tekstu — rozumie semantykę. "Gdzie obsługujemy błędy płatności" znajdzie kod nawet jeśli nie zawiera słowa "payment error".
9. Dependency Impact Analysis
Przed zmianą funkcji, sprawdź co może się zepsuć.
Jak działa: Zaznacz funkcję, "Analyze Impact". Wtyczka znajduje wszystkie miejsca które używają tej funkcji i analizuje jak twoja zmiana na nie wpłynie.
Przykład:
[User] Chcę zmienić signature calculate_total(items) → calculate_total(items, tax_rate)
[Impact Analysis]
- 15 call sites found
- 3 will break (no tax_rate passed)
- 12 already have tax logic elsewhere (potential duplication)
[Suggestion] Consider default parameter tax_rate=0 for backward compatibility
10. Verification Profiles
Różne tryby weryfikacji dla różnych sytuacji.
Jak działa: Zdefiniuj profiles które łączą patterns, prompts, severity thresholds:
Quick Check — Tylko critical issues, szybko, tani w tokenach.
Deep Review — Wszystkie patterns, pełny kontekst, dokładna analiza.
Security Audit — Tylko security patterns, skupiony na vulnerabilities.
Pre-Release — Wszystko + sprawdzenie dokumentacji + change analysis.
Debugging — Włącz diagnostic patterns, szukaj przyczyn konkretnego buga.
11. Multi-File Refactoring Verification
Przy dużym refactoringu, sprawdź całość.
Jak działa: Zaznacz wszystkie pliki które zmieniłeś w ramach refactoringu. "Verify Refactoring" analizuje czy zmiany są spójne, czy nic nie zostało pominięte, czy nie ma broken references.
Checks:

Czy wszystkie call sites zostały zaktualizowane?
Czy typy się zgadzają po zmianach?
Czy dokumentacja została zaktualizowana?
Czy testy pokrywają zmiany?

12. Context Pinning
Zawsze dołączaj pewne pliki do weryfikacji.
Jak działa: "Pin" plik w panelu bocznym. Od teraz każda weryfikacja w projekcie dołącza ten plik jako kontekst.
Use cases:

Types/interfaces file — zawsze relevantne
Config file — wpływa na zachowanie
Base classes — potrzebne do zrozumienia inheritance
README z konwencjami — przypomina o zasadach

13. Verification Checkpoints
Zapisz "stan dobry" i porównuj z nim później.
Jak działa: Po weryfikacji która przeszła czysto, "Save Checkpoint". Później możesz "Compare with Checkpoint" aby zobaczyć co się zmieniło od tamtego momentu.
Use case: Przed dużą zmianą, zapisz checkpoint. Po zmianach, porównaj. Jeśli coś poszło nie tak, wiesz dokładnie co.
14. Natural Language Rules
Definiuj reguły w naturalnym języku zamiast regex/YAML.
Jak działa: W ustawieniach projektu wpisz po prostu:
"Nigdy nie używaj print() w kodzie produkcyjnym"
"Każda funkcja publiczna musi mieć docstring"
"SQL queries muszą używać parameterized queries, nie string concatenation"
Wtyczka przekształca te reguły w część prompta i LLM ich pilnuje.
15. Verification Annotations
Oznacz kod który nie powinien być weryfikowany lub powinien być weryfikowany specjalnie.
Jak działa: Komentarze w kodzie:
python# @dv-ignore - This is intentionally complex
def legacy_calculation():
    ...

# @dv-verify security
def handle_user_input():
    ...

# @dv-context file:../types.py
def process_data():
    ...
Wtyczka rozumie te annotacje i odpowiednio modyfikuje weryfikację.

Flow Użytkownika — Dzień z Życia
Rano: Start Pracy
Otwierasz VS Code, wtyczka ładuje konfigurację projektu. W status barze widzisz "DV: Claude ✓". Wszystko gotowe.
9:15: Przeglądasz Kod Kolegi
Kolega prosił o review jego PR. Otwierasz zmienione pliki, zaznaczasz kluczową funkcję, Ctrl+Shift+V. Po 5 sekundach masz listę uwag. Jedna jest CRITICAL — race condition którego byś nie zauważył przy normalnym review.
10:30: Piszesz Nową Funkcję
Kończysz pisać funkcję, nie jesteś pewien czy obsłużyłeś wszystkie edge cases. "Deep Verify: Custom Prompt" → "Czy ta funkcja obsługuje: puste dane, null values, bardzo duże listy, concurrent access?"
Wtyczka znajduje że nie obsługujesz pustej listy — możliwy IndexError.
11:45: Dokumentacja
PM pyta czy dokumentacja API jest aktualna. Otwierasz api-spec.yaml, Right-click → "Compare with Mapped Code". Wtyczka porównuje ze wszystkimi plikami route'ów. Dwa endpoints mają rozbieżności — jeden brakujący parametr, jeden zmieniony response type.
14:00: Debugging
Test failuje, nie wiesz dlaczego. "Verify" na testowanej funkcji z kontekstem failing testu. Wtyczka widzi test expectation i kod, znajduje że off-by-one error w loop condition.
16:30: Przed Commitem
Zrobiłeś dużo zmian, chcesz commitować. "Verify Uncommitted Changes". Wtyczka analizuje git diff. Wszystko czyste poza jednym WARNING o potencjalnym performance issue. Decydujesz że to OK na teraz, dismissujesz z notatką, commitujesz.
17:00: Nowy Pattern
Drugi raz w tym tygodniu złapałeś ten sam błąd w code review. "Create New Pattern" → definiujesz regułę. Dodajesz do .deepverify/patterns/team.yaml. Commitujesz. Teraz cały zespół ma automatyczne sprawdzanie.

Podsumowanie Korzyści
Szybkość: Weryfikacja w sekundach, nie w minutach. Bez opuszczania edytora.
Kontekst: Wtyczka rozumie strukturę projektu i dołącza relevantny kontekst automatycznie.
Specificity: Patterns specyficzne dla twojego stacku (Spark, Databricks, etc.) łapią problemy których generic tools nie widzą.
Flexibility: Od quick check po deep audit, od manualnych triggerów po automatyczne.
Team Knowledge: Patterns i prompts w repo = wiedza zespołu zapisana i współdzielona.
Control: Ty kontrolujesz CLI, koszty, dane. Wtyczka to tylko interfejs.


Deep Verify + Deep Develop — Kompletna Specyfikacja

Część I: Filozofia i Architektura
1.1 Dwa Narzędzia, Jeden Ekosystem
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  DEEP VERIFY + DEEP DEVELOP ECOSYSTEM                                                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                      │
│                        ┌─────────────────────────────┐                                               │
│                        │      USER / OTHER PLUGIN    │                                               │
│                        └──────────────┬──────────────┘                                               │
│                                       │                                                              │
│              ┌────────────────────────┼────────────────────────┐                                     │
│              │                        │                        │                                     │
│              ▼                        ▼                        ▼                                     │
│  ┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐                               │
│  │   VS Code UI      │   │   Extension API   │   │   CLI Bridge      │                               │
│  │   (commands,      │   │   (programmatic   │   │   (headless       │                               │
│  │    menus, panels) │   │    access)        │   │    execution)     │                               │
│  └─────────┬─────────┘   └─────────┬─────────┘   └─────────┬─────────┘                               │
│            │                       │                       │                                         │
│            └───────────────────────┼───────────────────────┘                                         │
│                                    │                                                                 │
│                                    ▼                                                                 │
│            ┌────────────────────────────────────────────────────────────────────────┐                │
│            │              CORE ENGINE                                               │                │
│            │                                                                        │                │
│            │  ┌─────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐ │                │
│            │  │  DEEP VERIFY    │  │   DEEP DEVELOP      │  │   DEEP EXPLORE      │ │                │
│            │  │                 │  │                     │  │                     │ │                │
│            │  │  • Sprawdza     │  │  • Planuje          │  │  • eksploruje       │ │                │
│            │  │  • Waliduje     │  │  • Analizuje        │  │  • poznaje          │ │                │
│            │  │  • Raportuje    │  │  • Wykonuje         │  │  • bada             │ │                │
│            │  │                 │  │  • Iteruje          │  │  • wkyrywa          │ │                │
│            │  └────────┬────────┘  └──────────┬──────────┘  └──────────┬──────────┘ │                │
│            │           │                      │                        │            │                │
│            │           └──────────┬───────────┘────────────────────────┘            │                │
│            │                      │                                                 │                │
│            │           ┌──────────▼──────────┐                                      │                │
│            │           │   SHARED SERVICES   │                                      │                │
│            │           │                     │                                      │                │
│            │           │  • Context Collector│                                      │                │
│            │           │  • CLI Adapter      │                                      │                │
│            │           │  • Pattern Library  │                                      │                │
│            │           │  • Method Engine    │                                      │                │
│            │           │  • Config Manager   │                                      │                │
│            │           └─────────────────────┘                                      │                │
│            └────────────────────────────────────────────────────────────────────────┘                │
│                                    │                                                                 │
│                                    ▼                                                                 │
│            ┌───────────────────────────────────────────────┐                                         │
│            │           EXTERNAL CLI (Claude/Gemini/Ollama)  │                                        │
│            └───────────────────────────────────────────────┘                                         │
│                                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
1.2 Deep Verify vs Deep Develop
AspektDeep VerifyDeep DevelopCelSprawdzić istniejąceStworzyć noweInputArtefakt do weryfikacjiProblem/zadanie do wykonaniaOutputRaport z findingsPlan + wykonanie + artefaktyKiedyPo stworzeniu czegośPrzed/podczas tworzeniaPytanie"Czy to jest poprawne?""Jak to zrobić najlepiej?"ZłożonośćJednokrokowa analizaWielokrokowy proces

Część II: Deep Develop
2.1 Czym Jest Deep Develop
Deep Develop to asystent który na podstawie zadania użytkownika:


Część III: Deep Explore
32.1 Czym Jest Deep Develop
Deep Develop to asystent który na podstawie zadania użytkownika:


Analizuje kontekst i wymagania
Planuje najlepsze podejście
Wykonuje pracę (lub prowadzi użytkownika)
Weryfikuje wyniki
Iteruje aż do zakończenia

Nie jest to prosty generator kodu. To inteligentny asystent który rozumie domenę pracy, dobiera metody do złożoności zadania, i adaptuje się do kontekstu projektu.
2.2 Tryby Złożoności
┌─────────────────────────────────────────────────────────────────────────────┐
│  COMPLEXITY MODES                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LIGHT MODE                                                                  │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  Dla: Proste, dobrze zdefiniowane zadania                                  │
│  Czas: Sekundy                                                              │
│  Koszt: Niski (1 wywołanie LLM)                                            │
│                                                                              │
│  Flow:                                                                       │
│  [Zadanie] → [Minimalny kontekst] → [LLM] → [Wynik]                        │
│                                                                              │
│  Metody:                                                                    │
│  • Direct prompting                                                         │
│  • Basic context (aktywny plik)                                            │
│  • No planning phase                                                        │
│                                                                              │
│  Przykłady:                                                                  │
│  • "Napisz funkcję sortującą listę"                                        │
│  • "Popraw ten błąd składni"                                               │
│  • "Dodaj docstring do tej funkcji"                                        │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  MEDIUM MODE                                                                 │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  Dla: Zadania wymagające kontekstu i przemyślenia                          │
│  Czas: 10-60 sekund                                                         │
│  Koszt: Średni (2-5 wywołań LLM)                                           │
│                                                                              │
│  Flow:                                                                       │
│  [Zadanie] → [Zbierz kontekst] → [Analiza] → [Plan] → [Wykonanie] → [Wynik]│
│                                                                              │
│  Metody:                                                                    │
│  • Context gathering (projekt, importy)                                    │
│  • Brief analysis phase                                                     │
│  • Simple planning                                                          │
│  • Pattern matching                                                         │
│  • One-shot execution with review                                          │
│                                                                              │
│  Przykłady:                                                                  │
│  • "Dodaj nowy endpoint do API"                                            │
│  • "Napisz testy dla tego modułu"                                          │
│  • "Zrefaktoryzuj tę funkcję"                                              │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  HEAVY MODE                                                                  │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  Dla: Złożone zadania wymagające głębokiej analizy                        │
│  Czas: Minuty                                                               │
│  Koszt: Wysoki (5-20+ wywołań LLM)                                         │
│                                                                              │
│  Flow:                                                                       │
│  [Zadanie] → [Deep context] → [Multi-angle analysis] → [Options] →        │
│  [Detailed plan] → [Phased execution] → [Verification] → [Iteration]      │
│                                                                              │
│  Metody:                                                                    │
│  • Comprehensive context (cały projekt)                                    │
│  • Multi-perspective analysis                                              │
│  • Trade-off evaluation                                                     │
│  • Detailed step-by-step planning                                          │
│  • Incremental execution with checkpoints                                  │
│  • Self-verification after each step                                       │
│  • Rollback capability                                                      │
│                                                                              │
│  Przykłady:                                                                  │
│  • "Zaprojektuj architekturę mikroserwisów"                               │
│  • "Napisz pełny rozdział dokumentacji"                                   │
│  • "Przeprowadź migrację bazy danych"                                     │
│  • "Zaimplementuj system autentykacji"                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
2.3 Domeny Pracy (Work Domains)
┌─────────────────────────────────────────────────────────────────────────────┐
│  WORK DOMAINS                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Każda domena ma:                                                           │
│  • Specyficzne metody analizy                                              │
│  • Dedykowane prompty                                                       │
│  • Własne patterns                                                          │
│  • Dostosowane UI/output                                                    │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  DOMAIN: CODE                                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Sub-domains:                                                                │
│  • backend — API, services, databases                                      │
│  • frontend — UI, components, state                                        │
│  • data-engineering — pipelines, ETL, Spark                               │
│  • devops — infrastructure, CI/CD, containers                             │
│  • mobile — iOS, Android, React Native                                    │
│                                                                              │
│  Metody:                                                                    │
│  • AST analysis                                                             │
│  • Dependency graph                                                         │
│  • Pattern detection                                                        │
│  • Type inference                                                           │
│  • Test generation                                                          │
│                                                                              │
│  Context sources:                                                           │
│  • Source files                                                             │
│  • Package manifests                                                        │
│  • Config files                                                             │
│  • Existing tests                                                           │
│  • Git history                                                              │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DOMAIN: DOCUMENTATION                                                      │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Sub-domains:                                                                │
│  • technical-docs — architecture, API, guides                             │
│  • user-docs — manuals, tutorials, FAQ                                    │
│  • internal-docs — processes, runbooks                                    │
│                                                                              │
│  Metody:                                                                    │
│  • Structure analysis                                                       │
│  • Terminology extraction                                                   │
│  • Cross-reference checking                                                │
│  • Readability scoring                                                      │
│  • Consistency validation                                                   │
│                                                                              │
│  Context sources:                                                           │
│  • Existing docs                                                            │
│  • Code (for technical docs)                                               │
│  • Style guides                                                             │
│  • Terminology glossaries                                                   │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DOMAIN: BOOK / LONG-FORM WRITING                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Sub-domains:                                                                │
│  • fiction — novels, stories                                               │
│  • non-fiction — textbooks, guides                                        │
│  • technical-book — programming books                                     │
│                                                                              │
│  Metody:                                                                    │
│  • Outline management                                                       │
│  • Character/concept tracking                                              │
│  • Narrative consistency                                                   │
│  • Tone analysis                                                            │
│  • Chapter flow                                                             │
│  • Word count management                                                   │
│                                                                              │
│  Context sources:                                                           │
│  • Previous chapters                                                        │
│  • Character sheets                                                         │
│  • Plot outline                                                             │
│  • Style samples                                                            │
│  • Research notes                                                           │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DOMAIN: API DESIGN                                                         │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Sub-domains:                                                                │
│  • rest-api — RESTful endpoints                                           │
│  • graphql — GraphQL schemas                                              │
│  • grpc — Protocol buffers                                                │
│  • event-driven — Message schemas                                         │
│                                                                              │
│  Metody:                                                                    │
│  • Schema validation                                                        │
│  • Contract analysis                                                        │
│  • Breaking change detection                                               │
│  • Consistency checking                                                     │
│  • SDK generation                                                           │
│                                                                              │
│  Context sources:                                                           │
│  • OpenAPI/Swagger specs                                                   │
│  • Existing endpoints                                                       │
│  • Client implementations                                                   │
│  • API guidelines                                                           │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DOMAIN: DATA                                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Sub-domains:                                                                │
│  • analysis — exploration, visualization                                  │
│  • modeling — ML, statistics                                              │
│  • pipeline — ETL, transformation                                         │
│                                                                              │
│  Metody:                                                                    │
│  • Schema inference                                                         │
│  • Data profiling                                                           │
│  • Query optimization                                                       │
│  • Lineage tracking                                                         │
│                                                                              │
│  Context sources:                                                           │
│  • Data schemas                                                             │
│  • Sample data                                                              │
│  • Existing queries                                                         │
│  • Pipeline definitions                                                     │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DOMAIN: CUSTOM                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Użytkownik może zdefiniować własną domenę z:                              │
│  • Custom methods                                                           │
│  • Custom prompts                                                           │
│  • Custom context sources                                                   │
│  • Custom patterns                                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
2.4 Metody Analizy i Wykonania
┌─────────────────────────────────────────────────────────────────────────────┐
│  METHODS ENGINE                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Metody są dobierane automatycznie na podstawie:                           │
│  • Domeny pracy                                                             │
│  • Trybu złożoności                                                         │
│  • Typu zadania                                                             │
│  • Dostępnego kontekstu                                                     │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  ANALYSIS METHODS                                                           │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  decomposition:                                                              │
│    Rozbija złożone zadanie na mniejsze podzadania.                        │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  context-mapping:                                                           │
│    Identyfikuje relevantne części projektu dla zadania.                   │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: code, documentation                                             │
│                                                                              │
│  pattern-recognition:                                                       │
│    Wykrywa wzorce w istniejącym kodzie/treści.                            │
│    Używane w: wszystkie                                                    │
│    Domeny: code, api                                                       │
│                                                                              │
│  dependency-analysis:                                                       │
│    Mapuje zależności między komponentami.                                 │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: code                                                             │
│                                                                              │
│  impact-analysis:                                                           │
│    Ocenia wpływ zmian na resztę projektu.                                 │
│    Używane w: HEAVY                                                        │
│    Domeny: code, api                                                       │
│                                                                              │
│  trade-off-evaluation:                                                      │
│    Porównuje różne podejścia do rozwiązania.                              │
│    Używane w: HEAVY                                                        │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  consistency-check:                                                         │
│    Sprawdza spójność z istniejącymi elementami.                           │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: documentation, book                                             │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  PLANNING METHODS                                                           │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  outline-first:                                                             │
│    Tworzy outline przed szczegółami.                                      │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: documentation, book                                             │
│                                                                              │
│  interface-first:                                                           │
│    Projektuje interfejsy przed implementacją.                             │
│    Używane w: MEDIUM, HEAVY                                                │
│    Domeny: code, api                                                       │
│                                                                              │
│  test-first:                                                                │
│    Pisze testy przed kodem.                                               │
│    Używane w: HEAVY                                                        │
│    Domeny: code                                                             │
│                                                                              │
│  phased-delivery:                                                           │
│    Dzieli wykonanie na fazy z checkpointami.                              │
│    Używane w: HEAVY                                                        │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  EXECUTION METHODS                                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  direct-generation:                                                         │
│    Bezpośrednie generowanie wyniku.                                       │
│    Używane w: LIGHT                                                        │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  template-based:                                                            │
│    Generowanie na podstawie wykrytych wzorców.                            │
│    Używane w: LIGHT, MEDIUM                                                │
│    Domeny: code, api                                                       │
│                                                                              │
│  incremental-build:                                                         │
│    Budowanie wyniku kawałek po kawałku.                                   │
│    Używane w: HEAVY                                                        │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  self-verification:                                                         │
│    Sprawdzanie wyniku po każdym kroku.                                    │
│    Używane w: HEAVY                                                        │
│    Domeny: code                                                             │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  VERIFICATION METHODS                                                       │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  syntax-check:                                                              │
│    Sprawdzenie poprawności składni.                                       │
│    Domeny: code                                                             │
│                                                                              │
│  type-check:                                                                │
│    Sprawdzenie poprawności typów.                                         │
│    Domeny: code                                                             │
│                                                                              │
│  deep-verify-integration:                                                   │
│    Uruchomienie Deep Verify na wyniku.                                    │
│    Domeny: wszystkie                                                        │
│                                                                              │
│  consistency-verify:                                                        │
│    Sprawdzenie spójności z projektem.                                     │
│    Domeny: wszystkie                                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
2.5 Flow Deep Develop
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP FLOW                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  1. INPUT                                                            │   │
│  │                                                                       │   │
│  │  • Zadanie w naturalnym języku                                       │   │
│  │  • Tryb: light / medium / heavy (lub auto-detect)                   │   │
│  │  • Domena: code / documentation / book / api / custom                │   │
│  │  • Scope: pliki / foldery / projekt                                 │   │
│  │  • Opcje: verify after, interactive, dry-run                        │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  2. TASK ANALYSIS                                                    │   │
│  │                                                                       │   │
│  │  • Klasyfikacja typu zadania                                        │   │
│  │  • Auto-detect złożoności (jeśli nie podano)                        │   │
│  │  • Auto-detect domeny (jeśli nie podano)                            │   │
│  │  • Wybór metod do zastosowania                                      │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  3. CONTEXT GATHERING                                                │   │
│  │                                                                       │   │
│  │  LIGHT: Minimalny (aktywny plik, basic project info)               │   │
│  │  MEDIUM: Rozszerzony (scope + importy + powiązane pliki)           │   │
│  │  HEAVY: Pełny (projekt + historia + external docs)                 │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  4. PLANNING (skip for LIGHT)                                        │   │
│  │                                                                       │   │
│  │  MEDIUM:                                                              │   │
│  │  • Analiza podejść                                                   │   │
│  │  • Prosty plan kroków                                               │   │
│  │                                                                       │   │
│  │  HEAVY:                                                               │   │
│  │  • Głęboka analiza opcji                                            │   │
│  │  • Trade-off evaluation                                             │   │
│  │  • Detailed plan z fazami                                           │   │
│  │  • Risk assessment                                                   │   │
│  │  • USER CHECKPOINT: Akceptacja planu przed wykonaniem               │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  5. EXECUTION                                                        │   │
│  │                                                                       │   │
│  │  LIGHT:                                                               │   │
│  │  • Jedno wywołanie LLM → wynik                                      │   │
│  │                                                                       │   │
│  │  MEDIUM:                                                              │   │
│  │  • Wykonanie planu krok po kroku                                    │   │
│  │  • Łączenie wyników                                                  │   │
│  │                                                                       │   │
│  │  HEAVY:                                                               │   │
│  │  • Wykonanie faza po fazie                                          │   │
│  │  • Verification po każdej fazie                                     │   │
│  │  • USER CHECKPOINT opcjonalnie między fazami                        │   │
│  │  • Rollback jeśli faza fail                                         │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  6. VERIFICATION                                                     │   │
│  │                                                                       │   │
│  │  • Syntax/type check (dla kodu)                                     │   │
│  │  • Deep Verify integration                                          │   │
│  │  • Consistency check                                                 │   │
│  │  • Output formatting                                                 │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  7. PRESENTATION                                                     │   │
│  │                                                                       │   │
│  │  • Wyświetlenie wyników w panelu                                    │   │
│  │  • Opcje: Apply, Copy, Edit, Iterate                               │   │
│  │  • Jeśli verification failed → opcja auto-fix                      │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  8. ITERATION (optional)                                             │   │
│  │                                                                       │   │
│  │  • User feedback / follow-up                                        │   │
│  │  • Refinement loop                                                   │   │
│  │  • Additional requests                                               │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
2.6 Konfiguracja Domeny
json// .deepverify/config.json
{
  "develop": {
    "domain": "code",
    "subDomain": "data-engineering",
    
    "defaultMode": "medium",
    "autoDetectMode": true,
    
    "methods": {
      "analysis": ["decomposition", "context-mapping", "pattern-recognition"],
      "planning": ["interface-first"],
      "execution": ["template-based", "incremental-build"],
      "verification": ["syntax-check", "deep-verify-integration"]
    },
    
    "modeOverrides": {
      "light": {
        "methods": {
          "analysis": [],
          "planning": [],
          "execution": ["direct-generation"]
        }
      },
      "heavy": {
        "methods": {
          "analysis": ["decomposition", "context-mapping", "dependency-analysis", "impact-analysis", "trade-off-evaluation"],
          "planning": ["interface-first", "test-first", "phased-delivery"],
          "execution": ["incremental-build", "self-verification"],
          "verification": ["syntax-check", "type-check", "deep-verify-integration", "consistency-verify"]
        },
        "requirePlanApproval": true,
        "checkpointsBetweenPhases": true
      }
    },
    
    "contextSources": {
      "light": ["active-file"],
      "medium": ["scope", "imports", "related-files", "config"],
      "heavy": ["project", "git-history", "documentation", "external-refs"]
    }
  }
}
2.7 Konfiguracja Domeny: Book
json// .deepverify/config.json (dla projektu książki)
{
  "develop": {
    "domain": "book",
    "subDomain": "technical-book",
    
    "bookConfig": {
      "structure": {
        "outlineFile": "OUTLINE.md",
        "chaptersDir": "chapters/",
        "charactersFile": null,
        "glossaryFile": "GLOSSARY.md",
        "styleGuide": "STYLE.md"
      },
      
      "consistency": {
        "trackTerminology": true,
        "trackCharacters": false,
        "trackReferences": true,
        "crossReferenceChapters": true
      },
      
      "targets": {
        "averageChapterLength": 5000,
        "maxSectionLength": 1500,
        "targetAudience": "intermediate developers"
      }
    },
    
    "methods": {
      "analysis": ["outline-analysis", "terminology-extraction", "cross-reference-check"],
      "planning": ["outline-first", "chapter-flow"],
      "execution": ["incremental-build", "consistency-maintain"],
      "verification": ["consistency-verify", "readability-check", "terminology-verify"]
    }
  }
}

Część III: Wspólne API i Interfejsy
3.1 Extension API
typescript// src/api/index.ts

/**
 * Deep Verify/Develop Extension API
 * 
 * Dostępne dla innych wtyczek VS Code po aktywacji
 */
export interface DeepExtensionAPI {
  
  // ═══════════════════════════════════════════════════════════════════════
  // DEEP VERIFY API
  // ═══════════════════════════════════════════════════════════════════════
  
  verify: {
    /**
     * Weryfikuje tekst/kod
     */
    verifyText(text: string, options?: VerifyOptions): Promise<VerifyResult>;
    
    /**
     * Weryfikuje plik
     */
    verifyFile(filePath: string, options?: VerifyOptions): Promise<VerifyResult>;
    
    /**
     * Weryfikuje wiele plików
     */
    verifyFiles(filePaths: string[], options?: VerifyOptions): Promise<VerifyResult>;
    
    /**
     * Weryfikuje folder
     */
    verifyFolder(folderPath: string, options?: VerifyFolderOptions): Promise<VerifyResult>;
    
    /**
     * Weryfikuje zmiany git
     */
    verifyGitChanges(options?: VerifyGitOptions): Promise<VerifyResult>;
    
    /**
     * Porównuje dokumentację z kodem
     */
    compareDocWithCode(docPath: string, codePaths: string[]): Promise<CompareResult>;
  };
  
  // ═══════════════════════════════════════════════════════════════════════
  // DEEP DEVELOP API
  // ═══════════════════════════════════════════════════════════════════════
  
  develop: {
    /**
     * Wykonuje zadanie
     */
    execute(task: string, options?: DevelopOptions): Promise<DevelopResult>;
    
    /**
     * Wykonuje z planem (MEDIUM/HEAVY)
     */
    executeWithPlan(task: string, options?: DevelopOptions): Promise<DevelopPlanResult>;
    
    /**
     * Tylko planowanie bez wykonania
     */
    plan(task: string, options?: DevelopOptions): Promise<DevelopPlan>;
    
    /**
     * Wykonuje istniejący plan
     */
    executePlan(plan: DevelopPlan): Promise<DevelopResult>;
    
    /**
     * Kontynuuje/iteruje poprzedni wynik
     */
    continue(previousResult: DevelopResult, followUp: string): Promise<DevelopResult>;
  };
  
  // ═══════════════════════════════════════════════════════════════════════
  // SHARED API
  // ═══════════════════════════════════════════════════════════════════════
  
  /**
   * Konfiguracja
   */
  config: {
    getConfig(): DeepConfig;
    setConfig(config: Partial<DeepConfig>): void;
    getProjectConfig(): ProjectConfig | null;
  };
  
  /**
   * CLI providers
   */
  cli: {
    getAvailableProviders(): CLIProvider[];
    getCurrentProvider(): CLIProvider;
    setProvider(name: string): void;
  };
  
  /**
   * Patterns
   */
  patterns: {
    getPatterns(domain?: string): Pattern[];
    addPattern(pattern: Pattern): void;
    disablePattern(patternId: string): void;
  };
  
  /**
   * Events
   */
  onVerifyComplete: Event<VerifyResult>;
  onDevelopComplete: Event<DevelopResult>;
  onError: Event<DeepError>;
}

// ═══════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════

interface VerifyOptions {
  provider?: string;
  patterns?: string[];
  contextLevel?: 'minimal' | 'file' | 'project';
  timeout?: number;
}

interface DevelopOptions {
  mode?: 'light' | 'medium' | 'heavy' | 'auto';
  domain?: WorkDomain;
  scope?: ScopeDefinition;
  interactive?: boolean;
  dryRun?: boolean;
  verifyAfter?: boolean;
  provider?: string;
}

interface WorkDomain {
  type: 'code' | 'documentation' | 'book' | 'api' | 'data' | 'custom';
  subType?: string;
  config?: Record<string, any>;
}

interface ScopeDefinition {
  type: 'file' | 'files' | 'folder' | 'glob' | 'project';
  paths?: string[];
  pattern?: string;
  recursive?: boolean;
}

interface VerifyResult {
  success: boolean;
  findings: Finding[];
  summary: string;
  metadata: {
    duration: number;
    provider: string;
    filesAnalyzed: number;
  };
}

interface DevelopResult {
  success: boolean;
  plan?: DevelopPlan;
  outputs: DevelopOutput[];
  verification?: VerifyResult;
  metadata: {
    duration: number;
    provider: string;
    mode: string;
    methodsUsed: string[];
  };
}

interface DevelopOutput {
  type: 'create' | 'modify' | 'delete' | 'info';
  path?: string;
  content?: string;
  diff?: string;
  description: string;
}

interface DevelopPlan {
  summary: string;
  approach: string;
  phases: PlanPhase[];
  risks?: string[];
  alternatives?: string[];
}

interface PlanPhase {
  name: string;
  description: string;
  steps: PlanStep[];
  estimatedDuration?: string;
  checkpoint?: boolean;
}

interface PlanStep {
  id: string;
  action: string;
  target?: string;
  dependencies?: string[];
}
3.2 Użycie API z Innej Wtyczki
typescript// Inna wtyczka VS Code używająca Deep Verify/Develop

import * as vscode from 'vscode';

interface DeepExtensionAPI {
  verify: { /* ... */ };
  develop: { /* ... */ };
  // ...
}

export async function activate(context: vscode.ExtensionContext) {
  
  // Pobierz API Deep Verify/Develop
  const deepExtension = vscode.extensions.getExtension('your-publisher.deep-verify');
  
  if (!deepExtension) {
    vscode.window.showWarningMessage('Deep Verify extension not installed');
    return;
  }
  
  // Aktywuj jeśli nie aktywne
  const api: DeepExtensionAPI = await deepExtension.activate();
  
  // ═══════════════════════════════════════════════════════════════════════
  // PRZYKŁAD: Weryfikacja po zapisie pliku
  // ═══════════════════════════════════════════════════════════════════════
  
  vscode.workspace.onDidSaveTextDocument(async (document) => {
    if (document.languageId === 'python') {
      const result = await api.verify.verifyFile(document.uri.fsPath, {
        contextLevel: 'file'
      });
      
      if (result.findings.some(f => f.severity === 'critical')) {
        vscode.window.showWarningMessage(
          `Deep Verify found ${result.findings.length} issues`
        );
      }
    }
  });
  
  // ═══════════════════════════════════════════════════════════════════════
  // PRZYKŁAD: Generowanie kodu przez Deep Develop
  // ═══════════════════════════════════════════════════════════════════════
  
  const generateCommand = vscode.commands.registerCommand(
    'myExtension.generateWithDeep',
    async () => {
      const task = await vscode.window.showInputBox({
        prompt: 'What do you want to create?'
      });
      
      if (!task) return;
      
      const result = await api.develop.execute(task, {
        mode: 'medium',
        domain: { type: 'code', subType: 'backend' },
        verifyAfter: true
      });
      
      // Pokaż wyniki
      if (result.success) {
        for (const output of result.outputs) {
          if (output.type === 'create' && output.path && output.content) {
            // Utwórz plik
            const uri = vscode.Uri.file(output.path);
            await vscode.workspace.fs.writeFile(uri, Buffer.from(output.content));
          }
        }
      }
    }
  );
  
  context.subscriptions.push(generateCommand);
  
  // ═══════════════════════════════════════════════════════════════════════
  // PRZYKŁAD: Nasłuchiwanie na events
  // ═══════════════════════════════════════════════════════════════════════
  
  api.onVerifyComplete((result) => {
    console.log('Verification completed:', result.summary);
  });
  
  api.onDevelopComplete((result) => {
    console.log('Development completed:', result.metadata.methodsUsed);
  });
}
3.3 Commands (Command Palette + Programmatic)
typescript// src/commands/registry.ts

/**
 * Wszystkie komendy są wywoływalne przez:
 * 1. Command Palette (Ctrl+Shift+P)
 * 2. Skróty klawiszowe
 * 3. Menu kontekstowe
 * 4. Programatycznie: vscode.commands.executeCommand()
 * 5. CLI bridge
 */

export const COMMANDS = {
  
  // ═══════════════════════════════════════════════════════════════════════
  // DEEP VERIFY COMMANDS
  // ═══════════════════════════════════════════════════════════════════════
  
  // Podstawowe
  'deepVerify.verifySelection': {
    title: 'Deep Verify: Verify Selection',
    handler: verifySelectionHandler,
    args: [] // brak argumentów = użyj aktualnego zaznaczenia
  },
  
  'deepVerify.verifyFile': {
    title: 'Deep Verify: Verify File',
    handler: verifyFileHandler,
    args: ['filePath?'] // opcjonalny, domyślnie aktywny plik
  },
  
  'deepVerify.verifyFileWithContext': {
    title: 'Deep Verify: Verify File with Project Context',
    handler: verifyFileWithContextHandler,
    args: ['filePath?']
  },
  
  'deepVerify.verifyFolder': {
    title: 'Deep Verify: Verify Folder',
    handler: verifyFolderHandler,
    args: ['folderPath?', 'recursive?']
  },
  
  'deepVerify.verifyGitChanges': {
    title: 'Deep Verify: Verify Uncommitted Changes',
    handler: verifyGitChangesHandler,
    args: ['staged?'] // true = tylko staged
  },
  
  'deepVerify.compareDocCode': {
    title: 'Deep Verify: Compare Documentation with Code',
    handler: compareDocCodeHandler,
    args: ['docPath?', 'codePaths?']
  },
  
  'deepVerify.customPrompt': {
    title: 'Deep Verify: Custom Verification',
    handler: customPromptHandler,
    args: ['prompt?', 'target?']
  },
  
  // ═══════════════════════════════════════════════════════════════════════
  // DEEP DEVELOP COMMANDS
  // ═══════════════════════════════════════════════════════════════════════
  
  'deepDevelop.quick': {
    title: 'Deep Develop: Quick (Light Mode)',
    handler: developQuickHandler,
    args: ['task?']
  },
  
  'deepDevelop.standard': {
    title: 'Deep Develop: Standard (Medium Mode)',
    handler: developStandardHandler,
    args: ['task?', 'scope?']
  },
  
  'deepDevelop.deep': {
    title: 'Deep Develop: Deep (Heavy Mode)',
    handler: developDeepHandler,
    args: ['task?', 'scope?']
  },
  
  'deepDevelop.auto': {
    title: 'Deep Develop: Auto (Detect Complexity)',
    handler: developAutoHandler,
    args: ['task?', 'scope?']
  },
  
  'deepDevelop.inContext': {
    title: 'Deep Develop: In This Context',
    handler: developInContextHandler,
    args: ['task?'] // kontekst = aktualne zaznaczenie
  },
  
  'deepDevelop.planOnly': {
    title: 'Deep Develop: Create Plan Only',
    handler: developPlanOnlyHandler,
    args: ['task?', 'scope?']
  },
  
  'deepDevelop.executePlan': {
    title: 'Deep Develop: Execute Saved Plan',
    handler: executePlanHandler,
    args: ['planId?']
  },
  
  'deepDevelop.continue': {
    title: 'Deep Develop: Continue Previous',
    handler: developContinueHandler,
    args: ['followUp?']
  },
  
  // Specjalizowane
  'deepDevelop.generateTests': {
    title: 'Deep Develop: Generate Tests',
    handler: generateTestsHandler,
    args: ['target?']
  },
  
  'deepDevelop.generateDocs': {
    title: 'Deep Develop: Generate Documentation',
    handler: generateDocsHandler,
    args: ['target?']
  },
  
  'deepDevelop.refactor': {
    title: 'Deep Develop: Refactor',
    handler: refactorHandler,
    args: ['target?', 'goal?']
  },
  
  'deepDevelop.fixError': {
    title: 'Deep Develop: Fix This Error',
    handler: fixErrorHandler,
    args: ['errorMessage?', 'filePath?']
  },
  
  // ═══════════════════════════════════════════════════════════════════════
  // CONFIGURATION COMMANDS
  // ═══════════════════════════════════════════════════════════════════════
  
  'deep.selectProvider': {
    title: 'Deep: Select AI Provider',
    handler: selectProviderHandler,
    args: []
  },
  
  'deep.initProject': {
    title: 'Deep: Initialize Project Configuration',
    handler: initProjectHandler,
    args: ['domain?']
  },
  
  'deep.openConfig': {
    title: 'Deep: Open Configuration',
    handler: openConfigHandler,
    args: []
  },
  
  'deep.managePatterns': {
    title: 'Deep: Manage Patterns',
    handler: managePatternsHandler,
    args: []
  }
};

// ═══════════════════════════════════════════════════════════════════════
// WYWOŁANIE PROGRAMATYCZNE Z ARGUMENTAMI
// ═══════════════════════════════════════════════════════════════════════

// Przykład z innej wtyczki lub skryptu:
// 
// vscode.commands.executeCommand('deepVerify.verifyFile', '/path/to/file.py');
// 
// vscode.commands.executeCommand('deepDevelop.standard', 
//   'Add caching to this function',
//   { type: 'file', paths: ['/path/to/file.py'] }
// );
```

### 3.4 CLI Bridge
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CLI BRIDGE ARCHITECTURE                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Problem:                                                                    │
│  Chcemy uruchamiać Deep Verify/Develop z terminala lub skryptów,           │
│  ale wtyczka VS Code wymaga działającej instancji VS Code.                 │
│                                                                              │
│  Rozwiązanie: Dwa tryby                                                     │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  MODE 1: VS CODE COMMAND LINE                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Wymaga: Otwarte VS Code z workspace                                       │
│                                                                              │
│  $ code --command "deepVerify.verifyFile" --args "/path/to/file.py"        │
│  $ code --command "deepDevelop.quick" --args "Add logging"                 │
│                                                                              │
│  Ograniczenia:                                                              │
│  • VS Code musi być uruchomione                                            │
│  • Workspace musi być otwarty                                               │
│  • Wynik tylko w VS Code UI                                                │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  MODE 2: STANDALONE CLI (Osobny pakiet)                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Osobne CLI które używa tego samego core engine co wtyczka.               │
│  Może działać bez VS Code (headless).                                      │
│                                                                              │
│  $ npx deep-verify verify src/main.py                                      │
│  $ npx deep-verify develop "Add caching" --scope src/services/            │
│                                                                              │
│  Pełne możliwości:                                                         │
│  • Headless execution                                                       │
│  • CI/CD integration                                                        │
│  • JSON output                                                              │
│  • Exit codes                                                               │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  MODE 3: IPC BRIDGE (Zaawansowane)                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Wtyczka startuje lokalny server (socket/HTTP).                           │
│  CLI łączy się do tego servera.                                           │
│  Pozwala na pełną komunikację między CLI a działającą wtyczką.            │
│                                                                              │
│  ┌──────────┐         ┌─────────────────────────────────┐                  │
│  │   CLI    │ ──IPC── │  VS Code Extension (server)     │                  │
│  └──────────┘         └─────────────────────────────────┘                  │
│                                                                              │
│  $ dv verify src/main.py --connect                                         │
│  # Łączy się do działającej instancji VS Code                             │
│  # Używa jej contextu, konfiguracji, otwartych plików                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.5 Standalone CLI Specification
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STANDALONE CLI: deep-verify                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INSTALLATION:                                                              │
│  $ npm install -g @anthropic/deep-verify-cli                               │
│  # lub                                                                       │
│  $ npx @anthropic/deep-verify-cli                                          │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  VERIFY COMMANDS:                                                           │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  # Weryfikuj plik                                                           │
│  $ dv verify <file>                                                         │
│  $ dv verify src/main.py                                                   │
│  $ dv verify src/main.py --context project                                 │
│                                                                              │
│  # Weryfikuj wiele plików                                                   │
│  $ dv verify src/*.py                                                      │
│  $ dv verify src/api/ --recursive                                          │
│                                                                              │
│  # Weryfikuj git changes                                                    │
│  $ dv verify --git                                                         │
│  $ dv verify --git-staged                                                  │
│                                                                              │
│  # Porównaj doc z kodem                                                     │
│  $ dv compare README.md src/main.py                                        │
│                                                                              │
│  # Custom prompt                                                            │
│  $ dv verify src/main.py --prompt "Check for security issues"             │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  DEVELOP COMMANDS:                                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  # Quick (light mode)                                                       │
│  $ dv develop "Add error handling" --mode light                            │
│  $ dv develop "Add error handling" src/main.py                             │
│                                                                              │
│  # Standard (medium mode)                                                   │
│  $ dv develop "Add caching layer" --scope src/services/                   │
│                                                                              │
│  # Deep (heavy mode)                                                        │
│  $ dv develop "Implement authentication system" --mode heavy              │
│                                                                              │
│  # Plan only                                                                │
│  $ dv develop "Refactor to microservices" --plan-only                     │
│  $ dv develop --execute-plan plan-123.json                                │
│                                                                              │
│  # Domain-specific                                                          │
│  $ dv develop "Write chapter 3" --domain book --scope chapters/           │
│  $ dv develop "Create user endpoint" --domain api                         │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  GLOBAL OPTIONS:                                                            │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  --provider, -p      AI provider (claude, gemini, ollama)                  │
│  --config, -c        Config file path                                      │
│  --output, -o        Output format (text, json, markdown)                  │
│  --quiet, -q         Minimal output                                        │
│  --verbose, -v       Detailed output                                       │
│  --dry-run           Don't write files                                     │
│  --yes, -y           Auto-confirm prompts                                  │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  OUTPUT FORMATS:                                                            │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  # Human-readable (default)                                                 │
│  $ dv verify src/main.py                                                   │
│                                                                              │
│  # JSON (for CI/CD, scripting)                                             │
│  $ dv verify src/main.py --output json                                     │
│  {                                                                           │
│    "success": true,                                                         │
│    "findings": [...],                                                       │
│    "summary": "..."                                                         │
│  }                                                                           │
│                                                                              │
│  # Exit codes                                                               │
│  # 0 = success / no issues                                                 │
│  # 1 = critical issues found                                               │
│  # 2 = warnings found                                                       │
│  # 3 = error                                                                │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  CI/CD EXAMPLE:                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  # GitHub Actions                                                           │
│  - name: Deep Verify                                                        │
│    run: |                                                                   │
│      npx @anthropic/deep-verify-cli verify src/ \                         │
│        --recursive \                                                        │
│        --output json \                                                      │
│        --provider claude \                                                 │
│        > verify-results.json                                               │
│                                                                              │
│  - name: Check results                                                      │
│    run: |                                                                   │
│      if [ $(jq '.findings | map(select(.severity == "critical")) | length' verify-results.json) -gt 0 ]; then│
│        echo "Critical issues found!"                                       │
│        exit 1                                                               │
│      fi                                                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Część IV: Interfejs Użytkownika

### 4.1 Panel Główny Deep Develop
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP                                                    [×]        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  What do you want to create?                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Add a Redis caching layer to the user service with TTL support and  │   │
│  │ cache invalidation on user update                                    │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  MODE                                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ○ Light   — Quick, single-step generation                          │   │
│  │  ● Medium  — Analysis + planning + execution                        │   │
│  │  ○ Heavy   — Deep analysis, phased execution, verification          │   │
│  │  ○ Auto    — Let Deep Develop decide                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  DOMAIN                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ● Code        ○ Documentation   ○ Book                             │   │
│  │  ○ API Design  ○ Data           ○ Custom                           │   │
│  │                                                                       │   │
│  │  Sub-domain: [data-engineering ▼]                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  SCOPE                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ○ Current file only                                                │   │
│  │  ○ Current file + imports                                           │   │
│  │  ● Folder: src/services/user/                        [Browse...]   │   │
│  │  ○ Selected files                                    [Select...]   │   │
│  │  ○ Entire project                                                   │   │
│  │  ○ Git changed files                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  OPTIONS                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ☑ Verify result after completion                                   │   │
│  │  ☐ Interactive mode (confirm each step)                            │   │
│  │  ☐ Dry run (show changes without applying)                         │   │
│  │  ☐ Generate tests                                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  PROVIDER: [Claude ▼]                                                      │
│                                                                              │
│                                     [Cancel]  [Plan Only]  [Execute]       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Panel Wyników Deep Develop (Heavy Mode)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP RESULTS                                   [Claude] 2m 34s    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ✓ TASK COMPLETED                                                          │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  Add Redis caching layer to user service                                   │
│                                                                              │
│  ANALYSIS SUMMARY                                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  I analyzed your project and found:                                        │
│  • Existing Redis connection in src/config/redis.py                       │
│  • Caching pattern already used in src/services/product/cache.py         │
│  • User service has 3 functions that would benefit from caching           │
│                                                                              │
│  I followed your existing caching pattern for consistency.                 │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  EXECUTION PLAN                                                   ✓ Done   │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Phase 1: Setup cache utilities                            ✓ Completed    │
│  ├── Create src/services/user/cache.py                     ✓              │
│  └── Add cache key generators                              ✓              │
│                                                                              │
│  Phase 2: Modify user repository                           ✓ Completed    │
│  ├── Add caching to get_user()                            ✓              │
│  ├── Add caching to get_user_by_email()                   ✓              │
│  └── Add cache invalidation to update_user()              ✓              │
│                                                                              │
│  Phase 3: Add tests                                        ✓ Completed    │
│  └── Create tests/services/user/test_cache.py             ✓              │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  CHANGES                                                                    │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  📄 CREATE: src/services/user/cache.py                     [View] [Diff]   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  """User service cache utilities."""                                 │   │
│  │  from src.config.redis import redis_client                          │   │
│  │  from src.services.user.types import UserData                       │   │
│  │                                                                       │   │
│  │  CACHE_TTL = 300  # 5 minutes                                       │   │
│  │                                                                       │   │
│  │  def cache_key(user_id: str) -> str:                                │   │
│  │      return f"user:{user_id}"                                       │   │
│  │  ...                                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  📝 MODIFY: src/services/user/repository.py                [View] [Diff]   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  @@ -1,5 +1,7 @@                                                    │   │
│  │  +from src.services.user.cache import (                             │   │
│  │  +    cache_key, CACHE_TTL, get_cached, set_cached, invalidate     │   │
│  │  +)                                                                  │   │
│  │                                                                       │   │
│  │  @@ -23,8 +25,18 @@                                                 │   │
│  │   def get_user(user_id: str) -> UserData:                           │   │
│  │  +    # Try cache first                                             │   │
│  │  +    cached = get_cached(cache_key(user_id))                       │   │
│  │  +    if cached:                                                     │   │
│  │  +        return cached                                              │   │
│  │  ...                                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  📄 CREATE: tests/services/user/test_cache.py              [View] [Diff]   │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  VERIFICATION                                                   ✓ Passed   │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Deep Verify found no issues in generated code.                            │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  METHODS USED                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Analysis: context-mapping, pattern-recognition, dependency-analysis       │
│  Planning: interface-first, phased-delivery                                │
│  Execution: template-based, incremental-build, self-verification          │
│  Verification: syntax-check, deep-verify-integration                      │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  [Apply All]  [Apply Selected]  [Export]  [Continue...]  [New Task]       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Panel dla Domeny: Book
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP DEVELOP: BOOK MODE                                    [Claude] 45s   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ✓ CHAPTER GENERATED                                                       │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  Chapter 5: Advanced Caching Patterns                                      │
│                                                                              │
│  CONTEXT USED                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  📖 Previous chapters analyzed for:                                        │
│  • Terminology consistency (42 terms tracked)                              │
│  • Code example style (Python with type hints)                            │
│  • Tone (technical but accessible)                                        │
│  • Cross-references                                                         │
│                                                                              │
│  📋 Outline followed: OUTLINE.md section 5                                │
│  📝 Style guide: STYLE.md                                                  │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  GENERATED CONTENT                                                         │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  📄 chapters/05-advanced-caching.md                                        │
│  Word count: 4,823 (target: 5,000 ± 500) ✓                                │
│                                                                              │
│  ## Chapter 5: Advanced Caching Patterns                                   │
│                                                                              │
│  In the previous chapter, we explored basic caching strategies...         │
│  [Preview - click to expand full content]                                  │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  CONSISTENCY CHECK                                                 ✓ Pass  │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  ✓ All code examples follow project style                                 │
│  ✓ Terminology matches glossary                                           │
│  ✓ References to previous chapters are valid                              │
│  ✓ Tone consistent with other chapters                                    │
│                                                                              │
│  ⚠️ Note: Consider adding cross-reference to Chapter 3 section on Redis   │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  [Apply]  [Edit in Editor]  [Regenerate Section...]  [Continue to Ch.6]   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.4 Sidebar
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEEP                                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  QUICK ACTIONS                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│  [▶ Verify Selection]          Ctrl+Shift+V                                │
│  [▶ Verify File]                                                            │
│  [💡 Quick Develop]             Ctrl+Shift+D                                │
│  [💡 Develop in Scope...]                                                   │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  CURRENT SESSION                                                            │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  💡 "Add caching to user service"                          [Continue]      │
│     Status: Completed ✓                                                    │
│     Mode: Medium | Domain: Code                                            │
│     3 files changed                                                         │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  RECENT                                                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  ✓ Verify: pipeline.py — clean — 1h ago                                   │
│  💡 Develop: "Add logging" — done — 2h ago               [Re-open]        │
│  ⚠ Verify: api/routes.py — 2 warnings — 3h ago          [Details]        │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  CONFIGURATION                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Provider: Claude ✓                                        [Change]        │
│  Domain: Code (data-engineering)                           [Change]        │
│  Project config: .deepverify/config.json                  [Edit]          │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  PATTERNS                                                                   │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Enabled: 47 patterns                                      [Manage]        │
│  • python-core (12)                                                         │
│  • spark-patterns (15)                                                      │
│  • project-custom (8)                                                       │
│  • ...                                                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

Część V: Konfiguracja Kompletna
5.1 Plik Konfiguracyjny Projektu
json// .deepverify/config.json

{
  "$schema": "https://deep-verify.dev/schemas/config.json",
  "version": "1.0",

  // ═══════════════════════════════════════════════════════════════════════
  // PROJECT INFO
  // ═══════════════════════════════════════════════════════════════════════
  
  "project": {
    "name": "My Data Platform",
    "type": "data-engineering",
    "languages": ["python", "sql"],
    "frameworks": ["spark", "databricks", "delta", "airflow"]
  },

  // ═══════════════════════════════════════════════════════════════════════
  // CLI PROVIDERS
  // ═══════════════════════════════════════════════════════════════════════
  
  "cli": {
    "default": "claude",
    "providers": {
      "claude": {
        "enabled": true,
        "command": "claude",
        "timeout": 120
      },
      "gemini": {
        "enabled": true,
        "command": "gemini",
        "timeout": 120
      },
      "ollama": {
        "enabled": false,
        "command": "ollama run codellama",
        "timeout": 300
      }
    },
    "custom": []
  },

  // ═══════════════════════════════════════════════════════════════════════
  // DEEP VERIFY CONFIG
  // ═══════════════════════════════════════════════════════════════════════
  
  "verify": {
    "defaultContextLevel": "file-with-imports",
    
    "patterns": {
      "enabled": true,
      "useGlobal": true,
      "useProject": true,
      "files": [
        "patterns/spark.yaml",
        "patterns/security.yaml"
      ],
      "disabled": ["style-nitpicks"]
    },
    
    "autoTriggers": {
      "onSave": false,
      "onPreCommit": true,
      "onPrePush": false
    },
    
    "severity": {
      "failThreshold": "critical",
      "warnThreshold": "warning"
    },
    
    "documentation": {
      "mappingFile": "doc-mapping.json",
      "autoDetect": true
    }
  },

  // ═══════════════════════════════════════════════════════════════════════
  // DEEP DEVELOP CONFIG
  // ═══════════════════════════════════════════════════════════════════════
  
  "develop": {
    "domain": {
      "type": "code",
      "subType": "data-engineering"
    },
    
    "defaultMode": "medium",
    "autoDetectMode": true,
    
    "modes": {
      "light": {
        "contextSources": ["active-file"],
        "methods": {
          "analysis": [],
          "planning": [],
          "execution": ["direct-generation"],
          "verification": []
        },
        "verifyAfter": false
      },
      
      "medium": {
        "contextSources": ["scope", "imports", "related-files", "config"],
        "methods": {
          "analysis": ["decomposition", "context-mapping", "pattern-recognition"],
          "planning": ["interface-first"],
          "execution": ["template-based", "incremental-build"],
          "verification": ["syntax-check"]
        },
        "verifyAfter": true
      },
      
      "heavy": {
        "contextSources": ["project", "git-history", "documentation"],
        "methods": {
          "analysis": ["decomposition", "context-mapping", "dependency-analysis", "impact-analysis", "trade-off-evaluation"],
          "planning": ["interface-first", "test-first", "phased-delivery"],
          "execution": ["incremental-build", "self-verification"],
          "verification": ["syntax-check", "type-check", "deep-verify-integration", "consistency-verify"]
        },
        "verifyAfter": true,
        "requirePlanApproval": true,
        "checkpointsBetweenPhases": true
      }
    },
    
    "context": {
      "maxSize": "200KB",
      "alwaysInclude": [
        "src/config/settings.py",
        "src/utils/spark_utils.py"
      ],
      "exclude": [
        "**/*.test.py",
        "**/fixtures/**",
        "legacy/**"
      ]
    },
    
    "scopePresets": {
      "api": {
        "include": ["src/api/**"],
        "alwaysAdd": ["src/types/api.py", "src/middleware/*.py"]
      },
      "pipelines": {
        "include": ["src/pipelines/**"],
        "alwaysAdd": ["src/config/spark.py", "src/utils/delta.py"]
      }
    },
    
    "savedPrompts": {
      "new-pipeline": "Create a new Spark pipeline for {description} following project patterns",
      "add-tests": "Add comprehensive tests for {target} following existing test patterns"
    }
  },

  // ═══════════════════════════════════════════════════════════════════════
  // DOMAIN-SPECIFIC: BOOK (example for different project)
  // ═══════════════════════════════════════════════════════════════════════
  
  "bookConfig": {
    "structure": {
      "outlineFile": "OUTLINE.md",
      "chaptersDir": "chapters/",
      "glossaryFile": "GLOSSARY.md",
      "styleGuide": "STYLE.md"
    },
    "targets": {
      "averageChapterLength": 5000,
      "targetAudience": "intermediate developers"
    },
    "consistency": {
      "trackTerminology": true,
      "crossReferenceChapters": true
    }
  },

  // ═══════════════════════════════════════════════════════════════════════
  // UI PREFERENCES
  // ═══════════════════════════════════════════════════════════════════════
  
  "ui": {
    "showInlineDecorations": true,
    "panelPosition": "bottom",
    "autoShowResults": true
  },

  // ═══════════════════════════════════════════════════════════════════════
  // API / INTEGRATION
  // ═══════════════════════════════════════════════════════════════════════
  
  "api": {
    "enableExtensionAPI": true,
    "enableIPCBridge": false,
    "bridgePort": 9876
  }
}
```

### 5.2 Hierarchia Konfiguracji
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONFIGURATION HIERARCHY                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PRIORITY (highest to lowest):                                              │
│                                                                              │
│  1. Command arguments                                                       │
│     └── --mode heavy --provider gemini                                     │
│                                                                              │
│  2. Project config                                                          │
│     └── .deepverify/config.json                                            │
│                                                                              │
│  3. Workspace settings                                                      │
│     └── .vscode/settings.json → "deepVerify.*"                             │
│                                                                              │
│  4. Global user config                                                      │
│     └── ~/.deepverify/config.json                                          │
│                                                                              │
│  5. Extension defaults                                                      │
│     └── Built into extension                                               │
│                                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│  PATTERNS merge (nie nadpisują):                                           │
│                                                                              │
│  builtin + global-user + project = all enabled                            │
│                                                                              │
│  Project może tylko DISABLE patterns z wyższych poziomów.                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Część VI: Przykłady Użycia

### 6.1 Scenariusz: Data Engineer - Nowy Pipeline
```
# 1. Użytkownik otwiera projekt Databricks w VS Code

# 2. Ctrl+Shift+D → Deep Develop Quick Input
   "Create a new Spark pipeline that reads from Delta table 'sales',
    aggregates by region and month, and writes to 'sales_summary'"

# 3. Wtyczka auto-detects:
   - Mode: MEDIUM (złożoność wymaga planu)
   - Domain: code/data-engineering (wykryte z projektu)
   - Scope: src/pipelines/ (suggested based on task)

# 4. Execution:
   
   ANALYSIS:
   - Found existing pipeline pattern in src/pipelines/orders/
   - Found Delta utilities in src/utils/delta.py
   - Found config pattern in src/config/tables.py
   
   PLAN:
   1. Create pipeline skeleton from template
   2. Add read logic from sales table
   3. Add aggregation transformations
   4. Add write logic to sales_summary
   5. Add config entry
   
   EXECUTION:
   - Creates src/pipelines/sales/pipeline.py
   - Creates src/pipelines/sales/transformations.py
   - Modifies src/config/tables.py
   
   VERIFICATION:
   - Runs Deep Verify → no issues
   - Syntax check → pass

# 5. Output panel shows changes, user clicks [Apply All]

# 6. Files created, user can run and test
```

### 6.2 Scenariusz: Technical Writer - Chapter
```
# 1. Użytkownik ma projekt książki technicznej

# 2. Deep Develop: "Write Chapter 7: Testing Spark Applications"

# 3. Wtyczka:
   - Mode: HEAVY (chapter to dużo contentu)
   - Domain: book/technical-book
   - Scope: chapters/, OUTLINE.md, poprzednie rozdziały

# 4. Execution:
   
   CONTEXT GATHERING:
   - Reads OUTLINE.md for Chapter 7 requirements
   - Analyzes chapters 1-6 for:
     - Terminology (extracts 87 terms)
     - Code style (Python with type hints, pytest)
     - Tone (technical but accessible)
     - Structure (intro → concepts → examples → summary)
   
   PLANNING (pokazany użytkownikowi):
   
   Chapter 7: Testing Spark Applications
   
   7.1 Introduction to Spark Testing (500 words)
   7.2 Unit Testing with PySpark (1200 words)
       - Setting up test environment
       - Testing transformations
       - Mocking SparkSession
   7.3 Integration Testing (1000 words)
   7.4 Testing Delta Lake Operations (800 words)
   7.5 CI/CD for Spark Tests (700 words)
   7.6 Summary and Best Practices (400 words)
   
   [Approve Plan] [Modify Plan] [Cancel]
   
# 5. User approves → Execution phase by phase

# 6. After each section:
   - Consistency check against previous chapters
   - Terminology verification
   - Word count tracking

# 7. Output: Complete chapter with verified consistency
6.3 Scenariusz: API z CLI
bash# CI/CD Pipeline - weryfikacja przed merge

#!/bin/bash

# Verify all changed files
CHANGED_FILES=$(git diff --name-only origin/main)

npx @anthropic/deep-verify-cli verify $CHANGED_FILES \
  --provider claude \
  --output json \
  --config .deepverify/config.json \
  > verify-results.json

# Check for critical issues
CRITICAL_COUNT=$(jq '[.findings[] | select(.severity == "critical")] | length' verify-results.json)

if [ "$CRITICAL_COUNT" -gt 0 ]; then
  echo "❌ Found $CRITICAL_COUNT critical issues"
  jq '.findings[] | select(.severity == "critical")' verify-results.json
  exit 1
fi

echo "✅ Verification passed"
6.4 Scenariusz: Inna Wtyczka Używa API
typescript// Wtyczka do testowania integruje się z Deep Verify/Develop

import * as vscode from 'vscode';

export async function activate(context: vscode.ExtensionContext) {
  const deep = await getDeepAPI();
  
  // Po wygenerowaniu testu, automatycznie zweryfikuj
  vscode.commands.registerCommand('myTests.generateAndVerify', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) return;
    
    // 1. Użyj Deep Develop do wygenerowania testów
    const result = await deep.develop.execute(
      `Generate comprehensive tests for this file`,
      {
        mode: 'medium',
        domain: { type: 'code' },
        scope: { type: 'file', paths: [editor.document.uri.fsPath] }
      }
    );
    
    // 2. Dla każdego wygenerowanego pliku testów
    for (const output of result.outputs) {
      if (output.type === 'create' && output.path?.includes('test_')) {
        
        // 3. Weryfikuj wygenerowany test
        const verification = await deep.verify.verifyText(output.content!, {
          patterns: ['test-quality', 'test-coverage']
        });
        
        // 4. Jeśli są problemy, popraw
        if (verification.findings.length > 0) {
          const fixed = await deep.develop.continue(
            result,
            `Fix these issues in the tests: ${verification.summary}`
          );
          // Apply fixed version
        }
      }
    }
  });
}
```

---

## Część VII: Podsumowanie

### Co Dostarcza Deep Verify + Deep Develop
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CAPABILITIES SUMMARY                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DEEP VERIFY                                                                │
│  ═══════════════════════════════════════════════════════════════════════   │
│  ✓ Weryfikacja kodu, dokumentacji, dowolnych artefaktów                   │
│  ✓ Pattern-based detection                                                  │
│  ✓ Porównanie doc ↔ kod                                                    │
│  ✓ Git-aware (uncommitted changes)                                         │
│  ✓ Konfigurowalne per projekt                                              │
│                                                                              │
│  DEEP DEVELOP                                                               │
│  ═══════════════════════════════════════════════════════════════════════   │
│  ✓ Trzy tryby złożoności (light/medium/heavy)                             │
│  ✓ Wiele domen (code/documentation/book/api/data/custom)                  │
│  ✓ Inteligentne zbieranie kontekstu                                       │
│  ✓ Metody dobierane do zadania                                            │
│  ✓ Planowanie i fazowe wykonanie                                          │
│  ✓ Auto-weryfikacja wyników                                               │
│  ✓ Iteracja i kontynuacja                                                  │
│                                                                              │
│  INTEGRACJA                                                                 │
│  ═══════════════════════════════════════════════════════════════════════   │
│  ✓ VS Code UI (menus, commands, panels)                                   │
│  ✓ Extension API dla innych wtyczek                                       │
│  ✓ Standalone CLI dla CI/CD                                               │
│  ✓ IPC bridge (opcjonalny)                                                │
│  ✓ Konfigurowalne CLI providers                                           │
│                                                                              │
│  KONFIGURACJA                                                               │
│  ═══════════════════════════════════════════════════════════════════════   │
│  ✓ Hierarchia: defaults → global → project → command                      │
│  ✓ Domain-specific settings                                                │
│  ✓ Custom patterns i prompts                                               │
│  ✓ Scope presets                                                           │
│  ✓ Method customization                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

