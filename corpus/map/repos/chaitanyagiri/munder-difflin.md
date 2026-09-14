# chaitanyagiri/munder-difflin

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 417d8decf08c @ ba331b94f28a7410

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a desktop app that wraps real terminal-agent CLIs as agents, wires them into a hive mind, and puts a clone agent (Michael) in charge of coordination. Supported agent CLIs include Claude Code, Codex, Grok, Kimi, Gemini CLI, Antigravity, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, and Cursor, plus custom commands and local models via Ollama, LM Studio, or vLLM.

## Source coverage

Source coverage (partial): 3 of 29 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a desktop app that wraps real terminal-agent CLIs as agents, wires them into a hive mind, and puts a clone agent (Michael) in charge of coordination. -- evidence: [README.md#L107-L110](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L107-L110)
- components (1 claim(s)):
  - [observation/documented] The app is built with Electron, React, TypeScript, Pixi.js, xterm.js, and node-pty; each agent session runs as a real process in a pseudo-terminal rendered with xterm.js. -- evidence: [README.md#L112-L119](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L112-L119), [README.md#L27-L29](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L27-L29)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: every pull request must include before/after evidence under the PR template's '### Before' and '### After' headings, enforced by an automated 'PR evidence' check; PRs failing it do not merge, with only a maintainer-applied no-visual-change label as exemption. -- evidence: [CONTRIBUTING.md#L95-L98](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L95-L98), [README.md#L392-L397](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L392-L397), [CONTRIBUTING.md#L74-L77](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L74-L77)
  - [observation/documented] Repository development practice: contributors run npm install && npm run dev, keep npm run typecheck green, run npm run test:focused, confirm npm run build works, derive new UI from DESIGN.md tokens, and keep changes scoped to one improvement per PR. -- evidence: [CONTRIBUTING.md#L102-L121](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L102-L121), [README.md#L387-L390](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L387-L390), [CONTRIBUTING.md#L17-L33](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L17-L33)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Supported agent CLIs include Claude Code, Codex, Grok, Kimi, Gemini CLI, Antigravity, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, and Cursor, plus custom commands and local models via Ollama, LM Studio, or vLLM. -- evidence: [README.md#L103-L103](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L103-L103), [README.md#L21-L25](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L21-L25), [README.md#L87-L101](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L87-L101)
  - [observation/documented] The architecture has two data planes — a terminal plane owning PTYs, filesystem and git, and an event plane running the hive, hook server, and router — with the renderer accessing both only through a typed bridge. -- evidence: [README.md#L352-L354](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L352-L354)
- memory-state (2 claim(s)):
  - [observation/documented] The hive is a local git repo of plain files: agents write to their own outbox, a router delivers to recipients' inboxes, and only the harness touches git (single-committer design to avoid index.lock corruption). -- evidence: [README.md#L140-L149](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L140-L149)
More evidence: [full detail](munder-difflin.detail.md)

Metadata and full claim list: [full detail](munder-difflin.detail.md)
Human notes ([notes](munder-difflin.notes.md), never overwritten by build)

[Back to map index](../../index.md)
