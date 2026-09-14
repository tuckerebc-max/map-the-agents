# tt-a1i/hive -- full detail

[Back to orientation](hive.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tt-a1i/hive/1096789b17cc8215869616d21aa6e76cd139eb19/70e013b173adfc67.json](../../../wiki/dossiers/tt-a1i/hive/1096789b17cc8215869616d21aa6e76cd139eb19/70e013b173adfc67.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Hive runs CLI agents (Claude Code, Codex, Gemini, OpenCode, Qwen, and others) as real PTY processes on the local machine, with a browser workbench where an Orchestrator plans and delegates to workers. -- evidence: [README.md#L11-L13](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L11-L13) (`clm_2c8f27c6e25a8b43d64c55dfb011a70ee27104b315e06d764f385195438b8596`)
- [observation/documented] An experimental Workflows feature (off by default) lets the Orchestrator author and run multi-stage multi-agent workflows, with a Workflows panel showing runs, phase results, logs, schedules, and stop controls, plus a CLI policy for workflow-created agents. -- evidence: [README.md#L182-L187](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L182-L187), [README.md#L242-L260](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L242-L260) (`clm_275ef0ca4ddc880471f825963dee1fe42aa3e6acd15dfefc46f37d6f765712e6`)
- [observation/documented] A fully client-side demo mode (fake orchestrator plus two workers with prerecorded scrollback and a prefilled task list) is available from the first-run wizard without a server or any real CLI agent. -- evidence: [README.md#L96-L100](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L96-L100) (`clm_b856361d8448c23b5ed4eb44f2b868a2f4875fc74461780e281f23fc28adae3c`)

## design-choices (1 claim(s))

- [observation/documented] Hive is local-first: the runtime binds to 127.0.0.1, stores SQLite metadata under ~/.config/hive (or %APPDATA%\hive on Windows, or $HIVE_DATA_DIR), and the browser UI talks to it over HTTP and WebSocket. -- evidence: [README.md#L302-L318](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L302-L318), [README.md#L191-L207](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L191-L207), [README.md#L28-L35](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L28-L35), [README.md#L242-L260](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L242-L260) (`clm_1f30d7325dee632d4e90818049be47911d2f936c813f7323da9584967dc6e44d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors develop with pnpm (`pnpm install`, `pnpm dev`, `pnpm check`, `pnpm build`, `pnpm test`); dev mode runs the runtime on port 4010 with Vite on 5180 proxying API and WebSocket traffic. -- evidence: [README.md#L445-L446](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L445-L446), [README.md#L450-L454](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L450-L454), [README.md#L440-L443](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L440-L443) (`clm_370da2c42b4f1bb160c4f4bb855465d7a231e71a15f6b57e211124eae72a6c9a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Optional Remote access (off by default) pairs a phone to the desktop via a desktop-confirmed pairing flow and relays through an end-to-end encrypted gateway; paired devices have the same authority as the local browser and can be revoked, and CLI subcommands like `hive remote login/status/devices/revoke` manage it. -- evidence: [CHANGELOG.md#L35-L57](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/CHANGELOG.md#L35-L57), [README.md#L267-L271](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L267-L271), [README.md#L275-L284](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L275-L284) (`clm_7741b9c5651ebf26cf106aff78086a89cea6d7e17c1efc939f9ba1f46106bae3`)
- [observation/documented] The web shell is installable as a PWA in Chromium browsers via the omnibox install icon, with a service worker that caches the SPA shell and assets but never intercepts /api/*, /ws/*, or non-GET requests. -- evidence: [README.md#L146-L151](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L146-L151), [CHANGELOG.md#L174-L243](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/CHANGELOG.md#L174-L243) (`clm_14a7556807ef01215f295139cef32b37e1adfaf16290c5fcf174b9d2add04045`)

## memory-state (1 claim(s))

- [observation/documented] The shared task graph is a markdown file at `<workspace>/.hive/tasks.md` that users can inspect or edit outside the app, and the editor handles external-file conflicts with Reload/Keep Local options. -- evidence: [README.md#L215-L220](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L215-L220), [README.md#L53-L57](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L53-L57), [README.md#L429-L430](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L429-L430) (`clm_31a60a9f9b9229542963b9ff3473fa0aeccdf2771f9a11da9896ce8c64dbb783`)

## orchestration (2 claim(s))

- [observation/documented] The Orchestrator is itself a real agent CLI process, not a scripted manager; it dispatches tasks with `team send <worker> "<task>"` and workers report back with `team report`. -- evidence: [README.md#L169-L175](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L169-L175), [README.md#L53-L57](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L53-L57) (`clm_cc624db332fe4912c8f74607df88f39cd1efd535f6ec9489af09c300c9792b71`)
- [observation/documented] Auto-staff (experimental, on by default) lets the Orchestrator `team spawn` temporary coders, testers, and reviewers sized to the task, and Hive dismisses those ephemeral workers once their dispatch reports back. -- evidence: [README.md#L242-L260](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L242-L260), [README.md#L177-L180](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L177-L180) (`clm_eae4861820d35373f3b20253dd2983e74635ee9065b4dd4534f56527111d061b`)

## tools-permissions (1 claim(s))

- [observation/documented] Built-in agent presets intentionally launch CLIs in bypass/non-interactive modes (e.g. `--dangerously-skip-permissions` for Claude Code, `--yolo` for Gemini), so workers can run arbitrary shell commands in the workspace; Hive provides no sandboxing or multi-user auth. -- evidence: [README.md#L302-L318](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L302-L318), [README.md#L262-L263](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L262-L263), [README.md#L224-L235](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L224-L235) (`clm_f70a5580df06360455211a27adfac197f86b2a2ffcf00c6dfe1d0903d23ea8ba`)

## evaluation (1 claim(s))

- [inference/documented] No evidence in the provided slices describes any benchmark or success-rate evaluation of the agent system; the only test-related material is the repository's own `pnpm test` check, so agent performance evaluation appears undocumented here. -- evidence: [README.md#L450-L454](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L450-L454) (`clm_95c31f7f9e6ac56d3d42db7a1bdf29808e32383b1e78f700e9e59904b6f7940d`)

## dependencies (1 claim(s))

- [observation/documented] Hive requires Node.js 22 or newer and depends on native packages node-pty and better-sqlite3, so native build tooling may be needed when prebuilt binaries are unavailable; agent CLIs must be installed and authenticated by the user, not by Hive. -- evidence: [README.md#L294-L296](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L294-L296), [README.md#L368-L370](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L368-L370), [README.md#L106-L108](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L106-L108), [README.md#L237-L238](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L237-L238) (`clm_815b740adffdb023271ef1961cb39cee10173648245cdda3f4760f496689b819`)

## limitations (1 claim(s))

- [observation/documented] Hive does not provide sandboxing, multi-user authentication, or any bundled agent model; it coordinates CLIs the user already runs locally, and same-machine processes reaching the local port are treated as trusted. -- evidence: [README.md#L302-L318](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L302-L318), [README.md#L262-L263](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L262-L263) (`clm_06eeb9b112005d4f77656715d8e43968151aff2864ba5ded782ac5967ebb0b1b`)

## relevance (1 claim(s))

- [observation/documented] Hive targets users who already run CLI agents and want coordination for multi-agent work such as implement/review splits, parallel bug hunts, and research/draft/fact-check pipelines, without juggling terminal windows. -- evidence: [README.md#L15-L15](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L15-L15), [README.md#L61-L61](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L61-L61), [README.md#L83-L83](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L83-L83), [README.md#L43-L44](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L43-L44), [README.md#L72-L72](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L72-L72) (`clm_545826e3e56ae737a858c1c5741e46b7508d82fb8aa20bd7338db4fda4c517f5`)

