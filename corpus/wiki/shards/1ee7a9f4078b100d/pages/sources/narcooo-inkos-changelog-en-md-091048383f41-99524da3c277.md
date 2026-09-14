---
access: public
aliases: []
claim_ids:
- clm_5b6ae0598c07a64af0973569496d5a6bf417eda076c07696525a8d2a2c6d295e
- clm_68b587e937f3178cfdbc8ac6cf6912d2aac2d56014a11d80afc447f1074cee36
- clm_ef4b9e97508cb52f912eb536c5c775ed395a997e7834e7bd2c1b2d7ee6ee9e5c
- clm_f1a54fe597ed80fa1bb23df6b9aa630849996aa2c6c471be10eb3f7a5ad7eeee
maturity: draft
page_id: pg_a658270facac522282d599524da3c277
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7b614c56382452c183d13519429e16df
title: Narcooo/inkos/CHANGELOG.en.md @ 091048383f41
updated_at: '2026-09-14T04:12:04Z'
---

# Narcooo/inkos/CHANGELOG.en.md @ 091048383f41

<!-- rcw:begin owner=source:src_7b614c56382452c183d13519429e16df block=evidence -->
- Version 1.8.0 ships 15 built-in professional skills (long-form writing/review, shorts, Play, scripts, storyboards, interactive film, translation, import, covers, de-AI-flavor, etc.), each with its own SKILL.md. [@claim:clm_5b6ae0598c07a64af0973569496d5a6bf417eda076c07696525a8d2a2c6d295e]
- Story memory, material library, and skill references share a SQLite FTS5/BM25 retrieval projection; source files remain authoritative and indexes are rebuildable, with results retaining source and location. [@claim:clm_68b587e937f3178cfdbc8ac6cf6912d2aac2d56014a11d80afc447f1074cee36]
- Prose, state, hooks, and run snapshots are validated in a chapter workspace and atomically committed together, so failures do not leave state advanced without persisted text. [@claim:clm_ef4b9e97508cb52f912eb536c5c775ed395a997e7834e7bd2c1b2d7ee6ee9e5c]
- The runtime is built on a pi-agent harness: the agent produces structured actions, and the host executes deterministic tools, manages confirmations and state, and judges completion from real files and tool results rather than model claims. [@claim:clm_f1a54fe597ed80fa1bb23df6b9aa630849996aa2c6c471be10eb3f7a5ad7eeee]
<!-- rcw:end owner=source:src_7b614c56382452c183d13519429e16df block=evidence -->

## Researcher notes

