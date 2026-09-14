---
access: public
aliases: []
claim_ids:
- clm_36850e209d5ad562c9fe5522e7deaea9b40cf63a15c48000e5c727f292e347ec
- clm_3bca7e114ba718fa0234897b938aadf034bdf90c90018b1de224e77f933eec5d
- clm_57338955f7519da31ab6a1dcd5465cb40648e912aefd623b7fa5beed8ccc6c63
- clm_5d164e60f352336836b10738691eba4c0ee9e4baa87d510a87a9a5665f00db23
- clm_6f20407cb0f47be747b4458f6e55972ef3308f67b300aaa3bd564eede04c21d6
- clm_7e2d1c9d73000aa14376b7b18de478a16a07b0660ca1443fbd71c2d37e4f7530
- clm_c3d4b2a534ce839726525a6c572f1d41238c45bcc6a2a19fec109f3b76197c02
- clm_cb197ff0b99e1c364b2a8cf847282e21d897324035c16dd0492420229308cf7f
- clm_d4ea3da642146da12e478885cc91159d3e75f10232bd0e13e8eca10027f2060d
- clm_d80b16e83656ad4a5d617dafcf0a548c425635363c621e570fb4dce15ac9c91d
- clm_f57466bc7d9cd4e5ff7b201c2023c3995ad5eab8888f97437363b9fbf064a200
maturity: draft
page_id: pg_d8fb185614d25c72b98dfbf32ecd64ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d2505e27d7550328ad9a442fa3f4e45
title: zhnt/loushang/docs/internals/architecture/harness/plugin/architecture.md @
  89d885f53c1a
updated_at: '2026-09-14T03:27:30Z'
---

# zhnt/loushang/docs/internals/architecture/harness/plugin/architecture.md @ 89d885f53c1a

<!-- rcw:begin owner=source:src_9d2505e27d7550328ad9a442fa3f4e45 block=evidence -->
- The agent loop remains owned by loushang.agent; plugins may contribute tools, resources, capability providers, and adapters but cannot replace its state machine. [@claim:clm_36850e209d5ad562c9fe5522e7deaea9b40cf63a15c48000e5c727f292e347ec]
- The plugin runtime manifest is a strict plugin.json carrying identity, version, engine range, contribution index, configuration schema, dependencies, requested authority, and execution topology. [@claim:clm_3bca7e114ba718fa0234897b938aadf034bdf90c90018b1de224e77f933eec5d]
- Plugin discovery, inspection, dependency solving, and selection operate on inert serializable data and never import modules or run scripts; execution starts only after revalidation of revision, scope, authority, and approval. [@claim:clm_57338955f7519da31ab6a1dcd5465cb40648e912aefd623b7fa5beed8ccc6c63]
- The current PyPI materializer can invoke uv pip install/pip install without wheel-only or contained build service, which the document calls an explicit current security gap for untrusted plugin admission. [@claim:clm_5d164e60f352336836b10738691eba4c0ee9e4baa87d510a87a9a5665f00db23]
- The threat model assumes plugins and dependencies may be malicious or compromised, and mandates fail-closed handling of traversal, symlink escape, approval replay, stale IPC, and output floods. [@claim:clm_6f20407cb0f47be747b4458f6e55972ef3308f67b300aaa3bd564eede04c21d6]
- The plugin architecture document states implementation is partial: strict codecs, ledgers, and some coding paths exist, while the public SDK, managed Skill actions, and isolated Plugin Workers remain future delivery work. [@claim:clm_7e2d1c9d73000aa14376b7b18de478a16a07b0660ca1443fbd71c2d37e4f7530]
- Manifests may request authority but cannot grant it, self-mark trust, choose sandbox exemptions, or widen product policy; trust is evaluated by Host-owned policy. [@claim:clm_c3d4b2a534ce839726525a6c572f1d41238c45bcc6a2a19fec109f3b76197c02]
- Skills are typed Resource projections containing instructions, metadata, assets, and optional scripts; script existence grants no execution authority, and the catalog/Skill parser never executes scripts. [@claim:clm_cb197ff0b99e1c364b2a8cf847282e21d897324035c16dd0492420229308cf7f]
- Process isolation is treated as distinct from security isolation: Policy, Approval, Sandbox, Host, and Domain are separate axes, and required containment fails closed before spawn. [@claim:clm_d4ea3da642146da12e478885cc91159d3e75f10232bd0e13e8eca10027f2060d]
- The architecture keeps declaration axes independent (artifact, identity, contribution, capability, execution topology, trust, lifetime, scope), so resource/capability/worker/remote are not Plugin types. [@claim:clm_d80b16e83656ad4a5d617dafcf0a548c425635363c621e570fb4dce15ac9c91d]
- The accepted plugin architecture treats a Plugin as an independently selectable activation identity grouping typed contributions, distinct from Capability, Skill, Tool, Extension, or process. [@claim:clm_f57466bc7d9cd4e5ff7b201c2023c3995ad5eab8888f97437363b9fbf064a200]
<!-- rcw:end owner=source:src_9d2505e27d7550328ad9a442fa3f4e45 block=evidence -->

## Researcher notes

