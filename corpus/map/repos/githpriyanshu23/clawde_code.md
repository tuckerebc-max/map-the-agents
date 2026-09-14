# githpriyanshu23/clawde_code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 00e3585ae83a @ 425f298bc7ee3322

## Summary (orientation draft, not independently verified)

The repository archives the leaked source of Anthropic's Claude Code CLI (TypeScript/Bun, React+Ink), and its README documents the product's architecture, tools, commands, services, and an included MCP server for exploring the source. Evidence is documentation-only; no code slices are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The archived project is Claude Code, a CLI for interacting with Claude from the terminal for software engineering tasks such as editing files, running commands, and searching codebases. -- evidence: [README.md#L19-L19](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L19-L19)
  - [observation/documented] Per the README, the codebase is TypeScript running on Bun with a React+Ink terminal UI, spanning roughly 1,900 files and over 512,000 lines. -- evidence: [README.md#L23-L27](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L23-L27)
- components (2 claim(s)):
  - [observation/documented] The src tree includes a tool registry, command registry, QueryEngine for LLM API calls, cost tracking, and directories for tools, commands, components, services, bridge, coordinator, plugins, skills, and memory. -- evidence: [README.md#L31-L71](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L31-L71)
  - [observation/documented] Documented agent tools include BashTool, file read/write/edit tools, GlobTool, ripgrep-based GrepTool, web fetch/search, AgentTool for sub-agents, MCPTool, LSPTool, and task/team management tools. -- evidence: [README.md#L79-L103](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L79-L103)
- design-choices (2 claim(s)):
  - [observation/documented] Startup is optimized by prefetching MDM settings, keychain reads, and API preconnect in parallel before heavy module evaluation, and heavy modules like OpenTelemetry and gRPC are lazily loaded via dynamic import. -- evidence: [README.md#L227-L227](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L227-L227), [README.md#L217-L217](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L217-L217)
  - [observation/documented] Feature flags via Bun's bundler strip inactive code at build time; notable flags include PROACTIVE, KAIROS, BRIDGE_MODE, DAEMON, VOICE_MODE, AGENT_TRIGGERS, and MONITOR_TOOL. -- evidence: [README.md#L177-L177](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L177-L177), [README.md#L171-L175](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L171-L175), [README.md#L166-L166](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L166-L166)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the README instructs running bash ./gitpretty-apply.sh to apply per-file emoji commit formatting, optionally with --hooks to install hooks for future commits. -- evidence: [README.md#L255-L255](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L255-L255), [README.md#L245-L247](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L245-L247), [README.md#L257-L259](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L257-L259), [README.md#L243-L243](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L243-L243)
  - [observation/documented] Repository development practice: to use the bundled source-explorer MCP server, clone the repo, run npm install && npm run build in mcp-server, then register it with claude mcp add claude-code-explorer. -- evidence: [README.md#L269-L269](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L269-L269), [README.md#L282-L283](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L282-L283), [README.md#L279-L279](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L279-L279)
- skills-patterns (1 claim(s)):
  - [observation/documented] Reusable workflows live in the skills directory and execute through SkillTool, and users can add custom skills. -- evidence: [README.md#L235-L235](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L235-L235)
- interfaces (2 claim(s)):
  - [observation/documented] Users invoke slash commands with a / prefix, including /commit, /review, /compact, /mcp, /doctor, /login, /memory, /resume, and /cost, among about 50 commands. -- evidence: [README.md#L109-L130](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L109-L130), [README.md#L107-L107](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L107-L107)
  - [observation/documented] The bundled MCP server exposes tools such as list_tools, get_tool_source, read_source_file, search_source, and get_architecture, plus prompts like explain_tool and architecture_overview. -- evidence: [README.md#L313-L317](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L313-L317), [README.md#L300-L309](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L300-L309)
- memory-state (1 claim(s)):
More evidence: [full detail](clawde_code.detail.md)

Metadata and full claim list: [full detail](clawde_code.detail.md)
Human notes ([notes](clawde_code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
