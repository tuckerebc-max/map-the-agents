# the-open-agent/openagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b98d42165dc0 @ 7c6747567e0868ba

## Summary (orientation draft, not independently verified)

OpenAgent is described as an open-source, self-hostable personal AI assistant combining LLMs, a personal knowledge base, and autonomous agent loops, shipped as a single binary with a web interface on port 14000; pre-built binaries cover Linux, macOS, and Windows (natively). The agent loop reportedly supports browser automation, web search, shell execution, Office file read/write, and MCP tool servers; a RAG subsystem ingests documents; workflow automation offers a BPMN-style visual builder; platform features include SSO, multi-tenant workspaces, a REST API, and an admin dashboard. CLAUDE.md/CONTRIBUTING.md describe repository development practice (Beego/xorm backend, prerequisites). The playground demo resets every 5 minutes. Evidence: 6 of 6 candidate files stored; selection complete.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] OpenAgent is described as an open-source, self-hostable personal AI assistant combining LLMs, a personal knowledge base, and autonomous agent loops, shipped as a single binary requiring no installation. -- evidence: [README.md#L8-L8](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L8-L8), [README.md#L35-L35](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L35-L35)
  - [observation/documented] Pre-built binaries are offered for Linux, macOS, and Windows on x86_64 and arm64, with Windows running natively without WSL or Docker; install scripts download the latest release and start the service. -- evidence: [README.md#L160-L168](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L160-L168), [README.md#L80-L80](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L80-L80), [README.md#L68-L68](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L68-L68)
- components (4 claim(s)):
  - [observation/documented] The agent loop reportedly supports browser automation (navigate, click, fill forms, scrape, screenshot), web search and page fetching, shell command execution, Office file read/write, and integration of MCP-compatible servers over SSE, Stdio, or StreamableHTTP, with tool invocations shown transparently. -- evidence: [README.md#L125-L132](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L125-L132)
  - [observation/documented] The RAG subsystem ingests documents (PDF, Word, Excel) with automatic chunking, embedding, and indexing, performs semantic retrieval before each LLM response, supports pluggable embedding providers, and organizes knowledge into isolated stores assignable per chat or application. -- evidence: [README.md#L138-L143](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/README.md#L138-L143)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs contributors to build with go build, run tests via go test ./..., and develop the React frontend with yarn install/start/lint:js; a full production build via build.sh cross-compiles for linux/amd64, arm64, and riscv64. -- evidence: [CLAUDE.md#L15-L21](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L15-L21), [CLAUDE.md#L7-L13](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L7-L13), [CLAUDE.md#L23-L23](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L23-L23)
  - [observation/documented] Repository development practice: CLAUDE.md documents a Beego MVC backend where each entity follows a three-layer pattern (object structs with xorm tags, controllers wired to routes in routers/router.go, and auto-migration via engine.Sync2 in object/adapter.go), with composite primary keys of (Owner, Name). -- evidence: [CLAUDE.md#L35-L35](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L35-L35), [CLAUDE.md#L33-L33](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L33-L33), [CLAUDE.md#L41-L41](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L41-L41), [CLAUDE.md#L39-L39](https://github.com/the-open-agent/openagent/blob/b98d42165dc00860449a6894021e5f1f97762837/CLAUDE.md#L39-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
More evidence: [full detail](openagent.detail.md)

Metadata and full claim list: [full detail](openagent.detail.md)
Human notes ([notes](openagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
