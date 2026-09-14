---
access: public
aliases: []
claim_ids:
- clm_06969276b3a98a4869f3a2f25a5dccbd9832a791f96cd33a6f382a8221d2cfd8
- clm_0eacd21a288181e5cd3ef9da5467fee8f5a9ce8bf6bc5c172a987a6fd275835c
- clm_0ed3360e813d3487b706ad97c3bb57bf1a097d0868e24ee7a4be376600e75be1
- clm_3718b754eab28a42da0e179bf0de1c1c7f055801699dff600343993ec63eb3f6
- clm_3a88cdb910818510cdddaf176ee9708e816ef6b05336c0d616cd72e20de48e17
- clm_526e69148fffdc87e4a7a3e11afb11e8c5d99c0d0d39c5b7e0f77d4cace61d31
- clm_674ef61b2b0b45162c14489af92a761e146d9afafe61600dd35cf25a5b53f94d
- clm_a3bdcb20d3f2d6fc2f9513dabdae78f6acdbd83a71228f68273bdf8160e9ea40
- clm_c05868133baa7c64ea4ca4e40e503df30ab8f1bb0f97186c1084ac287d784e88
- clm_e82ef438f974b5aa0242d88f7e21bed91370c64b7c65b1a904b687731fa7a9b0
- clm_e9bb72f0c587d495934aaf4fba94709f0fe3dc447123fe1984767ed52da03c4e
- clm_fd525f652754d207dd48211c085581357b7731c42653cd7f409cc12ecb4f02a2
maturity: draft
page_id: pg_19556bfadf4f5c98833eaef1615b795e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7d60ba9054ec56d9b44152409fd3e6f1
title: HKUDS/DeepCode/README.md @ 4bb4fd9cb9e8
updated_at: '2026-09-14T02:03:22Z'
---

# HKUDS/DeepCode/README.md @ 4bb4fd9cb9e8

<!-- rcw:begin owner=source:src_7d60ba9054ec56d9b44152409fd3e6f1 block=evidence -->
- Sessions are stored locally and linked to their project, keeping tool calls, permission decisions, goals, model configuration, and verification records; history survives restarts and model switches, and compaction preserves the recent tail verbatim. [@claim:clm_06969276b3a98a4869f3a2f25a5dccbd9832a791f96cd33a6f382a8221d2cfd8]
- Command execution includes a sandbox as the security boundary, with a legacy dangerous-command screen matching on argv (not substrings) as a cheap first pass, and native file commands declining operands outside the working directory. [@claim:clm_0eacd21a288181e5cd3ef9da5467fee8f5a9ce8bf6bc5c172a987a6fd275835c]
- Complex work can be split across focused parallel agents that run in isolated Git worktrees to avoid editing the same directory; conflicts are surfaced explicitly and the main agent owns the final goal. [@claim:clm_0ed3360e813d3487b706ad97c3bb57bf1a097d0868e24ee7a4be376600e75be1]
- Skills can declare tool and skill dependencies that are expanded in order with cycle detection, failing before the first model request if a requirement is unavailable; sessions persist only skill identity, invocation kind, and revision, not the instruction body. [@claim:clm_3718b754eab28a42da0e179bf0de1c1c7f055801699dff600343993ec63eb3f6]
- The TUI exposes slash commands such as /model, /preset, /effort, /permissions, /transcript, /skill, /resume, /compact, and /context, with bare invocations opening a picker and argument forms keeping text paths. [@claim:clm_3a88cdb910818510cdddaf176ee9708e816ef6b05336c0d616cd72e20de48e17]
- Completion is evidence-driven rather than rule-based: the agent selects task-appropriate evidence such as test results, build output, static checks, diagnostics, diffs, or artifacts, and a failed verification feeds the next repair instead of being reported as success. [@claim:clm_526e69148fffdc87e4a7a3e11afb11e8c5d99c0d0d39c5b7e0f77d4cace61d31]
- Projects must be explicitly trusted before execution, and each session uses one of three modes: Ask (confirm sensitive operations), Read only, or Full access; individual tools also support allow, ask, and deny settings shared between CLI and Desktop. [@claim:clm_674ef61b2b0b45162c14489af92a761e146d9afafe61600dd35cf25a5b53f94d]
- Compaction summaries are written into workspace memory on a background thread, and injected memory content is wrapped in an escaped `<untrusted-data>` boundary so a poisoned note cannot forge instructions. [@claim:clm_a3bdcb20d3f2d6fc2f9513dabdae78f6acdbd83a71228f68273bdf8160e9ea40]
- The agent is model-provider agnostic, supporting OpenRouter, OpenAI, Anthropic, DeepSeek, Gemini, OpenAI-compatible gateways, Ollama, vLLM, and other compatible endpoints with the user's own API key; the README badge indicates Python 3.12+. [@claim:clm_c05868133baa7c64ea4ca4e40e503df30ab8f1bb0f97186c1084ac287d784e88]
- For multi-step work, users give a natural-language Goal and the agent loops through analyzing, implementing, verifying, and fixing; users can add requirements, revise the goal, queue instructions, or pause, stop, and resume while it runs. [@claim:clm_e82ef438f974b5aa0242d88f7e21bed91370c64b7c65b1a904b687731fa7a9b0]
- Skills are discovered from project `.agents/skills` and personal `~/.agents/skills`, plus bundled pinned upstream skills for authoring, review, security, frontend, MCP, and web testing; a Skill can narrow already-allowed tools but cannot grant new permissions. [@claim:clm_e9bb72f0c587d495934aaf4fba94709f0fe3dc447123fe1984767ed52da03c4e]
- DeepCode ships TUI, Desktop, and Web clients over one shared local service, launched via `deepcode`, `deepcode desktop`, or `deepcode web`; all three share projects, sessions, models, skills, permissions, goals, and automations. [@claim:clm_fd525f652754d207dd48211c085581357b7731c42653cd7f409cc12ecb4f02a2]
<!-- rcw:end owner=source:src_7d60ba9054ec56d9b44152409fd3e6f1 block=evidence -->

## Researcher notes

