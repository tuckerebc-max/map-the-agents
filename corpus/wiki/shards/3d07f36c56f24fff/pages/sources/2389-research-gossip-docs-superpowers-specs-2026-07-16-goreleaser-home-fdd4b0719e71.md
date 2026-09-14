---
access: public
aliases: []
claim_ids:
- clm_15c53c9fc340f6900e9c6d34946a26da746e5f464497cb1696034e7833bdd610
- clm_aee5553be45bc74727ad77b37f6ec40a44e5129bcfa1b498654373cdf76c8bd4
- clm_b7b13fb3d0d804bd0640fddcb0311a5f070a31fd13f2023920c83bbb4c3621bb
maturity: draft
page_id: pg_a41e617905a853e6813afdd4b0719e71
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_61782d3cae565f74a154388c268bfb86
title: 2389-research/gossip/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md
  @ fb54508fa18c
updated_at: '2026-09-14T03:28:42Z'
---

# 2389-research/gossip/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md @ fb54508fa18c

<!-- rcw:begin owner=source:src_61782d3cae565f74a154388c268bfb86 block=evidence -->
- Repository development practice: the canonical gate is ./scripts/check (gofmt, vet, test) run before every commit, with conventional commits, ABOUTME header lines in .go and YAML files, and hooks never bypassed. [@claim:clm_15c53c9fc340f6900e9c6d34946a26da746e5f464497cb1696034e7833bdd610]
- The tool is a single Go binary built with cobra, using pure-Go SQLite via modernc.org/sqlite so CGO_ENABLED=0 cross-compiles cleanly for darwin/linux on amd64 and arm64. [@claim:clm_aee5553be45bc74727ad77b37f6ec40a44e5129bcfa1b498654373cdf76c8bd4]
- Repository development practice: releases are automated via a tag-push (v*) GitHub Actions workflow running goreleaser, which builds binaries, creates the GitHub release, and publishes a formula to 2389-research/homebrew-tap. [@claim:clm_b7b13fb3d0d804bd0640fddcb0311a5f070a31fd13f2023920c83bbb4c3621bb]
<!-- rcw:end owner=source:src_61782d3cae565f74a154388c268bfb86 block=evidence -->

## Researcher notes

