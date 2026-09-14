# elirantutia/vibeyard

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 19bc19f0fac0 @ 4f13da1bc0dfb5da

## Summary (orientation draft, not independently verified)

Vibeyard is described as an IDE built for AI coding agents: it manages multiple agent sessions, runs them in parallel, tracks costs, and supports Claude Code, Codex CLI, and Gemini CLI. Documented features include a customizable per-project dashboard with widgets, a kanban task board, P2P session sharing, multi-session management, cost/context tracking, a session inspector, and an AI Readiness Score. Evidence coverage: 152 of 172 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vibeyard is described as an IDE built for AI coding agents: it manages multiple agent sessions, runs them in parallel, tracks costs, and supports Claude Code, Codex CLI, and Gemini CLI. -- evidence: [README.md#L56-L56](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L56-L56), [README.md#L16-L19](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L16-L19)
- components (2 claim(s)):
  - [observation/documented] Documented features include a customizable per-project dashboard with widgets, a kanban task board, P2P session sharing, multi-session management, cost/context tracking, a session inspector, and an AI Readiness Score. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54), [README.md#L37-L37](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L37-L37)
  - [inference/documented] The changelog suggests the app was renamed from CCIDE to Vibeyard and evolved from macOS-only unsigned builds to signed, cross-platform releases. -- evidence: [CHANGELOG.md#L651-L657](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L651-L657), [CHANGELOG.md#L752-L752](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L752-L752), [CHANGELOG.md#L632-L643](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CHANGELOG.md#L632-L643)
- design-choices (2 claim(s)):
  - [observation/documented] Each agent session runs in its own PTY, and multiple Claude profiles are supported with each session backed by an isolated config directory so credentials and history do not mix. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54)
  - [observation/documented] P2P session sharing uses encrypted WebRTC connections with read-only or read-write modes and PIN-based authentication. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run tests with npm test, test:watch, or test:coverage using Vitest with v8 coverage, with tests co-located as *.test.ts files. -- evidence: [CLAUDE.md#L30-L30](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L30-L30), [CLAUDE.md#L24-L28](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L24-L28)
  - [observation/documented] Repository development practice: building uses npm run build and npm start, requires Node v24 per .nvmrc, has no lint tooling configured, and changes require a rebuild plus app restart since there is no hot reload. -- evidence: [CLAUDE.md#L16-L16](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L16-L16), [CLAUDE.md#L11-L14](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L11-L14), [CLAUDE.md#L18-L18](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/CLAUDE.md#L18-L18)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes keyboard-driven interfaces, including Cmd+\ to spin up new sessions in swarm mode and Cmd+Shift+I to open the session inspector. -- evidence: [README.md#L41-L54](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L41-L54)
  - [observation/documented] Distribution channels documented are macOS .dmg, Linux .deb and AppImage, Windows NSIS installer and portable .exe, and a global npm package that downloads and launches the app on first run. -- evidence: [README.md#L90-L90](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L90-L90), [README.md#L64-L64](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L64-L64), [README.md#L68-L68](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L68-L68), [README.md#L81-L81](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L81-L81), [README.md#L85-L88](https://github.com/elirantutia/vibeyard/blob/19bc19f0fac04f11e7d9e5cf68ed75ac7d291566/README.md#L85-L88)
More evidence: [full detail](vibeyard.detail.md)

Metadata and full claim list: [full detail](vibeyard.detail.md)
Human notes ([notes](vibeyard.notes.md), never overwritten by build)

[Back to map index](../../index.md)
