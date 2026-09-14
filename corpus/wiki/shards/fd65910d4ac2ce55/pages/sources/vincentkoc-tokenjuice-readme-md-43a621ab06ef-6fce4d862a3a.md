---
access: public
aliases: []
claim_ids:
- clm_12ea4a9761d815c0765fd9fb08e4dadbc95984e948a10978c95757180111e2e4
- clm_1b39b28e54f0344981ba85b66ddae5196177e6fed2c9fd316f57c39ace214af2
- clm_1baf119d122b6de0611f2750b4801eb0a8641396e85f7ac74c4570636c8325f6
- clm_2aed415c8051e4b113c13b67c42346d05963b8fe58f50e20418c8295f6c44335
- clm_6262ae9de4ca0a4a1de7af14adff2f8b3676b54349a88b1ffff12f6003abc0f4
- clm_6820141872b1c8bab63a6b6b95af564a3f20a45d0b1067f322c30de42590e81f
- clm_6b1c93925aca75d3c71781f7ffffa0a712075c9edddc351d57440f94fc21e496
- clm_798e8d56af8265e89e755d8d3222777cddce51f50f3fbfb205a6d277e166807e
- clm_8563deaaa301352baa4c73d3913786e76f8ec4a7f11e3a00d0f27e1c028ed95e
- clm_9236783652fb6073241ccd2c6160a2b6df79cef51773d2d8df8258f43f40b27f
- clm_a61f3305173e2669b96b8618c2fcb64b7a5f9cb5f05c4cafdfdbf3a027eaa995
- clm_c4076aa8303a4fe2a278b2ee6ba86f0fdb8a1d32183dc38d1d7b2ce591ba1fff
maturity: draft
page_id: pg_be587d107160547ba2866fce4d862a3a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f20f33d559455ba9a3052f838a3bca7c
title: vincentkoc/tokenjuice/README.md @ 43a621ab06ef
updated_at: '2026-09-14T04:30:22Z'
---

# vincentkoc/tokenjuice/README.md @ 43a621ab06ef

<!-- rcw:begin owner=source:src_f20f33d559455ba9a3052f838a3bca7c block=evidence -->
- The CLI ships install/uninstall commands covering many agent hosts (including claude-code, codex, cursor, droid, copilot-cli), plus `doctor hooks` to check installed wiring and `doctor <host>` for a single integration. [@claim:clm_12ea4a9761d815c0765fd9fb08e4dadbc95984e948a10978c95757180111e2e4]
- Documented integrations include Claude Code, CodeBuddy, Codex CLI, Cursor, Droid, GitHub Copilot CLI, and OpenClaw, each with an install command and hook/settings file location; OpenClaw support is bundled on the OpenClaw side and requires version 2026.4.22 or newer. [@claim:clm_1b39b28e54f0344981ba85b66ddae5196177e6fed2c9fd316f57c39ace214af2]
- Host adapters apply a narrow safe-inventory policy: exact file-content reads stay raw, standalone repository inventory commands can be compacted, and unsafe mixed command sequences stay raw. [@claim:clm_1baf119d122b6de0611f2750b4801eb0a8641396e85f7ac74c4570636c8325f6]
- The CLI has three surfaces: `reduce` compacts existing text, `wrap` runs a command and compacts its observed output, and `reduce-json` provides a stable machine protocol for host adapters. [@claim:clm_2aed415c8051e4b113c13b67c42346d05963b8fe58f50e20418c8295f6c44335]
- tokenjuice is distributed via npm (`npm install -g tokenjuice`), pnpm, yarn global, and a Homebrew tap (`brew tap vincentkoc/tap; brew install tokenjuice`). [@claim:clm_6262ae9de4ca0a4a1de7af14adff2f8b3676b54349a88b1ffff12f6003abc0f4]
- The project's stated status is a usable foundation for token reduction with diagnostics and a growing reducer set, now focused on deeper coverage and tuning. [@claim:clm_6820141872b1c8bab63a6b6b95af564a3f20a45d0b1067f322c30de42590e81f]
- Repository development practice: Homebrew publication is owned by the Tokenjuice workflow in the canonical vincentkoc/homebrew-tap repository, and release maintainers dispatch it manually with the published tag until GitHub App automation lands. [@claim:clm_6b1c93925aca75d3c71781f7ffffa0a712075c9edddc351d57440f94fc21e496]
- Statistics use bounded metadata segments, support paging via --limit and a returned --cursor, report partial coverage, and can be disabled with TOKENJUICE_STATS=off or --no-stats; artifact retention is opt-in via --store. [@claim:clm_798e8d56af8265e89e755d8d3222777cddce51f50f3fbfb205a6d277e166807e]
- `reduce-json` reads JSON from stdin or a file and always writes JSON to stdout; the documented payload includes fields such as toolName, command, argv, combinedText, and exitCode. [@claim:clm_8563deaaa301352baa4c73d3913786e76f8ec4a7f11e3a00d0f27e1c028ed95e]
- tokenjuice is described as a deterministic output compactor for terminal-heavy agent workflows: it observes command output after execution and returns a smaller payload built from rule-driven reducers instead of the full terminal text. [@claim:clm_9236783652fb6073241ccd2c6160a2b6df79cef51773d2d8df8258f43f40b27f]
- The design keeps command semantics untouched, exposes raw output only via explicit --raw/--full or opt-in artifact storage, keeps rules as inspectable JSON, and keeps host integrations as thin wrappers around one shared core reducer. [@claim:clm_a61f3305173e2669b96b8618c2fcb64b7a5f9cb5f05c4cafdfdbf3a027eaa995]
- The reduction engine is rule-driven: built-in JSON rules live in src/rules, user overrides in ~/.config/tokenjuice/rules, and project overrides in .tokenjuice/rules, with later layers overriding earlier ones by rule id. [@claim:clm_c4076aa8303a4fe2a278b2ee6ba86f0fdb8a1d32183dc38d1d7b2ce591ba1fff]
<!-- rcw:end owner=source:src_f20f33d559455ba9a3052f838a3bca7c block=evidence -->

## Researcher notes

