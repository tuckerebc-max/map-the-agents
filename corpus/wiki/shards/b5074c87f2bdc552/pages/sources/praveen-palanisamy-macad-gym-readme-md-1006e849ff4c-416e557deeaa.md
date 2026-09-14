---
access: public
aliases: []
claim_ids:
- clm_038a2c8020f7466a81b19c6e0ec1409d8a36801cbc7908d8a8788487683a67c0
- clm_24bb1962300d8767cf291b952a612b3f72a77eaafe1b66468286d9be5e83e6b1
- clm_639fee8d29cc91f3716e143a920ac98639a6c9aaba723f74c4be8e3ef5c98b40
- clm_6c92abeead458afc88c4fe9a67aeff098f978efc91d11af3edcd14948e57b4e7
- clm_a7e3bb51506e55a8110398dd58793c68480b388e793c83b1348a92bfbbcdc69f
- clm_c1dde8b6cccbf84ec01aa324597df2485fd33f5d236153a573647b1310747930
- clm_d48e87f1b78a13e86ccc9d74ca9876a8b624bf4f4c491af0908fb74766d22d99
- clm_e7af349c52fd1c11f0c39b7ffcd04ccb13411eed96df98a23b9d1483682a0837
- clm_fc3641430169b2fee1fdeb43768089189acc9ef18e0c635d3a73d70a4b521ad0
- clm_fdeffb0be8c30f704c45bb7dc7b82a5464458a58b6e9489db8eb11c8018196a4
maturity: draft
page_id: pg_7ce51cb0daf95d5bac66416e557deeaa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_865c5e1b832252d0b2f15e710ddb0a4f
title: praveen-palanisamy/macad-gym/README.md @ 1006e849ff4c
updated_at: '2026-09-14T04:16:18Z'
---

# praveen-palanisamy/macad-gym/README.md @ 1006e849ff4c

<!-- rcw:begin owner=source:src_865c5e1b832252d0b2f15e710ddb0a4f block=evidence -->
- Environments follow the OpenAI Gym interface; users create them via gym.make with IDs like HomoNcomIndePOIntrxMASS3CTWN3-v0. [@claim:clm_038a2c8020f7466a81b19c6e0ec1409d8a36801cbc7908d8a8788487683a67c0]
- Installation is via pip install macad-gym, or a developer path cloning the repo, creating a conda env from conda_env.yml, and pip install -e . [@claim:clm_24bb1962300d8767cf291b952a612b3f72a77eaafe1b66468286d9be5e83e6b1]
- MACAD-Gym supports multi-GPU setups and selects the least-loaded GPU to launch the simulation for RL training environments. [@claim:clm_639fee8d29cc91f3716e143a920ac98639a6c9aaba723f74c4be8e3ef5c98b40]
- Environments can be test-driven directly, e.g. python -m macad_gym.envs.homo.ncom.inde.po.intrx.ma.stop_sign_3c_town03. [@claim:clm_6c92abeead458afc88c4fe9a67aeff098f978efc91d11af3edcd14948e57b4e7]
- Environment IDs follow a naming convention encoding scenario attributes (homogeneous/heterogeneous, communicating, observability) to support versioned benchmarking of agent algorithms. [@claim:clm_a7e3bb51506e55a8110398dd58793c68480b388e793c83b1348a92bfbbcdc69f]
- macad_gym.list_available_envs() prints available environments with short descriptions, such as two intersection scenarios in Town3. [@claim:clm_c1dde8b6cccbf84ec01aa324597df2485fd33f5d236153a573647b1310747930]
- New environments and scenarios can be added using a simple, JSON-like configuration. [@claim:clm_d48e87f1b78a13e86ccc9d74ca9876a8b624bf4f4c491af0908fb74766d22d99]
- Observation and action spaces are Gym Dict spaces keyed per actor, e.g. per-car Box(168,168,3) observations and Discrete(9) actions. [@claim:clm_e7af349c52fd1c11f0c39b7ffcd04ccb13411eed96df98a23b9d1483682a0837]
- MACAD-Gym is a training platform for Multi-Agent Connected Autonomous Driving built on top of the CARLA simulator. [@claim:clm_fc3641430169b2fee1fdeb43768089189acc9ef18e0c635d3a73d70a4b521ad0]
- The platform targets CARLA 0.9.x and above; setup uses CARLA 0.9.13 with the matching carla PyPI client package, plus Miniconda, cmake, and zlib. [@claim:clm_fdeffb0be8c30f704c45bb7dc7b82a5464458a58b6e9489db8eb11c8018196a4]
<!-- rcw:end owner=source:src_865c5e1b832252d0b2f15e710ddb0a4f block=evidence -->

## Researcher notes

