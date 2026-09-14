---
access: public
aliases: []
claim_ids:
- clm_136be139d93078e7a01a6a3da4340afd8ac1775984948462c464518f733e0261
- clm_2fbca97b9da7abbbdbfff1842c20f3361eaf18397db44760d59072a7e2291891
- clm_3bab233abd5bfce5d559362fcd663fcc102bdc351189e2f0c54bac19294f78b4
- clm_4e2ddcdbd7f515d20e8eda03065f1b7aaa7f47bf30f95f4f8afe97870be2bcfa
- clm_4f8d0980b671bc30ae0fa074f068644e8b893ca12730f6368ec6bb70c3cba0b9
- clm_515b61b28c01e6812634967f1ccbeb0fd8d71c2f79a74584035395d6e6d7dc91
- clm_58ecac9b533fb9cb23ab9c69e876737673c814a7041cc6c063b58809fd54316e
- clm_ecfb844fd722440ca026adccddf7966888d4332354a78d8cee5935bb344eac3b
- clm_f21fc26059000f3bae36d300a3ca2a4c9f2d891a937f157c9ad11552d6d78c26
- clm_f4bd4e999040000f03c5c6adad572761915de4b5be2b26ab519f93c7aab8a303
- clm_ffede67f18689a3bb68db8c95fed03885addb7a11120a43100c4a8e6e3139ae8
maturity: draft
page_id: pg_8a0f18c4a1ba546694256d84793a8e35
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7d6e943246b05207a2c105d196c0044c
title: datacurve-ai/deep-swe/README.md @ 0b9fabbb63b9
updated_at: '2026-09-14T03:45:11Z'
---

# datacurve-ai/deep-swe/README.md @ 0b9fabbb63b9

<!-- rcw:begin owner=source:src_7d6e943246b05207a2c105d196c0044c block=evidence -->
- The benchmark comprises 113 tasks spanning TypeScript, Go, Python, JavaScript, and Rust, with isolated environments and program-based verifiers. [@claim:clm_136be139d93078e7a01a6a3da4340afd8ac1775984948462c464518f733e0261]
- The verifier accepts any solution whose observable behavior is correct, regardless of internal symbol names or structure, and the reference patch is never used at grading time. [@claim:clm_2fbca97b9da7abbbdbfff1842c20f3361eaf18397db44760d59072a7e2291891]
- Pier, a Harbor-compatible eval framework, adds per-agent network allowlists so agents get only needed network access while the task environment stays isolated, unlike Harbor's blanket blocking in no-internet tasks. [@claim:clm_3bab233abd5bfce5d559362fcd663fcc102bdc351189e2f0c54bac19294f78b4]
- Since v1.1, grading uses Harbor's separate verifier environment: the agent works in isolation, commits its work, and a collect hook extracts commits as a patch applied and graded in a pristine container. [@claim:clm_4e2ddcdbd7f515d20e8eda03065f1b7aaa7f47bf30f95f4f8afe97870be2bcfa]
- DeepSWE is a benchmark measuring frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repositories. [@claim:clm_4f8d0980b671bc30ae0fa074f068644e8b893ca12730f6368ec6bb70c3cba0b9]
- Tasks use the Harbor task format, with task.toml metadata, instruction.md, an environment Dockerfile, tests, and a held-out reference solution. [@claim:clm_515b61b28c01e6812634967f1ccbeb0fd8d71c2f79a74584035395d6e6d7dc91]
- Each run produces verifier outputs including reward.json with binary reward and pass fractions, ctrf.json test reports, raw stdout logs, and framework-native grader reports. [@claim:clm_58ecac9b533fb9cb23ab9c69e876737673c814a7041cc6c063b58809fd54316e]
- The benchmark is run via Pier, installed with uv, using commands like 'pier run -p deep-swe/tasks --agent mini-swe-agent' with model-specific API keys exported. [@claim:clm_ecfb844fd722440ca026adccddf7966888d4332354a78d8cee5935bb344eac3b]
- Runs can be subsetted deterministically via --n-tasks with --sample-seed, or targeted at a single task by passing a task-id path to pier run. [@claim:clm_f21fc26059000f3bae36d300a3ca2a4c9f2d891a937f157c9ad11552d6d78c26]
- The separate-verifier grading flow requires the datacurve-pier package at a version newer than 0.3.0. [@claim:clm_f4bd4e999040000f03c5c6adad572761915de4b5be2b26ab519f93c7aab8a303]
- Pier supports multiple agents: mini-swe-agent is model-agnostic, and Pier also drives claude-code, codex, gemini-cli, and opencode; --env modal runs parallel sandboxes on Modal. [@claim:clm_ffede67f18689a3bb68db8c95fed03885addb7a11120a43100c4a8e6e3139ae8]
<!-- rcw:end owner=source:src_7d6e943246b05207a2c105d196c0044c block=evidence -->

## Researcher notes

