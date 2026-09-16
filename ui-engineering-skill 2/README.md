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

Then:

```text
/uiEng discover physician-management
/uiEng ask
/uiEng mobbin
/uiEng analyze
/uiEng compare
/uiEng synthesize
/uiEng spec physician-management
/uiEng build physician-management
/uiEng review
/uiEng fix
/uiEng status
```

You do not need to run every command manually. `/uiEng` can inspect state and
route to the next stage.

## Example

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
12. Ask for/recognize approval before implementation when appropriate.
13. Build using existing components.
14. Validate.
15. Report remaining issues.

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
└── status.py
```

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
