# codebuffai/freebuff

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: codebuffai/codebuff (github id 826515105).
Latest snapshot: commit 654a906e6758 @ eb011fd48855153f

## Summary (orientation draft, not independently verified)

The snapshot is documentation-only (READMEs and docs) for Freebuff, a free multi-product AI coding suite built on the Codebuff framework, plus contributor testing/CI guidance. No source code slices are present, so claims are documented behavior and development practice. Evidence coverage: 131 of 224 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Freebuff ships five products: Desktop (parallel local agents), CLI, Web (full-stack app building), Cloud (agents on GitHub repos), and Chat. -- evidence: [README.md#L11-L17](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L11-L17)
- design-choices (2 claim(s)):
  - [observation/documented] Freebuff uses specialized agents rather than one model and prompt; agents gather context, plan, edit, research, run tools, and review results. -- evidence: [README.md#L57-L57](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L57-L57)
  - [observation/documented] The run_terminal_command tool separates process ownership from terminal UI ownership via a broker; a broker startup failure prevents the shell from running with no direct-console fallback. -- evidence: [docs/agents-and-tools.md#L24-L24](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L24-L24), [docs/agents-and-tools.md#L26-L45](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L26-L45)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors clone, run 'bun install' and 'bun up', start the CLI with 'bun start-cli', and consult the contributing, development, and testing guides before opening a PR. -- evidence: [README.md#L88-L93](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L88-L93), [README.md#L101-L101](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L101-L101), [README.md#L97-L99](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L97-L99)
  - [observation/documented] Repository development practice: CI runs tests through scripts/ci/test-with-guard.ts, which fails the build on errors outside test bodies or on test/file counts below a recorded baseline in .github/test-baselines.json. -- evidence: [docs/testing.md#L27-L28](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/testing.md#L27-L28), [docs/testing.md#L25-L25](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/testing.md#L25-L25)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI is installed globally via npm and run with the 'freebuff' command inside a project directory. -- evidence: [README.md#L23-L27](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L23-L27)
  - [observation/documented] Shell shims let users invoke agents as direct commands without a 'codebuff' prefix, installed via 'codebuff shims install' and an env eval. -- evidence: [docs/agents-and-tools.md#L10-L10](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L10-L10), [docs/agents-and-tools.md#L12-L16](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/docs/agents-and-tools.md#L12-L16)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Freebuff is built on the Codebuff open multi-agent framework, which powers its orchestration, tools, and SDK; custom agents can use @codebuff/sdk. -- evidence: [README.md#L105-L105](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L105-L105)
  - [observation/documented] The repository is a TypeScript monorepo built with Bun, and local development requires Docker and a configured .env.local. -- evidence: [README.md#L83-L83](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L83-L83), [README.md#L85-L86](https://github.com/CodebuffAI/freebuff/blob/654a906e6758ffe17974dae829d35423dcd827b3/README.md#L85-L86)
- limitations (2 claim(s)):
More evidence: [full detail](freebuff.detail.md)

Metadata and full claim list: [full detail](freebuff.detail.md)
Human notes ([notes](freebuff.notes.md), never overwritten by build)

[Back to map index](../../index.md)
