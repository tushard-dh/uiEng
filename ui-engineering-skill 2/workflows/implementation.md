# Implementation

Only implement after a sufficiently complete UI specification exists.

## Process

1. Read UI spec.
2. Inspect existing design-system components.
3. Inspect routes.
4. Inspect API client/types.
5. Identify reusable components.
6. Implement the smallest maintainable change.
7. Add required states.
8. Add responsive behavior.
9. Add accessibility.
10. Add tests for important interactions.
11. Run validation.

## Avoid

- duplicate components
- hardcoded design tokens
- arbitrary spacing
- fake API fields
- inaccessible controls
- hidden state handling
- large unrelated refactors

## Enterprise frontend rule

Prefer composition of approved primitives and patterns over one-off page
implementations.
