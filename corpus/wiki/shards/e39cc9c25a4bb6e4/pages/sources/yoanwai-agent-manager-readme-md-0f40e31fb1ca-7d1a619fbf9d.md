---
access: public
aliases: []
claim_ids:
- clm_1b49bc5398d6def9b474b252c6b7aaca31b5c5c8aff7e7740aa2653ce4572abf
- clm_268e9cd23d33acdcad65fc800712eb26ea2e8cd488347aba211f67efb54e39dc
- clm_41b3ab4699836279ba1617a58cbc12c7dbf7eb7b6082ebb5d5727e98d457026e
- clm_53343d20c7fd8c8bfb24b4790d6e52c440df2b136d40e299e16d0617dbd10b88
- clm_5479739fc7d94f57e46d707a9e8060d45143601a0c50fab5848071087b4cb7ee
- clm_5846a60cef94e6c76f8226bbd4ce3b1e3372bb22730c3f45cd18ffad99b0622e
- clm_788cfa0229c15a90813cb802336b72edb9b39c8307aa6be60386d561e5e94b08
- clm_848d73a953683d5679c7886f24ddbee1f880a31e45f4752cc3f12cc627b528b6
- clm_90676f13d7c01fc9ad34b332e004ca6cd2031884ca810c7ced91d94e1ba95bb6
- clm_a129c3e2722c338e58a04205d72d293a5a9ffd7038dcb295461d01c8f3cb16a8
- clm_cfcdb84c60a65d0822d02b5b5372e54fc3b218a91cb6559915dd26a93772bf6a
- clm_d0e1c445473e94ad7dd52287a8d331cb13fc22e1954e2638c03e4e0fec3556d0
- clm_d652a84e4fb02101de726a314085753f6b3c2f3856c9550093cfc122f7199d7a
maturity: draft
page_id: pg_a4a6407e6a635d6e9b9e7d1a619fbf9d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_282e43fd453957c497eace1166cd636c
title: YoanWai/agent-manager/README.md @ 0f40e31fb1ca
updated_at: '2026-09-14T03:26:06Z'
---

# YoanWai/agent-manager/README.md @ 0f40e31fb1ca

<!-- rcw:begin owner=source:src_282e43fd453957c497eace1166cd636c block=evidence -->
- The tool runs on macOS and Linux, and on Windows inside WSL2. [@claim:clm_1b49bc5398d6def9b474b252c6b7aaca31b5c5c8aff7e7740aa2653ce4572abf]
- An agent can spawn another agent, send it a message, and wait until it is done; every MCP-capable session carries those tools on launch. [@claim:clm_268e9cd23d33acdcad65fc800712eb26ea2e8cd488347aba211f67efb54e39dc]
- Sessions can spawn into their own git worktree under <repo>-worktrees/<name> on branch am/<name>, toggled on the new-session form or set as default in Settings. [@claim:clm_41b3ab4699836279ba1617a58cbc12c7dbf7eb7b6082ebb5d5727e98d457026e]
- Status detection rules for the eight supported CLIs ship in the binary, so upgrades bring current launch, revive, fork, and status rules. [@claim:clm_53343d20c7fd8c8bfb24b4790d6e52c440df2b136d40e299e16d0617dbd10b88]
- ctrl+r opens a syntax-highlighted full-file diff of an agent's changes; line comments are sent back to the agent's pane as one review prompt when pressing C. [@claim:clm_5479739fc7d94f57e46d707a9e8060d45143601a0c50fab5848071087b4cb7ee]
- Agent sessions run on a private tmux server named agentmgr with am_* session names, isolated from the user's own tmux; reachable via tmux -L agentmgr. [@claim:clm_5846a60cef94e6c76f8226bbd4ce3b1e3372bb22730c3f45cd18ffad99b0622e]
- The README states cost tracking and mouse-driven list navigation are not yet implemented. [@claim:clm_788cfa0229c15a90813cb802336b72edb9b39c8307aa6be60386d561e5e94b08]
- The tool is described as a thin layer over the user's installed CLIs: sessions launch the user's own tool with its login, config, and MCP servers intact. [@claim:clm_848d73a953683d5679c7886f24ddbee1f880a31e45f4752cc3f12cc627b528b6]
- Pressing f forks a session's conversation into a separate named fork, and v revives a dead session on its own conversation. [@claim:clm_90676f13d7c01fc9ad34b332e004ca6cd2031884ca810c7ced91d94e1ba95bb6]
- Keybindings are configurable via [keybindings.session] and [keybindings.list] tables in config.toml, with esc and ctrl+c kept fixed. [@claim:clm_a129c3e2722c338e58a04205d72d293a5a9ffd7038dcb295461d01c8f3cb16a8]
- The product depends on tmux (3.1+ per the install script) and git; the Homebrew tap installs tmux if missing, and the install script offers to install missing dependencies via the detected package manager. [@claim:clm_cfcdb84c60a65d0822d02b5b5372e54fc3b218a91cb6559915dd26a93772bf6a]
- Sessions show in one list with live status grouped into a foldable project tree; space sends a prompt into a session's pane or spawns a new agent in the selected group. [@claim:clm_d0e1c445473e94ad7dd52287a8d331cb13fc22e1954e2638c03e4e0fec3556d0]
- The product is a terminal workspace where Claude Code, Codex, OpenCode, Grok, Gemini CLI, Pi, Command Code, and Hermes Agent run side by side, each in its own persistent tmux session. [@claim:clm_d652a84e4fb02101de726a314085753f6b3c2f3856c9550093cfc122f7199d7a]
<!-- rcw:end owner=source:src_282e43fd453957c497eace1166cd636c block=evidence -->

## Researcher notes

