# Reference Analysis

Analyze each selected reference independently before comparing references.

## Evidence classes

Every important statement must be classified:

- `observed`: directly visible in the supplied reference.
- `inferred`: a reasonable interpretation not directly visible.
- `unknown`: cannot be determined from the reference.

Never convert inferred behavior into observed behavior.

## Analysis dimensions

1. Product context
2. Information architecture
3. Layout
4. Visual language
5. Components
6. Composition/relationships
7. Interactions
8. States
9. Responsive behavior
10. Accessibility
11. Content design
12. Semantic design-token roles
13. Patterns
14. Constraints
15. Provenance

## Token rule

Do not copy arbitrary raw colors or pixel values into application code.

Instead infer semantic roles such as:

```text
surface.default
surface.raised
text.primary
text.secondary
border.default
action.primary
status.success
status.warning
status.error
```

Then map these to the internal design system.

## Output

Produce:

```text
.ui-engineering/knowledge/<feature-or-pattern>.json
```

using `schemas/ui-knowledge.schema.json`.
