# denchhq/denchclaw -- full detail

[Back to orientation](denchclaw.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/denchhq/denchclaw/f14eb4c239002d7b28673c60955b689b9d69db22/3670cd3429a5893a.json](../../../wiki/dossiers/denchhq/denchclaw/f14eb4c239002d7b28673c60955b689b9d69db22/3670cd3429a5893a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The posthog-analytics OpenClaw plugin runs in-process with the gateway, hooks agent lifecycle events (e.g. before_model_resolve, before_tool_call, agent_end), and emits PostHog AI events; it is installed automatically during bootstrap when a PostHog project key is available. -- evidence: [TELEMETRY.md#L238-L256](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L238-L256), [TELEMETRY.md#L76-L78](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L76-L78) (`clm_20d4974bb838a9ec25213f07d71eadb0e0c77a82771be3245b92f7ae9b9b0220`)

## design-choices (3 claim(s))

- [observation/documented] Bootstrap creates a dedicated OpenClaw gateway under ~/.openclaw-dench on port 19001, separate from a usual ~/.openclaw gateway, with config in ~/.openclaw-dench/openclaw.json. -- evidence: [README.md#L33-L35](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L33-L35) (`clm_b87f23ed0415829893b9b14b2c15b8921f6d1d9f40dd229c89b2490fc25b906a`)
- [observation/documented] Setting DENCHCLAW_DAEMONLESS=1 skips all gateway daemon management and launchd installation across commands, for Docker or environments without systemd/launchd; the gateway must then be run as a foreground process. -- evidence: [README.md#L72-L74](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L72-L74), [README.md#L76-L76](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L76-L76) (`clm_643d7ce14e79a30fc5872f000ae54ca7a5934973096b5084f885848b1949bb1a`)
- [observation/documented] Telemetry is anonymous and optional, split into product telemetry (CLI/web usage events) and AI observability via a PostHog LLM analytics plugin; both share opt-out controls and privacy mode, which is on by default and redacts message content and tool parameters. -- evidence: [TELEMETRY.md#L9-L11](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L9-L11), [TELEMETRY.md#L13-L13](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L13-L13), [TELEMETRY.md#L108-L111](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L108-L111), [TELEMETRY.md#L3-L5](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L3-L5), [TELEMETRY.md#L106-L106](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L106-L106) (`clm_04b81301411a384071e95bf4e09b85c2e19f15bbe1fcacba99ca0cc60ab7c5bc`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local development uses pnpm (pnpm install, pnpm build, pnpm dev, and pnpm web:dev for Web UI development). -- evidence: [README.md#L137-L140](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L137-L140), [README.md#L129-L130](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L129-L130), [README.md#L132-L133](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L132-L133) (`clm_bde32b3a9aaa60757e366a3e61713dc84d13ef0bcb178e999f0ecf84c70bcac0`)
- [observation/documented] Repository development practice: releases are driven by package.json; pushing a version bump to main triggers .github/workflows/release.yml, which runs deploy.sh checks in validation mode before publishing to npm and creating a GitHub release, with reruns safe via existence checks. -- evidence: [RELEASING.md#L7-L12](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L7-L12), [RELEASING.md#L3-L3](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L3-L3), [RELEASING.md#L14-L14](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L14-L14) (`clm_896710952dbd1f408ea93c33d3dbeed041c1edc1d3fb2ab2b4048a7c1a8486c6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] DenchClaw provides an npm CLI with subcommands bootstrap, update, restart, start, and stop for onboarding and managing the web server. -- evidence: [README.md#L51-L56](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L51-L56) (`clm_0a61ac4fd5959db8953d87a72b62191a05797638e9580d37f011349b807edcf7`)
- [observation/documented] OpenClaw commands for DenchClaw must be prefixed with 'openclaw --profile dench', e.g. gateway restart or config set gateway.port 19001. -- evidence: [README.md#L62-L66](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L62-L66), [README.md#L59-L60](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L59-L60) (`clm_ab05579102803d9f7115c940f0be3d366375581dff984005ea1497272ac54582`)
- [observation/documented] After onboarding, the web UI is served at localhost:3100 by default. -- evidence: [README.md#L33-L35](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L33-L35), [README.md#L45-L45](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L45-L45) (`clm_6cffd5f5b16d9fca6b952b7dc1d8f69f46eec0cca6f17a4610f0e06dd89d15ad`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Gateway connections use device pairing: a 'pairing required' error means the local device awaits approval, and pending operator requests can be listed and approved via 'openclaw --profile dench devices list/approve'. -- evidence: [README.md#L106-L107](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L106-L107), [README.md#L96-L96](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L96-L96), [README.md#L100-L102](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L100-L102), [README.md#L104-L104](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L104-L104) (`clm_700e3a0317cf2eea3354b15d1e279f02d4def9f0809c1ce55f501d87a1b0beea`)

## evaluation (1 claim(s))

- [observation/documented] PostHog Evaluations can score captured $ai_generation events using LLM-as-a-judge or deterministic Hog-based checks, storing pass/fail results with reasoning, configured entirely in the PostHog dashboard. -- evidence: [TELEMETRY.md#L129-L132](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L129-L132), [TELEMETRY.md#L134-L136](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L134-L136), [TELEMETRY.md#L126-L127](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L126-L127) (`clm_f957eaee971edd9c099b2cf40e25160ef50c16e6e4ebf5a28b954df2960ee995`)

## dependencies (1 claim(s))

- [observation/documented] Manual install requires Node 22+ and is run via 'npx denchclaw@latest bootstrap'; the product is built on OpenClaw and must be kept up to date with it. -- evidence: [README.md#L33-L35](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L33-L35), [README.md#L41-L43](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L41-L43), [README.md#L39-L39](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L39-L39) (`clm_f464192fdd2dd52c7873dbec40e325cf7e615e6181e1c3390fccc37cb86b6555`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

