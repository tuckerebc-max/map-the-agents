# saadnvd1/agent-os

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 378069fed637 @ 82000dd2a4b2ad99

## Summary (orientation draft, not independently verified)

AgentOS is a mobile-first web UI for managing AI coding sessions, installable via npm or a curl script, with a CLI, desktop wrapper builds, multi-agent support, and a documented iOS Safari WebSocket reconnection fix. A roadmap file lists many features as unchecked ideas.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The product supports multiple AI coding agents with a capability matrix: only Claude Code and Kilo Code support resume and fork, and each agent has a distinct auto-approve mechanism (flags or config files). -- evidence: [README.md#L66-L77](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L66-L77)
  - [observation/documented] Documented features include voice-to-text prompting, up to four side-by-side session panes, code search, file picker with mobile upload, GitHub cloning, git integration, git worktrees, dev server control, and conductor/worker session orchestration via MCP. -- evidence: [README.md#L81-L90](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L81-L90)
- design-choices (1 claim(s)):
  - [observation/documented] The desktop app is a native wrapper around the web UI; the backend server must still be installed and run separately, with the wrapper only providing a native window instead of a browser. -- evidence: [README.md#L44-L44](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L44-L44)
- workflows (2 claim(s)):
  - [observation/documented] Installation paths: global npm install followed by 'agent-os install' and 'agent-os start' (recommended when Node.js 20+ exists), a curl-piped install script for fresh machines without Node.js, or manual git clone with npm install and npm run dev. -- evidence: [README.md#L19-L19](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L19-L19), [README.md#L22-L22](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L22-L22), [README.md#L30-L30](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L30-L30), [README.md#L32-L35](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L32-L35), [README.md#L15-L15](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L15-L15), [README.md#L25-L26](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L25-L26), [README.md#L50-L55](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L50-L55)
  - [observation/documented] Mobile access is documented via Tailscale: install on machine and phone, sign in with the same account, then reach the server at its 100.x.x.x address on port 3011. -- evidence: [README.md#L105-L105](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L105-L105), [README.md#L107-L109](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L107-L109)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] AgentOS provides a mobile-first web UI for managing AI coding sessions, served on port 3011 in the manual dev setup. -- evidence: [README.md#L3-L3](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L3-L3), [README.md#L50-L55](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L50-L55)
  - [observation/documented] The CLI offers run, start, stop, status, logs, and update commands for controlling the server. -- evidence: [README.md#L94-L101](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L94-L101)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Prerequisites are Node.js 20+, tmux, and ripgrep (auto-installed by the installer script per the README), plus at least one supported AI CLI such as Claude Code, Codex, Gemini CLI, Aider, or Cursor CLI. -- evidence: [README.md#L59-L62](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L59-L62)
More evidence: [full detail](agent-os.detail.md)

Metadata and full claim list: [full detail](agent-os.detail.md)
Human notes ([notes](agent-os.notes.md), never overwritten by build)

[Back to map index](../../index.md)
