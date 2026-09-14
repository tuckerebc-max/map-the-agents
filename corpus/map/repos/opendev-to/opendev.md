# opendev-to/opendev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d32c660e4eed @ 6c2de2a3889db931

## Summary (orientation draft, not independently verified)

OpenDev is a Rust-based open-source terminal coding agent that binds multiple LLM providers to five workflow slots and supports parallel/background sub-agents, teams, mailboxes, and git-worktree isolation. Evidence is mostly README and an adaptation design document; no source code slices are present. Evidence coverage: 158 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] OpenDev is described as an open-source, terminal-native coding agent built as a compound AI system of agents and workflows, each independently bound to a user-configured model. -- evidence: [README.md#L29-L29](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L29-L29)
  - [observation/documented] Five workflow slots are defined: Normal (execution), Thinking (reasoning), Compact (context summarization), Critique (self-critique), and VLM (vision), each bindable to any configured LLM. -- evidence: [README.md#L224-L228](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L224-L228), [README.md#L33-L33](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L33-L33)
- components (3 claim(s)):
  - [observation/documented] The design doc specifies a TaskManager in opendev-runtime: a UI-agnostic task lifecycle state machine with idempotent transitions, a notified flag, 5-second eviction grace, and retain-to-block-eviction. -- evidence: [docs/agent-framework-adaptation.md#L44-L44](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L44-L44), [docs/agent-framework-adaptation.md#L48-L52](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L48-L52)
  - [observation/documented] A file-based mailbox system gives each agent an inbox with fd-lock protocol, corruption recovery via rename, a 1000-entry cap, and message types including Text, ShutdownRequest, ShutdownResponse, and Idle. -- evidence: [docs/agent-framework-adaptation.md#L156-L162](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L156-L162), [docs/agent-framework-adaptation.md#L152-L152](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L152-L152), [docs/agent-framework-adaptation.md#L164-L164](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L164-L164)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors build with `cargo build --workspace`, run `cargo test --workspace`, and use cargo check, clippy, and fmt; the Web UI frontend is built with `npm ci && npm run build`. -- evidence: [README.md#L277-L279](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L277-L279), [README.md#L257-L262](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L257-L262), [README.md#L264-L269](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L264-L269)
  - [observation/documented] Repository development practice: contributors are asked to open an issue or submit a pull request, and a ROADMAP.md lists priorities for community contributions. -- evidence: [README.md#L285-L285](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L285-L285), [README.md#L283-L283](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L283-L283)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI offers an interactive TUI (`opendev`), a Web UI (`opendev run ui`), single-prompt mode (`-p`), session resume (`--continue`), and an interactive `opendev config setup` for provider/model binding. -- evidence: [README.md#L210-L210](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L210-L210), [README.md#L198-L198](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L198-L198), [README.md#L204-L204](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L204-L204), [README.md#L207-L208](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L207-L208), [README.md#L201-L201](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L201-L201)
  - [observation/documented] MCP integration provides dynamic tool discovery with subcommands such as `opendev mcp list`, `mcp add`, and `mcp enable/disable`. -- evidence: [README.md#L249-L253](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L249-L253), [README.md#L247-L247](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L247-L247)
- memory-state (1 claim(s)):
  - [observation/documented] Per-agent sidechain transcripts are stored as append-only JSONL at `~/.opendev/sessions/{session_id}/agents/{agent_id}.jsonl`, with readers that filter malformed lines and orphaned tool calls for resume. -- evidence: [docs/agent-framework-adaptation.md#L73-L73](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L73-L73), [docs/agent-framework-adaptation.md#L62-L62](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L62-L62), [docs/agent-framework-adaptation.md#L66-L71](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L66-L71)
- orchestration (2 claim(s)):
More evidence: [full detail](opendev.detail.md)

Metadata and full claim list: [full detail](opendev.detail.md)
Human notes ([notes](opendev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
