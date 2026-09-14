# raphaelregnier/vibe-annotations -- full detail

[Back to orientation](vibe-annotations.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/raphaelregnier/vibe-annotations/97c324e1f96b7bd818106554041060f321a25025/8ecb8626410ca4a9.json](../../../wiki/dossiers/raphaelregnier/vibe-annotations/97c324e1f96b7bd818106554041060f321a25025/8ecb8626410ca4a9.json)

## specifications (2 claim(s))

- [observation/documented] The product is a visual feedback tool for web development: users annotate page elements, make design tweaks, and share the results with AI coding agents or teammates. -- evidence: [README.md#L5-L5](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L5-L5) (`clm_ab3848626b3b62a01535fb1fd2d6b7141733ba92b2bf2a8f34d6f6af148ca320`)
- [observation/documented] The README badge indicates the Chrome extension has 6K+ users on the Chrome Web Store, and the server is distributed as the npm package vibe-annotations-server. -- evidence: [README.md#L3-L3](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L3-L3) (`clm_714bee9cba27f366a440d67d1a58ce95b927a0eb8cb1035ac1c71a0f86eb79ee`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Getting started involves installing the Chrome extension, running 'npx vibe-annotations-server init' (an interactive command that installs the global server, starts it in the background, and configures the AI coding agent), then annotating a localhost page. -- evidence: [README.md#L17-L19](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L17-L19), [README.md#L21-L21](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L21-L21), [README.md#L13-L13](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L13-L13), [README.md#L23-L23](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L23-L23) (`clm_3e9a9f2be29f5bacb723d71532db58b0e7ff843df549a5b46343289c8475d60a`)
- [observation/documented] Repository development practice: contributors work in a pnpm workspace with packages for extension, server, and website; the extension is built with WXT (pnpm dev gives live reload, load unpacked from .output/chrome-mv3), and the server runs via node lib/server.js or bin/cli.js start against 127.0.0.1:3846. -- evidence: [CLAUDE.md#L14-L14](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CLAUDE.md#L14-L14), [CONTRIBUTING.md#L78-L80](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L78-L80), [CONTRIBUTING.md#L67-L67](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L67-L67), [CONTRIBUTING.md#L69-L74](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L69-L74), [CONTRIBUTING.md#L54-L61](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L54-L61) (`clm_840a5fcb776024078b3264c3f566bbf41d69c1678208e855ff79e913465b6a61`)
- [observation/documented] Repository development practice: pull requests should branch from main, include tests where code should be tested, keep the test suite passing, and follow existing code style; commit messages use present tense, imperative mood, and a first line of 72 characters or less. -- evidence: [CONTRIBUTING.md#L42-L46](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L42-L46), [CONTRIBUTING.md#L91-L94](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L91-L94) (`clm_385e457ccc591b904ed3eaa19947993db1acbba7cf9df4fdda33f80418a6e3eb`)
- [observation/documented] Repository development practice: the npm server package is published automatically by a GitHub Action when changes to packages/server/** land on main, with version bumps in packages/server/package.json for intentional releases; the Chrome extension is published to the Web Store by maintainers only. -- evidence: [CONTRIBUTING.md#L104-L104](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L104-L104), [CONTRIBUTING.md#L100-L100](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L100-L100) (`clm_c363f505e7e7992284634b5f6e74709d475f03491e2778a6da1c27cb648a9d2f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] AI coding agents such as Claude Code, Cursor, Windsurf, Codex, and VS Code connect via Model Context Protocol (MCP) to read annotations and implement fixes; the MCP route is the recommended option, with clipboard copy as an alternative. -- evidence: [README.md#L27-L27](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L27-L27), [README.md#L25-L25](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L25-L25), [README.md#L21-L21](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L21-L21), [CLAUDE.md#L28-L31](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CLAUDE.md#L28-L31) (`clm_44a7cc5465a1ab02b9740b97f922356379cbfe593c1b408893ab98982178a681`)
- [observation/documented] The extension communicates only with a local server on port 3846, which the terms describe as the sole network endpoint for the product besides an optional NPM registry version check. -- evidence: [TERMS.md#L29-L31](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L29-L31) (`clm_bb1e1db9a3bd33418194b4c317472dd52524699e3ce00536dc724aed251e00ef`)

## memory-state (1 claim(s))

- [observation/documented] Annotation data is stored locally on the user's machine under ~/.vibe-annotations/, with the Chrome extension using the Chrome Storage API for persistence; no data is sent to external servers. -- evidence: [TERMS.md#L24-L26](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L24-L26) (`clm_3e7070b24578ddefc9b7e322d27416b8442d137036ee5646231773ed3999df9f`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The Chrome extension requests three permissions: activeTab (annotate the current page), storage (persist annotations locally), and scripting (inject the annotation interface). -- evidence: [TERMS.md#L34-L37](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L34-L37) (`clm_1a7e3221dbabeae39155ee368c97c5da668a60bcd25ada1d11292665a2a3bb10`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] The tool is designed to operate exclusively on local development environments (localhost, 127.0.0.1, 0.0.0.0, *.local, *.test, *.localhost, file://), and its terms prohibit annotating production websites or third-party services. -- evidence: [TERMS.md#L46-L50](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L46-L50), [TERMS.md#L15-L19](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L15-L19) (`clm_7b0868d7f7e0a7c5e3246482ce52df5cab446418cd5ae52487a70dd87b4a571d`)
- [observation/documented] The terms disclaim responsibility for AI-generated code quality and instruct users to review all AI-implemented changes before committing, placing responsibility for annotation-based code changes on the user. -- evidence: [TERMS.md#L75-L78](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L75-L78), [TERMS.md#L69-L72](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L69-L72), [TERMS.md#L64-L64](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L64-L64) (`clm_2867a2d8e472515af35d8619f411e1801c960384d09056ce962877ddaebe494f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

