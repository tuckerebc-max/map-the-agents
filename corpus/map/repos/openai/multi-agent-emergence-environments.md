# openai/multi-agent-emergence-environments

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bafaf1e11e63 @ ac080d53ec0aed79

## Summary (orientation draft, not independently verified)

The snapshot documents OpenAI's multi-agent emergence environments: MuJoCo-based environment generation code for the Emergent Tool Use paper, archived as-is, with several named environments and an examine tool. Evidence is mostly README-level; no runtime agent behavior beyond environment construction is documented.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository provides environment generation code accompanying the paper 'Emergent Tool Use From Multi-Agent Autocurricula' and its OpenAI blog post. -- evidence: [README.md#L4-L4](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L4-L4)
- components (1 claim(s)):
  - [observation/documented] Defined environments include Hide and Seek (random rooms, quadrant, food variants), Box locking (Lock and Return, Sequential Lock), Blueprint Construction, and Shelter Construction. -- evidence: [README.md#L22-L26](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L22-L26)
- design-choices (2 claim(s)):
  - [observation/documented] Environments are built by starting from a Base environment and adding environment modules (e.g. Boxes, Ramps, RandomWalls) plus wrappers on top. -- evidence: [README.md#L18-L18](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L18-L18)
  - [observation/documented] New objects or dynamics should be added via EnvModule classes (objects/sites, simulator changes) or gym.Wrapper classes (rewards, observations, game mechanics like Lock and Grab) rather than subclassing Base. -- evidence: [README.md#L20-L20](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L20-L20)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A bin/examine script lets users inspect environments and play saved policies, e.g. passing a jsonnet environment config and an npz policy from the examples folder. -- evidence: [README.md#L31-L31](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L31-L31), [README.md#L28-L29](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L28-L29)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The repository depends on the separate mujoco-worldgen package, which must be cloned and installed (with its requirements) before installing this repo in editable mode. -- evidence: [README.md#L7-L12](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L7-L12)
  - [observation/documented] Playing saved policies requires extra packages installable via requirements_ma_policy.txt, which pins tensorflow 1.13.1, cloudpickle 0.5.2, baselines 0.1.5, opencv-python, and pytest. -- evidence: [requirements_ma_policy.txt#L1-L5](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/requirements_ma_policy.txt#L1-L5), [README.md#L35-L35](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L35-L35), [README.md#L33-L33](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L33-L33)
- limitations (2 claim(s)):
  - [observation/documented] The project is archived: code is provided as-is with no updates expected. -- evidence: [README.md#L1-L1](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L1-L1)
  - [observation/documented] The repository has been tested only on Mac OS X and Ubuntu 16.04 with Python 3.6. -- evidence: [README.md#L14-L14](https://github.com/openai/multi-agent-emergence-environments/blob/bafaf1e11e6398624116761f91ae7c93b136f395/README.md#L14-L14)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](multi-agent-emergence-environments.detail.md).

Metadata and full claim list: [full detail](multi-agent-emergence-environments.detail.md)
Human notes ([notes](multi-agent-emergence-environments.notes.md), never overwritten by build)

[Back to map index](../../index.md)
