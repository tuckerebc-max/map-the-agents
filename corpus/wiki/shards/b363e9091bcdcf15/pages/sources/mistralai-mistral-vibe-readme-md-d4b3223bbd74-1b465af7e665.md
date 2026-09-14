---
access: public
aliases: []
claim_ids:
- clm_1963e688c519f838ccd8b9345dd33cb6bb414d3d1a2c5fc42dc5da8390f78a5e
- clm_3479157b9b2836b228dd7bf7d6e30d649b1eb009c98b4a1ee1eecdd17327de27
- clm_7136e8f77fcbfe620394b78fd3dd98b77d9aee993a6ee5973b10105280f810ba
- clm_839eb591feec058d5b3ce4c0633c38ea5c10159e6cd492489eb6b1116be63b31
- clm_9b4c72e1fbce1338457beebcbcf0686cf10c4a41199a1f7bdfe2d019976334d6
- clm_b260c0ae2c87d6ed6699f8d67ad4bd780c857f156edacc1c832de0e4ba5749f8
- clm_be58a10711a10a10e3225be11b34fd73012a878ca04c7c179deae9327a320f11
- clm_c376a6061f915170f92704e0d1cd4c4cf9393e7f176f62c579ffc94110f4e3a6
- clm_c4b898a11cae93255c053cc1b6a8477d57be6ae57904ff2f217c58b61979b3b6
- clm_c65253ae44b97c2ebbf5f644461470016f5fdb54061efa16444e40a9e85ca89e
- clm_c829feb7add145ddefa07733195838ef9a32c93d5391eee4c95f2cd79ac6785c
- clm_ce6cca88bfe85ad6d7aae3b72071a79425efeaac588c26030a6e2a350cb3d892
- clm_d8c413536c4feff1e58772c45df404da851ca2798c164c60f450eae9b1455fb8
maturity: draft
page_id: pg_c1f702efdc3a5cdebd6e1b465af7e665
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_da2c6401dc795aa38567aa61e36a00dd
title: mistralai/mistral-vibe/README.md @ d4b3223bbd74
updated_at: '2026-09-14T02:20:33Z'
---

# mistralai/mistral-vibe/README.md @ d4b3223bbd74

<!-- rcw:begin owner=source:src_da2c6401dc795aa38567aa61e36a00dd block=evidence -->
- A `task` tool delegates work to subagents that run independently without user interaction; a built-in read-only `explore` subagent exists, and custom subagents are defined with agent_type = "subagent". [@claim:clm_1963e688c519f838ccd8b9345dd33cb6bb414d3d1a2c5fc42dc5da8390f78a5e]
- Mistral Vibe is a command-line coding assistant powered by Mistral's models, providing a conversational interface to explore, modify, and interact with codebases using natural language. [@claim:clm_3479157b9b2836b228dd7bf7d6e30d649b1eb009c98b4a1ee1eecdd17327de27]
- Tool availability is configurable via enabled_tools and disabled_tools, supporting exact names, glob patterns, and regex (re: prefix); enabled_tools narrows the set first, then disabled_tools removes matching tools. [@claim:clm_7136e8f77fcbfe620394b78fd3dd98b77d9aee993a6ee5973b10105280f810ba]
- Programmatic mode accepts options including --max-turns, --max-price, --max-tokens, --agent, --auto-approve/--yolo, --enabled-tools/--disabled-tools, and --output with text, json, or streaming formats. [@claim:clm_839eb591feec058d5b3ce4c0633c38ea5c10159e6cd492489eb6b1116be63b31]
- Voice mode is documented as experimental and may change in future releases; it is toggled with the /voice slash command and recording starts via Ctrl+R. [@claim:clm_9b4c72e1fbce1338457beebcbcf0686cf10c4a41199a1f7bdfe2d019976334d6]
- Vibe ships built-in agent profiles governing tool approval: ask (approval required), plan (read-only, auto-approves safe tools), accept-edits (default, auto-approves file edits), and auto-approve (approves all tool executions). [@claim:clm_b260c0ae2c87d6ed6699f8d67ad4bd780c857f156edacc1c832de0e4ba5749f8]
- Vibe supports MCP server configuration under mcp_servers, with a `vibe mcp add` command supporting streamable-http transport, static auth via --api-key-env or --header, and OAuth browser login by default otherwise. [@claim:clm_be58a10711a10a10e3225be11b34fd73012a878ca04c7c179deae9327a320f11]
- Vibe includes a trust folder system: directories containing a .vibe subfolder may prompt for trust confirmation, trusted folders are remembered in ~/.vibe/trusted_folders.toml, and AGENTS.md instructions and project-local skills load only for trusted folders. [@claim:clm_c376a6061f915170f92704e0d1cd4c4cf9393e7f176f62c579ffc94110f4e3a6]
- Skills are directories with a SKILL.md using YAML frontmatter, following the Agent Skills specification; they can add tools, slash commands, and behaviors, and are discovered from config skill_paths, .agents/skills/, .vibe/skills/, and ~/.vibe/skills/. [@claim:clm_c4b898a11cae93255c053cc1b6a8477d57be6ae57904ff2f217c58b61979b3b6]
- Compaction uses a built-in prompt at prompts/compact.md by default, keeps the same session and visible conversation, and later model requests use the compacted context followed by newer messages; custom compaction prompts are supported. [@claim:clm_c65253ae44b97c2ebbf5f644461470016f5fdb54061efa16444e40a9e85ca89e]
- The package is published on PyPI as mistral-vibe and targets Python 3.12+; installation is via a curl install script, `uv tool install mistral-vibe`, or pip. [@claim:clm_c829feb7add145ddefa07733195838ef9a32c93d5391eee4c95f2cd79ac6785c]
- Built-in tools include read, write_file, edit, grep (with ripgrep support), todo list management, ask_user_question, and task delegation; shell tools exist in a legacy one-shot bash variant and a managed variant with session, stdin, and log-file tools. [@claim:clm_ce6cca88bfe85ad6d7aae3b72071a79425efeaac588c26030a6e2a350cb3d892]
- The CLI offers interactive chat via `vibe`, a one-shot prompt argument, and non-interactive programmatic mode through `--prompt` or piped input for scripting. [@claim:clm_d8c413536c4feff1e58772c45df404da851ca2798c164c60f450eae9b1455fb8]
<!-- rcw:end owner=source:src_da2c6401dc795aa38567aa61e36a00dd block=evidence -->

## Researcher notes

