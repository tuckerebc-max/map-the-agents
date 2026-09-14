# kuafuai/aipexbase -- full detail

[Back to orientation](aipexbase.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kuafuai/aipexbase/bf523cfa479f25dfe78516b78658fc98ed15c611/ba47eda61ca376d7.json](../../../wiki/dossiers/kuafuai/aipexbase/bf523cfa479f25dfe78516b78658fc98ed15c611/ba47eda61ca376d7.json)

## specifications (1 claim(s))

- [observation/documented] The project is described as backend-as-a-service infrastructure for the AI era, versioned 1.0.0 and licensed under Apache 2.0. -- evidence: [README.md#L3-L22](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L3-L22) (`clm_e3d8d8a9155a1e30c209e3253527f306685e8df36cbefd5169ce253478fdbab2`)

## components (2 claim(s))

- [observation/documented] The stack includes a Spring Boot 2 backend and a Vue 3 management console, per README badges. -- evidence: [README.md#L3-L22](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L3-L22) (`clm_08d4e8e5e3002d8f835360b60f07d9d0573bf0bb3f8acf10aed4c9d247d57ed0`)
- [observation/documented] Out-of-the-box capabilities include automated data storage, user authentication with permission control, third-party AI service integration, and session/state context management. -- evidence: [README.md#L59-L62](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L59-L62) (`clm_1664e5a66b28200ace3bae43f5da7db612e4c82c1ed1bdb3bc040c9b898f6126`)

## design-choices (1 claim(s))

- [observation/documented] The core philosophy is providing a complete backend without writing backend code, so developers can skip backend implementation and integrate via SDK from any AI coding tool. -- evidence: [README.md#L40-L40](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L40-L40), [README.md#L38-L38](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L38-L38) (`clm_0464457376fa17c1689b1f07a13a52ae25ede9fc3af2ee218ef9bb304c27e33b`)

## workflows (2 claim(s))

- [observation/documented] Source installation requires Java 1.8+, Node.js 18+, MySQL 8.0+, importing an init SQL script, editing JDBC config in application-mysql.yml, then running mvn spring-boot:run (service on port 8080). -- evidence: [README.md#L74-L77](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L74-L77), [README.md#L99-L100](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L99-L100), [README.md#L89-L93](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L89-L93), [README.md#L95-L97](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L95-L97), [README.md#L85-L85](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L85-L85) (`clm_5c8599c16cc547b44005296716380af121ed10f80b75ba5d5e2e052d94bf168e`)
- [observation/documented] Docker Compose deployment is the recommended install method; prerequisites are Linux, Docker, and Docker Compose v2.5+, started with docker-compose up -d. -- evidence: [docs/INSTALL.md#L4-L6](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L4-L6), [README.md#L110-L110](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L110-L110), [docs/INSTALL.md#L19-L21](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L19-L21) (`clm_72d9e90bdaef7eebba65b8b86bda525a0280233a303bbe6d406751aed04323fc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product offers native MCP compatibility so models and agents can directly invoke backend capabilities, plus a unified context and data layer for long-term memory and traceable state. -- evidence: [README.md#L54-L56](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L54-L56) (`clm_a4d23f2e873a0fec29372099564bfc76fc0d88a4e7f7a0ec9d3e70472540b865`)
- [observation/documented] AI IDEs connect via an MCP server endpoint of the form /mcp/sse?token=<apikey>, configured in Cursor's mcpServers settings. -- evidence: [docs/IntegrationAI.md#L16-L24](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/IntegrationAI.md#L16-L24), [docs/IntegrationAI.md#L12-L14](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/IntegrationAI.md#L12-L14) (`clm_a475a0c49a83fcfea4a9b67170eb723f3ed9f402d96ea6717beb58b5f7591019`)
- [observation/documented] A JavaScript SDK, aipexbase.js, integrates frontends with the AIPEXBASE backend, and the AI is said to automatically use it when generating code. -- evidence: [docs/IntegrationAI.md#L42-L43](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/IntegrationAI.md#L42-L43) (`clm_065ce5448784ce133fb7e4386ab08106312a6bc197943e0955a6156a6aefb6d2`)
- [observation/documented] External reverse-proxy setups are supported with nginx snippets routing /baas-api and /mcp to port 8080, with long-connection timeouts (86400s) and buffering disabled for the MCP route. -- evidence: [docs/INSTALL.md#L44-L51](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L44-L51), [docs/INSTALL.md#L53-L57](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L53-L57), [docs/INSTALL.md#L25-L42](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L25-L42) (`clm_f2e250d0fbb169ddeb3093a3b99ded31a0cf541cc04fd8cccbbea61779a93f97`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The platform advertises native support for Chinese ecosystem platforms including Feishu, DingTalk, and WeChat, plus HarmonyOS apps, mini-programs, and WebView containers. -- evidence: [README.md#L65-L66](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L65-L66) (`clm_a78831c6afffe4b9ef034c72d49c36382034a2f6c1ebfbe197d2b5bf05bd6787`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

