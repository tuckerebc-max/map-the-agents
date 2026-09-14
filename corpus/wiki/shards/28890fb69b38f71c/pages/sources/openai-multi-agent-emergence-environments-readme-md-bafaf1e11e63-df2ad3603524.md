---
access: public
aliases: []
claim_ids:
- clm_20c34998ce0fbaefa797a2ea97d5b5af26bdc1bd787828918d29490259ecdb51
- clm_2b4ce1fcaaa9b325110611aeb45939749b51af055d34921db2081379dce1fe64
- clm_2ff1c9e4eaa09a45f40438652f7487eb3f3530bc5b0f0ceb2c496c3d7c355c77
- clm_44440998770eac8ecfb17e491f7078280ce04c6787646665b97b93b7aa49ab2d
- clm_768c102d8d232c9c3804ff7c37e1faddf1832499f0a5c2eb2f5686b2e00625d3
- clm_a8a9c847d6a89d12be9b453d73911c6e7b5127902ff84e334dd09a1023878449
- clm_ac82ca8224b13346cfc243ee11ed2dc892d8069ce030a23f59cdb54ae230a169
- clm_bfd55558b2797e345d4754e919f217eae47040b6d3a52a358dfc8681f15957a8
- clm_db6412a692275e87d37a9a8400d6929cf9aecf2d8f45e48a26f5d0ced59ffd9b
maturity: draft
page_id: pg_4f352ec00b7154a4b2f2df2ad3603524
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c2910ef2b5675a43909e6ba441d0c1f6
title: openai/multi-agent-emergence-environments/README.md @ bafaf1e11e63
updated_at: '2026-09-14T04:13:58Z'
---

# openai/multi-agent-emergence-environments/README.md @ bafaf1e11e63

<!-- rcw:begin owner=source:src_c2910ef2b5675a43909e6ba441d0c1f6 block=evidence -->
- Playing saved policies requires extra packages installable via requirements_ma_policy.txt, which pins tensorflow 1.13.1, cloudpickle 0.5.2, baselines 0.1.5, opencv-python, and pytest. [@claim:clm_20c34998ce0fbaefa797a2ea97d5b5af26bdc1bd787828918d29490259ecdb51]
- Environments are built by starting from a Base environment and adding environment modules (e.g. Boxes, Ramps, RandomWalls) plus wrappers on top. [@claim:clm_2b4ce1fcaaa9b325110611aeb45939749b51af055d34921db2081379dce1fe64]
- The repository provides environment generation code accompanying the paper 'Emergent Tool Use From Multi-Agent Autocurricula' and its OpenAI blog post. [@claim:clm_2ff1c9e4eaa09a45f40438652f7487eb3f3530bc5b0f0ceb2c496c3d7c355c77]
- A bin/examine script lets users inspect environments and play saved policies, e.g. passing a jsonnet environment config and an npz policy from the examples folder. [@claim:clm_44440998770eac8ecfb17e491f7078280ce04c6787646665b97b93b7aa49ab2d]
- The repository depends on the separate mujoco-worldgen package, which must be cloned and installed (with its requirements) before installing this repo in editable mode. [@claim:clm_768c102d8d232c9c3804ff7c37e1faddf1832499f0a5c2eb2f5686b2e00625d3]
- The project is archived: code is provided as-is with no updates expected. [@claim:clm_a8a9c847d6a89d12be9b453d73911c6e7b5127902ff84e334dd09a1023878449]
- Defined environments include Hide and Seek (random rooms, quadrant, food variants), Box locking (Lock and Return, Sequential Lock), Blueprint Construction, and Shelter Construction. [@claim:clm_ac82ca8224b13346cfc243ee11ed2dc892d8069ce030a23f59cdb54ae230a169]
- New objects or dynamics should be added via EnvModule classes (objects/sites, simulator changes) or gym.Wrapper classes (rewards, observations, game mechanics like Lock and Grab) rather than subclassing Base. [@claim:clm_bfd55558b2797e345d4754e919f217eae47040b6d3a52a358dfc8681f15957a8]
- The repository has been tested only on Mac OS X and Ubuntu 16.04 with Python 3.6. [@claim:clm_db6412a692275e87d37a9a8400d6929cf9aecf2d8f45e48a26f5d0ced59ffd9b]
<!-- rcw:end owner=source:src_c2910ef2b5675a43909e6ba441d0c1f6 block=evidence -->

## Researcher notes

