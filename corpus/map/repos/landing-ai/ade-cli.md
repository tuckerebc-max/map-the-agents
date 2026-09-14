# landing-ai/ade-cli

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d1995ffef4e6 @ c1500fbf08ca7088

## Summary (orientation draft, not independently verified)

The repository ships the ADE CLI (formerly the agentic-doc SDK), a terminal client for Agentic Document Extraction with parse/extract commands, a local job-item store at ~/.ade, and agent-oriented JSON interfaces; a v2 design proposal documents the store and command design. Evidence coverage: 116 of 253 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] A draft v2 proposal (revised 2026-07-21) re-keys the store on job item ids — a hash of verb, source path, content, and params — replacing content-derived doc ids, with a flat ~/.ade/jobs/<id>/ layout. -- evidence: [docs/ade-cli-v2-proposal.md#L24-L29](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L24-L29), [docs/ade-cli-v2-proposal.md#L31-L32](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L31-L32), [docs/ade-cli-v2-proposal.md#L3-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L3-L10)
  - [observation/documented] The proposal defines parse as an idempotent state machine (absent/pending/complete/failed/expired) over the store, blocking by default with --wait, where Ctrl-C stops waiting but never the server-side work. -- evidence: [docs/ade-cli-v2-proposal.md#L197-L197](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L197-L197), [docs/ade-cli-v2-proposal.md#L180-L189](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L180-L189), [docs/ade-cli-v2-proposal.md#L193-L193](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L193-L193)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Re-running an identical command consumes no credits because results persist in the local store; parse dedup serves stored results with an explicit notice and only `--force` re-bills. -- evidence: [README.md#L6-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L6-L10), [docs/ade-cli-v2-proposal.md#L45-L47](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L45-L47)
  - [observation/documented] The CLI mentions new releases on stderr at most once a day, and ADE_NO_UPDATE_CHECK=1 disables that check; `ade update` self-updates, or points at uv tool upgrade for uv/pipx installs. -- evidence: [README.md#L114-L117](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L114-L117)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI offers `ade parse` to convert documents into grounded Markdown and elements, and `ade extract` to pull schema-shaped fields with page-and-box evidence, saving results to a local store at ~/.ade. -- evidence: [README.md#L6-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L6-L10)
  - [observation/documented] Every command accepts `--json` to emit one stable JSON object on stdout, and `ade help COMMAND` documents flags and result shapes. -- evidence: [README.md#L58-L60](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L58-L60)
- memory-state (1 claim(s)):
  - [observation/documented] The store lives at ~/.ade (app at ~/.ade/bin/ade), with ADE_HOME relocating it, ADE_CLI_VERSION pinning a version, and ADE_CLI_INSTALL_DIR changing the destination. -- evidence: [README.md#L111-L112](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L111-L112), [README.md#L105-L109](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L105-L109)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Releases ship self-contained binaries for macOS, Linux, and Windows on arm64 and x86_64, requiring no Python or uv. -- evidence: [README.md#L18-L19](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L18-L19)
- limitations (1 claim(s)):
More evidence: [full detail](ade-cli.detail.md)

Metadata and full claim list: [full detail](ade-cli.detail.md)
Human notes ([notes](ade-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
