# longngn204/local-coding-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 95144e610ddc @ 0ba6128836bbd797

## Summary (orientation draft, not independently verified)

Local Coding Agent is a local MCP server (v5.0.1) exposing workspace/file/search/command/git/approval tools with a dashboard and Electron tray supervisor, connecting AI coding agents like ChatGPT Web and Claude Code to a local machine. Claims below are drawn only from the supplied README/docs slices; development-practice items are prefixed accordingly. Evidence coverage: 145 of 227 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] An Electron tray app for Windows and macOS acts as a GUI supervisor for the same local server and tunnel, storing secrets with Windows DPAPI or macOS Keychain. -- evidence: [README.md#L245-L246](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L245-L246)
  - [observation/documented] Shipped helper scripts include local-coding-agent.mjs (prompt/setup-wizard/skills doctor), network-doctor.mjs, and support-report.mjs, which writes a redacted support-report.txt without keys or tokens. -- evidence: [README.md#L73-L81](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L73-L81), [README.md#L291-L293](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L291-L293), [README.md#L306-L309](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L306-L309), [README.md#L311-L314](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L311-L314)
- design-choices (2 claim(s)):
  - [observation/documented] Recommended safety defaults are AGENT_MODE=safe, AGENT_POLICY=balanced, and DASHBOARD_PORT=8790; file tools are confined to configured workspace roots and risky actions require local approval under balanced policy. -- evidence: [README.md#L397-L403](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L397-L403), [README.md#L389-L393](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L389-L393)
  - [observation/documented] Since v4.4.3, default tool outputs are kept small (tighter read_file/run_command output, smaller read_many batch caps) to reduce ChatGPT Web lag, with per-call parameters like max_chars and head_lines to raise limits. -- evidence: [README.md#L318-L320](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L318-L320), [README.md#L322-L331](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L322-L331)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: server tests run from the server directory via npm run test:agent, test:pro, test:security, test:hardening, and npm run eval; the tray app builds with dotnet build. -- evidence: [README.md#L434-L437](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L434-L437), [README.md#L423-L430](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L423-L430)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product runs a local MCP server at http://127.0.0.1:8787/mcp, with a /healthz health endpoint and a dashboard at http://127.0.0.1:8790/ui. -- evidence: [README.md#L97-L98](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L97-L98), [README.md#L407-L417](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L407-L417), [README.md#L280-L281](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L280-L281)
  - [observation/documented] The MCP tool surface includes workspace tools (workspace_info, workspace_snapshot, repo_map), file tools (read_file, write_file, apply_patch), search, command execution, git, and approval tools such as request_approval. -- evidence: [README.md#L364-L376](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L364-L376)
- memory-state (1 claim(s)):
  - [observation/documented] compact_context stores a local structured checkpoint (goal, decisions, tasks, git state) under server/data/ with best-effort credential redaction, and resume_context loads it in a fresh chat. -- evidence: [README.md#L356-L360](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L356-L360), [README.md#L342-L347](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L342-L347)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](local-coding-agent.detail.md)

Metadata and full claim list: [full detail](local-coding-agent.detail.md)
Human notes ([notes](local-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
