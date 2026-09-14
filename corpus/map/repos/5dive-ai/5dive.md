# 5dive-ai/5dive

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 420651c634b0 @ 00021c2ed875dd28

## Summary (orientation draft, not independently verified)

5dive is a self-hosted multi-agent runtime where each agent is its own Linux user running an official coding CLI as a systemd service, coordinated through a single bash CLI over a shared SQLite task queue. Evidence covers the CLI surface, isolation tiers, delegated push, constitution loading, memory, UI, and a not-yet-shipped decentralized loop-install spec. Evidence coverage: 151 of 375 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 12 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Agents take work from a shared SQLite task queue on one host, report up an org chart, hand work to each other, and escalate to a human via Telegram only when a decision is needed. -- evidence: [README.md#L81-L81](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L81-L81), [README.md#L40-L40](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L40-L40), [README.md#L293-L293](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L293-L293), [README.md#L280-L280](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L280-L280)
  - [observation/documented] Multiple agent types are supported, including claude, codex, antigravity, grok, devin, hermes, openclaw, opencode, and pi, each with its own auth options and channel support (Telegram and/or Discord). -- evidence: [README.md#L109-L119](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L109-L119)
- design-choices (1 claim(s)):
  - [observation/documented] The orchestrator is deliberately just bash: each agent is its own Linux user running an official coding CLI as a systemd service, with no framework, protocol, or broker; agents coordinate by invoking one shared 5dive CLI. -- evidence: [README.md#L97-L97](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L97-L97), [README.md#L103-L103](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L103-L103), [README.md#L38-L38](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L38-L38)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the 5dive bundle at the repo root is built from src/ via ./build.sh, and CI enforces that the bundle does not drift; contributing guidance lives in CONTRIBUTING.md. -- evidence: [README.md#L497-L497](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L497-L497)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The 5dive CLI exposes verbs for agent lifecycle (create/start/stop/logs/config), tasks, goals, loops, council, trace, run metrics, memory search, triggers, heartbeat, org, ui, account, and team import; every command accepts --json with an {ok,data}/{ok:false,error} envelope and exit codes matching error.code. -- evidence: [README.md#L385-L395](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L385-L395), [README.md#L473-L473](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L473-L473), [README.md#L369-L377](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L369-L377), [README.md#L379-L383](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L379-L383), [README.md#L361-L367](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L361-L367)
  - [observation/documented] `5dive ui` serves a local, read-only web UI on loopback (default port 8735) with org chart, queue, gates, and triggers views; it refuses routable --host addresses unless FIVE_UI_ALLOW_REMOTE=1 is set. -- evidence: [README.md#L357-L357](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L357-L357), [README.md#L346-L348](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L346-L348), [README.md#L352-L355](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/README.md#L352-L355)
- memory-state (2 claim(s)):
  - [observation/documented] Governance policy can be loaded from a constitution.yaml in the state dir (or FIVEDIVE_CONSTITUTION_FILE); if the file is absent or malformed the loader falls back atomically to shipped defaults and never applies a partial document. -- evidence: [docs/constitution.md#L3-L7](https://github.com/5dive-ai/5dive/blob/420651c634b0180b8efc189a357a47ea8f02ceb3/docs/constitution.md#L3-L7)
More evidence: [full detail](5dive.detail.md)

Metadata and full claim list: [full detail](5dive.detail.md)
Human notes ([notes](5dive.notes.md), never overwritten by build)

[Back to map index](../../index.md)
