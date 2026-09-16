# Discovery

## Objective

Understand the feature before choosing a visual solution.

## Required inputs

- feature name
- product purpose
- user roles
- primary task
- secondary tasks
- business constraints
- existing routes
- existing components
- API/data contracts
- responsive target
- accessibility requirements
- permissions

## Process

1. Inspect repository structure.
2. Locate frontend application.
3. Locate design system/components.
4. Locate routing.
5. Locate API client/types.
6. Inspect similar existing screens.
7. Extract product requirements.
8. Identify unknowns.
9. Classify unknowns by implementation impact.

## High-impact question rule

Ask a question when:

```text
uncertainty × implementation impact = high
```

Examples:
- table vs cards: ask
- drawer vs page: ask
- bulk actions: ask
- exact shadow value: usually do not ask
- exact spacing token when a token exists: do not ask

## Output

Update:

```text
.ui-engineering/project-context.md
```

and, when appropriate:

```text
.ui-engineering/status.yaml
```
