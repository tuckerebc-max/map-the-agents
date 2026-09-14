---
access: public
aliases: []
claim_ids:
- clm_03cafaff9eafdb77746476be72e8da2fd12326fa859cb76d989ea8796fadfb35
- clm_178f9737494d9dfd54ab8aa4eb45f86cb3086aa83c2f662bce9f288fe0b5c2e8
- clm_36f4b67f7b1bb671f3ee0b5fa9789527b09d6326fe36cdc0c57eee780dfb5b1f
- clm_42e0ebeab90ab0300f3f1297200a4c6b7ebc7e08a4c63bee95aad2b7d2d99753
- clm_443ebf52c720f5732eb2686f3ad2ee24b5f209ef5d96bc900b915b011d380f5f
- clm_68f6ffdcfc2355336ee20de7ad5d8003bc250f569c6c1eeb0a61098bd873d6af
- clm_738b6fd30507c82dc120589787d57fd28ee322813638538c4e05a93ad6912b6c
- clm_9bd221ade5fc1e6dcaa6a8a7bff631a3f6c49c6f9bad88ba3758e02da80269c5
- clm_b5b37cddb3098bb2503232b705c1835050087e2e50ca665833077e75f21441de
- clm_b9b31f1b0cb20cb1c9d5239ae0c2e943c826bd7d86a74dc90631805a66fd6ed1
- clm_e3f38bbb39a77de616410cdb009a73e4a163312a345d1804238f18833331f04f
- clm_f1ec04fc9fe2ea00a4273da0d97d9f46cc13cf8021d0b5f9838511689704f7e6
- clm_f9875fd02bc51cbd579b19e3c50188e6f26e28cd689836950803b349af6be2e8
maturity: draft
page_id: pg_37671bb45dbe597da631f72618c66891
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_924a791b29e157b18eb42755e3d51bdb
title: alchaincyf/fanbox/README.md @ 0394dae502b7
updated_at: '2026-09-14T01:32:13Z'
---

# alchaincyf/fanbox/README.md @ 0394dae502b7

<!-- rcw:begin owner=source:src_924a791b29e157b18eb42755e3d51bdb block=evidence -->
- FanBox offers a global fuzzy search (⌘K) with a content: prefix switching to full-text grep, ⌘↵ to open projects in an editor, and keyboard navigation via arrows, Enter, /, and Esc. [@claim:clm_03cafaff9eafdb77746476be72e8da2fd12326fa859cb76d989ea8796fadfb35]
- The app embeds a real terminal built on node-pty plus xterm.js with WebGL rendering, supporting Claude Code, vim, htop, and correct CJK wide-character display. [@claim:clm_178f9737494d9dfd54ab8aa4eb45f86cb3086aa83c2f662bce9f288fe0b5c2e8]
- Write endpoints require a per-launch random token never persisted to disk, the backend binds loopback only with Host-header validation, and HTML previews render in a sandboxed opaque-origin iframe. [@claim:clm_36f4b67f7b1bb671f3ee0b5fa9789527b09d6326fe36cdc0c57eee780dfb5b1f]
- Three full skins (Volt default, Archive, Index) change palette, typography, icons, code highlighting, and terminal ANSI themes together, not just a theme color. [@claim:clm_42e0ebeab90ab0300f3f1297200a4c6b7ebc7e08a4c63bee95aad2b7d2d99753]
- Project memory shows past agent sessions per folder (first message as title, files changed, skills triggered) with a resume button running 'claude --resume' or 'codex resume' in the embedded terminal. [@claim:clm_443ebf52c720f5732eb2686f3ad2ee24b5f209ef5d96bc900b915b011d380f5f]
- The product is positioned local-first with no cloud, remote access, or accounts, zero config, and zero runtime dependencies; the web version runs with just 'node server.js' on localhost:4567. [@claim:clm_68f6ffdcfc2355336ee20de7ad5d8003bc250f569c6c1eeb0a61098bd873d6af]
- Architecture: a zero-dependency Node.js server.js (file APIs, static serving, thumbnails), an Electron 33 main process handling window/pty/clipboard/fs.watch, a preload exposing fanboxPty/fanboxFs/fanboxClipboard, and a frontend SPA. [@claim:clm_738b6fd30507c82dc120589787d57fd28ee322813638538c4e05a93ad6912b6c]
- Repository development practice: development uses 'npm install', 'npm run app' for the full desktop app, and 'npm run dist' to build/sign the dmg, with an ELECTRON_MIRROR workaround for blocked Electron downloads. [@claim:clm_9bd221ade5fc1e6dcaa6a8a7bff631a3f6c49c6f9bad88ba3758e02da80269c5]
- Editing uses Monaco for code/JSON and Git diffs and Milkdown Crepe for Notion-style Markdown WYSIWYG with auto-save about 0.8s after typing stops and a Rich/Read/Source/Typeset switch. [@claim:clm_b5b37cddb3098bb2503232b705c1835050087e2e50ca665833077e75f21441de]
- When launching Claude Code or Codex, FanBox attaches their official hooks via its own extra settings file so agent states (working, needs approval, needs input, done) are exact events; hookless agents fall back to heuristics. [@claim:clm_b9b31f1b0cb20cb1c9d5239ae0c2e943c826bd7d86a74dc90631805a66fd6ed1]
- Core capabilities come from MIT/BSD/Apache open-source projects including Electron, node-pty, xterm.js, Monaco, Milkdown, marked, highlight.js, esbuild, electron-builder, and Playwright, with all frontend deps vendored locally under public/vendor/. [@claim:clm_e3f38bbb39a77de616410cdb009a73e4a163312a345d1804238f18833331f04f]
- Repository development practice: each development phase is reviewed by five independent subagent roles scoring product, live screenshots, and code, with a ≥90 score and zero red lines required to ship. [@claim:clm_f1ec04fc9fe2ea00a4273da0d97d9f46cc13cf8021d0b5f9838511689704f7e6]
- There is no official Windows build; the author states community Windows ports exist but are unofficial and not vetted by him. [@claim:clm_f9875fd02bc51cbd579b19e3c50188e6f26e28cd689836950803b349af6be2e8]
<!-- rcw:end owner=source:src_924a791b29e157b18eb42755e3d51bdb block=evidence -->

## Researcher notes

