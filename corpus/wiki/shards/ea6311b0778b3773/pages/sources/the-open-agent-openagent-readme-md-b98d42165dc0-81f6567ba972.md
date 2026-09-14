---
access: public
aliases: []
claim_ids:
- clm_131607886b3625a03f1be11b4c1d1faca33577a4a365bd1f0983c3d7f910b7b9
- clm_182a2ae04b0de33304a19aae0db1f6386069d4e6953d816cf20ab18104cd1a64
- clm_265aa4d02c5edc4ed29d2136b182f594016a7610a171fc176789fc172d38b4ab
- clm_26af758ee0ee71e01a643332a8ced3b2ef470b4f46e7e30176463a18c7e1f22f
- clm_37dd08d86928818507680ad93d835a3f8ad061f8ee4203b5eea1d9b7aadbe7c5
- clm_69b387220be6c37890d17ec1ee985f761ed2aefa866fdd9dad23389e2d3bf404
- clm_c9d99a561458afb32f7428188078aa62fbde6abbeadee685f72836c63f735655
- clm_d60e3c97f5cb0586bf89a97feb5bd4cc9386ac1a0f8e2deda19e6e368548d2ac
- clm_d91512226e08146d81a40d4bfdda24a6961447c89bf66d5fd15f774ff7b51a4d
- clm_e9fe6e8683a14c4511ea4323f6beaa00f4a7362b567913ac048eea3bceed7fb9
maturity: draft
page_id: pg_58de90d2a5ca5e07a9d581f6567ba972
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_43a36c78836e5a5ba72d925c2518d313
title: the-open-agent/openagent/README.md @ b98d42165dc0
updated_at: '2026-09-14T03:19:07Z'
---

# the-open-agent/openagent/README.md @ b98d42165dc0

<!-- rcw:begin owner=source:src_43a36c78836e5a5ba72d925c2518d313 block=evidence -->
- An admin dashboard provides usage statistics with charts and heatmaps, real-time activity monitoring with success/error rates, centralized CRUD tool management, and full request/response logs with filtering. [@claim:clm_131607886b3625a03f1be11b4c1d1faca33577a4a365bd1f0983c3d7f910b7b9]
- Platform features include single sign-on via OIDC/OAuth2/LDAP/SAML, multi-tenant isolated workspaces, a REST API with Swagger UI, audit logs, and built-in file/media storage. [@claim:clm_182a2ae04b0de33304a19aae0db1f6386069d4e6953d816cf20ab18104cd1a64]
- Repository development practice: contributors are asked to open an issue before larger changes, and security vulnerabilities must not be reported through public GitHub issues but emailed to admin@openagentai.org. [@claim:clm_265aa4d02c5edc4ed29d2136b182f594016a7610a171fc176789fc172d38b4ab]
- The RAG subsystem ingests documents (PDF, Word, Excel) with automatic chunking, embedding, and indexing, performs semantic retrieval before each LLM response, supports pluggable embedding providers, and organizes knowledge into isolated stores assignable per chat or application. [@claim:clm_26af758ee0ee71e01a643332a8ced3b2ef470b4f46e7e30176463a18c7e1f22f]
- Pre-built binaries are offered for Linux, macOS, and Windows on x86_64 and arm64, with Windows running natively without WSL or Docker; install scripts download the latest release and start the service. [@claim:clm_37dd08d86928818507680ad93d835a3f8ad061f8ee4203b5eea1d9b7aadbe7c5]
- The agent loop reportedly supports browser automation (navigate, click, fill forms, scrape, screenshot), web search and page fetching, shell command execution, Office file read/write, and integration of MCP-compatible servers over SSE, Stdio, or StreamableHTTP, with tool invocations shown transparently. [@claim:clm_69b387220be6c37890d17ec1ee985f761ed2aefa866fdd9dad23389e2d3bf404]
- A workflow automation feature set includes a BPMN-style drag-and-drop visual builder, conditional gateway branching with parallel execution, recurring task scheduling, and per-provider/model/user token and cost analytics. [@claim:clm_c9d99a561458afb32f7428188078aa62fbde6abbeadee685f72836c63f735655]
- The product runs a web interface on port 14000; after installation or starting containers, users access it at http://localhost:14000. [@claim:clm_d60e3c97f5cb0586bf89a97feb5bd4cc9386ac1a0f8e2deda19e6e368548d2ac]
- The playground demo environment resets all data every 5 minutes, so any changes made there are not persistent; the live preview is read-only. [@claim:clm_d91512226e08146d81a40d4bfdda24a6961447c89bf66d5fd15f774ff7b51a4d]
- OpenAgent is described as an open-source, self-hostable personal AI assistant combining LLMs, a personal knowledge base, and autonomous agent loops, shipped as a single binary requiring no installation. [@claim:clm_e9fe6e8683a14c4511ea4323f6beaa00f4a7362b567913ac048eea3bceed7fb9]
<!-- rcw:end owner=source:src_43a36c78836e5a5ba72d925c2518d313 block=evidence -->

## Researcher notes

