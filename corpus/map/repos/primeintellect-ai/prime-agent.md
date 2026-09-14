# primeintellect-ai/prime-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1fc1adb6e806 @ 500e7d550bac7429

## Summary (orientation draft, not independently verified)

README documents Prime Agent as an open-source self-improving RLM coding/research agent with a persistent Python REPL, subagents, durable harness state, and daemon-backed long-running sessions; AGENTS.md and CONTRIBUTING.md define contributor workflows. No agent-performance evaluation evidence is present.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A persistent Python REPL is the built-in model tool; file operations, shell commands, tool use, subagents, and context management all happen through code in that environment. -- evidence: [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52)
- design-choices (1 claim(s)):
  - [observation/documented] Prime Agent is built around two abstractions: a Recursive Language Model that treats context as variables and subagents as function calls in a persistent REPL, and a Continual Harness storing prompts, memories, skills, and subagent specs as durable state. -- evidence: [README.md#L41-L42](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L41-L42), [README.md#L39-L39](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L39-L39)
- workflows (7 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md requires running 'npm run check' after code changes, forbids npm run dev/build/test, and mandates running any created or modified test file until it passes, using the faux provider harness for coding-agent suite tests. -- evidence: [AGENTS.md#L25-L33](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L25-L33)
  - [observation/documented] Repository development practice: dependency updates are subject to a 7-day minimum release age enforced via .npmrc min-release-age=7 and a matching Dependabot cooldown, with an explicit override flag for urgent security patches. -- evidence: [AGENTS.md#L46-L48](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L46-L48)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are importable Python packages, and a built-in skill creator can turn recurring workflows into project or personal skills. -- evidence: [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI includes commands such as prime-agent agents, attach, --resume, status, doctor, update, and shutdown for browsing sessions, managing background services, and stopping all agents and workers. -- evidence: [README.md#L78-L86](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L78-L86)
  - [observation/documented] Documentation references JSON mode and RPC mode for headless automation and integrations, alongside a TUI for interactive use. -- evidence: [README.md#L100-L108](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L100-L108), [README.md#L89-L89](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L89-L89)
- memory-state (1 claim(s)):
  - [observation/documented] The /refine command reviews the current trajectory and can apply small, evidence-backed updates to supplemental harness state (prompts, memories, skill descriptions, subagent specs), never rewriting the immutable base system prompt, with snapshots supporting rollback. -- evidence: [README.md#L91-L96](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L91-L96), [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52)
- orchestration (2 claim(s)):
  - [observation/documented] rlm.spawn(...) creates real child agents for parallel or background work and returns their results programmatically; running agents can also discover and message each other directly without routing through the user. -- evidence: [README.md#L91-L96](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L91-L96), [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52)
More evidence: [full detail](prime-agent.detail.md)

Metadata and full claim list: [full detail](prime-agent.detail.md)
Human notes ([notes](prime-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
