# angleschina/angles-cli -- full detail

[Back to orientation](angles-cli.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/angleschina/angles-cli/53cf51b702e45dd0621b8453d0cc3d301b98cef1/8818c2194b628043.json](../../../wiki/dossiers/angleschina/angles-cli/53cf51b702e45dd0621b8453d0cc3d301b98cef1/8818c2194b628043.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The codebase is organized into Rust modules including main.rs (entry/routing), cli.rs, config.rs, provider.rs, gateway.rs, instructions.rs, api.rs, search.rs, server.rs, and tools.rs, plus instructions.txt, providers.toml, and docs/. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89) (`clm_96d7777be6e1d4b437721b14c8e7fe3f84ad6bc56be5017ef3269c91c739fe41`)
- [observation/documented] The conversation loop lives in api.rs, an OpenAI/Anthropic/Gemini client with streaming and a tool-calling loop that resolves angles-* commands to implementations in tools.rs. -- evidence: [README.md#L91-L91](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L91-L91) (`clm_d2dbc13f5fe6943e4a298d68ed6d0e8738d4d7469348c0164edfa72109819ae6`)

## design-choices (2 claim(s))

- [observation/documented] The tool ships as a single static ~1.6 MB Rust binary with zero runtime dependencies (no Node, Python, or dynamic libc), aimed at constrained environments like ARM64 SBCs, rootless containers, and iSH. -- evidence: [README.md#L37-L37](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L37-L37), [README.md#L54-L54](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L54-L54), [README.md#L56-L61](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L56-L61) (`clm_2c1b59e55b0b0464c09ba4fd8aee189e3548ef39726834691ab3c5420394c13f`)
- [observation/documented] All agent capabilities are exposed as curated angles-* commands rather than free-form shell improvisation, binding the model to a deterministic tool set. -- evidence: [README.md#L99-L99](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L99-L99) (`clm_41f06f5f6f6ba41e44dff6c443f3e2f8072039013482bd8e80437725096bb408`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building from source uses cargo build --release with Makefile targets for Linux ARM64/x64 and macOS ARM64 cross-compilation, and GitHub Actions produces prebuilt binaries for all 5 platforms on every tag push. -- evidence: [README.md#L256-L258](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L256-L258), [README.md#L266-L270](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L266-L270), [README.md#L272-L272](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L272-L272) (`clm_fbafde5fea1c06a8cf683e708f50dd842c8a351975b61be09d7ce184f9b2c7c1`)
- [observation/documented] Repository development practice: the repo includes a release workflow (.github/workflows/release.yml), a Cross.toml for cross-compilation, and a docs/ directory published as a GitHub Pages site. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89) (`clm_137c25aa3f9fb19b5e4975bee4ee14fe17e75143af74ac53b8d4a4e5ef77ce0f`)

## skills-patterns (1 claim(s))

- [observation/documented] The 13 KB instructions.txt system-prompt template uses handlebars-style {{variable}} injection for config values, persona, and architecture, and directs the agent to emit operation plans with fixed verbs before non-trivial tasks. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89), [instructions.txt#L99-L105](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L99-L105), [instructions.txt#L96-L97](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L96-L97), [instructions.txt#L21-L28](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L21-L28) (`clm_5980932033004b1dda83155dc8829566ea84800f8f8e395219b104048a36bfdd`)

## interfaces (2 claim(s))

- [observation/documented] The CLI offers subcommands including an interactive default session (angles), angles exec for one-shot runs, angles plan, angles serve, angles gateway, angles config, angles doctor, and angles help. -- evidence: [README.md#L218-L218](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L218-L218), [README.md#L221-L221](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L221-L221), [README.md#L215-L215](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L215-L215), [README.md#L212-L212](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L212-L212), [README.md#L209-L209](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L209-L209), [README.md#L224-L227](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L224-L227) (`clm_195c7c2307fe68aa29cb4f2fdea4ace41a70c590cac5f7e9760dcf3f4e0696be`)
- [observation/documented] angles serve starts an embedded axum HTTP server on 127.0.0.1:8080 exposing /health, /api/config, /api/providers, and /api/chat for a browser-based web console. -- evidence: [README.md#L119-L119](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L119-L119) (`clm_08de510213784991acff3a7ddfd2d26a1bf56dcfd722e924b8530389771b4057`)

## memory-state (1 claim(s))

- [observation/documented] Configuration persists at ~/.angles/config.json with fields for language, provider, base_url, wire_api, model, max_tokens, daily token budget, agent persona, search engine, and approval policy; API keys can come from ANGLES_API_KEY and are not sent through a relay. -- evidence: [README.md#L131-L146](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L131-L146), [gateway-flow.md#L219-L236](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/gateway-flow.md#L219-L236), [README.md#L123-L123](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L123-L123), [gateway-flow.md#L238-L241](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/gateway-flow.md#L238-L241), [README.md#L148-L148](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L148-L148) (`clm_4d4d807e141d1bd3d70afcd9edfa68e1404cea81c818e12ae4ee31dd82c2ce34`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The safety model: reads need no approval, writes follow the configured approval policy, and deletions or dangerous operations always require user confirmation. -- evidence: [README.md#L107-L107](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L107-L107) (`clm_d6957ea3dca3e0cd895169a043349e6a546e9b7e24b0d1aabfe86c3b58f6efe0`)
- [observation/documented] Approval policy is configurable to untrusted, on-request, or never, controlling whether tool calls require user confirmation. -- evidence: [gateway-flow.md#L124-L146](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/gateway-flow.md#L124-L146), [gateway-flow.md#L148-L151](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/gateway-flow.md#L148-L151) (`clm_b7f6125e64be730659260eee52527b4f498dce27912283e45836b4ac8f331e44`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] A provider registry (provider.rs plus providers.toml) maps 11 providers to three wire protocols — OpenAI Chat Completions, Anthropic Messages, or Gemini Native — normalizing streaming and tool calls so the rest of the code is provider-agnostic. -- evidence: [README.md#L111-L111](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L111-L111), [README.md#L233-L245](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L233-L245) (`clm_b6fc85dcc26bb20d936a881ee7d164ce4beef12e2b683f6c8008e14e2fdc4c92`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

