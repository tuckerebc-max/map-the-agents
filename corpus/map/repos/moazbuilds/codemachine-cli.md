# moazbuilds/codemachine-cli

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 572def63eb80 @ 3c737dd66b55d243

## Summary (orientation draft, not independently verified)

Selected evidence records: The tool is distributed as an npm package installable globally via 'npm i -g codemachine'. CodeMachine is an orchestration layer that runs AI coding CLIs through structured workflows, handling execution, context passing, and agent coordination.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A default workflow called the Ali Workflow Builder is included for creating workflows interactively. -- evidence: [README.md#L38-L38](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L38-L38)
- design-choices (1 claim(s)):
  - [observation/documented] Workflows can range from fully interactive to fully autonomous, with documentation on orchestration patterns available. -- evidence: [README.md#L34-L34](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L34-L34)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors need Bun 1.3+, install with 'bun install', start with 'bun dev', and run 'bun run lint' and 'bun run typecheck' before submitting PRs. -- evidence: [CONTRIBUTING.md#L41-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L41-L44), [CONTRIBUTING.md#L19-L22](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L19-L22), [CONTRIBUTING.md#L15-L15](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L15-L15)
  - [observation/documented] Repository development practice: UI and feature PRs require prior team review or will likely be refused; PRs should be focused on one feature or fix. -- evidence: [CONTRIBUTING.md#L11-L11](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L11-L11), [CONTRIBUTING.md#L46-L46](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L46-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The tool is distributed as an npm package installable globally via 'npm i -g codemachine'. -- evidence: [README.md#L5-L7](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L5-L7)
- memory-state (1 claim(s)):
  - [observation/documented] The tool centralizes prompts and manages dynamic context, controlling what each agent sees at each workflow step. -- evidence: [README.md#L40-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L40-L44)
- orchestration (4 claim(s)):
  - [observation/documented] CodeMachine is an orchestration layer that runs AI coding CLIs through structured workflows, handling execution, context passing, and agent coordination. -- evidence: [README.md#L29-L29](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L29-L29)
  - [observation/documented] It spawns AI coding engines via CLI using their headless scripting mode, passing appropriate arguments and flags to control agents. -- evidence: [README.md#L32-L32](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L32-L32)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The tool integrates multiple AI engines, including Claude Code, Codex, Cursor, CCR (Claude Code Router), OpenCode CLI, Auggie CLI, and Mistral Vibe, per contributor notes. -- evidence: [CONTRIBUTORS.md#L17-L17](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L17-L17), [README.md#L32-L32](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L32-L32), [CONTRIBUTORS.md#L29-L29](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L29-L29), [CONTRIBUTORS.md#L20-L20](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L20-L20), [CONTRIBUTORS.md#L11-L11](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L11-L11)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](codemachine-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](codemachine-cli.detail.md)
Human notes ([notes](codemachine-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
