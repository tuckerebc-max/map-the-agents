# herdrdev/herdr -- full detail

[Back to orientation](herdr.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/herdrdev/herdr/aa961df943b874730b23f78baf94af7332f7acfa/9d624c3d74eb8c6b.json](../../../wiki/dossiers/herdrdev/herdr/aa961df943b874730b23f78baf94af7332f7acfa/9d624c3d74eb8c6b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Herdr is described as a single Rust binary with no Electron dependency, running inside the user's existing terminal. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_2df600ab73b950089bd3a58b6414ce963c27ec834ef17a37d1c0fb87152bba84`)
- [observation/documented] The product keeps terminals running in a background server so work continues after the client closes or SSH drops, and restores saved layout after server or machine restart. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_ba62e3b07c1ec94ee50962ce29afc060a248fc218d3e5e906c14fe9f0f9bfb4d`)

## design-choices (2 claim(s))

- [observation/documented] Herdr runs agents like Claude Code, Codex, Cursor, OpenCode, and Grok in their own terminals without wrapping or replacing them. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_f3ce657bedc76bb15260ef489db1ebaadb3ba3d47c9ab3158fe92d81ebe2f2b8`)
- [observation/documented] Each pane is marked working, blocked, or idle, and Herdr signals when an agent stops and needs input. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_92210d92405ff1624b4d399a4ae581d9850e4833f2728906b5e8edc5996c5bfd`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors should use just recipes (just test, just check) rather than invoking cargo directly, and run just check before committing. -- evidence: [AGENTS.md#L141-L141](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L141-L141), [AGENTS.md#L136-L139](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L136-L139), [AGENTS.md#L134-L134](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L134-L134) (`clm_27cc1c66b0c94d350798b0b90d4cbff4a96aac4b94225cb1ad9352383475f5e4`)
- [observation/documented] Repository development practice: Rust production code must avoid unwrap(), use tracing for logging, and gate platform-specific code via cfg attributes in src/platform/. -- evidence: [AGENTS.md#L251-L255](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L251-L255) (`clm_07d91a02c0212240ca632a315bd896d598d6371a9ba62240d76cc263ab99dcac`)
- [observation/documented] Repository development practice: external contributors' unsolicited implementation PRs are closed automatically unless the human is listed in .github/APPROVED_CONTRIBUTORS; agents may only file verified, reproducible bug reports. -- evidence: [AGENTS.md#L315-L315](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L315-L315), [AGENTS.md#L313-L313](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L313-L313), [AGENTS.md#L311-L311](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L311-L311) (`clm_8bed0e196ed063659d069e5d55b2b8ce0e31b499268d5caece88418d34c4fe4b`)
- [observation/documented] Repository development practice: commits use lowercase conventional-commit style with no emojis or AI co-author lines, and reference issues with 'refs #<n>' rather than closing keywords. -- evidence: [AGENTS.md#L247-L247](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L247-L247), [AGENTS.md#L235-L235](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L235-L235) (`clm_584cd59b8e63da898eb5112c9645d734e79c1b296fbd04cd4287325507988c84`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Agents can drive Herdr through a CLI and socket API to spawn panes, prompt each other, and wait until another agent is blocked. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_16b2ac86a400ecfc2abd2ad751c23e0c6067d6307ea85e230d1e6aabf09b0b65`)
- [observation/documented] The TUI supports tmux-style prefix keys plus mouse click, drag, and split interactions. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_1830d8daed69ad935906c2dacc7147ecb9e35d3b5cadcfb9dd848ea54631162e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] After a server or machine restart, Herdr restores layout and can resume supported agent sessions, but the original processes do not survive. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38) (`clm_217402aa2d8e51ffed9849a6e4850a2b576d04d99095f4151368e72d585d7c62`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

