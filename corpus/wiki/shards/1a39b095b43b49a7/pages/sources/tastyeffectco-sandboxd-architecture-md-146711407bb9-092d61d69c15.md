---
access: public
aliases: []
claim_ids:
- clm_25c10b740f7138f0607433ae782c7879e69fb45e395fa2cecc99a2d2eec56cd4
- clm_27c2cdae83c088c029611f5af0bc7b75dd52ee21d0bfd1d820ef60ac1e2159b7
- clm_39193b384bd8514484a026e19972e97238779c8b5b22456acf87ff3b40d3c7c5
- clm_39b6b7a89fcb55dc055d665d7f35047a2b89091a28d718484b734e9f615865f9
- clm_8cbd2e7199062aab13b507b0bf4591f3c4747abd761fb8f1efbf2bba847c7ed5
- clm_d23df24be027342632044db5df6a1ad4e1f3468865c2175e324ea82e033ae1a6
- clm_eb1ea4d0c150f30055784d8e55d2a215367413a8720316182b7714ca95760e5f
maturity: draft
page_id: pg_c2767a5419e35887b63c092d61d69c15
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c01c22871b1156a3b740a4f963ee2552
title: tastyeffectco/sandboxd/ARCHITECTURE.md @ 146711407bb9
updated_at: '2026-09-14T03:18:13Z'
---

# tastyeffectco/sandboxd/ARCHITECTURE.md @ 146711407bb9

<!-- rcw:begin owner=source:src_c01c22871b1156a3b740a4f963ee2552 block=evidence -->
- The system is a single Go control-plane binary that shells out to the Docker CLI (no SDK), fronted by Traefik for preview routing, with SQLite (WAL) as the source of truth and an in-sandbox supervisor called runtimed baked into the base image. [@claim:clm_25c10b740f7138f0607433ae782c7879e69fb45e395fa2cecc99a2d2eec56cd4]
- Documented trade-offs include no per-workspace disk quota, default-allow unlogged egress, one instance-wide base image with no per-app image selection, experimental snapshots on directory storage, and no in-sandbox service layer for Postgres/MySQL/Redis. [@claim:clm_27c2cdae83c088c029611f5af0bc7b75dd52ee21d0bfd1d820ef60ac1e2159b7]
- Each sandbox exposes exactly one public preview endpoint (the manifest's web.port); HTTP, WebSocket upgrades, and SSE all work on that single port, while multi-port apps are not reachable on a second port (multi-port is roadmap, not current behaviour). [@claim:clm_39193b384bd8514484a026e19972e97238779c8b5b22456acf87ff3b40d3c7c5]
- Workspaces live under SANDBOXD_DATA_DIR/workspaces/<id> as bind mounts and survive stop and reboot; control-plane state is a SQLite file; the container writable layer is none (read-only rootfs) and /tmp is tmpfs, so only /home/sandbox is writable in-sandbox. [@claim:clm_39b6b7a89fcb55dc055d665d7f35047a2b89091a28d718484b734e9f615865f9]
- Agent credentials never enter a sandbox: a control-plane-side auth proxy holds the real keys and injects Authorization/X-Api-Key on the wire, giving the sandbox only a base URL and a dummy key; credential-shaped env vars are scrubbed from agent processes. [@claim:clm_8cbd2e7199062aab13b507b0bf4591f3c4747abd761fb8f1efbf2bba847c7ed5]
- Sandboxes run under hardened runc with all capabilities dropped, no-new-privileges, a read-only rootfs with tmpfs /tmp, a hard memory ceiling, pids limit, and fd ulimits; the threat model is authenticated users running their own code, not hostile multi-tenancy. [@claim:clm_d23df24be027342632044db5df6a1ad4e1f3468865c2175e324ea82e033ae1a6]
- The control plane runs an idle reaper that stops sandboxes past an idle threshold and a pressure reaper that stops sandboxes when host memory is low; a wake path starts a stopped container on the first preview request and serves a warming page. [@claim:clm_eb1ea4d0c150f30055784d8e55d2a215367413a8720316182b7714ca95760e5f]
<!-- rcw:end owner=source:src_c01c22871b1156a3b740a4f963ee2552 block=evidence -->

## Researcher notes

