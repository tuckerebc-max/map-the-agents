# talha-ali-5365/instantrun

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8d0164276f02 @ aa6519e646d92387

## Summary (orientation draft, not independently verified)

InstantRun is a LangGraph-based agent that autonomously clones, plans, and deploys GitHub repositories inside Docker, using an LLM (gpt-4o-mini) for planning, error detection, and fixes. Evidence is mostly README documentation plus a pinned requirements file.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool is described as an AI agent that autonomously deploys GitHub repositories on a user's local machine, handling cloning through command execution in Docker. -- evidence: [README.md#L5-L5](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The workflow includes an error-check step where an LLM analyzes terminal output after command execution, and a fix step that may modify the Dockerfile or commands and re-execute them. -- evidence: [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44)
- design-choices (3 claim(s)):
  - [observation/documented] The agent uses Docker to provide a consistent, isolated execution environment, creating a Dockerfile when one does not exist in the target repository. -- evidence: [README.md#L19-L25](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L19-L25), [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44)
  - [observation/documented] The LLM is gpt-4o-mini by default, configurable in instantrun.py, and all LLM interactions follow a strict JSON output format for consistent parsing. -- evidence: [README.md#L58-L63](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L58-L63)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: setup requires installing Python 3.10+, Docker, and pip packages, and setting an OpenAI API key and base URL directly in instantrun.py. -- evidence: [README.md#L48-L50](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L48-L50)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The entry point is a Python script: running 'python main.py' deploys the repository whose URL is set in the github_repo_url variable in main.py. -- evidence: [README.md#L48-L50](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L48-L50), [README.md#L54-L54](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L54-L54)
  - [observation/documented] The docker run command is prefixed with 'alacritty -e' to open a new terminal window, so the alacritty terminal must be installed on the user's machine. -- evidence: [README.md#L67-L68](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L67-L68), [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Deployment is driven by a structured LangGraph workflow covering clone, file extraction, setup planning, command execution, error checking, and error fixing steps. -- evidence: [README.md#L31-L44](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L31-L44), [README.md#L5-L5](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L5-L5)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] No benchmark or success-rate evaluation harness appears in the evidence; the only performance indications are two YouTube demo videos of deployments. -- evidence: [README.md#L14-L15](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L14-L15), [README.md#L12-L12](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/README.md#L12-L12)
- dependencies (1 claim(s)):
  - [observation/documented] The project depends on LangGraph (langgraph 0.2.58), LangChain packages including langchain-openai, the Docker SDK (docker 7.1.0), and OpenAI, per the pinned requirements file. -- evidence: [requirements.txt#L1-L144](https://github.com/Talha-Ali-5365/InstantRun/blob/8d0164276f026ac939e4343112edacdb6ba7bf15/requirements.txt#L1-L144)
- limitations (1 claim(s)):
More evidence: [full detail](instantrun.detail.md)

Metadata and full claim list: [full detail](instantrun.detail.md)
Human notes ([notes](instantrun.notes.md), never overwritten by build)

[Back to map index](../../index.md)
