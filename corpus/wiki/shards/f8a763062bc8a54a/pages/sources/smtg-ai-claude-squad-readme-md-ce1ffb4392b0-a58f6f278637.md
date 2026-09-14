---
access: public
aliases: []
claim_ids:
- clm_092df2b58322bc5b0db1807afeea6943b7cfdcb411ddb0f68adab51406f7b4b7
- clm_4fc6e84aa2b46ee403a7ecbf24736f6bfca79214ba07886e912ea130eaca3f2a
- clm_5c82fe4ca46b5ab66e1f81c45f62240767ab8507bb10bfa4c82aea8e29f36f76
- clm_711115868d893aa61ac071c5bf63b3a281fd1da0050acbcd8dd73c87aab2c3df
- clm_87fa88b518a1a8d3f6b426cf0bb27a06902e993999f3aee5cbd238108a4f72e1
- clm_8ce9e1559ffd1d59cfae0f909159c1c503f6688c82e50994060f220ae5a4f55f
- clm_a05a6ed103a32d9e76cb1cc9d13c11420b416513972d622c55262b5bbc62428c
- clm_a7a576cc5d4dbd0b750ed866770788ffc74a0c575e71acfdd3dbdfa63dc8a725
- clm_b7dad2ea275be19f97b0732252b4ea4997f0fcf395afcb4b914787055811e1c1
- clm_ec68ea97733d3e9f6bf9e6118d1fcc6e9c3f74de0dc4656a8e5937bea7e7874c
maturity: draft
page_id: pg_0a012e726f8f58fc9706a58f6f278637
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c7c41fc7632d5b258cc6d29ce33b666e
title: smtg-ai/claude-squad/README.md @ ce1ffb4392b0
updated_at: '2026-09-14T02:40:57Z'
---

# smtg-ai/claude-squad/README.md @ ce1ffb4392b0

<!-- rcw:begin owner=source:src_c7c41fc7632d5b258cc6d29ce33b666e block=evidence -->
- The CLI is invoked as `cs` with subcommands including completion, debug, help, reset, and version, plus flags like --autoyes and --program. [@claim:clm_092df2b58322bc5b0db1807afeea6943b7cfdcb411ddb0f68adab51406f7b4b7]
- The product requires tmux and the GitHub CLI (gh) as prerequisites. [@claim:clm_4fc6e84aa2b46ee403a7ecbf24736f6bfca79214ba07886e912ea130eaca3f2a]
- When no profiles are defined, the app uses `default_program` directly as the launch command, defaulting to `claude`. [@claim:clm_5c82fe4ca46b5ab66e1f81c45f62240767ab8507bb10bfa4c82aea8e29f36f76]
- Claude Squad is a terminal application that manages multiple local AI coding agents such as Claude Code, Codex, Gemini, and Aider in separate workspaces for parallel tasks. [@claim:clm_711115868d893aa61ac071c5bf63b3a281fd1da0050acbcd8dd73c87aab2c3df]
- The app uses tmux for isolated per-agent terminal sessions and git worktrees so each session works on its own branch, with a TUI for navigation. [@claim:clm_87fa88b518a1a8d3f6b426cf0bb27a06902e993999f3aee5cbd238108a4f72e1]
- Configuration is stored in `~/.claude-squad/config.json`, and the exact path can be found via `cs debug`. [@claim:clm_8ce9e1559ffd1d59cfae0f909159c1c503f6688c82e50994060f220ae5a4f55f]
- Profiles allow named program configurations selectable at session creation; a `profiles` array with name/program fields and `default_program` is set in the config file. [@claim:clm_a05a6ed103a32d9e76cb1cc9d13c11420b416513972d622c55262b5bbc62428c]
- The `-p/--program` flag lets users launch a chosen agent command in new instances, e.g. `cs -p "codex"` or an aider command with a specific model. [@claim:clm_a7a576cc5d4dbd0b750ed866770788ffc74a0c575e71acfdd3dbdfa63dc8a725]
- An experimental `-y/--autoyes` flag makes all instances automatically accept prompts for Claude Code and Aider; the README also mentions background yolo/auto-accept mode. [@claim:clm_b7dad2ea275be19f97b0732252b4ea4997f0fcf395afcb4b914787055811e1c1]
- Keybindings support session creation (`n`, `N`), deletion (`D`), attach/detach (`↵/o`, ctrl-q), commit-push (`s`), checkout (`c`), resume (`r`), and diff-view navigation. [@claim:clm_ec68ea97733d3e9f6bf9e6118d1fcc6e9c3f74de0dc4656a8e5937bea7e7874c]
<!-- rcw:end owner=source:src_c7c41fc7632d5b258cc6d29ce33b666e block=evidence -->

## Researcher notes

