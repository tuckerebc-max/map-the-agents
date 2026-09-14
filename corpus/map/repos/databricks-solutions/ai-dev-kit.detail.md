# databricks-solutions/ai-dev-kit -- full detail

[Back to orientation](ai-dev-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/databricks-solutions/ai-dev-kit/b059fd017a2c5743c31a0ff30dc8a618723aae4f/8f133f51eafee394.json](../../../wiki/dossiers/databricks-solutions/ai-dev-kit/b059fd017a2c5743c31a0ff30dc8a618723aae4f/8f133f51eafee394.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The kit ships as four composable pieces: skills, a full-stack Builder App, a Python library (databricks-tools-core), and a standalone MCP server exposing 40+ Databricks tools. -- evidence: [README.md#L382-L382](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L382-L382), [README.md#L390-L396](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L390-L396) (`clm_8d1174a7dd2307c26802613082301e4b509fbe1a828b7c7f0194632777366a18`)

## design-choices (2 claim(s))

- [observation/documented] The databricks-apps-python skill defaults to AppKit (TypeScript + React) and falls back to Python frameworks (Dash, Streamlit, Flask, FastAPI, Gradio, Reflex); the APX framework lives in a separate repo. -- evidence: [README.md#L138-L138](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L138-L138) (`clm_4d77fc99b9912103ca47d6c61abce36f4a0a90cd4030a293ba45ebbebd4155f8`)
- [observation/documented] By default `databricks aitools install` installs the official databricks plugin through each agent's own plugin CLI for Claude Code, Codex, and Copilot, and writes raw skill files for Cursor, OpenCode, and Antigravity; --skills-only forces raw files everywhere. -- evidence: [README.md#L342-L347](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L342-L347) (`clm_102d6ab63675c662ef98d27527d6426c11c43dc12e52b881ddabdf33519a838d`)

## workflows (3 claim(s))

- [observation/documented] The installer records resolved refs, commit SHAs, and the aitools release in a skills.lock file inside a scope-local .ai-dev-kit/ state directory. -- evidence: [README.md#L248-L248](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L248-L248) (`clm_cd757a1497838a8823da2e6873b53df61b51f3d2b0f2be936cda298a318348d6`)
- [observation/documented] For Genie Code, skills are uploaded to /Workspace/Users/<you>/.assistant/skills using a provided notebook that downloads skills from GitHub and uploads them via the Databricks SDK, including on serverless compute. -- evidence: [README.md#L360-L363](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L360-L363), [README.md#L356-L358](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L356-L358) (`clm_b87575b77ebcbe8e00220410f61c77aae11b8f3e7e3f0a9ea9a2e49015ce4a1f`)
- [observation/documented] Repository development practice: the project is maintained by Databricks for Field Engineers; external contributions are not currently accepted, though issues may be opened. Contributors follow PEP 8, add type hints, and run ruff (pinned 0.11.0, line-length 120, py311) before submitting PRs. -- evidence: [CONTRIBUTING.md#L3-L3](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/CONTRIBUTING.md#L3-L3), [CONTRIBUTING.md#L37-L37](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L57-L60](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/CONTRIBUTING.md#L57-L60), [CONTRIBUTING.md#L30-L33](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/CONTRIBUTING.md#L30-L33) (`clm_5f4d41aba6ad7277180d0ed72811a387e09099d6eb3b0b7e565237ff1cf490f5`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are no longer bundled in this repo; they come from databricks/databricks-agent-skills via `databricks aitools install` and from mlflow/skills fetched from main (overridable with MLFLOW_REF). -- evidence: [README.md#L227-L228](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L227-L228), [README.md#L230-L233](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L230-L233), [README.md#L371-L378](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L371-L378), [README.md#L349-L352](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L349-L352) (`clm_e4e01b79c33a37fae13e88ccbd9bf81dfd2f1dc4aa0caa973a06aa0302faa8ee`)
- [observation/documented] Several skills were renamed or consolidated in the official install, e.g. databricks-bundles to databricks-dabs, databricks-genie to databricks-genie-agents, and databricks-config merged into databricks-core. -- evidence: [README.md#L36-L37](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L36-L37), [README.md#L39-L45](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L39-L45) (`clm_d8d94ee3dc6ecae988d41f45af7528c214c1a325c5a0a68c4103153c4b2491fd`)

## interfaces (3 claim(s))

- [observation/documented] The databricks-tools-core Python library exposes functions such as execute_sql for direct use in Python projects, and is described as compatible with LangChain and the OpenAI Agents SDK. -- evidence: [README.md#L329-L329](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L329-L329), [README.md#L323-L324](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L323-L324), [README.md#L321-L321](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L321-L321), [README.md#L326-L327](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L326-L327) (`clm_cdbefb355db3753968da14fb00b0e86d63c306d24e0dc0722ea0e2b58ecea831`)
- [observation/documented] The Builder App can be deployed with --enable-mcp so it also serves as an MCP server at /mcp, exposing 40+ Databricks tools to Genie Code, AI Playground, and other MCP clients in a single deployment. -- evidence: [README.md#L314-L314](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L314-L314), [README.md#L311-L312](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L311-L312) (`clm_d5393d67e112c01c9aa218800f5638e444fb91cc011fdc245fa8fb75d08bc627`)
- [observation/documented] The installer supports --list-skills and --dry-run to preview skills, profiles, resolved refs, and the aitools command without changing anything, plus environment variables MLFLOW_REF, INCLUDE_PRERELEASES, and DRY_RUN. -- evidence: [README.md#L237-L237](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L237-L237), [README.md#L242-L246](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L242-L246) (`clm_bb1653b3d968f52e0ff93da03551952ba0de26fc759ddb5b54ffb21f38515822`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] After a litellm supply-chain incident affecting versions 1.82.7-1.82.8, the litellm dependency was removed for most usage and is now only used in the test directory, pinned to a safe version. -- evidence: [README.md#L47-L50](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L47-L50) (`clm_e3954cd54d465aad3671a5f13104c0e6a3033381d934b59a539916bc6565c6fa`)
- [observation/documented] Third-party components include fastmcp, the MCP Python SDK, sqlglot, sqlfluff, claude-agent-sdk, FastAPI, uvicorn, httpx, SQLAlchemy, alembic, asyncpg, and the Databricks and Anthropic Python SDKs, under MIT, BSD-3-Clause, Apache-2.0, and LGPL-3.0 licenses. -- evidence: [NOTICE.txt#L60-L60](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L60-L60), [NOTICE.txt#L78-L80](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L78-L80), [NOTICE.txt#L14-L16](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L14-L16), [NOTICE.txt#L74-L76](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L74-L76), [NOTICE.txt#L72-L72](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L72-L72), [NOTICE.txt#L86-L86](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L86-L86), [NOTICE.txt#L18-L20](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.txt#L18-L20), [README.md#L421-L436](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L421-L436) (`clm_3ddcdbdcac8fbac6f96291d61cc311a3c0d19b01cec42c57b91892edd636e232`)

## limitations (2 claim(s))

- [observation/documented] Databricks does not offer official support for Databricks Solutions repositories; issues are handled on a best-effort basis via GitHub, and the MCP server is likewise maintained on a best-effort basis. -- evidence: [NOTICE.md#L2-L3](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/NOTICE.md#L2-L3), [README.md#L26-L28](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L26-L28) (`clm_3c5fcb5066a28d033f3c1623e1f11d6b621fc9862b720502937a413144d49ed1`)
- [observation/documented] Cursor and Copilot require manual settings updates after install, and `databricks aitools install` does not yet cover Genie Code skill uploads. -- evidence: [README.md#L188-L189](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L188-L189), [README.md#L222-L223](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L222-L223), [README.md#L356-L358](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L356-L358) (`clm_7cd7c2f181a37a966455bd10c0961f684d328bc20b0195ee607d5296b4f4b835`)

## relevance (1 claim(s))

- [observation/documented] The kit targets developers building on Databricks with AI coding agents, covering Spark Declarative Pipelines, Jobs, AI/BI Dashboards, Unity Catalog, Genie Spaces, MLflow, Model Serving, and Databricks Apps. -- evidence: [README.md#L127-L136](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L127-L136), [README.md#L91-L91](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L91-L91) (`clm_3169d0aa5c97fce1d0ca5a93883ecab40c83b3517d2df8adf0a51d5a2d1ac731`)

