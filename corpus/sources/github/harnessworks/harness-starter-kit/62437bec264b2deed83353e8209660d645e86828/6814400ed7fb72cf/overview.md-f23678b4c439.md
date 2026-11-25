# Harness Engineering Overview

Harness engineering is the practice of designing a repository environment so
coding agents can do reliable work inside durable rules.

It is different from prompt engineering. Prompts improve one interaction.
Harnesses improve the project environment.

This starter kit is prompt-first reference material. Give an agent the Git URL
from a target repository, have the agent clone the kit into
`./harness-starter-kit`, read it, and adapt the pattern to the target
repository's actual architecture, tools, and constraints. The optional installer
only bootstraps skeleton files; it does not replace repository inspection or
project-specific adoption.

## The Shift

Software agents can read files, edit code, run tests, and open pull requests.
That autonomy creates a new problem: agents do not automatically know a team's
implicit architecture, taste, history, or rejected approaches.

A harness turns that implicit context into repository artifacts.

For the fuller model and its relationship to test harnesses, CI, ADRs, failure
memory, agent evaluation, and governance loops, see
[`docs/theory/harness-engineering.md`](theory/harness-engineering.md).

## Core Model

```text
Harness = Instructions + Constraints + Feedback + Memory + Evaluation + Governance
```

| Component | Role | Typical Files |
| --- | --- | --- |
| Instructions | Tells the agent how to behave | `AGENTS.md`, `CLAUDE.md` |
| Constraints | Blocks invalid structure | linters, type checks, import rules |
| Feedback | Corrects behavior quickly | tests, CI, pre-commit, examples |
| Memory | Preserves decisions and context | `docs/decisions`, `docs/failures` |
| Evaluation | Separates harness health from agent outcomes | Harness Doctor, effectiveness reports |
| Governance | Keeps the harness current without blind overwrites | `/harness update`, `/harness refresh` |

This starter kit also includes garbage collection, which keeps the harness from
drifting over time.

## Operating Principle

When an agent repeats a mistake, add a durable harness improvement:

- add a specific instruction
- add a test
- add a linter or type check
- add an ADR or failure record
- add a drift check

The goal is not to make agents perfect. The goal is to make the project easier
for agents to understand and harder for them to damage.
