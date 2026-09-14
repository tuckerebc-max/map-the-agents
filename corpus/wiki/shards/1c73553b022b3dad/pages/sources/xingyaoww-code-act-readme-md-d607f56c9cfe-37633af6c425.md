---
access: public
aliases: []
claim_ids:
- clm_1bf43c288d3cc85b46c2e7c13a964952699f9ca39ef535c1e80f2281a9902a1e
- clm_20861860fad0c266f19753fb21eba6da67fc23bf6f95c6ecc6df048cc3e6b750
- clm_3491975c3f530622f979c934f4e9d964cbef512a3a7389751f3896868e66ffcf
- clm_6cbb7b7948fd85ddcd4b6c2fd6f6ce818de2b3880fa7cfe0d1713ef7dc8e2060
- clm_be833915e75abae8de582004c37af8fd9ea67b53e6648bd8f0ad8460d02a7756
- clm_e3c8564315e97072da76ec1060ae5787e419f95951e990ee9227b682c88cf140
- clm_f8fd70f16858d7279a3eac3e3a11c4d6d928a92ab3fe64b4752d394a8dfe991d
maturity: draft
page_id: pg_48f483c246d95f398f2637633af6c425
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6b7d389a12af5f2fb73c2d3e02801a70
title: xingyaoww/code-act/README.md @ d607f56c9cfe
updated_at: '2026-09-14T04:59:21Z'
---

# xingyaoww/code-act/README.md @ d607f56c9cfe

<!-- rcw:begin owner=source:src_6b7d389a12af5f2fb73c2d3e02801a70 block=evidence -->
- Two agent variants are released: CodeActAgent-Mistral-7b-v0.1 (recommended, Mistral-7b-v0.1 base with a 32k context window) and CodeActAgent-Llama-7b (Llama-2-7b base with a 4k context window), trained on the 7k multi-turn CodeActInstruct dataset. [@claim:clm_1bf43c288d3cc85b46c2e7c13a964952699f9ca39ef535c1e80f2281a9902a1e]
- A CodeActAgent system comprises an LLM serving layer (e.g., vLLM exposing an OpenAI-compatible API), an interaction interface (chat-ui with MongoDB history or a simple Python script), and a code execution engine service. [@claim:clm_20861860fad0c266f19753fb21eba6da67fc23bf6f95c6ecc6df048cc3e6b750]
- The code execution engine exposes an HTTP endpoint (example port 8081 via start_jupyter_server.sh) that the demo Python script consumes through a jupyter_kernel_url /execute path. [@claim:clm_3491975c3f530622f979c934f4e9d964cbef512a3a7389751f3896868e66ffcf]
- CodeAct consolidates LLM agent actions into a unified action space using executable code, integrated with a Python interpreter so the agent can revise prior actions or emit new ones based on execution results across multi-turn interactions. [@claim:clm_6cbb7b7948fd85ddcd4b6c2fd6f6ce818de2b3880fa7cfe0d1713ef7dc8e2060]
- The code execution engine is built on JupyterKernelGateway and starts a Jupyter server inside a Docker container per chat session to serve code execution requests, with sessions timing out after a fixed period. [@claim:clm_be833915e75abae8de582004c37af8fd9ea67b53e6648bd8f0ad8460d02a7756]
- Repository development practice: reproducing the released models involves cloning submodules, optionally generating CodeActInstruct trajectories via the MINT framework in Docker, and training with a forked Megatron-LLM using provided 4xA100 scripts or SLURM job files. [@claim:clm_e3c8564315e97072da76ec1060ae5787e419f95951e990ee9227b682c88cf140]
- The paper's analysis covers 17 LLMs on API-Bank and a newly curated M3ToolEval benchmark, reporting CodeAct outperforming Text and JSON action formats by up to 20% higher success rate. [@claim:clm_f8fd70f16858d7279a3eac3e3a11c4d6d928a92ab3fe64b4752d394a8dfe991d]
<!-- rcw:end owner=source:src_6b7d389a12af5f2fb73c2d3e02801a70 block=evidence -->

## Researcher notes

