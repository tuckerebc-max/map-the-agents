# mereyabdenbekuly-ctrl/clodex-ide

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dc023d1f6fea @ 0b38f45985df361f

## Summary (orientation draft, not independently verified)

README and developer docs describe CLODEx, an AGPL-3.0 local-first agentic IDE derived from Stagewise, with an Electron multi-process architecture, durable tasks, MCP/model integrations, and approval-gated tool execution; contributor-facing setup, review, and governance guidance is also documented. Evidence coverage: 124 of 129 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 151 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] CLODEx is an open-source, local-first agentic IDE for long-running engineering work that keeps code, Git, terminal, browser, models, and MCP tools in one durable desktop workspace. -- evidence: [README.md#L17-L20](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L17-L20)
  - [observation/documented] The project is licensed under GNU Affero General Public License v3.0, with third-party components keeping their original licenses and notices. -- evidence: [README.md#L366-L368](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L366-L368)
- components (2 claim(s)):
  - [observation/documented] The application is an Electron app split into isolated runtime lanes including main, renderer, agent host, MCP host, sandbox worker, and a headless CLI host, each with documented source paths. -- evidence: [docs/developer/architecture.md#L5-L5](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L5-L5), [docs/developer/architecture.md#L7-L16](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L7-L16)
  - [observation/documented] The main process composes backend service groups such as task, file-tree, terminal, Git, diff, credentials, model providers, MCP, skills, plugins, network policy, and telemetry services. -- evidence: [docs/developer/architecture.md#L23-L24](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L23-L24), [docs/developer/architecture.md#L26-L37](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L26-L37)
- design-choices (2 claim(s)):
  - [observation/documented] The stated product principle is that model output is input, not authority; sensitive operations can require explicit approval and remain reviewable. -- evidence: [README.md#L68-L74](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L68-L74), [README.md#L78-L78](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L78-L78)
  - [observation/documented] Utility-process crashes reject in-flight work, apply bounded restart policies, and do not replay side effects, with the main process owning supervision. -- evidence: [docs/developer/architecture.md#L18-L19](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L18-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: before opening a pull request, contributors run pnpm check, typecheck, test, and security:secrets, and commits must be DCO-signed with focused tests for changed behavior. -- evidence: [README.md#L285-L290](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L285-L290), [README.md#L283-L283](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L283-L283), [README.md#L341-L345](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L341-L345)
  - [observation/documented] Repository development practice: local setup involves cloning, enabling corepack pnpm 10.30.3, copying .env.example to .env and .env.dev, then building packages and starting apps/browser, never committing .env files or credentials. -- evidence: [README.md#L277-L279](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L277-L279), [README.md#L265-L268](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L265-L268), [README.md#L262-L263](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L262-L263), [README.md#L255-L257](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L255-L257)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Communication contracts include Karton for typed browser state and procedures, an Agent Host protocol, an MCP runtime normalizing stdio/HTTP/OAuth, runner contracts, and an Artifact Bridge with principal-scoped sessions and two-phase privileged writes. -- evidence: [docs/developer/architecture.md#L91-L98](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L91-L98)
  - [observation/documented] CLODEx.xyz sign-in uses the system browser with an RFC 8252 loopback callback, state, and PKCE S256, and bearer tokens are not returned in the callback URL. -- evidence: [README.md#L87-L96](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L87-L96), [README.md#L209-L226](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L209-L226)
More evidence: [full detail](clodex-ide.detail.md)

Metadata and full claim list: [full detail](clodex-ide.detail.md)
Human notes ([notes](clodex-ide.notes.md), never overwritten by build)

[Back to map index](../../index.md)
