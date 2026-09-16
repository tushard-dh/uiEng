# UI Engineering Skill

An installable Claude Skill for product UI/UX engineering with optional Mobbin
MCP integration.

## What it solves

This skill creates a repeatable workflow:

```text
Product Requirement
       ↓
Discover
       ↓
Ask high-impact questions
       ↓
Mobbin MCP references
       ↓
UI/UX knowledge
       ↓
Compare / Synthesize
       ↓
UI Specification
       ↓
Frontend implementation
       ↓
Validation
       ↓
Evolution
```

It is designed for enterprise applications where consistency, accessibility,
traceability and maintainability matter.

## Important architecture

Mobbin is a reference library.

Claude is the reasoning/orchestration layer.

The application's internal design system is the implementation source of
truth.

Project-local `.ui-engineering/` is the persistent knowledge/state layer.

## Installation

Copy the `ui-engineering` directory into the Claude Code skills directory
used by your environment.

Example layout:

```text
<claude-skills-directory>/
└── ui-engineering/
    ├── SKILL.md
    ├── workflows/
    ├── schemas/
    ├── rules/
    ├── templates/
    ├── examples/
    └── scripts/
```

Then restart/reload the Claude Code environment if required by your setup.

## First use

Inside a product repository:

```text
/uiEng init
```

Then, for any feature (replace `<feature-name>` with whatever you're
actually building — this sequence is not tied to any specific product):

```text
/uiEng mode thorough
/uiEng discover <feature-name>
/uiEng catalog
/uiEng ask
/uiEng mobbin
/uiEng analyze
/uiEng compare
/uiEng synthesize
/uiEng spec <feature-name>
/uiEng mock <feature-name> --lang typescript
/uiEng build <feature-name>
/uiEng review
/uiEng fix
/uiEng status
/uiEng patterns
```

You do not need to run every command manually. `/uiEng` can inspect state and
route to the next stage.

## Worked example (illustrative — not the only use case)

User:

```text
/uiEng

Build the physician management screen for recruiters.
Use Mobbin references for an enterprise healthcare dashboard.
```

Expected behavior:

1. Inspect application.
2. Find existing design system.
3. Identify API/data requirements.
4. Identify unresolved decisions.
5. Ask only important questions.
6. Use Mobbin MCP.
7. Let the user select one or more references.
8. Analyze references.
9. Compare if multiple references are selected.
10. Synthesize a product-specific pattern.
11. Generate UI specification.
12. Optionally generate a real HTML/React/TypeScript mock for visual sign-off.
13. Ask for/recognize approval before implementation when appropriate.
14. Build using existing components.
15. Validate.
16. Report remaining issues.

## Depth control

`/uiEng mode quick|standard|thorough` trades speed for exhaustiveness:
fewer/more questions asked, fewer/more Mobbin references pulled, and one
recommendation vs. several scored synthesis variants. See
`workflows/mode.md`. Accessibility, security, and product-requirement
rules are never affected by mode.

## Decision memory

Repeated decisions across features (e.g. "drawer vs. full page" showing up
the same way on a third screen) get promoted into
`.ui-engineering/decisions/patterns.json` and reused automatically on
later features instead of being re-asked, while staying overridable. See
`workflows/decision-memory.md`. Use `/uiEng patterns` to see what's been
established.

## Mocking (real files, not just a spec)

`/uiEng mock <feature> [--lang html|react|typescript]` turns a UI spec
into an actual, viewable prototype under `.ui-engineering/mocks/<feature>/`
— open the HTML directly, or run the generated React/TypeScript scaffold.
It asks which language if one isn't set in `config.yaml` or inferable from
the product's existing stack. Mocks are disposable and not wired to real
APIs or the component catalog; `/uiEng build` is the separate path that
produces integrated, catalog-registered production code. See
`workflows/mocking.md`.

## Design distinctiveness (why this isn't just a layout generator)

AI-generated UI has well-documented failure modes: visual homogenization
(every screen looks like every other AI-generated screen), shallow
"vibe"-driven design with no user-research grounding, screens that
function but feel undesigned, requests executed without any critical
pushback, and prototypes that don't scale past the first demo. `/uiEng`
counters each of these with an explicit process step rather than a
disclaimer — see `workflows/distinctiveness.md` and
`rules/distinctiveness-rules.md`:

- discovery requires a user-research signal (or an honest `unknown`),
- every feature gets a "challenge" step before anything is built,
- every synthesis gets checked against common AI-generated defaults before
  being finalized,
- every spec must cover real states and at least one micro-interaction
  before it's considered complete, not just the happy-path layout,
- the component catalog and design tokens keep output consistent as the
  product grows, instead of accumulating one-off styles.

## Multi-reference example

Reference A contributes:
- navigation
- dashboard hierarchy

Reference B contributes:
- table
- search
- filters
- row actions

The skill creates a synthesis rather than copying either design.

## Q&A / Decision Engine

The decision engine asks only questions with meaningful implementation impact.

Good:

```text
Should physician details open in a drawer or full page?
```

Low value:

```text
Should the border radius be 8px or 10px?
```

If the design system already defines radius, the second question is unnecessary.

Use:

```text
/uiEng why physician-detail
```

to explain a stored decision.

## Scripts

Only deterministic tasks are scripted.

```text
scripts/
├── validate_schema.py
├── create_artifact.py
├── validate_ui.py
├── status.py
└── scan_components.py
```

`scan_components.py` walks the configured component directories and
produces a raw, deterministic component inventory (name, path, best-effort
props). Claude then classifies ambiguous entries semantically as a
follow-up pass — see `workflows/component-catalog.md`. This is what backs
the `/uiEng catalog` command and lets `/uiEng build`/`/uiEng spec` reuse
real components instead of guessing what already exists.

No AI reasoning is hidden inside Python scripts.

## Mobbin MCP

The skill does not bundle credentials or a Mobbin server.

Configure your Mobbin MCP separately according to your MCP/Claude Code
environment. The skill consumes the reference data exposed by that MCP.

Never commit credentials, API keys or MCP secrets to this repository.

## Enterprise recommendation

Use this skill alongside:

- an approved internal design system
- frontend coding standards
- accessibility standards
- API contracts
- product requirements
- security requirements
- automated frontend tests
- CI validation

The skill should improve engineering consistency, not replace engineering
governance.
