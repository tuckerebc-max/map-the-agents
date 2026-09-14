---
access: public
aliases: []
claim_ids:
- clm_149a190fb794a5c7020cc99802cb63b967a43cc97ccd95cd8bbe6becb0fe0dc2
- clm_665a2b565d04a6d93e64ef6234871db8d20d9e5102ad264db40ece396019bf9c
- clm_7844959ef0b0822bf31286dad73f4a5f5243c610f4d080a09044bb52136daa2d
- clm_ae9f27385b83bf8aaea0c185150f8da4623c9d17dc23accdc068e9586a38eaba
- clm_b0d860cda64beb82ce512eb3bd80b778826e85cbb126392ccf27975688b20d38
- clm_c0f1365948313364066c9a61f92f5107f80ab83c1ac25edd46cd4006483d048b
- clm_cde2fbb4711673355804bcd857f14126a7e873fb5cbd5fb82a658cb78aa45000
- clm_d0566ae51692f2a1218ec2fbbcf7e9b059f7894bc8fb9b23f204121dd9ea85da
- clm_f7d11faa42b6be413f538e4b2bab18401eb534542b9615e753d8e7cee18f1758
maturity: draft
page_id: pg_7fa865d7c6cf5c889e073396c27e046c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0181f6dab422564b8220988a441bb267
title: fy0/CodeKanban/README.md @ 921b2512aeb0
updated_at: '2026-09-14T02:01:10Z'
---

# fy0/CodeKanban/README.md @ 921b2512aeb0

<!-- rcw:begin owner=source:src_0181f6dab422564b8220988a441bb267 block=evidence -->
- Development requires Node.js v20.19.0+ or v22.12.0+, Go 1.25+, and pnpm 9.15.9. [@claim:clm_149a190fb794a5c7020cc99802cb63b967a43cc97ccd95cd8bbe6becb0fe0dc2]
- The build produces a single-file executable: frontend artifacts from ui/dist are copied to static/ and embedded into the Go binary. [@claim:clm_665a2b565d04a6d93e64ef6234871db8d20d9e5102ad264db40ece396019bf9c]
- The repo ships an installable Codex skill bundle built around a single public CLI, codekanban-cli, with the skill source at packages/codekanban-cli/skills/codekanban-cli. [@claim:clm_7844959ef0b0822bf31286dad73f4a5f5243c610f4d080a09044bb52136daa2d]
- The backend exposes an OpenAPI docs page at /docs and a health check at /api/v1/health in development. [@claim:clm_ae9f27385b83bf8aaea0c185150f8da4623c9d17dc23accdc068e9586a38eaba]
- The project is a Go backend paired with a Vue 3.5 / TypeScript 5.8 frontend, per README badges. [@claim:clm_b0d860cda64beb82ce512eb3bd80b778826e85cbb126392ccf27975688b20d38]
- Worktree management uses a hybrid Git engine: go-git for fast in-process reads (status, diff, line stats) and system Git preferred for commits and mutations to preserve hooks, signing, filters, and user config; read and write engines are independently selectable in Settings. [@claim:clm_c0f1365948313364066c9a61f92f5107f80ab83c1ac25edd46cd4006483d048b]
- The product is runnable via `npx codekanban` or a global npm install of the codekanban package. [@claim:clm_cde2fbb4711673355804bcd857f14126a7e873fb5cbd5fb82a658cb78aa45000]
- The backend binary accepts flags: -m/--migrate to force database migration, -i/--install to install as a system service, and --uninstall. [@claim:clm_d0566ae51692f2a1218ec2fbbcf7e9b059f7894bc8fb9b23f204121dd9ea85da]
- codekanban-cli defaults to service URL http://127.0.0.1:3007, supports --base-url overrides, saves auth tokens via `auth save-token --password-stdin`, and stores session.json under %APPDATA% or XDG config paths. [@claim:clm_f7d11faa42b6be413f538e4b2bab18401eb534542b9615e753d8e7cee18f1758]
<!-- rcw:end owner=source:src_0181f6dab422564b8220988a441bb267 block=evidence -->

## Researcher notes

