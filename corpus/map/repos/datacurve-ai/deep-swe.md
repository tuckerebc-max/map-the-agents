# datacurve-ai/deep-swe

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0b9fabbb63b9 @ a2fc1feb8fd2295f

## Summary (orientation draft, not independently verified)

DeepSWE is a benchmark of 113 long-horizon software engineering tasks from active open-source projects, run via the Pier/Harbor harness with isolated environments and program-based verifiers. Evidence covers task format, grading flow, verifier outputs, run commands, and licensing provenance.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] DeepSWE is a benchmark measuring frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repositories. -- evidence: [README.md#L3-L3](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L3-L3)
  - [observation/documented] The benchmark comprises 113 tasks spanning TypeScript, Go, Python, JavaScript, and Rust, with isolated environments and program-based verifiers. -- evidence: [README.md#L3-L3](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] The benchmark is run via Pier, installed with uv, using commands like 'pier run -p deep-swe/tasks --agent mini-swe-agent' with model-specific API keys exported. -- evidence: [README.md#L46-L48](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L46-L48), [README.md#L35-L35](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L35-L35), [README.md#L37-L39](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L37-L39), [README.md#L42-L43](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L42-L43)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Tasks use the Harbor task format, with task.toml metadata, instruction.md, an environment Dockerfile, tests, and a held-out reference solution. -- evidence: [README.md#L9-L15](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L9-L15), [README.md#L7-L7](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L7-L7)
  - [observation/documented] Runs can be subsetted deterministically via --n-tasks with --sample-seed, or targeted at a single task by passing a task-id path to pier run. -- evidence: [README.md#L70-L72](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L70-L72), [README.md#L64-L66](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L64-L66), [README.md#L62-L62](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L62-L62)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Since v1.1, grading uses Harbor's separate verifier environment: the agent works in isolation, commits its work, and a collect hook extracts commits as a patch applied and graded in a pristine container. -- evidence: [README.md#L20-L20](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L20-L20)
  - [observation/documented] Pier supports multiple agents: mini-swe-agent is model-agnostic, and Pier also drives claude-code, codex, gemini-cli, and opencode; --env modal runs parallel sandboxes on Modal. -- evidence: [README.md#L58-L58](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L58-L58)
- tools-permissions (1 claim(s)):
  - [observation/documented] Pier, a Harbor-compatible eval framework, adds per-agent network allowlists so agents get only needed network access while the task environment stays isolated, unlike Harbor's blanket blocking in no-internet tasks. -- evidence: [README.md#L52-L52](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L52-L52)
- evaluation (2 claim(s)):
  - [observation/documented] The verifier accepts any solution whose observable behavior is correct, regardless of internal symbol names or structure, and the reference patch is never used at grading time. -- evidence: [README.md#L17-L18](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L17-L18)
  - [observation/documented] Each run produces verifier outputs including reward.json with binary reward and pass fractions, ctrf.json test reports, raw stdout logs, and framework-native grader reports. -- evidence: [README.md#L24-L31](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L24-L31)
- dependencies (2 claim(s)):
More evidence: [full detail](deep-swe.detail.md)

Metadata and full claim list: [full detail](deep-swe.detail.md)
Human notes ([notes](deep-swe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
