# praveen-palanisamy/macad-gym

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1006e849ff4c @ 438be4c3b960c4e2

## Summary (orientation draft, not independently verified)

MACAD-Gym is an OpenAI Gym-compatible multi-agent driving training platform built on CARLA 0.9.x, with pip-installable package, versioned environment IDs, and a documented setup/usage workflow.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MACAD-Gym is a training platform for Multi-Agent Connected Autonomous Driving built on top of the CARLA simulator. -- evidence: [README.md#L1-L3](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L1-L3)
- components (1 claim(s)):
  - [observation/documented] The docs reference a MultiCarlaEnv class in macad_gym.carla.multi_env as a core environment component. -- evidence: [docs/index.rst#L16-L17](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/docs/index.rst#L16-L17)
- design-choices (3 claim(s)):
  - [observation/documented] Environment IDs follow a naming convention encoding scenario attributes (homogeneous/heterogeneous, communicating, observability) to support versioned benchmarking of agent algorithms. -- evidence: [README.md#L86-L93](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L86-L93)
  - [observation/documented] New environments and scenarios can be added using a simple, JSON-like configuration. -- evidence: [README.md#L5-L8](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L5-L8)
- workflows (3 claim(s)):
  - [observation/documented] Installation is via pip install macad-gym, or a developer path cloning the repo, creating a conda env from conda_env.yml, and pip install -e . -- evidence: [README.md#L15-L17](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L15-L17), [README.md#L69-L81](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L69-L81)
  - [observation/documented] Environments can be test-driven directly, e.g. python -m macad_gym.envs.homo.ncom.inde.po.intrx.ma.stop_sign_3c_town03. -- evidence: [README.md#L33-L33](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L33-L33), [README.md#L35-L37](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L35-L37)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Environments follow the OpenAI Gym interface; users create them via gym.make with IDs like HomoNcomIndePOIntrxMASS3CTWN3-v0. -- evidence: [README.md#L100-L102](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L100-L102), [README.md#L5-L8](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L5-L8), [README.md#L104-L108](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L104-L108)
  - [observation/documented] Observation and action spaces are Gym Dict spaces keyed per actor, e.g. per-car Box(168,168,3) observations and Discrete(9) actions. -- evidence: [README.md#L113-L118](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L113-L118)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The platform targets CARLA 0.9.x and above; setup uses CARLA 0.9.13 with the matching carla PyPI client package, plus Miniconda, cmake, and zlib. -- evidence: [README.md#L53-L58](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L53-L58), [README.md#L221-L223](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L221-L223), [README.md#L60-L60](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L60-L60), [README.md#L69-L81](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L69-L81), [README.md#L64-L65](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L64-L65)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](macad-gym.detail.md) for every claim.)

Metadata and full claim list: [full detail](macad-gym.detail.md)
Human notes ([notes](macad-gym.notes.md), never overwritten by build)

[Back to map index](../../index.md)
