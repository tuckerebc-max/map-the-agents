# swe-agent/swe-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3ea751c087f3 @ 9b7bae7bd10c873c

## Summary (orientation draft, not independently verified)

Evidence covers SWE-agent's README and docs: an agent framework that lets LLMs use tools to fix GitHub issues, configured via YAML, built on SWE-ReX/Docker, with an EnIGMA cybersecurity mode and a successor project mini-SWE-agent. No code internals beyond documented architecture are shown.

## Source coverage

Source coverage (partial): 6 of 59 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SWE-agent enables a user-chosen language model (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories, find cybersecurity vulnerabilities, or perform custom tasks. -- evidence: [README.md#L27-L30](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L27-L30)
- components (3 claim(s)):
  - [observation/documented] The central entry point is the sweagent CLI, which initializes a SWEEnv environment wrapper (a thin wrapper around SWE-ReX since 1.0) and an Agent class whose forward() method prompts the model and executes its action. -- evidence: [docs/background/architecture.md#L13-L13](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L13-L13), [docs/background/architecture.md#L7-L11](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L7-L11)
  - [observation/documented] A HistoryProcessor compresses the conversation history to make best use of the model's context window, and a parser extracts the action from the model output before it is executed in the shell session via SWEEnv. -- evidence: [docs/background/architecture.md#L15-L15](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/background/architecture.md#L15-L15)
- design-choices (2 claim(s)):
  - [observation/documented] A single YAML configuration governs the agent: it defines tools, prompts shown deterministically or conditionally during a trajectory, demonstrations, model behavior, and the agent-environment input/output interface. -- evidence: [docs/config/config.md#L7-L11](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L7-L11), [README.md#L32-L35](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L32-L35)
  - [observation/documented] At the start of each run the agent is fed a demonstration trajectory showing how to solve an example issue, which the docs say substantially improves its ability to solve novel issues. -- evidence: [docs/faq.md#L41-L43](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/faq.md#L41-L43)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are welcomed via GitHub issues and pull requests, with discussion in issues encouraged before larger code changes; CI badges show pytest, docs builds, codecov, pre-commit, and link checking. -- evidence: [README.md#L139-L143](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L139-L143), [README.md#L91-L91](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md#L91-L91)
  - [observation/documented] Repository development practice: relative paths in config files resolve to the SWE_AGENT_CONFIG_ROOT environment variable if set, otherwise the repository root. -- evidence: [docs/config/config.md#L39-L41](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L39-L41)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Configurations are YAML files passed via the --config flag to commands like 'sweagent run' and 'sweagent run-batch'; multiple config files can be given and are merged in a nested way. -- evidence: [docs/config/config.md#L20-L23](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L20-L23), [docs/config/config.md#L5-L5](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L5-L5), [docs/config/config.md#L25-L27](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L25-L27)
  - [observation/documented] Multimodal support is provided via config/default_mm_with_images.yaml, which enables GitHub issue image processing to base64, an image_tools bundle, a web_browser bundle, and an image_parsing history processor. -- evidence: [docs/config/config.md#L51-L55](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L51-L55), [docs/config/config.md#L16-L16](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L16-L16), [docs/config/config.md#L59-L70](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/docs/config/config.md#L59-L70)
- memory-state (1 claim(s)):
More evidence: [full detail](swe-agent.detail.md)

Metadata and full claim list: [full detail](swe-agent.detail.md)
Human notes ([notes](swe-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
