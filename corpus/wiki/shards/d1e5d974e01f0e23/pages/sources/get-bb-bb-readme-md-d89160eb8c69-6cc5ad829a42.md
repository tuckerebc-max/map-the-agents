---
access: public
aliases: []
claim_ids:
- clm_03149061ce175b954a765eb9812c93a1b2e5332d72c5d6378b1ea13e207898a3
- clm_0efd7845d3ff01d2d002f9ba0bccebe9aa818fd937bbb508953280bad32cbdea
- clm_1b8d88c5987103a1b8a0c523e15d638f6e28e88fc4257a568db691572b353ff6
- clm_25213cc62ea367d2396d161c7ddace8d5ba299472b47b72c86d52a60a1b957c0
- clm_354d4984d659e3e26d61cbc0cbb5ca300d78fc7efce155f3cb1be644f3299c22
- clm_38afb1a3663c2af1fb36780d1d2b0dbd8bae3f103a8560031a803831a71d975d
- clm_85c2c208380e2d11056e49174a13542f6484a6c549b268096fde050148d77fc2
- clm_c796ccadbdf74a94eb73d209964406eaa036cfa09c8d7c645e7f4dcd2a0231f5
- clm_dcd90f7b77db69dc9b504d015a134812a81bc52a360533c5a829f4b480771666
- clm_f6ff59583867d01f506c74b13ea330fdcb4e4e847eb392d734433507c55011e5
maturity: draft
page_id: pg_b379a9446b5751ab96ef6cc5ad829a42
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0f2057fc3eca56deb77c7165cbf2337e
title: get-bb/bb/README.md @ d89160eb8c69
updated_at: '2026-09-14T01:51:21Z'
---

# get-bb/bb/README.md @ d89160eb8c69

<!-- rcw:begin owner=source:src_0f2057fc3eca56deb77c7165cbf2337e block=evidence -->
- bb is described as an agentic IDE that builds itself, able to control, customize, and automate itself as groundwork for a user's own software factory. [@claim:clm_03149061ce175b954a765eb9812c93a1b2e5332d72c5d6378b1ea13e207898a3]
- Running via npx serves a web interface at http://localhost:38886. [@claim:clm_0efd7845d3ff01d2d002f9ba0bccebe9aa818fd937bbb508953280bad32cbdea]
- bb depends on native add-ons including better-sqlite3, node-pty, and @parcel/watcher built by npm install scripts; npm 12+ blocks those scripts by default, requiring --allow-scripts. [@claim:clm_1b8d88c5987103a1b8a0c523e15d638f6e28e88fc4257a568db691572b353ff6]
- The product exposes a desktop app, web app, CLI, and HTTP API as first-class ways to drive bb, with work running in threads that can be followed live, steered, or handed off to another agent. [@claim:clm_25213cc62ea367d2396d161c7ddace8d5ba299472b47b72c86d52a60a1b957c0]
- bb is in active development: core architecture is described as stable, but workflows and surfaces are still evolving. [@claim:clm_354d4984d659e3e26d61cbc0cbb5ca300d78fc7efce155f3cb1be644f3299c22]
- Repository development practice: the dev loop uses pnpm dev (Vite with proxied API/WebSocket traffic and per-checkout data dirs under ~/.bb-dev) and pnpm start:worktree to test the production bundle without switching to production data or ports. [@claim:clm_38afb1a3663c2af1fb36780d1d2b0dbd8bae3f103a8560031a803831a71d975d]
- In remote development modes the server API is unauthenticated and permits command execution and file reads, so the docs instruct restricting access to trusted network boundaries. [@claim:clm_85c2c208380e2d11056e49174a13542f6484a6c549b268096fde050148d77fc2]
- Production runs send anonymous usage telemetry (app starts, thread and message counts, plugin installs) with a random per-install id; development/source runs never send, and BB_TELEMETRY=false opts out. [@claim:clm_c796ccadbdf74a94eb73d209964406eaa036cfa09c8d7c645e7f4dcd2a0231f5]
- The project is relevant to agent-runtime work: an agentic IDE with plugin/marketplace concepts, a Codex provider plugin adapter, and a published plugin SDK. [@claim:clm_dcd90f7b77db69dc9b504d015a134812a81bc52a360533c5a829f4b480771666]
- The desktop app supports macOS on Apple Silicon; the Linux x64 AppImage is alpha, Intel Mac users should use npx, and native Windows PowerShell/CMD are unsupported (WSL2 instead). [@claim:clm_f6ff59583867d01f506c74b13ea330fdcb4e4e847eb392d734433507c55011e5]
<!-- rcw:end owner=source:src_0f2057fc3eca56deb77c7165cbf2337e block=evidence -->

## Researcher notes

