# yanhua1010/build-your-own-coding-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1e607dbb2f08 @ f0cb08e3c2e0dca7

## Summary (orientation draft, not independently verified)

A Chinese-language tutorial repository that dissects coding-agent internals using the pi project as the main reference (with codex and grok-build for comparison), pairing six published articles with independently runnable mini-agent stages under steps/. The code uses domestic LLM APIs (DeepSeek/GLM/Kimi), runs locally via npm, and is MIT licensed with third-party snippets under their original licenses.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository is a tutorial series that dissects the internals of coding agents layer by layer while building a runnable mini-agent, using three open-source coding agent projects as references. -- evidence: [README.md#L3-L3](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] Six published articles cover the agent loop, unified LLM API and error contracts, tool calling, context compaction and session persistence, and permission/security philosophy, each linked to notes and runnable code. -- evidence: [README.md#L13-L20](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L13-L20)
  - [observation/documented] Each article maps to an independently runnable stage under steps/, starting from a ~100-line minimal loop and progressively adding tool execution, context management, and a TUI. -- evidence: [README.md#L26-L26](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L26-L26)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] A step can be run by exporting DEEPSEEK_API_KEY and executing 'cd steps/01-minimal-loop && npm install && npm start'. -- evidence: [README.md#L30-L32](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L30-L32)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [inference/documented] The mini-agent likely exposes a terminal/TUI interface, since a TUI is listed among the capabilities progressively added in later steps. -- evidence: [README.md#L26-L26](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L26-L26)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The series uses domestic Chinese model APIs (DeepSeek, GLM, Kimi), and the code is stated to run directly locally. -- evidence: [README.md#L9-L9](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L9-L9)
  - [observation/documented] The repository code is MIT licensed; quoted third-party snippets follow their original licenses (pi: MIT; codex and grok-build: Apache-2.0), with copyright retained by the original authors. -- evidence: [README.md#L36-L36](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L36-L36)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The series uses pi (TypeScript, MIT, ~78k stars) as the main teaching text, with codex (Rust, ~101k stars) and grok-build (Rust, ~23k stars) used for architecture comparison. -- evidence: [README.md#L5-L7](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L5-L7)

Every claim for this repository is shown above and in [full detail](build-your-own-coding-agent.detail.md).

Metadata and full claim list: [full detail](build-your-own-coding-agent.detail.md)
Human notes ([notes](build-your-own-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
