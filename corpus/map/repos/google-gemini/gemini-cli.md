# google-gemini/gemini-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9c1b0a610534 @ 65fb3d86d9eafaa4

## Summary (orientation draft, not independently verified)

Selected evidence records: Gemini CLI is an open-source AI agent that brings Gemini into the terminal, providing lightweight access from the user's prompt to the model. Built-in tools include Google Search grounding, file operations, shell commands, and web fetching, with MCP support for custom integrations.

## Source coverage

Source coverage (partial): 6 of 102 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Gemini CLI is an open-source AI agent that brings Gemini into the terminal, providing lightweight access from the user's prompt to the model. -- evidence: [README.md#L11-L13](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L11-L13)
- components (1 claim(s)):
  - [observation/documented] Built-in tools include Google Search grounding, file operations, shell commands, and web fetching, with MCP support for custom integrations. -- evidence: [README.md#L19-L28](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L19-L28)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm run test for unit tests, test:e2e for integration, and preflight (clean, install, build, lint, type check, tests) before submitting PRs. -- evidence: [GEMINI.md#L44-L65](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L44-L65)
  - [observation/documented] Repository development practice: PRs should be small and issue-linked, commits follow Conventional Commits, and new source files need Apache-2.0 license headers enforced by ESLint. -- evidence: [GEMINI.md#L69-L80](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L69-L80)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports non-interactive scripting via -p, with --output-format json for structured output and stream-json for newline-delimited event streaming. -- evidence: [README.md#L240-L242](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L240-L242), [README.md#L251-L252](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L251-L252), [README.md#L244-L245](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L244-L245), [README.md#L254-L256](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L254-L256)
  - [observation/documented] CLI flags include --include-directories for multiple directories, -m for model selection, and -s for sandboxing. -- evidence: [README.md#L226-L228](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L226-L228), [docs/cli/sandbox.md#L41-L43](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L41-L43), [README.md#L232-L234](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L232-L234)
- memory-state (2 claim(s)):
  - [observation/documented] The agent persists durable facts by editing Markdown memory files, routing shared project instructions to GEMINI.md and personal preferences to the global ~/.gemini/GEMINI.md. -- evidence: [docs/tools/memory.md#L8-L11](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L8-L11), [docs/tools/memory.md#L3-L4](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L3-L4)
  - [observation/documented] Stored memories are edited with write_file or replace and are automatically included in the hierarchical context system for all future sessions. -- evidence: [docs/tools/memory.md#L15-L19](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L15-L19)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (3 claim(s)):
  - [observation/documented] Sandboxing can be enabled via the -s/--sandbox flag, the GEMINI_SANDBOX env var, or settings.json, with providers including docker, podman, sandbox-exec, runsc, and lxc. -- evidence: [docs/cli/sandbox.md#L75-L79](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L75-L79)
  - [observation/documented] A sandbox expansion mechanism detects permission denials or proactively identified needs and shows a modal request; approval grants extended permissions for that specific run. -- evidence: [docs/cli/sandbox.md#L298-L299](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L298-L299), [docs/cli/sandbox.md#L301-L304](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L301-L304), [docs/cli/sandbox.md#L308-L313](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L308-L313)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](gemini-cli.detail.md)

Metadata and full claim list: [full detail](gemini-cli.detail.md)
Human notes ([notes](gemini-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
