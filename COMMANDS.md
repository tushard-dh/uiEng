# /uiEng command reference

Quick cheat sheet for the `ui-engineering` skill. Full behavioral rules live
in the skill's own `SKILL.md`; this is just the command surface.

| Command | Purpose |
|---|---|
| `/uiEng` | Inspect current project state and route to the next useful stage. Can also be given a free-form request (e.g. "build a physician management page") and it will figure out what stage to start at. |
| `/uiEng init` | Create `.ui-engineering/` in the current project (config, state, empty dirs for decisions/references/knowledge/synthesis/specs). |
| `/uiEng discover <feature>` | Understand requirements, existing UI, API contracts, roles, unknowns. Writes `.ui-engineering/project-context.md`. |
| `/uiEng ask` | Ask only high-impact UX/product questions (e.g. drawer vs. full page) — skips low-value questions already answered by the design system. |
| `/uiEng mobbin` | Search Mobbin (via the Mobbin MCP tools) for reference screens/flows and let you pick one or more. This is keyword search, not a raw-URL fetch — describe what you want (e.g. "enterprise dashboard, web") rather than pasting a mobbin.com link. |
| `/uiEng analyze` | Turn selected references into structured JSON knowledge (`.ui-engineering/knowledge/`), tagging every claim as observed / inferred / unknown. |
| `/uiEng compare` | Compare 2+ references, surface conflicts, map which reference contributes what. |
| `/uiEng synthesize` | Merge references + decisions + design system into one product-specific pattern (`.ui-engineering/synthesis/`). |
| `/uiEng spec <feature>` | Generate an implementation-ready UI specification (`.ui-engineering/specs/`) — routes, layout, components, states, a11y, acceptance criteria. |
| `/uiEng build <feature>` | Implement the frontend from the spec, reusing existing design-system components. |
| `/uiEng review` | Validate the implementation against rules + spec (design-system compliance, states, a11y, responsiveness, component reuse). |
| `/uiEng fix` | Apply fixes for findings from `/uiEng review`. |
| `/uiEng status` | Print current workflow state across all stages. |
| `/uiEng why <decision-or-screen>` | Explain a stored decision — evidence, tradeoffs, provenance. |
| `/uiEng evolve` | Analyze an existing (already-built) UI and recommend controlled, incremental changes instead of a rewrite. |

## Typical end-to-end run

```text
/uiEng init
/uiEng discover physician-matching
/uiEng ask
/uiEng mobbin
/uiEng analyze
/uiEng compare
/uiEng synthesize
/uiEng spec physician-matching
/uiEng build physician-matching
/uiEng review
/uiEng fix
```

## Notes

- Mobbin is a reference source only — the application's internal design
  system is always the implementation source of truth.
- Nothing gets implemented before a UI spec exists (`require_spec_before_build`
  in `config.example.yaml`).
- Deterministic checks (`scripts/validate_schema.py`, `scripts/validate_ui.py`)
  can be wired into CI; everything else (analysis, decisions, synthesis) is
  Claude reasoning, not scripted.
