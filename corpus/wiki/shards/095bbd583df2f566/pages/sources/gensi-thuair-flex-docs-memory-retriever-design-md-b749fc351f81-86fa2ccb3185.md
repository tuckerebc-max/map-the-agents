---
access: public
aliases: []
claim_ids:
- clm_3e91a69bfd6979c28cacf1312f36439b4dbce91ec0da21a77663910322b3ff1d
- clm_437e55d386afe831d23a86b47988825b88e06ab8f4d26fe6f15e1fb83131e0a7
- clm_525c59aa3d1930d4679511584bfc72bd6de27498e72aac9b48a5e97fac8767e6
- clm_6033c9341e04ed26b98d86dd309d4f498e8001edd480496d2e883e08e871e3d8
- clm_838ad953422c2926dc31fe65a39fd4f6a9ab9e85177d5a478f6ed8ab0e974c26
maturity: draft
page_id: pg_5970ef7a015f5da3b98486fa2ccb3185
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bbd45fcdbeee5d7e80256fff9e4915c2
title: GenSI-THUAIR/FLEX/docs/memory_retriever_design.md @ b749fc351f81
updated_at: '2026-09-14T04:43:20Z'
---

# GenSI-THUAIR/FLEX/docs/memory_retriever_design.md @ b749fc351f81

<!-- rcw:begin owner=source:src_bbd45fcdbeee5d7e80256fff9e4915c2 block=evidence -->
- The retriever exposes multi-level abstraction tools (get_partition_methods, get_partition_rules, get_partition_trajectories), state tools, get_memory_statistics, and a final_answer tool for the actor. [@claim:clm_3e91a69bfd6979c28cacf1312f36439b4dbce91ec0da21a77663910322b3ff1d]
- The memory retriever design prioritizes exhaustive exploration over efficiency, and keeps tools limited to data retrieval while the agent performs semantic analysis and response generation. [@claim:clm_437e55d386afe831d23a86b47988825b88e06ab8f4d26fe6f15e1fb83131e0a7]
- Each memory entry stores a method description, rules with examples, a revised trajectory with comments, and metadata such as memory_type, problem_category, priority, and timestamps. [@claim:clm_525c59aa3d1930d4679511584bfc72bd6de27498e72aac9b48a5e97fac8767e6]
- The retriever agent maintains per-partition exploration state (explored_up_to and recommended_indices) to avoid redundant exploration and support multi-turn continuity. [@claim:clm_6033c9341e04ed26b98d86dd309d4f498e8001edd480496d2e883e08e871e3d8]
- The memory library is partitioned into Golden (successful experiences), Warning (failure cases), and Mixed (learning trajectories) partitions. [@claim:clm_838ad953422c2926dc31fe65a39fd4f6a9ab9e85177d5a478f6ed8ab0e974c26]
<!-- rcw:end owner=source:src_bbd45fcdbeee5d7e80256fff9e4915c2 block=evidence -->

## Researcher notes

