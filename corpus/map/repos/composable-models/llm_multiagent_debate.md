# composable-models/llm_multiagent_debate

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9846749350eb @ 999fcd98f0a463c8

## Summary (orientation draft, not independently verified)

A preliminary implementation of the paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', providing generation and evaluation scripts for four benchmark tasks (math, GSM, biographies, MMLU) with pinned Python dependencies.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository is described as a preliminary implementation of the paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', with more tasks and settings to be released. -- evidence: [README.md#L11-L12](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L11-L12)
- components (1 claim(s)):
  - [observation/documented] The repo contains four task subfolders: ./math, ./gsm, ./biography, and ./mmlu, each holding code for running its respective task. -- evidence: [README.md#L18-L18](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L18-L18), [README.md#L20-L23](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L20-L23)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Each task is run via a generation script (e.g. gen_math.py, gen_gsm.py, gen_conversation.py, gen_mmlu.py) executed from its task directory. -- evidence: [README.md#L51-L52](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L51-L52), [README.md#L43-L44](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L43-L44), [README.md#L27-L28](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L27-L28), [README.md#L32-L33](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L32-L33)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Separate evaluation scripts exist per task: eval_gsm.py, eval_conversation.py, and eval_mmlu.py evaluate the generated results of GSM, biography, and MMLU problems respectively. -- evidence: [README.md#L54-L55](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L54-L55), [README.md#L35-L36](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L35-L36), [README.md#L46-L47](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L46-L47)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt pins numpy 1.22.4, openai 0.27.6, pandas 1.5.3, and tqdm 4.64.1. -- evidence: [requirements.txt#L1-L4](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/requirements.txt#L1-L4)
  - [inference/documented] The pinned openai 0.27.6 package suggests the code calls OpenAI models via the OpenAI Python client. -- evidence: [requirements.txt#L1-L4](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/requirements.txt#L1-L4)
- limitations (1 claim(s)):
  - [observation/documented] The README notes this is a preliminary implementation and that additional debate logs are hosted externally on Dropbox. -- evidence: [README.md#L11-L12](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L11-L12)
- relevance (2 claim(s)):
  - [observation/documented] The GSM and MMLU datasets are external, with links to the openai/grade-school-math and hendrycks/test repositories for download. -- evidence: [README.md#L38-L38](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L38-L38), [README.md#L57-L57](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L57-L57)
  - [observation/documented] The work is associated with authors Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch, with a project page and arXiv paper (2305.14325). -- evidence: [README.md#L59-L67](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L59-L67), [README.md#L5-L9](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L5-L9)

Every claim for this repository is shown above and in [full detail](llm_multiagent_debate.detail.md).

Metadata and full claim list: [full detail](llm_multiagent_debate.detail.md)
Human notes ([notes](llm_multiagent_debate.notes.md), never overwritten by build)

[Back to map index](../../index.md)
