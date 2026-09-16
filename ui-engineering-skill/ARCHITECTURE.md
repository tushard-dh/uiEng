# UI Engineering Architecture

```text
                    /uiEng
                       |
              +--------+--------+
              |                 |
        Product Context     Existing Code
              |                 |
              |          Component Catalog
              |           (scan_components.py
              |            + Claude classification)
              |                 |
              +--------+--------+
                       |
                 Decision Engine <---> Decision Memory
                       |               (patterns.json,
                       |                cross-feature reuse)
             +---------+---------+
             |         |         |
          Mobbin    Knowledge   Design System
            MCP        JSON         |
             |           |          |
             +-----------+----------+
                         |
                     Synthesis  <---- variant count set by
                         |            active Mode (quick/standard/thorough)
                         |
                     UI Spec  <---- checked against Component Catalog
                         |          before proposing new components
                    Frontend Code
                         |
                   Validation
                         |
                      Evolve
```

## Responsibilities

### Claude Skill
- reasoning
- analysis
- Q&A
- decision making
- synthesis
- specification
- implementation orchestration
- semantic review

### Mobbin MCP
- reference retrieval/selection data exposed by the configured MCP

### Application
- business rules
- backend APIs
- internal design system
- production source code
- authentication/authorization
- observability
- tests

### Deterministic scripts
- schema validation
- workspace creation
- status
- static UI checks
- component catalog scanning (filesystem only; semantic classification of
  ambiguous entries is done by the Claude Skill, not the script)

### Decision memory
- cross-feature pattern storage (`.ui-engineering/decisions/patterns.json`)
- matching analogous decisions across features and promoting/overriding
  patterns is reasoning, done by the Claude Skill, not scripted

### Mode
- a persisted config value (`workflow.mode`) that scales question count,
  reference count, and synthesis variant count up or down; does not alter
  the source-of-truth hierarchy below

## Source-of-truth hierarchy

1. Product requirements
2. Security/accessibility constraints
3. Backend/API contracts
4. Internal design system
5. Approved UX decisions
6. Synthesized UI specification
7. Mobbin references
8. AI suggestions
