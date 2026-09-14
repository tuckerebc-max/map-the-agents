# rokoss21/iosm-cli -- full detail

[Back to orientation](iosm-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rokoss21/iosm-cli/6cb971ca9c23266d83bb86597c381dd83b2ace0d/d07da58db67add57.json](../../../wiki/dossiers/rokoss21/iosm-cli/6cb971ca9c23266d83bb86597c381dd83b2ace0d/d07da58db67add57.json)

## specifications (1 claim(s))

- [observation/documented] iosm-spec.md is a normative specification of the IOSM (Improve, Optimize, Shrink, Modularize) methodology, defining ordered phases, quality gates, normalized metrics, evidence-confidence rules, and an aggregate IOSM-Index score. -- evidence: [iosm-spec.md#L3-L3](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L3-L3), [iosm-spec.md#L7-L7](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L7-L7), [iosm-spec.md#L11-L14](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/iosm-spec.md#L11-L14) (`clm_b75920c89206e8abc5e0d46a940a641afdf0ba8908586cdb712fcf0dc7dfe8fd`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Settings merge later-wins: global ~/.iosm/agent/settings.json lowest priority, then project .iosm/settings.json, then CLI flags at highest priority. -- evidence: [docs/configuration.md#L72-L76](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L72-L76), [docs/configuration.md#L70-L70](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L70-L70) (`clm_87cae113a1c3c5204a6909af3016baaaf4afc920614b36a75d5cfc75677876e9`)
- [observation/documented] Profiles control behavior and available tools: full grants all built-ins, plan is a read-only bundle, iosm adds IOSM cycle context, and meta is orchestration-first for multi-agent delegation; db_run is enabled only in write-capable profiles (full, meta, iosm). -- evidence: [docs/configuration.md#L406-L411](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L406-L411), [docs/configuration.md#L422-L423](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L422-L423) (`clm_c1edaa8f67958d6ec4f988e69f8d9fd8b156d9a720a67484bc02df5c1fca6a46`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product supports an ACP compatibility mode via --mode acp, with a documented acp.handshake returning protocol version and capabilities including streaming, permissionBridge, toolEvents, sessionLifecycle, backCompatRpc, and execSessions. -- evidence: [docs/acp-rpc-mapping.md#L7-L9](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L7-L9), [docs/acp-rpc-mapping.md#L3-L3](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L3-L3) (`clm_e8831cd744a1b75fd08ac7668c8f462edb19b9c0b0de8f53568c6525dd424f50`)
- [observation/documented] ACP methods map to internal runtime actions: session start/prompt/steer/follow_up/abort/state, builtin slash command dispatch, resumable shell exec sessions with stdin writes, and permission bridge responses supporting scope=once|turn|session. -- evidence: [docs/acp-rpc-mapping.md#L13-L24](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L13-L24) (`clm_d5a030ee615a2e8d25aa434d10f704a5fbceca884ad6a6d07cef4f69cece19c6`)
- [observation/documented] Unsupported ACP methods return JSON-RPC -32601 with reason=capability_not_supported; the ACP adapter is additive, leaving --mode rpc unchanged, and unsupported features fail with capability-level rejections rather than crashes. -- evidence: [docs/acp-rpc-mapping.md#L36-L38](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L36-L38), [docs/acp-rpc-mapping.md#L7-L9](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/acp-rpc-mapping.md#L7-L9) (`clm_0be1cc2ba787de562b79c51def908d2c4f4b1c78f3c0997d0795c4a4be830872`)

## memory-state (1 claim(s))

- [observation/documented] Sessions persist under ~/.iosm/agent/sessions with JSONL trace files in session-traces; semantic search indexes are cached per project hash under ~/.iosm/agent/semantic/indexes containing meta.json, chunks.jsonl, and vectors.jsonl. -- evidence: [docs/configuration.md#L332-L337](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L332-L337), [docs/configuration.md#L11-L25](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L11-L25) (`clm_feda1eb8196f0b2bae19da4afe24bd56939ec1b9d03740ef44cc854177f653fe`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] The permissionMode setting defaults to "ask" and allows ask, auto, or yolo, controlling default tool-execution approval behavior. -- evidence: [docs/configuration.generated.md#L7-L10](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.generated.md#L7-L10) (`clm_3d4d1180066861d1a5ddf7e8e8c6c07630123a613be962879662edea0ad3bcc3`)
- [observation/documented] Extension tools can declare permission tiers (read-only, workspace-write, danger-full-access); with permissions.extensionToolEnforcement=true, read-only extension tools run automatically in auto mode and tools lacking requiredPermission metadata are blocked there. -- evidence: [docs/configuration.md#L481-L483](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L481-L483), [docs/configuration.md#L479-L479](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L479-L479), [docs/configuration.md#L475-L477](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.md#L475-L477) (`clm_681652bc83cda90b4f779bd6c102b5f44ae1b049b6f42ecc42ed186913c08dd3`)
- [observation/documented] A sandbox.enabled setting (default false) enables a Linux bubblewrap sandbox for process-based tools. -- evidence: [docs/configuration.generated.md#L49-L52](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/docs/configuration.generated.md#L49-L52) (`clm_2af9f142dc6fe250783b00e62ad5d053c00d0711d690e94b15ba48653a37cb8e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is published on npm as iosm-cli, MIT-licensed, and requires Node.js >= 20.6.0 per its README badges. -- evidence: [README.md#L7-L13](https://github.com/rokoss21/iosm-cli/blob/6cb971ca9c23266d83bb86597c381dd83b2ace0d/README.md#L7-L13) (`clm_c31780a6e4cc31cff60bc116bbbc2c8276804aaa78341dd33a6a1b9d5904419b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

