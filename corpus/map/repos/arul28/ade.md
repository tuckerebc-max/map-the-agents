# arul28/ade

Status: distilled - Freshness: stale
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6ed7c542ae45 @ 3aeae0a1ce58a285

## Summary (orientation draft, not independently verified)

ADE is a local-first workspace for running multiple AI coding agents across desktop, web, terminal, and iOS clients, all attached to an always-on 'ADE Brain' process. Most evidence is README product description plus contributor instructions in AGENTS.md/CLAUDE.md.

## Source coverage

Source coverage (partial): 3 of 99 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] ADE runs Claude Code, Codex, Cursor, Factory Droid, and OpenCode in one workspace reachable from any machine, the web, or a mobile app, and is described as free. -- evidence: [README.md#L40-L40](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L40-L40)
- components (1 claim(s)):
  - [observation/documented] The repo contains apps/ade-cli (Brain, CLI, and ade code TUI), apps/desktop (Electron), apps/ios (SwiftUI), and apps/web (website and downloads). -- evidence: [README.md#L189-L195](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L189-L195)
- design-choices (1 claim(s)):
  - [observation/documented] ADE is local-first: the Brain is the always-on process owning the project catalog, sync websocket, and authority to run things; project data lives in .ade/ per repo and machine state in ~/.ade. -- evidence: [README.md#L187-L187](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L187-L187)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md defines a five-stage dev loop (/context, /quality, /test, /ship plus utilities) implemented as agent skills under .agents/skills/, with /ship wrapping an autonomous PR-to-merge playbook. -- evidence: [AGENTS.md#L17-L17](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L17-L17), [AGENTS.md#L19-L22](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L19-L22), [AGENTS.md#L12-L15](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L12-L15), [AGENTS.md#L26-L26](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L26-L26)
  - [observation/documented] Repository development practice: validation uses desktop and CLI typecheck/test/build commands, with the large desktop suite sharded and the smallest relevant subset run first. -- evidence: [AGENTS.md#L79-L91](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L79-L91), [README.md#L210-L210](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L210-L210), [AGENTS.md#L138-L141](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L138-L141)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The ade CLI offers subcommands such as desktop, brain status, code, lanes create, prs checks, and actions list, sharing the same binary that runs the Brain. -- evidence: [README.md#L174-L181](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L174-L181), [README.md#L172-L172](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L172-L172)
  - [observation/documented] ade connect links a machine to an ADE account, with flags --status --text, --headless for SSH device flow, and --no-login for local/LAN-only service setup. -- evidence: [README.md#L157-L157](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L157-L157), [README.md#L161-L166](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L161-L166)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Mobile connections prefer LAN, then Tailscale, falling back to ADE's own relay service; without an account, pairing is possible via QR/link, LAN/Tailscale scan, or SSH. -- evidence: [README.md#L151-L151](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L151-L151)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project is licensed AGPL-3.0, while the @ade-dev/sdk and @ade-dev/chat-ui npm packages are MIT and an ADE Runtime Embedding Exception covers shipping the runtime binary. -- evidence: [README.md#L222-L222](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L222-L222), [README.md#L224-L224](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L224-L224)
- limitations (1 claim(s)):
More evidence: [full detail](ade.detail.md)

Metadata and full claim list: [full detail](ade.detail.md)
Human notes ([notes](ade.notes.md), never overwritten by build)

[Back to map index](../../index.md)
