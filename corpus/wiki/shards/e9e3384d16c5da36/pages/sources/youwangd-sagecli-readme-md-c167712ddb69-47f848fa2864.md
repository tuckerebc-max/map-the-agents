---
access: public
aliases: []
claim_ids:
- clm_08672c9775ef7d74f49ecb31ee13ca1e12433055fa3e2a1c12ed5808ba8928c1
- clm_3697de9d8cc9981387434cd62f011ffeb3ffd46a5d5896dc9b317ee16137ca52
- clm_3b96fa9b1d0200ff0d3963e64cd337d35281296a7c9a821a006898f3e9dd5f46
- clm_8b04a8aec629f51f9157d99c14f442b007cd4f88fd8bddf49e72efe170d29a93
- clm_983ae5355d6d7250d3a9ac89780b9119725e08db33a9a546f1b5f71d329cf14c
- clm_bb585b6e0036113098b66907c0ac2654f666f2ef97436eddf6e14600e16d16b8
- clm_c435c521b6ac7cef7b486d41fcabd687e01a893b4bca2de3677ab5b2caf4f2f5
- clm_e3556cc2f423dbbcc5c2f54c106615e9321bab1064708bf955127d45fbba1936
- clm_e88b9ed6edd31b30e578db8576bc3950d228fb3ff65ede97a82ac0679c5735e6
maturity: draft
page_id: pg_368e3779f00b57489b2547f848fa2864
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_59d288d1fcef550e980f7c77e41d1b21
title: youwangd/SageCLI/README.md @ c167712ddb69
updated_at: '2026-09-14T03:26:20Z'
---

# youwangd/SageCLI/README.md @ c167712ddb69

<!-- rcw:begin owner=source:src_59d288d1fcef550e980f7c77e41d1b21 block=evidence -->
- The acp runtime speaks JSON-RPC 2.0 over stdio and maintains persistent sessions across tasks, unlike one-shot runtimes such as cline/claude-code which spawn a fresh process per task. [@claim:clm_08672c9775ef7d74f49ecb31ee13ca1e12433055fa3e2a1c12ed5808ba8928c1]
- Sage is a vendor-neutral, Unix-native control plane for agent CLIs implemented as one bash script (~8,500 lines) under an MIT license. [@claim:clm_3697de9d8cc9981387434cd62f011ffeb3ffd46a5d5896dc9b317ee16137ca52]
- Design emphasizes vendor neutrality: 8 runtimes plus any ACP agent behind one command surface, backends swappable with a flag, and a --fallback chain that auto-routes to healthy runtimes after a pre-flight health check. [@claim:clm_3b96fa9b1d0200ff0d3963e64cd337d35281296a7c9a821a006898f3e9dd5f46]
- Each agent runs a runner.sh process in a tmux window that polls its inbox directory every 300ms, sources the runtime script, and calls runtime_inject() per message. [@claim:clm_8b04a8aec629f51f9157d99c14f442b007cd4f88fd8bddf49e72efe170d29a93]
- The CLI exposes 53 commands across 12 domains (e.g. create, send, call, tasks, bench, mcp, skill, memory, trace, dashboard, doctor), with inline help via sage help and per-command --help. [@claim:clm_983ae5355d6d7250d3a9ac89780b9119725e08db33a9a546f1b5f71d329cf14c]
- Required dependencies are bash 4.0+, jq 1.6+, and tmux 3.0+; agent CLIs such as Claude Code, Gemini CLI, Codex, Cline, and ACP agents are optional per-runtime. [@claim:clm_bb585b6e0036113098b66907c0ac2654f666f2ef97436eddf6e14600e16d16b8]
- All state lives under ~/.sage/ as files: per-agent inbox/replies/results/workspace/state, runtime.json, instructions.md, steer.md, plus shared runtimes/, tools/, tasks/, plans/, and trace.jsonl. [@claim:clm_c435c521b6ac7cef7b486d41fcabd687e01a893b4bca2de3677ab5b2caf4f2f5]
- Sage positions itself as glue for orchestrating existing coding agents rather than a coding assistant, targeting users who already run Claude Code, Codex, or Gemini CLI and want them to interoperate. [@claim:clm_e3556cc2f423dbbcc5c2f54c106615e9321bab1064708bf955127d45fbba1936]
- Sage includes bench-as-code: sage bench run executes real tasks through multiple agents' CLIs and sage bench report emits metrics such as success rate and median wall time per agent. [@claim:clm_e88b9ed6edd31b30e578db8576bc3950d228fb3ff65ede97a82ac0679c5735e6]
<!-- rcw:end owner=source:src_59d288d1fcef550e980f7c77e41d1b21 block=evidence -->

## Researcher notes

