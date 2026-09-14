# herry2059/project-os-for-codex -- full detail

[Back to orientation](project-os-for-codex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/herry2059/project-os-for-codex/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/6d015e25229802c1.json](../../../wiki/dossiers/herry2059/project-os-for-codex/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/6d015e25229802c1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The stack is React, Vite, TypeScript, and Tailwind CSS on the frontend with Node.js and Express on the backend, persisting to local JSON files by default under an Apache-2.0 license. -- evidence: [README.md#L262-L266](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L262-L266) (`clm_82308b18879b1cb426a3bb84259dfdebd0e9dc5a54e8009b41466598cf90cd2e`)

## design-choices (2 claim(s))

- [observation/documented] Version 0.3.0 adds a fail-closed first-run contract: the MCP process verifies credential, project binding, scopes, and the exact two-tool surface before Codex uses it, with a project-level config allowlisting only released tools. -- evidence: [README.md#L80-L80](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L80-L80), [README.md#L82-L85](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L82-L85) (`clm_505d5baa55fb3ede538bd2052b62e1e06fd6fb18d838d148cb4a6cf6ae650743`)
- [observation/documented] The open-source design keeps private infrastructure behind replaceable adapter boundaries for Git, AI provider, knowledge base, and deployment/reverse proxy, with local JSON persistence for simple evaluation. -- evidence: [README.md#L169-L169](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L169-L169), [README.md#L171-L175](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L171-L175) (`clm_10ff73852c2d3d163a52758640ad407003784c72df654bb915656190d8a43136`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to work one vertical slice at a time, use pnpm, run pnpm run check before committing, and inspect affected UI in light and dark themes. -- evidence: [AGENTS.md#L7-L9](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L7-L9), [AGENTS.md#L21-L25](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L21-L25) (`clm_db3b24e29683f5708b493e5bd57d102e200e4fcd1e758d41836aec85ccd24a52`)
- [observation/documented] Repository development practice: the Codex session protocol requires calling project_os_get_context before planning, running pnpm codex:doctor on failure, and only appending progress after verifying one vertical slice. -- evidence: [AGENTS.md#L36-L39](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L36-L39) (`clm_f00787d89e66c27b7e7dea63559e294e777c2d02b11d20e25efa9eb4ace123e9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The released MCP surface contains exactly two tools: project_os_get_context for scoped context reads and project_os_append_progress for validated, idempotent progress appends. -- evidence: [README.md#L75-L76](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L75-L76), [README.md#L192-L196](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L192-L196) (`clm_0e614fceb948b9c17a8db38686ffd89d1975719960b9002ebb55fff992091592`)
- [observation/documented] An Agent API endpoint accepts progress events via POST with X-Project-Key and Idempotency-Key headers, including verification notes, progress percentage, and next step. -- evidence: [README.md#L322-L328](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L322-L328), [README.md#L320-L320](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L320-L320) (`clm_3d9f3f90adfad3d749fcc33d51447b9f783542095e435499bc12986616b5c9db`)

## memory-state (1 claim(s))

- [observation/documented] The server creates a local Git-backed project record for kickoff, progress, issues, and handoff files, with important progress linked to Git commits as the durable record. -- evidence: [README.md#L138-L138](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L138-L138), [README.md#L140-L143](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L140-L143), [README.md#L104-L111](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L104-L111) (`clm_875b5289194917f8ebaa709322274ff9972ab45318e387a1a2d1f5436d3cdc14`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] AI credentials are short-lived (24 hours or 7 days), revocable independently, stored only as hashes, and cannot access members, keys, deletion, publication, or deployment. -- evidence: [README.md#L78-L78](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L78-L78) (`clm_9af94a8357694dc42a69c58861d1d1e0fd2701f6da0d837477594db662c1fa36`)
- [observation/documented] High-risk actions such as payment, deletion, role changes, publication, deployment, and rollback stay outside the MCP surface and require explicit human confirmation. -- evidence: [README.md#L91-L96](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L91-L96), [AGENTS.md#L13-L17](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L13-L17) (`clm_d5ee7eba328c2168569c7a435e4c6b2e8c81109864dc019699b222a873cbe029`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] The product does not run Codex, monitor sessions automatically, control a Codex account, or modify an existing source repository; its Git commits belong to the local Project OS record repository. -- evidence: [README.md#L192-L196](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L192-L196) (`clm_bdb1c7199cce60d79e28e986dc1158d3715f255a802840c364e77a0a05701a67`)
- [observation/documented] Verification notes are agent-reported and validated for structure, identity, scope, idempotency, and progress rules, but the server does not independently prove source code or deployments passed. -- evidence: [README.md#L192-L196](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L192-L196) (`clm_0bf96c9f545e21013613668df7059b1be652419401bc2439d188c07d4db841d2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

