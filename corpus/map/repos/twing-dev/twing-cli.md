# twing-dev/twing-cli

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 49b1d2c19911 @ 77b105848016c816

## Summary (orientation draft, not independently verified)

twing-cli is a coordination tool for multiple coding agents: a CLI plus a Claude Code hook and a coordinator server that gate edits behind registered designs and flag conflicts. Evidence is mostly README documentation plus a design-conflict coordinator spec; contributor build instructions appear only near the end. Evidence coverage: 112 of 162 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Twing is a CLI plus a hook for coding agents (Claude Code today, others planned) and a small server that every agent's client talks to, letting multiple agents on a team coordinate. -- evidence: [README.md#L3-L6](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L3-L6)
  - [observation/documented] Setup installs a hook wired into Claude Code and starts a background daemon; hooks are stateless per-invocation, while the daemon watches edits and syncs them to the server. -- evidence: [README.md#L38-L57](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L38-L57)
- design-choices (4 claim(s)):
  - [observation/documented] Conflicts collapse into four buckets; bucket 1 (constraint violations) is admin-gated and blocking, bucket 2 never blocks, and peer-vs-peer buckets 3/4 can be self-resolved with a justification. -- evidence: [README.md#L111-L127](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L111-L127), [README.md#L96-L100](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L96-L100)
  - [observation/documented] Bucket 3 conflicts come from Tree-sitter-parsed claims and bucket 4 from an async Bedrock semantic pass, so those findings can arrive after the edit already succeeded via align or an alignment thread. -- evidence: [README.md#L111-L127](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L111-L127)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors need Node.js >= 20, git, and Go for the hook; the repo builds packages/core, packages/cli, and packages/server via TypeScript project references with npm install and npm run build, and npm link in packages/cli provides a local twing command. -- evidence: [README.md#L548-L550](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L548-L550), [README.md#L541-L546](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L541-L546), [README.md#L533-L537](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L533-L537)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands such as twing init, twing align, and twing design register/amend/close, with register taking a summary and touched paths. -- evidence: [README.md#L291-L297](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L291-L297), [README.md#L129-L133](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L129-L133)
  - [observation/documented] The coordinator spec defines a single POST /v1/designs/check call that registers a design and returns a verdict (clean, overlap, or constraint_flag) in one blocking round trip. -- evidence: [docs/design-conflict-coordinator-spec.md#L117-L118](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L117-L118), [docs/design-conflict-coordinator-spec.md#L142-L158](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L142-L158), [docs/design-conflict-coordinator-spec.md#L160-L171](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L160-L171), [docs/design-conflict-coordinator-spec.md#L134-L140](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L134-L140)
- memory-state (1 claim(s)):
  - [observation/documented] The coordinator server (packages/server) is described as a single process with no external database, and it generates a one-time bootstrap token on first run. -- evidence: [README.md#L407-L412](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L407-L412), [README.md#L399-L400](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L399-L400)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](twing-cli.detail.md)

Metadata and full claim list: [full detail](twing-cli.detail.md)
Human notes ([notes](twing-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
