---
access: public
aliases: []
claim_ids:
- clm_01d4d177b42d251d665b922cee4e393d5b167028351dcc4de1e8999d73ff63bf
- clm_0acdf504db33a39dd2384f698e4feedc45531e9fcdf3e6888e8303325132ed4e
- clm_3b4e5e1b8a5d9e15f7fea2161dc93a640f16df865886cf8a28b0efb0f5ea6745
- clm_aa6f12ede55e354d8e764ce322a96e3c372fbac0885147bd9a059d02d108c217
- clm_c01d5b8f8615df92088917ac0bb275bff94f10ad9b83d655a874dcda3bcc4e1c
- clm_ce515a991e4e4029df4ea6f024dcda4b6850f596c99728a2d58bae56500b3de3
- clm_d2da4b46c34912e686ae17ecf9bb610008b2ce226f9a8cc2d0929ac48159753d
- clm_fd0e3f2c1c9b0799904a331c0536f8db65804b63d3d453b723a73a994be40f3d
- clm_fdc4018060eb05485d101a2401b5a598f4f45a67d9b30d460d4e00466788ae4f
maturity: draft
page_id: pg_e354b5dde0b75c3d82db0c9c06def635
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_856ee9e81bd95ed3bf127aa7b114a6b1
title: Fission-AI/OpenSpec/README.md @ 9d4e5974e5c0
updated_at: '2026-09-14T03:51:47Z'
---

# Fission-AI/OpenSpec/README.md @ 9d4e5974e5c0

<!-- rcw:begin owner=source:src_856ee9e81bd95ed3bf127aa7b114a6b1 block=evidence -->
- The product maintains an openspec/ directory separating openspec/specs/ (current truth) from openspec/changes/ (proposed updates), and archiving merges approved updates back into the specs. [@claim:clm_01d4d177b42d251d665b922cee4e393d5b167028351dcc4de1e8999d73ff63bf]
- The stated philosophy favors fluid, iterative workflows over rigid phase gates, targeting brownfield projects and scaling from personal projects to enterprises. [@claim:clm_0acdf504db33a39dd2384f698e4feedc45531e9fcdf3e6888e8303325132ed4e]
- openspec init --tools <ids> generates per-tool skill and command files for the selected AI assistants, and the README claims support for 30+ tools. [@claim:clm_3b4e5e1b8a5d9e15f7fea2161dc93a640f16df865886cf8a28b0efb0f5ea6745]
- OpenSpec collects anonymous telemetry limited to command names and version, disabled automatically in CI, with opt-out via config or OPENSPEC_TELEMETRY/DO_NOT_TRACK environment variables. [@claim:clm_aa6f12ede55e354d8e764ce322a96e3c372fbac0885147bd9a059d02d108c217]
- Repository development practice: contributors should open a discussion or issue before a PR and link it; new features, significant refactors, and architectural changes require an OpenSpec change proposal first, with details in CONTRIBUTING.md. [@claim:clm_c01d5b8f8615df92088917ac0bb275bff94f10ad9b83d655a874dcda3bcc4e1c]
- Specs are plain Markdown with requirements and concrete scenarios and no special syntax to learn; each change gets its own folder containing proposal, specs, design, and tasks artifacts. [@claim:clm_ce515a991e4e4029df4ea6f024dcda4b6850f596c99728a2d58bae56500b3de3]
- OpenSpec is driven from AI coding tools via slash commands such as /opsx:explore, /opsx:propose, /opsx:apply, and /opsx:archive, with tool-specific spellings like /opsx-propose (Cursor, Copilot), @opsx-propose (Amazon Q), or $openspec-propose (Codex). [@claim:clm_d2da4b46c34912e686ae17ecf9bb610008b2ce226f9a8cc2d0929ac48159753d]
- OpenSpec requires Node.js 20.19.0 or higher, and the install prompt instructs checking node --version before installing. [@claim:clm_fd0e3f2c1c9b0799904a331c0536f8db65804b63d3d453b723a73a994be40f3d]
- The product ships a CLI installed globally via npm, pnpm, yarn, or bun (with a Nix option), with commands including openspec init, openspec update, and openspec config profile. [@claim:clm_fdc4018060eb05485d101a2401b5a598f4f45a67d9b30d460d4e00466788ae4f]
<!-- rcw:end owner=source:src_856ee9e81bd95ed3bf127aa7b114a6b1 block=evidence -->

## Researcher notes

