---
access: public
aliases: []
claim_ids:
- clm_4d5864539bcdf51e95a81c3e778b258bbf1afc348a88eb2603a8c9d83372070a
- clm_d22f21a396d154d7cd6b5b8a43ea95021f04dafe26f5557f0887365651e93db9
maturity: draft
page_id: pg_6f8aa98156175e6883f66e72b672d954
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_32828b59d75e5a61bb5cc62b1fb2bf54
title: continuedev/continue/BUILD_DEPENDENCIES.md @ 5522c6f44ca0
updated_at: '2026-09-14T01:44:07Z'
---

# continuedev/continue/BUILD_DEPENDENCIES.md @ 5522c6f44ca0

<!-- rcw:begin owner=source:src_32828b59d75e5a61bb5cc62b1fb2bf54 block=evidence -->
- The CLI uses `CONTINUE_API_BASE` (defaulting to https://api.continue.dev/) and `CONTINUE_API_KEY` for Continue API authentication, per the repository's build-dependency catalog. [@claim:clm_4d5864539bcdf51e95a81c3e778b258bbf1afc348a88eb2603a8c9d83372070a]
- Repository development practice: CI workflows reference many secrets, including marketplace publishing tokens (VSCE_TOKEN, VSX_REGISTRY_TOKEN), JetBrains signing/notarization credentials, semantic-release npm/GitHub tokens, and AI provider API keys used in PR checks and releases. [@claim:clm_d22f21a396d154d7cd6b5b8a43ea95021f04dafe26f5557f0887365651e93db9]
<!-- rcw:end owner=source:src_32828b59d75e5a61bb5cc62b1fb2bf54 block=evidence -->

## Researcher notes

