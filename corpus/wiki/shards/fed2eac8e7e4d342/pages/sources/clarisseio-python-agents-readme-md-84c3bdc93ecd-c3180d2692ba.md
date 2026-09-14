---
access: public
aliases: []
claim_ids:
- clm_1e1d0808139d05dba3864b86d25529872625311a4effe2d41a99e60192c16b84
- clm_9c4e6d06d460d4142badf7aa52e19bce7e1bccf67582aff4296e4ed4dc407e4e
- clm_a8de7343144be5b87745fe02e08557bee254684a2e777138baec5ccf4c9f557a
- clm_dde7c03a70959a2e0be462959b04513032da6fa5df74c4f487b3c7f017da1258
- clm_e0f554009905401c66358f2863bc660907310f45ee2d059481676b150e47bcbf
- clm_e323144efd2cd4e2b3eed95db1b65ff5f592b13cb7d11b6738292f13d1cc45e7
- clm_f04908d4897156bb7710f69f1b00a1f1d173ef83a828ad73d94ebf0ca2c01ec2
maturity: draft
page_id: pg_9d571ec5fe0758a080eac3180d2692ba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f18ca62e82445030871acb4bf623017b
title: clarisseIO/python-agents/README.md @ 84c3bdc93ecd
updated_at: '2026-09-14T02:00:10Z'
---

# clarisseIO/python-agents/README.md @ 84c3bdc93ecd

<!-- rcw:begin owner=source:src_f18ca62e82445030871acb4bf623017b block=evidence -->
- The framework ships modules for agents, LLMs, prompt templating (Mustache-based), memory, tools, cache, errors, adapters, and logger, with agents and LLMs described as base classes defining common interfaces. [@claim:clm_1e1d0808139d05dba3864b86d25529872625311a4effe2d41a99e60192c16b84]
- The run method supports an observe callback exposing an emitter where listeners can subscribe to events such as 'update' during execution; observe is also supported on tools and LLMs. [@claim:clm_9c4e6d06d460d4142badf7aa52e19bce7e1bccf67582aff4296e4ed4dc407e4e]
- The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other popular LLMs stated as ongoing work. [@claim:clm_a8de7343144be5b87745fe02e08557bee254684a2e777138baec5ccf4c9f557a]
- Agents are constructed with an LLM, memory, and tools, and run via an awaited run({prompt}) call whose result exposes response.result.text. [@claim:clm_dde7c03a70959a2e0be462959b04513032da6fa5df74c4f487b3c7f017da1258]
- The legal notice states the code is an IBM open-source project, not an IBM product, with no obligation to provide enhancements, updates, support, or ongoing maintenance. [@claim:clm_e0f554009905401c66358f2863bc660907310f45ee2d059481676b150e47bcbf]
- The package installs via npm or yarn as 'Clarisse-agent-framework', and examples use an Ollama chat LLM adapter defaulting to llama3.1 (8B) with the 70B model recommended. [@claim:clm_e323144efd2cd4e2b3eed95db1b65ff5f592b13cb7d11b6738292f13d1cc45e7]
- Repository development practice: local setup involves cloning, yarn install --immutable && yarn prepare, creating .env from .env.template, and running examples via yarn start with a file path; contributions follow CONTRIBUTING.md. [@claim:clm_f04908d4897156bb7710f69f1b00a1f1d173ef83a828ad73d94ebf0ca2c01ec2]
<!-- rcw:end owner=source:src_f18ca62e82445030871acb4bf623017b block=evidence -->

## Researcher notes

