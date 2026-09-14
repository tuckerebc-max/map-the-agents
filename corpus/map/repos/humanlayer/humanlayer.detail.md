# humanlayer/humanlayer -- full detail

[Back to orientation](humanlayer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/humanlayer/humanlayer/99abe673498cf8bdcd5f989aebe9406a27185b3b/847cd17b149ba4c3.json](../../../wiki/dossiers/humanlayer/humanlayer/99abe673498cf8bdcd5f989aebe9406a27185b3b/847cd17b149ba4c3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Internal docs knowledge describes contact channels (Slack, email, web embeds, SMS/WhatsApp in beta) as composable, with web embeds requiring a backend proxy so HumanLayer API keys are never exposed to the frontend. -- evidence: [docs/docs.knowledge.md#L160-L175](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L160-L175), [docs/docs.knowledge.md#L186-L194](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L186-L194) (`clm_eb697444ddf96211dbc3b7a78818c29ac3ba2f69415f94c3da1138448098928d`)
- [observation/documented] Docs knowledge describes a three-level contact-channel configuration hierarchy (operation, SDK, project) where operation-level settings override SDK-level, which override project defaults. -- evidence: [docs/docs.knowledge.md#L222-L227](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L222-L227) (`clm_54dbea4180ee8566b6b015034185e0fffa7c623697be356becec4f660b1f0ce4`)

## workflows (10 claim(s))

- [observation/documented] Repository development practice: the README states the code in this repo is largely deprecated and points readers to a rebuilt HumanLayer at humanlayer.com. -- evidence: [README.md#L3-L3](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md#L3-L3) (`clm_0991dbd63ce1faaf24b63a6a1d11d5949475e114020bf689732f760cda170bf6`)
- [observation/documented] Repository development practice: DEVELOPMENT.md describes parallel 'nightly' (stable) and 'dev' (testing) environments so daemon or WUI changes can be tested without restarting the daemon and breaking active Claude sessions. -- evidence: [DEVELOPMENT.md#L23-L26](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L23-L26), [DEVELOPMENT.md#L7-L7](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L7-L7) (`clm_22c39c780ce9b703a46c1130f08bc00dc043a2b6045866a0730dfca25dc94511`)
- [observation/documented] Repository development practice: the two environments use separate Unix sockets (daemon.sock vs daemon-dev.sock) and separate databases (daemon.db vs timestamped dev DBs) to prevent accidental cross-connections. -- evidence: [DEVELOPMENT.md#L11-L21](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L11-L21), [DEVELOPMENT.md#L45-L52](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L45-L52), [DEVELOPMENT.md#L139-L143](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L139-L143) (`clm_d11c603c3825dd625f1a1801c7ae074377531796d42c121cb5afcdc07d577f43`)
- [observation/documented] Repository development practice: make targets such as daemon-nightly, wui-nightly, daemon-dev, wui-dev, copy-db-to-dev, cleanup-dev, and dev-status build and run each environment; make daemon-dev starts with a fresh database copy. -- evidence: [DEVELOPMENT.md#L32-L33](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L32-L33), [DEVELOPMENT.md#L36-L37](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L36-L37), [DEVELOPMENT.md#L65-L73](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L65-L73), [DEVELOPMENT.md#L76-L78](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L76-L78), [DEVELOPMENT.md#L139-L143](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L139-L143) (`clm_a7214538f8b3ea1fab2ee34bca831fff49d4d695f35fe8adf9d8aeb4da12297e`)
- [observation/documented] Repository development practice: the daemon and WUI respect HUMANLAYER_DAEMON_SOCKET, HUMANLAYER_DATABASE_PATH, and HUMANLAYER_DAEMON_VERSION_OVERRIDE environment variables, with the socket variable defaulting to ~/.humanlayer/daemon.sock. -- evidence: [DEVELOPMENT.md#L147-L147](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L147-L147), [DEVELOPMENT.md#L149-L152](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L149-L152) (`clm_31799fa410e759f6199b6b0ff2205071c9ed4abfdde7bebb64715a0a44b43f79`)
- [observation/documented] Repository development practice: npx humanlayer launch accepts a custom daemon socket via a --daemon-socket flag, the HUMANLAYER_DAEMON_SOCKET environment variable, or a daemon_socket entry in humanlayer.json. -- evidence: [DEVELOPMENT.md#L87-L89](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L87-L89), [DEVELOPMENT.md#L84-L84](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L84-L84), [DEVELOPMENT.md#L97-L102](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L97-L102), [DEVELOPMENT.md#L92-L94](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L92-L94) (`clm_fbba4f4433e8a236e51d28882eb61c2ff5fd51be933692d3957b512656b15b26`)
- [observation/documented] Repository development practice: MCP servers launched by Claude Code sessions are passed HUMANLAYER_DAEMON_SOCKET so they connect to the daemon instance that launched them. -- evidence: [DEVELOPMENT.md#L82-L82](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L82-L82), [DEVELOPMENT.md#L149-L152](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L149-L152) (`clm_1c49c1fae4258d95de0abc4cf4dd6d9fd749464a8b458b38c16d949673c7ce41`)
- [observation/documented] Repository development practice: the monorepo offers make setup, check-test, check, and test targets, plus check-py/test-py for Python; TypeScript and Go projects are expected to define their own commands in package.json and Makefiles. -- evidence: [DEVELOPMENT.md#L195-L198](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L195-L198), [DEVELOPMENT.md#L187-L192](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L187-L192), [DEVELOPMENT.md#L204-L204](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L204-L204), [DEVELOPMENT.md#L201-L201](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/DEVELOPMENT.md#L201-L201) (`clm_177fd386b796e3afa2f39c569f20c5858d4462abeb3c15d04ebf2164b7b91e2f`)
- [observation/documented] Repository development practice: docs.knowledge.md records a release process using semver tags, jointly versioned Python and TypeScript packages, pyproject.toml/package.json version edits, and make build-and-publish / npm publish steps. -- evidence: [docs/docs.knowledge.md#L7-L32](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L7-L32), [docs/docs.knowledge.md#L45-L49](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L45-L49) (`clm_a03dabd60352c3d0a2411f6216043256f18d058526e1b72aff97fe68ad362454`)
- [observation/documented] Repository development practice: documentation is built on Mintlify, previewed locally via 'mintlify dev' (Node.js 19+ required), and deployed automatically to docs.humanlayer.dev through a Vercel integration. -- evidence: [docs/development.mdx#L6-L9](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/development.mdx#L6-L9), [docs/docs.knowledge.md#L60-L60](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L60-L60), [docs/docs.knowledge.md#L86-L86](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/docs.knowledge.md#L86-L86), [docs/development.mdx#L29-L31](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/development.mdx#L29-L31) (`clm_9d194bb0ee338f0b176325a2cdf72524d348d7d5e02515a0dea182fa11703d6b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The humanlayer.md SDK documentation notes the HumanLayer SDKs were removed in pull request #646 and are being superseded by CodeLayer. -- evidence: [humanlayer.md#L3-L3](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L3-L3), [humanlayer.md#L5-L5](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L5-L5) (`clm_0a189502108a53c404c050f3afa6c2a8efac484bf52b6452a75ac33c97ec5c99`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

