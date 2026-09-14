---
access: public
aliases: []
claim_ids:
- clm_18717ad39db8fd8ae98ae08317b7513eb2c705203d59af5ec9935a38f4171686
- clm_3469e33fb11471d3e0dea4d24e2d3b09e7b2c47a3614b426314ed69c1224c5a1
- clm_537824c46a6e73bdf161248591ab26d17feb765a4014c76d369b64d5b588f7cd
- clm_6cb883017dd5c08eaf99214efa1d2c3c02a787d446cb0c0a133d819a9e22860a
- clm_a999e89005ff357cc6a3d619f4153b93c5ef0fabc997fd4c6a6fb3bd8cd45123
- clm_b10d9d7192a4f23e89bc6a372286012de54afa6ebead2308d3c383f6b5e55940
- clm_cc2eb3133e6418fe59c5523d3484c55d641db004908753583da6645c03acd130
- clm_cc8ae33c43d0a792cecbd8b21a4b82b031c6dffaedbb02f38e33030c27d271f0
- clm_d7b8d4dabb921312004629f99342020564404b723f2fbf0d869e76ad26b40111
- clm_db6abf3e80398365ddc11ff1b5e404c342a3b6c1436c275c74313203f5f27896
- clm_e59158bf9fb3e5e391fd44a03b755b68b48ea1049baea3f5a3bf3951ea3d9992
maturity: draft
page_id: pg_ed52f4864b175229890c8cce69ddaec9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bd4e011147b35a7d85c38772c06790b9
title: nam271212/strategic-advisor-orchestrator/README.md @ fedbb4fb4afc
updated_at: '2026-09-14T04:11:38Z'
---

# nam271212/strategic-advisor-orchestrator/README.md @ fedbb4fb4afc

<!-- rcw:begin owner=source:src_bd4e011147b35a7d85c38772c06790b9 block=evidence -->
- Synaptic Compass is described as an advisory orchestration framework that deploys a secondary, higher-order reasoning model to guide AI coding agents on architecture, security, performance, and debugging. [@claim:clm_18717ad39db8fd8ae98ae08317b7513eb2c705203d59af5ec9935a38f4171686]
- Documented components include an orchestrator module, context aggregator, configurable reasoning engine, feedback interface, and a memory buffer retaining pattern awareness across sessions. [@claim:clm_3469e33fb11471d3e0dea4d24e2d3b09e7b2c47a3614b426314ed69c1224c5a1]
- Integration is documented for agents exposing streaming output hooks, session context injection, or external tool calling (MCP, plugins, API endpoints), with Claude Code, Cursor, Gemini CLI, and Cline listed as stable integrations. [@claim:clm_537824c46a6e73bdf161248591ab26d17feb765a4014c76d369b64d5b588f7cd]
- The documented workflow captures prompt, agent reasoning, and project context, dispatches it to the advisor for architecture, security, performance, and edge-case analysis, then injects structured feedback the agent may accept, override, or escalate. [@claim:clm_6cb883017dd5c08eaf99214efa1d2c3c02a787d446cb0c0a133d819a9e22860a]
- Advisor contexts are documented as ephemeral and discarded after each orchestration cycle unless the memory buffer is explicitly preserved. [@claim:clm_a999e89005ff357cc6a3d619f4153b93c5ef0fabc997fd4c6a6fb3bd8cd45123]
- The README's disclaimer states the tool is advisory, not a replacement for human judgment, does not guarantee bug-free or secure software, and its advisor feedback may be inaccurate or incomplete. [@claim:clm_b10d9d7192a4f23e89bc6a372286012de54afa6ebead2308d3c383f6b5e55940]
- The security posture is documented as minimum privilege: no data leaves the environment unless a cloud advisor endpoint is configured, local models are supported, and the security layer never transmits credentials even in diagnostic logs. [@claim:clm_cc2eb3133e6418fe59c5523d3484c55d641db004908753583da6645c03acd130]
- Configuration uses a compass.yaml or compass.json file defining advisor model, feedback mode (blocking, non_blocking, advisory_only), validation layers, security scan depth, and output format, overridable per session via environment variables or flags. [@claim:clm_cc8ae33c43d0a792cecbd8b21a4b82b031c6dffaedbb02f38e33030c27d271f0]
- The advisor model appears configurable across providers (Claude, GPT, Gemini, or local LLMs such as Llama 3 and Mistral), suggesting no hard dependency on a single model vendor. [@claim:clm_d7b8d4dabb921312004629f99342020564404b723f2fbf0d869e76ad26b40111]
- Repository development practice: contributions are welcomed for new validation modules, agent adapters, and orchestration-loop optimization, with CONTRIBUTING.md referenced for the code of conduct and pull request process. [@claim:clm_db6abf3e80398365ddc11ff1b5e404c342a3b6c1436c275c74313203f5f27896]
- The product is documented as a stateless, event-driven orchestrator positioned between the user's prompt and the coding agent's execution layer. [@claim:clm_e59158bf9fb3e5e391fd44a03b755b68b48ea1049baea3f5a3bf3951ea3d9992]
<!-- rcw:end owner=source:src_bd4e011147b35a7d85c38772c06790b9 block=evidence -->

## Researcher notes

