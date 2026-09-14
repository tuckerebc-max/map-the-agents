# oso95/codirigent -- full detail

[Back to orientation](codirigent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oso95/codirigent/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/c4a8c82490e66983.json](../../../wiki/dossiers/oso95/codirigent/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/c4a8c82490e66983.json)

## specifications (1 claim(s))

- [observation/documented] Codirigent is described as a terminal workspace for running multiple AI coding CLIs in parallel, styled after tmux, with sessions restored to their prior directory, layout, and agent on launch. -- evidence: [README.md#L35-L35](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L35-L35), [README.md#L7-L9](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L7-L9) (`clm_542452ea9f1ae3657a2c63cc99fe7e1372687d69468a585b4162967e09f06b9e`)

## components (3 claim(s))

- [observation/documented] The project ships two binaries: the main `codirigent` app and a `codirigent-hook` binary that gets registered into supported CLIs' configuration files for real-time agent status tracking. -- evidence: [README.md#L107-L107](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L107-L107), [README.md#L86-L86](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L86-L86) (`clm_3dc2e64476dd44cfadd83ad5ab8a6d400885a341eca193a2a54d1f3f956106b5`)
- [observation/documented] Documented features include custom saveable grid layouts with drag-and-drop session headers, a file tree synced to the focused session, and Git worktree support for running agents on isolated branches concurrently. -- evidence: [README.md#L54-L54](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L54-L54), [README.md#L50-L50](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L50-L50), [README.md#L58-L58](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L58-L58) (`clm_c54c3f89766f7d361ce0e70c195aba577097c60f9fe02b71c8082df541f7eab0`)
- [observation/documented] The app automatically detects and resumes previous Claude Code and Codex sessions, and its clipboard supports pasting text, files, or images with file paths converted to shell-friendly formats for the target CLI. -- evidence: [README.md#L62-L62](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L62-L62), [README.md#L66-L66](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L66-L66) (`clm_d56cbdd5293aa34890f1fef29ddfdd26e20595fd311a156278182a1788faaf04`)

## design-choices (2 claim(s))

- [observation/documented] Status tracking uses lightweight hooks registered into each CLI's config (Claude Code at ~/.claude/settings.json, Codex at ~/.codex/config.toml, Gemini at ~/.gemini/settings.json); when hooks are unavailable it falls back to a less precise reader/detector path. -- evidence: [README.md#L84-L84](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L84-L84), [README.md#L88-L92](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L88-L92) (`clm_f07c37705cb4382971490b382c1c08a3a90b3ea3625f90f520d2bc9a28e7edd1`)
- [observation/documented] Hooks are installed automatically on first launch for supported CLIs, and relaunching after moving or reinstalling the app re-registers the hook binary path. -- evidence: [README.md#L94-L94](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L94-L94), [README.md#L86-L86](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L86-L86) (`clm_4cefe28591499d8d81f2cbd348706cc0f6563fc647a7b4b8432312bc56d9f4e3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run tests with `cargo test --all --all-targets`, format with `cargo fmt --all`, and lint with `cargo clippy --all -- -D warnings`; major changes require opening an issue first, and PRs are welcome. -- evidence: [README.md#L127-L127](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L127-L127), [README.md#L119-L123](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L119-L123) (`clm_6a1cf5d52c7f0884e1acef37461241260eba96f0a02ee926212f792df42378b7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Each session displays a real-time status indicator with four states: Idle (gray), Working (amber, agent generating a response), Attention (rose, awaiting user input or permission), and Ready (green, finished response in an unfocused session). -- evidence: [README.md#L41-L46](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L41-L46), [README.md#L39-L39](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L39-L39) (`clm_b03b00dfff8fa5fc06fc294df42372c0141999c706790b6bae159417fc5682e8`)
- [observation/documented] Distribution is via a code-signed .msi installer for Windows (with a SmartScreen reputation warning on first install) and a .dmg for macOS, both from GitHub releases. -- evidence: [README.md#L74-L74](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L74-L74), [README.md#L76-L76](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L76-L76), [README.md#L80-L80](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L80-L80) (`clm_4260ee46310a6df98e5dadc0e6b5b5fba131558032f0c17f1022764f973be578`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Rust 1.75+ on Windows or macOS; the project is written in Rust and installs via cargo into ~/.cargo/bin/. -- evidence: [README.md#L98-L98](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L98-L98), [README.md#L107-L107](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L107-L107), [README.md#L100-L105](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L100-L105) (`clm_18080795255e6770c720aabcf3d3ed8be07a3890f49c0e1e5c28297b2b0b50a1`)

## limitations (2 claim(s))

- [observation/documented] The README states Linux support is not yet complete, and the project is an early alpha (version 0.1.0) where rough edges are expected. -- evidence: [README.md#L11-L16](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L11-L16), [README.md#L115-L115](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L115-L115), [README.md#L70-L70](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L70-L70) (`clm_76c908a0c92363c642db98f9a38a041b43427d6ceb07ec4862f7cad970773cda`)
- [inference/documented] The Chinese READMEs say the app is not yet code-signed while the English README says the MSI is code-signed, suggesting the signing status changed between documentation revisions or translations are out of sync. -- evidence: [README.zh-TW.md#L75-L75](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.zh-TW.md#L75-L75), [README.zh-CN.md#L75-L75](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.zh-CN.md#L75-L75), [README.md#L76-L76](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L76-L76) (`clm_1100df4364467048d7f98b22772195d91f9602e361279022e415736327c4a672`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers running Claude Code, Codex, or Gemini across multiple projects simultaneously, aiming to reduce terminal juggling and losing track of which agent is doing what. -- evidence: [README.md#L35-L35](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L35-L35), [README.md#L33-L33](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L33-L33) (`clm_4d23d2e8808793c1dbf2e072b06b9c4df2a538d18ec924741de7a56510cddf39`)

