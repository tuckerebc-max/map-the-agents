# nexu-io/looper

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 141510c0967f @ 3ca8b4de5320199a

## Summary (orientation draft, not independently verified)

The evidence documents Looper, a Go daemon (looperd) that orchestrates coding-agent roles against GitHub/Forgejo projects, with layered config loading, hot-reload allowlists, SQLite project authority, webhook/network modes, and credential-isolated bot identities. All claims below are product-runtime statements from the configuration documentation; the CI sandbox-e2e material is retained only as repository development practice. Evidence coverage: 133 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 34 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] looper daemon install places a managed daemon binary at ~/.looper/bin/looperd; daemon start writes a pid file and lifecycle diagnostics under ~/.looper, and the CLI looks up the daemon there before $PATH. -- evidence: [docs/configuration.md#L9-L13](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L9-L13), [docs/configuration.md#L15-L15](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L15-L15)
  - [observation/documented] Webhook support has two delivery modes: gh-forward (default), where Looper runs gh webhook forward per repo and receives deliveries on the daemon route /webhook/forward, and tunnel, where Looper creates per-repo GitHub webhooks and the user supplies a tunnel to 127.0.0.1:<listenPort>. -- evidence: [docs/configuration.md#L47-L48](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L47-L48), [docs/configuration.md#L75-L80](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L75-L80), [docs/configuration.md#L45-L45](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L45-L45)
- design-choices (4 claim(s)):
  - [observation/documented] looperd loads configuration in layers: built-in defaults, config file, environment variables, then CLI flags; later layers override earlier ones, objects merge deeply, arrays are replaced as a whole, and omitted fields keep the previous layer's value. -- evidence: [docs/configuration.md#L84-L84](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L84-L84), [docs/configuration.md#L86-L89](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L86-L89), [docs/configuration.md#L91-L91](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L91-L91)
  - [observation/documented] looperd watches the config file and atomically publishes a candidate only when every changed effective field is hot-safe per an explicit allowlist; invalid or restart-bound-containing candidates are rejected as a whole, leaving the last-known-good snapshot active with diagnostics at /dashboard/config. -- evidence: [docs/configuration.md#L97-L97](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L97-L97), [docs/configuration.md#L95-L95](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L95-L95)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: a separate sandbox-e2e CI workflow runs on main and manual dispatch using a repository variable and secret for a GitHub App, mints an installation token via actions/create-github-app-token, and cleans up temporary issues, PRs, and branches afterward. -- evidence: [docs/configuration.md#L595-L602](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L595-L602), [docs/configuration.md#L574-L582](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L574-L582)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The daemon exposes a dashboard config editor at /dashboard/config and a PATCH /api/v1/config endpoint; every patch must submit the revision of the file generation that produced the published values, and when token auth is unset the endpoint accepts only loopback peer/Host requests and rejects proxy-forwarding headers. -- evidence: [docs/configuration.md#L119-L119](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L119-L119), [docs/configuration.md#L121-L121](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L121-L121)
More evidence: [full detail](looper.detail.md)

Metadata and full claim list: [full detail](looper.detail.md)
Human notes ([notes](looper.notes.md), never overwritten by build)

[Back to map index](../../index.md)
