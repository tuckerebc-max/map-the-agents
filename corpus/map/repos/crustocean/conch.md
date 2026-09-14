# crustocean/conch

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8db9729c56f5 @ 059971ac3aad652e

## Summary (orientation draft, not independently verified)

README-only evidence for Conch, a Crustocean-hosted cloud coding agent powered by Claude that reads GitHub repos, writes patches, and opens PRs. Claims cover product behavior, architecture, security model, and deployment; no code-inspected or evaluation evidence is present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Conch is a cloud coding agent powered by Claude that reads repositories, writes patches, and opens pull requests, steered from Crustocean chat. -- evidence: [README.md#L12-L12](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L12-L12)
- components (1 claim(s)):
  - [observation/documented] The codebase includes index.js for orchestration, lib/ modules for the Anthropic client, tools, repo config, diffs, and a demo workspace, plus workspace/ GitHub helpers. -- evidence: [README.md#L118-L132](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L118-L132)
- design-choices (2 claim(s)):
  - [observation/documented] Staged writes are held in an in-memory Map and only reach GitHub when commit() runs during PR creation, making changes ephemeral per run. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142)
  - [observation/documented] Commits are made atomically via the Git Data API (blobs, tree, commit, ref update), avoiding merge conflicts from concurrent contents API calls. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves creating the agent via /agency and /boot commands, copying .env.example to .env with API URL, agent token, and Anthropic key, then npm install and npm start. -- evidence: [README.md#L39-L43](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L39-L43), [README.md#L55-L59](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L55-L59), [README.md#L49-L51](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L49-L51), [README.md#L63-L66](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L63-L66)
  - [observation/documented] Repository development practice: the private @crustocean/sdk can be made available via npm link, a file: workspace reference in package.json, or publishing to a private registry. -- evidence: [README.md#L159-L159](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L159-L159), [README.md#L169-L175](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L169-L175), [README.md#L161-L167](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L161-L167), [README.md#L177-L178](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L177-L178)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent can read and explore files, search code, write targeted patches, create and manage pull requests (merge, comment, inspect checks), and delete merged feature branches. -- evidence: [README.md#L18-L23](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L18-L23)
- interfaces (2 claim(s)):
  - [observation/documented] Chat commands include !conch connect owner/repo, disconnect, status, and help; users can also @mention Conch with coding tasks. -- evidence: [README.md#L86-L86](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L86-L86), [README.md#L97-L102](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L97-L102)
  - [observation/documented] Runs surface in the Crustocean UI as an Agent Run with tool cards, status updates, permission gates, streaming responses, and a collapsible run timeline. -- evidence: [README.md#L25-L25](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L25-L25), [README.md#L110-L114](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L110-L114)
- memory-state (1 claim(s)):
  - [observation/documented] Per-agency repository configuration stores the repo slug in notes and the GitHub token in agent config, with tokens stored encrypted via the Crustocean API. -- evidence: [README.md#L118-L132](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L118-L132), [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155)
- orchestration (1 claim(s)):
  - [observation/documented] Conch is a stateless worker with no database, filesystem, or ports, connecting to Crustocean via WebSocket and GitHub via REST; deployable via Railway, Docker, or any Node.js host. -- evidence: [README.md#L184-L188](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L184-L188), [README.md#L199-L202](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L199-L202), [README.md#L192-L195](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L192-L195), [README.md#L204-L204](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L204-L204)
- tools-permissions (3 claim(s)):
More evidence: [full detail](conch.detail.md)

Metadata and full claim list: [full detail](conch.detail.md)
Human notes ([notes](conch.notes.md), never overwritten by build)

[Back to map index](../../index.md)
