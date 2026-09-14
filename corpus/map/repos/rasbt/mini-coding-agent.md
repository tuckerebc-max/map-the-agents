# rasbt/mini-coding-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 717cae4ff10d @ c0f5070d67f9fc18

## Summary (orientation draft, not independently verified)

The evidence consists of README.md documentation for a small standalone coding agent built on Ollama, describing its agent loop, CLI, approval modes, session persistence, and design choices. All product claims below are documented in the README; no source code slices were provided.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The agent is described as a minimal local agent loop with workspace snapshot collection, stable prompt plus turn state, structured tools, approval handling for risky tools, transcript/memory persistence, and bounded delegation. -- evidence: [README.md#L9-L9](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L9-L9), [README.md#L11-L16](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L11-L16)
- design-choices (3 claim(s)):
  - [observation/documented] The agent expects the model to emit either <tool>...</tool> or <final>...</final>, and notes that different Ollama models follow this format with varying reliability. -- evidence: [README.md#L249-L252](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L249-L252)
  - [observation/documented] The design uses a stable prompt prefix separate from the changing request, transcript, and memory, so repeated model calls can reuse the static parts efficiently. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The agent exposes a CLI with flags including --cwd, --model, --host, --ollama-timeout, --resume, --approval, --max-steps, --max-new-tokens, --temperature, and --top-p, with documented defaults such as max-steps 6 and max-new-tokens 512. -- evidence: [README.md#L220-L239](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L220-L239)
  - [observation/documented] Inside the REPL, slash commands (/help, /memory, /session, /reset, /exit, /quit) are handled directly by the agent rather than sent to the model as tasks. -- evidence: [README.md#L189-L200](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L189-L200), [README.md#L186-L187](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L186-L187)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions are saved under the target workspace root in .mini-coding-agent/sessions/, and can be resumed by id or with --resume latest. -- evidence: [README.md#L165-L167](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L165-L167), [README.md#L178-L180](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L178-L180), [README.md#L163-L163](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L163-L163), [README.md#L169-L169](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L169-L169)
  - [observation/documented] The runtime reportedly keeps both a full durable transcript and a smaller working memory so sessions can be resumed while preserving important state. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49)
- orchestration (1 claim(s)):
  - [observation/documented] Scoped subtasks can be delegated to helper subagents that inherit enough context to help while operating within limits. -- evidence: [README.md#L38-L49](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L38-L49)
- tools-permissions (1 claim(s)):
  - [observation/documented] Risky tools such as shell commands and file writes are gated by approval, with three modes: ask (default and recommended), auto (allows arbitrary command execution and file writes), and never (denies risky actions). -- evidence: [README.md#L143-L143](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L143-L143), [README.md#L145-L150](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md#L145-L150)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](mini-coding-agent.detail.md)

Metadata and full claim list: [full detail](mini-coding-agent.detail.md)
Human notes ([notes](mini-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
