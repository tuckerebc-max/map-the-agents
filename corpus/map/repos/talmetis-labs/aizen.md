# talmetis-labs/aizen

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: aizen-stack/aizen (github id 1289932122).
Latest snapshot: commit 997bdd3bbba4 @ 861f8119c0413970

## Summary (orientation draft, not independently verified)

Selected evidence records: Aizen is documented as a single static binary (~34 MB, ~10 ms cold start claimed) requiring no Node, Python, Docker, or cloud account, targeting Windows, Linux, and macOS. The agent accepts any OpenAI-style /chat/completions endpoint, including OpenAI, OpenRouter, local llama.cpp/vLLM, or an Anthropic gateway.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The sandbox code is organized under src/sandbox with modules for policy, capabilities, a single runner that builds sandboxed commands, audit logging, and per-platform backends (guarded, linux, windows, macos). -- evidence: [docs/SANDBOX.md#L55-L68](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L55-L68)
  - [observation/documented] v0.6.1 consolidated tools: multi_edit merged into file_edit (edits[] for atomic multi-edit), and four checkpoint tools collapsed into checkpoint (save/rewind/restore) and read-only checkpoint_view (diff/list). -- evidence: [release-notes-v0.6.1.md#L22-L23](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/release-notes-v0.6.1.md#L22-L23), [release-notes-v0.6.1.md#L16-L18](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/release-notes-v0.6.1.md#L16-L18)
- design-choices (1 claim(s)):
  - [observation/documented] Aizen is documented as a single static binary (~34 MB, ~10 ms cold start claimed) requiring no Node, Python, Docker, or cloud account, targeting Windows, Linux, and macOS. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [README.md#L8-L8](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L8-L8), [README.md#L19-L24](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L19-L24)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors sign a CLA once via a bot-comment flow with the exact sentence 'I have read the CLA Document and I hereby sign the CLA'; the CLA grants the maintainer commercial relicensing rights while the public project stays Apache-2.0. -- evidence: [CLA.md#L42-L45](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L42-L45), [CLA.md#L100-L100](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L100-L100), [CLA.md#L96-L98](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L96-L98), [README.md#L123-L125](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L123-L125)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The agent accepts any OpenAI-style /chat/completions endpoint, including OpenAI, OpenRouter, local llama.cpp/vLLM, or an Anthropic gateway. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [README.md#L10-L11](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L10-L11)
- memory-state (1 claim(s)):
  - [observation/documented] The agent is documented to keep an offline BM25-ranked memory that learns from reuse, plus a persona, a durable 'SOUL' identity, and skills it writes for itself after real work. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94)
- orchestration (1 claim(s)):
  - [observation/documented] A 'Pantheon' of seven capability-scoped sub-agents (argus, metis, daedalus, nemesis, themis, clio, mnemosyne) is fanned out via `aizen workflow`, which synthesizes one answer. -- evidence: [README.md#L108-L113](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L108-L113)
- tools-permissions (3 claim(s)):
  - [observation/documented] The sandbox runs commands without inheriting API keys, denies network by default, and enforces filesystem policy via Landlock+seccomp on Linux and Seatbelt on macOS; Windows uses Job-Object containment and reports 'partial'. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [docs/SANDBOX.md#L101-L108](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L101-L108)
  - [observation/documented] Sandbox modes are auto (default), strict, guarded, and off; strict refuses spawns rather than downgrading, and unattended runs fail closed unless sandbox.allow_guarded_fallback is true. -- evidence: [docs/SANDBOX.md#L85-L90](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L85-L90)
More evidence: [full detail](aizen.detail.md)

Metadata and full claim list: [full detail](aizen.detail.md)
Human notes ([notes](aizen.notes.md), never overwritten by build)

[Back to map index](../../index.md)
