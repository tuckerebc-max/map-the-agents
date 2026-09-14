# scaleapi/swe-interact

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b32f98c3b8f7 @ 48f528eef0784222

## Summary (orientation draft, not independently verified)

The repository ships task data under data/multiturn and example run configs under run_configs/multiturn that correspond to that data directory. Running the tasks requires installing Harbor, done by cloning the laude-institute/harbor repository and installing it with uv tool install.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository ships task data under data/multiturn and example run configs under run_configs/multiturn that correspond to that data directory. -- evidence: [README.md#L9-L14](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L9-L14)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Runs are launched from the repository root by executing a run config script, e.g. bash run_configs/multiturn/gpt-5p5-high_codex.sh; a single-turn baseline example is also provided. -- evidence: [README.md#L67-L67](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L67-L67), [README.md#L79-L81](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L79-L81), [README.md#L71-L73](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L71-L73), [README.md#L77-L77](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L77-L77)
  - [observation/documented] Run scripts write outputs under results/, and custom configs are made by copying an existing script and adjusting the agent, model, sampling count, or Harbor arguments. -- evidence: [README.md#L83-L83](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L83-L83)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Run configs load credentials from a harbor/.env file located relative to the repository root, which must be created before launching a run. -- evidence: [README.md#L37-L40](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L37-L40), [README.md#L35-L35](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L35-L35)
  - [observation/documented] Per-agent configs require different credentials: Codex configs need only the common block, Claude Code configs need ANTHROPIC_API_KEY, OpenCode needs GEMINI_API_KEY, and kimi-cli needs an OpenAI-compatible endpoint. -- evidence: [README.md#L57-L63](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L57-L63)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The benchmark uses a simulated user (GPT 5.5 high) and rubric grading; the RF task default rubric model is Anthropic Opus 4.5, matching the original SWE Atlas Refactoring task. -- evidence: [README.md#L44-L44](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L44-L44)
  - [observation/documented] The configured API gateway must support both openai/gpt-5.5 and the rubric model anthropic/claude-opus-4-5-20251101; a LiteLLM gateway works, while direct OpenAI endpoints need an EVAL_MODEL override. -- evidence: [README.md#L51-L51](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L51-L51)
- dependencies (2 claim(s)):
  - [observation/documented] Running the tasks requires installing Harbor, done by cloning the laude-institute/harbor repository and installing it with uv tool install. -- evidence: [README.md#L20-L24](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L20-L24), [README.md#L18-L18](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L18-L18)
  - [observation/documented] Modal is set up to provide sandbox environments, via installing the modal package with uv pip and running modal setup. -- evidence: [README.md#L26-L26](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L26-L26), [README.md#L28-L31](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L28-L31)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](swe-interact.detail.md)

Metadata and full claim list: [full detail](swe-interact.detail.md)
Human notes ([notes](swe-interact.notes.md), never overwritten by build)

[Back to map index](../../index.md)
