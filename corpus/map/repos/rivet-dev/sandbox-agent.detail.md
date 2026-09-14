# rivet-dev/sandbox-agent -- full detail

[Back to orientation](sandbox-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rivet-dev/sandbox-agent/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/56989d83a6914f57.json](../../../wiki/dossiers/rivet-dev/sandbox-agent/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/56989d83a6914f57.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project comprises a Rust daemon ('sandbox-agent server') exposing HTTP+SSE, a TypeScript SDK with embedded and server modes, a built-in Inspector UI, and a CLI mirroring the HTTP endpoints. -- evidence: [README.md#L53-L58](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L53-L58) (`clm_bd54df6b2cc9905d7aa78b3796af6cc63e894512520caad0bb1888cfa90fd357`)

## design-choices (1 claim(s))

- [observation/documented] The server is implemented as a single static Rust binary, chosen for fast startup and predictable memory usage so it can run in sandboxes or CI without a Node.js runtime. -- evidence: [README.md#L33-L38](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L33-L38), [README.md#L254-L255](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L254-L255) (`clm_5699c7bdc6e84a2368dff746f65401fe9b415f28da3374d59a37474bf3293576`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs contributors to keep CLI subcommands and HTTP endpoints in sync, update docs/cli.mdx on CLI changes, and regenerate docs/openapi.json when HTTP contracts change. -- evidence: [CLAUDE.md#L31-L38](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/CLAUDE.md#L31-L38) (`clm_36c34769412bbc0fed30a69dfaa7fedeb057783af4401c71a9204f7cd1641014`)
- [observation/documented] Repository development practice: contributors must keep three files in sync (common-software docs, a Dockerfile, and a Rust test file) and can verify with 'cargo test -p sandbox-agent --test common_software'. -- evidence: [CLAUDE.md#L47-L52](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/CLAUDE.md#L47-L52) (`clm_e5e119691cee36d26dde10fbd579239fa8934c666b117b5ad2c45debfc442e0f`)

## skills-patterns (1 claim(s))

- [observation/documented] A skill for the product can be installed via 'npx skills add rivet-dev/skills -s sandbox-agent' or the bunx equivalent. -- evidence: [README.md#L72-L74](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L72-L74), [README.md#L68-L70](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L68-L70) (`clm_16d113dec9f7509298c8c01a10bc131339d728df168ce9376f23ad98867540d9`)

## interfaces (5 claim(s))

- [observation/documented] The product exposes a single HTTP API with SSE streaming that normalizes different coding agents' proprietary APIs, so integrations can swap agents via configuration rather than code changes. -- evidence: [README.md#L27-L27](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L27-L27), [README.md#L25-L25](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L25-L25) (`clm_15175ee4db2049a588eb0d4805f15d96e35df34aa512a6026abbc6f404c93dc8`)
- [observation/documented] The TypeScript SDK supports embedded mode via SandboxAgent.start() and remote server mode via SandboxAgent.connect() with a baseUrl and token, and offers methods like listAgents, createSession, postMessage, and streamEvents. -- evidence: [README.md#L107-L111](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L107-L111), [README.md#L115-L116](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L115-L116), [README.md#L118-L121](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L118-L121), [README.md#L123-L123](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L123-L123), [README.md#L99-L100](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L99-L100), [README.md#L125-L128](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L125-L128) (`clm_3b99eb62e5f03b235d5b8f0a137a788a2fc0444bb7b473a4c6f7336adaee8f05`)
- [observation/documented] The server is started with a token for auth (e.g. 'sandbox-agent server --token ... --host 127.0.0.1 --port 2468'), and a --no-token flag exists to disable auth locally. -- evidence: [README.md#L140-L141](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L140-L141), [README.md#L149-L149](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L149-L149), [README.md#L151-L153](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L151-L153) (`clm_a9e4a25e4a74a1fa96bc095f1a7408e6a1dc215e99ebffb61a659b79bd0eb7af`)
- [observation/documented] A built-in Inspector UI for debugging sessions and events is served at a path like http://localhost:2468/ui/. -- evidence: [README.md#L193-L193](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L193-L193) (`clm_fd20928cf36dd687d6c27a895a787fd780ad987e842f5004264589b6d33cbced`)
- [observation/documented] An experimental OpenCode compatibility layer lets OpenCode CLI, SDK, or web UI connect to control agents through OpenCode tooling; CLAUDE.md references an /opencode/* surface when enabled. -- evidence: [CLAUDE.md#L5-L9](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/CLAUDE.md#L5-L9), [README.md#L15-L17](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L15-L17), [README.md#L33-L38](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L33-L38) (`clm_025330e06eb33b0b34663592c480e4a6c7d92c3a35699d0d490c734770ed3cbb`)

## memory-state (1 claim(s))

- [observation/documented] The SDK does not persist session data itself; events stream in a universal JSON schema that consumers are expected to store externally, e.g. in Postgres, ClickHouse, or Rivet. -- evidence: [README.md#L29-L29](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L29-L29), [README.md#L230-L231](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L230-L231) (`clm_78cd62e388ca61b9205ba5caa1357221fd1591520093c04db81b49dab1015226`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Agent binaries are installed lazily on first use by default, with an optional 'sandbox-agent install-agent --all' command to preinstall them. -- evidence: [README.md#L145-L147](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L145-L147), [README.md#L143-L143](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L143-L143) (`clm_941e2d550bd396066cd667c7725808f6aedd6502c061458f50d88467876322b8`)

## limitations (1 claim(s))

- [observation/documented] The README explicitly lists out-of-scope areas: on-disk session storage, direct LLM wrappers, git repo management, and a sandbox-provider API abstraction layer. -- evidence: [README.md#L277-L280](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md#L277-L280) (`clm_be02c656aaba0703376e1247050b6fa12502604b784adc5b15d8e56c68bbe487`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

