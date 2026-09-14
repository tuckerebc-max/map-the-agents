---
access: public
aliases: []
claim_ids:
- clm_4470697a9f676492f651f4239cdfed50f8c1c47aac9eed66ad8cd875686cd213
- clm_7447858dcbdcaaab82e209d5632265ba932ebf12cde85ecddd1a98d0ed5276e5
maturity: draft
page_id: pg_0dd6e8db6d465e4b9cc0062f554bd003
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d0c43684f58526fa26813b356bfbc1c
title: ivan-magda/swift-coding-agent/docs/s00.md @ 88ed290dff95
updated_at: '2026-09-14T02:06:02Z'
---

# ivan-magda/swift-coding-agent/docs/s00.md @ 88ed290dff95

<!-- rcw:begin owner=source:src_2d0c43684f58526fa26813b356bfbc1c block=evidence -->
- Repository development practice: the stage-0 guide walks contributors through a two-target SPM layout with a Swift Testing test target (CoreTests importing Core), .env-based ANTHROPIC_API_KEY configuration, and swift build/run/test verification commands. [@claim:clm_4470697a9f676492f651f4239cdfed50f8c1c47aac9eed66ad8cd875686cd213]
- The package depends on AsyncHTTPClient (from 1.32.0, SwiftNIO-based) rather than URLSession for cross-platform macOS/Linux HTTP and streaming SSE, built with Swift 6.2 strict concurrency. [@claim:clm_7447858dcbdcaaab82e209d5632265ba932ebf12cde85ecddd1a98d0ed5276e5]
<!-- rcw:end owner=source:src_2d0c43684f58526fa26813b356bfbc1c block=evidence -->

## Researcher notes

