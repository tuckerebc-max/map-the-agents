# praveen-palanisamy/macad-gym -- full detail

[Back to orientation](macad-gym.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/praveen-palanisamy/macad-gym/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/438be4c3b960c4e2.json](../../../wiki/dossiers/praveen-palanisamy/macad-gym/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/438be4c3b960c4e2.json)

## specifications (1 claim(s))

- [observation/documented] MACAD-Gym is a training platform for Multi-Agent Connected Autonomous Driving built on top of the CARLA simulator. -- evidence: [README.md#L1-L3](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L1-L3) (`clm_fc3641430169b2fee1fdeb43768089189acc9ef18e0c635d3a73d70a4b521ad0`)

## components (1 claim(s))

- [observation/documented] The docs reference a MultiCarlaEnv class in macad_gym.carla.multi_env as a core environment component. -- evidence: [docs/index.rst#L16-L17](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/docs/index.rst#L16-L17) (`clm_89b56def8816c814378301d3de3fa0173225ef9894e150b7fca94124f2b42993`)

## design-choices (3 claim(s))

- [observation/documented] Environment IDs follow a naming convention encoding scenario attributes (homogeneous/heterogeneous, communicating, observability) to support versioned benchmarking of agent algorithms. -- evidence: [README.md#L86-L93](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L86-L93) (`clm_a7e3bb51506e55a8110398dd58793c68480b388e793c83b1348a92bfbbcdc69f`)
- [observation/documented] New environments and scenarios can be added using a simple, JSON-like configuration. -- evidence: [README.md#L5-L8](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L5-L8) (`clm_d48e87f1b78a13e86ccc9d74ca9876a8b624bf4f4c491af0908fb74766d22d99`)
- [observation/documented] MACAD-Gym supports multi-GPU setups and selects the least-loaded GPU to launch the simulation for RL training environments. -- evidence: [README.md#L219-L219](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L219-L219) (`clm_639fee8d29cc91f3716e143a920ac98639a6c9aaba723f74c4be8e3ef5c98b40`)

## workflows (3 claim(s))

- [observation/documented] Installation is via pip install macad-gym, or a developer path cloning the repo, creating a conda env from conda_env.yml, and pip install -e . -- evidence: [README.md#L15-L17](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L15-L17), [README.md#L69-L81](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L69-L81) (`clm_24bb1962300d8767cf291b952a612b3f72a77eaafe1b66468286d9be5e83e6b1`)
- [observation/documented] Environments can be test-driven directly, e.g. python -m macad_gym.envs.homo.ncom.inde.po.intrx.ma.stop_sign_3c_town03. -- evidence: [README.md#L33-L33](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L33-L33), [README.md#L35-L37](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L35-L37) (`clm_6c92abeead458afc88c4fe9a67aeff098f978efc91d11af3edcd14948e57b4e7`)
- [observation/documented] Repository development practice: contributors must activate the macad-gym conda env, follow PEP8/Google style, run bash .ci/format_code.sh before pushing, and ensure CI passes. -- evidence: [CONTRIBUTING.md#L3-L11](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/CONTRIBUTING.md#L3-L11) (`clm_e4e278811cdd717969e7a30d888e589ea2e1ad49c151c19f9dba2813b8072df1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Environments follow the OpenAI Gym interface; users create them via gym.make with IDs like HomoNcomIndePOIntrxMASS3CTWN3-v0. -- evidence: [README.md#L100-L102](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L100-L102), [README.md#L5-L8](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L5-L8), [README.md#L104-L108](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L104-L108) (`clm_038a2c8020f7466a81b19c6e0ec1409d8a36801cbc7908d8a8788487683a67c0`)
- [observation/documented] Observation and action spaces are Gym Dict spaces keyed per actor, e.g. per-car Box(168,168,3) observations and Discrete(9) actions. -- evidence: [README.md#L113-L118](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L113-L118) (`clm_e7af349c52fd1c11f0c39b7ffcd04ccb13411eed96df98a23b9d1483682a0837`)
- [observation/documented] macad_gym.list_available_envs() prints available environments with short descriptions, such as two intersection scenarios in Town3. -- evidence: [README.md#L123-L128](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L123-L128), [README.md#L120-L121](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L120-L121), [README.md#L130-L142](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L130-L142) (`clm_c1dde8b6cccbf84ec01aa324597df2485fd33f5d236153a573647b1310747930`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The platform targets CARLA 0.9.x and above; setup uses CARLA 0.9.13 with the matching carla PyPI client package, plus Miniconda, cmake, and zlib. -- evidence: [README.md#L53-L58](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L53-L58), [README.md#L221-L223](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L221-L223), [README.md#L60-L60](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L60-L60), [README.md#L69-L81](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L69-L81), [README.md#L64-L65](https://github.com/praveen-palanisamy/macad-gym/blob/1006e849ff4c5bf5d29cb43ab8c2a0bdcc992367/README.md#L64-L65) (`clm_fdeffb0be8c30f704c45bb7dc7b82a5464458a58b6e9489db8eb11c8018196a4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

