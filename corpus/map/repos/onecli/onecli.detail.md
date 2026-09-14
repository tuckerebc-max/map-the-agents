# onecli/onecli -- full detail

[Back to orientation](onecli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/onecli/onecli/3e595ef04d1af420aab35bbe014967d1024e3d86/675314da46d13fff.json](../../../wiki/dossiers/onecli/onecli/3e595ef04d1af420aab35bbe014967d1024e3d86/675314da46d13fff.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The platform comprises a Next.js web dashboard, an API server control plane owning the database and work queue, a Rust gateway, a runner, a sandbox supervisor, an SSH terminator, and a Slack channel adapter. -- evidence: [README.md#L91-L98](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L91-L98) (`clm_ff863f7e4d7efd0d3989321d9308e4ac0d17862d80d28648d33af977834d0074`)

## design-choices (2 claim(s))

- [observation/documented] Agents run in isolated sandboxes whose only network egress is the gateway, so they can reach only granted resources; the runner is outbound-only with no inbound ports, enabling NAT'd hosts without ingress or tunnels. -- evidence: [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79), [README.md#L81-L81](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L81-L81) (`clm_d4b8cc091be8782a24b9a52609eb9151e9d46fb8f72a10f4309ec48af2f0334d`)
- [observation/documented] Licensing is Apache-2.0 except for `ee/` directories under the OneCLI Enterprise License, which is free for development, testing and evaluation but requires a subscription for production use. -- evidence: [README.md#L121-L127](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L121-L127) (`clm_ec7c6cbbd4514ccd5c2e08bdd3fda4e54437dac2e0f8798b02121dd4e734f8f5`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local setup is `mise install`, `pnpm install`, `pnpm dev`, which generates .env secrets, starts PostgreSQL, applies migrations, and runs web, api, gateway and runner; `pnpm check` is the pre-push and CI gate and `pnpm test` runs test suites. -- evidence: [docs/development.md#L17-L21](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L17-L21), [docs/development.md#L34-L47](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L34-L47), [README.md#L102-L107](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L102-L107) (`clm_78f7ed147a13da0000b6a127a2f4815f6d09a2646b96f43e3bb711526ee39989`)
- [observation/documented] Repository development practice: contributions require reading the Contributing Guide and Code of Conduct and are accepted under a Contributor License Agreement with ChartDB, Inc., signable via the CLA Assistant flow on a pull request. -- evidence: [README.md#L113-L113](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L113-L113), [CLA.md#L3-L5](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/CLA.md#L3-L5), [CLA.md#L84-L88](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/CLA.md#L84-L88) (`clm_e8ef9c3b9376c86d199a7a71036e552f4cb129bbd512f9f2a7bfc1d13d2c8645`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Each agent can have its own Slack app answering in channels and DMs under its own name; a DM shares the same conversation as the web dashboard, and gateway approvals appear as Slack cards with Approve/Deny buttons. -- evidence: [docs/channels-slack.md#L15-L20](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/channels-slack.md#L15-L20), [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79) (`clm_a686b8a5402d83443b13188e2d5f894af99a4e81e00d6e52cea6a5c4169312a2`)

## memory-state (1 claim(s))

- [observation/documented] Agent memory is kept by the platform so it persists, and users can read and edit it at any time from the dashboard. -- evidence: [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79) (`clm_6ca02f5aaf94f803bd4bf6f3575aeac290e2996dd83b1701b3738e7a52814922`)

## orchestration (1 claim(s))

- [observation/documented] The runner starts, parks and reaps agent sandboxes, polls a work queue owned by the API server, and never touches the database directly. -- evidence: [README.md#L91-L98](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L91-L98) (`clm_9da261786b514d052e4c5b44818fc4aa5c68cd1cbac8420f9bbc3a0f702c68c6`)

## tools-permissions (1 claim(s))

- [observation/documented] Credentials are never given to agents: the gateway injects them per request, matching secrets by host and path pattern into headers or query parameters, and agents authenticate with access tokens via Proxy-Authorization headers. -- evidence: [README.md#L73-L79](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L73-L79), [README.md#L91-L98](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/README.md#L91-L98) (`clm_1aafcecba604e3a6b3425e43d4e63cd4c4c1243a5eb977c0316f6985630d6282`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Development prerequisites are mise (provisioning Node.js and pnpm), Rust for the gateway, and Docker for PostgreSQL and agent sandboxes; the stack uses Prisma ORM with PostgreSQL. -- evidence: [docs/development.md#L51-L82](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L51-L82), [docs/development.md#L5-L7](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L5-L7) (`clm_83a09b4e49e1aeb4047c4e5fb537b39ad886445f9d366d3349c185b671d90947`)
- [observation/documented] The codebase is a pnpm/turbo monorepo with apps (web, api-server, gateway, runner, sandbox-supervisor, ssh-terminator, channel-adapter, e2e suites) and packages (api, agent-protocol, db, ui), plus Docker Compose files for self-hosting. -- evidence: [docs/development.md#L51-L82](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/development.md#L51-L82) (`clm_4ec3ec229c4844c6806718c17320ce8c41791919b2d519f37493de1b6409bc62`)

## limitations (1 claim(s))

- [observation/documented] Self-hosted upgrades must not use a bare `docker compose pull && up -d`, because the agent sandbox image is set via RUNNER_AGENT_IMAGE on the runner service and would silently stay stale while other services update. -- evidence: [docs/self-hosting.md#L52-L59](https://github.com/onecli/onecli/blob/3e595ef04d1af420aab35bbe014967d1024e3d86/docs/self-hosting.md#L52-L59) (`clm_98b16239a052c95aeebc96a92a50232eaf733deb37c40bc0272cf6d3e17ebae9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

