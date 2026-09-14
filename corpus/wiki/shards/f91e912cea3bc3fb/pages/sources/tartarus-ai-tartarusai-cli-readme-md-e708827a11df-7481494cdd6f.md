---
access: public
aliases: []
claim_ids:
- clm_1753787732615197f2ef03d35ea24c138b9a4a76cca505b0b2b290c2f4a0bc54
- clm_3268dd22e065f8595afdbbbf8f5e4b587ae983a3d7950722366faa662d60e371
- clm_33e35aba6c96c57cebe421425a381db6ba2ea0b5cc0ab0cd1a2b117902db34d0
- clm_50d29438b0a390b917939868b1f4b0e89da37a5fe8132e659bc6ba2514a2edf9
- clm_7400b1f34b147139ac2c889e6131f3cc376a3a4b654a04f999ff17851f3fc834
- clm_99ba21905e6465ed3bd80e88a07a90a9f7c7018f3d2b6ca32cddb9cd1b4c2008
- clm_9eb9988def17469a3e1d598bcef584a5189f9bf0554c8a5cb60ecc42dd602351
- clm_c6f9abb1ae627f83809d280eada8d04f4d89e7f8424c3671cdc978114531349e
- clm_deb736b876fc2a25a0d5f6624f7510864d92dfe4d84d550f694e79d3e861fdee
maturity: draft
page_id: pg_4709b76897be5821b01a7481494cdd6f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3e5536f924985437a087c04ea97e00bb
title: Tartarus-AI/tartarusai-cli/README.md @ e708827a11df
updated_at: '2026-09-14T03:17:54Z'
---

# Tartarus-AI/tartarusai-cli/README.md @ e708827a11df

<!-- rcw:begin owner=source:src_3e5536f924985437a087c04ea97e00bb block=evidence -->
- The CLI ships as a single self-contained binary requiring no Python, pip, or Node runtime. [@claim:clm_1753787732615197f2ef03d35ea24c138b9a4a76cca505b0b2b290c2f4a0bc54]
- The README states stated boundaries: no weaponized payloads, spyware, DRM bypass, or license cracking; lab PoCs for patched public CVEs are in scope, attacking systems you don't own is not. [@claim:clm_3268dd22e065f8595afdbbbf8f5e4b587ae983a3d7950722366faa662d60e371]
- Installation on macOS/Linux is via a curl-piped setup script that installs to ~/.local/bin and auto-detects OS and CPU, falling back to a baseline build on CPUs without AVX2. [@claim:clm_33e35aba6c96c57cebe421425a381db6ba2ea0b5cc0ab0cd1a2b117902db34d0]
- The project is MIT-licensed, with LICENSE and NOTICE files referenced for full attribution. [@claim:clm_50d29438b0a390b917939868b1f4b0e89da37a5fe8132e659bc6ba2514a2edf9]
- Quickstart: create an account and CLI token at dash.tartarusai.dev/account, run 'tartarus' in a project directory, and paste the API key on first launch, where it is validated and saved. [@claim:clm_7400b1f34b147139ac2c889e6131f3cc376a3a4b654a04f999ff17851f3fc834]
- Advertised capabilities include a 256K context window, crypto-only billing, roughly 30 seconds from payment to activation, and a 14-day refund policy. [@claim:clm_99ba21905e6465ed3bd80e88a07a90a9f7c7018f3d2b6ca32cddb9cd1b4c2008]
- tartarusai-cli is a terminal client for TartarusAI, invoked as the 'tartarus' command, with a --help flag and docs hosted at dash.tartarusai.dev/docs. [@claim:clm_9eb9988def17469a3e1d598bcef584a5189f9bf0554c8a5cb60ecc42dd602351]
- The product is marketed as an uncensored coding agent with no policy filter, aimed at security research and edge-case automation that mainstream models reportedly refuse. [@claim:clm_c6f9abb1ae627f83809d280eada8d04f4d89e7f8424c3671cdc978114531349e]
- Windows users download a zip from the latest GitHub release and run tartarus.exe; separate release artifacts exist for linux-x64, linux-x64-baseline, darwin-arm64, and darwin-x64. [@claim:clm_deb736b876fc2a25a0d5f6624f7510864d92dfe4d84d550f694e79d3e861fdee]
<!-- rcw:end owner=source:src_3e5536f924985437a087c04ea97e00bb block=evidence -->

## Researcher notes

