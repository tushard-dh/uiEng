# Synthesis

Synthesis is a controlled composition of patterns from multiple references.

Before finalizing, run the sameness check in
`workflows/distinctiveness.md` step 2 — this is what stops the skill from
defaulting to the most statistically common AI-generated layout for the
screen type instead of one grounded in this product's actual context.

## Required behavior

- Never concatenate references blindly.
- Resolve conflicts explicitly.
- Apply product requirements first.
- Normalize all visual primitives to the internal design system.
- Record contribution/provenance.
- Produce 1 recommendation in `quick`/`standard` mode. In `thorough` mode,
  produce 2–3 scored variants with explicit tradeoffs instead, and ask the
  user to pick one before moving to spec (`workflows/mode.md`).

Example:

```yaml
synthesis:
  name: physician-management
  references:
    - id: mobbin-dashboard-01
      contribution:
        - navigation
        - page-hierarchy
        - dashboard-layout
    - id: mobbin-table-07
      contribution:
        - search
        - filtering
        - table
        - row-actions
  rules:
    navigation: reference_1
    page_structure: reference_1
    table: reference_2
    filters: reference_2
    typography: internal_design_system
    colors: internal_design_system
```

## Conflict resolution

Example:

```text
Reference A: large rounded cards
Reference B: dense square cards

Conflict: card radius

Decision:
Use internal design-system radius.medium.

Reason:
Consistency is more valuable than copying either reference.
```
