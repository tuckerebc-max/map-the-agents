# liumengxuan04/minicode -- full detail

[Back to orientation](minicode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/liumengxuan04/minicode/40413758cc12892528d31c85edbe53e97e25a88d/45c51cd2158f37a9.json](../../../wiki/dossiers/liumengxuan04/minicode/40413758cc12892528d31c85edbe53e97e25a88d/45c51cd2158f37a9.json)

## specifications (1 claim(s))

- [observation/documented] The README describes MiniCode as a lightweight terminal coding assistant for local development, offering Claude Code-like workflow and architectural ideas in a much smaller implementation aimed at learning, experimentation, and custom tooling. -- evidence: [README.md#L26-L26](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L26-L26), [README.md#L28-L28](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L28-L28) (`clm_746138e03329d7aaf8438de9d29b59a80e2f4c46a2a41af5401b95ad04f025be`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Documentation lists planned-but-not-built items including full Ink/React rendering, bridge/IDE two-way communication, remote sessions, LSP support, and a skill marketplace, while noting a minimal sub-agent runtime and basic layered memory loading are already implemented. -- evidence: [ARCHITECTURE.md#L31-L40](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L31-L40) (`clm_114825a60fc34c1d8d312ca1f7f56dce379c14b0e1f7b1c7460e98bae80d9baa`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: Documented development commands are npm run check and npm test, alongside a stated goal of keeping the architecture understandable, hackable, and easy to extend. -- evidence: [README.md#L222-L222](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L222-L222), [README.md#L217-L220](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L217-L220) (`clm_fef0f9b8cbeaeb0ae6dac1162487b8615c3878a13255360894637978ab0ad2be`)

## skills-patterns (1 claim(s))

- [observation/documented] Documented local skills are discovered through SKILL.md files, alongside MCP tools, resources, and prompts reachable over stdio or remote HTTP. -- evidence: [README.md#L125-L136](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L125-L136) (`clm_422237ee93d4c0d224dcf35b07e48b67a517cfe6a4a33c9c14e4e742a512c375`)

## interfaces (1 claim(s))

- [observation/documented] Documented slash commands include /plan for an in-memory Todo list, /goal with pause/resume for a Goal that persists across turns, and /loop for a recurring prompt with a default ten-minute interval and a one-minute minimum. -- evidence: [README.md#L178-L190](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L178-L190) (`clm_1d421d22562b7bb527ea10cec246578cb8fff75827e6a436c6038e20690e5f91`)

## memory-state (2 claim(s))

- [observation/documented] Documented runtime state keeps conversation messages in memory during a turn, appends them to a per-project session log after each successful turn, and treats fresh provider-reported usage as the source of truth for context accounting, with local token estimation only as a fallback or a tail estimate. -- evidence: [ARCHITECTURE.md#L72-L77](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L72-L77) (`clm_4c019ef5a773046599f77e39a45913620653c5c44c0177de1818ae771b0fea28`)
- [observation/documented] Documentation states very large tool outputs are moved out of the prompt context and stored on disk, leaving the model a preview and a path to the full output. -- evidence: [ARCHITECTURE.md#L72-L77](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L72-L77) (`clm_40dc4f5aef9806c88552096ddcb9375b567853316f3303e9b0a1ef977b11fcd0`)

## orchestration (2 claim(s))

- [observation/documented] Documented core capabilities include multi-step tool execution within a single turn, forming a model-to-tool-to-model loop. -- evidence: [README.md#L125-L136](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L125-L136) (`clm_49627410332c511d185a16e477eecb60833204ead2a36933c7761350a2d2e518`)
- [observation/documented] Documentation describes a root agent that can spawn up to three concurrent read-only sub-agents restricted to file search/read, skill loading, and web research tools; sub-agents cannot edit files, run commands, ask the user, or spawn further agents, and the root owns every code change. -- evidence: [ARCHITECTURE.md#L83-L87](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L83-L87) (`clm_72f5babcd14862814804547e09713d8b4dd2fab801551c1bcc46938470d0bbc5`)

## tools-permissions (1 claim(s))

- [observation/documented] Documentation states file edits follow a review-before-write flow with path and command permission checks. -- evidence: [README.md#L125-L136](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L125-L136) (`clm_0edf5e8ace2f01205b327aa8b3d78fcc88f576721201043a63721ea1ad96b9ae`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The documented installer asks for a model name plus ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN, storing configuration under a dedicated home directory that can be relocated with the MINI_CODE_HOME variable. -- evidence: [README.md#L154-L154](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L154-L154), [README.md#L149-L149](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L149-L149) (`clm_4dec81d428bee0b11483dff8f673d5685c95e7f99a88428e2a3381ca91cdc979`)

## limitations (1 claim(s))

- [observation/documented] Documentation states this multi-agent MVP does not persist workers, load .claude/agents, support nesting, isolate worktrees, or allow live user steering, framing itself as a minimal teaching implementation. -- evidence: [ARCHITECTURE.md#L89-L89](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L89-L89) (`clm_dca464b68ac577dbf8fb71231ce1326e3f24725f39a523ad159ca7bb687f524c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

