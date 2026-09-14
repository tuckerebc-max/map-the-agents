---
access: public
aliases: []
claim_ids:
- clm_12835b3581a8ee06b361d386a3427530e6fe681c6be566b795a534fede23bed5
- clm_8f729e7c537ee21ae268179046ee5dafdbcd30d81eea055a0f05f9e8f6a795e2
- clm_e2c4a7e02780c99a606d0a060b9d957ee88177403dc648913f9761d6ebb17d7a
- clm_fb4a742c61058378a2a37f96f8b255894389ee4a827d408ef50887732cf8911a
- clm_fc1ca4942c79f5850132d0872162d751598a6781dfdd6f5ca83d9fa84d75c4bb
maturity: draft
page_id: pg_04da15216afa57529b88bdf3c4988757
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f45e46cdb1725033a5de810b64cbcad3
title: anomalyco/opencode/README.md @ df23b7f9488a
updated_at: '2026-09-14T04:57:56Z'
---

# anomalyco/opencode/README.md @ df23b7f9488a

<!-- rcw:begin owner=source:src_f45e46cdb1725033a5de810b64cbcad3 block=evidence -->
- OpenCode is installable via a curl script and many package managers including npm/bun/pnpm/yarn, Scoop, Chocolatey, Homebrew, pacman, AUR, mise, and nix. [@claim:clm_12835b3581a8ee06b361d386a3427530e6fe681c6be566b795a534fede23bed5]
- The README documents two built-in agents switchable with the Tab key: build (default, full access) and plan (read-only, denies file edits by default and asks before running bash commands), plus a general subagent invoked via @general. [@claim:clm_8f729e7c537ee21ae268179046ee5dafdbcd30d81eea055a0f05f9e8f6a795e2]
- A desktop application is offered in BETA for macOS (arm64/x64 dmg), Windows exe, and Linux deb/rpm/AppImage, also installable via Homebrew cask or Scoop extras. [@claim:clm_e2c4a7e02780c99a606d0a060b9d957ee88177403dc648913f9761d6ebb17d7a]
- The install script resolves its target directory by priority: OPENCODE_INSTALL_DIR, XDG_BIN_DIR, $HOME/bin, then $HOME/.opencode/bin as fallback. [@claim:clm_fb4a742c61058378a2a37f96f8b255894389ee4a827d408ef50887732cf8911a]
- Repository development practice: contributors are directed to read CONTRIBUTING.md before submitting pull requests, and derivative projects using 'opencode' in their name must state they are unaffiliated with the OpenCode team. [@claim:clm_fc1ca4942c79f5850132d0872162d751598a6781dfdd6f5ca83d9fa84d75c4bb]
<!-- rcw:end owner=source:src_f45e46cdb1725033a5de810b64cbcad3 block=evidence -->

## Researcher notes

