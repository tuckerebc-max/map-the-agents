---
access: public
aliases: []
claim_ids:
- clm_393a89decc217335128a19a8061fcb03c78a04fcd9620f35e34b405bae33eaaa
- clm_4bb283606bcd897a87dc54c262f3e8ad737dbbb46739f2b0d5983c60f5b0a0e9
- clm_9c5da556c2d145f176791006c1991c10606765cb95c5a2a80826063e8e001420
- clm_e825889515b7b4d46bbba3f986dfce0fd01d2296ad5d01838eba3c9e68362f59
maturity: draft
page_id: pg_da6681c024925dcc87f5c0b4d39c108d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_00685acfe4df544897473a3f347220b6
title: YoanWai/agent-manager/AGENTS.md @ 0f40e31fb1ca
updated_at: '2026-09-14T03:26:06Z'
---

# YoanWai/agent-manager/AGENTS.md @ 0f40e31fb1ca

<!-- rcw:begin owner=source:src_00685acfe4df544897473a3f347220b6 block=evidence -->
- Repository development practice: the codebase layout is main.go dispatching subcommands, internal/ui as a Bubble Tea program, internal/tmux for the dedicated socket, internal/store for SQLite state, and internal/status for classifying pane output. [@claim:clm_393a89decc217335128a19a8061fcb03c78a04fcd9620f35e34b405bae33eaaa]
- Repository development practice: contributors should keep the product a thin wrapper around supported TUIs, avoiding hardcoded models and provider-specific features, and do feature work in an isolated git worktree. [@claim:clm_4bb283606bcd897a87dc54c262f3e8ad737dbbb46739f2b0d5983c60f5b0a0e9]
- Repository development practice: releases are cut locally with goreleaser from a clean worktree at the tag, with no release workflow in CI; AUR_KEY is required or the Arch package publish silently skips. [@claim:clm_9c5da556c2d145f176791006c1991c10606765cb95c5a2a80826063e8e001420]
- Repository development practice: tests must run as `env -u TMUX TMUX_TMPDIR=/tmp/amtest go test ./...` because the suite drives a real tmux server and a bare go test could hit the live socket; gofmt and go vet must be clean before finishing. [@claim:clm_e825889515b7b4d46bbba3f986dfce0fd01d2296ad5d01838eba3c9e68362f59]
<!-- rcw:end owner=source:src_00685acfe4df544897473a3f347220b6 block=evidence -->

## Researcher notes

