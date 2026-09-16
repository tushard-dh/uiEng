# Physician Matching Example

Example command sequence:

```text
/uiEng init
/uiEng discover physician-matching
/uiEng ask
/uiEng mobbin
/uiEng analyze
/uiEng compare
/uiEng synthesize
/uiEng spec physician-matching
/uiEng build physician-matching
/uiEng review
/uiEng status
```

Expected UI concerns:
- recruiter dashboard
- physician search
- specialty filters
- availability filters
- hospital privilege indicators
- physician detail view
- AI extraction/review state
- loading/empty/error states
- responsive table behavior
- permission-aware actions

Backend/API contracts remain owned by the application's backend SDD/API
specification. This skill consumes those contracts and does not invent them.
