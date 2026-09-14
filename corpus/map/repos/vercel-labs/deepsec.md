# vercel-labs/deepsec

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 23a69227e338 @ 83b78ffadd29c0d1

## Summary (orientation draft, not independently verified)

deepsec is an agent-powered vulnerability scanner for large existing codebases, with a regex scan stage, AI process/revalidate stages, append-only per-file on-disk state, plugin-mediated integrations, and optional Vercel Sandbox fan-out. All prior product claims were verified against cited slices; the plugin extension-point count was corrected to match the source's stated 'five'. Evidence coverage: 130 of 181 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] deepsec is an agent-powered vulnerability scanner that runs in the user's own infrastructure and is optimized for on-demand review of all code in large existing repositories. -- evidence: [README.md#L3-L4](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L3-L4)
- components (5 claim(s)):
  - [observation/documented] The scan stage globs the project root, applies regex matchers to every matched file, and writes candidate matches into per-file FileRecords without any AI usage. -- evidence: [docs/architecture.md#L86-L91](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L86-L91)
  - [observation/documented] The process stage batches pending files, sends each batch to a configured AI agent backend with the system prompt and INFO.md, and parses JSON responses into findings stored on FileRecords. -- evidence: [docs/architecture.md#L99-L106](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L99-L106)
- design-choices (1 claim(s)):
  - [observation/documented] The unit of work is a source file rather than a finding, which the architecture doc says makes per-file atomic locking and idempotent merges natural. -- evidence: [docs/architecture.md#L184-L186](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L184-L186)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes subcommands including scan, process, process --diff, triage, revalidate, enrich, report, export, metrics, status, and sandbox for running any command on Vercel Sandbox microVMs. -- evidence: [README.md#L120-L132](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L120-L132)
  - [observation/documented] Configuration lives in deepsec.config.ts (or .mjs/.js/.cjs) resolved from the current directory walking upward, declaring projects, plugins, matcher filters, default agent/model/thinking level, AI route, and dataDir. -- evidence: [docs/configuration.md#L6-L7](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/configuration.md#L6-L7), [docs/configuration.md#L29-L38](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/configuration.md#L29-L38)
- memory-state (2 claim(s)):
  - [observation/documented] On-disk state is append-only: re-scans merge new candidates, re-processing appends to analysisHistory and merges findings, and revalidation annotates findings with verdicts without overwriting or deleting anything. -- evidence: [docs/data-layout.md#L88-L91](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/data-layout.md#L88-L91), [docs/architecture.md#L58-L61](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L58-L61)
  - [observation/documented] Each FileRecord tracks candidates, findings, an append-only analysisHistory, gitInfo, a lifecycle status (pending/processing/analyzed/error), and a lockedByRunId field used for atomic file claiming. -- evidence: [docs/data-layout.md#L98-L110](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/data-layout.md#L98-L110)
- orchestration (3 claim(s)):
  - [observation/documented] The processor claims files atomically via lockedByRunId so multiple workers can run in parallel; concurrency and batch size flags control how many files are in flight. -- evidence: [docs/architecture.md#L120-L123](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L120-L123)
More evidence: [full detail](deepsec.detail.md)

Metadata and full claim list: [full detail](deepsec.detail.md)
Human notes ([notes](deepsec.notes.md), never overwritten by build)

[Back to map index](../../index.md)
