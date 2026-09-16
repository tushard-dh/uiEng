# Component Catalog

Purpose: give every later stage (`/uiEng spec`, `/uiEng build`, `/uiEng
review`) a ground-truth inventory of components that already exist in the
product repo, so the skill proposes reuse before proposing something new.

## When to run

- On `/uiEng catalog` (explicit refresh).
- Automatically at the start of `/uiEng discover` if no catalog exists yet.
- Automatically before `/uiEng build` if the catalog is older than
  `component_catalog.stale_after_days` (see `config.example.yaml`), or any
  scanned path contains files newer than `generated_at`.

## Process

1. Read `component_catalog.paths` and `component_catalog.extensions` from
   the project's `.ui-engineering/config.yaml` (fall back to the defaults
   in `config.example.yaml` if the project hasn't overridden them).
2. Run the deterministic scanner:
   ```bash
   python scripts/scan_components.py <project_root> \
     --paths <paths...> --extensions <extensions...> \
     --out .ui-engineering/component-catalog.json
   ```
   This step only walks the filesystem and extracts a component name, file
   path, and best-effort prop list per file via regex. It does not infer
   purpose, category, or design intent — that would be reasoning, not
   scripting (see `SKILL.md` "Scripts" rule).
3. Read the resulting catalog. For every entry with `needs_review: true` or
   `category: "unknown"`:
   - Open the file.
   - Classify `category` as `primitive` (e.g. Button, Input), `composite`
     (e.g. Card, FormField), `pattern` (e.g. DataTable, FilterBar), or
     `page`.
   - Write a one-line `description` of what it does.
   - List `design_tokens_used` if the component references design tokens.
   - Set `needs_review: false` once classified.
4. Save the enriched catalog back to
   `.ui-engineering/component-catalog.json`, validated against
   `schemas/component-catalog.schema.json`.

## Rules

1. Never describe a component as "existing" if it is not in the catalog —
   if it's not there, it's new.
2. Before specifying or building a new component, search the catalog for a
   near-duplicate (same purpose, different name). If a plausible match
   exists and it isn't obvious whether to reuse or create new, treat it as
   a high-impact question (see `workflows/decision-making.md`) instead of
   deciding silently.
3. If the catalog is stale at the start of `/uiEng build`, refresh it
   before proceeding rather than building against outdated information.
4. Components added during `/uiEng build` must be appended to the catalog
   immediately (`source: "manual"` until the next scan confirms them), so
   the very next feature sees them as reusable.
5. This scanner is intentionally generic (configurable paths/extensions,
   framework auto-detected) so the same skill package works unmodified
   across different product repos.

## Output

`.ui-engineering/component-catalog.json` using
`schemas/component-catalog.schema.json`.
