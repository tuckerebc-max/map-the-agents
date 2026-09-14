# mereyabdenbekuly-ctrl/clodex-ide -- full detail

[Back to orientation](clodex-ide.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mereyabdenbekuly-ctrl/clodex-ide/dc023d1f6fea166a23243dff7cf4e2dc824c035b/0b38f45985df361f.json](../../../wiki/dossiers/mereyabdenbekuly-ctrl/clodex-ide/dc023d1f6fea166a23243dff7cf4e2dc824c035b/0b38f45985df361f.json)

## specifications (2 claim(s))

- [observation/documented] CLODEx is an open-source, local-first agentic IDE for long-running engineering work that keeps code, Git, terminal, browser, models, and MCP tools in one durable desktop workspace. -- evidence: [README.md#L17-L20](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L17-L20) (`clm_876e99da5d5d2bf4d32c96adbaabfd78b0a33d987d6cf49d239801ccca143b63`)
- [observation/documented] The project is licensed under GNU Affero General Public License v3.0, with third-party components keeping their original licenses and notices. -- evidence: [README.md#L366-L368](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L366-L368) (`clm_6bc19c26e746317f4a238a0bbdb481969d549899f3d381e9ce6f513852ce9453`)

## components (2 claim(s))

- [observation/documented] The application is an Electron app split into isolated runtime lanes including main, renderer, agent host, MCP host, sandbox worker, and a headless CLI host, each with documented source paths. -- evidence: [docs/developer/architecture.md#L5-L5](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L5-L5), [docs/developer/architecture.md#L7-L16](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L7-L16) (`clm_226cec2acb27c79a2c00c6b04d314b3071e58a90b501809865ccfa5cdb3d418a`)
- [observation/documented] The main process composes backend service groups such as task, file-tree, terminal, Git, diff, credentials, model providers, MCP, skills, plugins, network policy, and telemetry services. -- evidence: [docs/developer/architecture.md#L23-L24](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L23-L24), [docs/developer/architecture.md#L26-L37](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L26-L37) (`clm_5ac382a6e2aa2ff252643d7e68c1533b38961fc9d909b67d46913bd2923d696b`)

## design-choices (2 claim(s))

- [observation/documented] The stated product principle is that model output is input, not authority; sensitive operations can require explicit approval and remain reviewable. -- evidence: [README.md#L68-L74](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L68-L74), [README.md#L78-L78](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L78-L78) (`clm_87c09092df9f604100710dbd86db38a21217a182997f98e206cc284b578ea48b`)
- [observation/documented] Utility-process crashes reject in-flight work, apply bounded restart policies, and do not replay side effects, with the main process owning supervision. -- evidence: [docs/developer/architecture.md#L18-L19](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L18-L19) (`clm_2cbd53cdbeb29c7344d0475b65510bf224de84d40ecbd488857fe59d45f83b37`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: before opening a pull request, contributors run pnpm check, typecheck, test, and security:secrets, and commits must be DCO-signed with focused tests for changed behavior. -- evidence: [README.md#L285-L290](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L285-L290), [README.md#L283-L283](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L283-L283), [README.md#L341-L345](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L341-L345) (`clm_c8027d7cc54be23e63d3851f161a1a5e1516ceea039ca9ed22d0ff27e7578ac0`)
- [observation/documented] Repository development practice: local setup involves cloning, enabling corepack pnpm 10.30.3, copying .env.example to .env and .env.dev, then building packages and starting apps/browser, never committing .env files or credentials. -- evidence: [README.md#L277-L279](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L277-L279), [README.md#L265-L268](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L265-L268), [README.md#L262-L263](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L262-L263), [README.md#L255-L257](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L255-L257) (`clm_346d9420e567e8df9696228e6c03cd42180b33b0f7400e81d7b8ffb2d79888b5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Communication contracts include Karton for typed browser state and procedures, an Agent Host protocol, an MCP runtime normalizing stdio/HTTP/OAuth, runner contracts, and an Artifact Bridge with principal-scoped sessions and two-phase privileged writes. -- evidence: [docs/developer/architecture.md#L91-L98](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L91-L98) (`clm_5bae3851a4151b76a2451f2fce10a7ecedd2eee4e4a1e88a9397000d4cb32729`)
- [observation/documented] CLODEx.xyz sign-in uses the system browser with an RFC 8252 loopback callback, state, and PKCE S256, and bearer tokens are not returned in the callback URL. -- evidence: [README.md#L87-L96](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L87-L96), [README.md#L209-L226](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L209-L226) (`clm_87aed4c8803b90ee8a6ac432a2467a45d5f486b7340f891867a783f53e909054`)

## memory-state (1 claim(s))

- [observation/documented] The product offers searchable task history, workspace-aware context, restart recovery, and continued work across sessions, with session continuity and workspace snapshot services listed in the architecture. -- evidence: [README.md#L87-L96](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L87-L96), [docs/developer/architecture.md#L26-L37](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L26-L37) (`clm_e5c32bb22106681f850eeaf27cd60a2bac5714c6fdecefd4385eb2ff4451a6df`)

## orchestration (1 claim(s))

- [observation/documented] Agent turns run in an isolated Agent Host outside the main process: the Agent Core resolves goal, workspace, memory, and prompt, selects a model, and streams events back through the main process to the UI. -- evidence: [docs/developer/architecture.md#L41-L49](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L41-L49), [docs/developer/architecture.md#L51-L68](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L51-L68) (`clm_6a0282749fda3cf2336879deab8f2c22bec9957ef06cf320c47649291cc71636`)

## tools-permissions (1 claim(s))

- [observation/documented] Requested side effects are assessed by a policy component that either grants capability-bound approval for tool execution or denies/escalates; extension runtimes receive explicit capabilities rather than arbitrary host access. -- evidence: [docs/developer/architecture.md#L86-L87](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L86-L87), [docs/developer/architecture.md#L51-L68](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/docs/developer/architecture.md#L51-L68) (`clm_87fa17da62037bef5f17293e6f21b3713d68c88b4a3464da6a18ab1f99394347`)

## evaluation (1 claim(s))

- [inference/documented] No evidence in the provided slices describes an agent or task performance evaluation harness or benchmark results; the release evidence described covers packaging, checksums, and byte audits rather than agent behavior scoring. -- evidence: [README.md#L161-L167](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L161-L167), [README.md#L132-L138](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L132-L138) (`clm_da57e40349fef1459d3346dc5f01fa6800175665a24cdad0f9e952324a7f6cde`)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Node.js 22.23.1, pnpm 10.30.3, and Git, with pnpm activated via corepack and a frozen-lockfile install. -- evidence: [README.md#L259-L260](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L259-L260), [README.md#L248-L251](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L248-L251), [README.md#L265-L268](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L265-L268) (`clm_8311affde9b017729b618aabc6c510f0567c0cb2aefd5cd7a35fc7af50aac55b`)

## limitations (1 claim(s))

- [observation/documented] The Community Observed 21 preview packages are unsigned or ad-hoc signed, not notarized, lack Authenticode on Windows and vendor signatures on Linux, so users are told to verify SHA-256 and keep OS protections enabled. -- evidence: [README.md#L169-L174](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L169-L174) (`clm_3e581500b5fb5d192bc065b594c5679b8a601c00b0de667063969c450efbccfd`)

## relevance (1 claim(s))

- [observation/documented] CLODEx began as a modified version of the Stagewise codebase, diverging at upstream commit ef9d249f, and documents lineage, attribution obligations, and a reproducible diff against the upstream base. -- evidence: [CLODEX_VS_UPSTREAM.md#L44-L51](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/CLODEX_VS_UPSTREAM.md#L44-L51), [README.md#L326-L329](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/README.md#L326-L329), [CLODEX_VS_UPSTREAM.md#L15-L20](https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/dc023d1f6fea166a23243dff7cf4e2dc824c035b/CLODEX_VS_UPSTREAM.md#L15-L20) (`clm_91bdf3e14711c46a408005acb36dc4e4b9f6b695ad628d385fa74b12c5798d40`)

