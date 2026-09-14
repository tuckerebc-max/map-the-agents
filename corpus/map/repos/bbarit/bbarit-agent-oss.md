# bbarit/bbarit-agent-oss

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2cb8b723f278 @ 193ffd7e172b4267

## Summary (orientation draft, not independently verified)

README, ARCHITECTURE, and CHANGELOG slices describe bbarit-oss, a terminal AI coding agent in Rust with multi-provider LLM support, tools, personas, memory, wiki, and orchestration; contributor workflow details appear in the Contributing and Architecture sections. Evidence coverage: 121 of 124 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] bbarit-oss is a terminal-native AI coding agent CLI that reads, writes, and edits code, runs shell commands, and ships as a single static Rust binary with no runtime to install. -- evidence: [README.md#L120-L125](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L120-L125)
- components (1 claim(s)):
  - [observation/documented] Built-in tools called autonomously in the agent loop include read/write/edit, bash, grep/find/ls/tree, hybrid BM25+semantic code_search, web_search/web_fetch, a task sub-agent spawner, and an opt-in computer tool. -- evidence: [README.md#L312-L320](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L312-L320)
- design-choices (1 claim(s)):
  - [observation/documented] The project is a from-scratch Rust rewrite of Pi (MIT), keeping Pi's small agent-loop philosophy and provider-agnostic registry while adding an orchestrator, wiki, personas, and semantic code search; it reports near-zero source overlap with Pi. -- evidence: [README.md#L612-L612](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L612-L612), [README.md#L24-L81](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L24-L81)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run cargo fmt --all, cargo build, and cargo test; CI runs fmt, build, and tests on Linux and macOS with clippy advisory, and fmt is treated as a hard gate. -- evidence: [README.md#L640-L641](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L640-L641), [README.md#L634-L638](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L634-L638), [ARCHITECTURE.md#L40-L47](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/ARCHITECTURE.md#L40-L47)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent ships 295 curated personas across 30 domains, each a markdown brief at personas/<division>/<id>.md; user-added .md files join the library without code changes, and personas are injected into the system prompt. -- evidence: [README.md#L345-L349](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L345-L349), [README.md#L392-L397](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L392-L397), [README.md#L409-L412](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L409-L412)
- interfaces (2 claim(s)):
  - [observation/documented] Non-interactive modes include --print, where stdout carries only the final answer while narration goes to stderr, and --mode json, which streams newline-delimited JSON events for programmatic consumers. -- evidence: [README.md#L253-L254](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L253-L254), [README.md#L258-L259](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L258-L259)
  - [observation/documented] An /interop toggle (off by default) lets the agent read Claude Code and Codex MCP-server and skill configs as-is, read-only, using only stdio servers and skipping disabled entries. -- evidence: [README.md#L505-L510](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L505-L510), [README.md#L516-L516](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L516-L516), [README.md#L512-L514](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L512-L514), [README.md#L518-L522](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L518-L522)
- memory-state (3 claim(s)):
  - [observation/documented] Auto-memory recalls stored facts at turn start via keyword-overlap scoring without an LLM call, and a background sub-agent extracts durable facts typed as user, feedback, project, or reference after each turn. -- evidence: [README.md#L426-L430](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L426-L430), [README.md#L432-L434](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L432-L434), [README.md#L436-L441](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L436-L441)
More evidence: [full detail](bbarit-agent-oss.detail.md)

Metadata and full claim list: [full detail](bbarit-agent-oss.detail.md)
Human notes ([notes](bbarit-agent-oss.notes.md), never overwritten by build)

[Back to map index](../../index.md)
