# gensi-thuair/flex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b749fc351f81 @ c67fc1de393d9761

## Summary (orientation draft, not independently verified)

FLEX is a research codebase for experience-library-based agent learning, with a reject-sampling training pipeline and evaluation scripts for AIME25 and USPTO-50k. A design doc details a partitioned memory retriever agent with exploration-state tools. Evidence coverage: 164 of 251 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] FLEX (Forward Learning from Experience) is a learning paradigm that shifts learning from modifying model parameters to building and leveraging an evolvable experience library. -- evidence: [README.md#L37-L38](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L37-L38)
- components (1 claim(s)):
  - [observation/documented] Core modules include actor.py (task-solving agent), critic.py (experience extraction), explib.py (library abstraction), updater.py (dedup/acceptance), memory_retriever.py, and rate_limiter.py. -- evidence: [README.md#L273-L278](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L273-L278)
- design-choices (1 claim(s)):
  - [observation/documented] The memory retriever design prioritizes exhaustive exploration over efficiency, and keeps tools limited to data retrieval while the agent performs semantic analysis and response generation. -- evidence: [docs/memory_retriever_design.md#L10-L12](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L10-L12), [docs/memory_retriever_design.md#L15-L17](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L15-L17), [docs/memory_retriever_design.md#L5-L5](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L5-L5), [docs/memory_retriever_design.md#L62-L64](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L62-L64)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] test_flex.py exposes CLI flags including --task_type (math/retro), --actor, --memory_path, --split, --samples, --batch_size, --no-retrieve for ablation, --pass_at_n, and --no-telemetry. -- evidence: [README.md#L251-L263](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L251-L263)
  - [observation/documented] The retriever exposes multi-level abstraction tools (get_partition_methods, get_partition_rules, get_partition_trajectories), state tools, get_memory_statistics, and a final_answer tool for the actor. -- evidence: [docs/memory_retriever_design.md#L609-L617](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L609-L617), [docs/memory_retriever_design.md#L604-L607](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L604-L607), [docs/memory_retriever_design.md#L593-L597](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L593-L597), [docs/memory_retriever_design.md#L626-L629](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L626-L629), [docs/memory_retriever_design.md#L631-L634](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L631-L634), [docs/memory_retriever_design.md#L599-L602](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L599-L602)
- memory-state (3 claim(s)):
  - [observation/documented] The memory library is partitioned into Golden (successful experiences), Warning (failure cases), and Mixed (learning trajectories) partitions. -- evidence: [docs/memory_retriever_design.md#L564-L567](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L564-L567), [docs/memory_retriever_design.md#L559-L562](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L559-L562), [docs/memory_retriever_design.md#L32-L37](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L32-L37), [docs/memory_retriever_design.md#L554-L557](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L554-L557)
  - [observation/documented] Each memory entry stores a method description, rules with examples, a revised trajectory with comments, and metadata such as memory_type, problem_category, priority, and timestamps. -- evidence: [docs/memory_retriever_design.md#L571-L589](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L571-L589), [docs/memory_retriever_design.md#L40-L57](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/docs/memory_retriever_design.md#L40-L57)
- orchestration (1 claim(s)):
  - [observation/documented] Training via reject_sampling.py runs a multi-round loop: an actor attempts the task, a verifier LLM decides continue/stop, a critic extracts experiences, and an updater writes accepted entries into the experience library JSON. -- evidence: [README.md#L106-L109](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L106-L109)
- tools-permissions (1 claim(s)):
  - [observation/documented] In FLEX evaluation, the experience library is wrapped via create_memory_retrieval_tool into a tool the Actor can call during reasoning when retrieval is enabled. -- evidence: [README.md#L218-L221](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L218-L221), [README.md#L267-L269](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L267-L269)
- evaluation (1 claim(s)):
  - [observation/documented] The paper reports experiments on AIME25, USPTO-50k retrosynthesis, and ProteinGym, with improvements such as 40% to 63% on AIME25 and 20% to 30% on USPTO50k. -- evidence: [README.md#L40-L40](https://github.com/GenSI-THUAIR/FLEX/blob/b749fc351f81d834b71edb13bc7bc0e51cfdc15d/README.md#L40-L40)
- dependencies (1 claim(s)):
More evidence: [full detail](flex.detail.md)

Metadata and full claim list: [full detail](flex.detail.md)
Human notes ([notes](flex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
