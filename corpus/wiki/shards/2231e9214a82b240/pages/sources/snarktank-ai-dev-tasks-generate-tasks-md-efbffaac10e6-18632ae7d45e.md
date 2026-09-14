---
access: public
aliases: []
claim_ids:
- clm_0259ac4a8b17321494274b872e31b2065bbb1ff3ebaa421d756cdd4e38bcf0fe
- clm_17690a95fffef2e79e76785fe8b7a1b3341ee555ab5d7c1aaf19e5a37d083569
- clm_a13a359c65cb376c6f4464dccdb58d9930fdd392f9fd750a2ee6449684e1c3a7
- clm_f0eca526e442a736ecf168125128b199ced8378c3060110191eb3334e24a9607
- clm_fec857fa2fe3686db02e816b9b2188d35ef0759dd6560087c3c11bd461b03c72
maturity: draft
page_id: pg_95d1aafdda955e3c8e8f18632ae7d45e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2daff52f46df51d199cc9e2f8e7750c4
title: snarktank/ai-dev-tasks/generate-tasks.md @ efbffaac10e6
updated_at: '2026-09-14T04:21:57Z'
---

# snarktank/ai-dev-tasks/generate-tasks.md @ efbffaac10e6

<!-- rcw:begin owner=source:src_2daff52f46df51d199cc9e2f8e7750c4 block=evidence -->
- The generated task list must include a 'Relevant Files' section listing files to create or modify, with corresponding test files where applicable. [@claim:clm_0259ac4a8b17321494274b872e31b2065bbb1ff3ebaa421d756cdd4e38bcf0fe]
- Repository development practice: the task-list template tells the implementing agent to run tests with 'npx jest [optional/path/to/test/file]' and to place unit tests alongside the code they test. [@claim:clm_17690a95fffef2e79e76785fe8b7a1b3341ee555ab5d7c1aaf19e5a37d083569]
- generate-tasks.md requires task 0.0 'Create feature branch' as the first task unless the user opts out, and pauses for user confirmation ('Go') before generating sub-tasks. [@claim:clm_a13a359c65cb376c6f4464dccdb58d9930fdd392f9fd750a2ee6449684e1c3a7]
- generate-tasks.md instructs the AI to check off each sub-task in the markdown file by changing '- [ ]' to '- [x]' after completion, updating after each sub-task. [@claim:clm_f0eca526e442a736ecf168125128b199ced8378c3060110191eb3334e24a9607]
- Both prompt files state the PRD and task list are written for a junior developer, requiring explicit, unambiguous, jargon-light requirements. [@claim:clm_fec857fa2fe3686db02e816b9b2188d35ef0759dd6560087c3c11bd461b03c72]
<!-- rcw:end owner=source:src_2daff52f46df51d199cc9e2f8e7750c4 block=evidence -->

## Researcher notes

