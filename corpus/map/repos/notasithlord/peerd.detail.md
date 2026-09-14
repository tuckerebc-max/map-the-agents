# notasithlord/peerd -- full detail

[Back to orientation](peerd.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/notasithlord/peerd/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/c54f3ca7139dac7c.json](../../../wiki/dossiers/notasithlord/peerd/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/c54f3ca7139dac7c.json)

## specifications (1 claim(s))

- [observation/documented] peerd is described as a general-purpose agent runtime built on browser primitives (Workers, origins, sandboxing, OPFS, WASM/WASI, WebRTC, WebAuthn, WebExtensions) that runs inside Chrome and Firefox. -- evidence: [README.md#L24-L24](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L24-L24) (`clm_b0e0b7e93437fe7741ab03b85ed11bba215278617b02b76b74ea6b49c13ec04b`)

## components (1 claim(s))

- [observation/documented] The extension has five main modules, each exposing its public API via index.js: peerd-provider (model adapters), peerd-egress (vault, network policy, denylist, audit), peerd-engine (WebVM/Notebook/App/headless execution), peerd-runtime (agent loop, actors, tools, sessions, memory, permissions), and peerd-distributed (preview-only P2P). -- evidence: [README.md#L151-L157](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L151-L157), [README.md#L148-L149](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L148-L149) (`clm_7ffb39d9dd53d3709f9ddb054d15da4cc24521bcb49841076596aff7ecbb9ea6`)

## design-choices (1 claim(s))

- [observation/documented] The source extension is vanilla JavaScript with ES modules running directly when loaded unpacked, with no development bundler or transpiler; release packaging with Bun minifies only a disposable staging copy and preserves module boundaries and vendored bytes. -- evidence: [README.md#L166-L172](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L166-L172) (`clm_911ac392ddb6c1f71ea69f84caed15ac36739f8f5b786f40565c75f572a8bb36`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: development uses Bun commands (bun install, gen:dev, test, typecheck, lint, e2e:verify, preflight) across three test surfaces (Bun unit tests, in-browser Chrome/Gecko tests, live Chrome E2E), plus a red-team suite; generated files like extension/manifest.json must not be hand-edited and CI checks them for drift. -- evidence: [README.md#L213-L215](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L213-L215), [README.md#L174-L183](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L174-L183), [README.md#L187-L193](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L187-L193), [README.md#L195-L198](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L195-L198) (`clm_6199c440af142e87948f652ed539e828ec4ee6ef42b59e5d5ae9f8a003ae860a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Apps integrate via window.peerd APIs: agent.open() reveals a trusted drawer only during real user activation, agent.expose() declares observe/act semantic adapters, and peerd.data provides bounded JSON persistence (1 MB per write) mapped to data/<key>.json in the App's working tree. -- evidence: [docs/APP-ACTORS.md#L120-L125](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L120-L125), [docs/APP-ACTORS.md#L113-L118](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L113-L118), [docs/APP-ACTORS.md#L16-L18](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L16-L18), [docs/APP-ACTORS.md#L20-L24](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L20-L24), [docs/APP-ACTORS.md#L81-L109](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L81-L109) (`clm_493a5940a94099b8603b9a0fef44d07ade0064dd0ce5b00f2f566449ab05e48f`)
- [observation/documented] App manifests use peerd.json with fields like kind, entry, agent (kind bound-app, profile, surface, name, instructions, runtime), and capabilities; a conforming Git repository places peerd.json and its entry file at the root. -- evidence: [docs/APP-ACTORS.md#L151-L154](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L151-L154), [docs/APP-ACTORS.md#L61-L76](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L61-L76) (`clm_2d5ed33ed3326fa1f189374f1712af495251c40c0e4a91394e3be81d744ba76c`)

## memory-state (1 claim(s))

- [observation/documented] Sessions, memory, skills, goals, review, and checkpoints live in the extension; a local vault holds secrets and protected security records, with passphrase unlock always available and passkey unlock dependent on WebAuthn PRF support. -- evidence: [README.md#L142-L144](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L142-L144), [README.md#L135-L140](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L135-L140), [README.md#L38-L54](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L38-L54) (`clm_804ed06809a60749efeded84ac6a12179a8bf6c2a03d12e4c41016c38d8f8492`)

## orchestration (1 claim(s))

- [observation/documented] The main agent delegates page and compute-environment work to separate keyless actors whose tools are scoped to that environment; non-orchestrator agent loops run in dedicated worker heaps, and requests fail if the browser cannot prove that boundary. -- evidence: [README.md#L87-L91](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L87-L91), [README.md#L38-L54](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L38-L54) (`clm_daf7653b96fb12bd81fdb2e05601b573c5f9449df6538c91823d10b66c9978e0`)

## tools-permissions (1 claim(s))

- [observation/documented] Credentials, network rules, confirmations, and audit stay with the extension; egress controls include refusal of private-network/cloud-metadata targets, denylist checks, and redirect blocking, with per-operation scoped network policies. -- evidence: [README.md#L62-L65](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L62-L65), [README.md#L93-L97](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L93-L97), [docs/security/ARC-TESTING.md#L51-L60](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/security/ARC-TESTING.md#L51-L60) (`clm_47bd4b11d4833074141f3c11470f7d7ee0fefd90aa9243b3c9b4b295b36dedbb`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The shipped extension has no npm runtime dependencies; third-party runtime code is vendored under extension/vendor/ with SOURCE.txt provenance files and SHA-256 pinning in vendor.lock.json, verified by bun run check:vendor. -- evidence: [README.md#L233-L240](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L233-L240) (`clm_9d436bff6373fd6860f6912f796530a39ac58b9820ec5f48b44e647f25d866eb`)

## limitations (2 claim(s))

- [observation/documented] On Firefox, WebVM cannot boot from an extension page, threaded WebAssembly is unavailable, the Pod 'js' command is refused, Apps are disabled pending Firefox 154 adoption, offscreen-hosted tools are absent or degraded, and CDP-only automation features fall back to chrome.scripting. -- evidence: [docs/BROWSER-COMPATIBILITY.md#L87-L100](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L87-L100), [docs/BROWSER-COMPATIBILITY.md#L34-L48](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L34-L48), [docs/BROWSER-COMPATIBILITY.md#L73-L83](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L73-L83), [docs/BROWSER-COMPATIBILITY.md#L54-L69](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L54-L69), [docs/BROWSER-COMPATIBILITY.md#L104-L118](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L104-L118), [docs/BROWSER-COMPATIBILITY.md#L18-L24](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/BROWSER-COMPATIBILITY.md#L18-L24) (`clm_49c4ba9d289e2de2df1495b5d9705982d3b48fdc34cbca22dd730db9c4c20f70`)
- [observation/documented] Documented residual egress limits: Chrome DNR does not intercept worker-created WebSockets, private-network classification is lexical (no DNS resolution, so DNS rebinding is outside the check), and query strings/fragments are not a complete DLP boundary. -- evidence: [docs/security/ARC-TESTING.md#L51-L60](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/security/ARC-TESTING.md#L51-L60), [docs/security/ARC-TESTING.md#L81-L91](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/security/ARC-TESTING.md#L81-L91), [docs/security/ARC-TESTING.md#L62-L64](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/security/ARC-TESTING.md#L62-L64), [docs/security/ARC-TESTING.md#L66-L68](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/security/ARC-TESTING.md#L66-L68) (`clm_402c631786821379e914a8231aadfd4c38c1200a4aa4fc1c09a17bf031dacaf9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

