---
access: public
aliases: []
claim_ids:
- clm_1c90b86d4e8b96db524ccf6dcd9f644b80fcb71a713068a8aa99dca13fd6d17b
- clm_27451c3268805d2a8496acaa1f7f12edf909de6bba7c96be5d90dfd8a709318f
- clm_3c7ce68dbbf6eee3d825392e647d9a80732755843ada1872d762ea421e26cc1d
- clm_5f36c5ea8b6ce0a874be89d00de2a3c9c45d6479e32ba7b4c75b8ea395571645
- clm_7fc09b5b0759d72c0499d8cf22b7d2352a6042e18241b3089ba761325f1831d3
- clm_a62a0b97bad6c36191699dc2cdf0c0e2576a5162cbc4d85f869a3020fae4cff5
- clm_c4b1ff73576888c48feeb92f86ad5c0a074f1abb8d16c1b66019a397cc770dcf
maturity: draft
page_id: pg_bdf4c042e7bb517c8d90250efd5b0dc6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_842d991c73375108b27a474a2492c958
title: PolymathWizard/BHIL-AI-First-Development-Toolkit/README.md @ 161f8e5311bd
updated_at: '2026-09-14T04:16:31Z'
---

# PolymathWizard/BHIL-AI-First-Development-Toolkit/README.md @ 161f8e5311bd

<!-- rcw:begin owner=source:src_842d991c73375108b27a474a2492c958 block=evidence -->
- The toolkit prescribes a traceable artifact chain — PRD (what), SPEC (how), ADR (why), TASK (steps) — flowing through code, review, deploy, and closed by a sprint retrospective. [@claim:clm_1c90b86d4e8b96db524ccf6dcd9f644b80fcb71a713068a8aa99dca13fd6d17b]
- Beyond standard ADRs, the toolkit defines three AI-native ADR categories — model selection, prompt strategy, and agent orchestration — each with its own template. [@claim:clm_27451c3268805d2a8496acaa1f7f12edf909de6bba7c96be5d90dfd8a709318f]
- Traceability links are asymmetric: children reference parents (e.g., SPECs reference parent PRD-NNN; TASKs reference spec and ADRs), while PRDs reference nothing upstream. [@claim:clm_3c7ce68dbbf6eee3d825392e647d9a80732755843ada1872d762ea421e26cc1d]
- Every artifact carries a traceability ID in YAML frontmatter with defined formats such as PRD-NNN, SPEC-NNN, ADR-NNN, TASK-NNN, S-NN, and PV-NNN. [@claim:clm_5f36c5ea8b6ce0a874be89d00de2a3c9c45d6479e32ba7b4c75b8ea395571645]
- The repository ships copy-and-fill templates including PRD, SPEC, TASK, sprint plan, and four ADR variants: core MADR-style, model-selection, prompt-strategy, and agent-orchestration. [@claim:clm_7fc09b5b0759d72c0499d8cf22b7d2352a6042e18241b3089ba761325f1831d3]
- The methodology assigns RuVector the role of maintaining persistent memory across sessions so agent context does not start cold; RuFlo optionally orchestrates agents across the artifact chain. [@claim:clm_a62a0b97bad6c36191699dc2cdf0c0e2576a5162cbc4d85f869a3020fae4cff5]
- The toolkit is released under the MIT License, with copyright attributed to BarryHurd.com. [@claim:clm_c4b1ff73576888c48feeb92f86ad5c0a074f1abb8d16c1b66019a397cc770dcf]
<!-- rcw:end owner=source:src_842d991c73375108b27a474a2492c958 block=evidence -->

## Researcher notes

