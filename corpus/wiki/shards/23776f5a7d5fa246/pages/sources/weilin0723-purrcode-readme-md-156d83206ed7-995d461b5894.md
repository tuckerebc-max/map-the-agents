---
access: public
aliases: []
claim_ids:
- clm_2c4d3e8d3cebfd554a8f5fae8cb0f170a696238cef3182b6a4f46f5b0b014685
- clm_2fd468cddbb832af7d6a5c090acd44764815cb0e773cd00360ae897414dbc9da
- clm_3b8a94e5cfe6f5795bc5b5e474ecf2723dca41f43dc91df56f7c55b6c607077a
- clm_6cec5f10685cc227fa13b9ac1578c1c1f4e78d00858143fbb240ea8f944a3c4f
- clm_8bca330ca74031fbc29ebff32dd74a6bfdcc231c5c6872c4bd416b4fb727a147
- clm_c749e9d12bd6ef1a66876f15b3241e62251a11601fc619725cdf50092957b3ab
- clm_dc882e293cc6bbf333c6cc8763fda4fbd852f066f70ab74ed02a8a299436960b
- clm_f9c45bb610ee0070d1d3204492ee4eaa5f943a72d02a1f29c820bfb1911f04c1
maturity: draft
page_id: pg_6f603d3f7172583a91a6995d461b5894
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb44ebcbbdd052b69a4488cbf6cedb55
title: Weilin0723/PurrCode/README.md @ 156d83206ed7
updated_at: '2026-09-14T03:22:45Z'
---

# Weilin0723/PurrCode/README.md @ 156d83206ed7

<!-- rcw:begin owner=source:src_eb44ebcbbdd052b69a4488cbf6cedb55 block=evidence -->
- The macOS PurrCode.app is not notarized, so Gatekeeper may block first launch until the user right-clicks and chooses Open; the project plans to notarize future releases. [@claim:clm_2c4d3e8d3cebfd554a8f5fae8cb0f170a696238cef3182b6a4f46f5b0b014685]
- Building from source requires Rust 1.88 or newer, Git, and platform build tools; the npm launcher requires Node.js 18+, and optional isolation dependencies are sandbox-exec (macOS) and bubblewrap (Linux). [@claim:clm_2fd468cddbb832af7d6a5c090acd44764815cb0e773cd00360ae897414dbc9da]
- TUI, IDE, and CLI share one daemon-owned session model; the IDE holds no session store, model state, permission state, or execution path, and the daemon exposes typed presentation endpoints (activity, validation, summary, usage). [@claim:clm_3b8a94e5cfe6f5795bc5b5e474ecf2723dca41f43dc91df56f7c55b6c607077a]
- Repository development practice: repository checks run cargo fmt --check, clippy with -D warnings, cargo test --workspace, plus npm tests for the purrcode package and TypeScript SDK and Python unittest discovery for the Python SDK. [@claim:clm_6cec5f10685cc227fa13b9ac1578c1c1f4e78d00858143fbb240ea8f944a3c4f]
- TUI slash commands include /connect (provider discovery/import), /mode (Ask/Plan/Build/Review), /permission (Ask/Auto/Full Access), and /ide; one-shot commands include plan, run, review, approve, doctor, sessions, resume, and rollback. [@claim:clm_8bca330ca74031fbc29ebff32dd74a6bfdcc231c5c6872c4bd416b4fb727a147]
- The product exposes a terminal Workbench (bare `purrcode`), a native Rust desktop IDE (`purrcode ide`/`gui`), and a browser Studio client (`purrcode studio`) for daemon health, sessions, and environment inspection. [@claim:clm_c749e9d12bd6ef1a66876f15b3241e62251a11601fc619725cdf50092957b3ab]
- Model output is treated as a proposal, never authority: every native action is bound to a durable authorization, re-checked before execution, and followed by recorded validation; repository content, model output, and downloaded skills are untrusted. [@claim:clm_dc882e293cc6bbf333c6cc8763fda4fbd852f066f70ab74ed02a8a299436960b]
- The IDE appears to depend on the Rust eframe/egui stack, since the docs describe it as a pure-Rust eframe/egui desktop application with no browser, Electron, Tauri, or VS Code dependency. [@claim:clm_f9c45bb610ee0070d1d3204492ee4eaa5f943a72d02a1f29c820bfb1911f04c1]
<!-- rcw:end owner=source:src_eb44ebcbbdd052b69a4488cbf6cedb55 block=evidence -->

## Researcher notes

