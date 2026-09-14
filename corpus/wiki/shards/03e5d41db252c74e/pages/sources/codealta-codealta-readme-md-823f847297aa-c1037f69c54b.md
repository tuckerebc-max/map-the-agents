---
access: public
aliases: []
claim_ids:
- clm_0eec30d1d88beb8ad7c5cc5969a19787270def7e5ad0dc07c71fbd47ec6426ec
- clm_273f1f6d380f8126f781489b3deefb03ed1cda43de79b591b6863f366295d712
- clm_4fb51b45446c4fc50320e764c9919189090f247ee1ec419d6bd76b3d4ac5d757
- clm_62191ab58edb1d8e18a05f804eb2d7c56fd76345433ab2fc9e12d483cb5efd15
- clm_7e22fe5742cbcec9f00ea2005a4d13769f868f5bbf4282445ccf9b03d6775bf3
- clm_8201ed11d6397eaa2f3160e11324088928bc29f08b89602208ac1b51ce4b46b5
- clm_9cd83eb66198470021588e31e602ed326a8c85d86c7c02c8d0358f2fb170c627
- clm_d5f8c94c30368f21bcb1cc4dfa11db134a0ebca986a73af09807f5ed7ed65e8e
- clm_e3bb666a49f4d38533de7f03f341fa0088bd15e61e8ef1b96eb805698534ad2a
maturity: draft
page_id: pg_8b12c41cabf55ccf8854c1037f69c54b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_401af064b3dc571ba474ace989399845
title: CodeAlta/CodeAlta/readme.md @ 823f847297aa
updated_at: '2026-09-14T01:41:42Z'
---

# CodeAlta/CodeAlta/readme.md @ 823f847297aa

<!-- rcw:begin owner=source:src_401af064b3dc571ba474ace989399845 block=evidence -->
- The TUI exposes slash commands and shortcuts such as `/open` (Ctrl+O), `/prompt`, `/model_providers`, `/models`, `/logs`, and `/help`. [@claim:clm_0eec30d1d88beb8ad7c5cc5969a19787270def7e5ad0dc07c71fbd47ec6426ec]
- Installation requires .NET 10 and is done via `dotnet tool install -g CodeAlta`, with updates via `dotnet tool update -g CodeAlta`. [@claim:clm_273f1f6d380f8126f781489b3deefb03ed1cda43de79b591b6863f366295d712]
- CodeAlta runs as a terminal workspace invoked via the `alta` command, providing a keyboard-first TUI with tabs, prompt editor, project sidebar, and command discovery. [@claim:clm_4fb51b45446c4fc50320e764c9919189090f247ee1ec419d6bd76b3d4ac5d757]
- Supported model providers include Codex, Copilot, xAI Grok, OpenAI/Azure OpenAI/Alibaba APIs, Anthropic, Gemini/Vertex, and custom endpoints. [@claim:clm_62191ab58edb1d8e18a05f804eb2d7c56fd76345433ab2fc9e12d483cb5efd15]
- CodeAlta is pre-release software; configuration, screenshots, and extension APIs may change before version 1.0. [@claim:clm_7e22fe5742cbcec9f00ea2005a4d13769f868f5bbf4282445ccf9b03d6775bf3]
- The UI is multilingual, offering Auto, English, Spanish, French, German, Japanese, or Simplified Chinese via Workspace Settings. [@claim:clm_8201ed11d6397eaa2f3160e11324088928bc29f08b89602208ac1b51ce4b46b5]
- Agent sessions are durable and project-scoped, stored in CodeAlta-owned journals, and can be reopened independently of provider startup; prompts can be queued on busy sessions. [@claim:clm_9cd83eb66198470021588e31e602ed326a8c85d86c7c02c8d0358f2fb170c627]
- The repository includes a skills feature documented in doc/skills.md, referenced from the readme's documentation list. [@claim:clm_d5f8c94c30368f21bcb1cc4dfa11db134a0ebca986a73af09807f5ed7ed65e8e]
- On first launch the tool creates `~/.alta/config.toml` and leaves existing config untouched on later launches; if no provider is enabled, a Model Providers dialog opens. [@claim:clm_e3bb666a49f4d38533de7f03f341fa0088bd15e61e8ef1b96eb805698534ad2a]
<!-- rcw:end owner=source:src_401af064b3dc571ba474ace989399845 block=evidence -->

## Researcher notes

