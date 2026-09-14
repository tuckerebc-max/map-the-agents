---
access: public
aliases: []
claim_ids:
- clm_47bd4b11d4833074141f3c11470f7d7ee0fefd90aa9243b3c9b4b295b36dedbb
- clm_6199c440af142e87948f652ed539e828ec4ee6ef42b59e5d5ae9f8a003ae860a
- clm_7ffb39d9dd53d3709f9ddb054d15da4cc24521bcb49841076596aff7ecbb9ea6
- clm_804ed06809a60749efeded84ac6a12179a8bf6c2a03d12e4c41016c38d8f8492
- clm_911ac392ddb6c1f71ea69f84caed15ac36739f8f5b786f40565c75f572a8bb36
- clm_9d436bff6373fd6860f6912f796530a39ac58b9820ec5f48b44e647f25d866eb
- clm_b0e0b7e93437fe7741ab03b85ed11bba215278617b02b76b74ea6b49c13ec04b
- clm_daf7653b96fb12bd81fdb2e05601b573c5f9449df6538c91823d10b66c9978e0
maturity: draft
page_id: pg_ae8456091ded510686d2e1b00dfdfccd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fff4f1b8fce156b9ae5b28baa4870253
title: NotASithLord/peerd/README.md @ 12d1a54976bc
updated_at: '2026-09-14T02:23:22Z'
---

# NotASithLord/peerd/README.md @ 12d1a54976bc

<!-- rcw:begin owner=source:src_fff4f1b8fce156b9ae5b28baa4870253 block=evidence -->
- Credentials, network rules, confirmations, and audit stay with the extension; egress controls include refusal of private-network/cloud-metadata targets, denylist checks, and redirect blocking, with per-operation scoped network policies. [@claim:clm_47bd4b11d4833074141f3c11470f7d7ee0fefd90aa9243b3c9b4b295b36dedbb]
- Repository development practice: development uses Bun commands (bun install, gen:dev, test, typecheck, lint, e2e:verify, preflight) across three test surfaces (Bun unit tests, in-browser Chrome/Gecko tests, live Chrome E2E), plus a red-team suite; generated files like extension/manifest.json must not be hand-edited and CI checks them for drift. [@claim:clm_6199c440af142e87948f652ed539e828ec4ee6ef42b59e5d5ae9f8a003ae860a]
- The extension has five main modules, each exposing its public API via index.js: peerd-provider (model adapters), peerd-egress (vault, network policy, denylist, audit), peerd-engine (WebVM/Notebook/App/headless execution), peerd-runtime (agent loop, actors, tools, sessions, memory, permissions), and peerd-distributed (preview-only P2P). [@claim:clm_7ffb39d9dd53d3709f9ddb054d15da4cc24521bcb49841076596aff7ecbb9ea6]
- Sessions, memory, skills, goals, review, and checkpoints live in the extension; a local vault holds secrets and protected security records, with passphrase unlock always available and passkey unlock dependent on WebAuthn PRF support. [@claim:clm_804ed06809a60749efeded84ac6a12179a8bf6c2a03d12e4c41016c38d8f8492]
- The source extension is vanilla JavaScript with ES modules running directly when loaded unpacked, with no development bundler or transpiler; release packaging with Bun minifies only a disposable staging copy and preserves module boundaries and vendored bytes. [@claim:clm_911ac392ddb6c1f71ea69f84caed15ac36739f8f5b786f40565c75f572a8bb36]
- The shipped extension has no npm runtime dependencies; third-party runtime code is vendored under extension/vendor/ with SOURCE.txt provenance files and SHA-256 pinning in vendor.lock.json, verified by bun run check:vendor. [@claim:clm_9d436bff6373fd6860f6912f796530a39ac58b9820ec5f48b44e647f25d866eb]
- peerd is described as a general-purpose agent runtime built on browser primitives (Workers, origins, sandboxing, OPFS, WASM/WASI, WebRTC, WebAuthn, WebExtensions) that runs inside Chrome and Firefox. [@claim:clm_b0e0b7e93437fe7741ab03b85ed11bba215278617b02b76b74ea6b49c13ec04b]
- The main agent delegates page and compute-environment work to separate keyless actors whose tools are scoped to that environment; non-orchestrator agent loops run in dedicated worker heaps, and requests fail if the browser cannot prove that boundary. [@claim:clm_daf7653b96fb12bd81fdb2e05601b573c5f9449df6538c91823d10b66c9978e0]
<!-- rcw:end owner=source:src_fff4f1b8fce156b9ae5b28baa4870253 block=evidence -->

## Researcher notes

