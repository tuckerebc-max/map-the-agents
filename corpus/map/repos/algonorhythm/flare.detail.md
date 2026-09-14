# algonorhythm/flare -- full detail

[Back to orientation](flare.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/algonorhythm/flare/5adc94b0616c6eae8c1f86aa97df264968fc52ab/f5b26167e3c40f3e.json](../../../wiki/dossiers/algonorhythm/flare/5adc94b0616c6eae8c1f86aa97df264968fc52ab/f5b26167e3c40f3e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Architecture separates a pure shared/ engine (import parser, resolver, incremental graph builder, scanner), an Electron-free core in electron/core.ts, desktop and browser adapters, and a React renderer with the three graph views, Monaco, and xterm terminals. -- evidence: [README.md#L438-L459](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L438-L459) (`clm_f91c7f521ac5bca3c9f83eb89ca880bd9de94944c76b67462d25034036992a9d`)

## design-choices (2 claim(s))

- [observation/documented] One implementation serves two transports: electron/core.ts holds all behavior as channel handlers, with desktop and browser adapters only translating; a test reportedly enforces that neither adapter names a channel. -- evidence: [README.md#L430-L436](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L430-L436) (`clm_0ccf9434076aa99200562c5c0bc8b209441540fc265463eab365d2191a047f26`)
- [observation/documented] Flare deliberately does not lock files, arguing a lock would be an ignorable request that can silently fail open; instead agents announce intentions in a Channel and contention is surfaced on the graph and in review. -- evidence: [README.md#L151-L155](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L151-L155), [README.md#L172-L179](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L172-L179) (`clm_d8ae073b1b08b916ad6b359fa3e212262e74b4887d309664feefa764dd4480bd`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: testing is via npm test (633 vitest unit tests), npm run e2e (80 Playwright tests), and npm run verify (build + unit + e2e); releases build one runner per platform via a GitHub Actions matrix. -- evidence: [README.md#L512-L517](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L512-L517), [README.md#L422-L426](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L422-L426) (`clm_b05567290a2992a004c538a8a0619dce1dc61dbe34b9452f9ad56ca8007ece52`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Flare exposes an MCP endpoint at /mcp/<slug> with tools including graph_overview, impact_of, tasks_list, task_get, task_update, task_create, decision_record, question_ask, working_agreement, chat_post, chat_read, and agents_list. -- evidence: [README.md#L597-L605](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L597-L605), [README.md#L379-L418](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L379-L418), [README.md#L356-L358](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L356-L358) (`clm_52a23282974ea8f2bb1853dd8ac178215d760de9d2fa3aae35d3c73b7fa661da`)
- [observation/documented] The UI offers three graph views — Canvas (default), Wheel, and Districts treemap — switchable from the toolbar or command palette, each honoring the active lens, selection, collapsed directories, and search filter. -- evidence: [README.md#L37-L38](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L37-L38), [README.md#L40-L57](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L40-L57) (`clm_ef05c7214423757b2d5eb65ccc4625cbf8e373dd7cbcc56ec2476d2906501441`)
- [observation/documented] The browser server exposes one shared port (shown as 7345 in the printed URLs) where the port itself is the start screen; each project gets a stable slug URL, runs as its own process, and agents connect over the same port at /mcp/<slug>. -- evidence: [README.md#L570-L574](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L570-L574), [README.md#L597-L605](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L597-L605), [README.md#L564-L568](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L564-L568) (`clm_66b737b89966d66400da69238589d4c5503bfb22600b4945d9258a0cf0fa1b56`)

## memory-state (2 claim(s))

- [observation/documented] Every change burst is snapshotted into a local shadow history that can be diffed and reverted per file or whole tree; review supports reverting a file, a burst, or jumping to the last state whose checks passed. -- evidence: [README.md#L256-L285](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L256-L285), [README.md#L8-L12](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L8-L12) (`clm_a3cdfef4f4349d7f5a40f237e541f9cfd7717edb063885dbf3352dd45a575f00`)
- [observation/documented] Agent identity is minted from the MCP session, which is established on initialize and echoed on every request, letting Flare name agents like 'Claude 2' and attribute writes where process lists cannot distinguish sessions. -- evidence: [README.md#L196-L214](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L196-L214) (`clm_47ecdbce7234ce07d74315d863cd2982407375738d9c8d8d2ca9f53e631b0307`)

## orchestration (2 claim(s))

- [observation/documented] A routine wizard configures agent behavior when out of work: re-check the board, record design decisions as proposals a human must approve, park questions instead of halting, and an editable working agreement returned by the working_agreement tool. -- evidence: [README.md#L108-L125](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L108-L125) (`clm_370465cbf97680773e0b3b19f22f77e528e16d3054f62cc866bd1052bf80ea04`)
- [observation/documented] Flare can answer an assistant's stop hook with the board state, handing back a workable card by name; it adds a Stop hook to local .claude/settings.local.json and removes it when switched off, firing only once per stop. -- evidence: [README.md#L132-L139](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L132-L139) (`clm_e8d9fa1d609a541cd0492800cb417c60422b523ff3d50e7d668d262a55e4924c`)

## tools-permissions (1 claim(s))

- [observation/documented] Browser access is gated by a token generated on first run and stored in ~/.flare/web-token, settable via --token or $FLARE_TOKEN and disableable with --no-token; the MCP endpoint stays token-free and loopback-only by default. -- evidence: [README.md#L623-L631](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L623-L631), [README.md#L633-L635](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L633-L635) (`clm_8d6d8d1b924a0de3a8ba4582fda96069251906404675452d8c84ba6fa8cf6ddf`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Flare requires Node 20 or newer, and its only native dependency is the terminal's PTY module (@lydell/node-pty), shipped as a per-platform prebuilt binary; everything else is pure JavaScript. -- evidence: [README.md#L671-L672](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L671-L672), [README.md#L466-L466](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L466-L466), [README.md#L512-L517](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L512-L517), [README.md#L674-L676](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L674-L676) (`clm_3ec73970e6af72f2e5f2ed744eaf8cba16f147bf79cbc07a5d29bacb799bbb36`)

## limitations (2 claim(s))

- [observation/documented] macOS arm64 packages are built and signed but have never been launched on Apple silicon, which is what the beta label on the macOS DMGs denotes; the project's hardware is Intel. -- evidence: [README.md#L478-L483](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L478-L483), [README.md#L488-L494](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L488-L494) (`clm_5b0a37ca8f1d179415472f1c4f3ce1564b8df0700fd1ff35a00faccd21a2785f`)
- [observation/documented] macOS builds are ad-hoc signed and un-notarised, so Gatekeeper refuses first launch; users must right-click → Open or clear the quarantine attribute. -- evidence: [README.md#L501-L503](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L501-L503), [README.md#L496-L499](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L496-L499) (`clm_d2cf9c798e2662c1cc6b209edf9d2416eabf5542a3cd8f412a4bb71ac6faba5b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

