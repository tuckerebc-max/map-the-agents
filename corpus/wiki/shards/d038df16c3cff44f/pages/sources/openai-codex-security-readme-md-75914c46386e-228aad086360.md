---
access: public
aliases: []
claim_ids:
- clm_47b50309adebda75fb9fc8a606567e889b95406e9565faf4757cce5d24a50888
- clm_8231562a344e80320068977e13af1913161345bed4c613decfa278fab6631769
- clm_8a0fc9831562973ae8549085492350895a3737bb5a1e172577c5e6b51cdc1fc6
- clm_c9debfacb60ec1a1b56f75fa257fbb2a436596415e251c5e30a1cb6c969b8b43
- clm_e7431597e8b814377aa9179a759376552573e5b742a70641f2783c2eb4d0ebdb
maturity: draft
page_id: pg_44b4f64c5f8555e6a8fe228aad086360
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9b22d7c956425666a855a4dc95bd72e3
title: openai/codex-security/README.md @ 75914c46386e
updated_at: '2026-09-14T03:11:02Z'
---

# openai/codex-security/README.md @ 75914c46386e

<!-- rcw:begin owner=source:src_9b22d7c956425666a855a4dc95bd72e3 block=evidence -->
- The product ships as a CLI and TypeScript SDK; the SDK exposes a CodexSecurity class with run() accepting options like mode, workers, subagents, and maxTimeHours, plus a close() method. [@claim:clm_47b50309adebda75fb9fc8a606567e889b95406e9565faf4757cce5d24a50888]
- A findings service (preview) runs from the same ghcr.io/openai/codex-security image, stores findings and embeddings in SQLite, serves a read-only /dashboard refreshing every five seconds, and returns duplicate candidates by embedding similarity. [@claim:clm_8231562a344e80320068977e13af1913161345bed4c613decfa278fab6631769]
- The tool requires Node.js 22.13.0 or later and Python 3.10 or later, and is installed via npm as @openai/codex-security. [@claim:clm_8a0fc9831562973ae8549085492350895a3737bb5a1e172577c5e6b51cdc1fc6]
- Alternative inference providers are supported via --provider with documented examples for amazon-bedrock, openrouter, and fireworks, each using its own API-key environment variable. [@claim:clm_c9debfacb60ec1a1b56f75fa257fbb2a436596415e251c5e30a1cb6c969b8b43]
- The policy command drafts SECURITY.md guidance outside the checkout without installing it or scanning, and supporting architecture or threat-model documents are kept outside the repository. [@claim:clm_e7431597e8b814377aa9179a759376552573e5b742a70641f2783c2eb4d0ebdb]
<!-- rcw:end owner=source:src_9b22d7c956425666a855a4dc95bd72e3 block=evidence -->

## Researcher notes

