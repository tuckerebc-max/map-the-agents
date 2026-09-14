---
access: public
aliases: []
claim_ids:
- clm_04ca44a21ca25df5c2c52c838258e9f80fed4ce6b453e030bb04776eb0c9dbd1
- clm_09ab4aa3a35d0cb5fecc7245e06c53b1bb8ec5d2837440d2e4bf4f36df77bd83
- clm_397f2765b0cccf2f32eba58283621aedeeb6dd03de00ad9e70629f3f2a683416
- clm_6321470c198809b3ff97493e98680c2b3979e65f0063018ee5214cf8315af50d
- clm_7d70330eb113d82e1ae0d4d175f9c766d023603df3a3a0d0efaa6ea4df88f126
- clm_99bf147b6880b03e234149178b4d9e520a629e84910f95181e7994c58459762c
- clm_a16343be002907b975b80822bce704c6ba1aafe213d32b0c2795c928f3b19e31
- clm_c0ee8c0af87bc4ac86a6577db657a9bdeb21dc6c2bf753747dc4d9d8b0729427
- clm_c19d1ef74a63224219b7f6ee6bf44a94476d92f871ae272cb0fe17b21d7caad6
- clm_d2d617bc87e36c6f10d29ca3341c065e8d73037a15661e59380795a71d2c5550
- clm_e9615466d953f7c839e05939da3d5b1a5de7a7d2b509c24c4a2a5092835b027b
- clm_ee0a970facdf5a50ca9e1417629b50aa5ddf188fc60d7be2002631adcaa26010
maturity: draft
page_id: pg_c20f0d191bd85d19b063e9f08851f22d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7d1b807eeb835257ae2e20000e8b398b
title: madarco/agentbox/README.md @ 138c1f585fdb
updated_at: '2026-09-14T02:15:17Z'
---

# madarco/agentbox/README.md @ 138c1f585fdb

<!-- rcw:begin owner=source:src_7d1b807eeb835257ae2e20000e8b398b block=evidence -->
- Boxes support checkpoints: new boxes can start from a previous checkpoint in under a second, boxes auto-pause when idle to save resources, and `agentbox checkpoint` lists/creates project checkpoints. [@claim:clm_04ca44a21ca25df5c2c52c838258e9f80fed4ce6b453e030bb04776eb0c9dbd1]
- Repository development practice: contributors must keep the public docs site (apps/web/content/docs) in sync in the same change whenever a CLI command, flag, config key, default, or provider behavior changes, and first-time contributors sign a one-line CLA on their first PR. [@claim:clm_09ab4aa3a35d0cb5fecc7245e06c53b1bb8ec5d2837440d2e4bf4f36df77bd83]
- A box argument is optional in most commands, defaulting to the current project's box, and can be given as a short index, name, or id prefix. [@claim:clm_397f2765b0cccf2f32eba58283621aedeeb6dd03de00ad9e70629f3f2a683416]
- Custom providers are supported via plugins built as npm packages on @madarco/agentbox-provider-sdk, registered with `agentbox plugin add` without modifying AgentBox itself. [@claim:clm_6321470c198809b3ff97493e98680c2b3979e65f0063018ee5214cf8315af50d]
- Cloud provider credentials are configured via per-provider interactive login commands (vercel, hetzner, daytona, e2b, digitalocean) saved to ~/.agentbox/secrets.env, and remote-docker connects over SSH using the user's own ~/.ssh/config. [@claim:clm_7d70330eb113d82e1ae0d4d175f9c766d023603df3a3a0d0efaa6ea4df88f126]
- Git credentials stay on the local machine, and pushing to the remote repository requires permission requests, as a safety design. [@claim:clm_99bf147b6880b03e234149178b4d9e520a629e84910f95181e7994c58459762c]
- Repository development practice: build from source by cloning the repo, running `pnpm install && pnpm build`, then invoking `node apps/cli/dist/index.js --help`; the full dev workflow and smoke tests live in docs/development.md. [@claim:clm_a16343be002907b975b80822bce704c6ba1aafe213d32b0c2795c928f3b19e31]
- The CLI exposes commands grouped as create/run (create, claude), access (url, screen, code, shell, open, logs, dashboard), inspect (list, status, top), lifecycle (start, stop, destroy, pause/unpause), sync (download, cp, checkpoint), and advanced (wait, prune, self-update, config, relay, app). [@claim:clm_c0ee8c0af87bc4ac86a6577db657a9bdeb21dc6c2bf753747dc4d9d8b0729427]
- Requirements are macOS (arm64 or Intel) or Linux, Docker Desktop or OrbStack, and Node >=20.10; the first create/claude builds a ~1 GB agentbox/box:dev image once, and portless gives box web apps consistent URLs. [@claim:clm_c19d1ef74a63224219b7f6ee6bf44a94476d92f871ae272cb0fe17b21d7caad6]
- `agentbox claude` creates a sandboxed box and launches Claude Code in a detachable tmux session, and `agentbox attach 1` reconnects to a box later. [@claim:clm_d2d617bc87e36c6f10d29ca3341c065e8d73037a15661e59380795a71d2c5550]
- The product offers a nightly pre-release install channel via @madarco/agentbox@nightly, with `agentbox self-update --channel stable` to opt back out. [@claim:clm_e9615466d953f7c839e05939da3d5b1a5de7a7d2b509c24c4a2a5092835b027b]
- Multiple sandbox backends are supported: local Docker, remote Docker, Hetzner, Vercel, and E2B fully supported, with Daytona marked partial; each differs in base image source, snapshot support, and preview URL mechanism. [@claim:clm_ee0a970facdf5a50ca9e1417629b50aa5ddf188fc60d7be2002631adcaa26010]
<!-- rcw:end owner=source:src_7d1b807eeb835257ae2e20000e8b398b block=evidence -->

## Researcher notes

