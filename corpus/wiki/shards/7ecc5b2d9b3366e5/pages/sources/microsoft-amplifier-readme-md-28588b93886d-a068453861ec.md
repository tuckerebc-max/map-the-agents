---
access: public
aliases: []
claim_ids:
- clm_5f23cd0a1d1cc5075c6b7f5409d2ff64849371e5a57f4c56bc2b863ad3580245
- clm_826e6306bbdac5ac13e2013ae1369de1c5a011ac42d60cea392ddc8e46e0da39
- clm_a26993efb185ee35ced6adbddb41155da058d46c48382d1e514300c4bc200c94
- clm_cab973f079ba450cab067414c89d55ea3da7b9bb45dad0be19eed1dd998e408e
- clm_d5560c1df3035c0971e1a927de12d61acbb413349ee2fccb3e24ae8cf52713dc
- clm_d99c7d6b39df0f0d2203b1679d7f215aae5e97f3991ef53793cbe136a09d03df
- clm_f2759e7fb0653255324577daf8f08b5de9fe5a0f1806202ae13680385d6d1d50
- clm_feafbfee899df31c306b17cb804cd51a9f235c122792c03ee0ff551bfe567138
maturity: draft
page_id: pg_6a99110343165e8fb5bea068453861ec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_76647e7a95ad50b1a5935bb534ffdf39
title: microsoft/amplifier/README.md @ 28588b93886d
updated_at: '2026-09-14T02:19:10Z'
---

# microsoft/amplifier/README.md @ 28588b93886d

<!-- rcw:begin owner=source:src_76647e7a95ad50b1a5935bb534ffdf39 block=evidence -->
- Providers are switched with commands like 'amplifier provider use openai' or explicit flags such as --model and --deployment; bundles are added and activated with 'amplifier bundle add' and 'amplifier bundle use'. [@claim:clm_5f23cd0a1d1cc5075c6b7f5409d2ff64849371e5a57f4c56bc2b863ad3580245]
- The project builds on separate ecosystem repos: amplifier-core, a roughly 2,600-line kernel providing module protocols, session lifecycle, and hooks, and amplifier-foundation, a bundle composition library plus the default foundation bundle. [@claim:clm_826e6306bbdac5ac13e2013ae1369de1c5a011ac42d60cea392ddc8e46e0da39]
- Bundles are composable configuration packages defining tools, providers, agents, and behaviors; the default 'foundation' bundle includes filesystem, bash, web, search, and task-delegation tools plus 14 specialized agents. [@claim:clm_a26993efb185ee35ced6adbddb41155da058d46c48382d1e514300c4bc200c94]
- Supported AI providers include Anthropic Claude (recommended and most tested), OpenAI, Azure OpenAI with managed identity support, and Ollama for local free use; other providers are acknowledged as needing more testing. [@claim:clm_cab973f079ba450cab067414c89d55ea3da7b9bb45dad0be19eed1dd998e408e]
- Amplifier is a command-line AI assistant with a modular, extensible architecture; the CLI is described as just one reference interface for the underlying modular platform. [@claim:clm_d5560c1df3035c0971e1a927de12d61acbb413349ee2fccb3e24ae8cf52713dc]
- Every interaction is automatically saved and sessions are project-scoped; users can list sessions for the current project or across all projects with 'amplifier session list' and its --all-projects flag. [@claim:clm_d99c7d6b39df0f0d2203b1679d7f215aae5e97f3991ef53793cbe136a09d03df]
- The project is an early research demonstrator with safety systems not yet built in; APIs may change, some features are experimental, and native Windows shells have known issues with WSL recommended instead. [@claim:clm_f2759e7fb0653255324577daf8f08b5de9fe5a0f1806202ae13680385d6d1d50]
- Chat mode persists context across messages and offers slash commands (/help, /tools, /agents, /status, /config) plus /think and /do to toggle plan mode; single-shot use is via 'amplifier run'. [@claim:clm_feafbfee899df31c306b17cb804cd51a9f235c122792c03ee0ff551bfe567138]
<!-- rcw:end owner=source:src_76647e7a95ad50b1a5935bb534ffdf39 block=evidence -->

## Researcher notes

