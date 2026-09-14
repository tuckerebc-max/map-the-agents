---
access: public
aliases: []
claim_ids:
- clm_16e079f5acfe6bb64bd02f41e52fe79b9d0113d22d02742b48fd679678db01b4
- clm_2c095273fbfb88b4109d2437695fdc23559f7163bd0008987f4a9c09ac43c2f3
- clm_41b168109285f4ce36c520ef4a2f804bc6990ae5b9ce98dbe9ebf79a685b5a07
- clm_8664445b26972b0ec469f10cc5ae017773e322c5504d1f6f10ebd61952619f15
- clm_9f3064bee04729bf4c796e1e78a648cce9ce2c3deebf958eee41190820959691
- clm_a4e2bd97a5beb2a2c38461cf865b1eaa531deb9d7787c6c34e20fc84ee47bdde
- clm_b8399ffe6af39d20a9818d54b9ff307f3fed6597de2ab583009ff85382ce9a56
- clm_c9081a390d5a93146fc361fe53be3cf4fe312949944ae4d430eed9c8c740fe9d
maturity: draft
page_id: pg_a86b56591d7c5d408218ba0dbd4431a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c59cbcaa1c895d1695debca63d455aa7
title: amix/dunk/README.md @ c82459356688
updated_at: '2026-09-14T03:34:16Z'
---

# amix/dunk/README.md @ c82459356688

<!-- rcw:begin owner=source:src_c59cbcaa1c895d1695debca63d455aa7 block=evidence -->
- dunk exports a DunkDiffView component from dunkdiff/opentui so the diff renderer can be embedded in other OpenTUI applications. [@claim:clm_16e079f5acfe6bb64bd02f41e52fe79b9d0113d22d02742b48fd679678db01b4]
- The intended workflow pairs a human reviewer running dunk diff --watch with a coding agent in another terminal: the agent reads comments, fixes code, resolves entries, and the watched diff reloads in place as code and comments change. [@claim:clm_2c095273fbfb88b4109d2437695fdc23559f7163bd0008987f4a9c09ac43c2f3]
- Branch-review base resolution follows an explicit order: the --branch=<ref> flag, then [branch_review] base in .dunk/config.toml, then origin/HEAD, then main/master/trunk fallbacks, with the resolved base shown in the status bar. [@claim:clm_41b168109285f4ce36c520ef4a2f804bc6990ae5b9ce98dbe9ebf79a685b5a07]
- dunk is a hard fork of hunk that keeps the OpenTUI/Pierre diff-viewer foundation while removing the daemon, MCP, and session-broker layers; agent integration flows through the on-disk comments file. [@claim:clm_8664445b26972b0ec469f10cc5ae017773e322c5504d1f6f10ebd61952619f15]
- Review comments are stored in .dunk/comments.json with the file path, hunk anchor line, body, and a context hash so comments survive small nearby edits; the file is meant to stay local and gitignored, and is deleted once the last comment is resolved. [@claim:clm_9f3064bee04729bf4c796e1e78a648cce9ce2c3deebf958eee41190820959691]
- Configuration is read from ~/.config/dunk/config.toml or .dunk/config.toml, with keys for theme, layout mode, watch, exclude_untracked, line_numbers, wrap_lines, and selection_auto_copy; a CLI --watch flag overrides the config watch value. [@claim:clm_a4e2bd97a5beb2a2c38461cf865b1eaa531deb9d7787c6c34e20fc84ee47bdde]
- Comments are hunk-scoped rather than line-scoped: the user picks a hunk with J/K and presses 'a' to comment, and drifted comments surface at the top of the diff (clearable with d/D) instead of getting lost. [@claim:clm_b8399ffe6af39d20a9818d54b9ff307f3fed6597de2ab583009ff85382ce9a56]
- The product builds on the OpenTUI and Pierre (@pierre/diffs) diff-viewer foundation, requires Node.js 18+ and Git, and ships via npm (dunkdiff) with prebuilt macOS and Linux binaries. [@claim:clm_c9081a390d5a93146fc361fe53be3cf4fe312949944ae4d430eed9c8c740fe9d]
<!-- rcw:end owner=source:src_c59cbcaa1c895d1695debca63d455aa7 block=evidence -->

## Researcher notes

