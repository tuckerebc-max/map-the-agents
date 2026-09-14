# talha-ali-5365/instantrun -- full detail

[Back to orientation](instantrun.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/talha-ali-5365/instantrun/8d0164276f026ac939e4343112edacdb6ba7bf15/aa6519e646d92387.json](../../../wiki/dossiers/talha-ali-5365/instantrun/8d0164276f026ac939e4343112edacdb6ba7bf15/aa6519e646d92387.json)

## specifications (1 claim(s))

- [observation/documented] The tool is described as an AI agent that autonomously deploys GitHub repositories on a user's local machine, handling cloning through command execution in Docker. -- evidence: [README.md#L5-L5](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L5-L5) (`clm_7528710a3a1835c90ad3ae04b1bdd545788679c51d0ba1626aec74f2d8a1a93b`)

## components (1 claim(s))

- [observation/documented] The workflow includes an error-check step where an LLM analyzes terminal output after command execution, and a fix step that may modify the Dockerfile or commands and re-execute them. -- evidence: [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44) (`clm_3fad31d43f1e596cf81f8bd89e8475f4c3632fc97c2821289f0b7b5fc7618dab`)

## design-choices (3 claim(s))

- [observation/documented] The agent uses Docker to provide a consistent, isolated execution environment, creating a Dockerfile when one does not exist in the target repository. -- evidence: [README.md#L19-L25](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L19-L25), [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44) (`clm_3747548af2df89d0d1419b39b254d552d070e58712717ae65893d9b4d81c6c0a`)
- [observation/documented] The LLM is gpt-4o-mini by default, configurable in instantrun.py, and all LLM interactions follow a strict JSON output format for consistent parsing. -- evidence: [README.md#L58-L63](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L58-L63) (`clm_73b179eb63235b1ced60889d5639b43bfa70eeb982461d65a5f87d621769e205`)
- [observation/documented] The tool is designed for Arch Linux but may be adaptable to other Linux distributions with minor modifications; it targets Python 3.10+ for Python projects. -- evidence: [README.md#L58-L63](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L58-L63) (`clm_f74c45ba99c329b85b81575702271bb1256372c3eb1907c8aef43d68db3a0788`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: setup requires installing Python 3.10+, Docker, and pip packages, and setting an OpenAI API key and base URL directly in instantrun.py. -- evidence: [README.md#L48-L50](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L48-L50) (`clm_851213cbfee4bf33a95c5037c21dc697a3f4a4ba890ebf8b3cbf1f90565e0691`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The entry point is a Python script: running 'python main.py' deploys the repository whose URL is set in the github_repo_url variable in main.py. -- evidence: [README.md#L48-L50](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L48-L50), [README.md#L54-L54](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L54-L54) (`clm_3e4135f377cacfe978ac85958ce7dde1211c99677167a74ef8c7c1840062a5ee`)
- [observation/documented] The docker run command is prefixed with 'alacritty -e' to open a new terminal window, so the alacritty terminal must be installed on the user's machine. -- evidence: [README.md#L67-L68](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L67-L68), [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44) (`clm_44ff88ceb5495fa9b8236d32c6c54c66da4d04af1ef67eb5a62f3871eba66ce5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Deployment is driven by a structured LangGraph workflow covering clone, file extraction, setup planning, command execution, error checking, and error fixing steps. -- evidence: [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44), [README.md#L5-L5](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L5-L5) (`clm_3ae8bd61db604055d123b89321f208e6e6f53e929137c30ff73fd40af3057464`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] No benchmark or success-rate evaluation harness appears in the evidence; the only performance indications are two YouTube demo videos of deployments. -- evidence: [README.md#L14-L15](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L14-L15), [README.md#L12-L12](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L12-L12) (`clm_f8e4405a94257d77eead51a58deb8ebdd662cb7934f85cb92b0e2977f59ab356`)

## dependencies (1 claim(s))

- [observation/documented] The project depends on LangGraph (langgraph 0.2.58), LangChain packages including langchain-openai, the Docker SDK (docker 7.1.0), and OpenAI, per the pinned requirements file. -- evidence: [requirements.txt#L1-L144](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/requirements.txt#L1-L144) (`clm_123d86226f0398bb9fdad6aec9ab0bf0c8fdc87bddc7e30cd3f5f4b84104a915`)

## limitations (1 claim(s))

- [observation/documented] The README notes the agent is not perfect and may encounter issues with certain repositories, recommending users review terminal output for errors. -- evidence: [README.md#L67-L68](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L67-L68) (`clm_41d18c70e02adaf81678dd104ec88154575725b7276a7fa54fbd3ec7ba92b01c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

