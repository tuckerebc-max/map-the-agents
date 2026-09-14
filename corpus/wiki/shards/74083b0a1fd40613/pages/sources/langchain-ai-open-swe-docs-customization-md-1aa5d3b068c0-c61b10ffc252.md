---
access: public
aliases: []
claim_ids:
- clm_48a50b6f1cca70c7d6b6878699a9ad939c23417a1d9d36cd4415866b6e9e2d67
- clm_577b614381fab4418b75ea648d9438ea1082f80f4351c694c135902468d1e5d2
- clm_676c40853ff37e9148beb3dd2417582aaf7277322c59750fe31050ca74c2b4ca
- clm_8de56af2cfa5a93a1bf4cb0e3cbfcc3c1da84b2dcf97ace0bd6bcd0b2722226d
- clm_d9fe1c643132a386b8e356e05b3d4fb227d30657f84769ceefdaae34fb26822e
- clm_f26c6b8dede45e8fd1dbd978bc158faf62561c576a36b146af11efd8467db946
maturity: draft
page_id: pg_2f156ab3ba445d80b322c61b10ffc252
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7b3ceefcc93454a881818cfa6136ac1f
title: langchain-ai/open-swe/docs/CUSTOMIZATION.md @ 1aa5d3b068c0
updated_at: '2026-09-14T02:10:57Z'
---

# langchain-ai/open-swe/docs/CUSTOMIZATION.md @ 1aa5d3b068c0

<!-- rcw:begin owner=source:src_7b3ceefcc93454a881818cfa6136ac1f block=evidence -->
- The core agent is assembled in a single function, get_agent() in agent/server.py, where the sandbox, model, tools, and triggers can be swapped; custom sandbox providers implement SandboxBackendProtocol from deepagents. [@claim:clm_48a50b6f1cca70c7d6b6878699a9ad939c23417a1d9d36cd4415866b6e9e2d67]
- LangSmith is the default sandbox and tracing provider; Modal, Daytona, Runloop, E2B, and local execution are also supported via a pluggable provider interface selected by the SANDBOX_TYPE environment variable. [@claim:clm_577b614381fab4418b75ea648d9438ea1082f80f4351c694c135902468d1e5d2]
- Model defaults are configurable via LLM_MODEL_ID and LLM_REASONING_EFFORT; an Anthropic-only deployment defaults to anthropic:claude-opus-5, other deployments to openai:gpt-5.6-sol, with default reasoning effort medium. [@claim:clm_676c40853ff37e9148beb3dd2417582aaf7277322c59750fe31050ca74c2b4ca]
- Admins can connect remote MCP servers whose enabled tools become available to all coding-agent users; personal MCP connections load only in private threads owned by the triggering user, and plan mode blocks workspace MCP tools. [@claim:clm_8de56af2cfa5a93a1bf4cb0e3cbfcc3c1da84b2dcf97ace0bd6bcd0b2722226d]
- The project is under active development and its APIs, setup, and product surfaces may continue to evolve; the local sandbox provider runs commands directly on the host with no isolation and is intended only for development. [@claim:clm_d9fe1c643132a386b8e356e05b3d4fb227d30657f84769ceefdaae34fb26822e]
- For LangSmith sandboxes, GitHub proxy rules give github.com Basic auth for git-over-HTTPS and api.github.com Bearer auth for gh/REST; the proxy token is minted at runtime from GitHub App installation credentials rather than stored as env vars. [@claim:clm_f26c6b8dede45e8fd1dbd978bc158faf62561c576a36b146af11efd8467db946]
<!-- rcw:end owner=source:src_7b3ceefcc93454a881818cfa6136ac1f block=evidence -->

## Researcher notes

