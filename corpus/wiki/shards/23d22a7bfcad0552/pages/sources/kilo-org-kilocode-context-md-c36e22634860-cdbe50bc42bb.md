---
access: public
aliases: []
claim_ids:
- clm_7065836d8d126c3c73cab862751e87c3c8b23879aef152eebaba77b39db2cbeb
- clm_82a1dc7ff3dc65c425b84d05768f618fea08a90c56049220bcd51a6e2ccfba6e
- clm_97c56a1931f126ae17e420eb8a81d0d87e8ee25f72f11ab519f9017da33f74be
- clm_c5148cdb21b2e43917cead849e0db5672cb0a2e6768276469370f2ceb19246df
maturity: draft
page_id: pg_94f52b87669d52728bfecdbe50bc42bb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8aff3e65fa025adaadc7d8b9baaa8b3a
title: Kilo-Org/kilocode/CONTEXT.md @ c36e22634860
updated_at: '2026-09-14T02:09:52Z'
---

# Kilo-Org/kilocode/CONTEXT.md @ c36e22634860

<!-- rcw:begin owner=source:src_8aff3e65fa025adaadc7d8b9baaa8b3a block=evidence -->
- Tool output persisted in session history is size-bounded by the Tool Registry; oversized output is retained in a temporary managed tool-output file under a shared directory. [@claim:clm_7065836d8d126c3c73cab862751e87c3c8b23879aef152eebaba77b39db2cbeb]
- The runtime defines a session context model: a System Context assembled from typed Context Sources, Session History projected per provider turn, and a Context Snapshot tracking each source's last-admitted value. [@claim:clm_82a1dc7ff3dc65c425b84d05768f618fea08a90c56049220bcd51a6e2ccfba6e]
- Context changes are admitted lazily at a Safe Provider-Turn Boundary rather than pushed asynchronously, and changes from multiple sources at one boundary combine into a single Mid-Conversation System Message. [@claim:clm_97c56a1931f126ae17e420eb8a81d0d87e8ee25f72f11ab519f9017da33f74be]
- The architecture exposes a public HttpApi from which Promise and Effect clients are generated, plus an Embedded OpenCode in-process host using an in-memory HTTP transport against the same router. [@claim:clm_c5148cdb21b2e43917cead849e0db5672cb0a2e6768276469370f2ceb19246df]
<!-- rcw:end owner=source:src_8aff3e65fa025adaadc7d8b9baaa8b3a block=evidence -->

## Researcher notes

