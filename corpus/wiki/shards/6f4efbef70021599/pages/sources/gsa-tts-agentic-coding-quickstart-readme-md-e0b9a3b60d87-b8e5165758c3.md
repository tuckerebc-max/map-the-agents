---
access: public
aliases: []
claim_ids:
- clm_48943dbfaf9facae9d6e09e77b8c14547c34dddc49d9c1ff44dad1ca2ba20608
- clm_716833d4b1537dab00f86cfb1764f13d54581aed86f384bc781595fc1b9a8727
- clm_a4600bd06623848c727681178028fff7c21b85aef18643951c0cd1620d0e77eb
- clm_d0ba634522f37ab024d8e9e5d7d8dc6b73299a4817392db6862c88ffdc5bf36c
- clm_eaefae11f3ee353787874776163f43a32a7ef20b75c67b93c73163277bb12d99
maturity: draft
page_id: pg_277204203f9c5027a6d2b8e5165758c3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca5d5fff1b9b51e286b58280ed68180d
title: GSA-TTS/agentic-coding-quickstart/README.md @ e0b9a3b60d87
updated_at: '2026-09-14T03:54:37Z'
---

# GSA-TTS/agentic-coding-quickstart/README.md @ e0b9a3b60d87

<!-- rcw:begin owner=source:src_ca5d5fff1b9b51e286b58280ed68180d block=evidence -->
- The product's entry point is the `acq` CLI, invoked e.g. as `acq run opencode ~/my-project`, which runs the agent in a sandbox configured for federal usage. [@claim:clm_48943dbfaf9facae9d6e09e77b8c14547c34dddc49d9c1ff44dad1ca2ba20608]
- acq supports two shipped isolation backends: msb (microsandbox, a lightweight open-source microVM runtime, the default) and sbx (Docker Sandboxes), with a Podman-based 'ppp' backend listed as in development. [@claim:clm_716833d4b1537dab00f86cfb1764f13d54581aed86f384bc781595fc1b9a8727]
- The quickstart targets federal teams using AI coding agents, connecting them to USAi (GSA's LLM gateway at api.gsa.usai.gov), and is classified as a local development environment for Low/Moderate-impact work, not a production/hosted environment. [@claim:clm_a4600bd06623848c727681178028fff7c21b85aef18643951c0cd1620d0e77eb]
- Secrets are injected at runtime via a proxy/host-env binding (e.g. `--secret USAI_API_KEY@api.gsa.usai.gov`), so real secret values never enter the guest VM or container. [@claim:clm_d0ba634522f37ab024d8e9e5d7d8dc6b73299a4817392db6862c88ffdc5bf36c]
- The companion playbook provides agent skills following the agentskills.io standard (e.g. federal-security-controls-lookup, ato-package, code-review), symlinked into ~/.agents/skills when a sandbox launches so agents discover them automatically. [@claim:clm_eaefae11f3ee353787874776163f43a32a7ef20b75c67b93c73163277bb12d99]
<!-- rcw:end owner=source:src_ca5d5fff1b9b51e286b58280ed68180d block=evidence -->

## Researcher notes

