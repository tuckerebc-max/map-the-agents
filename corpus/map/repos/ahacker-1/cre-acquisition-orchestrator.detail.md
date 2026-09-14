# ahacker-1/cre-acquisition-orchestrator -- full detail

[Back to orientation](cre-acquisition-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ahacker-1/cre-acquisition-orchestrator/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/071fa960b755d387.json](../../../wiki/dossiers/ahacker-1/cre-acquisition-orchestrator/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/071fa960b755d387.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The product includes a dashboard Conversation Desk where operators pick a deal, one of 31 registered AI roles, and in-scope deal documents to continue a retained thread. -- evidence: [CHANGELOG.md#L11-L13](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L11-L13) (`clm_e8258f15fc0664e1f08a5bfd9dc0d7e0a81e526971875a04144dee7ff31b44d2`)
- [observation/documented] XLSX/CSV rent rolls and T12s can become reviewable candidate deal fields carrying parser metadata, file hashes, confidence, and source-location provenance. -- evidence: [CHANGELOG.md#L501-L504](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L501-L504) (`clm_7f25fb8d6e4080a308a443e72d6354c38a595d9b7855ba7ca26ec5e2bd83842d`)
- [observation/documented] Scanned/image-only PDFs are rendered with PyMuPDF and OCR'd locally via tesseract.js, producing candidate fields with snippets, page provenance, source hash, and confidence, with no external OCR service. -- evidence: [CHANGELOG.md#L320-L330](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L320-L330) (`clm_d7084f17cd547ed3ca8c203f45b8e0bcee97b29e568bc68aba7930fbcac8928f`)

## design-choices (1 claim(s))

- [observation/documented] The product follows a local-first, operator-review contract: extracted values are review-gated candidates that must be approved and applied before changing deal inputs. -- evidence: [CHANGELOG.md#L350-L355](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L350-L355), [CHANGELOG.md#L501-L504](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L501-L504) (`clm_5c2db328859b233e13a48395eab4af967c4b11da401c2387e94bc8e0ec1d93b5`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the changelog lists release gates that must pass before tagging v3.6.0, including verify:v3, release:check, validate:docs, npm test, dashboard typecheck/build, dependency audits, and Playwright coverage. -- evidence: [CHANGELOG.md#L70-L70](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L70-L70), [CHANGELOG.md#L72-L83](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L72-L83) (`clm_cef3faa8428a87d5027ea5ec08bb225e57f07a5537efe3aec9c559cff8b89f98`)
- [observation/documented] Repository development practice: an audit progress ledger tracks batched hardening work with gate status, noting tsc must be run from dashboard/ because npm --prefix exec swallows compiler args. -- evidence: [AUDIT-PROGRESS.md#L5-L26](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/AUDIT-PROGRESS.md#L5-L26) (`clm_26c3e8d7acfa859bae326bb4ded89518de48ce4f3e6758936da6232cbf394643`)

## skills-patterns (1 claim(s))

- [observation/documented] The agent registry reports 31 roles and 8 skills, including four document-ingestion roles and a self-review-protocol skill. -- evidence: [CHANGELOG.md#L457-L458](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L457-L458), [CHANGELOG.md#L462-L463](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L462-L463) (`clm_681fa4ba22e759248c4f344fce0cc9b68bdcac262385d44702896f8fc814f664`)

## interfaces (2 claim(s))

- [observation/documented] The changelog documents a conversation REST API and a WebSocket activity envelope for the dashboard's client/server architecture. -- evidence: [CHANGELOG.md#L59-L66](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L59-L66) (`clm_e92514a70a11937b1cc2867c34d7eec86b6a2134d8f326dda5151902c562e065`)
- [observation/documented] Thread, deal, and agent selection is encoded in the URL, supporting deep links, reload recovery, and browser Back/Forward navigation. -- evidence: [CHANGELOG.md#L17-L34](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L17-L34) (`clm_05494c3c9bbe1548560eca72dc50436d1e3ddf2e49c155ca89f00ff3ae474588`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The dashboard launches workflows on live Codex/ChatGPT by default, with a deterministic Simulation runtime kept as the no-credential fallback for demos, screenshots, and CI. -- evidence: [CHANGELOG.md#L210-L224](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L210-L224) (`clm_6fa35b2a371be739ffeb8ef31a854a9020badf7cc1d642cb346577bf211e8b46`)
- [observation/documented] The Codex runner threads a searchEnabled flag into agent prompts so agents actively look up and cite real market data; web search is on by default with a visible toggle. -- evidence: [CHANGELOG.md#L210-L224](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L210-L224) (`clm_26251368d15e104a292dcfe144e2f5e5e1e135435062fd30820b88a742cfaec4`)

## tools-permissions (1 claim(s))

- [observation/documented] Document conversations run from a fresh read-only evidence root with shell, browser, app, plugin, MCP, memory, skill, and web capabilities disabled, and unsafe IDs or cross-deal documents are rejected before execution. -- evidence: [CHANGELOG.md#L38-L55](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L38-L55) (`clm_b65c3923c72b3c287836d39b2c9d1171d664ddf3ab78b28ce55b9192dbb8825c`)

## evaluation (2 claim(s))

- [observation/documented] A live Codex evaluation over 8 synthetic benchmark deals reported 100% IC exact/directional match, 100% determinable financial accuracy, 100% red-flag and dealbreaker recall, and 0 partial failures. -- evidence: [CHANGELOG.md#L152-L161](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L152-L161) (`clm_d11f291baa2a5a2e0deb88d5162615e95e3b225db036c9ad442dd5ad86c3e25a`)
- [observation/documented] An evaluation harness scores the orchestrator on 8 synthetic benchmark deals against committed ground truth, writing scorecard.json and TRUST-REPORT.md; the cited text names deterministic extraction and the simulation fixture as measured layers. -- evidence: [CHANGELOG.md#L429-L432](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L429-L432) (`clm_980a694c4f605d3f40910c3fc4db39317f86a5ee8320efa4a3998c962877972c`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The changelog identifies model-dependent returns as the documented weak spot, scoring 25% in the reported live evaluation. -- evidence: [CHANGELOG.md#L152-L161](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L152-L161), [CHANGELOG.md#L179-L185](https://github.com/ahacker-1/cre-acquisition-orchestrator/blob/a1cdd7f680a4dcf2f5e70a8380d6eb5eaccda878/CHANGELOG.md#L179-L185) (`clm_29e2f41ea0f9c640985434e0895650d4aa074fa2a95035185245b69fdadec53d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

