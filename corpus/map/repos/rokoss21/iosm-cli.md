# rokoss21/iosm-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6cb971ca9c23 @ d07da58db67add57

## Summary (orientation draft, not independently verified)

Selected evidence records: The product supports an ACP compatibility mode via --mode acp, with a documented acp.handshake returning protocol version and capabilities including streaming, permissionBridge, toolEvents, sessionLifecycle, backCompatRpc, and execSessions. ACP methods map to internal runtime actions: session start/prompt/steer/follow_up/abort/state, builtin slash command dispatch, resumable shell exec sessions with stdin writes, and permission bridge responses supporting scope=once|turn|session.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] iosm-spec.md is a normative specification of the IOSM (Improve, Optimize, Shrink, Modularize) methodology, defining ordered phases, quality gates, normalized metrics, evidence-confidence rules, and an aggregate IOSM-Index score. -- evidence: [iosm-spec.md#L3-L3](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L3-L3), [iosm-spec.md#L7-L7](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L7-L7), [iosm-spec.md#L11-L14](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L11-L14)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Settings merge later-wins: global ~/.iosm/agent/settings.json lowest priority, then project .iosm/settings.json, then CLI flags at highest priority. -- evidence: [docs/configuration.md#L72-L76](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L72-L76), [docs/configuration.md#L70-L70](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L70-L70)
  - [observation/documented] Profiles control behavior and available tools: full grants all built-ins, plan is a read-only bundle, iosm adds IOSM cycle context, and meta is orchestration-first for multi-agent delegation; db_run is enabled only in write-capable profiles (full, meta, iosm). -- evidence: [docs/configuration.md#L406-L411](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L406-L411), [docs/configuration.md#L422-L423](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L422-L423)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product supports an ACP compatibility mode via --mode acp, with a documented acp.handshake returning protocol version and capabilities including streaming, permissionBridge, toolEvents, sessionLifecycle, backCompatRpc, and execSessions. -- evidence: [docs/acp-rpc-mapping.md#L7-L9](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L7-L9), [docs/acp-rpc-mapping.md#L3-L3](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L3-L3)
  - [observation/documented] ACP methods map to internal runtime actions: session start/prompt/steer/follow_up/abort/state, builtin slash command dispatch, resumable shell exec sessions with stdin writes, and permission bridge responses supporting scope=once|turn|session. -- evidence: [docs/acp-rpc-mapping.md#L13-L24](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L13-L24)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions persist under ~/.iosm/agent/sessions with JSONL trace files in session-traces; semantic search indexes are cached per project hash under ~/.iosm/agent/semantic/indexes containing meta.json, chunks.jsonl, and vectors.jsonl. -- evidence: [docs/configuration.md#L332-L337](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L332-L337), [docs/configuration.md#L11-L25](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L11-L25)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (3 claim(s)):
  - [observation/documented] The permissionMode setting defaults to "ask" and allows ask, auto, or yolo, controlling default tool-execution approval behavior. -- evidence: [docs/configuration.generated.md#L7-L10](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.generated.md#L7-L10)
  - [observation/documented] Extension tools can declare permission tiers (read-only, workspace-write, danger-full-access); with permissions.extensionToolEnforcement=true, read-only extension tools run automatically in auto mode and tools lacking requiredPermission metadata are blocked there. -- evidence: [docs/configuration.md#L481-L483](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L481-L483), [docs/configuration.md#L479-L479](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L479-L479), [docs/configuration.md#L475-L477](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L475-L477)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package is published on npm as iosm-cli, MIT-licensed, and requires Node.js >= 20.6.0 per its README badges. -- evidence: [README.md#L7-L13](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/README.md#L7-L13)
More evidence: [full detail](iosm-cli.detail.md)

Metadata and full claim list: [full detail](iosm-cli.detail.md)
Human notes ([notes](iosm-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
