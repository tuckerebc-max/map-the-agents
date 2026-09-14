---
access: public
aliases: []
claim_ids:
- clm_102d6ab63675c662ef98d27527d6426c11c43dc12e52b881ddabdf33519a838d
- clm_3169d0aa5c97fce1d0ca5a93883ecab40c83b3517d2df8adf0a51d5a2d1ac731
- clm_3c5fcb5066a28d033f3c1623e1f11d6b621fc9862b720502937a413144d49ed1
- clm_3ddcdbdcac8fbac6f96291d61cc311a3c0d19b01cec42c57b91892edd636e232
- clm_4d77fc99b9912103ca47d6c61abce36f4a0a90cd4030a293ba45ebbebd4155f8
- clm_7cd7c2f181a37a966455bd10c0961f684d328bc20b0195ee607d5296b4f4b835
- clm_8d1174a7dd2307c26802613082301e4b509fbe1a828b7c7f0194632777366a18
- clm_b87575b77ebcbe8e00220410f61c77aae11b8f3e7e3f0a9ea9a2e49015ce4a1f
- clm_bb1653b3d968f52e0ff93da03551952ba0de26fc759ddb5b54ffb21f38515822
- clm_cd757a1497838a8823da2e6873b53df61b51f3d2b0f2be936cda298a318348d6
- clm_cdbefb355db3753968da14fb00b0e86d63c306d24e0dc0722ea0e2b58ecea831
- clm_d5393d67e112c01c9aa218800f5638e444fb91cc011fdc245fa8fb75d08bc627
- clm_d8d94ee3dc6ecae988d41f45af7528c214c1a325c5a0a68c4103153c4b2491fd
- clm_e3954cd54d465aad3671a5f13104c0e6a3033381d934b59a539916bc6565c6fa
- clm_e4e01b79c33a37fae13e88ccbd9bf81dfd2f1dc4aa0caa973a06aa0302faa8ee
maturity: draft
page_id: pg_cfdb4b4ca78b5020ae0478b36b1cedd3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1afef3093e5f51ad95d749b3e1e1a8a1
title: databricks-solutions/ai-dev-kit/README.md @ b059fd017a2c
updated_at: '2026-09-14T03:45:10Z'
---

# databricks-solutions/ai-dev-kit/README.md @ b059fd017a2c

<!-- rcw:begin owner=source:src_1afef3093e5f51ad95d749b3e1e1a8a1 block=evidence -->
- By default `databricks aitools install` installs the official databricks plugin through each agent's own plugin CLI for Claude Code, Codex, and Copilot, and writes raw skill files for Cursor, OpenCode, and Antigravity; --skills-only forces raw files everywhere. [@claim:clm_102d6ab63675c662ef98d27527d6426c11c43dc12e52b881ddabdf33519a838d]
- The kit targets developers building on Databricks with AI coding agents, covering Spark Declarative Pipelines, Jobs, AI/BI Dashboards, Unity Catalog, Genie Spaces, MLflow, Model Serving, and Databricks Apps. [@claim:clm_3169d0aa5c97fce1d0ca5a93883ecab40c83b3517d2df8adf0a51d5a2d1ac731]
- Databricks does not offer official support for Databricks Solutions repositories; issues are handled on a best-effort basis via GitHub, and the MCP server is likewise maintained on a best-effort basis. [@claim:clm_3c5fcb5066a28d033f3c1623e1f11d6b621fc9862b720502937a413144d49ed1]
- Third-party components include fastmcp, the MCP Python SDK, sqlglot, sqlfluff, claude-agent-sdk, FastAPI, uvicorn, httpx, SQLAlchemy, alembic, asyncpg, and the Databricks and Anthropic Python SDKs, under MIT, BSD-3-Clause, Apache-2.0, and LGPL-3.0 licenses. [@claim:clm_3ddcdbdcac8fbac6f96291d61cc311a3c0d19b01cec42c57b91892edd636e232]
- The databricks-apps-python skill defaults to AppKit (TypeScript + React) and falls back to Python frameworks (Dash, Streamlit, Flask, FastAPI, Gradio, Reflex); the APX framework lives in a separate repo. [@claim:clm_4d77fc99b9912103ca47d6c61abce36f4a0a90cd4030a293ba45ebbebd4155f8]
- Cursor and Copilot require manual settings updates after install, and `databricks aitools install` does not yet cover Genie Code skill uploads. [@claim:clm_7cd7c2f181a37a966455bd10c0961f684d328bc20b0195ee607d5296b4f4b835]
- The kit ships as four composable pieces: skills, a full-stack Builder App, a Python library (databricks-tools-core), and a standalone MCP server exposing 40+ Databricks tools. [@claim:clm_8d1174a7dd2307c26802613082301e4b509fbe1a828b7c7f0194632777366a18]
- For Genie Code, skills are uploaded to /Workspace/Users/<you>/.assistant/skills using a provided notebook that downloads skills from GitHub and uploads them via the Databricks SDK, including on serverless compute. [@claim:clm_b87575b77ebcbe8e00220410f61c77aae11b8f3e7e3f0a9ea9a2e49015ce4a1f]
- The installer supports --list-skills and --dry-run to preview skills, profiles, resolved refs, and the aitools command without changing anything, plus environment variables MLFLOW_REF, INCLUDE_PRERELEASES, and DRY_RUN. [@claim:clm_bb1653b3d968f52e0ff93da03551952ba0de26fc759ddb5b54ffb21f38515822]
- The installer records resolved refs, commit SHAs, and the aitools release in a skills.lock file inside a scope-local .ai-dev-kit/ state directory. [@claim:clm_cd757a1497838a8823da2e6873b53df61b51f3d2b0f2be936cda298a318348d6]
- The databricks-tools-core Python library exposes functions such as execute_sql for direct use in Python projects, and is described as compatible with LangChain and the OpenAI Agents SDK. [@claim:clm_cdbefb355db3753968da14fb00b0e86d63c306d24e0dc0722ea0e2b58ecea831]
- The Builder App can be deployed with --enable-mcp so it also serves as an MCP server at /mcp, exposing 40+ Databricks tools to Genie Code, AI Playground, and other MCP clients in a single deployment. [@claim:clm_d5393d67e112c01c9aa218800f5638e444fb91cc011fdc245fa8fb75d08bc627]
- Several skills were renamed or consolidated in the official install, e.g. databricks-bundles to databricks-dabs, databricks-genie to databricks-genie-agents, and databricks-config merged into databricks-core. [@claim:clm_d8d94ee3dc6ecae988d41f45af7528c214c1a325c5a0a68c4103153c4b2491fd]
- After a litellm supply-chain incident affecting versions 1.82.7-1.82.8, the litellm dependency was removed for most usage and is now only used in the test directory, pinned to a safe version. [@claim:clm_e3954cd54d465aad3671a5f13104c0e6a3033381d934b59a539916bc6565c6fa]
- Skills are no longer bundled in this repo; they come from databricks/databricks-agent-skills via `databricks aitools install` and from mlflow/skills fetched from main (overridable with MLFLOW_REF). [@claim:clm_e4e01b79c33a37fae13e88ccbd9bf81dfd2f1dc4aa0caa973a06aa0302faa8ee]
<!-- rcw:end owner=source:src_1afef3093e5f51ad95d749b3e1e1a8a1 block=evidence -->

## Researcher notes

