---
access: public
aliases: []
claim_ids:
- clm_5f82b335d9ae867b65a424b52e048569e3e278dfd7a60edd0785cfd823ad4ed2
- clm_a1c47154b93baa5cc2a617ab589cd5938ceafbb4fd59216e03d5dcc312c749e4
- clm_dbddcc38b05e8a4bfafc9d6d60a0c60d47b6799e4246a7cc512151f50251663f
- clm_eae365bc1e2cc59600e948b8b4b2b2e3c80ecde0f81b14017aa760033b516687
maturity: draft
page_id: pg_c39238db851e5b36a3af8e7957a61cbc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a26c391fc90d5d6282f317051e3b615b
title: aaif-goose/goose/BUILDING_LINUX.md @ 50666ae0b9a5
updated_at: '2026-09-14T04:51:09Z'
---

# aaif-goose/goose/BUILDING_LINUX.md @ 50666ae0b9a5

<!-- rcw:begin owner=source:src_a26c391fc90d5d6282f317051e3b615b block=evidence -->
- Repository development practice: building the Linux desktop app requires Rust, Node.js 22.9.0+, pnpm 10+, and 'just'; the CLI is built with 'cargo build --release -p goose-cli --bin goose' and packaged via Electron Forge (ZIP recommended, plus DEB and Flatpak). [@claim:clm_5f82b335d9ae867b65a424b52e048569e3e278dfd7a60edd0785cfd823ad4ed2]
- The musl/portable Linux build disables local-inference (V8) and system-keyring (D-Bus SecretService) because neither is available on Android, and Snap packaging is not currently supported. [@claim:clm_a1c47154b93baa5cc2a617ab589cd5938ceafbb4fd59216e03d5dcc312c749e4]
- Repository development practice: BUILDING_LINUX.md asks contributors to Linux build changes to test on multiple distributions, update documentation, and consider CI/CD implications. [@claim:clm_dbddcc38b05e8a4bfafc9d6d60a0c60d47b6799e4246a7cc512151f50251663f]
- BUILDING_LINUX.md gives separate package commands for Debian/Ubuntu, Fedora, openSUSE, and Arch/Manjaro. The Debian command includes protobuf-compiler and libxcb1-dev; Fedora includes libxcb-devel. Its Arch command uses shaderc, while Debian, Fedora, and openSUSE list glslc. [@claim:clm_eae365bc1e2cc59600e948b8b4b2b2e3c80ecde0f81b14017aa760033b516687]
<!-- rcw:end owner=source:src_a26c391fc90d5d6282f317051e3b615b block=evidence -->

## Researcher notes

