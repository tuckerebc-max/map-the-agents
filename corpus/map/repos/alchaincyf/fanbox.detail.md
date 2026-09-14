# alchaincyf/fanbox -- full detail

[Back to orientation](fanbox.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/alchaincyf/fanbox/0394dae502b7e11ba261fccda189d17ccd184fec/4acfa729fa3f62f3.json](../../../wiki/dossiers/alchaincyf/fanbox/0394dae502b7e11ba261fccda189d17ccd184fec/4acfa729fa3f62f3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Architecture: a zero-dependency Node.js server.js (file APIs, static serving, thumbnails), an Electron 33 main process handling window/pty/clipboard/fs.watch, a preload exposing fanboxPty/fanboxFs/fanboxClipboard, and a frontend SPA. -- evidence: [README.md#L276-L298](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L276-L298), [README.md#L265-L271](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L265-L271) (`clm_738b6fd30507c82dc120589787d57fd28ee322813638538c4e05a93ad6912b6c`)
- [observation/documented] Editing uses Monaco for code/JSON and Git diffs and Milkdown Crepe for Notion-style Markdown WYSIWYG with auto-save about 0.8s after typing stops and a Rich/Read/Source/Typeset switch. -- evidence: [README.md#L245-L256](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L245-L256), [README.md#L93-L100](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L93-L100), [README.md#L138-L149](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L138-L149) (`clm_b5b37cddb3098bb2503232b705c1835050087e2e50ca665833077e75f21441de`)

## design-choices (2 claim(s))

- [observation/documented] The product is positioned local-first with no cloud, remote access, or accounts, zero config, and zero runtime dependencies; the web version runs with just 'node server.js' on localhost:4567. -- evidence: [README.md#L189-L189](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L189-L189), [docs/02-PRD.md#L19-L22](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/docs/02-PRD.md#L19-L22), [README.md#L60-L60](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L60-L60), [README.md#L58-L58](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L58-L58), [README.md#L183-L185](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L183-L185) (`clm_68f6ffdcfc2355336ee20de7ad5d8003bc250f569c6c1eeb0a61098bd873d6af`)
- [observation/documented] Three full skins (Volt default, Archive, Index) change palette, typography, icons, code highlighting, and terminal ANSI themes together, not just a theme color. -- evidence: [README.md#L65-L65](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L65-L65), [README.md#L69-L73](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L69-L73), [README.md#L67-L67](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L67-L67) (`clm_42e0ebeab90ab0300f3f1297200a4c6b7ebc7e08a4c63bee95aad2b7d2d99753`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: development uses 'npm install', 'npm run app' for the full desktop app, and 'npm run dist' to build/sign the dmg, with an ELECTRON_MIRROR workaround for blocked Electron downloads. -- evidence: [README.md#L193-L197](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L193-L197), [README.md#L199-L199](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L199-L199) (`clm_9bd221ade5fc1e6dcaa6a8a7bff631a3f6c49c6f9bad88ba3758e02da80269c5`)
- [observation/documented] Repository development practice: each development phase is reviewed by five independent subagent roles scoring product, live screenshots, and code, with a ≥90 score and zero red lines required to ship. -- evidence: [README.md#L236-L236](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L236-L236), [README.md#L234-L234](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L234-L234) (`clm_f1ec04fc9fe2ea00a4273da0d97d9f46cc13cf8021d0b5f9838511689704f7e6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] FanBox offers a global fuzzy search (⌘K) with a content: prefix switching to full-text grep, ⌘↵ to open projects in an editor, and keyboard navigation via arrows, Enter, /, and Esc. -- evidence: [README.md#L203-L209](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L203-L209), [README.md#L80-L89](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L80-L89), [docs/02-PRD.md#L36-L40](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/docs/02-PRD.md#L36-L40) (`clm_03cafaff9eafdb77746476be72e8da2fd12326fa859cb76d989ea8796fadfb35`)
- [observation/documented] The app embeds a real terminal built on node-pty plus xterm.js with WebGL rendering, supporting Claude Code, vim, htop, and correct CJK wide-character display. -- evidence: [README.md#L121-L134](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L121-L134), [README.md#L245-L256](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L245-L256) (`clm_178f9737494d9dfd54ab8aa4eb45f86cb3086aa83c2f662bce9f288fe0b5c2e8`)

## memory-state (1 claim(s))

- [observation/documented] Project memory shows past agent sessions per folder (first message as title, files changed, skills triggered) with a resume button running 'claude --resume' or 'codex resume' in the embedded terminal. -- evidence: [README.md#L104-L117](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L104-L117) (`clm_443ebf52c720f5732eb2686f3ad2ee24b5f209ef5d96bc900b915b011d380f5f`)

## orchestration (1 claim(s))

- [observation/documented] When launching Claude Code or Codex, FanBox attaches their official hooks via its own extra settings file so agent states (working, needs approval, needs input, done) are exact events; hookless agents fall back to heuristics. -- evidence: [README.md#L121-L134](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L121-L134) (`clm_b9b31f1b0cb20cb1c9d5239ae0c2e943c826bd7d86a74dc90631805a66fd6ed1`)

## tools-permissions (1 claim(s))

- [observation/documented] Write endpoints require a per-launch random token never persisted to disk, the backend binds loopback only with Host-header validation, and HTML previews render in a sandboxed opaque-origin iframe. -- evidence: [README.md#L214-L225](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L214-L225) (`clm_36f4b67f7b1bb671f3ee0b5fa9789527b09d6326fe36cdc0c57eee780dfb5b1f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Core capabilities come from MIT/BSD/Apache open-source projects including Electron, node-pty, xterm.js, Monaco, Milkdown, marked, highlight.js, esbuild, electron-builder, and Playwright, with all frontend deps vendored locally under public/vendor/. -- evidence: [README.md#L258-L258](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L258-L258), [README.md#L245-L256](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L245-L256), [README.md#L260-L260](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L260-L260) (`clm_e3f38bbb39a77de616410cdb009a73e4a163312a345d1804238f18833331f04f`)

## limitations (1 claim(s))

- [observation/documented] There is no official Windows build; the author states community Windows ports exist but are unofficial and not vetted by him. -- evidence: [README.md#L174-L174](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L174-L174), [README.md#L172-L172](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L172-L172), [README.md#L176-L179](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L176-L179), [README.md#L168-L168](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L168-L168) (`clm_f9875fd02bc51cbd579b19e3c50188e6f26e28cd689836950803b349af6be2e8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

