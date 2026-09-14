# get-bb/bb -- full detail

[Back to orientation](bb.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/get-bb/bb/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/3b3429692f6052ea.json](../../../wiki/dossiers/get-bb/bb/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/3b3429692f6052ea.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Production runs send anonymous usage telemetry (app starts, thread and message counts, plugin installs) with a random per-install id; development/source runs never send, and BB_TELEMETRY=false opts out. -- evidence: [README.md#L85-L93](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L85-L93) (`clm_c796ccadbdf74a94eb73d209964406eaa036cfa09c8d7c645e7f4dcd2a0231f5`)

## design-choices (1 claim(s))

- [observation/documented] bb is described as an agentic IDE that builds itself, able to control, customize, and automate itself as groundwork for a user's own software factory. -- evidence: [README.md#L14-L15](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L14-L15) (`clm_03149061ce175b954a765eb9812c93a1b2e5332d72c5d6378b1ea13e207898a3`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: the dev loop uses pnpm dev (Vite with proxied API/WebSocket traffic and per-checkout data dirs under ~/.bb-dev) and pnpm start:worktree to test the production bundle without switching to production data or ports. -- evidence: [README.md#L103-L109](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L103-L109), [README.md#L99-L101](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L99-L101), [README.md#L114-L116](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L114-L116), [README.md#L111-L112](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L111-L112) (`clm_38afb1a3663c2af1fb36780d1d2b0dbd8bae3f103a8560031a803831a71d975d`)
- [observation/documented] Repository development practice: releases ship two outputs from one commit — the bb-app npm package via publish-bb-app.yml and the desktop app via build-desktop.yml — and a release is not complete until both are published at the same locked version. -- evidence: [docs/bb-release-process.md#L11-L16](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L11-L16) (`clm_103d011baae5db64a94b7b50507d05f4a067940e79a9bf4f4d3406c85e4a6f4a`)
- [observation/documented] Repository development practice: a scheduled nightly channel publishes a next-patch prerelease under the npm nightly dist-tag and builds a separately installable bb Nightly desktop app without moving stable latest pointers. -- evidence: [docs/bb-release-process.md#L18-L27](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L18-L27) (`clm_4bb392bbb4b23f7bc77e611db1f4644ccebdedefaf8a626b4681d5e7963e0e33`)
- [observation/documented] Repository development practice: release validation includes a version-lockstep check, turbo typecheck/test for several packages, a bb-app tarball smoke task, and git diff --check before committing. -- evidence: [docs/bb-release-process.md#L126-L131](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L126-L131) (`clm_0ce995e32acc8707441989253083228a0e6804525be143f00ccfd61e41940faa`)
- [observation/documented] Repository development practice: the @get-bb/plugin-sdk publishes via an idempotent publish-if-missing job, with a CI guard that fails when a published version's packed tarball differs from the local build. -- evidence: [docs/bb-release-process.md#L276-L280](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L276-L280), [docs/bb-release-process.md#L282-L284](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L282-L284), [docs/bb-release-process.md#L286-L291](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L286-L291) (`clm_2feef4ac65a69fb17b4b15e74bfd8f66a92a9cd63ba15a62920c425e80f29cb5`)
- [observation/documented] Repository development practice: the React Compiler transform cache stores validated {code, map} results via npm cacache under <git-common-dir>/bb-cache/react-compiler, keyed on code, module identity, and a broad toolchain/environment namespace; diagnostics bypass the cache. -- evidence: [docs/build-performance.md#L3-L10](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/build-performance.md#L3-L10), [docs/build-performance.md#L22-L30](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/build-performance.md#L22-L30), [docs/build-performance.md#L12-L20](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/build-performance.md#L12-L20), [docs/build-performance.md#L32-L36](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/build-performance.md#L32-L36) (`clm_a6275a48eb0609e85c95abf4f965a2d8d57b3ca73827cec28fee0b31c0741a92`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes a desktop app, web app, CLI, and HTTP API as first-class ways to drive bb, with work running in threads that can be followed live, steered, or handed off to another agent. -- evidence: [README.md#L17-L19](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L17-L19) (`clm_25213cc62ea367d2396d161c7ddace8d5ba299472b47b72c86d52a60a1b957c0`)
- [observation/documented] Running via npx serves a web interface at http://localhost:38886. -- evidence: [README.md#L55-L55](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L55-L55), [README.md#L51-L53](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L51-L53) (`clm_0efd7845d3ff01d2d002f9ba0bccebe9aa818fd937bbb508953280bad32cbdea`)
- [observation/documented] A CLI subcommand interface exists for settings: bb-app config supports set, list, unset, and refresh for non-secret settings such as BB_APP_URL and BB_INFERENCE. -- evidence: [docs/configuration.md#L7-L7](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/configuration.md#L7-L7), [docs/configuration.md#L9-L17](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/configuration.md#L9-L17) (`clm_0069f425b760045938f15d1bd884089da26fac43794f1578984d35a4eb24bca5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] bb depends on native add-ons including better-sqlite3, node-pty, and @parcel/watcher built by npm install scripts; npm 12+ blocks those scripts by default, requiring --allow-scripts. -- evidence: [README.md#L63-L65](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L63-L65), [README.md#L244-L247](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L244-L247), [README.md#L67-L69](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L67-L69) (`clm_1b8d88c5987103a1b8a0c523e15d638f6e28e88fc4257a568db691572b353ff6`)

## limitations (3 claim(s))

- [observation/documented] The desktop app supports macOS on Apple Silicon; the Linux x64 AppImage is alpha, Intel Mac users should use npx, and native Windows PowerShell/CMD are unsupported (WSL2 instead). -- evidence: [README.md#L37-L42](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L37-L42) (`clm_f6ff59583867d01f506c74b13ea330fdcb4e4e847eb392d734433507c55011e5`)
- [observation/documented] bb is in active development: core architecture is described as stable, but workflows and surfaces are still evolving. -- evidence: [README.md#L21-L23](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L21-L23) (`clm_354d4984d659e3e26d61cbc0cbb5ca300d78fc7efce155f3cb1be644f3299c22`)
- [observation/documented] In remote development modes the server API is unauthenticated and permits command execution and file reads, so the docs instruct restricting access to trusted network boundaries. -- evidence: [README.md#L165-L169](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L165-L169), [README.md#L152-L156](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L152-L156) (`clm_85c2c208380e2d11056e49174a13542f6484a6c549b268096fde050148d77fc2`)

## relevance (1 claim(s))

- [observation/documented] The project is relevant to agent-runtime work: an agentic IDE with plugin/marketplace concepts, a Codex provider plugin adapter, and a published plugin SDK. -- evidence: [README.md#L85-L93](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L85-L93), [docs/bb-release-process.md#L262-L265](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L262-L265), [README.md#L14-L15](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L14-L15), [docs/codex-app-server.md#L8-L12](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/codex-app-server.md#L8-L12) (`clm_dcd90f7b77db69dc9b504d015a134812a81bc52a360533c5a829f4b480771666`)

