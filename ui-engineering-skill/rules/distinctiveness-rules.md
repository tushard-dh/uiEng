# Distinctiveness Rules

These rules exist to counter the known failure modes of "vibe coding" UI
generation: visual homogenization, shallow prompting, screens that
function but feel undesigned, uncritical execution of requests, and
prototypes that don't survive real growth. See
`workflows/distinctiveness.md` for the process; this file is the
non-negotiable rule set behind it.

1. Never default to the most statistically common layout for a given
   screen type (e.g. hero + 3-feature-cards + gradient CTA for landing
   pages; sidebar + top-right avatar + card-grid for dashboards) without
   first checking whether it actually fits this product's content,
   information priority, and brand — not just "modern SaaS" convention.
2. Every synthesis must be traceable to specific product context
   (requirements, user roles, existing brand/design system), not to
   "what most apps do." If a choice cannot be justified from product
   context, treat it as a low-confidence default and say so.
3. Never silently execute a shallow or ambiguous request. Surface at
   least one structural question, risk, or alternative before building —
   see the challenge step in `workflows/distinctiveness.md`. This applies
   even when the user has not asked for critique.
4. States, motion, and micro-interactions are part of the specification,
   not an afterthought. A spec that only covers the default/happy-path
   visual layout is incomplete regardless of mode.
5. Reuse the component catalog and design tokens over one-off styling
   (already required by rule 16 in `SKILL.md`) specifically because
   one-off styling is what causes prototypes to become unmaintainable as
   features grow — this rule exists for scalability, not just tidiness.
6. Do not treat visual novelty as success on its own. A distinctive layout
   that ignores accessibility, the design system, or the actual user task
   is a worse outcome than a conventional one that serves the user well.
   Distinctiveness is a tiebreaker among options that already satisfy the
   source-of-truth hierarchy in `ARCHITECTURE.md`, never a reason to
   violate it.
