---
access: public
aliases: []
claim_ids:
- clm_132e5bcf861beba6a970a0552b42e15ce5aed5fa8475761d86032f6e4f975a71
- clm_1e6720e863efb3acffd93a7beebcba77f5ed74672e4e68127fb1716dfd8b9be3
- clm_439e3f633817c52838301cc383057e473323fb20160a465d960e6f70c5c6e847
- clm_47720c30a93db38a48640aec6eeceea2ac2350b8b0f55a06d6c4f9e2e0c6b9bf
- clm_88b8f5e2f8c393f7d58ed141a6ef5e7012ba754772a28f5de94fbcdb692d6966
- clm_947f3411ed4fc6c214d783682e66482243f522fd6f4091824bf42047dc85680a
- clm_a3c80879c56c5eb9ef0a309de19a70e1636729fe4be2d6c2e23ee6ad78cd3c1e
- clm_b1d6feebcd035605d5c3ba519d51f6bf2ff12d86eb7c487a3785f4ba2bf7814e
- clm_c080489a54e4ad673de5a8c7c7a47688a9842147cdaa4e02b886b266ce075fca
- clm_e8e33caf985abce69dd7c7f834341e80e0b8a56f48832189078058838213420d
maturity: draft
page_id: pg_16d69e9e60b75aeca333e9c5e943a2d1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_15906de93ce25c1b95e64b43264cc0f6
title: codeany-ai/codeany/README.md @ 7e614dc436ef
updated_at: '2026-09-14T01:41:43Z'
---

# codeany-ai/codeany/README.md @ 7e614dc436ef

<!-- rcw:begin owner=source:src_15906de93ce25c1b95e64b43264cc0f6 block=evidence -->
- The product is a terminal TUI agent written in Go using Bubble Tea, invoked as the `codeany` binary with interactive, initial-prompt, pipe (-p), and print (--print) modes. [@claim:clm_132e5bcf861beba6a970a0552b42e15ce5aed5fa8475761d86032f6e4f975a71]
- MCP servers are configured in settings.json (e.g. a stdio filesystem server launched via npx) and managed at runtime through /mcp subcommands to list servers and tools or reconnect a server. [@claim:clm_1e6720e863efb3acffd93a7beebcba77f5ed74672e4e68127fb1716dfd8b9be3]
- The agent maintains memory files under ~/.codeany/memory/ (MEMORY.md plus files per the architecture doc), session history with save/restore/resume, and per-session context such as files accessed. [@claim:clm_439e3f633817c52838301cc383057e473323fb20160a465d960e6f70c5c6e847]
- Project-level instructions are read from CODEANY.md or CLAUDE.md in the project root, with personal gitignored variants and modular rules under .codeany/rules/ or .claude/rules/. [@claim:clm_47720c30a93db38a48640aec6eeceea2ac2350b8b0f55a06d6c4f9e2e0c6b9bf]
- The CLI supports flags including -p for pipe mode, -y to skip permission prompts, -m to select a model, and --output-format json for JSON output. [@claim:clm_88b8f5e2f8c393f7d58ed141a6ef5e7012ba754772a28f5de94fbcdb692d6966]
- Custom skills are markdown files at .codeany/skills/<name>/SKILL.md with YAML frontmatter (name, description, argumentHint) whose body can reference $ARGUMENTS and be invoked as a slash command like /deploy staging. [@claim:clm_947f3411ed4fc6c214d783682e66482243f522fd6f4091824bf42047dc85680a]
- The product has a permission model with a configurable permissionMode (e.g. "default") in settings.json, persisted permission rules in permissions.json, a /permissions command, and a -y flag to skip prompts. [@claim:clm_a3c80879c56c5eb9ef0a309de19a70e1636729fe4be2d6c2e23ee6ad78cd3c1e]
- Providers are configurable via environment variables: ANTHROPIC_API_KEY for Anthropic, or CODEANY_API_KEY, CODEANY_BASE_URL, and CODEANY_MODEL for OpenRouter or custom providers. [@claim:clm_b1d6feebcd035605d5c3ba519d51f6bf2ff12d86eb7c487a3785f4ba2bf7814e]
- Configuration lives in ~/.codeany/ with settings.json (model, permissions, MCP, hooks), an alternative config.yaml, persisted permissions.json, and directories for memory, sessions, skills, plugins, teams, and worktrees. [@claim:clm_c080489a54e4ad673de5a8c7c7a47688a9842147cdaa4e02b886b266ce075fca]
- The TUI advertises 78 slash commands such as /model, /compact, /plan, /commit, /review, /mcp, /skills, /resume, and /permissions, plus keyboard shortcuts including Tab completion and `! cmd` shell execution. [@claim:clm_e8e33caf985abce69dd7c7f834341e80e0b8a56f48832189078058838213420d]
<!-- rcw:end owner=source:src_15906de93ce25c1b95e64b43264cc0f6 block=evidence -->

## Researcher notes

