---
access: public
aliases: []
claim_ids:
- clm_0843c43cea0f7f996fc3b06433579df628af2ddbe539b6c955859f959f4df2d7
- clm_0b941c6f97c66cb7d9beb6a957b1a2ff36f5da1485463d1811a7381500b2ef3a
- clm_4b0d22519987c8435f5ce90f15786149e6ebaf8d09b5b56fbd843ed2eae7da76
- clm_5d063fda099910beb7928a5bcaa44ea620041349f2e50eb321101157d5ffc111
- clm_87edfd5b81ea0ea137590a463c845eaa3fa78c95cd2c38e6406e34f9baed78e5
- clm_b04524e197dab269ff66e0c843216a1797ccd61b8bf14b515393a8dfa89c6410
- clm_b5b07ce0d0748a7343ff6dbb7bd2aa2090b114eca059631e075abcbf3cd6eee0
- clm_bbffd5adecbe54708ec900cf447a5058d406c69f88287aad12f40877bb20cd0f
- clm_bf49f10a0168185ef7656dc83c2ddee53ca330ce482b4786c2c72acae16608c0
- clm_c3b729945ed711ee85cd235743e325bd06bb55af181f7279ab969c0fb5c7c5b9
- clm_e1b89d0f1bd9fb8c0bf46d8ca9695479f2bd9250246977494ab184f583b2cd33
maturity: draft
page_id: pg_fe2499e3f98558b8835c6b0a5d6018a6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7305b7512bc25bbaa92b5721bc981ef2
title: PrimeIntellect-ai/prime-agent/README.md @ 1fc1adb6e806
updated_at: '2026-09-14T02:32:27Z'
---

# PrimeIntellect-ai/prime-agent/README.md @ 1fc1adb6e806

<!-- rcw:begin owner=source:src_7305b7512bc25bbaa92b5721bc981ef2 block=evidence -->
- Daemon-backed agents keep running when the terminal disconnects and can be reattached; heartbeats, schedules, persistent goals, automatic compaction, and bounded autonomous mode preserve progress across turns. [@claim:clm_0843c43cea0f7f996fc3b06433579df628af2ddbe539b6c955859f959f4df2d7]
- The installer requires HTTPS for release downloads and verifies the archive against the release origin's SHA-256 inventory; the README notes HTTPS itself is the authenticity boundary since inventory and archive share an origin. [@claim:clm_0b941c6f97c66cb7d9beb6a957b1a2ff36f5da1485463d1811a7381500b2ef3a]
- Skills are importable Python packages, and a built-in skill creator can turn recurring workflows into project or personal skills. [@claim:clm_4b0d22519987c8435f5ce90f15786149e6ebaf8d09b5b56fbd843ed2eae7da76]
- The README warns that Prime Agent executes model-generated Python and project commands with the user's permissions; worker and kernel processes improve lifecycle isolation but are not a security sandbox. [@claim:clm_5d063fda099910beb7928a5bcaa44ea620041349f2e50eb321101157d5ffc111]
- rlm.spawn(...) creates real child agents for parallel or background work and returns their results programmatically; running agents can also discover and message each other directly without routing through the user. [@claim:clm_87edfd5b81ea0ea137590a463c845eaa3fa78c95cd2c38e6406e34f9baed78e5]
- A persistent Python REPL is the built-in model tool; file operations, shell commands, tool use, subagents, and context management all happen through code in that environment. [@claim:clm_b04524e197dab269ff66e0c843216a1797ccd61b8bf14b515393a8dfa89c6410]
- The /refine command reviews the current trajectory and can apply small, evidence-backed updates to supplemental harness state (prompts, memories, skill descriptions, subagent specs), never rewriting the immutable base system prompt, with snapshots supporting rollback. [@claim:clm_b5b07ce0d0748a7343ff6dbb7bd2aa2090b114eca059631e075abcbf3cd6eee0]
- The CLI includes commands such as prime-agent agents, attach, --resume, status, doctor, update, and shutdown for browsing sessions, managing background services, and stopping all agents and workers. [@claim:clm_bbffd5adecbe54708ec900cf447a5058d406c69f88287aad12f40877bb20cd0f]
- Documentation references JSON mode and RPC mode for headless automation and integrations, alongside a TUI for interactive use. [@claim:clm_bf49f10a0168185ef7656dc83c2ddee53ca330ce482b4786c2c72acae16608c0]
- The agent and TUI are built on top of the open-source 'pi' project, which the README acknowledges. [@claim:clm_c3b729945ed711ee85cd235743e325bd06bb55af181f7279ab969c0fb5c7c5b9]
- Prime Agent is built around two abstractions: a Recursive Language Model that treats context as variables and subagents as function calls in a persistent REPL, and a Continual Harness storing prompts, memories, skills, and subagent specs as durable state. [@claim:clm_e1b89d0f1bd9fb8c0bf46d8ca9695479f2bd9250246977494ab184f583b2cd33]
<!-- rcw:end owner=source:src_7305b7512bc25bbaa92b5721bc981ef2 block=evidence -->

## Researcher notes

