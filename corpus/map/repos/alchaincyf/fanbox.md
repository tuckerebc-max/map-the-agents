# alchaincyf/fanbox

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0394dae502b7 @ 4acfa729fa3f62f3

## Summary (orientation draft, not independently verified)

Evidence is README and design docs for FanBox, an Electron-based local 'cockpit' for coding agents combining file browsing, previews, an embedded terminal, and agent-change tracking. Claims below are documentation-based; no source code slices were provided.

## Source coverage

Source coverage (partial): 3 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Architecture: a zero-dependency Node.js server.js (file APIs, static serving, thumbnails), an Electron 33 main process handling window/pty/clipboard/fs.watch, a preload exposing fanboxPty/fanboxFs/fanboxClipboard, and a frontend SPA. -- evidence: [README.md#L276-L298](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L276-L298), [README.md#L265-L271](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L265-L271)
  - [observation/documented] Editing uses Monaco for code/JSON and Git diffs and Milkdown Crepe for Notion-style Markdown WYSIWYG with auto-save about 0.8s after typing stops and a Rich/Read/Source/Typeset switch. -- evidence: [README.md#L245-L256](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L245-L256), [README.md#L93-L100](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L93-L100), [README.md#L138-L149](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L138-L149)
- design-choices (2 claim(s)):
  - [observation/documented] The product is positioned local-first with no cloud, remote access, or accounts, zero config, and zero runtime dependencies; the web version runs with just 'node server.js' on localhost:4567. -- evidence: [README.md#L189-L189](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L189-L189), [docs/02-PRD.md#L19-L22](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/docs/02-PRD.md#L19-L22), [README.md#L60-L60](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L60-L60), [README.md#L58-L58](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L58-L58), [README.md#L183-L185](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L183-L185)
  - [observation/documented] Three full skins (Volt default, Archive, Index) change palette, typography, icons, code highlighting, and terminal ANSI themes together, not just a theme color. -- evidence: [README.md#L65-L65](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L65-L65), [README.md#L69-L73](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L69-L73), [README.md#L67-L67](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L67-L67)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: development uses 'npm install', 'npm run app' for the full desktop app, and 'npm run dist' to build/sign the dmg, with an ELECTRON_MIRROR workaround for blocked Electron downloads. -- evidence: [README.md#L193-L197](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L193-L197), [README.md#L199-L199](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L199-L199)
  - [observation/documented] Repository development practice: each development phase is reviewed by five independent subagent roles scoring product, live screenshots, and code, with a ≥90 score and zero red lines required to ship. -- evidence: [README.md#L236-L236](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L236-L236), [README.md#L234-L234](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L234-L234)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] FanBox offers a global fuzzy search (⌘K) with a content: prefix switching to full-text grep, ⌘↵ to open projects in an editor, and keyboard navigation via arrows, Enter, /, and Esc. -- evidence: [README.md#L203-L209](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L203-L209), [README.md#L80-L89](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L80-L89), [docs/02-PRD.md#L36-L40](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/docs/02-PRD.md#L36-L40)
  - [observation/documented] The app embeds a real terminal built on node-pty plus xterm.js with WebGL rendering, supporting Claude Code, vim, htop, and correct CJK wide-character display. -- evidence: [README.md#L121-L134](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L121-L134), [README.md#L245-L256](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L245-L256)
- memory-state (1 claim(s)):
  - [observation/documented] Project memory shows past agent sessions per folder (first message as title, files changed, skills triggered) with a resume button running 'claude --resume' or 'codex resume' in the embedded terminal. -- evidence: [README.md#L104-L117](https://github.com/alchaincyf/fanbox/blob/0394dae502b7e11ba261fccda189d17ccd184fec/README.md#L104-L117)
- orchestration (1 claim(s)):
More evidence: [full detail](fanbox.detail.md)

Metadata and full claim list: [full detail](fanbox.detail.md)
Human notes ([notes](fanbox.notes.md), never overwritten by build)

[Back to map index](../../index.md)
