---
access: public
aliases: []
claim_ids:
- clm_1100df4364467048d7f98b22772195d91f9602e361279022e415736327c4a672
- clm_18080795255e6770c720aabcf3d3ed8be07a3890f49c0e1e5c28297b2b0b50a1
- clm_3dc2e64476dd44cfadd83ad5ab8a6d400885a341eca193a2a54d1f3f956106b5
- clm_4260ee46310a6df98e5dadc0e6b5b5fba131558032f0c17f1022764f973be578
- clm_4cefe28591499d8d81f2cbd348706cc0f6563fc647a7b4b8432312bc56d9f4e3
- clm_4d23d2e8808793c1dbf2e072b06b9c4df2a538d18ec924741de7a56510cddf39
- clm_542452ea9f1ae3657a2c63cc99fe7e1372687d69468a585b4162967e09f06b9e
- clm_6a1cf5d52c7f0884e1acef37461241260eba96f0a02ee926212f792df42378b7
- clm_76c908a0c92363c642db98f9a38a041b43427d6ceb07ec4862f7cad970773cda
- clm_b03b00dfff8fa5fc06fc294df42372c0141999c706790b6bae159417fc5682e8
- clm_c54c3f89766f7d361ce0e70c195aba577097c60f9fe02b71c8082df541f7eab0
- clm_d56cbdd5293aa34890f1fef29ddfdd26e20595fd311a156278182a1788faaf04
- clm_f07c37705cb4382971490b382c1c08a3a90b3ea3625f90f520d2bc9a28e7edd1
maturity: draft
page_id: pg_928550e7c95b5c4987fcc1daa08edb66
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e5c44c6829815adab4c0aeeb9b48aec7
title: oso95/Codirigent/README.md @ 03d9f6b7302e
updated_at: '2026-09-14T02:27:17Z'
---

# oso95/Codirigent/README.md @ 03d9f6b7302e

<!-- rcw:begin owner=source:src_e5c44c6829815adab4c0aeeb9b48aec7 block=evidence -->
- The Chinese READMEs say the app is not yet code-signed while the English README says the MSI is code-signed, suggesting the signing status changed between documentation revisions or translations are out of sync. [@claim:clm_1100df4364467048d7f98b22772195d91f9602e361279022e415736327c4a672]
- Building from source requires Rust 1.75+ on Windows or macOS; the project is written in Rust and installs via cargo into ~/.cargo/bin/. [@claim:clm_18080795255e6770c720aabcf3d3ed8be07a3890f49c0e1e5c28297b2b0b50a1]
- The project ships two binaries: the main `codirigent` app and a `codirigent-hook` binary that gets registered into supported CLIs' configuration files for real-time agent status tracking. [@claim:clm_3dc2e64476dd44cfadd83ad5ab8a6d400885a341eca193a2a54d1f3f956106b5]
- Distribution is via a code-signed .msi installer for Windows (with a SmartScreen reputation warning on first install) and a .dmg for macOS, both from GitHub releases. [@claim:clm_4260ee46310a6df98e5dadc0e6b5b5fba131558032f0c17f1022764f973be578]
- Hooks are installed automatically on first launch for supported CLIs, and relaunching after moving or reinstalling the app re-registers the hook binary path. [@claim:clm_4cefe28591499d8d81f2cbd348706cc0f6563fc647a7b4b8432312bc56d9f4e3]
- The tool targets developers running Claude Code, Codex, or Gemini across multiple projects simultaneously, aiming to reduce terminal juggling and losing track of which agent is doing what. [@claim:clm_4d23d2e8808793c1dbf2e072b06b9c4df2a538d18ec924741de7a56510cddf39]
- Codirigent is described as a terminal workspace for running multiple AI coding CLIs in parallel, styled after tmux, with sessions restored to their prior directory, layout, and agent on launch. [@claim:clm_542452ea9f1ae3657a2c63cc99fe7e1372687d69468a585b4162967e09f06b9e]
- Repository development practice: contributors run tests with `cargo test --all --all-targets`, format with `cargo fmt --all`, and lint with `cargo clippy --all -- -D warnings`; major changes require opening an issue first, and PRs are welcome. [@claim:clm_6a1cf5d52c7f0884e1acef37461241260eba96f0a02ee926212f792df42378b7]
- The README states Linux support is not yet complete, and the project is an early alpha (version 0.1.0) where rough edges are expected. [@claim:clm_76c908a0c92363c642db98f9a38a041b43427d6ceb07ec4862f7cad970773cda]
- Each session displays a real-time status indicator with four states: Idle (gray), Working (amber, agent generating a response), Attention (rose, awaiting user input or permission), and Ready (green, finished response in an unfocused session). [@claim:clm_b03b00dfff8fa5fc06fc294df42372c0141999c706790b6bae159417fc5682e8]
- Documented features include custom saveable grid layouts with drag-and-drop session headers, a file tree synced to the focused session, and Git worktree support for running agents on isolated branches concurrently. [@claim:clm_c54c3f89766f7d361ce0e70c195aba577097c60f9fe02b71c8082df541f7eab0]
- The app automatically detects and resumes previous Claude Code and Codex sessions, and its clipboard supports pasting text, files, or images with file paths converted to shell-friendly formats for the target CLI. [@claim:clm_d56cbdd5293aa34890f1fef29ddfdd26e20595fd311a156278182a1788faaf04]
- Status tracking uses lightweight hooks registered into each CLI's config (Claude Code at ~/.claude/settings.json, Codex at ~/.codex/config.toml, Gemini at ~/.gemini/settings.json); when hooks are unavailable it falls back to a less precise reader/detector path. [@claim:clm_f07c37705cb4382971490b382c1c08a3a90b3ea3625f90f520d2bc9a28e7edd1]
<!-- rcw:end owner=source:src_e5c44c6829815adab4c0aeeb9b48aec7 block=evidence -->

## Researcher notes

