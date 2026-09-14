# marcusschiesser/edge-pi -- full detail

[Back to orientation](edge-pi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/marcusschiesser/edge-pi/c4b694c4abb1568c0ae3962d87ae028e94988d95/ec984f0805a83ae0.json](../../../wiki/dossiers/marcusschiesser/edge-pi/c4b694c4abb1568c0ae3962d87ae028e94988d95/ec984f0805a83ae0.json)

## specifications (3 claim(s))

- [observation/documented] Edge-Pi is a lightweight coding agent library built on the Vercel AI SDK, providing primitives for tool support, session management, and context compaction. -- evidence: [README.md#L3-L3](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L3-L3), [README.md#L5-L5](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L5-L5) (`clm_d874e68176a02760795f9054c986e252f513ceff1eb8f6955ed19524d1a8560e`)
- [observation/documented] The project positions itself as an open replacement for Anthropic's proprietary Claude Agent SDK, working with any LLM provider via the Vercel AI SDK. -- evidence: [README.md#L5-L5](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L5-L5) (`clm_be80024b9d295bc38041217eccdd4eae86261657a919461c580876ad7d6c955a`)
- [observation/documented] The `epi` CLI is a full-featured coding agent with multi-provider support and skills, described as a proof of concept for using the SDK. -- evidence: [README.md#L7-L7](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L7-L7) (`clm_633f2cbdd6d69285ebc9e8a15677228e1bae2ad5a90fc9e5498d7b09e26f8de8`)

## components (2 claim(s))

- [observation/documented] The edge-pi core package contains CodingAgent, Tool Factory with tools, SessionManager, Compaction, and a runtime abstraction, per the architecture diagram. -- evidence: [architecture.md#L14-L20](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L14-L20) (`clm_8d71fa897e9d0d658adea3b0dd229a2e0f56c543ca155465065327095becd55c`)
- [observation/documented] The edge-pi-cli package handles CLI args and modes, a model factory, auth storage/OAuth, and settings, skills, prompts, and context. -- evidence: [architecture.md#L7-L12](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L7-L12) (`clm_67ad10e89a7923ace210d22446d9c69172612e9134c448dc7edb3e470feee622`)

## design-choices (2 claim(s))

- [observation/documented] The runtime abstraction connects tools to a local filesystem/shell environment, with optional WebContainer and Vercel Sandbox execution environments. -- evidence: [architecture.md#L30-L35](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L30-L35), [architecture.md#L48-L57](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L48-L57) (`clm_725048b93485263b33e8782ef66faa3d0c29a58d759f2a96f66ebf83751589c7`)
- [observation/documented] The codebase is based on the pi coding agent by Mario Zechner, and the SDK is intentionally minimal with features that don't belong there directed to the CLI. -- evidence: [CONTRIBUTING.md#L38-L38](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L38-L38), [README.md#L9-L9](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L9-L9) (`clm_1ac1c5cf9b9d4c67b5cd3b6deaeeb5e25f2c5dde1ae1ab2abdb76107eb6ba8bf`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: AGENTS.md forbids running `npm run dev`, `npm run build`, or `npm test`, requires `npm run check` after code changes, and forbids committing unless the user asks. -- evidence: [AGENTS.md#L23-L28](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L23-L28) (`clm_3190afb783f44a3eb2985ee3cc353803ef9af2a39b57c3ba098855c90129f2dc`)
- [observation/documented] Repository development practice: first-time contributors must open an issue and receive a maintainer `lgtm` approval before submitting PRs, a gate intended to filter low-quality AI-generated contributions. -- evidence: [CONTRIBUTING.md#L15-L15](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L15-L15), [CONTRIBUTING.md#L23-L23](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L23-L23), [CONTRIBUTING.md#L17-L21](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L17-L21) (`clm_19fb234177892fa52e4e056ef848616f55fcbef6538e7a1f3fd6be16cd5517dd`)
- [observation/documented] Repository development practice: PRs require `npm run check` and `./test.sh` to pass, and contributors must not edit CHANGELOG.md files. -- evidence: [CONTRIBUTING.md#L27-L30](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L27-L30), [CONTRIBUTING.md#L32-L32](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/CONTRIBUTING.md#L32-L32) (`clm_798cef45b4812898f3a82990ee0af671fe2e90a2626afcd1069029f3e404b123`)
- [observation/documented] Repository development practice: releases use Changesets with lockstep versioning via fixed groups, using `npm run changeset`, `npm run version`, and `npm run release`. -- evidence: [AGENTS.md#L132-L132](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L132-L132), [AGENTS.md#L149-L152](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L149-L152), [AGENTS.md#L144-L147](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L144-L147), [AGENTS.md#L139-L142](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L139-L142), [AGENTS.md#L134-L135](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L134-L135) (`clm_4cbd1e6ec2e2d69019d4a124f1955aaa9cf52ad885e123bfea8e2fad296f78e0`)
- [observation/documented] Repository development practice: parallel agents must stage only their own files with explicit paths, never use `git add -A`, and avoid destructive commands like `git reset --hard` or `git stash`. -- evidence: [AGENTS.md#L175-L179](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L175-L179), [AGENTS.md#L165-L169](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/AGENTS.md#L165-L169) (`clm_23fc9875d2e536a0021c76d856a7548e540004ef8e3b90fccbfdcbea24d96743`)
- [observation/documented] Repository development practice: the README documents dev commands including npm install, build, check, ./test.sh (which skips LLM-dependent tests without API keys), and ./epi.sh from the repo root. -- evidence: [README.md#L37-L43](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L37-L43), [README.md#L45-L45](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L45-L45) (`clm_014ed5aa1174708bc93fcb7593ee46bb4fcafd84f05c3588dd31c34f9d6886bc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI is installed globally via `npm install -g edge-pi-cli` and run with the `epi` command, with `epi --help` for more information. -- evidence: [README.md#L31-L33](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L31-L33), [README.md#L19-L21](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L19-L21), [README.md#L25-L27](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/README.md#L25-L27) (`clm_d4917f5b93f267eb7f12d19d69c5f015b87b5f82a279fe6d06a61aa9516e2da7`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are persisted as JSONL files, and a changelog entry says SessionManager is integrated with CodingAgent so history is auto-restored and persisted during generate() and stream(). -- evidence: [docs/CHANGELOG.md#L7-L7](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/docs/CHANGELOG.md#L7-L7), [architecture.md#L30-L35](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L30-L35), [architecture.md#L48-L57](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L48-L57) (`clm_c6a2d9d2b1788e90147936eebd885332bc0b7a292aa5d66e87d8dd8d5cecb631`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The architecture diagram lists external provider integrations: Anthropic SDK, OpenAI SDK, Google SDK, a GitHub Copilot endpoint, and the Vercel AI SDK ToolLoopAgent. -- evidence: [architecture.md#L22-L28](https://github.com/marcusschiesser/edge-pi/blob/c4b694c4abb1568c0ae3962d87ae028e94988d95/architecture.md#L22-L28) (`clm_964871baad4c438d10f588df9ac25162e45c57e7ad330dbede75e17c51868bd3`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

