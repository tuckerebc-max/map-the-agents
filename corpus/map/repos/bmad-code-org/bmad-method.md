# bmad-code-org/bmad-method

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 94b6727b00c8 @ bdd9c2fe28189310

## Summary (orientation draft, not independently verified)

The snapshot contains multilingual READMEs and a removals list documenting BMad Method, an agile AI-driven development method installed via skills CLI, npm, or plugin marketplaces, with a `bmad` hub skill, `bmad-build`, `bmad-help`, and `bmad doctor` runtime commands, plus an official module ecosystem. Contributor-credit policy appears in CONTRIBUTORS.md; no agent performance evaluation is evidenced.

## Source coverage

Source coverage (partial): 6 of 205 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] An official module ecosystem is documented, including BMad Builder (skill/workflow/agent builder), Test Architect, Creative Intelligence Suite, BMad Loop (unattended epic build/verify/retro), and Game Dev Studio. -- evidence: [README_CN.md#L49-L49](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README_CN.md#L49-L49), [README.md#L74-L81](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L74-L81)
- design-choices (2 claim(s)):
  - [observation/documented] The method is described as right-sizing process to the work: small clear changes go straight to build, larger initiatives get deeper planning, and it supports both new and existing codebases. -- evidence: [README.md#L61-L66](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L61-L66), [README.md#L10-L10](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L10-L10)
  - [observation/documented] BMad emphasizes keeping decisions explicit and carrying product/technical context forward, with specialized agent perspectives (product, architecture, UX, development, testing) and multi-agent discussions. -- evidence: [README.md#L61-L66](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L61-L66), [README.md#L59-L59](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L59-L59)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to read CONTRIBUTING.md before opening a pull request, and CONTRIBUTORS.md states any merged pull request makes someone a contributor with no minimum contribution requirements. -- evidence: [CONTRIBUTORS.md#L22-L22](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/CONTRIBUTORS.md#L22-L22), [README.md#L105-L105](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L105-L105), [CONTRIBUTORS.md#L13-L13](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/CONTRIBUTORS.md#L13-L13)
- skills-patterns (1 claim(s)):
  - [observation/documented] Documented skills include `bmad-build` for implementing a requested change, `bmad-help` for guidance on required versus optional next steps, `bmad setup`, and `bmad doctor` to repair the project's existing runtime after updates. -- evidence: [README.md#L44-L46](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L44-L46), [README.md#L52-L55](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L52-L55), [README_CN.md#L45-L45](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README_CN.md#L45-L45)
- interfaces (4 claim(s)):
  - [observation/documented] The method is installed into a project via `npx skills add bmad-code-org/BMAD-METHOD`, letting users select skills and a target coding tool, including a `bmad` skill for setup and help. -- evidence: [README.md#L27-L27](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L27-L27), [README.md#L23-L25](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L23-L25)
  - [observation/documented] Alternative install routes exist as Claude Code and Codex plugin marketplaces (`bmad-code-org/bmad-plugins`), offering `bmad-method` for delivery workflows and `bmad-toolbox` for standalone skills. -- evidence: [README.md#L37-L39](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L37-L39), [README.md#L31-L33](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L31-L33), [README.md#L41-L42](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L41-L42)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Prerequisites vary by README: the English README requires a skills-capable AI coding tool plus uv; the Korean README lists Node.js 20.12+, Python 3.10+, and uv; the Chinese README lists Node.js v20+. -- evidence: [README.md#L18-L19](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README.md#L18-L19), [README_CN.md#L29-L29](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README_CN.md#L29-L29), [README_KR.md#L19-L19](https://github.com/bmad-code-org/BMAD-METHOD/blob/94b6727b00c8316557828c8a8ff2a48ff60d60cc/README_KR.md#L19-L19)
More evidence: [full detail](bmad-method.detail.md)

Metadata and full claim list: [full detail](bmad-method.detail.md)
Human notes ([notes](bmad-method.notes.md), never overwritten by build)

[Back to map index](../../index.md)
