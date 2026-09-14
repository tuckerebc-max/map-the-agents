# failproofai/failproofai

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 86f80fc59ee1 @ cca0cfe74a52d5e3

## Summary (orientation draft, not independently verified)

FailproofAI is a TypeScript npm package providing local hook-based observability and policy enforcement for 12 agent harnesses, with 39 built-in policies, a local dashboard on port 8020, and a hosted observability offering. Evidence is mostly README and translated docs; no source code slices are present.

## Source coverage

Source coverage (partial): 6 of 1040 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] 39 built-in policies ship with the tool and activate immediately on install; examples include blocking .env reads, sudo, rm -rf, force pushes, destructive SQL, and unreviewed terraform/kubectl changes. -- evidence: [README.md#L149-L158](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L149-L158), [README.md#L143-L143](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L143-L143)
  - [observation/documented] A hosted observability product offers fleet-wide runs, execution graphs with parallel sub-agent lanes, latency percentiles, per-model cost tracking, SQL over traces, scheduled audits, and Slack/email/webhook alerts; self-hosting is Enterprise-only. -- evidence: [README.md#L213-L220](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L213-L220)
- design-choices (1 claim(s)):
  - [observation/documented] The tool is licensed under MIT plus the Commons Clause: free for internal and personal use, but commercial resale of failproofai itself requires a separate agreement. -- evidence: [README.md#L258-L258](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L258-L258)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors must run 'bun install && bun run build' before starting, because the repo runs failproofai's own hooks on itself and they resolve the import against the compiled dist/ bundle. -- evidence: [README.md#L266-L270](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L266-L270)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The product hooks into 12 agent harnesses in two classes: ten coding CLIs (e.g. Claude Code, Codex) and two chat/assistant gateways (Hermes, OpenClaw), with the same events and policies across them. -- evidence: [README.md#L17-L21](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L17-L21), [README.md#L33-L35](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L33-L35)
  - [observation/documented] Agents outside supported harnesses can report via a Python SDK providing tracing, sessions and audits; enforcement there requires a hook in the user's own runtime. -- evidence: [README.md#L37-L39](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L37-L39)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Policies return one of three decisions: allow() permits the operation, deny(message) blocks it and returns the message to the agent, and instruct(message) lets it pass while adding context to the agent's next prompt. -- evidence: [README.md#L188-L192](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L188-L192)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package is distributed via npm as failproofai and installed globally with npm install -g; the project is written in TypeScript per its Trendshift badge. -- evidence: [README.md#L5-L5](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L5-L5), [README.md#L137-L141](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L137-L141)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](failproofai.detail.md)

Metadata and full claim list: [full detail](failproofai.detail.md)
Human notes ([notes](failproofai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
