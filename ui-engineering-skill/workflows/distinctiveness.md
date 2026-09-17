# Distinctiveness & Critical Design

Purpose: this skill exists partly to counter well-documented failure modes
of AI-generated ("vibe coded") UI:

- **Visual homogenization** — AI models default to the same landing pages,
  layouts, and component styles because that's the statistical mode of
  their training data.
- **Low creativity/depth** — prompting for a "vibe" prioritizes instant,
  surface-level aesthetics over user research, brand, and interaction
  nuance.
- **The "feels undesigned" trap** — screens work but lack rhythm, emotional
  resonance, and polish.
- **Erosion of critical thinking** — automated layouts get accepted without
  anyone challenging the prompt or the underlying structural problem.
- **Inconsistent scalability** — quick conversational prototypes break down
  as features grow, producing messy styles and maintenance debt.

This skill counters each of these with a concrete step, not a slogan:

| Failure mode | Countermeasure | Where |
|---|---|---|
| Visual homogenization | Sameness check before synthesis | This file, step 2 |
| Low creativity/depth | Required user-research capture in discovery | `workflows/discovery.md` |
| Feels undesigned | Mandatory polish pass before spec is "complete" | This file, step 3 |
| Erosion of critical thinking | Mandatory challenge step before building anything | This file, step 1 |
| Inconsistent scalability | Component catalog + design tokens (already required) | `workflows/component-catalog.md`, rule 16 |

## Step 1 — Challenge the request

Before discovery output is considered final, state at least one of:
- a structural risk in the request as given (e.g. "this table will need
  bulk actions once row count grows — should we design for that now?"),
- an alternative approach worth considering, or
- an assumption being made that the user should confirm.

This is not optional politeness — silently building exactly what was
asked, with no pushback, is how shallow "vibe coded" UI happens. If
nothing is genuinely worth challenging, say so explicitly ("no structural
concerns — proceeding") rather than skipping the step.

## Step 2 — Sameness check (before synthesis)

Before finalizing a synthesis, check the proposed layout/pattern against
common AI-generated defaults for this screen type (hero+cards+gradient CTA
for landing pages, sidebar+card-grid dashboards, generic modal wizards,
etc.). For each element that matches a common default, either:
- justify it from product context (it's the right, boring choice — that's
  fine when it serves the user), or
- propose a variation grounded in this product's actual content, brand, or
  user priority instead of an arbitrary alternative for its own sake.

Distinctiveness is never an excuse to violate accessibility, the design
system, or the source-of-truth hierarchy in `ARCHITECTURE.md` — see
`rules/distinctiveness-rules.md` rule 6.

## Step 3 — Polish pass (before spec is marked complete)

Confirm the spec explicitly covers, not just the happy path:
- loading, empty, error, and success states with real content (not
  "TODO"),
- at least one micro-interaction or transition note where it matters
  (hover/focus feedback, a state change, a drawer/modal entrance),
- spacing/rhythm using the design system's scale, not arbitrary values,
- copy that fits the actual product voice, not lorem-ipsum-adjacent
  placeholder text.

A spec that only describes the default visual layout has not passed the
polish pass, regardless of the active mode.

## Output

No separate artifact — this is a process gate. Record the challenge (step
1) and any sameness-check justifications (step 2) inline in
`.ui-engineering/decisions/<feature>.json` or `synthesis/<feature>.json`
so they're inspectable later via `/uiEng why`.
