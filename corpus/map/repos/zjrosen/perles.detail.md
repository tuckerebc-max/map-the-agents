# zjrosen/perles -- full detail

[Back to orientation](perles.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zjrosen/perles/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/a14eba7bf0be77df.json](../../../wiki/dossiers/zjrosen/perles/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/a14eba7bf0be77df.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The Control Plane comprises ControlPlane (lifecycle entry point), Registry (in-memory workflow storage), Supervisor, ResourceScheduler, HealthMonitor, and CrossWorkflowEventBus. -- evidence: [docs/CONTROL_PLANE.md#L66-L73](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L66-L73) (`clm_db79fa544a6d6824eec2af225c6372862eda6ef3abb381a67a65d57dfa95b1ab`)

## design-choices (2 claim(s))

- [observation/documented] Because Cursor reads MCP config only from .cursor/mcp.json, Perles writes role-specific server entries (orchestrator, per-worker, observer) into that shared file using a read-merge-write pattern. -- evidence: [docs/CURSOR_AGENT.md#L62-L62](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L62-L62), [docs/CURSOR_AGENT.md#L121-L121](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L121-L121), [docs/CURSOR_AGENT.md#L41-L41](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L41-L41), [docs/CURSOR_AGENT.md#L114-L114](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L114-L114) (`clm_ca60a241d71e0e380f83af37ead67cdb5acd88eb87175b101011a3f1d88c8516`)
- [observation/documented] Since Cursor lacks --append-system-prompt, Perles prepends the system prompt to the main prompt with a blank line separator, the same approach used for OpenCode. -- evidence: [docs/CURSOR_AGENT.md#L66-L66](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L66-L66) (`clm_503e285b1c2946cadebdc933aec798870296aca511fa21ad49d1fd537a77bbe9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: optional Cursor integration tests are build-tagged, run via go test -tags=cursor_integration, and are intended for local/dev environments rather than CI. -- evidence: [docs/CURSOR_AGENT.md#L94-L96](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L94-L96), [docs/CURSOR_AGENT.md#L90-L92](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L90-L92), [docs/CURSOR_AGENT.md#L84-L86](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L84-L86) (`clm_4e82b99eea7f379e5d9b27ddbbea96abd6a3007ce00b429e1f9fb3518851c1fc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Perles is a terminal UI for beads issue tracking powered by a custom BQL query language supporting boolean search, date filters, dependency traversal, and custom kanban views. -- evidence: [README.md#L3-L3](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/README.md#L3-L3) (`clm_67d304b32d49e6d6804bf7e4cb1f997137ee6f9fc06767fee16450e420195454`)
- [observation/documented] The CLI supports flags including --beads-dir, --config, --version, --help, and --debug, plus subcommands: perles (TUI), themes, workflows, and playground. -- evidence: [docs/getting-started.md#L62-L68](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L62-L68), [docs/getting-started.md#L72-L77](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L72-L77) (`clm_d023e10be69a11ffa689e2a4c84458c13c638bd91e6f2155b7cf65ff86bebe59`)
- [observation/documented] Global keybindings include ctrl+space to switch between Kanban and Search modes, ctrl+o to enter Orchestration/Dashboard mode, ? for help, and ctrl+c to quit. -- evidence: [docs/getting-started.md#L85-L90](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L85-L90) (`clm_5d91c901528c90de287e78daa34aa3331a8792b2089765c9fdacf0a3b4017b6b`)
- [observation/documented] The dashboard TUI offers keyboard actions for navigating workflows, filtering, starting (s), pausing (p), stopping (x), creating (n/N), and opening detail views. -- evidence: [docs/CONTROL_PLANE.md#L83-L98](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L83-L98) (`clm_b8fa05cd744f317cc191d5e3d32fc126c296dc3484d0b5ccb2aa0e1159a17183`)
- [observation/documented] Workflows move through states Pending, Running, Paused, Completed, Failed, and Stopped, with documented transitions including stop from pending, running, or paused. -- evidence: [docs/CONTROL_PLANE.md#L113-L125](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L113-L125), [docs/CONTROL_PLANE.md#L102-L109](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L102-L109) (`clm_bed82846bba2df1c454fe00cf07e28c8efc9a13835b6e95a60174f3bf6fd4678`)
- [observation/documented] Control Plane behavior is configured in ~/.config/perles/config.yaml under orchestration.control_plane, with resource policy defaults of 5 concurrent workflows, 10 workers, 5 AI calls, and MCP ports 9000-9100. -- evidence: [docs/CONTROL_PLANE.md#L155-L162](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L155-L162), [docs/CONTROL_PLANE.md#L131-L131](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L131-L131), [docs/CONTROL_PLANE.md#L133-L142](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L133-L142) (`clm_c69dcfae9bab0606dc85417860b81d5ea2504fb44f3e4b8e46e463f2bac98f7a`)

## memory-state (1 claim(s))

- [observation/documented] Workflow instances track identity, state, priority, labels, timestamps, runtime infrastructure/session/MCP port, token budget, and last heartbeat/progress times; the Registry stores them in memory. -- evidence: [docs/CONTROL_PLANE.md#L258-L261](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L258-L261), [docs/CONTROL_PLANE.md#L263-L267](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L263-L267), [docs/CONTROL_PLANE.md#L244-L249](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L244-L249), [docs/CONTROL_PLANE.md#L66-L73](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L66-L73), [docs/CONTROL_PLANE.md#L251-L253](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L251-L253), [docs/CONTROL_PLANE.md#L269-L273](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L269-L273) (`clm_e3d36677ff0027f70548783283f85b5471fa4b8a435b3ab55768dc95fc6f1347`)

## orchestration (3 claim(s))

- [observation/documented] Orchestration mode is a multi-agent control plane where a coordinator headless agent spawns, replaces, and retires worker agents via built-in MCP tools, with multiple workflows run in parallel. -- evidence: [ORCHESTRATION.md#L10-L11](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L10-L11), [ORCHESTRATION.md#L6-L8](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L6-L8) (`clm_5fe13e564fac56548fb95e11f15250fa0c114e1fee368ddd63877e69fa36a9ba`)
- [observation/documented] Orchestration providers include Claude, Amp, Codex, OpenCode, and Cursor Agent CLI; coordinator and worker clients can be mixed, e.g. cursor coordinator with claude workers. -- evidence: [docs/CURSOR_AGENT.md#L3-L3](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L3-L3), [docs/CURSOR_AGENT.md#L19-L19](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L19-L19), [ORCHESTRATION.md#L26-L29](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L26-L29) (`clm_68f82f927b6499f0b63334cf5fb9d06e259ebd2f9fadd0c9a207804df49b0bc9`)
- [observation/documented] The Control Plane supports multiple concurrent workflows with resource governance, health monitoring with stuck-workflow recovery, a dashboard TUI, and unified event aggregation. -- evidence: [docs/CONTROL_PLANE.md#L9-L13](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L9-L13) (`clm_9ef6f051824f29988f18b9657fd327695e71b43f41d44bdd19d0ad813380dd2f`)

## tools-permissions (1 claim(s))

- [observation/documented] The documentation warns that orchestration mode spawns headless AI agents that run with full permissions and can incur significant cost. -- evidence: [ORCHESTRATION.md#L3-L4](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L3-L4) (`clm_095bacad848204c4350d642916208f241e501dfd657705467a90ed59b8500359`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Perles requires a beads or beads-rust project with a .beads directory and a minimum beads database version of v0.62.0, upgradable via bd migrate. -- evidence: [README.md#L43-L44](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/README.md#L43-L44) (`clm_f667685ed442c4a2d0da97b271e381e793358542db02b964e9a5471788e0fab3`)
- [observation/documented] Using the Cursor provider requires the cursor-agent CLI on PATH; installing from source requires Go 1.27+. -- evidence: [docs/CURSOR_AGENT.md#L74-L74](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L74-L74), [docs/getting-started.md#L20-L20](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L20-L20) (`clm_76bf15a24d7e2c3d90352a377fd0f0cea1008b57ecc7460d6f62587266ad3307`)

## limitations (2 claim(s))

- [observation/documented] With the Cursor provider, token and cost fields show zero because Cursor's stream-json output lacks usage and cost data. -- evidence: [docs/CURSOR_AGENT.md#L102-L102](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L102-L102) (`clm_ae865c03813fb4c44446b647af734672451ce92b2e72db0cc8bcf004ed8d52ac`)
- [observation/documented] Cursor CLI does not support tool filtering flags, so all agent tools remain enabled and the DisallowedTools config field is silently ignored for that provider. -- evidence: [docs/CURSOR_AGENT.md#L106-L106](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L106-L106) (`clm_5487d2c58aa59d90888259336c8f2d28a0b823d8d2dc14049b98e1503155f97a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

