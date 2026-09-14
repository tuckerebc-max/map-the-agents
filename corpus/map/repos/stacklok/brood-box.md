# stacklok/brood-box

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5f27eeb76988 @ 7d277f4201e40de9

## Summary (orientation draft, not independently verified)

Brood Box is an experimental Go CLI that runs coding agents (Claude Code, Codex, OpenCode, Hermes, Gemini) inside libkrun/KVM microVMs with copy-on-write workspace snapshots, per-file diff review, a DNS-aware egress firewall, and an MCP proxy. Its architecture follows strict DDD layering with dependency injection, and contributor guidance mandates task-based build/test workflows. Evidence coverage: 136 of 177 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Brood Box is an experimental CLI for running coding agents in hardware-isolated microVMs, with APIs, flags, and config format subject to change between releases. -- evidence: [README.md#L6-L6](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L6-L6), [README.md#L3-L4](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L3-L4)
- components (2 claim(s)):
  - [observation/documented] The project follows a strict DDD layering: pure domain packages under pkg/domain, an application SandboxRunner in pkg/sandbox, infrastructure implementations in internal/infra, and a Cobra CLI composition root in cmd/bbox. -- evidence: [docs/ARCHITECTURE.md#L8-L34](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L8-L34), [docs/ARCHITECTURE.md#L163-L163](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L163-L163), [docs/ARCHITECTURE.md#L88-L88](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L88-L88), [docs/ARCHITECTURE.md#L110-L110](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L110-L110), [docs/ARCHITECTURE.md#L165-L169](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L165-L169), [docs/ARCHITECTURE.md#L3-L4](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L3-L4)
  - [observation/documented] Built-in agents (claude-code, codex, opencode, hermes, gemini) each ship as a per-agent client package pairing an Agent value with a Plugin for MCP config injection and credential seeding, and custom agents can be defined in config. -- evidence: [README.md#L291-L297](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L291-L297), [README.md#L301-L311](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L301-L311), [CLAUDE.md#L69-L73](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L69-L73)
- design-choices (2 claim(s)):
  - [observation/documented] The guest VM runs a custom Go init binary (bbox-init) as PID 1 that handles boot, networking, workspace mounting, and an embedded SSH server, with no shell scripts or external sshd. -- evidence: [docs/ARCHITECTURE.md#L222-L280](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L222-L280), [README.md#L360-L362](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L360-L362)
  - [observation/documented] Snapshot mode uses FICLONE (Linux) or clonefile (macOS) for copy-on-write cloning, SHA-256 based diffing with unified diffs, hash re-verification on flush to prevent TOCTOU, and the VM is stopped before review begins. -- evidence: [README.md#L364-L368](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L364-L368), [README.md#L374-L383](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L374-L383)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must always use `task` targets (build, test, lint, fmt, verify) rather than raw go/docker commands, because the Taskfile sets critical flags, ldflags, and environment variables. -- evidence: [README.md#L421-L423](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L421-L423), [CLAUDE.md#L10-L10](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L10-L10)
  - [observation/documented] Repository development practice: the project enforces strict DDD layer boundaries with dependency injection, and code that violates layer boundaries is treated as a blocking merge issue. -- evidence: [CLAUDE.md#L44-L44](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L44-L44)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands like `bbox claude-code`, `bbox list`, and `bbox run-image <oci-image>`, with flags for cpus, memory, workspace, review, egress profile, allow-host, and MCP settings. -- evidence: [README.md#L159-L159](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L159-L159), [README.md#L141-L141](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L141-L141), [README.md#L156-L156](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L156-L156), [README.md#L144-L144](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L144-L144), [README.md#L128-L128](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L128-L128), [README.md#L138-L138](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L138-L138), [README.md#L116-L119](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L116-L119), [README.md#L122-L122](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L122-L122)
More evidence: [full detail](brood-box.detail.md)

Metadata and full claim list: [full detail](brood-box.detail.md)
Human notes ([notes](brood-box.notes.md), never overwritten by build)

[Back to map index](../../index.md)
