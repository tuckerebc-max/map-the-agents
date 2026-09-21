# andrefetch/postal

Status: distilled - Freshness: stale
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4d9bf7122135 @ d6dfb027204c94e6

## Summary (orientation draft, not independently verified)

Postal is an open-source terminal-based AI coding agent (Python, distributed as postalcli on PyPI) that connects to LLMs via OpenRouter, provides built-in file/bash/network/memory tools, sub-agents, MCP support, six approval policies, and checkpointed resumable sessions. Evidence is documentation-only; no code slices are present, so all claims are documented rather than code-inspected.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Postal is an open-source AI coding agent that runs in the terminal, planning, editing, running, and reviewing code with any model available on OpenRouter. -- evidence: [README.md#L5-L8](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L5-L8)
- components (2 claim(s)):
  - [observation/documented] Built-in tools include file operations (read, write, edit, apply_patch, grep, glob, list_directories), bash, a plan todo-list tool, DuckDuckGo-backed web search, URL fetching, and cross-session key-value memory. -- evidence: [docs/tools.md#L27-L27](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L27-L27), [docs/tools.md#L38-L38](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L38-L38), [docs/tools.md#L23-L23](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L23-L23), [docs/tools.md#L9-L17](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L9-L17), [docs/tools.md#L31-L34](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L31-L34), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96)
  - [observation/documented] The main agent can delegate to five specialized sub-agents (codebase_investigator, code_reviewer, software_architect, test_writer, debugger), each running its own loop with a narrowed tool set and turn cap; sub-agent runs are never checkpointed. -- evidence: [docs/tools.md#L44-L50](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L44-L50), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96), [docs/tools.md#L42-L42](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L42-L42)
- design-choices (1 claim(s)):
  - [observation/documented] Context handling uses two loop-side mechanisms: pruning clears stale tool outputs to reclaim tokens, and compaction summarizes history into a continuation brief when the context window fills, instead of erroring out. -- evidence: [README.md#L77-L82](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L77-L82), [docs/tools.md#L62-L62](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L62-L62), [docs/tools.md#L64-L65](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L64-L65)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcomed in any size and prospective contributors are directed to CONTRIBUTING.md and the open issue tracker to get started. -- evidence: [README.md#L185-L185](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L185-L185)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI offers single-shot mode via a prompt argument, --cwd to target another directory, --continue/--resume for sessions, and a sessions subcommand; the interactive mode is a full-screen TUI. -- evidence: [README.md#L50-L56](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L50-L56), [README.md#L42-L46](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L42-L46), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96)
  - [observation/documented] The TUI supports slash commands including /model, /approval, /thinking, /clear, /stats, /tools, /mcp, /sessions, /resume, /checkpoint, /rewind and /exit, with autocomplete as the user types. -- evidence: [README.md#L119-L119](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L119-L119), [README.md#L100-L117](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L100-L117)
- memory-state (2 claim(s)):
  - [observation/documented] Conversations are checkpointed to disk after every turn under ~/.config/postal/sessions/<id>/ as JSONL transcripts plus meta.json; /rewind restores a checkpoint's conversation but does not revert files already written to disk. -- evidence: [README.md#L154-L154](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L154-L154), [README.md#L123-L123](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L123-L123), [README.md#L152-L152](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L152-L152)
  - [observation/documented] Resuming a session rebuilds the system prompt from current config and tool set rather than restoring it, so resumed sessions pick up later model, approval, or AGENTS.md changes. -- evidence: [README.md#L133-L133](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L133-L133)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
More evidence: [full detail](postal.detail.md)

Metadata and full claim list: [full detail](postal.detail.md)
Human notes ([notes](postal.notes.md), never overwritten by build)

[Back to map index](../../index.md)
