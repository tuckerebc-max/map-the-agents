---
access: public
aliases: []
claim_ids:
- clm_0808b10c7b4e58c0c6cf8f6f2428dac5de889fcc913debe8dc83c553bc7b9d9c
- clm_14c8597f04bfc0d0cf0b5d5b93433c504b99d82f60dcef54ee9012ac873c77d3
- clm_14e96e6a326c7ae9a658306bc71fe3c9a41b9cfb09c971c6e5715de88db63e2e
- clm_4981a9df3749bb06b507b8ab92f8f808bc0f91766a7c91d9536c88cc49f6d1b8
- clm_4eb915dd780f40054391d925df0c9cb362363e3758242172a87a8113c12c9d45
- clm_4f4cd292611887f4327dd9359ceabce5a010029ad44dbd4c84b2c5a8cfa8acd8
- clm_a1328d147906cc2b906f3313db67094ac302951fd34ce395cb553b00fe5420c1
- clm_be689ba1b82b866504cd1a97d9784424191a7485e886d111b79423c63a0ef25c
- clm_c4f3efd765e2dba08679f7f328c477c4cac16ea1a64d93770ea3c80d9c1545d3
- clm_fc4502c336b74932aa7b8d3822a2734f2ac0857f4d3608775371d02bfd273eef
maturity: draft
page_id: pg_1e45360a13955bafa3b0d505a85d1a9a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_934e4944539056409acf7e6c3719faa9
title: abcwyc/pi-agent-desktop/README.md @ 378db4dc27e4
updated_at: '2026-09-14T01:59:03Z'
---

# abcwyc/pi-agent-desktop/README.md @ 378db4dc27e4

<!-- rcw:begin owner=source:src_934e4944539056409acf7e6c3719faa9 block=evidence -->
- Repository development practice: contributors run npm test, tsc --noEmit, npm run lint, cargo fmt/clippy checks, and npm run release:verify; they should avoid next build during normal development. [@claim:clm_0808b10c7b4e58c0c6cf8f6f2428dac5de889fcc913debe8dc83c553bc7b9d9c]
- The app reads Pi's local data directory ~/.pi/agent by default, picking up existing sessions, models, and authentication; PI_CODING_AGENT_DIR can point elsewhere. [@claim:clm_14c8597f04bfc0d0cf0b5d5b93433c504b99d82f60dcef54ee9012ac873c77d3]
- The product is a local AI agent desktop application for macOS and Windows that packages the pi agent's capabilities into a standalone installable app. [@claim:clm_14e96e6a326c7ae9a658306bc71fe3c9a41b9cfb09c971c6e5715de88db63e2e]
- Features include browsing and resuming past Pi sessions, real-time chat with visible thinking/tool calls/cost, branching or forking conversations, and Git worktree switching from the sidebar. [@claim:clm_4981a9df3749bb06b507b8ab92f8f808bc0f91766a7c91d9536c88cc49f6d1b8]
- Repository development practice: a nightly component-updates workflow syncs upstream pi and pi-web releases, intersecting changes with fork-ownership.json and running the full gate before pushing to main or opening a PR. [@claim:clm_4eb915dd780f40054391d925df0c9cb362363e3758242172a87a8113c12c9d45]
- Building requires Node.js 22 (recommended), npm, Rust 1.85+, plus platform toolchains such as Xcode CLT on macOS and Microsoft C++ Build Tools with WebView2 on Windows. [@claim:clm_4f4cd292611887f4327dd9359ceabce5a010029ad44dbd4c84b2c5a8cfa8acd8]
- The desktop package bundles a Next.js standalone server, a Node.js runtime, and the current Pi SDK, so the local server starts with the app without separate installation. [@claim:clm_a1328d147906cc2b906f3313db67094ac302951fd34ce395cb553b00fe5420c1]
- The file-browsing API restricts access to the current session, the selected project, and explicitly authorized working directories; model keys and session data stay local. [@claim:clm_be689ba1b82b866504cd1a97d9784424191a7485e886d111b79423c63a0ef25c]
- The app can preview source code, diffs, Markdown, images, audio, PDF, and DOCX files, and offers dark mode, automatic session naming, and a completion sound. [@claim:clm_c4f3efd765e2dba08679f7f328c477c4cac16ea1a64d93770ea3c80d9c1545d3]
- Updates are whole-app only: the upgrade button installs one complete signed build containing all three components and restarts; it never patches individual JavaScript packages or downloads unsigned files. [@claim:clm_fc4502c336b74932aa7b8d3822a2734f2ac0857f4d3608775371d02bfd273eef]
<!-- rcw:end owner=source:src_934e4944539056409acf7e6c3719faa9 block=evidence -->

## Researcher notes

