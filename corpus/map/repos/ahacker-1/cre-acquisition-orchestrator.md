# ahacker-1/cre-acquisition-orchestrator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a1cdd7f680a4 @ 071fa960b755d387

## Summary (orientation draft, not independently verified)

Selected evidence records: The product includes a dashboard Conversation Desk where operators pick a deal, one of 31 registered AI roles, and in-scope deal documents to continue a retained thread. XLSX/CSV rent rolls and T12s can become reviewable candidate deal fields carrying parser metadata, file hashes, confidence, and source-location provenance.

## Source coverage

Source coverage (partial): 3 of 51 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The product includes a dashboard Conversation Desk where operators pick a deal, one of 31 registered AI roles, and in-scope deal documents to continue a retained thread. -- evidence: [CHANGELOG.md#L11-L13](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L11-L13)
  - [observation/documented] XLSX/CSV rent rolls and T12s can become reviewable candidate deal fields carrying parser metadata, file hashes, confidence, and source-location provenance. -- evidence: [CHANGELOG.md#L501-L504](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L501-L504)
- design-choices (1 claim(s)):
  - [observation/documented] The product follows a local-first, operator-review contract: extracted values are review-gated candidates that must be approved and applied before changing deal inputs. -- evidence: [CHANGELOG.md#L350-L355](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L350-L355), [CHANGELOG.md#L501-L504](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L501-L504)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the changelog lists release gates that must pass before tagging v3.6.0, including verify:v3, release:check, validate:docs, npm test, dashboard typecheck/build, dependency audits, and Playwright coverage. -- evidence: [CHANGELOG.md#L70-L70](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L70-L70), [CHANGELOG.md#L72-L83](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L72-L83)
  - [observation/documented] Repository development practice: an audit progress ledger tracks batched hardening work with gate status, noting tsc must be run from dashboard/ because npm --prefix exec swallows compiler args. -- evidence: [AUDIT-PROGRESS.md#L5-L26](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/AUDIT-PROGRESS.md#L5-L26)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent registry reports 31 roles and 8 skills, including four document-ingestion roles and a self-review-protocol skill. -- evidence: [CHANGELOG.md#L457-L458](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L457-L458), [CHANGELOG.md#L462-L463](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L462-L463)
- interfaces (2 claim(s)):
  - [observation/documented] The changelog documents a conversation REST API and a WebSocket activity envelope for the dashboard's client/server architecture. -- evidence: [CHANGELOG.md#L59-L66](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L59-L66)
  - [observation/documented] Thread, deal, and agent selection is encoded in the URL, supporting deep links, reload recovery, and browser Back/Forward navigation. -- evidence: [CHANGELOG.md#L17-L34](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L17-L34)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The dashboard launches workflows on live Codex/ChatGPT by default, with a deterministic Simulation runtime kept as the no-credential fallback for demos, screenshots, and CI. -- evidence: [CHANGELOG.md#L210-L224](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L210-L224)
  - [observation/documented] The Codex runner threads a searchEnabled flag into agent prompts so agents actively look up and cite real market data; web search is on by default with a visible toggle. -- evidence: [CHANGELOG.md#L210-L224](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L210-L224)
- tools-permissions (1 claim(s)):
More evidence: [full detail](cre-acquisition-orchestrator.detail.md)

Metadata and full claim list: [full detail](cre-acquisition-orchestrator.detail.md)
Human notes ([notes](cre-acquisition-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
