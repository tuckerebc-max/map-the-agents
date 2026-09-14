# withastro/flue

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1ae1c85dae55 @ e9dc4791c6cf7883

## Summary (orientation draft, not independently verified)

Flue is a TypeScript framework for building autonomous agents as exported functions composed via hooks (model, sandbox, skills, tools), shipped as multiple packages with a CLI, SDK, and durable sessions. Contribution policy accepts only bug reports and feature requests (PRs are auto-closed), under an AI-agent-driven 'Surgical Team' development model.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Agents are exported TypeScript functions marked with a 'use agent' directive; hooks like useModel, useSandbox, useSkill, and useTool compose capabilities, and the function's returned string is its instruction. -- evidence: [README.md#L30-L32](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L30-L32), [README.md#L14-L22](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L14-L22), [README.md#L5-L12](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L5-L12), [README.md#L24-L28](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L24-L28)
- components (1 claim(s)):
  - [observation/documented] The repository ships @flue/runtime (harness, sessions, tools, sandbox), @flue/vite (build plugin), @flue/cli (flue binary), @flue/sdk (client for deployed agent conversations), @flue/opentelemetry, and @flue/postgres. -- evidence: [README.md#L67-L74](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L67-L74)
- design-choices (1 claim(s)):
  - [observation/documented] The built-in TypeScript harness gives models sessions, tools, skills, instructions, filesystem access, and a secure sandbox; agents run locally via CLI or deploy to a hosted runtime. -- evidence: [README.md#L40-L40](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L40-L40)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: pull requests are not accepted and are automatically closed and converted into bug reports (GitHub issues) or feature requests (discussions), with agent-oriented templates also provided. -- evidence: [CONTRIBUTING.md#L11-L16](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L11-L16), [CONTRIBUTING.md#L20-L20](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/CONTRIBUTING.md#L20-L20), [AGENTS.md#L9-L11](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/AGENTS.md#L9-L11)
  - [observation/documented] Repository development practice: development uses pnpm in a turbo workspace, with commands for install, build, typechecking (excluding apps-www), and formatting. -- evidence: [AGENTS.md#L48-L53](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/AGENTS.md#L48-L53)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes a `flue` binary for local runs, blueprints, and offline docs; @flue/sdk is a client SDK for consuming deployed agent conversations. -- evidence: [README.md#L67-L74](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L67-L74)
  - [observation/documented] Documented deployment targets include Node.js, Cloudflare Workers, GitHub Actions, GitLab CI/CD, and Render; Daytona appears as a sandbox option rather than a deployment target. -- evidence: [README.md#L58-L63](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L58-L63)
- memory-state (1 claim(s)):
  - [observation/documented] Agents keep context across conversations and events, and preserve progress through failures and restarts via durable recovery for accepted work. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54)
- orchestration (1 claim(s)):
  - [observation/documented] The framework supports subagents: specialized roles can be defined for different tasks, and the agent can delegate work to the appropriate expert. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Agents can connect to authenticated tools and services through MCP servers, and telemetry can be exported via OpenTelemetry and Braintrust. -- evidence: [README.md#L46-L54](https://github.com/withastro/flue/blob/1ae1c85dae55e7b1215a6dc233796d36ec7d7c25/README.md#L46-L54)
More evidence: [full detail](flue.detail.md)

Metadata and full claim list: [full detail](flue.detail.md)
Human notes ([notes](flue.notes.md), never overwritten by build)

[Back to map index](../../index.md)
