# Workflow Mode

Purpose: give explicit control over depth vs. speed instead of one fixed
level of thoroughness, so the user can trade exhaustiveness for velocity
per feature.

## Setting the mode

- Persistent default: `.ui-engineering/config.yaml` → `workflow.mode`.
- Per-session override: `/uiEng mode <quick|standard|thorough>` — updates
  the persisted default until changed again.
- If unset, default to `standard`.

Announce the active mode at the start of `/uiEng discover` and `/uiEng
mobbin` (one line) so the user isn't surprised by how much, or how little,
gets asked or pulled.

## Modes

### quick

- Ask at most 2 high-impact questions. Auto-decide the rest using the
  priority order in `workflows/decision-making.md` plus any matching
  established pattern (`workflows/decision-memory.md`), and list every
  auto-decision made so the user can spot-check it.
- Pull at most 2 Mobbin references.
- Synthesis produces exactly 1 recommendation — no alternate variants.
- Spec covers required sections only (skip analytics/events unless the
  user explicitly asked for them).

### standard (default)

- Ask every high-impact question identified — no cap.
- Pull up to 5 Mobbin references.
- Synthesis produces 1 recommendation; alternatives are noted narratively
  but not fully specified.
- Spec covers every section listed in `SKILL.md` step 7 (Specify).

### thorough

- Ask every high-impact question, and also surface medium-impact ones that
  are genuinely ambiguous (never trivial/low-impact ones — rule 13 in
  `SKILL.md` still applies).
- Pull up to 10 Mobbin references, spanning multiple search queries if one
  query doesn't cover the pattern space.
- Synthesis produces 2–3 scored variants with explicit tradeoffs (see
  `workflows/synthesis.md`) and asks the user to pick one before moving to
  spec.
- Spec additionally includes edge cases and explicit acceptance criteria
  per state, beyond the required sections.

## Rules

1. Mode changes how much is asked or explored — never which accessibility,
   security, or product-requirement rules apply. Those are non-negotiable
   in every mode.
2. Mode does not change the source-of-truth hierarchy in
   `ARCHITECTURE.md`; it only changes how many options are generated
   before that hierarchy is applied.
3. Switching mode mid-feature only affects steps not yet completed —
   already-recorded decisions and specs are not retroactively changed.
4. `quick` mode auto-decisions still get persisted to the feature's
   decisions file with `confidence` and `reasoning`, exactly like an
   asked-and-answered decision — they are just not blocked on user input.

## Output

No dedicated artifact. Mode is read from `.ui-engineering/config.yaml` and
referenced by `workflows/discovery.md`, `workflows/decision-making.md`,
and `workflows/synthesis.md`.
