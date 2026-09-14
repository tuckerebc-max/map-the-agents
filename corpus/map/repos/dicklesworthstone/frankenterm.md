# dicklesworthstone/frankenterm

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9416f404da44 @ 89d4a383e008b698

## Summary (orientation draft, not independently verified)

Selected evidence records: Repository development practice: releases must go exclusively through Doodlestein Self-Releaser (dsr) — doctor/health, quality, build, release, and verify commands — and GitHub Actions must never be inspected, triggered, or relied on for any claim. Repository development practice: agents may never delete files without explicit written permission, must not use git worktrees, must work on `main` (never `master`), and must avoid destructive commands like `git reset --hard` or `rm -rf` without explicit user authorization.

## Source coverage

Source coverage (partial): 2 of 4 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] `ft` runs as the invoking user with no privilege separation; captured terminal bytes are redacted only on read surfaces, with the on-disk SQLite store holding raw bytes protected by file permissions. -- evidence: [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86), [SECURITY.md#L57-L58](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L57-L58)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: releases must go exclusively through Doodlestein Self-Releaser (dsr) — doctor/health, quality, build, release, and verify commands — and GitHub Actions must never be inspected, triggered, or relied on for any claim. -- evidence: [AGENTS.md#L15-L16](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L15-L16), [AGENTS.md#L23-L33](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L23-L33), [AGENTS.md#L18-L21](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L18-L21), [AGENTS.md#L35-L45](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L35-L45)
  - [observation/documented] Repository development practice: agents may never delete files without explicit written permission, must not use git worktrees, must work on `main` (never `master`), and must avoid destructive commands like `git reset --hard` or `rm -rf` without explicit user authorization. -- evidence: [AGENTS.md#L197-L197](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L197-L197), [AGENTS.md#L187-L191](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L187-L191), [AGENTS.md#L166-L166](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L166-L166), [AGENTS.md#L110-L110](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L110-L110), [AGENTS.md#L112-L112](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L112-L112), [AGENTS.md#L168-L171](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/AGENTS.md#L168-L171)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The stdio MCP transport (`ft mcp serve`) inherits the OS uid/gid with no in-band authentication, while MCP tool inputs are validated via workspace containment, size caps, and approval gating on mutating tools. -- evidence: [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (2 claim(s)):
  - [observation/documented] Per its security policy, the project has no CVE pipeline (fixes tracked by bead and commit) and release artifacts are not yet signed. -- evidence: [SECURITY.md#L104-L110](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L104-L110)
  - [observation/documented] The threat model treats host compromise and pre-existing DB write access as out of scope (attacker-equivalent), and notes findings requiring those positions should be reported as normal bugs. -- evidence: [SECURITY.md#L48-L53](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L48-L53), [SECURITY.md#L60-L86](https://github.com/Dicklesworthstone/frankenterm/blob/9416f404da44cd59c8d95de17c18c94fb8bea2c2/SECURITY.md#L60-L86)
More evidence: [full detail](frankenterm.detail.md)

Metadata and full claim list: [full detail](frankenterm.detail.md)
Human notes ([notes](frankenterm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
