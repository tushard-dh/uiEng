---
name: ui-engineering
description: >
  An AI UI/UX engineering workflow for analyzing product requirements,
  existing applications, and Mobbin UI references; asking targeted UX
  questions; creating machine-readable UI knowledge; comparing and
  synthesizing multiple references; generating implementation-ready UI
  specifications; and optionally building and validating frontend UI.
  Use when designing, analyzing, comparing, specifying, implementing,
  evolving, or reviewing product UI/UX.
---

# UI Engineering

## Purpose

Turn product requirements and selected UI references into implementation-ready,
consistent, accessible frontend experiences.

Core lifecycle:

Reference → Understand → Question → Decide → Synthesize → Specify →
Implement → Validate → Evolve

Mobbin is a reference source, not the product design system and not a code
source of truth.

## Command routing

Interpret `/uiEng` commands as follows:

- `/uiEng` — inspect project state and route to the next useful stage.
- `/uiEng init` — initialize `.ui-engineering/` and project context.
- `/uiEng discover <feature>` — understand requirements, existing UI, API
  contracts, user roles, and unknowns.
- `/uiEng catalog` — scan the product repo for existing UI components and
  refresh `.ui-engineering/component-catalog.json`.
- `/uiEng ask` — ask only high-impact UX/product questions.
- `/uiEng mobbin` — use the configured Mobbin MCP to browse/search references
  and let the user select one or more references.
- `/uiEng analyze` — analyze selected references into machine-readable
  knowledge.
- `/uiEng compare` — compare two or more references and expose conflicts.
- `/uiEng synthesize` — create a product-specific synthesis.
- `/uiEng spec <feature>` — create an implementation-ready UI specification.
- `/uiEng build <feature>` — implement frontend after the specification exists.
- `/uiEng review` — validate implementation against rules and spec.
- `/uiEng fix` — fix validation findings.
- `/uiEng status` — show current workflow state.
- `/uiEng why <decision-or-screen>` — explain the decision, evidence and
  tradeoffs.
- `/uiEng evolve` — analyze an existing UI and recommend controlled evolution.

If a command is ambiguous, inspect state first and ask only the smallest
number of questions needed to choose a safe path.

## Operating rules

1. Product requirements override visual references.
2. Accessibility and security constraints override aesthetics.
3. Existing approved design-system rules override arbitrary reference values.
4. User-stated preferences override AI preferences when they do not violate
   requirements.
5. Mobbin references provide patterns and visual/interaction inspiration.
6. Never claim behavior is observed if it was inferred.
7. Classify evidence as observed, inferred, or unknown.
8. Never invent unavailable reference metadata.
9. Preserve provenance for important decisions.
10. Do not implement before the UI specification is sufficiently complete.
11. Prefer existing components over creating duplicates.
12. Normalize colors, spacing, typography, radius and elevation into the
    internal design system.
13. Ask questions only when uncertainty × implementation impact is high.
14. Prefer qualitative decision confidence unless measurable scoring criteria
    are explicitly defined.
15. For multiple references, analyze each independently before synthesis.
16. Before proposing or building a new component, check the component
    catalog for reuse or near-duplicate candidates.

## Workflow

### 1. Discover

Read:
`workflows/discovery.md`

Collect:
- product context
- user roles
- feature goal
- primary and secondary tasks
- existing routes/components
- API/data contracts
- responsive requirements
- accessibility requirements
- business constraints
- unknowns

Create/update `.ui-engineering/project-context.md`.

As part of discovery, build or refresh the component catalog (see
`workflows/component-catalog.md`) if it does not exist yet or is stale.
Every later stage that reuses or creates components reads from this
catalog rather than re-inspecting the codebase ad hoc.

### 2. Select references

When the user requests Mobbin-based design:
- Use the configured Mobbin MCP.
- Let the user select one or more references.
- Save reference metadata using `schemas/ui-reference.schema.json`.
- Do not treat a screenshot as proof of hidden behavior.

### 3. Analyze references

Read:
`workflows/reference-analysis.md`

Produce canonical JSON using:
`schemas/ui-knowledge.schema.json`

Analyze:
- information architecture
- layout
- visual language
- components
- composition
- interactions
- states
- responsive behavior
- accessibility
- content design
- semantic design-token roles
- patterns
- constraints
- observations
- inferences
- unknowns
- provenance

### 4. Decide

Read:
`workflows/decision-making.md`

Ask only high-impact questions. Examples:
- table vs cards
- drawer vs full page
- single vs multi-step form
- bulk actions
- navigation model
- mobile transformation

Do not ask low-impact questions such as exact border radius when the design
system already defines it.

Persist decisions using:
`schemas/ui-decision.schema.json`

### 5. Compare

Read:
`workflows/comparison.md`

For multiple references:
- analyze independently
- compare equivalent patterns
- identify conflicts
- identify strengths/weaknesses
- map contributions
- recommend a product-specific choice

### 6. Synthesize

Read:
`workflows/synthesis.md`

Create:
`schemas/ui-synthesis.schema.json`

Synthesis must explicitly map which reference contributes which pattern.

Use this priority:
1. product requirements
2. accessibility/security
3. internal design system
4. established UX conventions
5. explicit user preference
6. selected reference priority
7. AI recommendation

### 7. Specify

Read:
`workflows/specification.md`

Create:
`schemas/ui-spec.schema.json`

The UI spec should define:
- routes/screens
- page hierarchy
- layouts
- components
- data bindings
- API dependencies
- interactions
- state matrix
- validation
- responsive behavior
- accessibility
- loading/empty/error/success states
- permissions
- analytics/events when required
- acceptance criteria
- reference provenance

### 8. Implement

Read:
`workflows/implementation.md`

Before coding:
- refresh the component catalog if stale (`workflows/component-catalog.md`)
- check the catalog for reusable/near-duplicate components before creating
  new ones
- reuse approved primitives
- inspect API types/contracts
- confirm spec status

Implementation should:
- avoid duplicate components
- use design tokens
- preserve state coverage
- support keyboard accessibility
- support responsive layouts
- keep business logic out of presentation where architecture requires
- add tests for important behavior

### 9. Validate

Read:
`workflows/validation.md`

Run deterministic checks with:
`scripts/validate_schema.py`
`scripts/validate_ui.py`

Review:
- design-system compliance
- required states
- responsive requirements
- accessibility
- component reuse
- hardcoded values
- API integration
- route/spec consistency

### 10. Evolve

When the UI already exists:
- inspect current implementation first
- compare it with requirements and selected references
- preserve working behavior
- identify incremental changes
- avoid wholesale rewrites unless justified
- update decisions/specs when behavior changes

## Artifacts

Use project-local `.ui-engineering/`:

```text
.ui-engineering/
├── config.yaml
├── project-context.md
├── component-catalog.json
├── decisions/
├── references/
├── knowledge/
├── synthesis/
├── specs/
└── status.yaml
```

The skill package is reusable. Project-specific knowledge belongs in the
application repository, not inside the global skill package.

## Scripts

Scripts are intentionally small and deterministic:

- `validate_schema.py` — validate JSON artifacts.
- `create_artifact.py` — create standard feature/artifact directories.
- `validate_ui.py` — static UI compliance checks.
- `status.py` — summarize project workflow state.
- `scan_components.py` — deterministic filesystem scan producing a raw
  component catalog (name, path, best-effort props); semantic
  classification is a Claude follow-up pass, not scripted.

Do not create scripts for reasoning tasks such as UI analysis, decision making,
reference synthesis, or UX recommendation. Those are Claude/MCP responsibilities.

## MCP contract

This skill assumes a Mobbin MCP is available/configured separately.

The skill must not pretend that an MCP tool exists if it is unavailable.
If Mobbin MCP is unavailable:
- continue with user-provided screenshots/reference metadata, or
- ask the user to configure the MCP,
- never fabricate reference analysis.

## Completion criteria

A feature is considered UI-complete only when:
- product requirements are mapped
- high-impact decisions are resolved
- references are analyzed when requested
- synthesis exists when multiple references are used
- UI specification exists
- implementation exists if requested
- validation has been run
- blocking findings are resolved or explicitly accepted
- provenance and decisions are persisted
