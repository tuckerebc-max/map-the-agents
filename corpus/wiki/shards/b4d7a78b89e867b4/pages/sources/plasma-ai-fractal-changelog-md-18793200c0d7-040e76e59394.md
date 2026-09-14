---
access: public
aliases: []
claim_ids:
- clm_05af5b814a1cbf5c2e845cc41e492577d47cae6367f9d8b4ff8c798e534f746a
- clm_2731eef859ee02b9120860244c4b1c0c7465d362958a6a9d12dc6c8c50b6f958
maturity: draft
page_id: pg_93bfec8da8455b78bf2a040e76e59394
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8065af0adf255028bd9d481965a173ba
title: plasma-ai/fractal/CHANGELOG.md @ 18793200c0d7
updated_at: '2026-09-14T02:31:11Z'
---

# plasma-ai/fractal/CHANGELOG.md @ 18793200c0d7

<!-- rcw:begin owner=source:src_8065af0adf255028bd9d481965a173ba block=evidence -->
- The package installs from PyPI as plasma-fractal (or via the fractal pointer dist); pipx/uv tool installs additionally require installing plasma-wiki, which a plain pip install pulls automatically. [@claim:clm_05af5b814a1cbf5c2e845cc41e492577d47cae6367f9d8b4ff8c798e534f746a]
- 'node stop' waits for the in-flight agent to complete rather than tearing the running seat, and cascades over the target's entire subtree children-first; 'node kill' remains the immediate path and can reap booting spawns. [@claim:clm_2731eef859ee02b9120860244c4b1c0c7465d362958a6a9d12dc6c8c50b6f958]
<!-- rcw:end owner=source:src_8065af0adf255028bd9d481965a173ba block=evidence -->

## Researcher notes

