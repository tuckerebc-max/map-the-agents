---
access: public
aliases: []
claim_ids:
- clm_00c534d9a19f30c0aeb36b258579b173bd2750877bf9deeee2b3023b615875ed
- clm_2b5b9d02bf71631cf3e0ece14eaf3a1bc356c5e0512ea8f5f66ed92bc82b2674
- clm_4671d0338deb3388a32eccf75e4677a78c6184b9900e8efe1237c2ac61d9d3c0
- clm_60304b7fe55ae495e4887467f3bae786d43986fb0c3ac526a774a489d8af1a71
- clm_91847c08b29c3888c967faee8796c4e7421eaaf3eb5ea232b31cf6af747718a7
- clm_a5860cc1cd80681c39ff1ab13cc4e9adcbc85ed48aeb96025dbe482d9d33d489
- clm_cf059549e5d7d1524f164073af267f0d6342b4cde38de156abe48924f8fd9cee
maturity: draft
page_id: pg_0803c10ccdd95668a670a3da76e86936
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2af848924fdb599ba9393c4e4579d053
title: SWE-bench/SWE-smith/README.md @ 9b74ac08118a
updated_at: '2026-09-14T04:24:25Z'
---

# SWE-bench/SWE-smith/README.md @ 9b74ac08118a

<!-- rcw:begin owner=source:src_2af848924fdb599ba9393c4e4579d053 block=evidence -->
- The package exposes a Python API: a repo profile registry can fetch a RepoProfile from a task instance and obtain a Docker container with the task initialized. [@claim:clm_00c534d9a19f30c0aeb36b258579b173bd2750877bf9deeee2b3023b615875ed]
- Creating execution environments requires Docker; the project was developed and tested on Ubuntu 22.04.4 LTS, and Windows or MacOS support is not planned. [@claim:clm_2b5b9d02bf71631cf3e0ece14eaf3a1bc356c5e0512ea8f5f66ed92bc82b2674]
- The fine-tuned SWE-agent-LM-32B reportedly achieves 40.2% pass@1 on SWE-bench Verified, and the README claims a 32% jump from fine-tuning Qwen 2.5 Coder with SWE-agent. [@claim:clm_4671d0338deb3388a32eccf75e4677a78c6184b9900e8efe1237c2ac61d9d3c0]
- The documented pipeline for building a dataset is: create an environment, synthesize task instances, keep tasks that break one or more unit tests, then generate issue text for the tasks. [@claim:clm_60304b7fe55ae495e4887467f3bae786d43986fb0c3ac526a774a489d8af1a71]
- SWE-smith is described as a toolkit for training SWE-agents that can turn any GitHub repository into a SWE-gym and create tasks such as file localization and program repair. [@claim:clm_91847c08b29c3888c967faee8796c4e7421eaaf3eb5ea232b31cf6af747718a7]
- Repository development practice: contributors are asked to additionally run 'pre-commit install' after setup, and a Contributing Guide is referenced for further details. [@claim:clm_a5860cc1cd80681c39ff1ab13cc4e9adcbc85ed48aeb96025dbe482d9d33d489]
- The README badge indicates Python 3.10+ is required, and the project is MIT licensed. [@claim:clm_cf059549e5d7d1524f164073af267f0d6342b4cde38de156abe48924f8fd9cee]
<!-- rcw:end owner=source:src_2af848924fdb599ba9393c4e4579d053 block=evidence -->

## Researcher notes

