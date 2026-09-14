# shoyann/thrush-swe-agent -- full detail

[Back to orientation](thrush-swe-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shoyann/thrush-swe-agent/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/ad148bedd351dcd1.json](../../../wiki/dossiers/shoyann/thrush-swe-agent/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/ad148bedd351dcd1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Auto Mode is backed by a bundled mini-swe-agent checkout in vendor/mini-swe-agent with a non-interactive runner at scripts/mini-auto-run.py; an ADR states the bundled copy should be managed as a Git submodule or clearly tracked vendored dependency. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [docs/adr/0003-bundle-mini-swe-agent.md#L3-L3](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/docs/adr/0003-bundle-mini-swe-agent.md#L3-L3) (`clm_7e6464333ecf12589fc953d9d751453083ee9243650e60a1f3ab0b41c14c0a89`)
- [observation/documented] Auto runs collect diff, diff stat, changed files, logs, and trajectory, and generate a human-readable Auto Report shown with these artifacts in a side drawer. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L133-L138](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L133-L138) (`clm_4dbc1854ca6ee65c4edb73b974457d5cb7c7e3fe0a2d7143f1c3ed208d30ff4e`)

## design-choices (1 claim(s))

- [observation/documented] Thrush offers two modes in one UI: Assist, where the agent drafts edits and the user approves before files are written, and Auto, where the agent attempts a full task in isolation and returns a report and diff. -- evidence: [README.md#L28-L31](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L28-L31), [README.md#L7-L11](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L7-L11) (`clm_caebe72601b17f80ddb6c1159a90fea84a793edaa0f60c8de3addc9fd4d7c9a4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run npm run test, npx tsc --noEmit, and npm run lint; the repo includes tests for Auto data flow, readiness checks, recommended environments, the mini resolver, and runner behavior with fake mini results. -- evidence: [README.md#L215-L215](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L215-L215), [README.md#L209-L213](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L209-L213) (`clm_c8dbd520fe1832b697c76f960007c48bfad79cb9920a451cc59687cd6e6dde45`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Before Auto starts, an Environment Doctor checks Git clean state, Docker availability, mini runtime readiness, model API key configuration, and GitHub readiness. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L125-L129](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L125-L129) (`clm_93207794c906f7a5a3a5e6e38ba6ddc9a9805a92efd99242a9b5a319a3bdb448`)
- [observation/documented] Model providers are configurable via environment variables: MODEL_PROVIDER supports deepseek (default), openai, or anthropic, with per-provider API key, base URL, and model variables, plus an AGENT_API_SECRET bearer token for /api/agent. -- evidence: [README.md#L82-L87](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L82-L87), [README.md#L162-L179](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L162-L179) (`clm_f2bc33ea7684df7f6a7858e9d8226ef2e94d3c3d788a7b3926bba918a7b18b80`)

## memory-state (1 claim(s))

- [observation/documented] Local state lives under data/: a SQLite database (thrush.db) with separate tables for Auto runs, events, artifacts, and presets, plus workspace, auto-runs, mini-venv, and pip/uv cache directories. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L185-L191](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L185-L191) (`clm_da554f128ee17778a6872f38ab62432877141a3474cb58e3567b7d1f19ffd8b1`)

## orchestration (2 claim(s))

- [observation/documented] Auto Mode runs mini-swe-agent in a separate Git worktree under data/auto-runs/<autoRunId>/worktree on a branch auto/<autoRunId>, leaving the main workspace unchanged; Draft PR creation is a user action, not automatic. -- evidence: [README.md#L197-L197](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L197-L197), [README.md#L33-L33](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L33-L33), [README.md#L133-L138](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L133-L138) (`clm_cb8a432e7cfe1bdf21b8a023f1eff93e4828ede144acb95f3bef8d40e8ef5d2b`)
- [observation/documented] A local Auto Worker claims queued runs, manages mini-swe-agent processes, handles cancellation, and writes events and artifacts, keeping long-running jobs separate from request handling. -- evidence: [docs/adr/0004-use-auto-worker.md#L3-L3](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/docs/adr/0004-use-auto-worker.md#L3-L3) (`clm_74652a3b62831b900d747c1d380e7ea37a89a2a8214fd7a361482d0593421807`)

## tools-permissions (2 claim(s))

- [observation/documented] In Assist Mode the agent can inspect files, search code, read pages, and run allowlisted commands; file writes are staged as pending drafts requiring explicit approval, and file tools reject paths outside the active workspace. -- evidence: [README.md#L219-L224](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L219-L224), [README.md#L152-L152](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L152-L152) (`clm_e8315007274e6a17064b2d3d7e1cb1b81721f103b1bff49beab64cb58bfdca43`)
- [observation/documented] Auto Runs execute mini-swe-agent in a Docker environment by default because the agent runs autonomously; local shell execution is an explicit advanced opt-in that gives the agent unrestricted host command access. -- evidence: [docs/adr/0001-default-auto-runs-to-docker.md#L3-L3](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/docs/adr/0001-default-auto-runs-to-docker.md#L3-L3) (`clm_699acd4ba97d5823bd8f1cabd51fefe13fb8f06327cffd3255dc264d1b2d93bc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The app is built with Next.js 15 and TypeScript 5, uses SQLite for local state, and bundles mini-swe-agent; a bootstrap step prepares data/mini-venv with the bundled agent and Python dependencies. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L13-L18](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L13-L18), [README.md#L72-L72](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L72-L72) (`clm_3c2f5390bbb0afe128de2d0e68b8c9e306100cf4913dec904c880f587b3b2d1a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

