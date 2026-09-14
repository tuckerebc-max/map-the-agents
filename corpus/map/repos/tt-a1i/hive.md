# tt-a1i/hive

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1096789b17cc @ 70e013b173adfc67

## Summary (orientation draft, not independently verified)

Hive runs CLI agents (Claude Code, Codex, Gemini, OpenCode, Qwen, and others) as real PTY processes on the local machine, with a browser workbench where an Orchestrator plans and delegates to workers. The Orchestrator is itself a real agent CLI process, not a scripted manager; it dispatches tasks with `team send <worker> "<task>"` and workers report back with `team report`. Evidence coverage: 136 of 173 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Hive runs CLI agents (Claude Code, Codex, Gemini, OpenCode, Qwen, and others) as real PTY processes on the local machine, with a browser workbench where an Orchestrator plans and delegates to workers. -- evidence: [README.md#L11-L13](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L11-L13)
  - [observation/documented] An experimental Workflows feature (off by default) lets the Orchestrator author and run multi-stage multi-agent workflows, with a Workflows panel showing runs, phase results, logs, schedules, and stop controls, plus a CLI policy for workflow-created agents. -- evidence: [README.md#L182-L187](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L182-L187), [README.md#L242-L260](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L242-L260)
- design-choices (1 claim(s)):
  - [observation/documented] Hive is local-first: the runtime binds to 127.0.0.1, stores SQLite metadata under ~/.config/hive (or %APPDATA%\hive on Windows, or $HIVE_DATA_DIR), and the browser UI talks to it over HTTP and WebSocket. -- evidence: [README.md#L302-L318](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L302-L318), [README.md#L191-L207](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L191-L207), [README.md#L28-L35](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L28-L35), [README.md#L242-L260](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L242-L260)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors develop with pnpm (`pnpm install`, `pnpm dev`, `pnpm check`, `pnpm build`, `pnpm test`); dev mode runs the runtime on port 4010 with Vite on 5180 proxying API and WebSocket traffic. -- evidence: [README.md#L445-L446](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L445-L446), [README.md#L450-L454](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L450-L454), [README.md#L440-L443](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L440-L443)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Optional Remote access (off by default) pairs a phone to the desktop via a desktop-confirmed pairing flow and relays through an end-to-end encrypted gateway; paired devices have the same authority as the local browser and can be revoked, and CLI subcommands like `hive remote login/status/devices/revoke` manage it. -- evidence: [CHANGELOG.md#L35-L57](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/CHANGELOG.md#L35-L57), [README.md#L267-L271](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L267-L271), [README.md#L275-L284](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L275-L284)
  - [observation/documented] The web shell is installable as a PWA in Chromium browsers via the omnibox install icon, with a service worker that caches the SPA shell and assets but never intercepts /api/*, /ws/*, or non-GET requests. -- evidence: [README.md#L146-L151](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/README.md#L146-L151), [CHANGELOG.md#L174-L243](https://github.com/tt-a1i/hive/blob/1096789b17cc8215869616d21aa6e76cd139eb19/CHANGELOG.md#L174-L243)
- memory-state (1 claim(s)):
More evidence: [full detail](hive.detail.md)

Metadata and full claim list: [full detail](hive.detail.md)
Human notes ([notes](hive.notes.md), never overwritten by build)

[Back to map index](../../index.md)
