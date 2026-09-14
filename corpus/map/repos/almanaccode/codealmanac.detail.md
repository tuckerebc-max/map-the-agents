# almanaccode/codealmanac -- full detail

[Back to orientation](codealmanac.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/almanaccode/codealmanac/0f153501f40a6596fe7c47dc6198eda149363135/7b563da85011a057.json](../../../wiki/dossiers/almanaccode/codealmanac/0f153501f40a6596fe7c47dc6198eda149363135/7b563da85011a057.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The wiki is plain markdown stored in the repo under almanac/, indexed locally and reviewed in Git like other code changes; a repo counts as a wiki when almanac/topics.yaml and almanac/README.md exist. -- evidence: [README.md#L19-L22](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L19-L22), [README.md#L280-L281](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L280-L281) (`clm_b156661f134fe4a626a4c5ef6cab80740e13d404de73f21a6b965a6c9ab242b3`)
- [observation/documented] The product is local-only: no hosted login, connect, or upload commands, no public SDK or MCP package, and no alternate wiki roots beyond almanac/. -- evidence: [README.md#L417-L431](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L417-L431), [README.md#L415-L415](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L415-L415), [README.md#L433-L435](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L433-L435) (`clm_2977149c896d390d85dc7b688e24d0de53cc006e0462a859791ae8181d201d77`)
- [observation/documented] Optional anonymous telemetry sends command/lifecycle outcomes and sanitized crashes under a random install UUID, never code, paths, prompts, or credentials; it can be disabled via setup flag, config, or DO_NOT_TRACK=1. -- evidence: [README.md#L72-L79](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L72-L79) (`clm_a563bc20230ea2696cfc480d8afcdee4f3ffd70199fb71282981b6de00cb24bd`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Read commands accept --wiki <name> to target another registered local wiki; by default they target the exact current directory when it is a registered repository root. -- evidence: [README.md#L126-L128](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L126-L128) (`clm_d312c51a35551142730fe5916cd76a6658ca102cc1958b87ea57f9e26cb6ef3a`)
- [observation/documented] The serve command opens a read-only local web viewer rendering pages, search, topics, backlinks, and file-reference navigation, with --no-open and --wiki options. -- evidence: [README.md#L352-L356](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L352-L356) (`clm_3c496fa181c347d4d2bc5d1d713272a867683522e9293cbe867f2d628f5edf49`)

## memory-state (1 claim(s))

- [observation/documented] Derived local state lives under ~/.codealmanac/, including a main database recording repositories, runs, run events, worker locks, and sync state, plus per-repo index databases. -- evidence: [README.md#L287-L290](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L287-L290), [README.md#L292-L294](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L292-L294), [README.md#L285-L285](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L285-L285) (`clm_d8e825009f4e4be073c8dc8c811ddef411ea6948c8737fe98e5c9f03f46fe9a1`)

## orchestration (3 claim(s))

- [observation/documented] Lifecycle commands (init, ingest, garden) queue runs and start a local worker; jobs can be listed, shown, logged, attached to, or cancelled, and records persist after the starting terminal closes. -- evidence: [README.md#L214-L214](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L214-L214), [README.md#L217-L217](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L217-L217), [README.md#L206-L207](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L206-L207), [README.md#L159-L161](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L159-L161), [README.md#L220-L220](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L220-L220), [README.md#L226-L230](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L226-L230), [README.md#L211-L211](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L211-L211), [README.md#L223-L224](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L223-L224) (`clm_8c7894a7fa7f85c096726b8d440f1909f6aad5fd0aa7fb372d1edd8beffe0310`)
- [observation/documented] Setup installs three macOS launchd jobs: Sync every 5 hours scanning agent conversations, Garden every 24 hours reviewing wikis, and Update every 24 hours installing safe CLI updates. -- evidence: [README.md#L63-L67](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L63-L67), [README.md#L60-L61](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L60-L61) (`clm_9a37a215454350cff077b7be60a3ad65d016ecccda6d8b76a32553e61d876430`)
- [observation/documented] Sync scans local Codex and Claude transcript stores and queues conversations from registered repositories as ingest jobs, possibly deciding a conversation holds no durable knowledge. -- evidence: [README.md#L168-L171](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L168-L171) (`clm_628012f55f1759ff16b6fdc0a848a6034952fe44437ec4da5938bf74d3466e08`)

## tools-permissions (1 claim(s))

- [observation/documented] Lifecycle agents run with broad, non-interactive filesystem permissions; the almanac/ boundary is described as an instruction and commit policy rather than an OS sandbox. -- evidence: [README.md#L137-L141](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L137-L141) (`clm_356548984db3b70dec0dac9254b93e3319b3637b92c1356fdc4205836dc4903d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Python 3.12+, is distributed via PyPI (the npm package is retired), and uses almanac-yoke as its single provider boundary for Codex and Claude runners. -- evidence: [README.md#L24-L24](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L24-L24), [README.md#L234-L237](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L234-L237), [README.md#L360-L363](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L360-L363) (`clm_51f805147a670437263e2ea05c5038d3e55dae7996da0334828ae8a95a7e926e`)

## limitations (1 claim(s))

- [observation/documented] Support is currently limited to macOS with Codex or Claude Code, and the rewrite is described as local-only for now, with hosted integration possible later but not in this release surface. -- evidence: [README.md#L24-L24](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L24-L24), [README.md#L415-L415](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L415-L415), [README.md#L433-L435](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L433-L435) (`clm_f1216dbd966231217d4dea2f9e592660ca95c677ee81d60d67548fbea74aee7c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

