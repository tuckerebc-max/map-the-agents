---
access: public
aliases: []
claim_ids:
- clm_55f2c41ecca2f0651e336554e0448c4c81c5ba78cb74a1b39f80aa6dae785844
- clm_56229336c50ba397bb242254f2fbe4cefda45d8c863c4e2a8ec1d030e049f5d9
- clm_5e672a90824e6b18afaa8845da6b8d906e4dd2b188dcfc290d2475f8c1794579
- clm_cd7a1bf6231d79a4a7d502245a606370cbfde2e93d85bfa5efe5f906f364050c
maturity: draft
page_id: pg_fd5f815674a755db91f72943828d7b31
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e74ef1e59e925fa4bc60464136f4f943
title: alibaba/open-code-review/ASSURANCE_CASE.md @ 494bf1c8d7a1
updated_at: '2026-09-14T01:59:22Z'
---

# alibaba/open-code-review/ASSURANCE_CASE.md @ 494bf1c8d7a1

<!-- rcw:begin owner=source:src_e74ef1e59e925fa4bc60464136f4f943 block=evidence -->
- The product optionally serves a local web viewer for browsing review session history; the viewer binds to localhost by default and uses a host-header allowlist (configurable via OCR_VIEWER_ALLOWED_HOSTS) to block DNS rebinding. [@claim:clm_55f2c41ecca2f0651e336554e0448c4c81c5ba78cb74a1b39f80aa6dae785844]
- Security defaults follow fail-safe principles: API keys come only from environment variables and are never logged or written to output files, and LLM responses undergo JSON schema validation with line-number bounds checking. [@claim:clm_56229336c50ba397bb242254f2fbe4cefda45d8c863c4e2a8ec1d030e049f5d9]
- Per the assurance case, agent file paths are validated against the repository root before and after symlink resolution, and external process execution is limited to git with hardcoded subcommands, plus a few user-configured call sites. [@claim:clm_5e672a90824e6b18afaa8845da6b8d906e4dd2b188dcfc290d2475f8c1794579]
- Each review session writes to its own JSONL file with no shared state between sessions, and interrupted reviews can be resumed via `--resume <session-id>`. [@claim:clm_cd7a1bf6231d79a4a7d502245a606370cbfde2e93d85bfa5efe5f906f364050c]
<!-- rcw:end owner=source:src_e74ef1e59e925fa4bc60464136f4f943 block=evidence -->

## Researcher notes

