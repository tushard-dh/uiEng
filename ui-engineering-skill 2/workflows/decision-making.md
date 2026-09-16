# Decision Making

## Purpose

Choose the best UX approach for the product, not the prettiest reference.

## Decision sequence

1. State the decision.
2. Identify options.
3. Evaluate against product context.
4. Identify tradeoffs.
5. Recommend an option.
6. Ask the user when a high-impact choice remains unresolved.
7. Record the final decision and rationale.

## Priority

1. Product requirements
2. Accessibility/security
3. Internal design system
4. Established UX conventions
5. User preference
6. Reference preference
7. AI recommendation

## Confidence

Use:

- high
- medium
- low
- unknown

Do not invent numeric scores unless measurable criteria exist.

## Ask rule

Ask only questions that materially change implementation.

Example:

```text
How should physician details open?
A. Full page
B. Drawer
C. Modal
```

Then record:

```yaml
id: UX-001
question: "How should physician details open?"
selected: drawer
reasoning:
  - preserves recruiter search context
  - supports rapid review
confidence: high
```

## Why command

`/uiEng why <decision-or-screen>` should retrieve the stored decision and
explain:
- what was chosen
- alternatives
- evidence
- tradeoffs
- provenance
- confidence
