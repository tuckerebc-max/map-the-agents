# d-kuro/gwq

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c4247734968b @ 554853775b2f91fa

## Summary (orientation draft, not independently verified)

Selected evidence records: The status command supports watch mode, filtering, sorting, and JSON/CSV output formats per its documented flags. gwq generates shell completions for Bash, Zsh, Fish, and PowerShell via a completion subcommand.

## Source coverage

Source coverage (partial): 6 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Per-repository setup_commands are rendered with Go text/template (variables like {{.Branch}} and {{.Path}}) and executed via POSIX sh -c; unknown template keys cause the command to be skipped with an error logged. -- evidence: [README.md#L393-L393](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L393-L393), [README.md#L410-L410](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L410-L410), [README.md#L384-L391](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L384-L391), [README.md#L382-L382](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L382-L382)
- design-choices (3 claim(s)):
  - [observation/documented] Worktrees are organized in a URL-based hierarchy (e.g. ~/worktrees/github.com/user/repo/branch) to prevent naming conflicts, with a configurable naming template. -- evidence: [docs/release-notes/v0.0.1.md#L13-L16](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L13-L16), [README.md#L464-L464](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L464-L464), [README.md#L479-L479](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L479-L479), [README.md#L466-L477](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L466-L477), [README.md#L335-L337](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L335-L337)
  - [observation/documented] Global worktree discovery uses filesystem scanning of a configured base directory rather than a separate registry, and behavior is context-aware inside versus outside Git repositories. -- evidence: [docs/release-notes/v0.0.1.md#L13-L16](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L13-L16), [README.md#L278-L280](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L278-L280), [README.md#L276-L276](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L276-L276)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: release notes state that comprehensive release documentation was added at docs/RELEASING.md, including step-by-step instructions, a notes template, and a release checklist. -- evidence: [docs/release-notes/v0.0.10.md#L37-L37](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L37-L37), [docs/release-notes/v0.0.10.md#L39-L43](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L39-L43)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The status command supports watch mode, filtering, sorting, and JSON/CSV output formats per its documented flags. -- evidence: [README.md#L216-L216](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L216-L216), [README.md#L213-L213](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L213-L213), [README.md#L210-L210](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L210-L210), [README.md#L223-L223](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L223-L223), [README.md#L219-L221](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L219-L221)
  - [observation/documented] gwq generates shell completions for Bash, Zsh, Fish, and PowerShell via a completion subcommand. -- evidence: [README.md#L288-L288](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L288-L288), [README.md#L290-L292](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L290-L292), [README.md#L302-L304](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L302-L304), [README.md#L296-L298](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L296-L298), [README.md#L308-L310](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L308-L310), [docs/release-notes/v0.0.1.md#L32-L34](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L32-L34)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Setup commands are described as a code-execution vector, and local .gwq.toml files must be trusted before they run, referencing a trust prompt mechanism. -- evidence: [README.md#L408-L408](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L408-L408)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements are Git 2.5+ for worktree support and Go 1.24+ for building from source; release notes also mention a dependency update to github.com/bmatcuk/doublestar/v4 v4.10.0. -- evidence: [docs/release-notes/v0.0.12.md#L37-L37](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.12.md#L37-L37), [docs/release-notes/v0.0.1.md#L46-L47](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L46-L47), [README.md#L507-L508](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L507-L508)
- limitations (1 claim(s)):
  - [observation/documented] PowerShell is not supported for shell integration, and the v0.0.1 release was explicitly labeled experimental with possible breaking changes in future versions. -- evidence: [README.md#L284-L284](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L284-L284), [docs/release-notes/v0.0.1.md#L61-L61](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L61-L61), [docs/release-notes/v0.0.1.md#L7-L7](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L7-L7), [README.md#L162-L162](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L162-L162)
- relevance (1 claim(s)):
More evidence: [full detail](gwq.detail.md)

Metadata and full claim list: [full detail](gwq.detail.md)
Human notes ([notes](gwq.notes.md), never overwritten by build)

[Back to map index](../../index.md)
