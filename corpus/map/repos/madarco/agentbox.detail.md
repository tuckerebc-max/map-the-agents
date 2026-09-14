# madarco/agentbox -- full detail

[Back to orientation](agentbox.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/madarco/agentbox/138c1f585fdbeddff392bbf76086b1d8382a998e/a04bee36c7612b6b.json](../../../wiki/dossiers/madarco/agentbox/138c1f585fdbeddff392bbf76086b1d8382a998e/a04bee36c7612b6b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Multiple sandbox backends are supported: local Docker, remote Docker, Hetzner, Vercel, and E2B fully supported, with Daytona marked partial; each differs in base image source, snapshot support, and preview URL mechanism. -- evidence: [README.md#L88-L93](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L88-L93) (`clm_ee0a970facdf5a50ca9e1417629b50aa5ddf188fc60d7be2002631adcaa26010`)

## design-choices (1 claim(s))

- [observation/documented] Git credentials stay on the local machine, and pushing to the remote repository requires permission requests, as a safety design. -- evidence: [README.md#L24-L28](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L24-L28) (`clm_99bf147b6880b03e234149178b4d9e520a629e84910f95181e7994c58459762c`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: build from source by cloning the repo, running `pnpm install && pnpm build`, then invoking `node apps/cli/dist/index.js --help`; the full dev workflow and smoke tests live in docs/development.md. -- evidence: [README.md#L174-L174](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L174-L174), [README.md#L168-L172](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L168-L172) (`clm_a16343be002907b975b80822bce704c6ba1aafe213d32b0c2795c928f3b19e31`)
- [observation/documented] Repository development practice: tests use vitest with default discovery and must stay pure (no docker, no network); integration testing is currently manual, and linting uses eslint plus prettier via `pnpm lint`/`pnpm format`. -- evidence: [CLAUDE.md#L62-L71](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/CLAUDE.md#L62-L71) (`clm_77ca1f3dff279cba57d6f65f706a95f0e2a40d76542dc37d89c2a0d576bbf3ed`)
- [observation/documented] Repository development practice: the codebase convention is strict TypeScript ESM with tsup builds, commander for the CLI, @clack/prompts for interactivity, and execa for shelling out to docker; a PTY harness (`pnpm drive`) drives interactive TUIs during verification. -- evidence: [CLAUDE.md#L62-L71](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/CLAUDE.md#L62-L71), [CLAUDE.md#L36-L58](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/CLAUDE.md#L36-L58) (`clm_975b03f08f602eac30b91a9f7d2847fd486771703376ef5a70876ff1a81783f2`)
- [observation/documented] Repository development practice: contributors must keep the public docs site (apps/web/content/docs) in sync in the same change whenever a CLI command, flag, config key, default, or provider behavior changes, and first-time contributors sign a one-line CLA on their first PR. -- evidence: [README.md#L209-L209](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L209-L209), [CLAUDE.md#L110-L134](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/CLAUDE.md#L110-L134) (`clm_09ab4aa3a35d0cb5fecc7245e06c53b1bb8ec5d2837440d2e4bf4f36df77bd83`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The CLI exposes commands grouped as create/run (create, claude), access (url, screen, code, shell, open, logs, dashboard), inspect (list, status, top), lifecycle (start, stop, destroy, pause/unpause), sync (download, cp, checkpoint), and advanced (wait, prune, self-update, config, relay, app). -- evidence: [README.md#L118-L124](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L118-L124), [README.md#L147-L152](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L147-L152), [README.md#L128-L130](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L128-L130), [README.md#L141-L143](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L141-L143), [README.md#L134-L137](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L134-L137), [README.md#L113-L114](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L113-L114) (`clm_c0ee8c0af87bc4ac86a6577db657a9bdeb21dc6c2bf753747dc4d9d8b0729427`)
- [observation/documented] `agentbox claude` creates a sandboxed box and launches Claude Code in a detachable tmux session, and `agentbox attach 1` reconnects to a box later. -- evidence: [README.md#L48-L48](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L48-L48), [README.md#L113-L114](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L113-L114) (`clm_d2d617bc87e36c6f10d29ca3341c065e8d73037a15661e59380795a71d2c5550`)
- [observation/documented] A box argument is optional in most commands, defaulting to the current project's box, and can be given as a short index, name, or id prefix. -- evidence: [README.md#L109-L109](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L109-L109) (`clm_397f2765b0cccf2f32eba58283621aedeeb6dd03de00ad9e70629f3f2a683416`)
- [observation/documented] Cloud provider credentials are configured via per-provider interactive login commands (vercel, hetzner, daytona, e2b, digitalocean) saved to ~/.agentbox/secrets.env, and remote-docker connects over SSH using the user's own ~/.ssh/config. -- evidence: [README.md#L97-L105](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L97-L105) (`clm_7d70330eb113d82e1ae0d4d175f9c766d023603df3a3a0d0efaa6ea4df88f126`)
- [observation/documented] The product offers a nightly pre-release install channel via @madarco/agentbox@nightly, with `agentbox self-update --channel stable` to opt back out. -- evidence: [README.md#L79-L81](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L79-L81) (`clm_e9615466d953f7c839e05939da3d5b1a5de7a7d2b509c24c4a2a5092835b027b`)

## memory-state (1 claim(s))

- [observation/documented] Boxes support checkpoints: new boxes can start from a previous checkpoint in under a second, boxes auto-pause when idle to save resources, and `agentbox checkpoint` lists/creates project checkpoints. -- evidence: [README.md#L24-L28](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L24-L28), [README.md#L141-L143](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L141-L143) (`clm_04ca44a21ca25df5c2c52c838258e9f80fed4ce6b453e030bb04776eb0c9dbd1`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requirements are macOS (arm64 or Intel) or Linux, Docker Desktop or OrbStack, and Node >=20.10; the first create/claude builds a ~1 GB agentbox/box:dev image once, and portless gives box web apps consistent URLs. -- evidence: [README.md#L83-L84](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L83-L84) (`clm_c19d1ef74a63224219b7f6ee6bf44a94476d92f871ae272cb0fe17b21d7caad6`)
- [observation/documented] Custom providers are supported via plugins built as npm packages on @madarco/agentbox-provider-sdk, registered with `agentbox plugin add` without modifying AgentBox itself. -- evidence: [README.md#L196-L199](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L196-L199), [README.md#L192-L192](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L192-L192) (`clm_6321470c198809b3ff97493e98680c2b3979e65f0063018ee5214cf8315af50d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

