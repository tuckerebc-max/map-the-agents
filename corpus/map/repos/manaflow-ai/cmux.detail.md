# manaflow-ai/cmux -- full detail

[Back to orientation](cmux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/manaflow-ai/cmux/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/7737fb865abe78b6.json](../../../wiki/dossiers/manaflow-ai/cmux/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/7737fb865abe78b6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] cmux is a native macOS app built with Swift and AppKit (not Electron), using libghostty for GPU-accelerated terminal rendering. -- evidence: [README.md#L87-L94](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L87-L94), [README.md#L332-L332](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L332-L332), [README.md#L125-L125](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L125-L125) (`clm_0b034bd9d02bff3f122cbfb9838ef0984e4b7233068285ba6bef7a7b6477b90a`)
- [observation/documented] An in-app browser can be split beside the terminal, with a scriptable API ported from vercel-labs/agent-browser for snapshotting, clicking, filling forms, and evaluating JavaScript. -- evidence: [README.md#L30-L85](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L30-L85), [README.md#L364-L364](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L364-L364), [README.md#L129-L129](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L129-L129) (`clm_dd7a977fd81359edc34f5ebe7d7211907b730b0af8d403589ac6a3c692bcb41d`)

## design-choices (2 claim(s))

- [observation/documented] cmux positions itself as a non-prescriptive primitive: a terminal, browser, notifications, workspaces, splits, tabs, and CLI, without forcing an opinionated agent workflow. -- evidence: [README.md#L135-L135](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L135-L135), [README.md#L137-L137](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L137-L137) (`clm_3de5165edc34a1d2c3e2be931f8d4f381259aa90ee4e803122cf8c38eff31341`)
- [observation/documented] Resume bindings are security-gated: only trusted bindings auto-run, approved command prefixes are bound to working directory and environment values, and sensitive environment keys are dropped before storage. -- evidence: [README.md#L292-L299](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L292-L299) (`clm_f7c3ad77a082cae5bd0b0d582fa020dc3db99d23d34bddb824eb0a832f9a8333`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors must sign a CLA (v2.2), which can be signed electronically by posting an exact phrase as a PR comment; the PR audit notes the contributor's unsigned CLA as an external blocker. -- evidence: [PR-10599-AUDIT.md#L87-L90](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L87-L90), [PR-10599-AUDIT.md#L142-L144](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L142-L144), [CLA.md#L5-L5](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/CLA.md#L5-L5) (`clm_018442b9651ada44c2ed6dbbe81441788b2e84ec42c2362bef69b7aa4e2c0dea`)
- [observation/documented] Repository development practice: the PR #10599 audit records focused Swift package test runs (e.g., 11 tests in CmuxFilePreviewCore, 24 in CmuxSyntaxHighlighting) plus project lint/check scripts such as check-pbxproj.sh and lint-pbxproj-test-wiring.sh. -- evidence: [PR-10599-AUDIT.md#L99-L110](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L99-L110) (`clm_3c1c188a716f1da30c780e6a064266f8a8a121f01f683af7df62cb0de0dc3e4a`)
- [observation/documented] Repository development practice: the PR audit documents review-tooling gates (Cursor Bugbot, CodeRabbit, Vercel preview authorization) and notes all 58 inline review threads resolved at the audited head. -- evidence: [PR-10599-AUDIT.md#L87-L90](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L87-L90), [PR-10599-AUDIT.md#L78-L85](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L78-L85) (`clm_18d10fd31b97f44d1b2a2edcf4470129f985dfbc558758818bd48a6b15d03600`)

## skills-patterns (1 claim(s))

- [observation/documented] cmux supports reusable skills for agents running in it (CLI control, workspace automation, settings, browser surfaces), with an open collection in the manaflow-ai/cmux-skills repository. -- evidence: [README.md#L368-L368](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L368-L368) (`clm_a9ece0720fa6a7ebc58bea40c95738efd583efbc22d74516d99168ab3543ffe5`)

## interfaces (4 claim(s))

- [observation/documented] The product exposes a CLI and Unix socket API to create workspaces, split panes, send keystrokes, read screen contents, take screenshots, and drive the in-app browser. -- evidence: [README.md#L87-L94](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L87-L94), [README.md#L131-L131](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L131-L131), [README.md#L360-L360](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L360-L360) (`clm_e1b5f6142c611e201527b74b1653970bf728583ea60909a3963c03f92ab0bc2c`)
- [observation/documented] cmux provides a `cmux notify` CLI and picks up OSC 9/99/777 terminal escape sequences to trigger notifications, usable from agent hooks. -- evidence: [README.md#L356-L356](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L356-L356), [README.md#L127-L127](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L127-L127) (`clm_b9580984505b4a10a070c74e1125a56ffecf70c28319574bf5a7fa998c81bd67`)
- [observation/documented] cmux reads the existing ~/.config/ghostty/config for themes, fonts, colors, and terminal keybindings, while its own settings live in ~/.config/cmux/cmux.json with editable shortcuts. -- evidence: [README.md#L372-L372](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L372-L372), [README.md#L87-L94](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L87-L94), [README.md#L376-L376](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L376-L376) (`clm_c791d2a25b0af66afaafee7a973d132a49a64b83653f73f7bf48717cca24f242`)
- [observation/documented] The CLI supports SSH workspaces (`cmux ssh user@remote` with an optional initial --command), remote tmux attachment, and custom surface resume commands such as `cmux surface resume set`. -- evidence: [README.md#L352-L352](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L352-L352), [README.md#L30-L85](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L30-L85), [README.md#L286-L290](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L286-L290) (`clm_f6d4934b8263a9e7d74b73de83aae7b0f3e11d793d859ad6f4f942f49239902a`)

## memory-state (2 claim(s))

- [observation/documented] On quit, cmux saves a versioned snapshot under ~/Library/Application Support/cmux/ and restores window/workspace/pane layout, working directories, best-effort scrollback, and browser history on relaunch. -- evidence: [README.md#L254-L259](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L254-L259), [README.md#L321-L324](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L321-L324) (`clm_e3ff139b3fe5ca32040bd3f1bdc95fa9bc0442e2f7e78b9a364ec3b9e9b69c7c`)
- [observation/documented] Agent hooks (`cmux hooks setup`) save native session IDs under ~/.cmuxterm/ so supported agents like Claude Code, Codex, and OpenCode can resume sessions on reopen. -- evidence: [README.md#L276-L280](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L276-L280), [README.md#L270-L274](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L270-L274), [README.md#L321-L324](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L321-L324), [README.md#L267-L268](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L267-L268) (`clm_589c19a93afb31a38750191703fba035cffdb226153d2aa24f2d0be3e648b04a`)

## orchestration (1 claim(s))

- [observation/documented] When an agent spawns subagents or teammates, cmux turns them into native panes and splits, and supports Claude Code teams and oh-my-opencode multi-model orchestration. -- evidence: [README.md#L348-L348](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L348-L348) (`clm_8de61ea72895fd3de4ab4639107c4cf034d5a89e91c78f78340b3691d392c0f7`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Stable releases auto-update via Sparkle, and the nightly build is a separate app with its own bundle ID and Sparkle feed built from the latest main commit. -- evidence: [README.md#L248-L248](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L248-L248), [README.md#L104-L104](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L104-L104) (`clm_efae817ed2e158423f84d5d89a19bdd6538e1458df8f53f97bc3e5c12c128c23`)
- [observation/documented] The PR audit states Highlightr is pinned exactly and that the audited change introduced no shell execution, network/eval, path traversal, authentication, or secret-handling paths. -- evidence: [PR-10599-AUDIT.md#L71-L74](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/PR-10599-AUDIT.md#L71-L74) (`clm_55bf3fc0cd120da9bdc12600958a081255941f84501907bfb198571ed8ff4b77`)

## limitations (2 claim(s))

- [observation/documented] cmux does not checkpoint arbitrary live process state; for live detach/reattach users must opt into `cmux local-tmux`, and a local tmux server cannot survive logout, restart, or power loss. -- evidence: [README.md#L380-L388](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L380-L388), [README.md#L261-L265](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L261-L265) (`clm_573c7d00bef214c2b4cf52725ed558f05446cf06a064c4be042d4b8f841e25c9`)
- [observation/documented] cmux supports macOS only, for now; an iOS companion app exists in beta on TestFlight. -- evidence: [README.md#L340-L340](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L340-L340), [README.md#L336-L336](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L336-L336) (`clm_980886ecbf94247bfa09218a3a4eb22589304e938ea385f834204a5071e39ed9`)

## relevance (1 claim(s))

- [observation/documented] cmux targets developers running multiple AI coding agents (Claude Code, Codex, OpenCode, Gemini CLI, etc.) in parallel, surfacing which agent needs attention via rings, badges, and a notification panel. -- evidence: [README.md#L344-L344](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L344-L344), [README.md#L123-L123](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L123-L123), [README.md#L356-L356](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L356-L356), [README.md#L127-L127](https://github.com/manaflow-ai/cmux/blob/419cf0a00cc3a86c80622dc6fe0eb03d498a2b90/README.md#L127-L127) (`clm_afd50d603ff7a6ef2880cf59d40c019f48780770f3cef122d06bdb5a61e0b472`)

