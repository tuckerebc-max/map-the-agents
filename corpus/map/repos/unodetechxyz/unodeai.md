# unodetechxyz/unodeai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e83cc216cd09 @ f3a2b20a71ff61b7

## Summary (orientation draft, not independently verified)

Evidence consists of README and wiki documentation for UnodeAi 0.9.79, a VS Code-family extension that organizes AI agents into role-based teams with an evidence layer separating agent claims from framework-observed facts. Claims below are documentation-based; no source code is in the snapshot. Evidence coverage: 98 of 118 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The wiki documents UnodeAi version 0.9.79. -- evidence: [docs/wiki/README.md#L3-L3](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The product ships 52 role templates and 25 team presets spanning areas like software engineering, marketing, sales, compliance, security, and operations. -- evidence: [README.md#L65-L68](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L65-L68)
- design-choices (1 claim(s)):
  - [observation/documented] Dashboard 'Done' status uses blue rather than green because the previous green failed contrast thresholds on the default light theme and resembled the working dot in dark themes, measured across all four bundled themes. -- evidence: [docs/wiki/README.md#L64-L73](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L64-L73)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the release runner requires all 12 targeted mutations to be killed, and CI builds the shipped artifact with a human publishing those exact bytes and the SHA-256. -- evidence: [README.md#L90-L94](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L90-L94), [docs/wiki/README.md#L64-L73](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L64-L73)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product runs in VS Code, Cursor, and Windsurf, and supports routing across Claude, OpenAI-compatible endpoints, local gateways, and the Unode gateway; Codex Headless is shown as Coming soon and cannot be selected or started in this release. -- evidence: [README.md#L251-L253](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L251-L253), [docs/wiki/README.md#L9-L12](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L9-L12), [README.md#L96-L97](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L96-L97)
  - [observation/documented] A command exports a run as standalone Markdown evidence ('UnodeAi: Export Run Evidence Pack'), and a portable-run-evidence/3 JSON schema carries hashes, actor ordinals, and read-receipt states while excluding raw commands, context contents, and credentials. -- evidence: [docs/wiki/README.md#L112-L112](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L112-L112), [docs/wiki/README.md#L114-L125](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L114-L125)
- memory-state (1 claim(s)):
  - [observation/documented] The memory_note tool appends to .unode/memory/notes.md with a routing tier and a semantic kind (pitfall, contract, or decision); reloaded rows are treated as untrusted claims, and human attestation affects prompt admission only, not trust or tool access. -- evidence: [docs/wiki/README.md#L19-L23](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L19-L23), [docs/wiki/README.md#L25-L30](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L25-L30), [README.md#L278-L300](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L278-L300)
- orchestration (2 claim(s)):
  - [observation/documented] A project manager agent breaks a goal into tasks and delegates to specialist agents, each with its own role, skills, chosen model, and granted permissions. -- evidence: [README.md#L11-L14](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/README.md#L11-L14), [docs/wiki/README.md#L5-L5](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L5-L5)
  - [observation/documented] Only the first PM in a team roster acts as coordinator; only it can dispatch, collect, or inspect delegation handles, and worker fan-out is removed in this release. -- evidence: [docs/wiki/README.md#L32-L35](https://github.com/UnodeTechxyz/unodeai/blob/e83cc216cd0991d9538d0c39a3faec3a393cfe87/docs/wiki/README.md#L32-L35)
More evidence: [full detail](unodeai.detail.md)

Metadata and full claim list: [full detail](unodeai.detail.md)
Human notes ([notes](unodeai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
