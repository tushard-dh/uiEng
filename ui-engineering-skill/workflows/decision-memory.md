# Decision Memory

Purpose: stop re-asking the same high-impact question on every new
feature, and keep the product consistent over time by promoting decisions
that repeat across features into project-wide patterns.

This is a reasoning task (matching analogous questions across different
features), not a scripted one — see `SKILL.md` "Scripts" rule.

## Storage

`.ui-engineering/decisions/patterns.json` using
`schemas/ui-pattern.schema.json`. This is project-wide, distinct from
`.ui-engineering/decisions/<feature>.json` (per-feature, `schemas/
ui-decision.schema.json`).

## Before asking a question

(This runs inside `workflows/decision-making.md` step 6, before asking.)

1. Generalize the question to a topic broad enough to match analogous
   decisions in other features, narrow enough not to conflate unrelated
   ones. Example: "Should physician details open in a drawer or full
   page?" → topic "detail view presentation for record-review flows", not
   "physician details" (too narrow to ever match again) and not "modal
   usage" (too broad — would wrongly match unrelated confirm-dialog
   decisions).
2. Search `patterns.json` for a matching topic.
3. If a match exists with `status: "established"`:
   - Do not ask the question again.
   - Apply the resolved answer.
   - Record it in the feature's own decisions file with
     `source: ["pattern:<id>"]`.
   - Tell the user which established pattern was reused, in one line, so
     it stays visible and overridable rather than silent.
4. If a match exists with `status: "proposed"` (a single prior
   confirmation) or no match exists, ask normally.

## After recording a decision

1. Search `patterns.json` for a topic match.
2. If none exists, add a new entry with `status: "proposed"` and one
   confirmation.
3. If a `proposed` entry exists and this decision agrees with it, append
   this feature to `confirmations`. Promote to `status: "established"`
   once confirmations reach `decision_memory.promote_after_confirmations`
   (`config.yaml`, default 2).
4. If a `proposed` or `established` entry exists and this decision
   disagrees (a different answer was chosen this time):
   - Do not silently overwrite it.
   - Ask the user whether this is a one-off exception for this feature, or
     should replace the established pattern going forward.
   - If replacing: set `status: "overridden"` on the old entry (kept for
     history/provenance, never deleted) and create a new entry for the new
     answer.

## Rules

1. Never auto-apply a `proposed` pattern (single confirmation) without
   asking — one instance is a decision, not yet a pattern.
2. Never merge two genuinely different topics just because their answers
   happen to match.
3. Patterns are proposals for consistency, not hard constraints — product
   requirements and accessibility/security always override an established
   pattern, per the same priority order as `workflows/decision-making.md`.
4. `/uiEng why <pattern-id>` explains a pattern exactly like a
   feature-level decision: resolved answer, confirming features, evidence,
   confidence, and any override history.
5. `/uiEng patterns` lists every stored pattern with its status and
   confirmation count.

## Output

`.ui-engineering/decisions/patterns.json` using
`schemas/ui-pattern.schema.json`.
