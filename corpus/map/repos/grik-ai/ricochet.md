# grik-ai/ricochet

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 706fceac6a3e @ b279f561c72e01dd

## Summary (orientation draft, not independently verified)

Ricochet is an open-source (Apache 2.0) local-first AI coding agent for VS Code-compatible editors and the terminal, with a native Go core, reviewable edits, checkpoints, Grik-hosted and BYOK model access, MCP/skills, and an optional Telegram/Discord Live Mode. Evidence is documentation-only; no runtime code slices are present.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Ricochet is described as an open-source AI coding agent for VS Code-compatible editors and the terminal, letting users plan changes, inspect code, run tools, and review edits. -- evidence: [README.md#L7-L10](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L7-L10)
- components (1 claim(s)):
  - [observation/documented] A native Go core handles planning, tool execution, provider routing, sessions, and terminal/TUI workflows, while the editor UI focuses on conversation, timeline, approvals, and checkpoints. -- evidence: [README.md#L30-L30](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L30-L30)
- design-choices (1 claim(s)):
  - [observation/documented] AI-generated file changes are surfaced for review before being applied, and task-level workspace checkpoints can be restored or compared. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build with ./scripts/build-all.sh and run focused checks including go test ./... in core, npm test/build in webview and extension-vscode, and scripts/check-public-hygiene.sh. -- evidence: [CONTRIBUTING.md#L23-L26](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L23-L26), [CONTRIBUTING.md#L19-L21](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L19-L21), [CONTRIBUTING.md#L30-L32](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L30-L32), [README.md#L110-L112](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L110-L112), [CONTRIBUTING.md#L9-L11](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L9-L11), [README.md#L116-L121](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L116-L121), [CONTRIBUTING.md#L15-L17](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L15-L17)
  - [observation/documented] Repository development practice: PRs should stay focused, include tests for behavior changes, avoid committing generated outputs or local secrets, and keep public docs user-facing. -- evidence: [CONTRIBUTING.md#L36-L39](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L36-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product ships as a VS Code Marketplace extension (grik.ricochet) and also offers a CLI/TUI mode for terminal use. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45), [README.md#L51-L53](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L51-L53), [README.md#L12-L18](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L12-L18)
  - [observation/documented] External tools can be connected via MCP, project-specific instructions can be added as skills, and an optional Live Mode provides Telegram or Discord control for updates and responses away from the IDE. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45)
- memory-state (1 claim(s)):
  - [observation/documented] BYOK provider keys are stored locally (user settings, OS secret store, or environment variables), and the Go core resolves catalog placeholders from the user's environment or local configuration at runtime. -- evidence: [docs/providers.md#L21-L21](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/providers.md#L21-L21), [docs/providers.md#L13-L13](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/providers.md#L13-L13)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent can read files, propose edits, and run commands in the workspace; permissions, approvals, checkpoints, and pending-change review are described as safety controls but explicitly not a complete sandbox. -- evidence: [README.md#L97-L97](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L97-L97), [SECURITY.md#L7-L11](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/SECURITY.md#L7-L11)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](ricochet.detail.md)

Metadata and full claim list: [full detail](ricochet.detail.md)
Human notes ([notes](ricochet.notes.md), never overwritten by build)

[Back to map index](../../index.md)
