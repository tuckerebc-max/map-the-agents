# oxgeneral/orch -- full detail

[Back to orientation](orch.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oxgeneral/orch/c066dc013e98e08d753ce204e604e04621dd4167/63003115ba6c9391.json](../../../wiki/dossiers/oxgeneral/orch/c066dc013e98e08d753ce204e604e04621dd4167/63003115ba6c9391.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The documented source layout includes domain (models, state machine), application (orchestrator engine, services, event bus), infrastructure (adapters, file storage, process management, LiquidJS templates, git worktree workspace), cli (Commander.js), and tui (Ink + React). -- evidence: [readme.md#L606-L618](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L606-L618) (`clm_d13e86e7b71a2d235b00d69607af451e7d611baabc9cec2863984070fc823c5a`)
- [observation/documented] Eight adapters are documented: Claude Code, OpenCode, Codex, Pi, Cursor, Grok, Antigravity, and Shell, where the shell adapter wraps any terminal CLI tool as an agent. -- evidence: [readme.md#L334-L334](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L334-L334), [readme.md#L711-L711](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L711-L711) (`clm_73a2fa9a38b90e6f54419894110e30021ecd96cfae5bac23943d763303bf82e5`)
- [observation/documented] Pre-built organization templates are provided (e.g. startup-mvp, pr-review-corp, migration-squad, security-dept, content-agency, data-lab, sales-machine, docs-team) deployable via `orch org deploy`, with export of custom setups. -- evidence: [readme.md#L375-L380](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L375-L380), [readme.md#L368-L373](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L368-L373), [readme.md#L357-L364](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L357-L364) (`clm_81fca59ea3a29c8b3a5ac861dcd6d032cd4d76749a8650f0174e25496be49562`)

## design-choices (2 claim(s))

- [observation/documented] Each agent works in an isolated git worktree on its own branch, and code reaches main only after explicit user approval through a mandatory review step in the task state machine. -- evidence: [readme.md#L198-L198](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L198-L198), [readme.md#L684-L684](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L684-L684) (`clm_9956bb50131e6ed127f2eda66b23e5f9e86f16ab9649e0740bff89cada5036aa`)
- [observation/documented] Tasks flow through a state machine (todo → in_progress → review → done) with validated transitions, and no code merges without approval. -- evidence: [readme.md#L265-L270](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L265-L270), [readme.md#L272-L272](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L272-L272) (`clm_cab5a1fa178971ea023cffef36eb30af85c3a1faef14849d68af9daecd41baf5`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] After installation, an `/orch` skill is reportedly available in Claude Code, translating natural-language requests into orch commands for agents, tasks, goals, and runs. -- evidence: [readme.md#L144-L144](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L144-L144), [readme.md#L150-L150](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L150-L150) (`clm_9949c9c5f9fd94f16d5909b6e4d3269c1086caa0d7b11e2925b0499568a82229`)

## interfaces (4 claim(s))

- [observation/documented] ORCH exposes a CLI including commands such as orch init, doctor, agent add/list, org deploy/export, task add/assign/cancel, team create, goal add, msg send/broadcast, run, serve, status, logs, and tui. -- evidence: [readme.md#L553-L557](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L553-L557), [readme.md#L542-L546](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L542-L546), [readme.md#L484-L488](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L484-L488), [readme.md#L530-L535](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L530-L535), [readme.md#L506-L511](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L506-L511), [readme.md#L564-L573](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L564-L573), [readme.md#L495-L499](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L495-L499), [readme.md#L518-L523](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L518-L523) (`clm_f5f29fbd0b7ae4437ede475e49b58c6a2e0a9b84600b96aa8dcda5093ca48e8c`)
- [observation/documented] The package can be imported as a library; the core reportedly has no dependency on the CLI/TUI layers, letting users build their own interface on top. -- evidence: [readme.md#L592-L592](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L592-L592) (`clm_0bd0f5f22d71c11d5ef518b271eb0f8eae03cad958f334c27546cd479d10c770`)
- [observation/documented] The CLI is published as the npm package @oxgeneral/orch, installed globally, and launching `orch` in a project opens a TUI dashboard after auto-initialization. -- evidence: [readme.md#L13-L19](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L13-L19), [readme.md#L36-L39](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L36-L39), [readme.md#L140-L140](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L140-L140) (`clm_5ecd8e0f55cf6451263727dcc2012865189445fd8a7bf5ac96586463c8cca31b`)
- [observation/documented] Serve mode emits one JSON line per event (e.g. agent:started, task:status_changed, orchestrator:tick) with configurable json/text format, optional log file, and a default 10000 ms tick interval. -- evidence: [readme.md#L419-L423](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L419-L423), [readme.md#L417-L417](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L417-L417), [readme.md#L407-L413](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L407-L413) (`clm_ca1122903fb4773dd73c69ec81c2d3eb6077f29fdb48bc2758aeda3ab49a3f82`)

## memory-state (1 claim(s))

- [observation/documented] Storage is file-based using YAML/JSON/JSONL, and agents communicate through direct messages, team broadcasts, and a shared context store. -- evidence: [readme.md#L255-L255](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L255-L255), [readme.md#L606-L618](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L606-L618) (`clm_4fca750d1579bb89b05b5efa0f3a5c80935ae5805b75527c1a6f1887e4112fe6`)

## orchestration (3 claim(s))

- [observation/documented] A CTO-style agent decomposes a high-level goal into tasks and delegates them; failed tasks auto-retry with exponential backoff and stalled agents are killed and re-queued by zombie detection. -- evidence: [readme.md#L240-L240](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L240-L240), [readme.md#L244-L244](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L244-L244) (`clm_13bd75b62e6872704931e609b0d874af568111c79315a5b02ed41b89bb2279eb`)
- [observation/documented] `orch serve` runs a headless daemon with a tick loop that picks up newly added tasks; a `--once` mode processes todo tasks and exits, with exit 0 meaning all done and exit 1 indicating failures. -- evidence: [readme.md#L399-L399](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L399-L399), [readme.md#L402-L403](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L402-L403), [readme.md#L461-L466](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L461-L466) (`clm_08569e44fc8bd43487689889348c5d96d9dced2ae1a09a227644c62f95570c32`)
- [observation/documented] The daemon enforces single-orchestrator-per-project via a lock file (.orchestry/orchestry.lock), shuts down gracefully on SIGINT/SIGTERM, logs heap usage each tick, and throttles idle-tick logging. -- evidence: [readme.md#L461-L466](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L461-L466) (`clm_7516dc2b3db2d8609a70e6c20dd1259b622fd18cf9f5c898f37ea6740ce0c709`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The runtime requires Node.js >= 20 on macOS, Linux, or WSL2, and needs no database, cloud service, Docker, or GPU since LLMs are accessed via API. -- evidence: [readme.md#L194-L194](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L194-L194), [readme.md#L168-L174](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L168-L174) (`clm_95b34a8fc44b365c6a4f30f774c90e4a0920f1eecc82f8a9fdfb9f711799b51e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] ORCH targets solo founders and small teams running multiple AI coding/CLI agents on one project, positioning itself as open-source (MIT) orchestration where users pay only for their own AI API usage. -- evidence: [readme.md#L675-L675](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L675-L675), [readme.md#L8-L11](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L8-L11), [readme.md#L702-L702](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L702-L702) (`clm_639e84802208e1b57113845f1f3b831ab7353ba48554e3009d850bdad05f0bdc`)

