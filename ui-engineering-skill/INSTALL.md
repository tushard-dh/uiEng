# End-to-End Installation and Usage

## 1. Install the skill

Extract the ZIP.

Copy:

```text
ui-engineering/
```

to the skills directory used by your Claude Code installation.

The exact parent directory can vary by Claude Code/runtime configuration. The
important requirement is that the directory containing `SKILL.md` is installed
as a skill.

## 2. Configure Mobbin MCP separately

The skill does not contain Mobbin credentials.

Your Claude Code/MCP configuration must expose Mobbin as an MCP server/tool.
Once configured, `/uiEng mobbin` should be able to use the available Mobbin
capabilities.

If Mobbin MCP is not available, use user-provided references or continue
without Mobbin.

## 3. Initialize a product repository

From the application repository:

```text
/uiEng init
```

The skill creates:

```text
.ui-engineering/
├── config.yaml
├── project-context.md
├── decisions/
├── references/
├── knowledge/
├── synthesis/
├── specs/
└── status.yaml
```

## 4. Recommended workflow

### Phase A — Understand

```text
/uiEng mode standard
/uiEng discover physician-management
```

`/uiEng mode` is optional — it defaults to `standard` if never set. Use
`quick` for a fast pass or `thorough` for a fully explored spec with
scored synthesis variants; see `workflows/mode.md`.

Claude inspects:
- frontend architecture
- routes
- components
- design system
- API contracts
- requirements
- existing screens

### Phase A.5 — Catalog existing components

```text
/uiEng catalog
```

Scans the configured component directories (`component_catalog.paths` in
`.ui-engineering/config.yaml`) and produces
`.ui-engineering/component-catalog.json`. Every later phase that reuses or
proposes components reads from this file.

### Phase B — Resolve important decisions

```text
/uiEng ask
```

Claude asks only high-impact questions.

### Phase C — Select Mobbin references

```text
/uiEng mobbin
```

The user selects one or more references through the available MCP workflow.

### Phase D — Convert visual reference to knowledge

```text
/uiEng analyze
```

Output:

```text
.ui-engineering/knowledge/
```

### Phase E — Compare multiple references

```text
/uiEng compare
```

### Phase F — Synthesize

```text
/uiEng synthesize
```

### Phase G — Create implementation specification

```text
/uiEng spec physician-management
```

### Phase H — Build

```text
/uiEng build physician-management
```

### Phase I — Review and validate

```text
/uiEng review
```

```text
/uiEng fix
```

### Phase J — Explain decisions

```text
/uiEng why physician-detail
```

Works for stored decisions and for established patterns
(`.ui-engineering/decisions/patterns.json`).

### Phase K — Check state

```text
/uiEng status
/uiEng patterns
```

## 5. One-command orchestration

You can also start with:

```text
/uiEng
```

The skill should inspect project state and route to the next useful action.

Example:

```text
/uiEng

I need a physician management page for recruiters.
Use Mobbin references and make it enterprise-grade.
```

The agent should not immediately code. It should first determine:
- whether the requirement is understood
- whether important UX decisions are missing
- whether references are selected
- whether a design system exists
- whether an API contract exists
- whether the UI spec is ready

## 6. Example for the locum platform

```text
/uiEng discover physician-matching
```

Then:

```text
/uiEng ask
```

Potential high-impact questions:

```text
1. Should physician details open in a drawer or full page?
2. Do recruiters need bulk selection/actions?
3. Should availability be shown as a calendar, table, or both?
```

Then:

```text
/uiEng mobbin
/uiEng analyze
/uiEng compare
/uiEng synthesize
/uiEng spec physician-matching
/uiEng build physician-matching
/uiEng review
```

## 7. CI integration

Run deterministic validation in CI:

```bash
python scripts/validate_schema.py .ui-engineering
python scripts/validate_ui.py .
python scripts/scan_components.py . --paths src/components --out .ui-engineering/component-catalog.json
```

Running `scan_components.py` in CI keeps the catalog's raw scan fresh even
if a contributor forgets to run `/uiEng catalog` locally; the semantic
classification pass still needs a Claude session before the enrichment is
complete.

The application repository can add these commands to its CI pipeline.

## 8. Security

Never commit:
- Mobbin credentials
- MCP secrets
- API keys
- service account JSON
- production credentials

Keep secrets in the application's approved secret-management system.

The skill should not contain secrets.

## 9. What is intentionally not scripted

Do not create Python scripts for:

```text
AI UI analyzer
UX decision engine
Mobbin interpretation
reference synthesis
UX recommendation
UI generation
```

Those require reasoning and context and should be performed by Claude using
the MCP and project files.

Scripts should remain deterministic and testable.
