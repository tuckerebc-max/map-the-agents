# lajosdeme/mole

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fcb92379120d @ 955c751591a38231

## Summary (orientation draft, not independently verified)

Selected evidence records: Mole is a deep-research agent that decomposes a question, searches, extracts claims, quote-checks each against its source, detects contradictions, and writes a cited answer. Every model call is reserved before it happens and settled after, against a ledger with non-negative constraints in the database schema, so a set budget ceiling is enforced rather than estimated.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Mole is a deep-research agent that decomposes a question, searches, extracts claims, quote-checks each against its source, detects contradictions, and writes a cited answer. -- evidence: [README.md#L10-L14](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L10-L14)
- components (1 claim(s)):
  - [observation/documented] The pipeline runs planner, executor, actor (search/fetch/extract/mine), verifier (pairing, adjudication, claim graph, re-read sampling), and output stages, with three actor types: web, academic (Crossref, OpenAlex, arXiv, PubMed), and local_compute. -- evidence: [README.md#L267-L270](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L267-L270), [README.md#L255-L265](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L255-L265)
- design-choices (3 claim(s)):
  - [observation/documented] Every model call is reserved before it happens and settled after, against a ledger with non-negative constraints in the database schema, so a set budget ceiling is enforced rather than estimated. -- evidence: [README.md#L31-L34](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L31-L34), [README.md#L10-L14](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L10-L14)
  - [observation/documented] Claims whose quotes do not appear verbatim in the mined page are discarded at extraction; surviving claims can be re-read against sources and marked unsupported in the report. -- evidence: [README.md#L36-L40](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L36-L40)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: code contributions require a CLA plus Signed-off-by (DCO) on every commit; the project's non-negotiable practice is to falsify your own fix by reverting the mechanism and confirming the test fails, and PRs must pass gofmt, go build, go test (no new skips) and go vet. -- evidence: [CONTRIBUTING.md#L42-L45](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L42-L45), [README.md#L298-L300](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L298-L300), [CONTRIBUTING.md#L65-L68](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L65-L68), [README.md#L304-L307](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L304-L307), [README.md#L309-L313](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L309-L313), [CONTRIBUTING.md#L113-L118](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L113-L118)
  - [observation/documented] Repository development practice: dependencies policy forbids copyleft (GPL/LGPL/MPL/AGPL) and cgo-requiring dependencies, one change per pull request, and Conventional Commits subjects with explanatory bodies. -- evidence: [CONTRIBUTING.md#L101-L103](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L101-L103), [CONTRIBUTING.md#L107-L109](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L107-L109), [CONTRIBUTING.md#L126-L129](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L126-L129)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Toolkit mode (`mole serve --toolkit`) exposes fourteen `mole.<tool>` tools alongside the research tools, including search/fetch through an SSRF guard, robots handling and rate limiter, plus verify_quote, claim_add, aggregate and dataset tools. -- evidence: [README.md#L234-L241](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L234-L241), [README.md#L231-L232](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L231-L232), [README.md#L218-L220](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L218-L220)
- evaluation (1 claim(s)):
More evidence: [full detail](mole.detail.md)

Metadata and full claim list: [full detail](mole.detail.md)
Human notes ([notes](mole.notes.md), never overwritten by build)

[Back to map index](../../index.md)
