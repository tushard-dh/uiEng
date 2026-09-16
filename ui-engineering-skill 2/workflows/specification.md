# UI Specification

A UI specification is the contract between product intent and frontend
implementation.

## Required sections

- feature purpose
- target users
- routes
- screens
- page hierarchy
- layout
- components
- component states
- data model/bindings
- API dependencies
- interactions
- validation
- permissions
- responsive behavior
- accessibility
- analytics/events if required
- acceptance criteria
- reference provenance
- unresolved decisions

## State coverage

At minimum consider:

- default
- loading
- empty
- error
- success
- disabled
- selected
- focus
- permission denied
- validation error

Add feature-specific states when needed.

## API rule

Do not invent frontend API fields. Read the existing contract or mark the
field as unresolved.

## Acceptance criteria

Acceptance criteria should be testable.

Example:

```text
Given a recruiter with access to Physician Management,
when they search by physician name,
then matching physicians appear without a full page reload.
```
