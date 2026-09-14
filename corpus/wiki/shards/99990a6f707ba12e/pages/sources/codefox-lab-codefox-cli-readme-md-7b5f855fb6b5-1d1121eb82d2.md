---
access: public
aliases: []
claim_ids:
- clm_283f95b00a318f8a9f87b30765e6882540ca3a7282fad85c164f2ffd5918e9c0
- clm_3dcb2265348d48aaf20cbf42c0fb80205c81b2a3ee22178192f6e88bb2d40b76
- clm_4b41872cc74b3cdd194e465d7060119be7b71b40fb127436a0d7f3491c499b46
- clm_790326232abb5c5523f567e39d219b0ffedeaff9b2676a35e131d2769129637a
- clm_aa3bd5cdb417dd33d5c20697b78fc9637600c52a86016c2acfcd80a9fc7b80fb
- clm_b8c3c78c82174558adf84c5c709c2d993c95dd72a7d2405468359489cbdb016b
- clm_bddcabe4e1e06c7aa3522a1051b41015d54d265af12f37239c4b6539661b75a0
maturity: draft
page_id: pg_bc4082432e175c57811a1d1121eb82d2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8fc8adbae2425a21a46085a4f2f80203
title: codefox-lab/CodeFox-CLI/README.md @ 7b5f855fb6b5
updated_at: '2026-09-14T03:41:04Z'
---

# codefox-lab/CodeFox-CLI/README.md @ 7b5f855fb6b5

<!-- rcw:begin owner=source:src_8fc8adbae2425a21a46085a4f2f80203 block=evidence -->
- Repository development practice: bug reports, pull requests, and documentation improvements are welcome, and a Contributor Covenant-based code of conduct governs the community. [@claim:clm_283f95b00a318f8a9f87b30765e6882540ca3a7282fad85c164f2ffd5918e9c0]
- Repository development practice: dev setup installs pytest, mypy, ruff, and types-PyYAML; tests run with 'pytest tests -v', linting via ruff, and type checking via mypy codefox. [@claim:clm_3dcb2265348d48aaf20cbf42c0fb80205c81b2a3ee22178192f6e88bb2d40b76]
- The tool is positioned as a CLI-first diff review tool, explicitly not an IDE coding assistant like Cursor or Claude Code. [@claim:clm_4b41872cc74b3cdd194e465d7060119be7b71b40fb127436a0d7f3491c499b46]
- Configuration uses ./.codefox.yml for model and analysis settings, ./.codefoxignore for excluded paths, and ./codefoxenv for the API token. [@claim:clm_790326232abb5c5523f567e39d219b0ffedeaff9b2676a35e131d2769129637a]
- The scan command collects the current git diff, loads project context, sends a review request to the configured model, and returns review comments with optional fix suggestions. [@claim:clm_aa3bd5cdb417dd33d5c20697b78fc9637600c52a86016c2acfcd80a9fc7b80fb]
- The CLI exposes commands: init, list, scan, version, clean, and --help, per the commands table. [@claim:clm_b8c3c78c82174558adf84c5c709c2d993c95dd72a7d2405468359489cbdb016b]
- Supported providers are Gemini (default), Ollama for local/remote servers, and OpenRouter; Ollama allows fully local reviews. [@claim:clm_bddcabe4e1e06c7aa3522a1051b41015d54d265af12f37239c4b6539661b75a0]
<!-- rcw:end owner=source:src_8fc8adbae2425a21a46085a4f2f80203 block=evidence -->

## Researcher notes

