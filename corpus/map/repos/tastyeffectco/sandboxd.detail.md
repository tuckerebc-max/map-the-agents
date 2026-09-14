# tastyeffectco/sandboxd -- full detail

[Back to orientation](sandboxd.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tastyeffectco/sandboxd/146711407bb9b3b0354b87758e3f9132e6616e12/f76f0ae5fc6ee5ae.json](../../../wiki/dossiers/tastyeffectco/sandboxd/146711407bb9b3b0354b87758e3f9132e6616e12/f76f0ae5fc6ee5ae.json)

## specifications (1 claim(s))

- [observation/documented] sandboxd is an open-source, self-hosted AI app builder: a prompt causes a coding agent to build a real app in an isolated sandbox on the user's server, each app live at a preview URL. -- evidence: [README.md#L3-L7](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L3-L7), [README.md#L79-L81](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L79-L81) (`clm_67acda3a4f656d110d3cc1f516153c97d1261e1600b7139d0e7939c04e5e2f32`)

## components (1 claim(s))

- [observation/documented] The system is a single Go control-plane binary that shells out to the Docker CLI (no SDK), fronted by Traefik for preview routing, with SQLite (WAL) as the source of truth and an in-sandbox supervisor called runtimed baked into the base image. -- evidence: [ARCHITECTURE.md#L48-L65](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L48-L65), [ARCHITECTURE.md#L12-L28](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L12-L28), [ARCHITECTURE.md#L68-L70](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L68-L70) (`clm_25c10b740f7138f0607433ae782c7879e69fb45e395fa2cecc99a2d2eec56cd4`)

## design-choices (2 claim(s))

- [observation/documented] Agent credentials never enter a sandbox: a control-plane-side auth proxy holds the real keys and injects Authorization/X-Api-Key on the wire, giving the sandbox only a base URL and a dummy key; credential-shaped env vars are scrubbed from agent processes. -- evidence: [ARCHITECTURE.md#L102-L128](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L102-L128), [AGENTS.md#L97-L100](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L97-L100) (`clm_8cbd2e7199062aab13b507b0bf4591f3c4747abd761fb8f1efbf2bba847c7ed5`)
- [observation/documented] Each sandbox exposes exactly one public preview endpoint (the manifest's web.port); HTTP, WebSocket upgrades, and SSE all work on that single port, while multi-port apps are not reachable on a second port (multi-port is roadmap, not current behaviour). -- evidence: [ARCHITECTURE.md#L224-L234](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L224-L234) (`clm_39193b384bd8514484a026e19972e97238779c8b5b22456acf87ff3b40d3c7c5`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENTS.md is a copy-pasteable runbook for an AI agent or human to install (./install.sh), operate, drive the API, run the console profile, and uninstall (./uninstall.sh with --images/--data flags) sandboxd. -- evidence: [AGENTS.md#L3-L6](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L3-L6), [AGENTS.md#L23-L31](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L23-L31), [AGENTS.md#L139-L145](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L139-L145), [AGENTS.md#L119-L128](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L119-L128) (`clm_e00752f04b3c9ba228ac94d7b44c043cd359127834ca14226a42ee9322f09d6e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (1 claim(s))

- [observation/documented] Workspaces live under SANDBOXD_DATA_DIR/workspaces/<id> as bind mounts and survive stop and reboot; control-plane state is a SQLite file; the container writable layer is none (read-only rootfs) and /tmp is tmpfs, so only /home/sandbox is writable in-sandbox. -- evidence: [ARCHITECTURE.md#L48-L65](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L48-L65), [ARCHITECTURE.md#L178-L179](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L178-L179), [ARCHITECTURE.md#L171-L176](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L171-L176) (`clm_39b6b7a89fcb55dc055d665d7f35047a2b89091a28d718484b734e9f615865f9`)

## orchestration (1 claim(s))

- [observation/documented] The control plane runs an idle reaper that stops sandboxes past an idle threshold and a pressure reaper that stops sandboxes when host memory is low; a wake path starts a stopped container on the first preview request and serves a warming page. -- evidence: [ARCHITECTURE.md#L48-L65](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L48-L65), [ARCHITECTURE.md#L151-L157](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L151-L157) (`clm_eb1ea4d0c150f30055784d8e55d2a215367413a8720316182b7714ca95760e5f`)

## tools-permissions (1 claim(s))

- [observation/documented] Sandboxes run under hardened runc with all capabilities dropped, no-new-privileges, a read-only rootfs with tmpfs /tmp, a hard memory ceiling, pids limit, and fd ulimits; the threat model is authenticated users running their own code, not hostile multi-tenancy. -- evidence: [ARCHITECTURE.md#L161-L167](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L161-L167) (`clm_d23df24be027342632044db5df6a1ad4e1f3468865c2175e324ea82e033ae1a6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running sandboxd requires Docker plus the Compose plugin and git on Linux (macOS via Docker Desktop is best-effort), runs natively on amd64 and arm64, and installs via a one-line curl script. -- evidence: [README.md#L159-L162](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L159-L162), [README.md#L164-L166](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L164-L166) (`clm_468c5c1ae1ae6b478fc7ff3d1c29c1f008e0c5d7059cd5c600a6781644b11068`)

## limitations (2 claim(s))

- [observation/documented] The project is beta 0.x: isolation is containers rather than VMs, it is single-server, API auth is off by default, and breaking changes are expected before 1.0. -- evidence: [README.md#L279-L282](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L279-L282) (`clm_75b5815b0090f20052326fae8ec7601288a8ef2a5e94d455fa4506bd6e8514b8`)
- [observation/documented] Documented trade-offs include no per-workspace disk quota, default-allow unlogged egress, one instance-wide base image with no per-app image selection, experimental snapshots on directory storage, and no in-sandbox service layer for Postgres/MySQL/Redis. -- evidence: [ARCHITECTURE.md#L210-L220](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L210-L220), [ARCHITECTURE.md#L238-L244](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L238-L244) (`clm_27c2cdae83c088c029611f5af0bc7b75dd52ee21d0bfd1d820ef60ac1e2159b7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

