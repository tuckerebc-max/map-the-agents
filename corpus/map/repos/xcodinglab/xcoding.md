# xcodinglab/xcoding

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 349a05eeb1e8 @ afb939c58d953fa6

## Summary (orientation draft, not independently verified)

Evidence consists of README files (English and Chinese) and a theme-packs doc for XCoding, an IDE for 'Vibe Coding' with multi-project/multi-task workspaces, AI-assisted editing, and a VS Code-style theme pack system. Development commands and licensing are also documented.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] XCoding is described as a new IDE for Vibe Coding, built to stay light, clean, and fast with a low footprint. -- evidence: [README.md#L5-L5](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L5-L5), [README.md#L3-L3](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] AI assistance is integrated: users can ask AI at any time and apply or roll back its changes in one step. -- evidence: [README.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L13-L15), [docs/README.zh-CN.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L13-L15)
  - [observation/documented] XCoding ships a non-deletable default theme pack 'builtin-classic' (auto-recreated if missing) and writes an editable 'builtin-dark' (Aurora Dark) pack on first initialization. -- evidence: [docs/theme-packs.md#L95-L96](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L95-L96), [docs/theme-packs.md#L98-L99](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L98-L99)
- design-choices (2 claim(s)):
  - [observation/documented] The IDE takes an opinionated-core approach: there is no plugin marketplace; built-in capabilities cover the main path. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [docs/README.zh-CN.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L19-L22)
  - [observation/documented] Theme color keys map to --vscode-* CSS variables; a non-standard 'css' field can load extra CSS, and 'cssVars' supplies additional non-VSCode variables. -- evidence: [docs/theme-packs.md#L59-L59](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L59-L59), [docs/theme-packs.md#L50-L50](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L50-L50), [docs/theme-packs.md#L55-L55](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L55-L55), [docs/theme-packs.md#L77-L77](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L77-L77)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local development uses pnpm — 'pnpm install' to install, 'pnpm run dev' to run, plus build, lint, and typecheck commands. -- evidence: [README.md#L30-L30](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L30-L30), [README.md#L40-L42](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L40-L42), [README.md#L32-L32](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L32-L32), [README.md#L36-L36](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L36-L36)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product supports managing several projects in one window, with project switching via Cmd/Ctrl+1..8 shortcuts. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [docs/README.zh-CN.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L19-L22)
  - [observation/documented] The workspace combines editor, terminal, app preview, and AI panels in one place, letting users code while running commands and previewing. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [README.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L13-L15)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Theme CSS is sandboxed: only relative paths inside the theme folder are allowed; remote/unsafe URLs are ignored and @import is stripped to block external resource loading. -- evidence: [docs/theme-packs.md#L70-L73](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L70-L73)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project is MIT licensed, with third-party notices located in the third_party/ directory. -- evidence: [README.md#L46-L46](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L46-L46), [README.md#L48-L48](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L48-L48)
- limitations (1 claim(s)):
  - [inference/documented] Deleting a theme folder causes the app to fall back to builtin-classic without a blank screen, suggesting built-in fallback handling for missing themes. -- evidence: [docs/theme-packs.md#L120-L126](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L120-L126)
More evidence: [full detail](xcoding.detail.md)

Metadata and full claim list: [full detail](xcoding.detail.md)
Human notes ([notes](xcoding.notes.md), never overwritten by build)

[Back to map index](../../index.md)
