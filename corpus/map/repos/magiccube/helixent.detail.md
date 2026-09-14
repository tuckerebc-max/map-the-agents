# magiccube/helixent -- full detail

[Back to orientation](helixent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/magiccube/helixent/5cc1fb3faf29b8db8dce614e925c89030ae2558b/1f960ac622028c5c.json](../../../wiki/dossiers/magiccube/helixent/5cc1fb3faf29b8db8dce614e925c89030ae2558b/1f960ac622028c5c.json)

## specifications (1 claim(s))

- [observation/documented] Helixent is described as a coding agent comprising an agent loop, a coding-focused agent layer, and a CLI, distributed as the npm package 'helixent'. -- evidence: [README.md#L79-L79](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L79-L79), [README.md#L14-L14](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L14-L14) (`clm_e9f347b39c8d9b3cb1edfe20eb716e93508bcbb241b5df0934d32358c837ef02`)

## components (3 claim(s))

- [observation/documented] The codebase is organized into three layers plus a community area: src/foundation (core primitives), src/agent (agent loop), src/coding (coding agent), and src/community (third-party integrations such as OpenAI). -- evidence: [README.md#L193-L193](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L193-L193), [README.md#L195-L201](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L195-L201) (`clm_2fb7c9a012a8db8f1f26d2bdf57a0b49bd650d5b2f1867e1ce9b466956dafcef`)
- [observation/documented] The foundation layer provides three core primitives: a Model abstraction over LLM providers, a single Message transcript type, and Tool definitions with execution plumbing. -- evidence: [README.md#L207-L209](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L207-L209), [docs/foundation.md#L3-L3](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L3-L3) (`clm_04dc357464cf162697013fdaac23860ac035b892e0c5c079b25089fe5126fd4c`)
- [observation/documented] The coding agent ships practical developer tools such as bash, read_file, write_file, str_replace, list_files, glob_search, grep_search, apply_patch, file_info, mkdir, and move_path, plus a todo-list-based plan mode. -- evidence: [README.md#L224-L224](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L224-L224), [README.md#L71-L77](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L71-L77) (`clm_d624157bcd874f0c0defb24485491997f8e7ad74d0bd80dd88ddb08c646cbaac`)

## design-choices (2 claim(s))

- [observation/documented] Bun was chosen over Node for its native async/await concurrency, faster HTTP/filesystem/cold-start performance, single-file compiled executables via 'bun build --compile', and bundled test runner, bundler, and TypeScript support. -- evidence: [README.md#L296-L296](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L296-L296), [README.md#L300-L303](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L300-L303) (`clm_8ff95731cd2059ea196c4abc2d871fc18e689466ed028ccdcc17c988340a6f19`)
- [observation/documented] The OpenAI provider defaults to temperature 0 and top_p 0, merges caller options last, and works with any OpenAI-compatible endpoint; thinking content is dropped when converting messages to OpenAI wire format. -- evidence: [README.md#L230-L230](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L230-L230), [docs/foundation.md#L81-L84](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L81-L84), [docs/foundation.md#L77-L77](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L77-L77), [docs/code-convention.md#L69-L70](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L69-L70) (`clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: all pushes and pull requests run 'bun run check' in GitHub Actions, local commits are gated by a pre-commit hook running the same check, and contributors build with bun install / bun run dev / bun run build:bin producing dist/bin/helixent. -- evidence: [README.md#L152-L154](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L152-L154), [README.md#L172-L172](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L172-L172), [README.md#L178-L180](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L178-L180), [README.md#L156-L156](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L156-L156), [README.md#L160-L162](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L160-L162), [README.md#L166-L168](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L166-L168) (`clm_901d657257d112c8e79f03e0c9f5fc04db5ecaa3d077c24a74d3f15a3b084933`)
- [observation/documented] Repository development practice: docs/bun.md instructs contributors to default to Bun (bun test, bun install, Bun.file, Bun.serve) and avoid Node/dotenv/express equivalents; docs/code-convention.md mandates kebab-case files, named exports only, _-prefixed private members, and layered dependency direction (agent stays generic; adapters live in community/). -- evidence: [docs/code-convention.md#L10-L11](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L10-L11), [docs/code-convention.md#L14-L18](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L14-L18), [docs/code-convention.md#L40-L44](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L40-L44), [docs/bun.md#L9-L15](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/bun.md#L9-L15), [docs/bun.md#L7-L7](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/bun.md#L7-L7) (`clm_d785aa05f215d45edd20d83d152e0f7684e0a30720182dd5450024b76f8ca9cc`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills in the standard agentskills.io format are discovered from ~/.agents/skills, ~/.helixent/skills, and the project's .agents/skills and .helixent/skills directories; duplicate skill names across folders are allowed. -- evidence: [README.md#L54-L69](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L54-L69) (`clm_b920bd4e7ee4db625ba774a418e1f195dbe328692fb1cabba6982410c1b6d7f9`)

## interfaces (3 claim(s))

- [observation/documented] The CLI stores configuration in ~/.helixent/config.yaml and offers subcommands including 'helixent config model list', 'add', 'remove <model_name>', and 'set-default <model_name>'. -- evidence: [README.md#L108-L110](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L108-L110), [README.md#L114-L116](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L114-L116), [README.md#L104-L104](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L104-L104), [README.md#L120-L122](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L120-L122), [README.md#L132-L134](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L132-L134) (`clm_0f0e03aabeacdb092b70168a2969e0fbb4801ef52f8e1502c819d967180afd58`)
- [observation/documented] Programmatic use is via createCodingAgent({ model }) from 'helixent/coding' and OpenAIModelProvider from 'helixent/community/openai'; agents expose a stream() method yielding messages whose content segments include thinking, text, and tool_use types. -- evidence: [README.md#L256-L260](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L256-L260), [README.md#L253-L254](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L253-L254), [README.md#L236-L239](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L236-L239), [README.md#L262-L273](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L262-L273) (`clm_dda06af36403353feea9a2c343eb2c1974914e98ac9c1eb43d0f71ef9fc2703f`)
- [observation/documented] The ModelProvider contract requires invoke(params) returning Promise<AssistantMessage> and stream(params) returning an AsyncGenerator of AssistantMessage; params bundle model, messages, optional tools, provider options, and an AbortSignal. -- evidence: [docs/foundation.md#L43-L43](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L43-L43), [docs/foundation.md#L36-L41](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L36-L41) (`clm_31f0c2abfe1a9546fda7f0ef6990a5a85e035ba5b7cf48a0a62e31d829b994e6`)

## memory-state (1 claim(s))

- [observation/documented] If an AGENTS.md file exists at the repository root, it is automatically picked up as project guidance, serving as long-term project memory. -- evidence: [README.md#L71-L77](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L71-L77) (`clm_170d4cc9d2d63e0ab6806a913c79e8d722a7c2a79ad736d644efb6917500f984`)

## orchestration (2 claim(s))

- [observation/documented] The agent loop is ReAct-style: it maintains conversation state, orchestrates think-act-observe steps, invokes tool calls in parallel, and feeds observations back into the next reasoning step. -- evidence: [README.md#L215-L218](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L215-L218), [README.md#L213-L213](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L213-L213) (`clm_0c1e4fce5eb57c5b4868effb9cfe854d7726c43b290cb2e33767544b95608264`)
- [observation/documented] A middleware system lets extensions observe and mutate agent behavior at eight lifecycle hooks (beforeAgentRun/afterAgentRun, beforeAgentStep/afterAgentStep, beforeModel/afterModel, beforeToolUse/afterToolUse), invoked sequentially in array order; hooks may return a partial update to merge or void. -- evidence: [README.md#L281-L290](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L281-L290), [README.md#L277-L277](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L277-L277), [README.md#L292-L292](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L292-L292) (`clm_c933882dbfbf09052492cbdcf84ac44cc5e38b1d4278efdc616ca78ad87c8a7c`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent loop supports human-in-the-loop approval of tool calls, listed as a key feature of the middleware-ready loop. -- evidence: [README.md#L54-L69](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L54-L69) (`clm_d7cc1bb61746dce3eb63d363acbeafd4851f160213002a519d85ce6f8a520545`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack uses TypeScript strict/ESM on the Bun runtime, Zod for schemas, the OpenAI SDK, Ink with React 19 for the TUI, Commander for the CLI, and gray-matter plus yaml for skills parsing. -- evidence: [docs/code-convention.md#L4-L7](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L4-L7) (`clm_934e9e18c7bd22d1559d3aefd58ec9588af109b3e7c571cc3989b1aaf2913b59`)

## limitations (1 claim(s))

- [inference/documented] Sub-agents, multi-agent teams, print mode, and file-based sessioning appear on the roadmap, suggesting these capabilities are planned rather than shipped in this version. -- evidence: [README.md#L309-L312](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L309-L312) (`clm_9cb44a4b8989cb8614aa65622ef35f5ea1ffa2045c6042604ff328b8ac3604b3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

