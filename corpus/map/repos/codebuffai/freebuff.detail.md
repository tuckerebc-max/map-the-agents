# codebuffai/freebuff -- full detail

[Back to orientation](freebuff.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/codebuffai/freebuff/654a906e6758ffe17974dae829d35423dcd827b3/eb011fd48855153f.json](../../../wiki/dossiers/codebuffai/freebuff/654a906e6758ffe17974dae829d35423dcd827b3/eb011fd48855153f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Freebuff ships five products: Desktop (parallel local agents), CLI, Web (full-stack app building), Cloud (agents on GitHub repos), and Chat. -- evidence: [README.md#L11-L17](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L11-L17) (`clm_145c33522168cc284258373d32434168b837495710c485a2d0ecd8b95afdd875`)

## design-choices (2 claim(s))

- [observation/documented] Freebuff uses specialized agents rather than one model and prompt; agents gather context, plan, edit, research, run tools, and review results. -- evidence: [README.md#L57-L57](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L57-L57) (`clm_205b0e1a8111b89503e077dfbb8d7b762402da47160c69f2177fa607c9d85fd3`)
- [observation/documented] The run_terminal_command tool separates process ownership from terminal UI ownership via a broker; a broker startup failure prevents the shell from running with no direct-console fallback. -- evidence: [docs/agents-and-tools.md#L24-L24](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L24-L24), [docs/agents-and-tools.md#L26-L45](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L26-L45) (`clm_07a9dd93100d463cf6e74e3b9d120fb151c8aba2315f4a3a2b4d40b21b52a6da`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors clone, run 'bun install' and 'bun up', start the CLI with 'bun start-cli', and consult the contributing, development, and testing guides before opening a PR. -- evidence: [README.md#L88-L93](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L88-L93), [README.md#L101-L101](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L101-L101), [README.md#L97-L99](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L97-L99) (`clm_ac9550387728feff74be59e29008398aca2aeacbc2bd2c0a69a426744737d847`)
- [observation/documented] Repository development practice: CI runs tests through scripts/ci/test-with-guard.ts, which fails the build on errors outside test bodies or on test/file counts below a recorded baseline in .github/test-baselines.json. -- evidence: [docs/testing.md#L27-L28](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/testing.md#L27-L28), [docs/testing.md#L25-L25](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/testing.md#L25-L25) (`clm_baa66fccea9d68de322450999c9097e9c192d1d498482975d0cdfa70da90cf11`)
- [observation/documented] Repository development practice: every package must have a bunfig.toml preloading sdk/test/setup-env.ts so package-local 'bun test' gets placeholder env values instead of the developer's .env. -- evidence: [docs/testing.md#L13-L13](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/testing.md#L13-L13) (`clm_881a28a14118ccf21bf2a78a50051e5082029de9df9b01caef85f464821a67e0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI is installed globally via npm and run with the 'freebuff' command inside a project directory. -- evidence: [README.md#L23-L27](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L23-L27) (`clm_29f46a03d925b4567f47fc4931dd2c636a63ea9f128f94181ad41691c6f50993`)
- [observation/documented] Shell shims let users invoke agents as direct commands without a 'codebuff' prefix, installed via 'codebuff shims install' and an env eval. -- evidence: [docs/agents-and-tools.md#L10-L10](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L10-L10), [docs/agents-and-tools.md#L12-L16](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L12-L16) (`clm_9f143f097156a2e43c1d93d5b1e5b78c2b536e01daf8ab5da700188ae4e90d7b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Freebuff is built on the Codebuff open multi-agent framework, which powers its orchestration, tools, and SDK; custom agents can use @codebuff/sdk. -- evidence: [README.md#L105-L105](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L105-L105) (`clm_b99f1129c3802c5c3b40c8c65f3807c3c9bbbcfd63a5286de4544b2f5a3088b7`)
- [observation/documented] The repository is a TypeScript monorepo built with Bun, and local development requires Docker and a configured .env.local. -- evidence: [README.md#L83-L83](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L83-L83), [README.md#L85-L86](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L85-L86) (`clm_9060f631018ed27b9ac2225de8a1cccd5c0d58175a87eb11a7cb5f1e24d030ee`)

## limitations (2 claim(s))

- [observation/documented] The Muse Spark 1.2 model is rate limited and shared by all users, so it queues when busy and answers on DeepSeek V4 Flash instead of making users wait. -- evidence: [README.md#L35-L42](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L35-L42) (`clm_2816fd116f916e5b4adf0a8556f7e60ac4c7b86726782e79afb1ea15b0bc14e6`)
- [observation/documented] Users outside supported regions and VPN users get limited access, restricted to GLM 5.3 Flash, DeepSeek V4.1 Flash, MiMo 2.5, and Solar Pro 4. -- evidence: [README.md#L67-L67](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L67-L67) (`clm_2d6dd0ab5e611300c1a92caa6e9b6525f3d86e81ba2bffa96fba69324d4bba49`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

