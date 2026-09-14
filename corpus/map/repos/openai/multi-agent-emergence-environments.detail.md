# openai/multi-agent-emergence-environments -- full detail

[Back to orientation](multi-agent-emergence-environments.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openai/multi-agent-emergence-environments/bafaf1e11e6398624116761f91ae7c93b136f395/ac080d53ec0aed79.json](../../../wiki/dossiers/openai/multi-agent-emergence-environments/bafaf1e11e6398624116761f91ae7c93b136f395/ac080d53ec0aed79.json)

## specifications (1 claim(s))

- [observation/documented] The repository provides environment generation code accompanying the paper 'Emergent Tool Use From Multi-Agent Autocurricula' and its OpenAI blog post. -- evidence: [README.md#L4-L4](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L4-L4) (`clm_2ff1c9e4eaa09a45f40438652f7487eb3f3530bc5b0f0ceb2c496c3d7c355c77`)

## components (1 claim(s))

- [observation/documented] Defined environments include Hide and Seek (random rooms, quadrant, food variants), Box locking (Lock and Return, Sequential Lock), Blueprint Construction, and Shelter Construction. -- evidence: [README.md#L22-L26](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L22-L26) (`clm_ac82ca8224b13346cfc243ee11ed2dc892d8069ce030a23f59cdb54ae230a169`)

## design-choices (2 claim(s))

- [observation/documented] Environments are built by starting from a Base environment and adding environment modules (e.g. Boxes, Ramps, RandomWalls) plus wrappers on top. -- evidence: [README.md#L18-L18](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L18-L18) (`clm_2b4ce1fcaaa9b325110611aeb45939749b51af055d34921db2081379dce1fe64`)
- [observation/documented] New objects or dynamics should be added via EnvModule classes (objects/sites, simulator changes) or gym.Wrapper classes (rewards, observations, game mechanics like Lock and Grab) rather than subclassing Base. -- evidence: [README.md#L20-L20](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L20-L20) (`clm_bfd55558b2797e345d4754e919f217eae47040b6d3a52a358dfc8681f15957a8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A bin/examine script lets users inspect environments and play saved policies, e.g. passing a jsonnet environment config and an npz policy from the examples folder. -- evidence: [README.md#L31-L31](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L31-L31), [README.md#L28-L29](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L28-L29) (`clm_44440998770eac8ecfb17e491f7078280ce04c6787646665b97b93b7aa49ab2d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The repository depends on the separate mujoco-worldgen package, which must be cloned and installed (with its requirements) before installing this repo in editable mode. -- evidence: [README.md#L7-L12](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L7-L12) (`clm_768c102d8d232c9c3804ff7c37e1faddf1832499f0a5c2eb2f5686b2e00625d3`)
- [observation/documented] Playing saved policies requires extra packages installable via requirements_ma_policy.txt, which pins tensorflow 1.13.1, cloudpickle 0.5.2, baselines 0.1.5, opencv-python, and pytest. -- evidence: [requirements_ma_policy.txt#L1-L5](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/requirements_ma_policy.txt#L1-L5), [README.md#L35-L35](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L35-L35), [README.md#L33-L33](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L33-L33) (`clm_20c34998ce0fbaefa797a2ea97d5b5af26bdc1bd787828918d29490259ecdb51`)

## limitations (2 claim(s))

- [observation/documented] The project is archived: code is provided as-is with no updates expected. -- evidence: [README.md#L1-L1](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L1-L1) (`clm_a8a9c847d6a89d12be9b453d73911c6e7b5127902ff84e334dd09a1023878449`)
- [observation/documented] The repository has been tested only on Mac OS X and Ubuntu 16.04 with Python 3.6. -- evidence: [README.md#L14-L14](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L14-L14) (`clm_db6412a692275e87d37a9a8400d6929cf9aecf2d8f45e48a26f5d0ced59ffd9b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

