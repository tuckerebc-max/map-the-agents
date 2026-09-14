---
access: public
aliases: []
claim_ids:
- clm_1e152ffba5bb509b795e092acb487b38650fd2b97ff4f21caef35710d72c21d4
- clm_38d90823ae2daa928ab01f58c12d659eae1864baa3de4cda9c02dfbd9c2b0abc
- clm_4306f314d8d92137c12642ee58d7d9a91625b2a285b827bebc7cf50c30591cc2
- clm_54efe180b906563606d715a65f05510f7ef6947b0309dff2f1708d7e2cb478eb
- clm_6840d2f95ef77ee5d009b170de725c71ef657ddf0d8e4f5cf0de9509fb132772
- clm_7d8d18004d1edfaec2739f140c2c309c01bf150d25ec034c4e827f0749c26fe8
- clm_89939e9b1770978a696a137c5f715e67e705c3d996d393bd21f9df4eed58244c
- clm_8ee09b42188338e586eceb7c4671bb3f27b64243e2cc05cf5641448638b9fbb7
- clm_a906c6c97146cc28eed680c67837bbea1cbcb9e16dd354804baf5f09fed2addd
- clm_b392578fc4ad67090dee56f8322a523521ecaf277dea7cfc46df953ad758f562
maturity: draft
page_id: pg_bde7740d68f05bfe801c0c1358548365
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9da569e1c935590ab1b7770237660edd
title: sahil87/run-kit/README.md @ 65653f4d91c5
updated_at: '2026-09-14T02:37:21Z'
---

# sahil87/run-kit/README.md @ 65653f4d91c5

<!-- rcw:begin owner=source:src_9da569e1c935590ab1b7770237660edd block=evidence -->
- `rk riff` requires being inside a tmux session (`$TMUX` set) and fails with "not in a tmux session" otherwise; agent state shows `—` until the hook setup runs and fresh agent sessions are started. [@claim:clm_1e152ffba5bb509b795e092acb487b38650fd2b97ff4f21caef35710d72c21d4]
- The product is deliberately agent-agnostic: it does not speak any agent's protocol or parse agent output, treating a pane as just a pane so the terminal layer survives agent-tooling churn. [@claim:clm_38d90823ae2daa928ab01f58c12d659eae1864baa3de4cda9c02dfbd9c2b0abc]
- `rk riff` supports repeatable `--skill`/`--cmd` flags (one pane each, in argv order), `--layout` (auto, tiled, even-*, main-*), presets in `fab/project/config.yaml`, `-N` parallel spawning with rollback on failure, and `--` passthrough of flags to `wt create`. [@claim:clm_4306f314d8d92137c12642ee58d7d9a91625b2a285b827bebc7cf50c30591cc2]
- The CLI includes an MCP server over stdio (`rk mcp`) as an allowlisted proxy over rk verbs, with `rk url --mcp` printing the `/mcp` endpoint, plus commands like `rk notify`, `rk cron`, `rk gui`, and `rk doctor`. [@claim:clm_54efe180b906563606d715a65f05510f7ef6947b0309dff2f1708d7e2cb478eb]
- The product is two independent halves that compose: `rk riff`, which spawns agent workspaces (git worktree plus tmux window), and `rk serve`, which runs the browser dashboard watching tmux; either can run alone. [@claim:clm_6840d2f95ef77ee5d009b170de725c71ef657ddf0d8e4f5cf0de9509fb132772]
- Windows running AI agents can report live lifecycle state (active, waiting, idle) via opt-in per-machine setup that installs agent-harness hooks for Claude Code, Codex, Gemini CLI, Copilot CLI, Kimi Code, OpenCode, and Antigravity CLI, stamping a `@rk_pane_agent_state` tmux pane option. [@claim:clm_7d8d18004d1edfaec2739f140c2c309c01bf150d25ec034c4e827f0749c26fe8]
- HexoKit is described as a remote, phone-first console for tmux: every tmux session and pane appears as a live browser terminal, with state read directly from tmux rather than a database. [@claim:clm_89939e9b1770978a696a137c5f715e67e705c3d996d393bd21f9df4eed58244c]
- The product requires tmux >= 3.4 (checked at runtime via `rk doctor`) and, for `rk riff`, the sibling `wt` tool and a launcher binary (default `claude --dangerously-skip-permissions`) on PATH. [@claim:clm_8ee09b42188338e586eceb7c4671bb3f27b64243e2cc05cf5641448638b9fbb7]
- The dashboard offers named cross-server boards pinning multiple tmux panes side-by-side (pin state stored in tmux), a GUI tile running the host desktop via a private X display with selectable window managers, and a macOS Electron desktop app installable via `rk desktop install`. [@claim:clm_a906c6c97146cc28eed680c67837bbea1cbcb9e16dd354804baf5f09fed2addd]
- `rk serve` is configurable via `RK_HOST` (default 127.0.0.1) and `RK_PORT` (default 3000), and background operation is provided by `rk daemon` subcommands (start, restart, stop, status) running in a dedicated `rk-daemon` tmux server. [@claim:clm_b392578fc4ad67090dee56f8322a523521ecaf277dea7cfc46df953ad758f562]
<!-- rcw:end owner=source:src_9da569e1c935590ab1b7770237660edd block=evidence -->

## Researcher notes

