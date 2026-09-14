---
access: public
aliases: []
claim_ids:
- clm_17217cf699bfd38da07d8c907d854bedc2b9988e5c42ea3a24eb4fb4b36a1f8e
- clm_44911d8e39912ea551937173f3d00c630abb2092254c023a7f40da446ac470f0
- clm_4efd055c34084012b33c8a01cb98b3fe87b9e67a8c9647c1f619979d0da4deda
- clm_6e938a3cc0480141ce1c4634cc6d47c30a94b2cf7c9189cd00425a424d358f3b
- clm_b60dc02eded538752cf5f0c4d508cc2d7dd860839337fbd0c5563f5b7111b5d1
- clm_c15962b476c4ab7d6489922eb9008d91f09d78b9b16c8c52b034c9f9c9e6e767
- clm_f7a93818d2994014d6f7ce9c72bd82fae8befabf766903ae6d1a5cdbb122b792
maturity: draft
page_id: pg_31a237adc6f55dc687cc51661b4f02fd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_84c23c9cbdcd559d93724bcf69c47939
title: GenSI-THUAIR/FLEX/README.md @ b749fc351f81
updated_at: '2026-09-14T04:43:20Z'
---

# GenSI-THUAIR/FLEX/README.md @ b749fc351f81

<!-- rcw:begin owner=source:src_84c23c9cbdcd559d93724bcf69c47939 block=evidence -->
- The project is installed as an editable package (uv pip install -e .) and uses OpenAI-compatible LLM endpoints configured via API_KEY and BASE_URL environment variables. [@claim:clm_17217cf699bfd38da07d8c907d854bedc2b9988e5c42ea3a24eb4fb4b36a1f8e]
- Training via reject_sampling.py runs a multi-round loop: an actor attempts the task, a verifier LLM decides continue/stop, a critic extracts experiences, and an updater writes accepted entries into the experience library JSON. [@claim:clm_44911d8e39912ea551937173f3d00c630abb2092254c023a7f40da446ac470f0]
- In FLEX evaluation, the experience library is wrapped via create_memory_retrieval_tool into a tool the Actor can call during reasoning when retrieval is enabled. [@claim:clm_4efd055c34084012b33c8a01cb98b3fe87b9e67a8c9647c1f619979d0da4deda]
- FLEX (Forward Learning from Experience) is a learning paradigm that shifts learning from modifying model parameters to building and leveraging an evolvable experience library. [@claim:clm_6e938a3cc0480141ce1c4634cc6d47c30a94b2cf7c9189cd00425a424d358f3b]
- test_flex.py exposes CLI flags including --task_type (math/retro), --actor, --memory_path, --split, --samples, --batch_size, --no-retrieve for ablation, --pass_at_n, and --no-telemetry. [@claim:clm_b60dc02eded538752cf5f0c4d508cc2d7dd860839337fbd0c5563f5b7111b5d1]
- The paper reports experiments on AIME25, USPTO-50k retrosynthesis, and ProteinGym, with improvements such as 40% to 63% on AIME25 and 20% to 30% on USPTO50k. [@claim:clm_c15962b476c4ab7d6489922eb9008d91f09d78b9b16c8c52b034c9f9c9e6e767]
- Core modules include actor.py (task-solving agent), critic.py (experience extraction), explib.py (library abstraction), updater.py (dedup/acceptance), memory_retriever.py, and rate_limiter.py. [@claim:clm_f7a93818d2994014d6f7ce9c72bd82fae8befabf766903ae6d1a5cdbb122b792]
<!-- rcw:end owner=source:src_84c23c9cbdcd559d93724bcf69c47939 block=evidence -->

## Researcher notes

