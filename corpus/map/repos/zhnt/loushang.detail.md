# zhnt/loushang -- full detail

[Back to orientation](loushang.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhnt/loushang/89d885f53c1a896477979d3a7371119a5fc76c54/c0aea91282c5ba83.json](../../../wiki/dossiers/zhnt/loushang/89d885f53c1a896477979d3a7371119a5fc76c54/c0aea91282c5ba83.json)

## specifications (1 claim(s))

- [observation/documented] Loushang is described as a method-native AI work system for running complex work from intent to verified delivery, with the current focus on a coding CLI. -- evidence: [README.md#L7-L7](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L7-L7), [README.md#L5-L5](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L5-L5) (`clm_398429fd77078216e050041812640bbc8965511e7f55d0e0f3d041d4f761a2d5`)

## components (1 claim(s))

- [observation/documented] The system is organized into named layers: method (work contract), work (runtime fact), agent (execution kernel), ai (model access), harness (substrate), coding (V1 surface), tui, and channel. -- evidence: [README.md#L15-L15](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L15-L15) (`clm_3b80c839ff4fe94da270af5359e37313e09a844637af63371223825f0f54a925`)

## design-choices (8 claim(s))

- [observation/documented] The accepted plugin architecture treats a Plugin as an independently selectable activation identity grouping typed contributions, distinct from Capability, Skill, Tool, Extension, or process. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L45-L48](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L45-L48), [docs/internals/architecture/harness/plugin/architecture.md#L43-L43](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L43-L43) (`clm_f57466bc7d9cd4e5ff7b201c2023c3995ad5eab8888f97437363b9fbf064a200`)
- [observation/documented] Plugin discovery, inspection, dependency solving, and selection operate on inert serializable data and never import modules or run scripts; execution starts only after revalidation of revision, scope, authority, and approval. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L101-L104](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L101-L104), [docs/internals/architecture/harness/plugin/architecture.md#L106-L108](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L106-L108) (`clm_57338955f7519da31ab6a1dcd5465cb40648e912aefd623b7fa5beed8ccc6c63`)
- [observation/documented] Manifests may request authority but cannot grant it, self-mark trust, choose sandbox exemptions, or widen product policy; trust is evaluated by Host-owned policy. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L112-L116](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L112-L116) (`clm_c3d4b2a534ce839726525a6c572f1d41238c45bcc6a2a19fec109f3b76197c02`)
- [observation/documented] The architecture keeps declaration axes independent (artifact, identity, contribution, capability, execution topology, trust, lifetime, scope), so resource/capability/worker/remote are not Plugin types. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L167-L176](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L167-L176), [docs/internals/architecture/harness/plugin/architecture.md#L164-L165](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L164-L165), [docs/internals/architecture/harness/plugin/architecture.md#L178-L183](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L178-L183) (`clm_d80b16e83656ad4a5d617dafcf0a548c425635363c621e570fb4dce15ac9c91d`)
- [observation/documented] The agent loop remains owned by loushang.agent; plugins may contribute tools, resources, capability providers, and adapters but cannot replace its state machine. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L233-L235](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L233-L235) (`clm_36850e209d5ad562c9fe5522e7deaea9b40cf63a15c48000e5c727f292e347ec`)
- [observation/documented] The threat model assumes plugins and dependencies may be malicious or compromised, and mandates fail-closed handling of traversal, symlink escape, approval replay, stale IPC, and output floods. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L607-L610](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L607-L610), [docs/internals/architecture/harness/plugin/architecture.md#L612-L621](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L612-L621) (`clm_6f20407cb0f47be747b4458f6e55972ef3308f67b300aaa3bd564eede04c21d6`)
- [observation/documented] Process isolation is treated as distinct from security isolation: Policy, Approval, Sandbox, Host, and Domain are separate axes, and required containment fails closed before spawn. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L544-L546](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L544-L546), [docs/internals/architecture/harness/plugin/architecture.md#L556-L560](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L556-L560), [docs/internals/architecture/harness/plugin/architecture.md#L548-L554](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L548-L554) (`clm_d4ea3da642146da12e478885cc91159d3e75f10232bd0e13e8eca10027f2060d`)
- [inference/documented] The loushang.ai SDK appears to provide provider-aware model access with a model registry, streaming, tool calls, and cost helpers, per the README feature list. -- evidence: [README.md#L19-L24](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L19-L24) (`clm_d428b6c2a8c8ab8f42e7ca5cd2982410a2a09c712538d9823e70ecdbb1098b01`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the recommended way to run Loushang is from source via git clone, a uv-created .venv, and editable install with the dev extra; `make bootstrap` automates this and no `make install` target exists. -- evidence: [README.md#L34-L36](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L34-L36), [README.md#L28-L28](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L28-L28), [README.md#L44-L44](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L44-L44) (`clm_f6aa6fda4581943d3b9bece0fa2d52aa2b67e2bcf99086b34e0482a972f63d90`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are typed Resource projections containing instructions, metadata, assets, and optional scripts; script existence grants no execution authority, and the catalog/Skill parser never executes scripts. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L455-L459](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L455-L459), [docs/internals/architecture/harness/plugin/architecture.md#L481-L485](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L481-L485), [docs/internals/architecture/harness/plugin/architecture.md#L469-L472](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L469-L472) (`clm_cb197ff0b99e1c364b2a8cf847282e21d897324035c16dd0492420229308cf7f`)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes flags such as --help, --list-models, and --list-commands, and supports a prompt mode like `loushang -p "..."` for one-shot requests. -- evidence: [README.md#L38-L42](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L38-L42) (`clm_a5d20332662bed4cd17db01f11749498d0cee804c323974803fdfeaf0e9285be`)
- [observation/documented] The plugin runtime manifest is a strict plugin.json carrying identity, version, engine range, contribution index, configuration schema, dependencies, requested authority, and execution topology. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L324-L329](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L324-L329), [docs/internals/architecture/harness/plugin/architecture.md#L313-L320](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L313-L320) (`clm_3bca7e114ba718fa0234897b938aadf034bdf90c90018b1de224e77f933eec5d`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are durable coding conversations that can be resumed, forked, exported, and inspected, with diagnostics available. -- evidence: [README.md#L19-L24](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L19-L24), [README.md#L50-L54](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L50-L54) (`clm_0fc68fde52d563550c27d6e11d9e914f76e1dd35ea55c1d3430629e4f85c4526`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Tools are defined as executable capabilities made available to the agent under policy, and the product offers built-in coding tools plus configurable tool surfaces. -- evidence: [README.md#L19-L24](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L19-L24), [README.md#L50-L54](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L50-L54) (`clm_42db6cd5c884fa23bd3ce3a04528b19747e16c2ce8ef2b2e014b0f81a33ee28d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project uses uv for virtual environment creation and pip-style editable installation with a [dev] extra, and third-party dependency information is documented in THIRD_PARTY_NOTICES.md. -- evidence: [README.md#L34-L36](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L34-L36), [README.md#L101-L101](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L101-L101) (`clm_db479b2adfa4034bcbfe216baf5a4cb738155f64a63a478793da4855d3dbea29`)

## limitations (3 claim(s))

- [observation/documented] The plugin architecture document states implementation is partial: strict codecs, ledgers, and some coding paths exist, while the public SDK, managed Skill actions, and isolated Plugin Workers remain future delivery work. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L5-L30](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L5-L30) (`clm_7e2d1c9d73000aa14376b7b18de478a16a07b0660ca1443fbd71c2d37e4f7530`)
- [observation/documented] The current PyPI materializer can invoke uv pip install/pip install without wheel-only or contained build service, which the document calls an explicit current security gap for untrusted plugin admission. -- evidence: [docs/internals/architecture/harness/plugin/architecture.md#L305-L309](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/docs/internals/architecture/harness/plugin/architecture.md#L305-L309) (`clm_5d164e60f352336836b10738691eba4c0ee9e4baa87d510a87a9a5665f00db23`)
- [observation/documented] Loushang is in active early development; the stable focus is loushang code and the loushang.ai SDK, while work/research/ppt surfaces are roadmap directions only. -- evidence: [README.md#L81-L81](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L81-L81), [README.md#L83-L83](https://github.com/zhnt/loushang/blob/89d885f53c1a896477979d3a7371119a5fc76c54/README.md#L83-L83) (`clm_ce0c26e1443a55dcd3d480879215783cda2d0eb8cd3edf9da5c64f2c5156e9f6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

