# traycerai/traycer -- full detail

[Back to orientation](traycer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/traycerai/traycer/b12949767727955f2b68546b772000c98d73e2b9/6d5e53e24e3c3dec.json](../../../wiki/dossiers/traycerai/traycer/b12949767727955f2b68546b772000c98d73e2b9/6d5e53e24e3c3dec.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The context window is shared across providers, so users can switch models within the same agent without losing context. -- evidence: [README.md#L22-L22](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L22-L22), [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32) (`clm_5d566ebf3b2cc9cf44854006c0c434451d89ec3915437b48b3aff2d5e1b94e0c`)
- [observation/documented] Agent-to-agent abilities such as reading a transcript or delivering a message are narrower and depend on the user, Host, and runtime, per a capability matrix. -- evidence: [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32) (`clm_3adeef74486337eb88fe0290f71b09fdf88a4f496269034887ea72917a8185ce`)
- [observation/documented] Privacy documentation states code is processed in-memory and never stored or used for training, with a Privacy Mode defaulting on for Team plans. -- evidence: [README.md#L69-L69](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L69-L69) (`clm_c7ed14339efd97dff1b26a7a3c3633906c97c0bfcca9bce95f8739e2a233e976`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use Bun 1.3.12 workspaces with Nx, run build/compile/lint/format via bun scripts, and commits require DCO sign-off; tests run in CI, not pre-commit hooks. -- evidence: [AGENTS.md#L42-L46](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L42-L46), [AGENTS.md#L3-L3](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L3-L3), [AGENTS.md#L26-L33](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L26-L33) (`clm_df431e42e62aac8deb9f94d13c79c402be1d86440ba1988de47b346e9fbf261d`)
- [observation/documented] Repository development practice: commits must not manually run compile/build/lint/format beforehand because pre-commit runs affected workspace checks, and make dev-desktop targets the production cloud with no local backends. -- evidence: [AGENTS.md#L42-L46](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L42-L46), [AGENTS.md#L39-L40](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/AGENTS.md#L39-L40) (`clm_210b97eed9bce74aee8ec375093c95733656c3f3c9c2f432a2b158b009b08808`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] An agent is a durable session inside a Task that the user interacts with through a Chat or Terminal interface, powered by an underlying coding-agent provider. -- evidence: [README.md#L49-L49](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L49-L49) (`clm_e7f4cdbcf9c202ddcaf3dde6c2e668e664a85710fcde72f22220bf9a60e1eb2c`)
- [observation/documented] Desktop builds are distributed for macOS (arm64 and x64 .dmg), Linux (AppImage, .deb, .rpm), and Windows x64 .exe via GitHub Releases. -- evidence: [README.md#L36-L43](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L36-L43) (`clm_2c14b4e5828cd3462e071b73b16a80b387c562512346a94243b9836f038d1ffb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Traycer is described as an AI orchestration app that runs multiple agents in parallel while sharing memory across all models and providers. -- evidence: [README.md#L20-L20](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L20-L20) (`clm_1b33568fe926ea67cf93306ba8ce7c2d87deb94900dae16b10eadc450134ccec`)
- [observation/documented] The product supports agent-to-agent communication, letting users create automated loops where agents debate architecture or peer-review each other's code. -- evidence: [README.md#L28-L32](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L28-L32) (`clm_7816c5179581b6c9c6eda32da210956dd8caec7136de7ebcca79c4d86ad0a5a1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Supported coding agents listed as fully supported are Claude Code, Codex, Cursor, and OpenCode, plus Traycer's own native inference subscription. -- evidence: [README.md#L51-L57](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L51-L57) (`clm_0e57e8738a6be0a0ed4f5d6a8bd6615bff103ba3dd1a8945f545be9c989a1bf8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed open source with community channels on Discord, X, and YouTube, and accepts contributions under a DCO. -- evidence: [README.md#L93-L95](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L93-L95), [README.md#L81-L81](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L81-L81), [README.md#L99-L99](https://github.com/traycerai/traycer/blob/b12949767727955f2b68546b772000c98d73e2b9/README.md#L99-L99) (`clm_ff6b7269561edf32772d284441145e3b286b6b4385983594aece2ab4b4bbb6af`)

