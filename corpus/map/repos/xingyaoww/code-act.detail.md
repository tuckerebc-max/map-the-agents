# xingyaoww/code-act -- full detail

[Back to orientation](code-act.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xingyaoww/code-act/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/f7a43317eb47f954.json](../../../wiki/dossiers/xingyaoww/code-act/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/f7a43317eb47f954.json)

## specifications (2 claim(s))

- [observation/documented] CodeAct consolidates LLM agent actions into a unified action space using executable code, integrated with a Python interpreter so the agent can revise prior actions or emit new ones based on execution results across multi-turn interactions. -- evidence: [README.md#L13-L14](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L13-L14) (`clm_6cbb7b7948fd85ddcd4b6c2fd6f6ce818de2b3880fa7cfe0d1713ef7dc8e2060`)
- [observation/documented] Two agent variants are released: CodeActAgent-Mistral-7b-v0.1 (recommended, Mistral-7b-v0.1 base with a 32k context window) and CodeActAgent-Llama-7b (Llama-2-7b base with a 4k context window), trained on the 7k multi-turn CodeActInstruct dataset. -- evidence: [README.md#L49-L51](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L49-L51), [README.md#L41-L41](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L41-L41) (`clm_1bf43c288d3cc85b46c2e7c13a964952699f9ca39ef535c1e80f2281a9902a1e`)

## components (2 claim(s))

- [observation/documented] A CodeActAgent system comprises an LLM serving layer (e.g., vLLM exposing an OpenAI-compatible API), an interaction interface (chat-ui with MongoDB history or a simple Python script), and a code execution engine service. -- evidence: [README.md#L67-L71](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L67-L71) (`clm_20861860fad0c266f19753fb21eba6da67fc23bf6f95c6ecc6df048cc3e6b750`)
- [observation/documented] The code execution engine is built on JupyterKernelGateway and starts a Jupyter server inside a Docker container per chat session to serve code execution requests, with sessions timing out after a fixed period. -- evidence: [README.md#L146-L146](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L146-L146) (`clm_be833915e75abae8de582004c37af8fd9ea67b53e6648bd8f0ad8460d02a7756`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: reproducing the released models involves cloning submodules, optionally generating CodeActInstruct trajectories via the MINT framework in Docker, and training with a forked Megatron-LLM using provided 4xA100 scripts or SLURM job files. -- evidence: [docs/MODEL_TRAINING.md#L103-L103](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L103-L103), [docs/MODEL_TRAINING.md#L95-L96](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L95-L96), [README.md#L215-L215](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L215-L215), [README.md#L204-L205](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L204-L205), [README.md#L211-L211](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L211-L211), [docs/DATA_GENERATION.md#L31-L31](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/DATA_GENERATION.md#L31-L31) (`clm_e3c8564315e97072da76ec1060ae5787e419f95951e990ee9227b682c88cf140`)
- [observation/documented] Repository development practice: training data is converted to Megatron format with ChatML chat templating and sequence packing (e.g., 78k instances packed into 19k sequences), and checkpoints can be converted back to HuggingFace format with a ChatML chat_template added. -- evidence: [docs/MODEL_TRAINING.md#L136-L136](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L136-L136), [docs/MODEL_TRAINING.md#L80-L80](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L80-L80), [docs/MODEL_TRAINING.md#L76-L78](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L76-L78) (`clm_0f1e88d9415ec6b2d0616a43280d7272405aa1f7576f16e94b28cb3d9693e390`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The code execution engine exposes an HTTP endpoint (example port 8081 via start_jupyter_server.sh) that the demo Python script consumes through a jupyter_kernel_url /execute path. -- evidence: [README.md#L161-L162](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L161-L162), [README.md#L150-L151](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L150-L151) (`clm_3491975c3f530622f979c934f4e9d964cbef512a3a7389751f3896868e66ffcf`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The paper's analysis covers 17 LLMs on API-Bank and a newly curated M3ToolEval benchmark, reporting CodeAct outperforming Text and JSON action formats by up to 20% higher success rate. -- evidence: [README.md#L30-L30](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L30-L30) (`clm_f8fd70f16858d7279a3eac3e3a11c4d6d928a92ab3fe64b4752d394a8dfe991d`)
- [observation/documented] MT-Bench evaluation requires an OPENAI_API_KEY because it uses GPT-4 as the judge; the corresponding lines in the mint-bench script can be commented out to disable it. -- evidence: [docs/EVALUATION.md#L57-L57](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/EVALUATION.md#L57-L57) (`clm_d2a39cc692b63bda89c9781c7c5f8a4f571f456c5e6b45f10a9c29ed690d3768`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

