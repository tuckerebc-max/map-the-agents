---
access: public
aliases: []
claim_ids:
- clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26
- clm_7f7b6605c571d369fa524101d1df8ae9f1b2a6d10f929c62895d4780b44a69ef
maturity: draft
page_id: pg_44aeb3da09bd5e8491d69f8b9bb4fb2d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f0da4b17648057c28619e11006e8f9cf
title: sondera-ai/sondera-coding-agent-hooks/docs/getting-started.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/docs/getting-started.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_f0da4b17648057c28619e11006e8f9cf block=evidence -->
- Trajectories persist in a Turso (SQLite) store defaulting to ~/.sondera/trajectories/trajectories.db, overridable via --db; the console reads agents and trajectories from the same store. [@claim:clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26]
- `sondera serve` runs two gRPC surfaces on one address: `sondera.harness.v1` for Cedar-backed adjudication and `sondera.console.v1` for agent and trajectory reads over the same store. [@claim:clm_7f7b6605c571d369fa524101d1df8ae9f1b2a6d10f929c62895d4780b44a69ef]
<!-- rcw:end owner=source:src_f0da4b17648057c28619e11006e8f9cf block=evidence -->

## Researcher notes

