# varie-ai/workstation

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 96d500b5cbb0 @ 225530cf02383a58

## Summary (orientation draft, not independently verified)

README-only evidence for Workstation, a macOS desktop app that manages Claude Code sessions with remote control via OpenClaw messaging, voice control, and work-tracking skills. Claims below are documentation-based; no code inspection is available.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A built-in bridge watches Claude Code sessions and sends notifications with screenshots when Claude finishes, requests plan approval, or asks a question. -- evidence: [README.md#L148-L148](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L148-L148), [README.md#L150-L154](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L150-L154)
- design-choices (2 claim(s)):
  - [observation/documented] The app claims to run entirely locally with no telemetry or analytics; checkpoints, session data, and configuration live in ~/.varie/ and are not synced or uploaded. -- evidence: [README.md#L277-L280](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L277-L280), [README.md#L275-L275](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L275-L275)
  - [observation/documented] Voice audio is processed on-device via Apple Speech or WhisperKit, while LLM-based voice routing and OpenClaw agent integration are opt-in features that are off by default. -- evidence: [README.md#L277-L280](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L277-L280)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build from source with npm install and npm run dev, run tests via npm run test, and package for macOS with npm run package:mac. -- evidence: [README.md#L88-L93](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L88-L93), [README.md#L297-L302](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L297-L302)
- skills-patterns (1 claim(s)):
  - [observation/documented] The plugin provides work-tracking skills such as /work-resume with fuzzy matching, /work-recover for post-crash checkpoint comparison, /work-stats for token usage, and /discover-projects to scan for new repos. -- evidence: [README.md#L252-L269](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L252-L269)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes slash commands including /work-start, /work-checkpoint, /work-report, /work-sessions, /route, /dispatch, /projects, and /workstation for session tracking, routing, and configuration. -- evidence: [README.md#L242-L246](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L242-L246), [README.md#L252-L269](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L252-L269), [README.md#L237-L239](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L237-L239)
  - [observation/documented] Screenshot capture supports three modes: session (Electron built-in, no permission), session plus multi-page scrollback via --pages N (max 10), and full-screen capture requiring macOS Screen Recording. -- evidence: [README.md#L187-L187](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L187-L187), [README.md#L181-L185](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L181-L185)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] Sessions are identified by repo/project name, and commands like 'run tests in my-app' are routed to the matching session automatically without needing session IDs. -- evidence: [README.md#L165-L168](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L165-L168), [README.md#L138-L138](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L138-L138)
  - [observation/documented] A manager terminal serves as a central hub for cross-project commands, and multiple Claude Code sessions can run side-by-side with auto-dispatch by repo name, task ID, or context. -- evidence: [README.md#L47-L51](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L47-L51)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](workstation.detail.md)

Metadata and full claim list: [full detail](workstation.detail.md)
Human notes ([notes](workstation.notes.md), never overwritten by build)

[Back to map index](../../index.md)
