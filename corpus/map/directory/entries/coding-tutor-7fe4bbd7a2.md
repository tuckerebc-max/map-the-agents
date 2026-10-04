# Coding-Tutor (`coding-tutor`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: iwangjian
- License: Apache-2.0
- Language: Python
- Interface: install=conda create -n coding-tutor python=3.10, pip install -r requirements.txt
- Model providers: Azure, open-weight backbone models
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [iwangjian/coding-tutor](../../repos/iwangjian/coding-tutor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Research project (ACL 2025 Findings paper) proposing Trace-and-Verify (Traver), an agent workflow combining knowledge tracing and turn-by-turn verification for LLM task-tutoring agents using coding tutoring as a scenario; introduces DICT (Dialogue for Coding Tutoring), a novel evaluation protocol combining student simulation and coding tests. Not a production coding agent harness.

(captured site page body (agents/coding-tutor.md), not a verified repo-code finding)
LLM tutors that teach programming lack a way to measure whether their teaching actually works, and dialogue quality metrics do not capture learning. This project, the research code for an ACL 2025 Findings paper, proposes Traver (Trace-and-Verify): a tutoring agent workflow that traces what the student knows and verifies turn by turn whether the dialogue is helping, using a trained verifier model released as a 7B checkpoint on Hugging Face. The accompanying DICT protocol evaluates tutoring agents by simulating students, running the tutoring dialogue, and scoring pre/post coding tests against the EvoCodeBench benchmark. The repository includes dialogue simulation, verifier training scripts, and evaluation pipelines. Researchers studying LLM-based tutoring and education use it; it is not a tool for developers writing production software.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/coding-tutor.md)
