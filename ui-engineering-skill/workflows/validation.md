# Validation

Validation has two layers.

## Deterministic validation

Use:

```bash
python scripts/validate_schema.py .ui-engineering
python scripts/validate_ui.py .
python scripts/status.py .
```

Static checks should identify:
- hardcoded color literals
- suspicious arbitrary spacing
- missing state declarations
- missing responsive declarations
- duplicated UI component names
- obvious accessibility omissions

These are signals, not substitutes for human UX review.

## AI review

Review:
- requirement coverage
- consistency
- usability
- information hierarchy
- interaction clarity
- state completeness
- accessibility
- responsive behavior
- design-system compliance
- polish pass (`workflows/distinctiveness.md` step 3): real content in
  every state, at least one micro-interaction/transition noted, spacing
  from the design system's scale — not just the happy path implemented

## Completion

Blocking findings must be fixed or explicitly accepted.
