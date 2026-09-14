# wellingfeng/ultragamestudio

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 034f599668f3 @ 5040c6a7d94315f8

## Summary (orientation draft, not independently verified)

README and SELF-DEV describe UltraGameStudio, a Tauri/React desktop AI coding agent specialized for game development, with asset-generation slash modes, a 40+ expert roster, free-channel model routing via a local Rust proxy, and a /studio dynamic harness. Evidence is documentation-only; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The stack comprises a Tauri 2/Rust desktop shell, React 18 with Vite 5 and TypeScript 5, Zustand state, Tailwind styling, and a Rust tiny_http+ureq free-channel proxy. -- evidence: [README.md#L47-L55](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L47-L55), [README.md#L320-L328](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L320-L328)
  - [observation/documented] A local Rust reverse proxy binds to 127.0.0.1, routes per channel at /ch/<channelId>, and translates between Anthropic and OpenAI-compatible streaming protocols so Claude Code can use non-Anthropic providers. -- evidence: [README.md#L313-L316](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L313-L316), [README.md#L144-L148](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L144-L148)
- design-choices (1 claim(s)):
  - [observation/documented] The product is local-first: sessions, favorites, scheduled prompts, API keys, and workspace history are stored locally and no hosted server is required. -- evidence: [README.md#L206-L208](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L206-L208)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm run dev/typecheck/lint/test/desktop/package from app/, and PRs should describe behavior changes, list verification commands, link issues, and include screenshots for UI changes. -- evidence: [README.md#L377-L377](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L377-L377), [README.md#L361-L368](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L361-L368)
  - [observation/documented] Repository development practice: SELF-DEV.md advises running workflows from a packaged standalone exe via run.bat rather than tauri dev, since dev mode watches source and hot-reloads would interrupt running workflows; a copy-workspace approach is recommended for self-modification. -- evidence: [SELF-DEV.md#L36-L36](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L36-L36), [SELF-DEV.md#L29-L32](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L29-L32), [SELF-DEV.md#L3-L3](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L3-L3), [SELF-DEV.md#L9-L13](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L9-L13)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent ships a roster of 40+ game-development specialist roles spanning engine, programming, design, art/audio, and production categories, configurable in Settings including engine and council mode. -- evidence: [README.md#L140-L140](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L140-L140), [README.md#L134-L138](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L134-L138), [README.md#L132-L132](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L132-L132)
- interfaces (2 claim(s)):
  - [observation/documented] Asset generation is exposed through slash commands: /image, /sprite, /music, /video, /mesh-mode-start, /comfyui-mode-start, /speech-mode-start, with matching *-mode-end commands to exit. -- evidence: [README.md#L292-L294](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L292-L294), [README.md#L128-L128](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L128-L128), [README.md#L118-L126](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L118-L126)
  - [observation/documented] A CLI form exists for the studio harness: ugs studio "<task>" with --json, --interactive, and --cwd options, runnable alongside the desktop app. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (4 claim(s)):
  - [observation/documented] The /studio command generates an on-the-fly execution harness with parallel subagents, adversarial verification, and acceptance gates, choosing among six internal strategies automatically. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174), [README.md#L168-L168](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L168-L168)
  - [observation/documented] Each /studio run is logged under .ugs-run/<run-id>/ with a task ledger, events, verdict, and final result, and reuses local claude CLI credentials without extra config. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174)
More evidence: [full detail](ultragamestudio.detail.md)

Metadata and full claim list: [full detail](ultragamestudio.detail.md)
Human notes ([notes](ultragamestudio.notes.md), never overwritten by build)

[Back to map index](../../index.md)
