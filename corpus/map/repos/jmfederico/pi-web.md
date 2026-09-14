# jmfederico/pi-web

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 46579c049a30 @ 3287e18d140e16b7

## Summary (orientation draft, not independently verified)

Selected evidence records: The product organizes work hierarchically: a machine is a runtime endpoint, a project is a folder on it, a workspace is a provider-owned working folder, and a session is a Pi Coding Agent chat inside a workspace. Sessions are designed to survive browser disconnects, letting users supervise agents from any browser while work continues on the host machine.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The product organizes work hierarchically: a machine is a runtime endpoint, a project is a folder on it, a workspace is a provider-owned working folder, and a session is a Pi Coding Agent chat inside a workspace. -- evidence: [README.md#L78-L83](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L78-L83)
  - [observation/documented] Sessions are designed to survive browser disconnects, letting users supervise agents from any browser while work continues on the host machine. -- evidence: [README.md#L24-L29](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L24-L29), [README.md#L31-L31](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L31-L31)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Configuration resolves as defaults, then the global config file, then environment overrides; project-local <project>/.pi-web/config.json can override upload and attachment defaults and merge allowed paths. -- evidence: [docs/config.md#L36-L38](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L36-L38), [docs/config.md#L40-L40](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L40-L40), [docs/config.md#L108-L108](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L108-L108)
- memory-state (2 claim(s)):
  - [observation/documented] PI_WEB_DATA_DIR sets the root for managed runtime state (default ~/.pi-web), holding project and machine registries, discovered plugins, the session-daemon socket, and session archives; each data directory starts independent and empty. -- evidence: [docs/config.md#L198-L198](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L198-L198), [docs/config.md#L200-L200](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L200-L200)
  - [observation/documented] One live session daemon owns each data directory, recording ownership in sessiond-owner.json; a second daemon pointed at the same directory fails loudly at startup, while stale markers from dead daemons are taken over automatically. -- evidence: [docs/config.md#L202-L202](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L202-L202)
- orchestration (1 claim(s)):
  - [observation/documented] PI WEB can register other PI WEB runtimes as remote machines, with one browser-facing instance proxying projects, files, git state, sessions, terminals, and Pi package management from trusted remote machines. -- evidence: [README.md#L105-L105](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L105-L105)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default workspace-relative file reads stay inside the workspace and absolute paths are denied; pathAccess.allowedPaths grants the file explorer access to specific external filesystem roots, with symlink escapes rejected, though this is not a sandbox for the agent or OS user. -- evidence: [docs/config.md#L230-L230](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L230-L230), [docs/config.md#L226-L226](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L226-L226), [docs/config.md#L216-L216](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L216-L216), [docs/config.md#L218-L218](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L218-L218)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](pi-web.detail.md)

Metadata and full claim list: [full detail](pi-web.detail.md)
Human notes ([notes](pi-web.notes.md), never overwritten by build)

[Back to map index](../../index.md)
