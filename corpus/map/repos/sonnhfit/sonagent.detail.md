# sonnhfit/sonagent -- full detail

[Back to orientation](sonagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sonnhfit/sonagent/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/2a013181a18ec69d.json](../../../wiki/dossiers/sonnhfit/sonagent/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/2a013181a18ec69d.json)

## specifications (1 claim(s))

- [observation/documented] The project describes itself as an autonomous 'Digital Consciousness Backup Agent' that uses LLMs to safeguard a user's digital presence, with self-editing source code capability. -- evidence: [README.MD#L9-L10](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L9-L10) (`clm_3a98cc0826a69cb4b3afb3af77d1fdb3d766487393c6e111f4979764415da4f2`)

## components (1 claim(s))

- [observation/documented] SkillBuilder consists of a SandboxExecutor that runs code with restricted imports/builtins and no file or network access, a SkillGenerator using templates, and a user-facing SkillBuilder skill with create_simple_skill, generate_skill, and test_skill_code methods. -- evidence: [docs/SKILL_BUILDER.md#L19-L23](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L19-L23), [docs/SKILL_BUILDER.md#L31-L38](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L31-L38), [docs/SKILL_BUILDER.md#L150-L154](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L150-L154), [docs/SKILL_BUILDER.md#L25-L29](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L25-L29) (`clm_9a74e32cec2c7a921ab996214ee4cc864f02058e25aa98992986e45d293bc5a5`)

## design-choices (2 claim(s))

- [observation/documented] The agent's stated design includes belief-based reasoning with LLMs, automatic belief acquisition over time, and learning from human feedback. -- evidence: [README.MD#L15-L15](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L15-L15), [README.MD#L19-L19](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L19-L19), [README.MD#L17-L17](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L17-L17) (`clm_5ad149584e62ab0e18c56936144f65417ac08e36a804911d599caefebfbde68d`)
- [observation/documented] Timezone is configurable via config.json or the SONAGENT_TIMEZONE environment variable, with priority env var > config file > default UTC, and any pytz-supported timezone string. -- evidence: [README.MD#L80-L80](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L80-L80), [README.MD#L82-L82](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L82-L82), [README.MD#L63-L71](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L63-L71), [README.MD#L73-L75](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L73-L75) (`clm_de35cdd140713252a9bcadbff29f35112c4d980fad4deab5dc719422f9ca98ba`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: dev tooling is pinned in requirements-dev.txt (pytest, ruff, mypy, pre-commit, coverage plugins), docs use Sphinx, and Docker images are built by CI to GitHub Container Registry with latest/dev/version/SHA tags. -- evidence: [requirements-dev.txt#L1-L10](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements-dev.txt#L1-L10), [README.MD#L147-L147](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L147-L147), [README.MD#L149-L152](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L149-L152), [docs/requirements.txt#L1-L2](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/requirements.txt#L1-L2) (`clm_d68420b789dcb729d754beb23c7b8e45b49b4bcf05aa95c089a67d805ded3f49`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills come in two types: Python classes inheriting from pydantic BaseModel, and markdown LLM instruction files; skills live in shared or per-agent directories under user_data/skills/. -- evidence: [docs/AGENT_SYSTEM.md#L110-L110](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L110-L110), [docs/AGENT_SYSTEM.md#L131-L131](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L131-L131), [docs/AGENT_SYSTEM.md#L115-L119](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L115-L119), [docs/AGENT_SYSTEM.md#L74-L78](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L74-L78) (`clm_a8c01500d523ac607337e643fad125b019d32962c5bcaa878c04d8433394b6d0`)
- [observation/documented] Standard starter skills (TextPrinter, WeatherAPISkill, HanoiWeatherChecker, SkillBuilder) are copied into user_data/skills/ on first run, and agent-specific starter skills are copied from sonagent/standard_skills/{agent_id}/ at startup. -- evidence: [README.MD#L45-L54](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L45-L54), [docs/AGENT_SYSTEM.md#L152-L152](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L152-L152), [docs/AGENT_SYSTEM.md#L179-L179](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L179-L179) (`clm_06600a8f74483dae422fb5578d4dc1450ebbdf8a05eadbb5f6e71f8721df90af`)

## interfaces (2 claim(s))

- [observation/documented] MainAgent exposes a command-based process interface supporting commands such as create_task, list_tasks, get_task_status, and kill_task, with task priority determining execution order. -- evidence: [docs/AGENT_SYSTEM.md#L334-L334](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L334-L334), [docs/AGENT_SYSTEM.md#L247-L251](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L247-L251), [docs/AGENT_SYSTEM.md#L230-L235](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L230-L235), [docs/AGENT_SYSTEM.md#L241-L244](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L241-L244), [docs/AGENT_SYSTEM.md#L238-L238](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L238-L238) (`clm_4d874d5587c55ca25a693d0243d4edcef81a613a208b86b6e9e0b6316c58389e`)
- [observation/documented] The CLI is installed via pip and run with 'sonagent run' taking --config, --agentdb (SQLite), --memory-url, --user-data-dir, and --log-level options; 'sonagent init' creates the user_data folder. -- evidence: [README.MD#L32-L34](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L32-L34), [README.MD#L38-L43](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L38-L43), [README.MD#L56-L58](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L56-L58), [README.MD#L45-L54](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L45-L54) (`clm_ba73c85060de8b39d8df65972d6e2c609b1903c5b1952d927a4613cb92f0b0b3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A multi-agent architecture includes a central AgentRegistry for registration, status tracking, and inter-agent message passing, plus a MainAgent coordinator that creates, assigns, and monitors tasks for sub-agents. -- evidence: [docs/AGENT_SYSTEM.md#L20-L23](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L20-L23), [docs/AGENT_SYSTEM.md#L58-L61](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L58-L61), [docs/AGENT_SYSTEM.md#L7-L12](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L7-L12) (`clm_06405e215164ce2eee204a8d34f104f9b82000b7701f5826b40c433434640fe2`)

## tools-permissions (1 claim(s))

- [observation/documented] The sandbox execution environment enforces whitelisted imports, a limited builtin set, no file-system modification, and restricted network access for unsaved skills, with syntax validation before execution. -- evidence: [docs/SKILL_BUILDER.md#L9-L13](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L9-L13), [docs/SKILL_BUILDER.md#L150-L154](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L150-L154) (`clm_c2f1da6be12dde276bab612886b68b82abbec9d8aa97527801943a4dc4b49a53`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include chromadb, SQLAlchemy, python-telegram-bot, FastAPI/uvicorn for an API server, and AI libraries agno, groq, and openai, plus research tools such as arxiv, wikipedia, yfinance, and ddgs. -- evidence: [requirements.txt#L39-L46](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements.txt#L39-L46), [requirements.txt#L1-L4](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements.txt#L1-L4), [requirements.txt#L13-L21](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements.txt#L13-L21), [requirements.txt#L34-L36](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements.txt#L34-L36) (`clm_7aaa4aace79cfd665caaa03c718120214a438d3cdc58450be4908fe808b1130a`)

## limitations (1 claim(s))

- [observation/documented] The SkillBuilder documentation acknowledges current limitations: generation is template-based, complex logic needs manual coding, LLM-based implementation generation is not yet present, and some Python features are restricted in the sandbox. -- evidence: [docs/SKILL_BUILDER.md#L201-L204](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L201-L204) (`clm_0c811e8e3a9f7bb9e12337e7a7d8170fb74eec7cd22e16a42d79fa12c08403f0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

