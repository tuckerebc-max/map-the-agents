---
access: public
aliases: []
claim_ids:
- clm_012ba13d2f4d1fd053e2a4741a45e129204ae2293fcd2b9c4dd13c9dbf1aecc8
- clm_2c94e3b8ec1f9d816c000a00c64b432928f2615611fcfa1b78bed6a3a7562ba0
- clm_319c7100f3669aad8b19cc32ec4f3bfb641c3040da6efacc725033c7c684e915
- clm_391a72e5e594caef77f2e63ad172d47e3c3ef1967208491db6d14a80506b64cb
- clm_39fb79aa6e34a28abb3e1c9877d6af6cf773a596633261506314d3165df81380
- clm_428422f5bf33b6035bd67118e332a58b18b1f8448fc011b768351955b1b021ce
- clm_51b6229c10720b1fa2bc44b7ab902b8ad05ad60aa405094e14644448b7a9e599
- clm_702a2f27ac3b1c92b23ba7a3bb13943dec811f47852df38e914cc057f7afd860
- clm_b674c37448cbbdfc81ad60e44f7457796b14d5e5a754a210e102d627394e1c4a
- clm_e2d3c884f44e5bd60f5b2f4685dc485d194085cb4c761bfabb917e00970e6a09
maturity: draft
page_id: pg_eb04f2955dc558c991b296b747dd346d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4086424b20115afdac9a9e897a4c7e73
title: arul28/ADE/README.md @ 4e14f9cdf0e4
updated_at: '2026-09-14T01:34:36Z'
---

# arul28/ADE/README.md @ 4e14f9cdf0e4

<!-- rcw:begin owner=source:src_4086424b20115afdac9a9e897a4c7e73 block=evidence -->
- The project is licensed AGPL-3.0, while the @ade-dev/sdk and @ade-dev/chat-ui npm packages are MIT and an ADE Runtime Embedding Exception covers shipping the runtime binary. [@claim:clm_012ba13d2f4d1fd053e2a4741a45e129204ae2293fcd2b9c4dd13c9dbf1aecc8]
- The repo contains apps/ade-cli (Brain, CLI, and ade code TUI), apps/desktop (Electron), apps/ios (SwiftUI), and apps/web (website and downloads). [@claim:clm_2c94e3b8ec1f9d816c000a00c64b432928f2615611fcfa1b78bed6a3a7562ba0]
- There is no Linux desktop app yet; Linux can run only the Brain, and the Windows desktop app is beta with some macOS features unavailable and ARM64 unsupported. [@claim:clm_319c7100f3669aad8b19cc32ec4f3bfb641c3040da6efacc725033c7c684e915]
- ADE runs Claude Code, Codex, Cursor, Factory Droid, and OpenCode in one workspace reachable from any machine, the web, or a mobile app, and is described as free. [@claim:clm_391a72e5e594caef77f2e63ad172d47e3c3ef1967208491db6d14a80506b64cb]
- ADE is local-first: the Brain is the always-on process owning the project catalog, sync websocket, and authority to run things; project data lives in .ade/ per repo and machine state in ~/.ade. [@claim:clm_39fb79aa6e34a28abb3e1c9877d6af6cf773a596633261506314d3165df81380]
- The ade CLI offers subcommands such as desktop, brain status, code, lanes create, prs checks, and actions list, sharing the same binary that runs the Brain. [@claim:clm_428422f5bf33b6035bd67118e332a58b18b1f8448fc011b768351955b1b021ce]
- ade connect links a machine to an ADE account, with flags --status --text, --headless for SSH device flow, and --no-login for local/LAN-only service setup. [@claim:clm_51b6229c10720b1fa2bc44b7ab902b8ad05ad60aa405094e14644448b7a9e599]
- The installer supports overrides including ADE_VERSION, ADE_INSTALL_DIR, ADE_HOME, ADE_INSTALL_NO_PATH, and ADE_INSTALL_NO_PROMPT, and skips prompts when no terminal is attached. [@claim:clm_702a2f27ac3b1c92b23ba7a3bb13943dec811f47852df38e914cc057f7afd860]
- Mobile connections prefer LAN, then Tailscale, falling back to ADE's own relay service; without an account, pairing is possible via QR/link, LAN/Tailscale scan, or SSH. [@claim:clm_b674c37448cbbdfc81ad60e44f7457796b14d5e5a754a210e102d627394e1c4a]
- Repository development practice: validation uses desktop and CLI typecheck/test/build commands, with the large desktop suite sharded and the smallest relevant subset run first. [@claim:clm_e2d3c884f44e5bd60f5b2f4685dc485d194085cb4c761bfabb917e00970e6a09]
<!-- rcw:end owner=source:src_4086424b20115afdac9a9e897a4c7e73 block=evidence -->

## Researcher notes

