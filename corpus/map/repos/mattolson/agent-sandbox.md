# mattolson/agent-sandbox

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5df0b4bc6c57 @ 4c77988393ee6d90

## Summary (orientation draft, not independently verified)

Selected evidence records: The sandbox restricts filesystem access to the repository directory, enforces egress via a sidecar proxy, and uses an iptables firewall so all outbound traffic must pass through the proxy. agentbox init prompts interactively for project name, agent, mode, and IDE, then generates docker compose and network policy files under .agent-sandbox/ plus a devcontainer.json for devcontainer mode.

## Source coverage

Source coverage (partial): 6 of 165 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The base image includes the GitHub CLI so agents can use gh api for issues and pull requests with a repo-scoped api policy surface while the token stays on the host. -- evidence: [README.md#L183-L183](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L183-L183)
  - [observation/documented] Supported agents include Claude Code, Codex, Gemini, OpenCode, Pi, Factory, Copilot, and Hermes, with support tiers ranging from full support to preview to not-supported per CLI/VS Code/JetBrains surface. -- evidence: [README.md#L38-L45](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L38-L45), [README.md#L27-L36](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L27-L36)
- design-choices (5 claim(s)):
  - [observation/documented] The sandbox restricts filesystem access to the repository directory, enforces egress via a sidecar proxy, and uses an iptables firewall so all outbound traffic must pass through the proxy. -- evidence: [README.md#L8-L15](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L8-L15), [README.md#L163-L164](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L163-L164)
  - [observation/documented] The proxy runs a mitmproxy addon (enforcer.py) that checks HTTPS CONNECT tunnels against the host policy and decrypted requests against scheme, method, path, and query rules, returning 403 for non-matching traffic. -- evidence: [README.md#L170-L170](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L170-L170)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: CONTRIBUTING.md is referenced as covering contribution paths, issue labels, planning requirements, and PR expectations; no contributor workflow details appear in the provided slices themselves. -- evidence: [README.md#L345-L345](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L345-L345)
- skills-patterns (1 claim(s)):
  - [observation/documented] The image ships an 'operating-in-agent-sandbox' skill baked in at /usr/local/share/agent-sandbox/skills/ and symlinked into agent skill-discovery directories at startup, explaining the proxy/firewall model and the read-only effective allowlist at /run/agentbox/policy.yaml. -- evidence: [README.md#L181-L181](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L181-L181), [README.md#L185-L185](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L185-L185)
- interfaces (3 claim(s)):
  - [observation/documented] agentbox init prompts interactively for project name, agent, mode, and IDE, then generates docker compose and network policy files under .agent-sandbox/ plus a devcontainer.json for devcontainer mode. -- evidence: [docs/cli.md#L43-L44](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/cli.md#L43-L44), [README.md#L97-L97](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L97-L97)
  - [observation/documented] Network policy is defined in project files under .agent-sandbox/policy/ with a user layer applied over the base agent policy, per-agent variants like user.agent.<agent>.policy.yaml, and hot-reload of the running proxy on saved changes. -- evidence: [README.md#L259-L259](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L259-L259), [README.md#L197-L197](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L197-L197), [README.md#L189-L189](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L189-L189)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agent-sandbox.detail.md)

Metadata and full claim list: [full detail](agent-sandbox.detail.md)
Human notes ([notes](agent-sandbox.notes.md), never overwritten by build)

[Back to map index](../../index.md)
