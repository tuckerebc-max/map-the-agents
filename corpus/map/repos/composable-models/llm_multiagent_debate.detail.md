# composable-models/llm_multiagent_debate -- full detail

[Back to orientation](llm_multiagent_debate.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/composable-models/llm_multiagent_debate/9846749350eb917ae5bfaaff4c645fc705b8d3af/999fcd98f0a463c8.json](../../../wiki/dossiers/composable-models/llm_multiagent_debate/9846749350eb917ae5bfaaff4c645fc705b8d3af/999fcd98f0a463c8.json)

## specifications (1 claim(s))

- [observation/documented] The repository is described as a preliminary implementation of the paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', with more tasks and settings to be released. -- evidence: [README.md#L11-L12](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L11-L12) (`clm_a4e6c19ef2d944ad051d237165fc9443e7f4ebb8e6e326fefc1ca43546b84790`)

## components (1 claim(s))

- [observation/documented] The repo contains four task subfolders: ./math, ./gsm, ./biography, and ./mmlu, each holding code for running its respective task. -- evidence: [README.md#L18-L18](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L18-L18), [README.md#L20-L23](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L20-L23) (`clm_89f602a850c2b4130f53212036cad093da57506ce8adee6811212e4b4824f014`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Each task is run via a generation script (e.g. gen_math.py, gen_gsm.py, gen_conversation.py, gen_mmlu.py) executed from its task directory. -- evidence: [README.md#L51-L52](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L51-L52), [README.md#L43-L44](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L43-L44), [README.md#L27-L28](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L27-L28), [README.md#L32-L33](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L32-L33) (`clm_22444835d11faf8ffb8f19dda5ba5f8748177023a40395279ec1b3be33c0236a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Separate evaluation scripts exist per task: eval_gsm.py, eval_conversation.py, and eval_mmlu.py evaluate the generated results of GSM, biography, and MMLU problems respectively. -- evidence: [README.md#L54-L55](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L54-L55), [README.md#L35-L36](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L35-L36), [README.md#L46-L47](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L46-L47) (`clm_cdde99fe7d15a7a5e7ffe04ab793464378d2c2ea3e02af6a0ca1b2028d8d525f`)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt pins numpy 1.22.4, openai 0.27.6, pandas 1.5.3, and tqdm 4.64.1. -- evidence: [requirements.txt#L1-L4](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/requirements.txt#L1-L4) (`clm_e6b5cc6261313aee7520a2da63819a180831905d5ac13f4864933e25c037bcb7`)
- [inference/documented] The pinned openai 0.27.6 package suggests the code calls OpenAI models via the OpenAI Python client. -- evidence: [requirements.txt#L1-L4](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/requirements.txt#L1-L4) (`clm_20dc6ae33487f2d955f6f976e47908473003e85e5a44b714bec2a087582a8136`)

## limitations (1 claim(s))

- [observation/documented] The README notes this is a preliminary implementation and that additional debate logs are hosted externally on Dropbox. -- evidence: [README.md#L11-L12](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L11-L12) (`clm_11baeaae672ee54036db2c0b8542e601a36de7c3074b13584bab5fe738415b03`)

## relevance (2 claim(s))

- [observation/documented] The GSM and MMLU datasets are external, with links to the openai/grade-school-math and hendrycks/test repositories for download. -- evidence: [README.md#L38-L38](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L38-L38), [README.md#L57-L57](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L57-L57) (`clm_4b475c9de024e71a72e9284553605942b02d56047a32dd7025651b8a4cd1b41b`)
- [observation/documented] The work is associated with authors Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch, with a project page and arXiv paper (2305.14325). -- evidence: [README.md#L59-L67](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L59-L67), [README.md#L5-L9](https://github.com/composable-models/llm_multiagent_debate/blob/9846749350eb917ae5bfaaff4c645fc705b8d3af/README.md#L5-L9) (`clm_fcedf510b3af498c2e246b727cb4e41951891943445becf8c4966f75e32948f6`)

