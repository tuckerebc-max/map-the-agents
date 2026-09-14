---
access: public
aliases: []
claim_ids:
- clm_01b6ccd6ecf6c879cab94da94e4746db6ba95e6da55b89ada882dbce83cc8c4b
- clm_09ac983a39b4d65f13385126ea847a3ed2410dd8a2f86da2e62339d6adfb81d1
- clm_239abd2d6b9914731550e176c18fb836cb84912c972f099379828ef1a7bb66ce
- clm_502e0bfc07f58f526d8ac2b2cba4799bb0ecc9cba616da1ea02a97b05b7fceae
- clm_7e8143552cce71c9bb0c6de3217ca379f828d8b4cb6a83c00de7e16fb27e8c66
- clm_9333519fc8b24b9e49e862e0364b9dad2f6b7221cace53cbffbd8f4db9c96b3f
- clm_d7b9486e6cfb860a0f62c3d700c971b7ec5e17eacb747a04c55a7a45fc91422a
- clm_ed6d237a89577ba47c72a9369f169b5442a03bae9762ab3cfabe0596bd01de42
- clm_f66d2049e19841f61aa7cd559f21a9b6523a74bacd502f945f740efe37036cef
maturity: draft
page_id: pg_fb1c5bd71d6754cfabdb76eb3eeee196
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d3339742ebab53fb96c8c109c736cfee
title: openinterpreter/openinterpreter/README.md @ 860153a5318d
updated_at: '2026-09-14T02:27:12Z'
---

# openinterpreter/openinterpreter/README.md @ 860153a5318d

<!-- rcw:begin owner=source:src_d3339742ebab53fb96c8c109c736cfee block=evidence -->
- Installation is via a shell script on macOS/Linux and a PowerShell script on Windows; a session starts by typing `i` or `interpreter` in the terminal. [@claim:clm_01b6ccd6ecf6c879cab94da94e4746db6ba95e6da55b89ada882dbce83cc8c4b]
- The product runs as an Agent Client Protocol agent via `interpreter acp` and speaks the Codex exec protocol, allowing a one-line Codex SDK binary override to `interpreter`. [@claim:clm_09ac983a39b4d65f13385126ea847a3ed2410dd8a2f86da2e62339d6adfb81d1]
- Portability is a stated product goal: shared AGENTS.md, `.agents/skills` directories, MCP, ACP, and the Codex exec protocol are preferred, with `~/.openinterpreter` reserved for config and runtime state lacking shared standards. [@claim:clm_239abd2d6b9914731550e176c18fb836cb84912c972f099379828ef1a7bb66ce]
- The project describes itself as a fork of OpenAI's Codex focused on emulating the agent harness that gets the best performance from low-cost models. [@claim:clm_502e0bfc07f58f526d8ac2b2cba4799bb0ecc9cba616da1ea02a97b05b7fceae]
- Repository development practice: provider and model membership is generated rather than maintained as Rust lists, refreshed from `codex-rs` with `python3 scripts/write_provider_catalog.py`, and a `scripts/test-codex-sdk-compat.sh` script provides a local provider-free compatibility check. [@claim:clm_7e8143552cce71c9bb0c6de3217ca379f828d8b4cb6a83c00de7e16fb27e8c66]
- The README notes this is the new Rust version of Open Interpreter; the original Python project continues as a community-maintained fork elsewhere. [@claim:clm_9333519fc8b24b9e49e862e0364b9dad2f6b7221cace53cbffbd8f4db9c96b3f]
- The product ships a QA skill that can drive web apps in a real browser via agent-browser or operate native apps via trycua. [@claim:clm_d7b9486e6cfb860a0f62c3d700c971b7ec5e17eacb747a04c55a7a45fc91422a]
- Skills live in shared `.agents/skills` or `~/.agents/skills` directories; legacy product-specific skill directories remain readable for compatibility. [@claim:clm_ed6d237a89577ba47c72a9369f169b5442a03bae9762ab3cfabe0596bd01de42]
- A `/harness` TUI command switches the active harness among listed modes including native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal. [@claim:clm_f66d2049e19841f61aa7cd559f21a9b6523a74bacd502f945f740efe37036cef]
<!-- rcw:end owner=source:src_d3339742ebab53fb96c8c109c736cfee block=evidence -->

## Researcher notes

