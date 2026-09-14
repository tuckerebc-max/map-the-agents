---
access: public
aliases: []
claim_ids:
- clm_36e37e49562b2b017ce12be1619d556474c724bd230b1c52a17f99bd2a1ada70
- clm_616922b72dacd88ed2014b9ecf1c50ce4239a640098c3e2837e8098b0eb00d73
- clm_7170227d3bda5cb1fdc4dc7708451a7879aa84ad27d64922ec960c1d430e7bfa
- clm_7c6e2a602675cae366b0be89cf922f8135be106869c65a19921311896fa5adf1
maturity: draft
page_id: pg_85b9751b17865fd0aa468a9825812a31
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_98ba94c2a3d259a7b62a3161e96047a2
title: boringcomputers/nehemiah/README.md @ fea6f0a52991
updated_at: '2026-09-14T03:39:33Z'
---

# boringcomputers/nehemiah/README.md @ fea6f0a52991

<!-- rcw:begin owner=source:src_98ba94c2a3d259a7b62a3161e96047a2 block=evidence -->
- Each machine is a hardware-virtualized Firecracker microVM with its own kernel, jailed and resource-capped, restored from a memory snapshot in milliseconds, with guests network-isolated behind an egress firewall. [@claim:clm_36e37e49562b2b017ce12be1619d556474c724bd230b1c52a17f99bd2a1ada70]
- Repository development practice: contributors use npm workspaces commands (npm run dev/build/check/lint) and are pointed to CONTRIBUTING.md; a route-inventory test fails if the exported OpenAPI contract drifts. [@claim:clm_616922b72dacd88ed2014b9ecf1c50ce4239a640098c3e2837e8098b0eb00d73]
- An MCP server package (nehemiah-mcp) lets clients like Claude Desktop and Cursor spin up and drive Nehemiah computers as a tool, configured via npx with a NEHEMIAH_URL env var. [@claim:clm_7170227d3bda5cb1fdc4dc7708451a7879aa84ad27d64922ec960c1d430e7bfa]
- The repo is a Turborepo/npm-workspaces monorepo: apps/web (SvelteKit site), nehemiahd (Go host daemon), packages/sdk (Effect-native TypeScript client), packages/mcp, and infra/latitude provisioning. [@claim:clm_7c6e2a602675cae366b0be89cf922f8135be106869c65a19921311896fa5adf1]
<!-- rcw:end owner=source:src_98ba94c2a3d259a7b62a3161e96047a2 block=evidence -->

## Researcher notes

