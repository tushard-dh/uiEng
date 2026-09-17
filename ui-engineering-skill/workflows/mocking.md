# Mocking

Purpose: produce a real, viewable prototype of the synthesized UI —
actual files the user opens or runs — before committing to a full,
backend-wired implementation via `/uiEng build`. This is what makes the
skill's output tangible instead of stopping at a written spec.

A mock is disposable and non-integrated. It proves the layout, states, and
interactions look and feel right. `/uiEng build` is the separate,
integrated path that reuses catalog components, wires real APIs, and adds
tests — see `workflows/implementation.md`. Never treat a mock's file as
production code without going through `/uiEng build`'s process.

## Command

`/uiEng mock <feature> [--lang html|react|typescript]`

Requires a UI spec to already exist for `<feature>`
(`.ui-engineering/specs/<feature>/spec.json`) — mocks visualize a spec, they do
not replace deciding one. If no spec exists, say so and offer to run
`/uiEng spec <feature>` first rather than improvising layout from
scratch.

## Choosing the language

1. If `--lang` is given, use it.
2. Otherwise, check `.ui-engineering/config.yaml` → `mocking.default_lang`.
3. Otherwise, infer from the product's actual frontend stack detected
   during discovery (`project-context.md` → "Frontend framework"):
   - React + TypeScript project → `typescript`
   - React + JavaScript project → `react`
   - no frontend yet / static site / unclear → ask once, offering `html`
     as the fastest zero-setup option.
4. Never silently pick a language the user hasn't confirmed when none of
   the above resolve it — this is a cheap, high-value question, ask it.

## Output location

```text
mocks/<feature>/
```

Top-level, at the product repo's root — a sibling of `.ui-engineering/`,
not nested inside it. Read `mocking.output_dir` from
`.ui-engineering/config.yaml` (default `mocks`) rather than assuming the
path.

This is deliberate: `.ui-engineering/` is the skill's internal
knowledge/state folder (specs, decisions, catalog) that nothing outside
the skill needs to open directly. A mock is the opposite — its entire
purpose is to be opened in a browser or run, by the user, right now.
Burying it inside the internal state folder defeats that.

Also kept out of `src/` — a mock is a preview artifact, not a component
the catalog should pick up. If the user later approves it for real
implementation, that happens through `/uiEng build`, which produces
proper, catalog-registered components in `src/`.

## Generation rules (all languages)

1. Implement every state the spec defines (loading, empty, error,
   success) — not just the happy path. This is the same requirement as
   the polish pass in `workflows/distinctiveness.md` step 3.
2. Use realistic sample data that matches the product's actual domain
   (from `project-context.md` / API contracts), not lorem ipsum or
   generic placeholder names, so the mock actually helps someone judge fit.
3. Start from the project's real design tokens if a design system exists
   (colors, spacing, radius, type scale). If none exists yet, start from
   `templates/mock-tokens.css` and say so — never invent arbitrary
   hex/pixel values that look like generic AI output (see
   `rules/distinctiveness-rules.md` rule 1). **Copy those token values
   directly into the mock's single stylesheet — never `@import` a
   separate tokens file.** Some browsers block `@import` of a local
   `file://` resource from a `file://` page; when that happens every CSS
   variable silently resolves to nothing and the page renders with no
   colors, no spacing, and no alignment, even though the HTML/CSS "looks"
   correct on inspection. This has actually happened — treat it as a
   known failure mode, not a hypothetical.
4. Include at least one interaction (a button click revealing a next
   state, a hover/focus style, a drawer opening) — a fully static image
   disguised as HTML is not a useful mock.
5. Keep it self-contained and runnable with minimal setup per language
   (see below) — the point is fast visual feedback, not a build pipeline.
6. For `html` mocks specifically: everything the page needs to render
   correctly (tokens, layout, component styles) must live in files loaded
   only via `<link>`/`<script>` tags in the HTML `<head>`/`<body>` —
   never via `@import` inside a CSS file, and never via `fetch`. Verify
   this by actually opening the generated `index.html` with a plain
   double-click / `open` command (true `file://`, not a local server) and
   confirming it's fully styled — a check over `http://localhost` alone
   does not catch this failure mode, because HTTP does not impose the
   same restriction `file://` does.

## Per-language output

### `html`

- `index.html`, `styles.css`, and `script.js` (vanilla, no build step).
- Opens directly in a browser — no server or install required.
- Best for: fastest possible look-and-feel check, non-JS stakeholders,
  projects with no JS framework yet.

### `react`

- One `.jsx` file per component named in the spec, plus a minimal `App.jsx`
  that composes them and a small static harness (`index.html` loading
  React via ESM CDN, or a `package.json` + Vite scaffold if the product
  repo already uses Vite/CRA — match the existing project's tooling if one
  exists, otherwise default to the zero-install CDN harness).
- Best for: teams whose product is already React/JS and want the mock's
  structure to translate directly into `/uiEng build` components later.

### `typescript`

- Same structure as `react`, but `.tsx` files with typed props derived
  from the spec's data bindings (and API contract types if available).
- Best for: products already on React + TypeScript — keeps the mock
  type-consistent with what `/uiEng build` will eventually produce.

## After generating

Tell the user:
- where the files were written,
- exactly how to view them (open the HTML file directly; or the run
  command if a build scaffold was generated),
- which states/interactions are included and which spec sections were
  intentionally left unmocked (e.g. real API wiring, auth).

For `html` mocks, actually open the generated `index.html` via `file://`
(not just a local server) before telling the user it's ready — see
generation rule 6. If it isn't fully styled, fix the CSS structure before
handing it off, don't ship it and hope.

## Rules

1. A mock is never wired to real APIs, auth, or the design system's actual
   component implementations — that is `/uiEng build`'s job.
2. Do not skip the polish pass or the sameness check on the grounds that
   "it's just a mock" — a mock that looks like generic AI output defeats
   the point of this skill.
3. If the user approves a mock, hand off to `/uiEng build` rather than
   promoting mock files into `src/` directly — build re-derives
   proper components against the catalog and design system.

## Output

`mocks/<feature>/` (top-level, see "Output location" above) — files as
specified above, in the chosen language. Not a JSON artifact; no schema.
