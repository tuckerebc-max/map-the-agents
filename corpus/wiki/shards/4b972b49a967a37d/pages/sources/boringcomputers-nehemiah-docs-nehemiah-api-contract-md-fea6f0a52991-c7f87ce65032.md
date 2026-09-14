---
access: public
aliases: []
claim_ids:
- clm_616922b72dacd88ed2014b9ecf1c50ce4239a640098c3e2837e8098b0eb00d73
- clm_6b0e262d57faa44b56d27264b0a2bbe7ef8c715c3f5fcd150ed319347f33d110
- clm_8ce63f73fc921269d564c3fb8a18964c6ca7e74625abbc3e7eb1671dd9146aaa
- clm_d3919cbdc044126fbc9daea90f000aa2f1855cd501eefc732da80825d116b3a4
maturity: draft
page_id: pg_653b9df7764a5bddbb5fc7f87ce65032
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3f90deb4003b5c8e84e129b05844b381
title: boringcomputers/nehemiah/docs/nehemiah/api-contract.md @ fea6f0a52991
updated_at: '2026-09-14T03:39:33Z'
---

# boringcomputers/nehemiah/docs/nehemiah/api-contract.md @ fea6f0a52991

<!-- rcw:begin owner=source:src_3f90deb4003b5c8e84e129b05844b381 block=evidence -->
- Repository development practice: contributors use npm workspaces commands (npm run dev/build/check/lint) and are pointed to CONTRIBUTING.md; a route-inventory test fails if the exported OpenAPI contract drifts. [@claim:clm_616922b72dacd88ed2014b9ecf1c50ce4239a640098c3e2837e8098b0eb00d73]
- Managed OCI image import/pull is not implemented: requests receive a typed 501 not_supported response, and the field is documented only as a deprecated reserved field. [@claim:clm_6b0e262d57faa44b56d27264b0a2bbe7ef8c715c3f5fcd150ed319347f33d110]
- Managed host-local LLM agents are not implemented; agent-capability session issuance fails with typed not_supported, and users are directed to run agents inside the guest via exec/TTY/file primitives. [@claim:clm_8ce63f73fc921269d564c3fb8a18964c6ca7e74625abbc3e7eb1671dd9146aaa]
- File access uses capability-scoped session tokens sent only as bearer headers; query tokens, cookies, and redirects are forbidden, uploads are capped at 16 MiB, and sessions can be revoked with a typed DELETE endpoint. [@claim:clm_d3919cbdc044126fbc9daea90f000aa2f1855cd501eefc732da80825d116b3a4]
<!-- rcw:end owner=source:src_3f90deb4003b5c8e84e129b05844b381 block=evidence -->

## Researcher notes

