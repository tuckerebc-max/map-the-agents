---
access: public
aliases: []
claim_ids:
- clm_05494c3c9bbe1548560eca72dc50436d1e3ddf2e49c155ca89f00ff3ae474588
- clm_26251368d15e104a292dcfe144e2f5e5e1e135435062fd30820b88a742cfaec4
- clm_29e2f41ea0f9c640985434e0895650d4aa074fa2a95035185245b69fdadec53d
- clm_5c2db328859b233e13a48395eab4af967c4b11da401c2387e94bc8e0ec1d93b5
- clm_681fa4ba22e759248c4f344fce0cc9b68bdcac262385d44702896f8fc814f664
- clm_6fa35b2a371be739ffeb8ef31a854a9020badf7cc1d642cb346577bf211e8b46
- clm_7f25fb8d6e4080a308a443e72d6354c38a595d9b7855ba7ca26ec5e2bd83842d
- clm_980a694c4f605d3f40910c3fc4db39317f86a5ee8320efa4a3998c962877972c
- clm_b65c3923c72b3c287836d39b2c9d1171d664ddf3ab78b28ce55b9192dbb8825c
- clm_cef3faa8428a87d5027ea5ec08bb225e57f07a5537efe3aec9c559cff8b89f98
- clm_d11f291baa2a5a2e0deb88d5162615e95e3b225db036c9ad442dd5ad86c3e25a
- clm_d7084f17cd547ed3ca8c203f45b8e0bcee97b29e568bc68aba7930fbcac8928f
- clm_e8258f15fc0664e1f08a5bfd9dc0d7e0a81e526971875a04144dee7ff31b44d2
- clm_e92514a70a11937b1cc2867c34d7eec86b6a2134d8f326dda5151902c562e065
maturity: draft
page_id: pg_db19f530321d5ee68a6142be0e0b3966
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6ab3526533bf59348497ca2adf41cb8c
title: ahacker-1/cre-acquisition-orchestrator/CHANGELOG.md @ a1cdd7f680a4
updated_at: '2026-09-14T03:32:12Z'
---

# ahacker-1/cre-acquisition-orchestrator/CHANGELOG.md @ a1cdd7f680a4

<!-- rcw:begin owner=source:src_6ab3526533bf59348497ca2adf41cb8c block=evidence -->
- Thread, deal, and agent selection is encoded in the URL, supporting deep links, reload recovery, and browser Back/Forward navigation. [@claim:clm_05494c3c9bbe1548560eca72dc50436d1e3ddf2e49c155ca89f00ff3ae474588]
- The Codex runner threads a searchEnabled flag into agent prompts so agents actively look up and cite real market data; web search is on by default with a visible toggle. [@claim:clm_26251368d15e104a292dcfe144e2f5e5e1e135435062fd30820b88a742cfaec4]
- The changelog identifies model-dependent returns as the documented weak spot, scoring 25% in the reported live evaluation. [@claim:clm_29e2f41ea0f9c640985434e0895650d4aa074fa2a95035185245b69fdadec53d]
- The product follows a local-first, operator-review contract: extracted values are review-gated candidates that must be approved and applied before changing deal inputs. [@claim:clm_5c2db328859b233e13a48395eab4af967c4b11da401c2387e94bc8e0ec1d93b5]
- The agent registry reports 31 roles and 8 skills, including four document-ingestion roles and a self-review-protocol skill. [@claim:clm_681fa4ba22e759248c4f344fce0cc9b68bdcac262385d44702896f8fc814f664]
- The dashboard launches workflows on live Codex/ChatGPT by default, with a deterministic Simulation runtime kept as the no-credential fallback for demos, screenshots, and CI. [@claim:clm_6fa35b2a371be739ffeb8ef31a854a9020badf7cc1d642cb346577bf211e8b46]
- XLSX/CSV rent rolls and T12s can become reviewable candidate deal fields carrying parser metadata, file hashes, confidence, and source-location provenance. [@claim:clm_7f25fb8d6e4080a308a443e72d6354c38a595d9b7855ba7ca26ec5e2bd83842d]
- An evaluation harness scores the orchestrator on 8 synthetic benchmark deals against committed ground truth, writing scorecard.json and TRUST-REPORT.md; the cited text names deterministic extraction and the simulation fixture as measured layers. [@claim:clm_980a694c4f605d3f40910c3fc4db39317f86a5ee8320efa4a3998c962877972c]
- Document conversations run from a fresh read-only evidence root with shell, browser, app, plugin, MCP, memory, skill, and web capabilities disabled, and unsafe IDs or cross-deal documents are rejected before execution. [@claim:clm_b65c3923c72b3c287836d39b2c9d1171d664ddf3ab78b28ce55b9192dbb8825c]
- Repository development practice: the changelog lists release gates that must pass before tagging v3.6.0, including verify:v3, release:check, validate:docs, npm test, dashboard typecheck/build, dependency audits, and Playwright coverage. [@claim:clm_cef3faa8428a87d5027ea5ec08bb225e57f07a5537efe3aec9c559cff8b89f98]
- A live Codex evaluation over 8 synthetic benchmark deals reported 100% IC exact/directional match, 100% determinable financial accuracy, 100% red-flag and dealbreaker recall, and 0 partial failures. [@claim:clm_d11f291baa2a5a2e0deb88d5162615e95e3b225db036c9ad442dd5ad86c3e25a]
- Scanned/image-only PDFs are rendered with PyMuPDF and OCR'd locally via tesseract.js, producing candidate fields with snippets, page provenance, source hash, and confidence, with no external OCR service. [@claim:clm_d7084f17cd547ed3ca8c203f45b8e0bcee97b29e568bc68aba7930fbcac8928f]
- The product includes a dashboard Conversation Desk where operators pick a deal, one of 31 registered AI roles, and in-scope deal documents to continue a retained thread. [@claim:clm_e8258f15fc0664e1f08a5bfd9dc0d7e0a81e526971875a04144dee7ff31b44d2]
- The changelog documents a conversation REST API and a WebSocket activity envelope for the dashboard's client/server architecture. [@claim:clm_e92514a70a11937b1cc2867c34d7eec86b6a2134d8f326dda5151902c562e065]
<!-- rcw:end owner=source:src_6ab3526533bf59348497ca2adf41cb8c block=evidence -->

## Researcher notes

