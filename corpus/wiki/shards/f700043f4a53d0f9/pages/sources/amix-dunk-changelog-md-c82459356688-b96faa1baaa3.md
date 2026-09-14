---
access: public
aliases: []
claim_ids:
- clm_2afbe2b1533dd434c447dca90c4445759bd3d25cf06e02820392bbdf6c6b4d34
- clm_41b168109285f4ce36c520ef4a2f804bc6990ae5b9ce98dbe9ebf79a685b5a07
- clm_8664445b26972b0ec469f10cc5ae017773e322c5504d1f6f10ebd61952619f15
- clm_9f3064bee04729bf4c796e1e78a648cce9ce2c3deebf958eee41190820959691
- clm_fa9ff5d7bd3ed30d8dbd53b6d86946ea6df2bce15ee4324886370c036ac65cf2
maturity: draft
page_id: pg_9907ec81e9785c06b7afb96faa1baaa3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eac0d473961157e7b010d72941b56a21
title: amix/dunk/CHANGELOG.md @ c82459356688
updated_at: '2026-09-14T03:34:16Z'
---

# amix/dunk/CHANGELOG.md @ c82459356688

<!-- rcw:begin owner=source:src_eac0d473961157e7b010d72941b56a21 block=evidence -->
- The agent-facing comments CLI supports listing pending comments, showing one with 10 lines of post-image context (configurable via --context), and an atomic resolve that refuses partial success; --json returns a stable shape with drift state. [@claim:clm_2afbe2b1533dd434c447dca90c4445759bd3d25cf06e02820392bbdf6c6b4d34]
- Branch-review base resolution follows an explicit order: the --branch=<ref> flag, then [branch_review] base in .dunk/config.toml, then origin/HEAD, then main/master/trunk fallbacks, with the resolved base shown in the status bar. [@claim:clm_41b168109285f4ce36c520ef4a2f804bc6990ae5b9ce98dbe9ebf79a685b5a07]
- dunk is a hard fork of hunk that keeps the OpenTUI/Pierre diff-viewer foundation while removing the daemon, MCP, and session-broker layers; agent integration flows through the on-disk comments file. [@claim:clm_8664445b26972b0ec469f10cc5ae017773e322c5504d1f6f10ebd61952619f15]
- Review comments are stored in .dunk/comments.json with the file path, hunk anchor line, body, and a context hash so comments survive small nearby edits; the file is meant to stay local and gitignored, and is deleted once the last comment is resolved. [@claim:clm_9f3064bee04729bf4c796e1e78a648cce9ce2c3deebf958eee41190820959691]
- Ctrl-Z suspension of dunk is a no-op on Windows, per the changelog; Jujutsu (jj) support was also removed, so dunk now targets Git only. [@claim:clm_fa9ff5d7bd3ed30d8dbd53b6d86946ea6df2bce15ee4324886370c036ac65cf2]
<!-- rcw:end owner=source:src_eac0d473961157e7b010d72941b56a21 block=evidence -->

## Researcher notes

