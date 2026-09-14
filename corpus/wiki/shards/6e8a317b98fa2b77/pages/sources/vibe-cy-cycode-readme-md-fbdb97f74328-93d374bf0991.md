---
access: public
aliases: []
claim_ids:
- clm_00d48a2b98038cf8b1f4bfc32f9a704844dc13122c43b2dcfd38c5edea4c3e37
- clm_01a66d1324c3c56b6e8d3bd5e0998e17bffd621623a7112299c215401c484d93
- clm_2acc2aa40a460e7e40fbfaadb567f2b34941ee79b65a2308ae170c33994d0bbb
- clm_4361db9bd4f5eaa47d1851bfc9646acda0788923e7e3ab209dd2d253bb0b877d
- clm_5b86cc351bf778568327d9f5238ada442b2eeebd013801b1e20ab3ab06e57e48
- clm_70126a05722a403f570a97d24a0037b32a28525525822748b8cbce8739809be7
- clm_7c812efe1a91322aa3e91b93b51908ed586045d3b2fec1938efc1ff56d47a31d
- clm_96ed01a0a946fbf0d6bbe9bec683bdfafd2f2733d6187e24cc4c0260972dfc49
- clm_af5a2d5d2b17bf8f7e8f140fbe23659e873b8f824b2275c8c115cf4fda53d494
- clm_b9352161465262d87738ae84743edaea0f154323349ef8e594b5ddbd91acedc2
- clm_ba087d78cc5182e37128d4112ca3e9d9a78c4131ad03d74f3f0b906dceb5329e
- clm_c1e145b8b844b788feb973589ebf2af464ee5af4a708c572a5b8d9416b9a493e
maturity: draft
page_id: pg_ef29e2f311ba51ddbb7193d374bf0991
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ed8369d7c0b15281bf0aef4706415f8c
title: vibe-cy/CyCode/README.md @ fbdb97f74328
updated_at: '2026-09-14T03:21:44Z'
---

# vibe-cy/CyCode/README.md @ fbdb97f74328

<!-- rcw:begin owner=source:src_ed8369d7c0b15281bf0aef4706415f8c block=evidence -->
- MAX_TURNS defaults to 50, capping tool-use turns per task, and CYCODE_MAX_TOKENS defaults to 4096 output tokens per call. [@claim:clm_00d48a2b98038cf8b1f4bfc32f9a704844dc13122c43b2dcfd38c5edea4c3e37]
- The bash tool blocks some high-risk command patterns like forced recursive deletion and piping scripts into a shell, but the README states this is not a complete sandbox. [@claim:clm_01a66d1324c3c56b6e8d3bd5e0998e17bffd621623a7112299c215401c484d93]
- Requirements are Node.js 18 or later, npm, and an OpenAI-compatible API key. [@claim:clm_2acc2aa40a460e7e40fbfaadb567f2b34941ee79b65a2308ae170c33994d0bbb]
- One-shot mode preserves plain stdout for scripting, while interactive mode prefers an Ink TUI with a text REPL fallback when TTY rendering is unavailable. [@claim:clm_4361db9bd4f5eaa47d1851bfc9646acda0788923e7e3ab209dd2d253bb0b877d]
- The project structure includes modules for the agent loop, CLI entry, config, context compression, LLM client, REPL, sessions, tool registry, built-in tools, and an Ink TUI. [@claim:clm_5b86cc351bf778568327d9f5238ada442b2eeebd013801b1e20ab3ab06e57e48]
- The CLI supports one-shot flags (-m/--message, -p/--prompt), session resume, working directory, model, base URL, API key, version, and help options. [@claim:clm_70126a05722a403f570a97d24a0037b32a28525525822748b8cbce8739809be7]
- Built-in tools exposed to the model include read_file, edit_file, write_file, bash, grep, glob, and an agent tool for spawning sub-agents. [@claim:clm_7c812efe1a91322aa3e91b93b51908ed586045d3b2fec1938efc1ff56d47a31d]
- edit_file relies on exact text matching; if the target fragment is not unique, the edit is rejected and more context is required. [@claim:clm_96ed01a0a946fbf0d6bbe9bec683bdfafd2f2733d6187e24cc4c0260972dfc49]
- Interactive mode provides slash commands including /reset, /model, /tokens, /compact, /diff, /save, and /sessions, plus quit/exit. [@claim:clm_af5a2d5d2b17bf8f7e8f140fbe23659e873b8f824b2275c8c115cf4fda53d494]
- Sessions can be saved, listed, and resumed, stored by default under ~/.cycode/sessions, with the root configurable via CYCODE_HOME. [@claim:clm_b9352161465262d87738ae84743edaea0f154323349ef8e594b5ddbd91acedc2]
- CyCode is described as a lightweight AI coding agent that runs in the terminal and uses an OpenAI-compatible Chat Completions API. [@claim:clm_ba087d78cc5182e37128d4112ca3e9d9a78c4131ad03d74f3f0b906dceb5329e]
- Repository development practice: npm scripts include build (TypeScript to dist/), start, dev, and test, where test builds then runs tests/*.test.mjs. [@claim:clm_c1e145b8b844b788feb973589ebf2af464ee5af4a708c572a5b8d9416b9a493e]
<!-- rcw:end owner=source:src_ed8369d7c0b15281bf0aef4706415f8c block=evidence -->

## Researcher notes

