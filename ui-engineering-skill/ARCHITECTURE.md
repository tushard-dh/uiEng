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
                     Synthesis  <---- sameness check vs. common
                         |            AI-generated defaults (Distinctiveness)
                         |            + variant count set by Mode
                         |
                     UI Spec  <---- checked against Component Catalog;
                         |          polish pass (Distinctiveness) required
                         |
                  +------+------+
                  |             |
                Mock       Frontend Code
             (html/react/    (catalog-registered,
              typescript,     API-wired, tested)
              disposable)
                  |             |
                  +------+------+
                         |
                   Validation
                         |
                      Evolve
```

Every stage from Discovery onward runs under the **Distinctiveness** gate
(`workflows/distinctiveness.md`): a challenge step before building, a
sameness check before synthesis, and a polish pass before a spec counts as
complete. This exists specifically to counter AI UI generation's known
failure modes — visual homogenization, shallow prompting, undesigned-
feeling output, uncritical execution, and unscalable prototypes.

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

### Distinctiveness
- a process gate, not an artifact: challenge step (discovery), sameness
  check (synthesis), polish pass (spec/validation) — see
  `workflows/distinctiveness.md` and `rules/distinctiveness-rules.md`

### Mocking
- produces real, viewable files (top-level `mocks/<feature>/`, sibling of
  `.ui-engineering/` — not inside it) in html/react/typescript from an
  existing spec; disposable and non-integrated, distinct from
  `/uiEng build`'s catalog-registered, API-wired output — see
  `workflows/mocking.md`

## Source-of-truth hierarchy

1. Product requirements
2. Security/accessibility constraints
3. Backend/API contracts
4. Internal design system
5. Approved UX decisions
6. Synthesized UI specification
7. Mobbin references
8. AI suggestions
