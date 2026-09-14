---
access: public
aliases: []
claim_ids:
- clm_1589f315b690b13265b2e92e0b57bae1bc305df92dc0668dd4d97ae6e326e6e3
- clm_8967c45b5d29a110cdac6308247608e5f58ccb0c57c0ee54df69052f026a0011
- clm_a4d9cf321f8ecae1861ede17de1fd1a7e7553eb219d6e9ed4c289cf1f66d1714
- clm_d530a1f25c83e05f228999bdb8b54f6c8ade851927ab79df85ac03529400b050
- clm_d60f58ee64c1335c77a3db2cdbda825769fcaafa33eba90b80c6f1faa15a259c
- clm_fa44460aebcf86a4b35d21cf46d876604f4f4c08595a17520f18b6c93974cb11
maturity: draft
page_id: pg_b70b1d6964ee5ff3a4ae17fe42322995
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_83dceec3784052a09cea4752da3be4fa
title: jmfederico/pi-web/README.md @ 46579c049a30
updated_at: '2026-09-14T02:08:25Z'
---

# jmfederico/pi-web/README.md @ 46579c049a30

<!-- rcw:begin owner=source:src_83dceec3784052a09cea4752da3be4fa block=evidence -->
- The product organizes work hierarchically: a machine is a runtime endpoint, a project is a folder on it, a workspace is a provider-owned working folder, and a session is a Pi Coding Agent chat inside a workspace. [@claim:clm_1589f315b690b13265b2e92e0b57bae1bc305df92dc0668dd4d97ae6e326e6e3]
- Running PI WEB requires Node.js 22.19.0 or newer, npm, a Pi Coding Agent of at least version 0.84.0, and git plus the development tools agents need. [@claim:clm_8967c45b5d29a110cdac6308247608e5f58ccb0c57c0ee54df69052f026a0011]
- Installation uses npm with the scoped --allow-scripts=node-pty flag so node-pty can build its native module without enabling install scripts for other packages. [@claim:clm_a4d9cf321f8ecae1861ede17de1fd1a7e7553eb219d6e9ed4c289cf1f66d1714]
- The security model assumes trusted users, repositories, and server paths; the product is explicitly not a sandbox, permission system, or multi-tenant platform and should not be exposed directly to the public internet. [@claim:clm_d530a1f25c83e05f228999bdb8b54f6c8ade851927ab79df85ac03529400b050]
- Sessions are designed to survive browser disconnects, letting users supervise agents from any browser while work continues on the host machine. [@claim:clm_d60f58ee64c1335c77a3db2cdbda825769fcaafa33eba90b80c6f1faa15a259c]
- PI WEB can register other PI WEB runtimes as remote machines, with one browser-facing instance proxying projects, files, git state, sessions, terminals, and Pi package management from trusted remote machines. [@claim:clm_fa44460aebcf86a4b35d21cf46d876604f4f4c08595a17520f18b6c93974cb11]
<!-- rcw:end owner=source:src_83dceec3784052a09cea4752da3be4fa block=evidence -->

## Researcher notes

