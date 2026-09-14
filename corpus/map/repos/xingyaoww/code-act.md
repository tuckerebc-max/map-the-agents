# xingyaoww/code-act

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d607f56c9cfe @ f7a43317eb47f954

## Summary (orientation draft, not independently verified)

Selected evidence records: CodeAct consolidates LLM agent actions into a unified action space using executable code, integrated with a Python interpreter so the agent can revise prior actions or emit new ones based on execution results across multi-turn interactions. A CodeActAgent system comprises an LLM serving layer (e.g., vLLM exposing an OpenAI-compatible API), an interaction interface (chat-ui with MongoDB history or a simple Python script), and a code execution engine service.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] CodeAct consolidates LLM agent actions into a unified action space using executable code, integrated with a Python interpreter so the agent can revise prior actions or emit new ones based on execution results across multi-turn interactions. -- evidence: [README.md#L13-L14](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L13-L14)
  - [observation/documented] Two agent variants are released: CodeActAgent-Mistral-7b-v0.1 (recommended, Mistral-7b-v0.1 base with a 32k context window) and CodeActAgent-Llama-7b (Llama-2-7b base with a 4k context window), trained on the 7k multi-turn CodeActInstruct dataset. -- evidence: [README.md#L49-L51](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L49-L51), [README.md#L41-L41](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L41-L41)
- components (2 claim(s)):
  - [observation/documented] A CodeActAgent system comprises an LLM serving layer (e.g., vLLM exposing an OpenAI-compatible API), an interaction interface (chat-ui with MongoDB history or a simple Python script), and a code execution engine service. -- evidence: [README.md#L67-L71](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L67-L71)
  - [observation/documented] The code execution engine is built on JupyterKernelGateway and starts a Jupyter server inside a Docker container per chat session to serve code execution requests, with sessions timing out after a fixed period. -- evidence: [README.md#L146-L146](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L146-L146)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: reproducing the released models involves cloning submodules, optionally generating CodeActInstruct trajectories via the MINT framework in Docker, and training with a forked Megatron-LLM using provided 4xA100 scripts or SLURM job files. -- evidence: [docs/MODEL_TRAINING.md#L103-L103](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L103-L103), [docs/MODEL_TRAINING.md#L95-L96](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L95-L96), [README.md#L215-L215](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L215-L215), [README.md#L204-L205](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L204-L205), [README.md#L211-L211](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L211-L211), [docs/DATA_GENERATION.md#L31-L31](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/DATA_GENERATION.md#L31-L31)
  - [observation/documented] Repository development practice: training data is converted to Megatron format with ChatML chat templating and sequence packing (e.g., 78k instances packed into 19k sequences), and checkpoints can be converted back to HuggingFace format with a ChatML chat_template added. -- evidence: [docs/MODEL_TRAINING.md#L136-L136](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L136-L136), [docs/MODEL_TRAINING.md#L80-L80](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L80-L80), [docs/MODEL_TRAINING.md#L76-L78](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/docs/MODEL_TRAINING.md#L76-L78)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The code execution engine exposes an HTTP endpoint (example port 8081 via start_jupyter_server.sh) that the demo Python script consumes through a jupyter_kernel_url /execute path. -- evidence: [README.md#L161-L162](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L161-L162), [README.md#L150-L151](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md#L150-L151)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](code-act.detail.md)

Metadata and full claim list: [full detail](code-act.detail.md)
Human notes ([notes](code-act.notes.md), never overwritten by build)

[Back to map index](../../index.md)
