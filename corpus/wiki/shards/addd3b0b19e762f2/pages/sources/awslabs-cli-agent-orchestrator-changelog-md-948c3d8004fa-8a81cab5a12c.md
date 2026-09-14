---
access: public
aliases: []
claim_ids:
- clm_42febe8e6d99ab2464dfd452a0620b84430fa96b0e2fc0a0ebaeb7fbda9fda4e
- clm_50bae23659e17f11e1e05ab011e1a0b3211155a5fbdb692e6399da4e3b8d6341
- clm_69523683b861008c7f526f19d0f8f59b04f5515ad335328c60394bee829316ae
- clm_85accfa3635dbc0d6bb6a30a9b7610cda1d1a48bedf3564256ac339a2bf44158
- clm_8d25ac339bc8aaca4df03f77e80eff23628a1b57aec6449aeb7abf6040f94ad2
- clm_9661057684772b4e36c1d48a8e66bcf421f824910fc9a5314af36046298677a4
- clm_a80ea9bd8bd3a66107d0d5094eef74417946ee52ab145020187f3007b2f6dcfa
- clm_c33855e07578e7ef161b073222344ed2eec5cdecd8c3a8199c9ad05b46a0f011
- clm_c578c9d5ca7ae4a8d504951834f86b58a5d60ded544d51d10977f80b89268576
- clm_d189db69298b2c94bfcfbe1dfba26deb49145a48e92291fb4ab1784a3ef105f7
- clm_d2fdee6cac98916e1c7ef790ca23600d607ced0aaea22ee8c2ad45213cf20ad7
- clm_fc8d937d761bfacf4e1a4e1031788b4c4ebcd22d15c68c07d742252ea8a6b4bc
maturity: draft
page_id: pg_e13dc9a89e065ac58f928a81cab5a12c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_74f324e69b0d55e3a7d548c455f19056
title: awslabs/cli-agent-orchestrator/CHANGELOG.md @ 948c3d8004fa
updated_at: '2026-09-14T01:36:40Z'
---

# awslabs/cli-agent-orchestrator/CHANGELOG.md @ 948c3d8004fa

<!-- rcw:begin owner=source:src_74f324e69b0d55e3a7d548c455f19056 block=evidence -->
- Intel macOS wheels are no longer published because cryptography 49.0.0+ ships no Intel-macOS wheel and CAO requires cryptography>=50.0.0, so Intel Macs cannot resolve dependencies. [@claim:clm_42febe8e6d99ab2464dfd452a0620b84430fa96b0e2fc0a0ebaeb7fbda9fda4e]
- Multiple agent CLI providers are supported, including MiniMax Code (mcode), Oh My Pi (omp), xAI Grok Build CLI (grok_cli), Cursor CLI, and Antigravity CLI (agy). [@claim:clm_50bae23659e17f11e1e05ab011e1a0b3211155a5fbdb692e6399da4e3b8d6341]
- The system includes a memory layer with typed relationship storage, memory plugins for Claude Code, Kiro, and Codex, and a wiki with self-healing via 'cao memory heal'. [@claim:clm_69523683b861008c7f526f19d0f8f59b04f5515ad335328c60394bee829316ae]
- CLI commands cao agent assign|handoff|send-message|status|result|cancel exist as a fallback when a terminal's MCP connection is unavailable, sharing an orchestration module with the MCP tools. [@claim:clm_85accfa3635dbc0d6bb6a30a9b7610cda1d1a48bedf3564256ac339a2bf44158]
- The project floors at cryptography>=50.0.0 for two HIGH CVEs, pins nanoid >=3.3.17 via npm overrides for CVE-2026-67213, and bumped mcp to 1.28.1. [@claim:clm_8d25ac339bc8aaca4df03f77e80eff23628a1b57aec6449aeb7abf6040f94ad2]
- Sessions run in tmux terminals with a conductor concept: a session's first (oldest surviving) terminal is normally its conductor, and five consumers depend on that ordering. [@claim:clm_9661057684772b4e36c1d48a8e66bcf421f824910fc9a5314af36046298677a4]
- Windows is unsupported: the backend is tmux and four modules import fcntl at module scope, so the package refuses Windows at import with an explanation. [@claim:clm_a80ea9bd8bd3a66107d0d5094eef74417946ee52ab145020187f3007b2f6dcfa]
- The grok_cli provider offers native hard tool restrictions, and network egress is gated behind a web_fetch tool category; per-role tool-restriction examples are provided. [@claim:clm_c33855e07578e7ef161b073222344ed2eec5cdecd8c3a8199c9ad05b46a0f011]
- An opt-in self-learning loop captures outcomes, performs retrospection, and promotes instructions; a skills/cao-learning skill instructs agents how to use it. [@claim:clm_c578c9d5ca7ae4a8d504951834f86b58a5d60ded544d51d10977f80b89268576]
- The project ships a cao-mcp-server that exposes orchestration tools such as assign, handoff, report_outcome, list_outcomes, and store_lesson to agents over MCP. [@claim:clm_d189db69298b2c94bfcfbe1dfba26deb49145a48e92291fb4ab1784a3ef105f7]
- Orchestration includes supervisor/worker flows, a run engine with durable run journal and playback, frozen execution manifests with plan approval, and a cross-node fleet coordinator. [@claim:clm_d2fdee6cac98916e1c7ef790ca23600d607ced0aaea22ee8c2ad45213cf20ad7]
- A Web UI provides a Profiles tab for browsing, creating, editing, cloning, and deleting agent profiles over profile management APIs, plus memory-system and fleet-panel views. [@claim:clm_fc8d937d761bfacf4e1a4e1031788b4c4ebcd22d15c68c07d742252ea8a6b4bc]
<!-- rcw:end owner=source:src_74f324e69b0d55e3a7d548c455f19056 block=evidence -->

## Researcher notes

