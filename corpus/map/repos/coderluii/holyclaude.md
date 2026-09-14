# coderluii/holyclaude

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 651c48fc01a9 @ ec0da588070ffb78

## Summary (orientation draft, not independently verified)

Selected evidence records: The container runs the official Anthropic Claude Code CLI (not a wrapper or proxy), served through a CloudCLI web UI on port 3001, with s6-overlay as PID 1 supervising Xvfb on :99 and optional sshd. The image bundles Chromium with Xvfb and Playwright for headless browser screenshots and testing, plus database clients (psql, redis-cli, sqlite3, MariaDB-based mysql) and GitHub CLI.

## Source coverage

Source coverage (partial): 5 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The container runs the official Anthropic Claude Code CLI (not a wrapper or proxy), served through a CloudCLI web UI on port 3001, with s6-overlay as PID 1 supervising Xvfb on :99 and optional sshd. -- evidence: [README.md#L58-L58](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L58-L58), [README.md#L765-L778](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L765-L778), [README.md#L195-L195](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L195-L195)
  - [observation/documented] The image bundles Chromium with Xvfb and Playwright for headless browser screenshots and testing, plus database clients (psql, redis-cli, sqlite3, MariaDB-based mysql) and GitHub CLI. -- evidence: [README.md#L765-L778](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L765-L778), [README.md#L592-L606](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L592-L606)
- design-choices (3 claim(s)):
  - [observation/documented] The compose templates set shm_size 2g because Chromium heavily uses /dev/shm and Docker's 64MB default causes tab crashes, and grant SYS_ADMIN, SYS_PTRACE, and seccomp=unconfined as the retained browser profile, with hardening described as a separate change. -- evidence: [README.md#L272-L301](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L272-L301), [README.md#L313-L313](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L313-L313), [README.md#L315-L315](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L315-L315)
  - [observation/documented] The web UI port is bound to 127.0.0.1 by default, and users needing remote access are directed to Tailscale or Cloudflare Tunnel rather than port forwarding. -- evidence: [README.md#L272-L301](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L272-L301), [README.md#L141-L141](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L141-L141), [README.md#L313-L313](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L313-L313)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: release-sensitive facts are published in contracts/product-facts.json, and the release workflow checks that contract against the Dockerfile and Compose files before building images. -- evidence: [README.md#L46-L46](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L46-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Authentication is done through the CloudCLI web UI: Claude Max/Pro users sign in via OAuth and API-key users paste their key; the container relays no credentials, with tools reading them from container files, bind mounts, or environment variables. -- evidence: [README.md#L60-L63](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L60-L63), [README.md#L65-L65](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L65-L65), [README.md#L199-L202](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L199-L202), [README.md#L224-L224](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L224-L224)
  - [observation/documented] The quick-start workflow is: create a docker-compose.yaml from a provided template, run docker compose up -d, then open http://localhost:3001 and create a CloudCLI account; no .env file is required. -- evidence: [README.md#L121-L123](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L121-L123), [README.md#L137-L137](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L137-L137), [README.md#L127-L129](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L127-L129), [README.md#L133-L135](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L133-L135), [README.md#L139-L139](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L139-L139)
- memory-state (1 claim(s)):
More evidence: [full detail](holyclaude.detail.md)

Metadata and full claim list: [full detail](holyclaude.detail.md)
Human notes ([notes](holyclaude.notes.md), never overwritten by build)

[Back to map index](../../index.md)
