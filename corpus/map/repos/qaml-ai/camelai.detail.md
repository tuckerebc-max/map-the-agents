# qaml-ai/camelai -- full detail

[Back to orientation](camelai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/qaml-ai/camelai/5f3c295d66fd3fe3d70069aa56a394faf75814d5/ceee23502cd9df82.json](../../../wiki/dossiers/qaml-ai/camelai/5f3c295d66fd3fe3d70069aa56a394faf75814d5/ceee23502cd9df82.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Each chat thread runs its own coding agent inside a Cloudflare Durable Object (ChatThreadDO), which owns the agent loop and persistent chat state. -- evidence: [README.md#L22-L25](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L22-L25), [README.md#L108-L111](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L108-L111) (`clm_c8af81d71844b747895c24a61502a0d15d5639e1f6df33dbe9737d2116a1789c`)

## design-choices (1 claim(s))

- [observation/documented] The agent harness is camelAI's own, built from pi's lower-level agent-loop and state-management libraries; Anthropic, OpenAI, OpenRouter, Bedrock, and custom endpoints supply only the model, not the harness. -- evidence: [README.md#L103-L106](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L103-L106) (`clm_e3b6115fae1f540bc58cf051436693dad2f772e12d44f78a15b70ace82991c4e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors should run bun run typecheck, lint, and test:all before opening a pull request, add focused tests for behavior changes, and follow the architecture and code conventions in AGENTS.md. -- evidence: [README.md#L218-L218](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L218-L218), [README.md#L226-L229](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L226-L229), [README.md#L220-L224](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L220-L224) (`clm_f745f92ef6afffcc11ac1011bef71fc1ab933a434b24dfcad914c24aaafc700d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Enterprise SSO uses OIDC and is configured per organization at Settings → Organization → Single sign-on, with fields for issuer URL, client ID/secret, token auth method, email claim, allowed domains, and an uninvited-users toggle. -- evidence: [CUSTOMER_SSO_SETUP_GUIDE.md#L78-L86](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L78-L86), [CUSTOMER_SSO_SETUP_GUIDE.md#L3-L5](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L3-L5), [CUSTOMER_SSO_SETUP_GUIDE.md#L76-L76](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L76-L76) (`clm_601e859402ab1fd65a5e690114d300d8c6279c17f37a57abe6b2a87dcb339ff2`)
- [observation/documented] Self-hosted deployments expose GET /api/selfhost/health as both the readiness endpoint and a versioned machine-readable capability contract; failed runtime checks return HTTP 503 with status fail. -- evidence: [SELF_HOSTING.md#L164-L166](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L164-L166), [SELF_HOSTING.md#L243-L250](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L243-L250) (`clm_198b9a40b18c3500cb4fc900d0af22c77ad2701cca1e757db87c1059f458473d`)

## memory-state (1 claim(s))

- [observation/documented] Project files live in WorkspaceFilesystemDO: small files in Durable Object SQLite, larger ones in R2, with git history provided by Cloudflare Artifacts. -- evidence: [README.md#L113-L117](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L113-L117) (`clm_0411518ed975874696d801f60216b7ec62c449f9ef1db632599339515cdd43f7`)

## orchestration (1 claim(s))

- [observation/documented] Linux sandbox containers are reserved for short-lived jobs (app builds, notebook analysis, SQL queries); project deploys flow through a build sandbox to Workers for Platforms, and a dispatcher Worker routes requests to published apps. -- evidence: [README.md#L113-L117](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L113-L117), [README.md#L97-L101](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L97-L101) (`clm_5a5054962e7f62e5f7ffe5dc0c3e47bd4734c919319bd15439e9ca3ec5603742`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent writes JavaScript instead of bash; Code Mode runs it in fresh V8 isolates with explicit platform and connection methods, and credentials remain outside the execution sandbox. -- evidence: [README.md#L108-L111](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L108-L111) (`clm_7225ccde0f524d2c7ff44ad39db83e362d44a93fa272cc000388deffca84cc8a`)

## evaluation (1 claim(s))

- [observation/documented] The repository includes agent evals run via 'bun run test:eval <eval-id>' by manifest ID, requiring Docker and additional credentials. -- evidence: [README.md#L167-L168](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L167-L168), [README.md#L170-L172](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L170-L172) (`clm_7e4102305bfd68ca4ccba87b7f58ab2c175d0ac62e2c2adf931f5c033adc1079`)

## dependencies (1 claim(s))

- [observation/documented] Development requires Node.js 22+, Bun, a Cloudflare account, and Docker for sandbox-backed features and agent evals; in the self-host target the application runs under workerd. -- evidence: [README.md#L40-L43](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L40-L43), [SELF_HOSTING.md#L3-L5](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L3-L5) (`clm_fd39b50ab4b25439b54249e86633fb6b220564146828fb0f3fbef988780abae6`)

## limitations (2 claim(s))

- [observation/documented] The self-hosted target intentionally lacks outbound email, password-email verification, and multi-node failover. -- evidence: [README.md#L185-L189](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L185-L189) (`clm_431e205479994e2aaf4be0fffdc678f8a3e1e9b89bde2cb2418bb0c7942e3f70`)
- [observation/documented] In self-host mode the application container has read-write Docker-socket access so workerd can manage sandbox containers; anyone controlling that container should be treated as having root-equivalent VM control. -- evidence: [SELF_HOSTING.md#L63-L65](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L63-L65) (`clm_5e9a0e1144ca8ecfcf0f277d84ab7888b113a30856e9e2e6247ae9c928aaea16`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

