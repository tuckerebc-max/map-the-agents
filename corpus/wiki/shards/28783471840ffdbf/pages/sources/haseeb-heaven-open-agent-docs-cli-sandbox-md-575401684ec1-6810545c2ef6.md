---
access: public
aliases: []
claim_ids:
- clm_034d9f2726efc55bc1b8b61472a3cb2c4b7435cc0dfe0a13f07f8007aa7ee584
- clm_12f396a2de65bc00993fb3d150ecdedf95e292e3d7a7cb8b6e2271714a11f29e
- clm_6327d588d85fdc9505c10bace3cd7ec0cf7d455216763f2c08866c280019c36c
- clm_a56667b19e5ead01debe255e8bcd864f3c171dc0425718866fee2fc03234d132
- clm_e193c63cea3e784214f330ee56e1ac19e4f123666a3daa67cb426fad634255e1
maturity: draft
page_id: pg_fdc8eb4cef245cb8a7246810545c2ef6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5360577a2fd551438291830585c626a4
title: haseeb-heaven/open-agent/docs/cli/sandbox.md @ 575401684ec1
updated_at: '2026-09-14T03:56:06Z'
---

# haseeb-heaven/open-agent/docs/cli/sandbox.md @ 575401684ec1

<!-- rcw:begin owner=source:src_5360577a2fd551438291830585c626a4 block=evidence -->
- A 'Sandbox Expansion Request' mechanism lets the agent ask for extra permissions (directories, network) when a sandboxed command is denied or proactively flagged, executed only after user approval for that run. [@claim:clm_034d9f2726efc55bc1b8b61472a3cb2c4b7435cc0dfe0a13f07f8007aa7ee584]
- The docs note sandboxing reduces but does not eliminate risk, and GUI applications may not work inside sandboxes. [@claim:clm_12f396a2de65bc00993fb3d150ecdedf95e292e3d7a7cb8b6e2271714a11f29e]
- macOS Seatbelt sandboxing offers profiles (permissive-open default, permissive-proxied, restrictive-*, strict-*) selected via the SEATBELT_PROFILE env var, controlling write and network restrictions. [@claim:clm_6327d588d85fdc9505c10bace3cd7ec0cf7d455216763f2c08866c280019c36c]
- LXC/LXD sandboxing is Linux-only and experimental: the container must already exist and be running before starting open-agent, which does not create it automatically, and the workspace must be writable at the same absolute path inside the container. [@claim:clm_a56667b19e5ead01debe255e8bcd864f3c171dc0425718866fee2fc03234d132]
- Sandboxing can be enabled via the -s/--sandbox flag, the OPENAGENT_SANDBOX env var (docker, podman, sandbox-exec, runsc, lxc, with legacy GEMINI_SANDBOX alias), or settings.json, in that precedence order. [@claim:clm_e193c63cea3e784214f330ee56e1ac19e4f123666a3daa67cb426fad634255e1]
<!-- rcw:end owner=source:src_5360577a2fd551438291830585c626a4 block=evidence -->

## Researcher notes

