# nanocoai/nanoclaw

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 3f9ed607b7e7 @ 2c4c789497c747f6

## Summary (orientation draft, not independently verified)

Selected evidence records: Agents run in their own Linux/Docker containers with filesystem isolation, so bash commands execute inside the container rather than on the host, and only explicitly mounted directories are visible. The project deliberately avoids configuration files; customization is done by asking Claude Code to modify the small codebase, or via a guided /customize command.

## Source coverage

Source coverage (partial): 6 of 49 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A single Node host process routes messages through an entity model (user → messaging group → agent group → session), writes to the session's inbound.db, and wakes the container; the agent-runner inside polls inbound.db and writes responses to outbound.db. -- evidence: [README.md#L192-L192](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L192-L192), [docs/architecture.md#L41-L54](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L41-L54)
- design-choices (2 claim(s)):
  - [observation/documented] Agents run in their own Linux/Docker containers with filesystem isolation, so bash commands execute inside the container rather than on the host, and only explicitly mounted directories are visible. -- evidence: [README.md#L223-L223](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L223-L223), [README.md#L38-L38](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L38-L38), [README.md#L77-L77](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L77-L77), [README.md#L91-L98](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L91-L98)
  - [observation/documented] The project deliberately avoids configuration files; customization is done by asking Claude Code to modify the small codebase, or via a guided /customize command. -- evidence: [README.md#L227-L227](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L227-L227), [README.md#L156-L156](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L156-L156), [README.md#L163-L163](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L163-L163)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions to the base are limited to security fixes, bug fixes, and clear improvements; new capabilities must be contributed as skills on the channels/providers branches or as self-contained skills, per CONTRIBUTING.md. -- evidence: [README.md#L258-L258](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L258-L258), [README.md#L260-L260](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L260-L260)
- skills-patterns (1 claim(s)):
  - [observation/documented] Trunk ships only the registry and infrastructure; channel adapters and alternative providers live on long-lived channels/providers branches and are installed into a user's fork via /add-<name> skills that copy modules, wire registration, and pin dependencies. -- evidence: [README.md#L85-L85](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L85-L85), [README.md#L171-L171](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L171-L171)
- interfaces (2 claim(s)):
  - [observation/documented] Channel adapters return platform channel and thread IDs without knowing agent-group or session IDs; the host maps those to the entity model, and session mode (shared vs per-thread) is configured per channel. -- evidence: [docs/architecture.md#L66-L66](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L66-L66), [docs/architecture.md#L68-L71](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L68-L71)
  - [observation/documented] Outbound file delivery is tool-based: the agent calls a dedicated send_file MCP tool, the runner stages files in an outbox directory per messages_out row, messages_out references filenames only, and the host delivers and cleans up after delivery. -- evidence: [docs/architecture.md#L191-L191](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L191-L191), [docs/architecture.md#L175-L175](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L175-L175), [docs/architecture.md#L193-L193](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L193-L193)
- memory-state (2 claim(s)):
  - [observation/documented] Each session has a pair of mounted SQLite files as the only host-container IO mechanism: inbound.db (host-written, container read-only) and outbound.db (container-written), each with exactly one writer and journal_mode=DELETE rather than WAL. -- evidence: [docs/architecture.md#L12-L17](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L12-L17), [docs/architecture.md#L7-L10](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L7-L10)
More evidence: [full detail](nanoclaw.detail.md)

Metadata and full claim list: [full detail](nanoclaw.detail.md)
Human notes ([notes](nanoclaw.notes.md), never overwritten by build)

[Back to map index](../../index.md)
