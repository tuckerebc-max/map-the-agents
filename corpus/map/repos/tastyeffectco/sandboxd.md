# tastyeffectco/sandboxd

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 146711407bb9 @ f76f0ae5fc6ee5ae

## Summary (orientation draft, not independently verified)

Selected evidence records: sandboxd is an open-source, self-hosted AI app builder: a prompt causes a coding agent to build a real app in an isolated sandbox on the user's server, each app live at a preview URL. The system is a single Go control-plane binary that shells out to the Docker CLI (no SDK), fronted by Traefik for preview routing, with SQLite (WAL) as the source of truth and an in-sandbox supervisor called runtimed baked into the base image.

## Source coverage

Source coverage (partial): 3 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] sandboxd is an open-source, self-hosted AI app builder: a prompt causes a coding agent to build a real app in an isolated sandbox on the user's server, each app live at a preview URL. -- evidence: [README.md#L3-L7](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L3-L7), [README.md#L79-L81](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/README.md#L79-L81)
- components (1 claim(s)):
  - [observation/documented] The system is a single Go control-plane binary that shells out to the Docker CLI (no SDK), fronted by Traefik for preview routing, with SQLite (WAL) as the source of truth and an in-sandbox supervisor called runtimed baked into the base image. -- evidence: [ARCHITECTURE.md#L48-L65](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L48-L65), [ARCHITECTURE.md#L12-L28](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L12-L28), [ARCHITECTURE.md#L68-L70](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L68-L70)
- design-choices (2 claim(s)):
  - [observation/documented] Agent credentials never enter a sandbox: a control-plane-side auth proxy holds the real keys and injects Authorization/X-Api-Key on the wire, giving the sandbox only a base URL and a dummy key; credential-shaped env vars are scrubbed from agent processes. -- evidence: [ARCHITECTURE.md#L102-L128](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L102-L128), [AGENTS.md#L97-L100](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L97-L100)
  - [observation/documented] Each sandbox exposes exactly one public preview endpoint (the manifest's web.port); HTTP, WebSocket upgrades, and SSE all work on that single port, while multi-port apps are not reachable on a second port (multi-port is roadmap, not current behaviour). -- evidence: [ARCHITECTURE.md#L224-L234](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L224-L234)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md is a copy-pasteable runbook for an AI agent or human to install (./install.sh), operate, drive the API, run the console profile, and uninstall (./uninstall.sh with --images/--data flags) sandboxd. -- evidence: [AGENTS.md#L3-L6](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L3-L6), [AGENTS.md#L23-L31](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L23-L31), [AGENTS.md#L139-L145](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L139-L145), [AGENTS.md#L119-L128](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/AGENTS.md#L119-L128)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state (1 claim(s)):
  - [observation/documented] Workspaces live under SANDBOXD_DATA_DIR/workspaces/<id> as bind mounts and survive stop and reboot; control-plane state is a SQLite file; the container writable layer is none (read-only rootfs) and /tmp is tmpfs, so only /home/sandbox is writable in-sandbox. -- evidence: [ARCHITECTURE.md#L48-L65](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L48-L65), [ARCHITECTURE.md#L178-L179](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L178-L179), [ARCHITECTURE.md#L171-L176](https://github.com/tastyeffectco/sandboxd/blob/146711407bb9b3b0354b87758e3f9132e6616e12/ARCHITECTURE.md#L171-L176)
- orchestration (1 claim(s)):
More evidence: [full detail](sandboxd.detail.md)

Metadata and full claim list: [full detail](sandboxd.detail.md)
Human notes ([notes](sandboxd.notes.md), never overwritten by build)

[Back to map index](../../index.md)
