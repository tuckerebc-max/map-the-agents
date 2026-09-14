# opensource03/harnss

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dc1dfd8a33ca @ 3c8c248556fb7ab2

## Summary (orientation draft, not independently verified)

Harnss is a cross-platform desktop app for running and switching between AI coding agents (Claude Code, Codex, ACP-compatible) with per-project workspaces, MCP/git/terminal/browser panels, and permission controls; the README states it is in early development pending a large rewrite. Evidence is README-only; no runtime code is shown.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (5 claim(s)):
  - [observation/documented] The app supports three execution engines: Claude Code via the Anthropic Agent SDK, Codex via a JSON-RPC app-server, and ACP agents via the Agent Client Protocol. -- evidence: [README.md#L149-L153](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L149-L153)
  - [observation/documented] MCP servers can be connected per project over stdio, SSE, or HTTP transports, with in-app OAuth handling and token persistence across sessions. -- evidence: [README.md#L97-L97](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L97-L97), [README.md#L173-L173](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L173-L173)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors should fork the repo, create a feature branch, follow conventions in CLAUDE.md, test with pnpm dev, and open a pull request; local development uses pnpm install and pnpm dev. -- evidence: [README.md#L213-L216](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L213-L216), [README.md#L194-L199](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L194-L199)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Harnss is a cross-platform desktop app providing a single interface to run, manage, and switch between AI coding agents including Claude Code, Codex, and ACP-compatible agents. -- evidence: [README.md#L26-L26](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L26-L26)
  - [observation/documented] Tool calls render as interactive cards with word-level diffs, syntax highlighting, inline bash output, nested subagent progress tracking, and a per-turn Changes panel. -- evidence: [README.md#L93-L93](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L93-L93)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions, history, and panel settings are scoped per project; projects map to disk folders and can be grouped into named Spaces with custom icons and colors. -- evidence: [README.md#L109-L109](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L109-L109)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product offers three permission levels (Ask First, Accept Edits, Allow All) plus a plan mode where the agent drafts a plan before changes; modes can be switched mid-session without losing context. -- evidence: [README.md#L117-L117](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L117-L117)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Running Claude Code requires a Claude account (subscription or API key); Codex requires the Codex CLI in PATH plus an OpenAI API key or ChatGPT account; ACP agents have agent-specific requirements. -- evidence: [README.md#L149-L153](https://github.com/OpenSource03/harnss/blob/dc1dfd8a33caa46a1eefcfe9e14697b27ac4c33d/README.md#L149-L153)
- limitations (2 claim(s)):
More evidence: [full detail](harnss.detail.md)

Metadata and full claim list: [full detail](harnss.detail.md)
Human notes ([notes](harnss.notes.md), never overwritten by build)

[Back to map index](../../index.md)
