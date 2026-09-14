# xcodinglab/xcoding -- full detail

[Back to orientation](xcoding.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xcodinglab/xcoding/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/afb939c58d953fa6.json](../../../wiki/dossiers/xcodinglab/xcoding/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/afb939c58d953fa6.json)

## specifications (1 claim(s))

- [observation/documented] XCoding is described as a new IDE for Vibe Coding, built to stay light, clean, and fast with a low footprint. -- evidence: [README.md#L5-L5](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L5-L5), [README.md#L3-L3](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L3-L3) (`clm_a026bed58b1e21442105b55ae97d558c5d43be2d26a7a92c53197b7402c821ab`)

## components (2 claim(s))

- [observation/documented] AI assistance is integrated: users can ask AI at any time and apply or roll back its changes in one step. -- evidence: [README.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L13-L15), [docs/README.zh-CN.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L13-L15) (`clm_0d3dccdb9abb51406f34f8944827388e82587dec11f32ffddba2f59cb064c3bc`)
- [observation/documented] XCoding ships a non-deletable default theme pack 'builtin-classic' (auto-recreated if missing) and writes an editable 'builtin-dark' (Aurora Dark) pack on first initialization. -- evidence: [docs/theme-packs.md#L95-L96](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L95-L96), [docs/theme-packs.md#L98-L99](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L98-L99) (`clm_f3a927b48065f242a51d9df4aab26026dbc0865d513aef6fa60dca2b496f250c`)

## design-choices (2 claim(s))

- [observation/documented] The IDE takes an opinionated-core approach: there is no plugin marketplace; built-in capabilities cover the main path. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [docs/README.zh-CN.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L19-L22) (`clm_2611fa23e121c82e0ca700fdebf39aa6515cda503abafb647625f10d8f691a02`)
- [observation/documented] Theme color keys map to --vscode-* CSS variables; a non-standard 'css' field can load extra CSS, and 'cssVars' supplies additional non-VSCode variables. -- evidence: [docs/theme-packs.md#L59-L59](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L59-L59), [docs/theme-packs.md#L50-L50](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L50-L50), [docs/theme-packs.md#L55-L55](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L55-L55), [docs/theme-packs.md#L77-L77](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L77-L77) (`clm_f30bb1b43f25a89c9ad640a215ea61b91bbc1d6f3bb3ae0a26fc687b207e219d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local development uses pnpm — 'pnpm install' to install, 'pnpm run dev' to run, plus build, lint, and typecheck commands. -- evidence: [README.md#L30-L30](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L30-L30), [README.md#L40-L42](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L40-L42), [README.md#L32-L32](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L32-L32), [README.md#L36-L36](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L36-L36) (`clm_7bd04fad145b63c48ee3b7c39aa2f11d81b62eb6103ad0fcd17b618a6a037cc3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The product supports managing several projects in one window, with project switching via Cmd/Ctrl+1..8 shortcuts. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [docs/README.zh-CN.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/README.zh-CN.md#L19-L22) (`clm_b8535c065ae918553ce37e2635fb23b8813738ff5f744d89d9d230834ec46fa0`)
- [observation/documented] The workspace combines editor, terminal, app preview, and AI panels in one place, letting users code while running commands and previewing. -- evidence: [README.md#L19-L22](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L19-L22), [README.md#L13-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L13-L15) (`clm_37cbaa81091a0b0bf76b8d8bf8ba81108ac25c3f92431c92a71a0dcf2c9ec442`)
- [observation/documented] Theme packs are folders placed in userData/themes/ that appear in Settings for selection; Settings offers an 'Open Themes Folder' action. -- evidence: [docs/theme-packs.md#L11-L13](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L11-L13), [docs/theme-packs.md#L3-L3](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L3-L3), [docs/theme-packs.md#L15-L15](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L15-L15) (`clm_f1c311867b3ff7b31ba4ff761d3eab2c604fe495983e7f50d6bc652d458e2c8d`)
- [observation/documented] A theme pack must contain theme.json following VS Code Color Theme JSON structure (name/type/colors/tokenColors), with optional theme.css and assets/. -- evidence: [docs/theme-packs.md#L32-L33](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L32-L33), [docs/theme-packs.md#L23-L28](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L23-L28), [docs/theme-packs.md#L21-L21](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L21-L21) (`clm_8106f3f7d1aa05bfe6eeb45687d4276555a62357f1c77e234446b7a7396af8bb`)
- [observation/documented] Settings supports importing .zip theme packs, prompting to replace existing themes with the same id; both single-top-level-directory and root-level theme.json zip layouts are accepted. -- evidence: [docs/theme-packs.md#L105-L105](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L105-L105), [docs/theme-packs.md#L107-L110](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L107-L110), [docs/theme-packs.md#L112-L114](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L112-L114) (`clm_6fb693d884be52eee3ce297bea6b3584daf52afd51e0b2d80cd3f5ca24f59a13`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Theme CSS is sandboxed: only relative paths inside the theme folder are allowed; remote/unsafe URLs are ignored and @import is stripped to block external resource loading. -- evidence: [docs/theme-packs.md#L70-L73](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L70-L73) (`clm_57ead4dc81d871de9a1e2cf9dbcc24185bc051cb6e7e89c358afbba0cadde00c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is MIT licensed, with third-party notices located in the third_party/ directory. -- evidence: [README.md#L46-L46](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L46-L46), [README.md#L48-L48](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/README.md#L48-L48) (`clm_3a256a377ba08fa9872b810f98c4571a37f25ff8af22914eab7669867275212b`)

## limitations (1 claim(s))

- [inference/documented] Deleting a theme folder causes the app to fall back to builtin-classic without a blank screen, suggesting built-in fallback handling for missing themes. -- evidence: [docs/theme-packs.md#L120-L126](https://github.com/XCodingLab/XCoding/blob/349a05eeb1e8dd5cbc456301a71bc9706f193fa8/docs/theme-packs.md#L120-L126) (`clm_2c82003ce49b23f6366e4681e44d956d4f7cb458fb3a42794ac4136cd4a5552e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

