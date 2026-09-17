# Pattern Gallery

Purpose: gather Mobbin references **one UI pattern at a time** — navigation,
tabs, action bar, buttons, table, cards, forms, detail presentation —
instead of picking one or two whole screens and inheriting everything
they happen to contain. This is how a UI/UX designer actually works: a
moodboard assembled pattern by pattern, each choice deliberate, then
composed into one coherent design — not "find one screen that looks
about right and copy it."

This replaces the old single-pass "search once, pick a screen" version of
step 2 (`Select references`) in `SKILL.md`. It runs after discovery,
before synthesis.

## Process

### 1. Derive the pattern list

From `project-context.md` and whatever screen list exists so far (from
discovery, or from a spec if one already exists), list the distinct UI
patterns this feature actually needs a visual/interaction decision for.
Typical patterns: primary navigation model, tabs (if a screen has
multiple views), action bar / toolbar, primary button style, table or
list row presentation, cards, form layout, detail presentation
(drawer/modal/full page), empty/error state treatment.

Do not list a pattern that has no real decision to make (e.g. don't list
"buttons" separately if the design system already fully defines button
styling — see rule 13 in `SKILL.md`).

### 2. Skip what's already settled

For each pattern, before spending a search on it, check in order:
1. **Component catalog** (`.ui-engineering/component-catalog.json`) — if
   a catalog component already implements this pattern, reuse it. Don't
   search Mobbin for something that already exists in the product.
2. **Decision memory** (`.ui-engineering/decisions/patterns.json`) — if
   an `established` pattern already resolves this (see
   `workflows/decision-memory.md`), apply it and say so; don't re-ask.

Only patterns that survive both checks get a Mobbin search.

### 3. Search + present, one pattern per round

For each remaining pattern, in descending order of implementation impact,
and within the active mode's total reference budget (see "Budget" below):

1. Search Mobbin scoped to that specific pattern, not the whole screen —
   e.g. `"settings tabs, web"`, `"table row actions, web"`,
   `"primary button, web"` — following the search-planning guidance in
   the `mobbin-search` skill (specific query terms, correct platform,
   reasonable limit).
2. Show the retrieved screens to the user (inline images), each labeled
   1, 2, 3… Drop near-duplicate results — never present two options that
   differ only in incidental brand color as if they were distinct choices.
3. Ask the user to pick one, as a genuine multiple-choice decision (this
   is what `AskUserQuestion` is for) — options described by what's
   visually/interactionally distinct about each (e.g. "pill tabs with an
   underline indicator" vs. "boxed tabs with a filled active state"), not
   just "Option 1" / "Option 2". Always include the option to describe
   something custom instead of picking from the search results.
4. Record the selection using `schemas/ui-reference.schema.json`,
   including which `pattern` it answers and the `alternatives_shown` that
   were not picked, for provenance.

### 4. Budget

The active mode (`workflows/mode.md`) sets a total reference count — quick
2, standard 5, thorough 10 — spread **across all patterns**, not per
pattern. If patterns outnumber the budget, prioritize by implementation
impact and disclose which remaining patterns fall back to the internal
design system / established conventions / AI recommendation (synthesis
priority order in `SKILL.md` step 6) rather than silently deciding them.

### 5. Analyze, then synthesize

Different patterns will very likely come from different reference
screens/apps. That's expected and fine — feed each selected reference
into `workflows/reference-analysis.md` independently, then into
`workflows/synthesis.md` to compose them into one coherent screen and
resolve any conflicts (e.g. differing radius/spacing between two source
apps) into the internal design system's tokens. Synthesis's conflict-
resolution job already covers this; pattern-by-pattern selection just
means it has more, smaller inputs to reconcile instead of one or two
large ones.

## Rules

1. Never let one Mobbin screen silently dictate every pattern in a
   feature. Picking references from the same app across several patterns
   is fine *if each one was independently evaluated for that pattern* —
   it's a synthesis outcome, not a shortcut around the per-pattern choice.
2. Never present near-duplicate options in the same round — it wastes the
   user's attention and isn't a real choice.
3. Always offer a "describe your own" escape from the multiple-choice
   round — the search results are a starting point, not a constraint.
4. Reuse component catalog and decision memory before spending a search —
   this is what keeps repeated pattern types (e.g. "detail presentation")
   from being re-litigated on every feature (see
   `workflows/decision-memory.md`).

## Output

`.ui-engineering/references/<feature>/<pattern-slug>.json` — one
reference record per pattern, using `schemas/ui-reference.schema.json`.
