# 5dive-ai/5dive -- full detail

[Back to orientation](5dive.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/5dive-ai/5dive/420651c634b0180b8efc189a357a47ea8f02ceb3/00021c2ed875dd28.json](../../../wiki/dossiers/5dive-ai/5dive/420651c634b0180b8efc189a357a47ea8f02ceb3/00021c2ed875dd28.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Agents take work from a shared SQLite task queue on one host, report up an org chart, hand work to each other, and escalate to a human via Telegram only when a decision is needed. -- evidence: [README.md#L81-L81](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L81-L81), [README.md#L40-L40](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L40-L40), [README.md#L293-L293](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L293-L293), [README.md#L280-L280](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L280-L280) (`clm_abd22f7ea7acdd2a5dc01c842a56c88e8cbb9d7956ee370b44548ea42dbc5730`)
- [observation/documented] Multiple agent types are supported, including claude, codex, antigravity, grok, devin, hermes, openclaw, opencode, and pi, each with its own auth options and channel support (Telegram and/or Discord). -- evidence: [README.md#L109-L119](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L109-L119) (`clm_9a747d4b3299db6f04e4ef4107e25799d1f69e8bf800cd34ecc57a3b1b2f7fbf`)

## design-choices (1 claim(s))

- [observation/documented] The orchestrator is deliberately just bash: each agent is its own Linux user running an official coding CLI as a systemd service, with no framework, protocol, or broker; agents coordinate by invoking one shared 5dive CLI. -- evidence: [README.md#L97-L97](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L97-L97), [README.md#L103-L103](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L103-L103), [README.md#L38-L38](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L38-L38) (`clm_6d48cb196ea12f9523eb26ff71576bfdc99d70e096073bb8b715deb5ada93811`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the 5dive bundle at the repo root is built from src/ via ./build.sh, and CI enforces that the bundle does not drift; contributing guidance lives in CONTRIBUTING.md. -- evidence: [README.md#L497-L497](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L497-L497) (`clm_d7a1ffcb8a8c306e0b48d2a89a74ef43c3ab9877882a23caaa64246620817d9a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The 5dive CLI exposes verbs for agent lifecycle (create/start/stop/logs/config), tasks, goals, loops, council, trace, run metrics, memory search, triggers, heartbeat, org, ui, account, and team import; every command accepts --json with an {ok,data}/{ok:false,error} envelope and exit codes matching error.code. -- evidence: [README.md#L385-L395](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L385-L395), [README.md#L473-L473](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L473-L473), [README.md#L369-L377](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L369-L377), [README.md#L379-L383](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L379-L383), [README.md#L361-L367](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L361-L367) (`clm_da3186d6d657068d89b343e6e34d5752d1349c292065e6b460461d58d35cc523`)
- [observation/documented] `5dive ui` serves a local, read-only web UI on loopback (default port 8735) with org chart, queue, gates, and triggers views; it refuses routable --host addresses unless FIVE_UI_ALLOW_REMOTE=1 is set. -- evidence: [README.md#L357-L357](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L357-L357), [README.md#L346-L348](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L346-L348), [README.md#L352-L355](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L352-L355) (`clm_2c962fe3fb8b0e08eb4bdf0e27182a7f2325d4d2afd11a5fc27945859c97a218`)
- [inference/documented] A design doc proposes decentralizing loop installation so `5dive loop install` resolves refs from any author-hosted github:/https: manifest, with the central index demoted to an optional discovery list and optional ed25519 signature verification; this appears to be a spec, not yet shipped behavior. -- evidence: [docs/agenticloops-decentralized-install.md#L28-L33](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/agenticloops-decentralized-install.md#L28-L33), [docs/agenticloops-decentralized-install.md#L3-L7](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/agenticloops-decentralized-install.md#L3-L7), [docs/agenticloops-decentralized-install.md#L57-L64](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/agenticloops-decentralized-install.md#L57-L64), [docs/agenticloops-decentralized-install.md#L16-L21](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/agenticloops-decentralized-install.md#L16-L21) (`clm_016102a7f5d09a07c02fe344ff7c04c359b5701b0727b50a8d0f5966ba443c71`)

## memory-state (2 claim(s))

- [observation/documented] Governance policy can be loaded from a constitution.yaml in the state dir (or FIVEDIVE_CONSTITUTION_FILE); if the file is absent or malformed the loader falls back atomically to shipped defaults and never applies a partial document. -- evidence: [docs/constitution.md#L3-L7](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/constitution.md#L3-L7) (`clm_9a22dca3a726dfdf22e94c4ac2871ffd25f03069392b9b244ceb86f273859797`)
- [observation/documented] The CLI offers durable team memory with provenance via `5dive memory search`, and Claude-runtime agents keep project memory under ~/.claude/projects/<dir>/memory/ across restarts. -- evidence: [README.md#L216-L217](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L216-L217), [README.md#L455-L455](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L455-L455) (`clm_a59cd720f80a3546294818c84947c582c058c394fd37939bb205a65e92046e7a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Each agent runs as its own Linux user under one of three isolation tiers: standard (shared read, limited write), admin (full host, auto-granted to the first agent on a fresh box), or sandboxed (own home, no sudo, systemd resource limits). -- evidence: [README.md#L246-L246](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L246-L246), [README.md#L248-L252](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L248-L252) (`clm_b06e6c4010e23dfcb83ee5b4f1fc476d9626a873362249d303b7b150748598d7`)
- [observation/documented] Delegated git push uses the operator's own GitHub App: the agent never holds a token; pushes are gate-gated on a human- or reviewer-cleared ship gate, restricted to one non-protected branch, and executed in a root-only helper with a repo-scoped short-lived token. -- evidence: [README.md#L418-L418](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L418-L418), [README.md#L427-L431](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L427-L431) (`clm_66444387b3258616d3bbadd052d91a323811eb6e43a72b0c2af8738ebbdebae4`)

## evaluation (1 claim(s))

- [observation/documented] The repo publishes a 'zero-human' badge measured as releases shipped versus decisions escalated to a human, presented as evidence that the agents building 5dive.ai operate autonomously on the same binary. -- evidence: [README.md#L44-L44](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L44-L44), [README.md#L14-L18](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L14-L18) (`clm_a69b4f8637668c206f48411b24049dc5fa7d07abf8d9bd116ac5ec19364de449`)

## dependencies (1 claim(s))

- [observation/documented] Requirements are a Linux host with systemd (Ubuntu 22.04+ recommended) and root for install; the installer apt-installs jq, tmux, and other dependencies, and a Docker image exists for hosts without systemd or root. -- evidence: [README.md#L459-L460](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L459-L460), [README.md#L462-L462](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L462-L462), [README.md#L437-L442](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L437-L442) (`clm_1fc47716ca4b45f065ea8e07ee736ebbfe058da967728431cee52df7cf8fdeeb`)

## limitations (1 claim(s))

- [observation/documented] 5dive does not auto-update; operators run `5dive self-update` manually or on a cron schedule, which refreshes the CLI, hooks, skills, and plugins and restarts running agents. -- evidence: [README.md#L446-L453](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L446-L453) (`clm_66e6bb78e704f367e2b9a731507899d964beeab371eee0a20ceaa69f9ebe1572`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

