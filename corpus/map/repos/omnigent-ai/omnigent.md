# omnigent-ai/omnigent

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 270eca52b1e0 @ 94cb8b38f0cdc681

## Summary (orientation draft, not independently verified)

Omnigent is an open-source meta-harness providing a common orchestration layer over multiple coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and YAML-defined custom agents), with a CLI/server/web-UI architecture, policy-based governance, cloud sandbox execution, and multi-device collaboration. Evidence is documentation-based (README); contributor guidance in AGENTS.md is reported only as repository development practice. Evidence coverage: 158 of 161 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 36 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Omnigent is described as an open-source meta-harness providing a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and self-written agents, allowing harness swapping without rewrites. -- evidence: [README.md#L7-L7](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] Agents are defined in YAML files declaring a prompt, an executor harness (e.g. claude-sdk, codex, cursor, pi, openai-agents), tools including local Python functions, MCP servers, and delegatable sub-agents. -- evidence: [README.md#L574-L577](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L574-L577), [README.md#L583-L586](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L583-L586), [README.md#L594-L597](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L594-L597), [README.md#L599-L605](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L599-L605), [README.md#L588-L592](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L588-L592)
- design-choices (1 claim(s)):
  - [observation/documented] On Linux, native harness terminal wrappers and the pi harness sandbox each agent terminal with bubblewrap, and that isolation is mandatory; macOS uses the built-in seatbelt sandbox instead. -- evidence: [README.md#L139-L165](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L139-L165)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs AI contributors to run the pre-commit hook before committing and fix reported issues so commits land clean, since CI runs the same checks. -- evidence: [AGENTS.md#L8-L10](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L8-L10)
  - [observation/documented] Repository development practice: contributors use 'just' recipes for common tasks (ensure, dev, lint, electron builds, lockfile normalization) and must fill in the repo's PR template with summary, test plan, and demo sections. -- evidence: [AGENTS.md#L14-L14](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L14-L14), [AGENTS.md#L25-L27](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L25-L27), [AGENTS.md#L29-L38](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L29-L38), [AGENTS.md#L16-L21](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L16-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI exposes per-harness launchers such as omnigent claude, codex, cursor, agy, opencode, hermes, and pi, plus an interchangeable short alias 'omni' installed alongside the main command. -- evidence: [README.md#L278-L286](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L278-L286), [README.md#L263-L265](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L263-L265)
  - [observation/documented] Running omnigent starts a terminal session and a local web UI at http://localhost:6767 showing the same session; a macOS desktop app wraps that UI with OS notifications and a dock badge. -- evidence: [README.md#L14-L14](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L14-L14), [README.md#L256-L261](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L256-L261)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions follow the user across devices: started in a terminal, they continue in the browser or on a phone, with messages, sub-agents, terminals, and files staying in sync. -- evidence: [README.md#L28-L30](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L28-L30)
- orchestration (2 claim(s)):
More evidence: [full detail](omnigent.detail.md)

Metadata and full claim list: [full detail](omnigent.detail.md)
Human notes ([notes](omnigent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
