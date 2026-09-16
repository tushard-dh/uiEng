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

## Completion

Blocking findings must be fixed or explicitly accepted.
