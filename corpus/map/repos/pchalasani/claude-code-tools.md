# pchalasani/claude-code-tools

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ee0f3099c05c @ 97d770c6b369880b

## Summary (orientation draft, not independently verified)

The repository ships CLI tools, skills, agents, hooks, and plugins for Claude Code and similar coding agents; the best-documented products are agent-tunnel (Discord-based sharing of local Claude sessions) and find-claude-session (keyword search over session JSONL files), plus a Zsh setup guide. Evidence coverage: 142 of 182 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project provides CLI tools, skills, agents, hooks, and plugins intended to enhance productivity with Claude Code and other coding agents. -- evidence: [README.md#L8-L8](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/README.md#L8-L8)
- components (4 claim(s)):
  - [observation/documented] The >share hook (hooks/share_hook.py) is a standalone stdlib UserPromptSubmit hook that reads session_id/cwd/transcript_path from stdin, writes an fcntl-locked atomic registry, and blocks the prompt to print the handle. -- evidence: [docs/agent-tunnel-spec.md#L64-L69](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L64-L69)
  - [observation/documented] Inbound attachments are downloaded to a per-thread uploads dir outside any repo and exposed to the fork via --add-dir, with per-file size and count caps; oversized or excess files are skipped with a notice. -- evidence: [docs/agent-tunnel-spec.md#L188-L196](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L188-L196)
- design-choices (2 claim(s)):
  - [observation/documented] Threads answer via --resume with --fork-session so the original session is untouched; remote turns run with --allowedTools Read,Grep,Glob, an explicit deny list, and --permission-mode dontAsk. -- evidence: [docs/agent-tunnel-spec.md#L19-L40](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L19-L40)
  - [observation/documented] agent-tunnel uses no inbound tunnel: it connects via the Discord Gateway's outbound websocket, so nothing on the machine is internet-reachable. -- evidence: [docs/agent-tunnel-spec.md#L19-L40](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L19-L40)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the agent-tunnel spec reports unit tests using real files without mocks, covering the registry, hook, store, session discovery, flag building, config, and attachment handling. -- evidence: [docs/agent-tunnel-spec.md#L281-L294](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L281-L294)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] agent-tunnel exposes long-lived local Claude Code sessions ('experts') to teammates over Discord; a session is published at runtime with >share and addressed by a short handle, with each conversation answered against a read-only fork. -- evidence: [docs/agent-tunnel-spec.md#L3-L7](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L3-L7)
  - [observation/documented] In a watched channel, '<handle> [question]' opens a Discord thread bound to that session with follow-ups staying in the thread; !list/!handles list active handles; !done/!close/!end tear down the fork immediately. -- evidence: [docs/agent-tunnel-spec.md#L168-L181](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L168-L181)
- memory-state (1 claim(s)):
  - [observation/documented] The config dir is propagated end to end: the hook derives it from transcript_path and records it in the registry, and the daemon pins each fork via CLAUDE_CONFIG_DIR so work and personal sessions fork under their own config/account. -- evidence: [docs/agent-tunnel-spec.md#L226-L231](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L226-L231), [docs/agent-tunnel-spec.md#L221-L224](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L221-L224)
- orchestration (1 claim(s)):
More evidence: [full detail](claude-code-tools.detail.md)

Metadata and full claim list: [full detail](claude-code-tools.detail.md)
Human notes ([notes](claude-code-tools.notes.md), never overwritten by build)

[Back to map index](../../index.md)
