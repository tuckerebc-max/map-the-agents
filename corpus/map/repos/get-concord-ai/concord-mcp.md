# get-concord-ai/concord-mcp

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d2408b0cbce5 @ 53cc4a249ea2b42d

## Summary (orientation draft, not independently verified)

Concord MCP is a local-first MCP server giving coding agents shared work-state (presence, messaging, task ownership, handoffs) backed by a per-repo SQLite store, with a CLI and per-harness adapters. Evidence is mostly README/docs documentation; no source code slices are present.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Lifecycle-changing operations use the task's monotonic version as expected_version, so of two agents acting on the same version only the first transition succeeds; ownership changes are kept in an append-only audit history. -- evidence: [README.md#L148-L153](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L148-L153)
  - [observation/documented] Delivery fails immediately when the named agent has no reachable endpoint rather than silently rerouting; hook-only integrations leave a durable pull message and state that limitation in the result. -- evidence: [README.md#L130-L137](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L130-L137)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: releases publish to npm via OIDC trusted publishing from a v* tag-triggered GitHub Actions workflow, with an optional maintainer-approval environment gate; contributing guidance points to CONTRIBUTING.md and CLAUDE.md and notes strict typing with no 'any' or typecasts. -- evidence: [RELEASING.md#L57-L60](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/RELEASING.md#L57-L60), [RELEASING.md#L3-L5](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/RELEASING.md#L3-L5), [README.md#L238-L240](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L238-L240)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes five MCP tools: start_work, inspect_work, update_work, transfer_work, and finish_work, covering presence/claims, state reads, prompts, ownership changes, and completion evidence. -- evidence: [README.md#L118-L124](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L118-L124)
  - [observation/documented] Besides MCP tools, Concord offers a CLI (setup, status, dashboard, who, tasks, handoff, review-packet, export, doctor, adapters status) operating on the same shared workspace. -- evidence: [README.md#L187-L189](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L187-L189), [README.md#L191-L201](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L191-L201)
- memory-state (2 claim(s)):
  - [observation/documented] SQLite in the repo-root .concord/ directory is the local source of truth; the root is resolved from CONCORD_REPO_ROOT, then CLAUDE_PROJECT_DIR, then the working directory, so agents in one repo share one store. -- evidence: [README.md#L157-L162](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L157-L162)
  - [observation/documented] The .concord/ workspace holds concord.db, HANDOFF.md, REVIEW_PACKET.md, and an optional WORK_STATE.json export; setup gitignores the directory so it stays local by default. -- evidence: [README.md#L177-L183](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L177-L183), [README.md#L172-L175](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L172-L175)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package is distributed as @concord-ai/concord-mcp on npm, installed globally, and the release workflow requires Node 24 and npm >= 11.5.1. -- evidence: [README.md#L52-L56](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/README.md#L52-L56), [RELEASING.md#L64-L67](https://github.com/Get-Concord-AI/concord-mcp/blob/d2408b0cbce5c24f9fd85ead5ec23522fbeea0e3/RELEASING.md#L64-L67)
- limitations (2 claim(s)):
More evidence: [full detail](concord-mcp.detail.md)

Metadata and full claim list: [full detail](concord-mcp.detail.md)
Human notes ([notes](concord-mcp.notes.md), never overwritten by build)

[Back to map index](../../index.md)
