# guanyang/open-agent-hub -- full detail

[Back to orientation](open-agent-hub.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/guanyang/open-agent-hub/c90c4f2b25baea05248025dd0442358709c5cc25/18ff33ab1ed1652b.json](../../../wiki/dossiers/guanyang/open-agent-hub/c90c4f2b25baea05248025dd0442358709c5cc25/18ff33ab1ed1652b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Five expert agent prompts are provided: architect (Orchestrator), reviewer and tester (Evaluators), refactorer and debugger (Optimizers). -- evidence: [docs/Agent_Guidelines.md#L11-L25](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L11-L25) (`clm_41f5c884de46731c25aa6be33c939582e505c5dbfe2a78bd4d6a1e0198e58273`)

## design-choices (2 claim(s))

- [observation/documented] Activation works by dynamically symlinking Skills, Agents, and Commands into subdirectories (skills/, agents/, commands/) of each assistant's project or global config directory. -- evidence: [README.md#L85-L85](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L85-L85), [README.md#L62-L63](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L62-L63), [README.md#L49-L49](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L49-L49) (`clm_03243d4a4a8589c88a69b0266e1a9fb1d75106a6e6143e991dfad6a5b013d91e`)
- [observation/documented] Components use standardized Markdown prompts with YAML frontmatter metadata, which host agents parse to decide when to trigger and load skills. -- evidence: [docs/Skill_Guidelines.md#L22-L22](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Skill_Guidelines.md#L22-L22), [docs/Skill_Guidelines.md#L24-L29](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Skill_Guidelines.md#L24-L29), [README.md#L49-L49](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L49-L49) (`clm_7b4d2adfb07d2156621f177dccfe6d17a5b52ddf3dd77a9e936efed4df5441c6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: GEMINI.md provides project-level LLM coding behavioral guidelines (think before coding, simplicity first, surgical changes, goal-driven execution) derived from andrej-karpathy-skills, and CONTRIBUTING.md covers contribution guidelines. -- evidence: [GEMINI.md#L54-L56](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L54-L56), [GEMINI.md#L13-L16](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L13-L16), [GEMINI.md#L22-L26](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L22-L26), [GEMINI.md#L36-L39](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L36-L39), [README.md#L169-L170](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L169-L170), [GEMINI.md#L3-L3](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L3-L3), [README.md#L11-L33](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L11-L33) (`clm_4d7f59ce6db9a2a0085ede3639ae87b2597fed536e2c41ff078eaa4fb43a1e6d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The `oah` CLI provides list, status, enable, disable, and sync commands, with filters (--skills/--agents/--commands), --global, --target, and --path options. -- evidence: [README.md#L113-L113](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L113-L113), [README.md#L107-L107](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L107-L107), [README.md#L134-L135](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L134-L135), [README.md#L104-L104](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L104-L104), [README.md#L138-L148](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L138-L148), [README.md#L110-L110](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L110-L110) (`clm_d84a5fc1d2e34b5563dd03f8bc0b7f9916b30fd4fdcc14f2567ea130005c8117`)
- [observation/documented] The --target option supports claude, antigravity, gemini, codex, cursor, trae, opencode, kiro, and all, defaulting to claude. -- evidence: [README.md#L138-L148](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L138-L148) (`clm_a1f72dca6c30518bf8dc05977680759a2e33d68ee3f195d9b44b81808c6a6687`)
- [observation/documented] Besides directory linking, native plugin configurations are provided for Claude Code (.claude-plugin/), Codex (.codex-plugin/), and Cursor (.cursor-plugin/). -- evidence: [README.md#L62-L63](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L62-L63) (`clm_05ead86cc9099c73b7454b891c51f24213613ef455f421f28e347b70e53432c1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Agent prompts support three collaboration patterns: handoff contracts with expected input/structured output, evaluator-optimizer loops with strict exit conditions, and XML compaction blocks for context pruning. -- evidence: [docs/Agent_Guidelines.md#L34-L34](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L34-L34), [docs/Agent_Guidelines.md#L41-L41](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L41-L41), [docs/Agent_Guidelines.md#L37-L38](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L37-L38) (`clm_9363d8cfc70c6d751e713a28203126cc6a4b0de5e5e9f87de6b3d00ae79e3fe1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool is described as a lightweight, zero-dependency CLI for managing and activating AI coding assistant capabilities. -- evidence: [README.md#L5-L5](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L5-L5) (`clm_95df2b689817c869eef4a8e3a7b09da3077b3e886284d83ede2c9ed549791f9c`)
- [observation/documented] Skills can alternatively be installed via Vercel's `skills` CLI (npx skills@latest add guanyang/open-agent-hub) without cloning the repository. -- evidence: [README.md#L80-L81](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L80-L81), [README.md#L69-L69](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L69-L69), [README.md#L77-L77](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L77-L77), [README.md#L73-L73](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L73-L73) (`clm_2a24b0d54acef71baa62a0642f967e44a946db75a1e9d62fbde2eb5c81c6a629`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

