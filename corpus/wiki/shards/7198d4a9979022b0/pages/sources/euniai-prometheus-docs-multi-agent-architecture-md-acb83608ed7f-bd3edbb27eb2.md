---
access: public
aliases: []
claim_ids:
- clm_2481920edbd1cdf058591e47861baf814d430f893a4876f03c7f54ef5962a79e
- clm_5c55f8bdb469d823199c245dca25af81d6ebc7bfe9ae38ce991fcdbc1122d8c4
- clm_a7d623e87abb0a1562618cd4240ed1d87148e8a53ebe6746e1e32feeac92dc4b
- clm_ffad3c20a3a1bdc9233b5338442c7b1002e6aedda687a51232a524c5b71af854
maturity: draft
page_id: pg_93f6ca5364975c36a227bd3edbb27eb2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_234d50c3503d5471ba57b8aefd5787b2
title: EuniAI/Prometheus/docs/Multi-Agent-Architecture.md @ acb83608ed7f
updated_at: '2026-09-14T01:48:13Z'
---

# EuniAI/Prometheus/docs/Multi-Agent-Architecture.md @ acb83608ed7f

<!-- rcw:begin owner=source:src_234d50c3503d5471ba57b8aefd5787b2 block=evidence -->
- Agents communicate through shared LangGraph state: each subgraph has a typed state dictionary, state flows through nodes, child subgraphs inherit parent state, and results return via state. [@claim:clm_2481920edbd1cdf058591e47861baf814d430f893a4876f03c7f54ef5962a79e]
- The issue resolution agent generates multiple candidate patches, validates them against reproduction tests (required) plus optional regression and existing tests, and selects the best patch using an LLM with retry on failure. [@claim:clm_5c55f8bdb469d823199c245dca25af81d6ebc7bfe9ae38ce991fcdbc1122d8c4]
- The bug reproduction agent generates reproduction tests via LLM, executes them in Docker, evaluates success, and retries with feedback in iterative loops. [@claim:clm_a7d623e87abb0a1562618cd4240ed1d87148e8a53ebe6746e1e32feeac92dc4b]
- The Environment Build Agent is documented as in-progress with only planned features (auto-detecting project type, installing dependencies, configuring build tools), and PR review, feature implementation, and documentation agents are listed as future enhancements. [@claim:clm_ffad3c20a3a1bdc9233b5338442c7b1002e6aedda687a51232a524c5b71af854]
<!-- rcw:end owner=source:src_234d50c3503d5471ba57b8aefd5787b2 block=evidence -->

## Researcher notes

