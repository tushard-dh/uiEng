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
                 Decision Engine
                       |
             +---------+---------+
             |         |         |
          Mobbin    Knowledge   Design System
            MCP        JSON         |
             |           |          |
             +-----------+----------+
                         |
                     Synthesis
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

## Source-of-truth hierarchy

1. Product requirements
2. Security/accessibility constraints
3. Backend/API contracts
4. Internal design system
5. Approved UX decisions
6. Synthesized UI specification
7. Mobbin references
8. AI suggestions
