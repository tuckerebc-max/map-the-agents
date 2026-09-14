# codebadger (`codebadger`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Lekssays
- License: GPL-3.0
- Language: Python
- Interface: install=Docker (Dockerfile, docker-compose.yml, Dockerfile.mcp) or Python (pyproject.toml, requirements.txt)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry (renamed): original lead [lekssays/codebadger](https://github.com/lekssays/codebadger) (source: backing, field: `source_code_url`) now resolves to [qcri/codebadger](../../repos/qcri/codebadger.md) (github id 1067656065, verified [https://github.com/qcri/codebadger](https://github.com/qcri/codebadger)).

## Description

Highlight (site page `what_makes_it_special`): Bridges Joern Code Property Graphs with LLMs via MCP - enables AI agents to run CPGQL queries, trace data flow/taint, slice programs, and hunt vulnerabilities across 13+ languages. Scales with per-CPG worker pools, memory-aware scheduling, Postgres/Redis backend. Accepted at ICSE 2026 Software Vulnerability Management Workshop.

(captured site page body (agents/codebadger.md), not a verified repo-code finding)
Codebadger, built at QCRI, gives LLM agents structured access to program analysis that plain code reading cannot provide. It constructs Joern Code Property Graphs from a git repository, local path, or pasted snippet, then exposes them over MCP so an external agent can run CPGQL queries, follow data-flow and taint paths, slice programs, and develop vulnerability proofs of concept across 13+ languages including Java, C/C++, Go, and Swift. The service scales through per-CPG worker pools with memory-aware scheduling on a Postgres and Redis backend, and documents an LLM workflow guide plus a security threat model for the analysis pipeline. It is a tools supplier rather than an agent: the repository is explicitly packaged as an MCP server (Dockerfile.mcp), with agents running externally, and it was published at the ICSE 2026 Software Vulnerability Management Workshop.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codebadger.md)
