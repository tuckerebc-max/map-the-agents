# getkimchi/kimchi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 15cdadae0c44 @ 2a86d2323cfc7801

## Summary (orientation draft, not independently verified)

The README documents kimchi, a terminal coding agent CLI built on the pi-mono SDK, with multi-model orchestration, Ferment project persistence, LSP tools, remote cloud sessions, and migration from other coding agents. Development/build instructions appear only in the latter sections and are kept under workflows. Evidence coverage: 147 of 310 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Kimchi ships built-in LSP support loaded by default, exposing tools such as lsp_diagnostics, lsp_hover, lsp_definition, lsp_references, and lsp_rename; servers are auto-detected on PATH and file edits sync to the language server. -- evidence: [README.md#L348-L348](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L348-L348), [README.md#L340-L346](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L340-L346), [README.md#L327-L327](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L327-L327), [README.md#L336-L336](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L336-L336)
  - [observation/documented] On first run kimchi detects Claude Code, OpenCode, or Cursor installations and offers one-shot migration of their MCP servers and skills, merging discovered servers into `~/.config/kimchi/harness/mcp.json` with existing Kimchi entries winning collisions. -- evidence: [README.md#L497-L497](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L497-L497), [README.md#L481-L481](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L481-L481), [README.md#L515-L517](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L515-L517)
- design-choices (2 claim(s)):
  - [observation/documented] Workspace sizing is declared in a root-level `kimchi_workspace.yaml` using Kubernetes quantity strings; invalid or unknown fields are refused with the field named, and sizing applies only at workspace creation since resources are immutable. -- evidence: [README.md#L399-L399](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L399-L399), [README.md#L397-L397](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L397-L397), [README.md#L387-L387](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L387-L387)
  - [observation/documented] A bash-tool guard steers the model away from shell commands that duplicate dedicated tools, flagging patterns like `cat`, `sed -i`, and output redirection, and suggesting read/edit/write instead; stream targets like /dev/null are exempt. -- evidence: [docs/bash-tool-guard.md#L3-L6](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/docs/bash-tool-guard.md#L3-L6), [docs/bash-tool-guard.md#L16-L17](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/docs/bash-tool-guard.md#L16-L17), [docs/bash-tool-guard.md#L10-L14](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/docs/bash-tool-guard.md#L10-L14)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: prerequisites are Node.js 22 LTS, Bun, corepack, and pnpm; `./scripts/dev-startup.sh` bootstraps the environment, and `pnpm run check`, `lint`, `test` (vitest), and `test:smoke` cover linting, type checking, and tests. -- evidence: [README.md#L538-L538](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L538-L538), [README.md#L534-L536](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L534-L536), [README.md#L553-L561](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L553-L561), [README.md#L527-L530](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L527-L530)
  - [observation/documented] Repository development practice: standalone binaries are built automatically by GitHub Actions on version tags using `bun build --compile`, producing tarballs/zip plus SHA256 checksums for macOS, Linux, and Windows. -- evidence: [README.md#L628-L628](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L628-L628), [README.md#L636-L636](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L636-L636), [README.md#L632-L634](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L632-L634)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Kimchi is a terminal coding agent CLI; users configure an API key via an interactive `kimchi setup` command and launch the agent with `kimchi`, with `--help` listing subcommands and flags. -- evidence: [README.md#L31-L34](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L31-L34), [README.md#L3-L3](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L3-L3), [README.md#L36-L36](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L36-L36)
  - [observation/documented] Installation paths include Homebrew (`getkimchi/tap/kimchi`), a curl install script for macOS/Linux, and a PowerShell one-liner for Windows. -- evidence: [README.md#L13-L15](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L13-L15), [README.md#L19-L21](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L19-L21), [README.md#L25-L27](https://github.com/getkimchi/kimchi/blob/15cdadae0c4459d47675398a95f125def4cba71f/README.md#L25-L27)
- memory-state (3 claim(s)):
More evidence: [full detail](kimchi.detail.md)

Metadata and full claim list: [full detail](kimchi.detail.md)
Human notes ([notes](kimchi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
