# d-kuro/gwq -- full detail

[Back to orientation](gwq.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/d-kuro/gwq/c4247734968bc3f66addd1e088c19b962c27cfc1/554853775b2f91fa.json](../../../wiki/dossiers/d-kuro/gwq/c4247734968bc3f66addd1e088c19b962c27cfc1/554853775b2f91fa.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Per-repository setup_commands are rendered with Go text/template (variables like {{.Branch}} and {{.Path}}) and executed via POSIX sh -c; unknown template keys cause the command to be skipped with an error logged. -- evidence: [README.md#L393-L393](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L393-L393), [README.md#L410-L410](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L410-L410), [README.md#L384-L391](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L384-L391), [README.md#L382-L382](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L382-L382) (`clm_164b95f801e99deb7557780d5865e388fcc345210150a7b9d8e63d6a55df4aea`)

## design-choices (3 claim(s))

- [observation/documented] Worktrees are organized in a URL-based hierarchy (e.g. ~/worktrees/github.com/user/repo/branch) to prevent naming conflicts, with a configurable naming template. -- evidence: [docs/release-notes/v0.0.1.md#L13-L16](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L13-L16), [README.md#L464-L464](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L464-L464), [README.md#L479-L479](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L479-L479), [README.md#L466-L477](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L466-L477), [README.md#L335-L337](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L335-L337) (`clm_a63cae1fd563bbc78b1c26143e013ea32969294204e3c131d85fce1858f93d35`)
- [observation/documented] Global worktree discovery uses filesystem scanning of a configured base directory rather than a separate registry, and behavior is context-aware inside versus outside Git repositories. -- evidence: [docs/release-notes/v0.0.1.md#L13-L16](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L13-L16), [README.md#L278-L280](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L278-L280), [README.md#L276-L276](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L276-L276) (`clm_e918e9ec99f0ad6c53f14ef09370ae171e13d803b1e72db8fafacc3251917fb0`)
- [observation/documented] Configuration uses a global TOML file (~/.config/gwq/config.toml) plus a local .gwq.toml that takes precedence, with repository_settings merged by repository key where local overrides global for the same repository. -- evidence: [docs/release-notes/v0.0.10.md#L21-L24](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L21-L24), [README.md#L416-L417](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L416-L417), [README.md#L323-L323](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L323-L323), [README.md#L414-L414](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L414-L414), [README.md#L318-L321](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L318-L321), [docs/release-notes/v0.0.10.md#L7-L7](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L7-L7), [README.md#L316-L316](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L316-L316), [docs/release-notes/v0.0.10.md#L30-L31](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L30-L31) (`clm_86a0f270b9d76f6c3bf885d239d46a9d15151f4c14cfc0249cc7e4a0fc5a445d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: release notes state that comprehensive release documentation was added at docs/RELEASING.md, including step-by-step instructions, a notes template, and a release checklist. -- evidence: [docs/release-notes/v0.0.10.md#L37-L37](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L37-L37), [docs/release-notes/v0.0.10.md#L39-L43](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.10.md#L39-L43) (`clm_9938163b3cf8401482fd943d22c56f6f7283883d5535a67ed73011bcd7141cea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The status command supports watch mode, filtering, sorting, and JSON/CSV output formats per its documented flags. -- evidence: [README.md#L216-L216](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L216-L216), [README.md#L213-L213](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L213-L213), [README.md#L210-L210](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L210-L210), [README.md#L223-L223](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L223-L223), [README.md#L219-L221](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L219-L221) (`clm_e48a0f7117c7a9abea400e100095f0034be2ec0703c2c19c9637887b4c2db544`)
- [observation/documented] gwq generates shell completions for Bash, Zsh, Fish, and PowerShell via a completion subcommand. -- evidence: [README.md#L288-L288](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L288-L288), [README.md#L290-L292](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L290-L292), [README.md#L302-L304](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L302-L304), [README.md#L296-L298](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L296-L298), [README.md#L308-L310](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L308-L310), [docs/release-notes/v0.0.1.md#L32-L34](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L32-L34) (`clm_0cadeb6a36d409e0cb419b90f4174c914f962ee1f4f80966de22d36a084d87c3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Setup commands are described as a code-execution vector, and local .gwq.toml files must be trusted before they run, referencing a trust prompt mechanism. -- evidence: [README.md#L408-L408](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L408-L408) (`clm_671990e08de1c5fdbf50b07290c9b879cb363bd213c9b6dabd2cf588353c6459`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Git 2.5+ for worktree support and Go 1.24+ for building from source; release notes also mention a dependency update to github.com/bmatcuk/doublestar/v4 v4.10.0. -- evidence: [docs/release-notes/v0.0.12.md#L37-L37](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.12.md#L37-L37), [docs/release-notes/v0.0.1.md#L46-L47](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L46-L47), [README.md#L507-L508](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L507-L508) (`clm_e309c7cd5ff22e5344f5af2cf56f04cf3e327ce1b9470d11a572c3883df8c725`)

## limitations (1 claim(s))

- [observation/documented] PowerShell is not supported for shell integration, and the v0.0.1 release was explicitly labeled experimental with possible breaking changes in future versions. -- evidence: [README.md#L284-L284](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L284-L284), [docs/release-notes/v0.0.1.md#L61-L61](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L61-L61), [docs/release-notes/v0.0.1.md#L7-L7](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L7-L7), [README.md#L162-L162](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L162-L162) (`clm_5dcd0bde4228996289ce35903bec6e0476078a104eec2ad37afc0dab35d1a122`)

## relevance (1 claim(s))

- [observation/documented] gwq is positioned for parallel AI coding agent workflows: multiple agents work in isolated worktrees simultaneously, monitored via gwq status --watch, without merge conflicts. -- evidence: [docs/release-notes/v0.0.1.md#L13-L16](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/docs/release-notes/v0.0.1.md#L13-L16), [README.md#L18-L18](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L18-L18), [README.md#L27-L29](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L27-L29), [README.md#L11-L14](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L11-L14), [README.md#L35-L35](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L35-L35), [README.md#L32-L33](https://github.com/d-kuro/gwq/blob/c4247734968bc3f66addd1e088c19b962c27cfc1/README.md#L32-L33) (`clm_5130a8f5cf0854f85ac00097eb5126d919a0a0b668b210af37002e56f6b51c77`)

