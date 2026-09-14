---
access: public
aliases: []
claim_ids:
- clm_04dc357464cf162697013fdaac23860ac035b892e0c5c079b25089fe5126fd4c
- clm_0c1e4fce5eb57c5b4868effb9cfe854d7726c43b290cb2e33767544b95608264
- clm_0f0e03aabeacdb092b70168a2969e0fbb4801ef52f8e1502c819d967180afd58
- clm_170d4cc9d2d63e0ab6806a913c79e8d722a7c2a79ad736d644efb6917500f984
- clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7
- clm_2fb7c9a012a8db8f1f26d2bdf57a0b49bd650d5b2f1867e1ce9b466956dafcef
- clm_8ff95731cd2059ea196c4abc2d871fc18e689466ed028ccdcc17c988340a6f19
- clm_901d657257d112c8e79f03e0c9f5fc04db5ecaa3d077c24a74d3f15a3b084933
- clm_9cb44a4b8989cb8614aa65622ef35f5ea1ffa2045c6042604ff328b8ac3604b3
- clm_b920bd4e7ee4db625ba774a418e1f195dbe328692fb1cabba6982410c1b6d7f9
- clm_c933882dbfbf09052492cbdcf84ac44cc5e38b1d4278efdc616ca78ad87c8a7c
- clm_d624157bcd874f0c0defb24485491997f8e7ad74d0bd80dd88ddb08c646cbaac
- clm_d7cc1bb61746dce3eb63d363acbeafd4851f160213002a519d85ce6f8a520545
- clm_dda06af36403353feea9a2c343eb2c1974914e98ac9c1eb43d0f71ef9fc2703f
- clm_e9f347b39c8d9b3cb1edfe20eb716e93508bcbb241b5df0934d32358c837ef02
maturity: draft
page_id: pg_5e081bd3f2455ac4ab04be412201b005
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_33168a2b47e25292a4d8e083804b62eb
title: MagicCube/helixent/README.md @ 5cc1fb3faf29
updated_at: '2026-09-14T02:15:19Z'
---

# MagicCube/helixent/README.md @ 5cc1fb3faf29

<!-- rcw:begin owner=source:src_33168a2b47e25292a4d8e083804b62eb block=evidence -->
- The foundation layer provides three core primitives: a Model abstraction over LLM providers, a single Message transcript type, and Tool definitions with execution plumbing. [@claim:clm_04dc357464cf162697013fdaac23860ac035b892e0c5c079b25089fe5126fd4c]
- The agent loop is ReAct-style: it maintains conversation state, orchestrates think-act-observe steps, invokes tool calls in parallel, and feeds observations back into the next reasoning step. [@claim:clm_0c1e4fce5eb57c5b4868effb9cfe854d7726c43b290cb2e33767544b95608264]
- The CLI stores configuration in ~/.helixent/config.yaml and offers subcommands including 'helixent config model list', 'add', 'remove <model_name>', and 'set-default <model_name>'. [@claim:clm_0f0e03aabeacdb092b70168a2969e0fbb4801ef52f8e1502c819d967180afd58]
- If an AGENTS.md file exists at the repository root, it is automatically picked up as project guidance, serving as long-term project memory. [@claim:clm_170d4cc9d2d63e0ab6806a913c79e8d722a7c2a79ad736d644efb6917500f984]
- The OpenAI provider defaults to temperature 0 and top_p 0, merges caller options last, and works with any OpenAI-compatible endpoint; thinking content is dropped when converting messages to OpenAI wire format. [@claim:clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7]
- The codebase is organized into three layers plus a community area: src/foundation (core primitives), src/agent (agent loop), src/coding (coding agent), and src/community (third-party integrations such as OpenAI). [@claim:clm_2fb7c9a012a8db8f1f26d2bdf57a0b49bd650d5b2f1867e1ce9b466956dafcef]
- Bun was chosen over Node for its native async/await concurrency, faster HTTP/filesystem/cold-start performance, single-file compiled executables via 'bun build --compile', and bundled test runner, bundler, and TypeScript support. [@claim:clm_8ff95731cd2059ea196c4abc2d871fc18e689466ed028ccdcc17c988340a6f19]
- Repository development practice: all pushes and pull requests run 'bun run check' in GitHub Actions, local commits are gated by a pre-commit hook running the same check, and contributors build with bun install / bun run dev / bun run build:bin producing dist/bin/helixent. [@claim:clm_901d657257d112c8e79f03e0c9f5fc04db5ecaa3d077c24a74d3f15a3b084933]
- Sub-agents, multi-agent teams, print mode, and file-based sessioning appear on the roadmap, suggesting these capabilities are planned rather than shipped in this version. [@claim:clm_9cb44a4b8989cb8614aa65622ef35f5ea1ffa2045c6042604ff328b8ac3604b3]
- Skills in the standard agentskills.io format are discovered from ~/.agents/skills, ~/.helixent/skills, and the project's .agents/skills and .helixent/skills directories; duplicate skill names across folders are allowed. [@claim:clm_b920bd4e7ee4db625ba774a418e1f195dbe328692fb1cabba6982410c1b6d7f9]
- A middleware system lets extensions observe and mutate agent behavior at eight lifecycle hooks (beforeAgentRun/afterAgentRun, beforeAgentStep/afterAgentStep, beforeModel/afterModel, beforeToolUse/afterToolUse), invoked sequentially in array order; hooks may return a partial update to merge or void. [@claim:clm_c933882dbfbf09052492cbdcf84ac44cc5e38b1d4278efdc616ca78ad87c8a7c]
- The coding agent ships practical developer tools such as bash, read_file, write_file, str_replace, list_files, glob_search, grep_search, apply_patch, file_info, mkdir, and move_path, plus a todo-list-based plan mode. [@claim:clm_d624157bcd874f0c0defb24485491997f8e7ad74d0bd80dd88ddb08c646cbaac]
- The agent loop supports human-in-the-loop approval of tool calls, listed as a key feature of the middleware-ready loop. [@claim:clm_d7cc1bb61746dce3eb63d363acbeafd4851f160213002a519d85ce6f8a520545]
- Programmatic use is via createCodingAgent({ model }) from 'helixent/coding' and OpenAIModelProvider from 'helixent/community/openai'; agents expose a stream() method yielding messages whose content segments include thinking, text, and tool_use types. [@claim:clm_dda06af36403353feea9a2c343eb2c1974914e98ac9c1eb43d0f71ef9fc2703f]
- Helixent is described as a coding agent comprising an agent loop, a coding-focused agent layer, and a CLI, distributed as the npm package 'helixent'. [@claim:clm_e9f347b39c8d9b3cb1edfe20eb716e93508bcbb241b5df0934d32358c837ef02]
<!-- rcw:end owner=source:src_33168a2b47e25292a4d8e083804b62eb block=evidence -->

## Researcher notes

