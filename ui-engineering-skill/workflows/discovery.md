# Discovery

## Objective

Understand the feature before choosing a visual solution.

## Required inputs

- feature name
- product purpose
- user roles
- primary task
- secondary tasks
- user research signal (a pain point, complaint, support ticket, or
  observed behavior motivating this feature — see the note below)
- business constraints
- existing routes
- existing components
- API/data contracts
- responsive target
- accessibility requirements
- permissions

If "user research signal" is genuinely unavailable, mark it `unknown`
rather than skipping it silently — a feature designed with zero grounding
in an actual user problem is exactly the shallow, "vibe coded" outcome
this skill exists to avoid (`workflows/distinctiveness.md`). Marking it
unknown is honest; omitting it is not.

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

## Readiness checklist

Before moving to reference selection or spec, output a checklist marking
each required input as:

- `known` — captured with a source (user, code, API contract),
- `assumed` — a reasonable default, stated explicitly so it can be
  challenged,
- `unknown` — genuinely missing; call out whether it blocks proceeding.

Example:

```text
Readiness for "bulk-invite-recruiters":
✅ user roles           — known (admin, recruiter)
✅ primary task         — known (invite N candidates at once)
❓ API/data contracts   — unknown: no bulk-invite endpoint found; confirm
                          with backend before spec
🔶 responsive target    — assumed: desktop-first (matches rest of app)
❓ user research signal — unknown: no complaint/ticket referenced
```

Do not silently proceed past a blocking `unknown` (e.g. a missing API
contract that spec/build would need) — surface it and ask, or explicitly
record it as an accepted risk.

Also apply the challenge step from `workflows/distinctiveness.md` here,
before the checklist is considered final.

## Output

Update:

```text
.ui-engineering/project-context.md
```

using `templates/project-context.md` (includes the readiness checklist
section), and, when appropriate:

```text
.ui-engineering/status.yaml
```
