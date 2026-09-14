# gensi-thuair/flex -- full detail

[Back to orientation](flex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gensi-thuair/flex/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/c67fc1de393d9761.json](../../../wiki/dossiers/gensi-thuair/flex/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/c67fc1de393d9761.json)

## specifications (1 claim(s))

- [observation/documented] FLEX (Forward Learning from Experience) is a learning paradigm that shifts learning from modifying model parameters to building and leveraging an evolvable experience library. -- evidence: [README.md#L37-L38](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L37-L38) (`clm_6e938a3cc0480141ce1c4634cc6d47c30a94b2cf7c9189cd00425a424d358f3b`)

## components (1 claim(s))

- [observation/documented] Core modules include actor.py (task-solving agent), critic.py (experience extraction), explib.py (library abstraction), updater.py (dedup/acceptance), memory_retriever.py, and rate_limiter.py. -- evidence: [README.md#L273-L278](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L273-L278) (`clm_f7a93818d2994014d6f7ce9c72bd82fae8befabf766903ae6d1a5cdbb122b792`)

## design-choices (1 claim(s))

- [observation/documented] The memory retriever design prioritizes exhaustive exploration over efficiency, and keeps tools limited to data retrieval while the agent performs semantic analysis and response generation. -- evidence: [docs/memory_retriever_design.md#L10-L12](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L10-L12), [docs/memory_retriever_design.md#L15-L17](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L15-L17), [docs/memory_retriever_design.md#L5-L5](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L5-L5), [docs/memory_retriever_design.md#L62-L64](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L62-L64) (`clm_437e55d386afe831d23a86b47988825b88e06ab8f4d26fe6f15e1fb83131e0a7`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] test_flex.py exposes CLI flags including --task_type (math/retro), --actor, --memory_path, --split, --samples, --batch_size, --no-retrieve for ablation, --pass_at_n, and --no-telemetry. -- evidence: [README.md#L251-L263](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L251-L263) (`clm_b60dc02eded538752cf5f0c4d508cc2d7dd860839337fbd0c5563f5b7111b5d1`)
- [observation/documented] The retriever exposes multi-level abstraction tools (get_partition_methods, get_partition_rules, get_partition_trajectories), state tools, get_memory_statistics, and a final_answer tool for the actor. -- evidence: [docs/memory_retriever_design.md#L609-L617](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L609-L617), [docs/memory_retriever_design.md#L604-L607](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L604-L607), [docs/memory_retriever_design.md#L593-L597](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L593-L597), [docs/memory_retriever_design.md#L626-L629](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L626-L629), [docs/memory_retriever_design.md#L631-L634](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L631-L634), [docs/memory_retriever_design.md#L599-L602](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L599-L602) (`clm_3e91a69bfd6979c28cacf1312f36439b4dbce91ec0da21a77663910322b3ff1d`)

## memory-state (3 claim(s))

- [observation/documented] The memory library is partitioned into Golden (successful experiences), Warning (failure cases), and Mixed (learning trajectories) partitions. -- evidence: [docs/memory_retriever_design.md#L564-L567](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L564-L567), [docs/memory_retriever_design.md#L559-L562](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L559-L562), [docs/memory_retriever_design.md#L32-L37](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L32-L37), [docs/memory_retriever_design.md#L554-L557](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L554-L557) (`clm_838ad953422c2926dc31fe65a39fd4f6a9ab9e85177d5a478f6ed8ab0e974c26`)
- [observation/documented] Each memory entry stores a method description, rules with examples, a revised trajectory with comments, and metadata such as memory_type, problem_category, priority, and timestamps. -- evidence: [docs/memory_retriever_design.md#L571-L589](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L571-L589), [docs/memory_retriever_design.md#L40-L57](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L40-L57) (`clm_525c59aa3d1930d4679511584bfc72bd6de27498e72aac9b48a5e97fac8767e6`)
- [observation/documented] The retriever agent maintains per-partition exploration state (explored_up_to and recommended_indices) to avoid redundant exploration and support multi-turn continuity. -- evidence: [docs/memory_retriever_design.md#L609-L617](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L609-L617), [docs/memory_retriever_design.md#L381-L400](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L381-L400) (`clm_6033c9341e04ed26b98d86dd309d4f498e8001edd480496d2e883e08e871e3d8`)

## orchestration (1 claim(s))

- [observation/documented] Training via reject_sampling.py runs a multi-round loop: an actor attempts the task, a verifier LLM decides continue/stop, a critic extracts experiences, and an updater writes accepted entries into the experience library JSON. -- evidence: [README.md#L106-L109](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L106-L109) (`clm_44911d8e39912ea551937173f3d00c630abb2092254c023a7f40da446ac470f0`)

## tools-permissions (1 claim(s))

- [observation/documented] In FLEX evaluation, the experience library is wrapped via create_memory_retrieval_tool into a tool the Actor can call during reasoning when retrieval is enabled. -- evidence: [README.md#L218-L221](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L218-L221), [README.md#L267-L269](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L267-L269) (`clm_4efd055c34084012b33c8a01cb98b3fe87b9e67a8c9647c1f619979d0da4deda`)

## evaluation (1 claim(s))

- [observation/documented] The paper reports experiments on AIME25, USPTO-50k retrosynthesis, and ProteinGym, with improvements such as 40% to 63% on AIME25 and 20% to 30% on USPTO50k. -- evidence: [README.md#L40-L40](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L40-L40) (`clm_c15962b476c4ab7d6489922eb9008d91f09d78b9b16c8c52b034c9f9c9e6e767`)

## dependencies (1 claim(s))

- [observation/documented] The project is installed as an editable package (uv pip install -e .) and uses OpenAI-compatible LLM endpoints configured via API_KEY and BASE_URL environment variables. -- evidence: [README.md#L70-L70](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L70-L70), [README.md#L63-L63](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L63-L63), [README.md#L72-L75](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L72-L75), [README.md#L65-L68](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L65-L68) (`clm_17217cf699bfd38da07d8c907d854bedc2b9988e5c42ea3a24eb4fb4b36a1f8e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

