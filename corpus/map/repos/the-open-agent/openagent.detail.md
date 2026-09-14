# the-open-agent/openagent -- full detail

[Back to orientation](openagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/the-open-agent/openagent/b98d42165dc00860449a6894021e5f1f97762837/7c6747567e0868ba.json](../../../wiki/dossiers/the-open-agent/openagent/b98d42165dc00860449a6894021e5f1f97762837/7c6747567e0868ba.json)

## specifications (2 claim(s))

- [observation/documented] OpenAgent is described as an open-source, self-hostable personal AI assistant combining LLMs, a personal knowledge base, and autonomous agent loops, shipped as a single binary requiring no installation. -- evidence: [README.md#L8-L8](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L8-L8), [README.md#L35-L35](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L35-L35) (`clm_e9fe6e8683a14c4511ea4323f6beaa00f4a7362b567913ac048eea3bceed7fb9`)
- [observation/documented] Pre-built binaries are offered for Linux, macOS, and Windows on x86_64 and arm64, with Windows running natively without WSL or Docker; install scripts download the latest release and start the service. -- evidence: [README.md#L160-L168](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L160-L168), [README.md#L80-L80](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L80-L80), [README.md#L68-L68](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L68-L68) (`clm_37dd08d86928818507680ad93d835a3f8ad061f8ee4203b5eea1d9b7aadbe7c5`)

## components (4 claim(s))

- [observation/documented] The agent loop reportedly supports browser automation (navigate, click, fill forms, scrape, screenshot), web search and page fetching, shell command execution, Office file read/write, and integration of MCP-compatible servers over SSE, Stdio, or StreamableHTTP, with tool invocations shown transparently. -- evidence: [README.md#L125-L132](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L125-L132) (`clm_69b387220be6c37890d17ec1ee985f761ed2aefa866fdd9dad23389e2d3bf404`)
- [observation/documented] The RAG subsystem ingests documents (PDF, Word, Excel) with automatic chunking, embedding, and indexing, performs semantic retrieval before each LLM response, supports pluggable embedding providers, and organizes knowledge into isolated stores assignable per chat or application. -- evidence: [README.md#L138-L143](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L138-L143) (`clm_26af758ee0ee71e01a643332a8ced3b2ef470b4f46e7e30176463a18c7e1f22f`)
- [observation/documented] A workflow automation feature set includes a BPMN-style drag-and-drop visual builder, conditional gateway branching with parallel execution, recurring task scheduling, and per-provider/model/user token and cost analytics. -- evidence: [README.md#L149-L154](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L149-L154) (`clm_c9d99a561458afb32f7428188078aa62fbde6abbeadee685f72836c63f735655`)
- [observation/documented] An admin dashboard provides usage statistics with charts and heatmaps, real-time activity monitoring with success/error rates, centralized CRUD tool management, and full request/response logs with filtering. -- evidence: [README.md#L174-L179](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L174-L179) (`clm_131607886b3625a03f1be11b4c1d1faca33577a4a365bd1f0983c3d7f910b7b9`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs contributors to build with go build, run tests via go test ./..., and develop the React frontend with yarn install/start/lint:js; a full production build via build.sh cross-compiles for linux/amd64, arm64, and riscv64. -- evidence: [CLAUDE.md#L15-L21](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L15-L21), [CLAUDE.md#L7-L13](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L7-L13), [CLAUDE.md#L23-L23](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L23-L23) (`clm_a3da54a361ea3be8ab1d570c303d765d075c1e3a686c8171f5fdd083ee7dfe9d`)
- [observation/documented] Repository development practice: CLAUDE.md documents a Beego MVC backend where each entity follows a three-layer pattern (object structs with xorm tags, controllers wired to routes in routers/router.go, and auto-migration via engine.Sync2 in object/adapter.go), with composite primary keys of (Owner, Name). -- evidence: [CLAUDE.md#L35-L35](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L35-L35), [CLAUDE.md#L33-L33](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L33-L33), [CLAUDE.md#L41-L41](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L41-L41), [CLAUDE.md#L39-L39](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L39-L39) (`clm_07d3b1438fd274ec16ef003070b0dbae2d0de9a737afed50666127426d2c7a8d`)
- [observation/documented] Repository development practice: contributors are asked to open an issue before larger changes, and security vulnerabilities must not be reported through public GitHub issues but emailed to admin@openagentai.org. -- evidence: [SECURITY.md#L9-L9](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/SECURITY.md#L9-L9), [README.md#L200-L201](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L200-L201), [SECURITY.md#L7-L7](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/SECURITY.md#L7-L7) (`clm_265aa4d02c5edc4ed29d2136b182f594016a7610a171fc176789fc172d38b4ab`)
- [observation/documented] Repository development practice: CONTRIBUTING.md lists prerequisites of Go 1.23.6+, Node.js 20+, Yarn 1.x, MySQL 8.0+ or MariaDB, and an auth service, with setup by copying conf/app.conf.example to conf/app.conf and editing DB and auth settings. -- evidence: [CONTRIBUTING.md#L31-L35](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CONTRIBUTING.md#L31-L35), [CONTRIBUTING.md#L21-L27](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CONTRIBUTING.md#L21-L27) (`clm_92228de0648ba92032b473cb3b8f0dda2040f31e348f2869c4f434f718aca5f0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product runs a web interface on port 14000; after installation or starting containers, users access it at http://localhost:14000. -- evidence: [README.md#L105-L105](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L105-L105), [README.md#L68-L68](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L68-L68), [README.md#L82-L82](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L82-L82) (`clm_d60e3c97f5cb0586bf89a97feb5bd4cc9386ac1a0f8e2deda19e6e368548d2ac`)
- [observation/documented] Platform features include single sign-on via OIDC/OAuth2/LDAP/SAML, multi-tenant isolated workspaces, a REST API with Swagger UI, audit logs, and built-in file/media storage. -- evidence: [README.md#L160-L168](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L160-L168) (`clm_182a2ae04b0de33304a19aae0db1f6386069d4e6953d816cf20ab18104cd1a64`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] The playground demo environment resets all data every 5 minutes, so any changes made there are not persistent; the live preview is read-only. -- evidence: [README.md#L185-L188](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L185-L188) (`clm_d91512226e08146d81a40d4bfdda24a6961447c89bf66d5fd15f774ff7b51a4d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

