# zhnt/loushang

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 89d885f53c1a @ c0aea91282c5ba83

## Summary (orientation draft, not independently verified)

Selected evidence records: Loushang is described as a method-native AI work system for running complex work from intent to verified delivery, with the current focus on a coding CLI. The system is organized into named layers: method (work contract), work (runtime fact), agent (execution kernel), ai (model access), harness (substrate), coding (V1 surface), tui, and channel.

## Source coverage

Source coverage (partial): 6 of 707 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Loushang is described as a method-native AI work system for running complex work from intent to verified delivery, with the current focus on a coding CLI. -- evidence: [README.md#L7-L7](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L7-L7), [README.md#L5-L5](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The system is organized into named layers: method (work contract), work (runtime fact), agent (execution kernel), ai (model access), harness (substrate), coding (V1 surface), tui, and channel. -- evidence: [README.md#L15-L15](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L15-L15)
- design-choices (8 claim(s)):
  - [observation/documented] The accepted plugin architecture treats a Plugin as an independently selectable activation identity grouping typed contributions, distinct from Capability, Skill, Tool, Extension, or process. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L45-L48](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L45-L48), [docs/internals/architecture/harness/plugin/architecture.md#L43-L43](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L43-L43)
  - [observation/documented] Plugin discovery, inspection, dependency solving, and selection operate on inert serializable data and never import modules or run scripts; execution starts only after revalidation of revision, scope, authority, and approval. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L101-L104](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L101-L104), [docs/internals/architecture/harness/plugin/architecture.md#L106-L108](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L106-L108)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the recommended way to run Loushang is from source via git clone, a uv-created .venv, and editable install with the dev extra; `make bootstrap` automates this and no `make install` target exists. -- evidence: [README.md#L34-L36](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L34-L36), [README.md#L28-L28](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L28-L28), [README.md#L44-L44](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L44-L44)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are typed Resource projections containing instructions, metadata, assets, and optional scripts; script existence grants no execution authority, and the catalog/Skill parser never executes scripts. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L455-L459](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L455-L459), [docs/internals/architecture/harness/plugin/architecture.md#L481-L485](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L481-L485), [docs/internals/architecture/harness/plugin/architecture.md#L469-L472](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L469-L472)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes flags such as --help, --list-models, and --list-commands, and supports a prompt mode like `loushang -p "..."` for one-shot requests. -- evidence: [README.md#L38-L42](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L38-L42)
  - [observation/documented] The plugin runtime manifest is a strict plugin.json carrying identity, version, engine range, contribution index, configuration schema, dependencies, requested authority, and execution topology. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L324-L329](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L324-L329), [docs/internals/architecture/harness/plugin/architecture.md#L313-L320](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L313-L320)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are durable coding conversations that can be resumed, forked, exported, and inspected, with diagnostics available. -- evidence: [README.md#L19-L24](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L19-L24), [README.md#L50-L54](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L50-L54)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](loushang.detail.md)

Metadata and full claim list: [full detail](loushang.detail.md)
Human notes ([notes](loushang.notes.md), never overwritten by build)

[Back to map index](../../index.md)
