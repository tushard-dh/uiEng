# Synthesis

Synthesis is a controlled composition of patterns from multiple references.

## Required behavior

- Never concatenate references blindly.
- Resolve conflicts explicitly.
- Apply product requirements first.
- Normalize all visual primitives to the internal design system.
- Record contribution/provenance.

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
