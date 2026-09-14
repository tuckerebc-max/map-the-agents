---
access: public
aliases: []
claim_ids:
- clm_d93387b1a99c554df0f156da90a3c302707cccbcc40c0346c3d9f69519e5bcde
- clm_e50a8246cedf5912f0eae6378494203698501ec6ef69568902a56b87cd1b1640
- clm_e59eb1dd41b81a120cdc28850402c76e612d4b7040b2482363470b04bb408920
- clm_f998c5bb9928e7ded53452411afad097e2584eec3bed5c2d253048c983e6e9c6
maturity: draft
page_id: pg_3edbbc8153795d638f3b6187ee03bc44
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_68bb307225295cee8b4ab485112cfe7f
title: jmfederico/pi-web/docs/config.md @ 46579c049a30
updated_at: '2026-09-14T02:08:25Z'
---

# jmfederico/pi-web/docs/config.md @ 46579c049a30

<!-- rcw:begin owner=source:src_68bb307225295cee8b4ab485112cfe7f block=evidence -->
- PI_WEB_DATA_DIR sets the root for managed runtime state (default ~/.pi-web), holding project and machine registries, discovered plugins, the session-daemon socket, and session archives; each data directory starts independent and empty. [@claim:clm_d93387b1a99c554df0f156da90a3c302707cccbcc40c0346c3d9f69519e5bcde]
- One live session daemon owns each data directory, recording ownership in sessiond-owner.json; a second daemon pointed at the same directory fails loudly at startup, while stale markers from dead daemons are taken over automatically. [@claim:clm_e50a8246cedf5912f0eae6378494203698501ec6ef69568902a56b87cd1b1640]
- By default workspace-relative file reads stay inside the workspace and absolute paths are denied; pathAccess.allowedPaths grants the file explorer access to specific external filesystem roots, with symlink escapes rejected, though this is not a sandbox for the agent or OS user. [@claim:clm_e59eb1dd41b81a120cdc28850402c76e612d4b7040b2482363470b04bb408920]
- Configuration resolves as defaults, then the global config file, then environment overrides; project-local <project>/.pi-web/config.json can override upload and attachment defaults and merge allowed paths. [@claim:clm_f998c5bb9928e7ded53452411afad097e2584eec3bed5c2d253048c983e6e9c6]
<!-- rcw:end owner=source:src_68bb307225295cee8b4ab485112cfe7f block=evidence -->

## Researcher notes

