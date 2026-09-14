# factory-ai/factory

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eb4c4e381fd7 @ b15ed6fa8ebff7dd

## Summary (orientation draft, not independently verified)

The snapshot contains only top-level README/docs content: Factory describes an agent-native development platform with a CLI agent called Droid, plus installation instructions, SDK links, and a Mintlify-based docs workflow. No source code or runtime internals are present in the evidence.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Separate TypeScript and Python SDK repositories for Droid are linked from the README. -- evidence: [README.md#L52-L53](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L52-L53)
  - [observation/documented] A Droid GitHub Action is referenced that runs AI-powered code reviews, security scans, and PR description generation on pull requests. -- evidence: [README.md#L57-L57](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L57-L57)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: docs contributors install the Mintlify CLI globally and run `mintlify dev` at the docs root (where docs.json lives) to preview changes locally. -- evidence: [docs/README.md#L21-L23](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L21-L23), [docs/README.md#L15-L17](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L15-L17), [docs/README.md#L19-L19](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L19-L19), [docs/README.md#L13-L13](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L13-L13)
  - [observation/documented] Repository development practice: troubleshooting guidance says to run `mintlify install` if the dev server fails, and that 404s usually mean the wrong folder (docs.json missing). -- evidence: [docs/README.md#L31-L32](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L31-L32)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Factory is described as an agent-native development platform available across CLI, Web, Slack/Teams, Linear/Jira, and Mobile. -- evidence: [README.md#L3-L3](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L3-L3)
  - [observation/documented] The product's agent is named Droid and is distributed as a CLI; users start a session by running `droid` inside a project directory. -- evidence: [README.md#L31-L31](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L31-L31), [README.md#L33-L36](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L33-L36), [README.md#L5-L5](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L5-L5)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README claims Droid is top performing in terminal benchmarks; this is a self-reported marketing statement, not an eval harness in the repo. -- evidence: [README.md#L5-L5](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L5-L5)
- dependencies (1 claim(s)):
  - [observation/documented] Installation options include a curl shell script for macOS/Linux, a PowerShell command for Windows, and a global npm install of the `droid` package. -- evidence: [README.md#L15-L17](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L15-L17), [README.md#L27-L29](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L27-L29), [README.md#L21-L23](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L21-L23)
- limitations (1 claim(s)):
  - [inference/documented] The evidence consists only of README/docs marketing and setup text; no source code appears in the snapshot, so runtime internals of Droid cannot be verified from this evidence. -- evidence: [README.md#L71-L71](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L71-L71), [README.md#L3-L3](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](factory.detail.md) for every claim.)

Metadata and full claim list: [full detail](factory.detail.md)
Human notes ([notes](factory.notes.md), never overwritten by build)

[Back to map index](../../index.md)
