# swe-agent/swe-agent -- full detail

[Back to orientation](swe-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swe-agent/swe-agent/3ea751c087f32b16e039a2233dd6eefecef325d5/9b7bae7bd10c873c.json](../../../wiki/dossiers/swe-agent/swe-agent/3ea751c087f32b16e039a2233dd6eefecef325d5/9b7bae7bd10c873c.json)

## specifications (1 claim(s))

- [observation/documented] SWE-agent enables a user-chosen language model (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories, find cybersecurity vulnerabilities, or perform custom tasks. -- evidence: [README.md#L27-L30](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L27-L30) (`clm_917cb9115361931b246d2da67b667ce4fc4d4d2295e85a44920a0ce2a7664b3b`)

## components (3 claim(s))

- [observation/documented] The central entry point is the sweagent CLI, which initializes a SWEEnv environment wrapper (a thin wrapper around SWE-ReX since 1.0) and an Agent class whose forward() method prompts the model and executes its action. -- evidence: [docs/background/architecture.md#L13-L13](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L13-L13), [docs/background/architecture.md#L7-L11](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L7-L11) (`clm_6b6235502d377abfb7244e922251b87dd7379f7f136f3e694c2665c997add103`)
- [observation/documented] A HistoryProcessor compresses the conversation history to make best use of the model's context window, and a parser extracts the action from the model output before it is executed in the shell session via SWEEnv. -- evidence: [docs/background/architecture.md#L15-L15](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L15-L15) (`clm_691fd690eead13be218f2520a2f8cde945841369f65328d62667bf1c83d45754`)
- [observation/documented] Agent tools are organized into tool bundles, each a folder containing bin/ executables, a config.yaml, install.sh, README.md and pyproject.toml; typical tools include bash, code inspection, and editors. -- evidence: [docs/config/tools.md#L30-L30](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L30-L30), [docs/config/tools.md#L11-L13](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L11-L13), [docs/config/tools.md#L19-L28](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L19-L28), [docs/config/tools.md#L15-L15](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L15-L15) (`clm_067eb2c8014a11d047985bcfee103453e823e2032d7943c8f2b8b103657f6cb5`)

## design-choices (2 claim(s))

- [observation/documented] A single YAML configuration governs the agent: it defines tools, prompts shown deterministically or conditionally during a trajectory, demonstrations, model behavior, and the agent-environment input/output interface. -- evidence: [docs/config/config.md#L7-L11](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L7-L11), [README.md#L32-L35](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L32-L35) (`clm_83ef7e99d45bee501f3512b5baaf6fbaa5dd7152c2e0d5c65acbc1eed0f9c84c`)
- [observation/documented] At the start of each run the agent is fed a demonstration trajectory showing how to solve an example issue, which the docs say substantially improves its ability to solve novel issues. -- evidence: [docs/faq.md#L41-L43](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L41-L43) (`clm_609db8841c70095d682e1ac732661bf15109ed8550f693984f4ba2a5c922341c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are welcomed via GitHub issues and pull requests, with discussion in issues encouraged before larger code changes; CI badges show pytest, docs builds, codecov, pre-commit, and link checking. -- evidence: [README.md#L139-L143](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L139-L143), [README.md#L91-L91](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L91-L91) (`clm_05d8b3693196e5dbdaf446f6b3c2e5d82116af3dc955d3dce027b23578d3dea9`)
- [observation/documented] Repository development practice: relative paths in config files resolve to the SWE_AGENT_CONFIG_ROOT environment variable if set, otherwise the repository root. -- evidence: [docs/config/config.md#L39-L41](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L39-L41) (`clm_c657bdca80777e0df4caf25540ef69f81dbe37b2fa030cf08e41f71e1308f0ad`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Configurations are YAML files passed via the --config flag to commands like 'sweagent run' and 'sweagent run-batch'; multiple config files can be given and are merged in a nested way. -- evidence: [docs/config/config.md#L20-L23](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L20-L23), [docs/config/config.md#L5-L5](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L5-L5), [docs/config/config.md#L25-L27](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L25-L27) (`clm_bd553d401c0673abbf71a9748552733091a2d9957534a7ebccd7e1f6e785dc4e`)
- [observation/documented] Multimodal support is provided via config/default_mm_with_images.yaml, which enables GitHub issue image processing to base64, an image_tools bundle, a web_browser bundle, and an image_parsing history processor. -- evidence: [docs/config/config.md#L51-L55](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L51-L55), [docs/config/config.md#L16-L16](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L16-L16), [docs/config/config.md#L59-L70](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L59-L70) (`clm_05528c43d5e9fee1fe2d4db10c2780d030a926c7594d3d8bda04c111a6def000`)

## memory-state (1 claim(s))

- [observation/documented] A special 'state' command runs after every action and returns a JSON string (e.g. current working directory and open file) that is parsed and used to format prompt templates. -- evidence: [docs/config/tools.md#L61-L64](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L61-L64), [docs/config/tools.md#L46-L49](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/tools.md#L46-L49) (`clm_0c956de854f8cbabd045791f03675d66251abc1fb1bb9055d34eda330edbe0b8`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The default response parser is function_calling, but users can configure agent.tools.parse_function to alternatives such as thought_action; custom tools can also be added per a tutorial. -- evidence: [docs/faq.md#L32-L35](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L32-L35), [docs/faq.md#L47-L47](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L47-L47), [docs/faq.md#L45-L45](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L45-L45) (`clm_b897a54d6ce116e473285b6067385118c0e817d05ac59b980e5e84cf95a051d5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] SWEEnv relies on the SWE-ReX package: its Deployment starts a local Docker container or a remote container (e.g. modal or aws) and starts a shell session inside it that executes commands. -- evidence: [docs/background/architecture.md#L17-L17](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L17-L17), [docs/background/architecture.md#L7-L11](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L7-L11) (`clm_b16214a73cf65b452dcaea65c42921655f7e9ffbe1710bfcbb0c9d4972bb1a7c`)
- [observation/documented] The FAQ notes SWE-agent runs on Windows/MacOS/Linux, with the main limitation being availability of Docker containers for the environments; cloud execution is an alternative. -- evidence: [docs/faq.md#L7-L8](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L7-L8), [docs/faq.md#L5-L5](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L5-L5) (`clm_5cc5ec1d110e3874be8228c46db8d04472b0663305c8f0b3b5459b8eb58cb057`)

## limitations (1 claim(s))

- [observation/documented] The EnIGMA offensive-security (CTF) mode currently recommends using SWE-agent 0.7 while EnIGMA is being updated for 1.0. -- evidence: [README.md#L65-L67](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L65-L67) (`clm_36192bb87d43b2124d368c59e36f7fa670d07127cbd0588414ccb0150488786b`)

## relevance (1 claim(s))

- [observation/documented] Development effort has largely moved to mini-SWE-agent, which the maintainers say matches SWE-agent's performance while being much simpler, and they recommend it going forward. -- evidence: [README.md#L19-L24](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L19-L24) (`clm_010850df770996483730a7a309904276ebe4ec30a63cf802defa27809149e677`)

