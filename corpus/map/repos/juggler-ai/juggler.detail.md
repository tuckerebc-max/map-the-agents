# juggler-ai/juggler -- full detail

[Back to orientation](juggler.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/juggler-ai/juggler/9446fd2936f02740057442a0a16b51440f68e63b/c554519a9ceb4f47.json](../../../wiki/dossiers/juggler-ai/juggler/9446fd2936f02740057442a0a16b51440f68e63b/c554519a9ceb4f47.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Most conversation capabilities are JavaScript extensions on a public SDK: context items defining tools like read/write/bash, strategies defining the LLM loop, slash commands, and UI cards or file viewers; MCP servers and skills enter through the same system. -- evidence: [README.md#L94-L94](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L94-L94), [README.md#L101-L101](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L101-L101), [README.md#L96-L99](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L96-L99) (`clm_99d9ed0006fcd6b92bb423d4c046192131c261faf446a2d50466e69b89572e39`)

## design-choices (4 claim(s))

- [observation/documented] Conversations are represented as persistent trees of typed items rather than scrolling transcripts, with Miller-column navigation and nested child threads that return results to their parent. -- evidence: [README.md#L7-L7](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L7-L7), [README.md#L13-L16](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L13-L16), [README.md#L82-L82](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L82-L82) (`clm_a004678d8d375f74679a0104b8468e0233309ae63e15b7ebba47d16d6c55fd0d`)
- [observation/documented] Context is editable: history can be folded into a thread, items moved or copied between branches, branches expanded back, and structural changes undone. -- evidence: [README.md#L22-L27](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L22-L27), [README.md#L82-L82](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L82-L82) (`clm_b95af7fbd951d9cb749761dd37c79fcf41fa575ee8f043a2a2374d17ea8a3a29`)
- [observation/documented] The backend is Go with Wails windowing; the UI is HTML and type-checked JavaScript served directly by the backend, with no Electron shell or frontend build step. -- evidence: [README.md#L239-L239](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L239-L239) (`clm_6bf4e1595bd9b8d014aa9d7b30dada39875a7ca4d59420936785e44876a36770`)
- [observation/documented] The server listens on localhost by default; LAN access is enabled via a keypress or `--public` flag and has no password, so the docs advise using it only on trusted networks. -- evidence: [README.md#L58-L58](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L58-L58) (`clm_d73c0706caecb027fb570982f0258d47329cd2ec6699150b7dd2f1f1e4c11074`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: builds require Go 1.26+ with vendored submodules; `make go-build` compiles, `make test` runs tests (race detector on by default), and `make test-full` with linting is expected before a PR. -- evidence: [README.md#L142-L142](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L142-L142), [README.md#L233-L233](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L233-L233), [README.md#L217-L217](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L217-L217), [README.md#L159-L161](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L159-L161) (`clm_cb97ecc66031d2a203d8cd67b96f9576654bb4cbc1948ec7ca0b74cf2b287be8`)
- [observation/documented] Repository development practice: every commit must carry a DCO `Signed-off-by:` line, and corporate or employer-owned contributions require executing the CCLA/CLA privately, not in public PRs. -- evidence: [CCLA.md#L11-L16](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CCLA.md#L11-L16), [CCLA.md#L130-L133](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CCLA.md#L130-L133), [CLA.md#L11-L14](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CLA.md#L11-L14) (`clm_b42af8a303167c3a5c0f2f1c56e09a13eff3d6772b68d25a5034f09ea1bd90a8`)
- [observation/documented] Repository development practice: CI is described as a sanity gate for linting, builds and tests that publishes no artifacts; official release builds come from a separate pipeline. -- evidence: [README.md#L235-L235](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L235-L235) (`clm_812f10d9e30520fd42f4c14871813e2892259a18396f5d4236c4601103d1409d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Juggler ships a native desktop app plus a headless `juggler` CLI server that serves a web UI, prints its URL and QR code, and can open the browser on a keypress. -- evidence: [README.md#L37-L38](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L37-L38), [README.md#L56-L56](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L56-L56) (`clm_fba0db03cafb74c95c2c6940229309926e60d579c3a1ed781911d04d1274fcfd`)
- [observation/documented] The desktop app and browser tabs are synchronized clients of the same server, so multiple clients can share one live session across machines or a phone. -- evidence: [README.md#L40-L40](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L40-L40), [README.md#L66-L66](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L66-L66) (`clm_cd14c83fbb2da5c49449bffb801b9670b500709a99bdcbc09082f30b1318eeb5`)
- [observation/documented] Users can inspect any recorded LLM transaction, seeing the system prompt, messages, tool schemas, output, token and cache usage, timing and stop reason. -- evidence: [README.md#L22-L27](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L22-L27), [README.md#L88-L88](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L88-L88) (`clm_7d16f2456ae6967171e56d9953b5d508ac8d7d3c04802daa5687caf21784d2fb`)

## memory-state (1 claim(s))

- [observation/documented] Session documents live on disk and persist across quit or reconnect, including pending approvals; synchronization uses Yjs. -- evidence: [README.md#L22-L27](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L22-L27), [README.md#L239-L239](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L239-L239) (`clm_eeb776fc95745d48e9dd01795c82c60207e60651ec70662524c1b3168111cf73`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] For MCP tools, users can allow or deny individual tools, set fixed default arguments, and view approximate context cost; approval decisions are visible in the handoff record. -- evidence: [README.md#L115-L118](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L115-L118), [README.md#L113-L113](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L113-L113) (`clm_38972e350de6b1e829ad61e18ce6114f764dda412deacdb1f72d67782e17284c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The product supports Anthropic/Claude Code, OpenAI/Codex, GitHub Copilot, Gemini, Mistral, Z.AI, Ollama, OpenRouter, DeepSeek and other OpenAI-compatible providers, plus local or remote MCP servers whose tools join the built-in toolset. -- evidence: [README.md#L113-L113](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L113-L113), [README.md#L124-L124](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L124-L124) (`clm_a48bf6ed5befddc40fc9b2603017aeae6bde1420461cfdd8622becc2ef5fdf9e`)
- [observation/documented] Juggler measures the full request before each model call, leaves room for the answer, and automatically compacts old history when a conversation exceeds the model's context window. -- evidence: [README.md#L126-L126](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L126-L126) (`clm_ba26792d73d995f3e64a47691a543e8f9a86d4db83fae08709cb4abd6e8c470e`)

## limitations (2 claim(s))

- [observation/documented] Repository builds support local and LAN access only; WAN/internet reachability modes are included solely in official binaries from juggler.studio, per the licensing boundary. -- evidence: [README.md#L60-L60](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L60-L60) (`clm_bea295b58cbfeeae6da9caa7019e08f10173df9624d2be16b4808ad101e94c60`)
- [observation/documented] LAN access to the server has no password, which the documentation itself flags as a constraint to consider on untrusted networks. -- evidence: [README.md#L58-L58](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L58-L58) (`clm_449c89ee99b6766c269e76fadb6b664b736cd5e8b88a53e5fe97dbf2b5849184`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

