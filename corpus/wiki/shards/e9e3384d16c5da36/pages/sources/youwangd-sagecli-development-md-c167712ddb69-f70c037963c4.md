---
access: public
aliases: []
claim_ids:
- clm_08672c9775ef7d74f49ecb31ee13ca1e12433055fa3e2a1c12ed5808ba8928c1
- clm_439c76c1b7b3d0e78111622c5890b642fffa350aad6e4b59675c313bb8356978
- clm_4559474154f34c584dbe731865a6ad480319d6a74cbb22d5a0b8904c5d877e76
- clm_54372bbec87d251009dc5a09ab32858e33e047b213b2b6ef519456ff0ea57eae
- clm_8b04a8aec629f51f9157d99c14f442b007cd4f88fd8bddf49e72efe170d29a93
- clm_bb585b6e0036113098b66907c0ac2654f666f2ef97436eddf6e14600e16d16b8
- clm_c435c521b6ac7cef7b486d41fcabd687e01a893b4bca2de3677ab5b2caf4f2f5
maturity: draft
page_id: pg_4d1c924f7de15119bd1bf70c037963c4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e2ae6ee918665d9ca4bd5c23030ee651
title: youwangd/SageCLI/DEVELOPMENT.md @ c167712ddb69
updated_at: '2026-09-14T03:26:20Z'
---

# youwangd/SageCLI/DEVELOPMENT.md @ c167712ddb69

<!-- rcw:begin owner=source:src_e2ae6ee918665d9ca4bd5c23030ee651 block=evidence -->
- The acp runtime speaks JSON-RPC 2.0 over stdio and maintains persistent sessions across tasks, unlike one-shot runtimes such as cline/claude-code which spawn a fresh process per task. [@claim:clm_08672c9775ef7d74f49ecb31ee13ca1e12433055fa3e2a1c12ed5808ba8928c1]
- Every runtime implements exactly two shell functions, runtime_start() for one-time setup and runtime_inject() for each incoming message, so a new runtime is a single bridge file. [@claim:clm_439c76c1b7b3d0e78111622c5890b642fffa350aad6e4b59675c313bb8356978]
- In the ACP runtime, when an agent requests a permission (e.g. file write), the Claude Code adapter's session/request_permission is auto-approved by the runtime; Cline handles tools internally. [@claim:clm_4559474154f34c584dbe731865a6ad480319d6a74cbb22d5a0b8904c5d877e76]
- sage send is asynchronous (writes JSON to the inbox, returns a task ID immediately, auto-starts the agent), while sage call is synchronous, polling a reply directory up to a specified timeout. [@claim:clm_54372bbec87d251009dc5a09ab32858e33e047b213b2b6ef519456ff0ea57eae]
- Each agent runs a runner.sh process in a tmux window that polls its inbox directory every 300ms, sources the runtime script, and calls runtime_inject() per message. [@claim:clm_8b04a8aec629f51f9157d99c14f442b007cd4f88fd8bddf49e72efe170d29a93]
- Required dependencies are bash 4.0+, jq 1.6+, and tmux 3.0+; agent CLIs such as Claude Code, Gemini CLI, Codex, Cline, and ACP agents are optional per-runtime. [@claim:clm_bb585b6e0036113098b66907c0ac2654f666f2ef97436eddf6e14600e16d16b8]
- All state lives under ~/.sage/ as files: per-agent inbox/replies/results/workspace/state, runtime.json, instructions.md, steer.md, plus shared runtimes/, tools/, tasks/, plans/, and trace.jsonl. [@claim:clm_c435c521b6ac7cef7b486d41fcabd687e01a893b4bca2de3677ab5b2caf4f2f5]
<!-- rcw:end owner=source:src_e2ae6ee918665d9ca4bd5c23030ee651 block=evidence -->

## Researcher notes

