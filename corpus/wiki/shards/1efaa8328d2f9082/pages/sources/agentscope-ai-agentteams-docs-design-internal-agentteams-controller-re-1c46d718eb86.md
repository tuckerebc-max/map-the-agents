---
access: public
aliases: []
claim_ids:
- clm_4897f815bb90c844c68b4e1e38184a56a3c1109b24a4677708c5d674c6d8e6c6
- clm_b8704347047e463dd3187992c90c92b5d3cdbc3f7b393bab11d5c84481f5a1a3
maturity: draft
page_id: pg_f34a809bd2995651a9871c46d718eb86
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_16b0962d5925536dae9f69f37e20b85e
title: agentscope-ai/AgentTeams/docs/design/internal/agentteams-controller-refactor.md
  @ f65d6e1af268
updated_at: '2026-09-14T01:31:19Z'
---

# agentscope-ai/AgentTeams/docs/design/internal/agentteams-controller-refactor.md @ f65d6e1af268

<!-- rcw:begin owner=source:src_16b0962d5925536dae9f69f37e20b85e block=evidence -->
- The refactor design gives Team Leaders heartbeat-based worker lifecycle management (wake/sleep, idle timeout) with controller-enforced permission isolation: leaders may only manage workers of their own team, and workers cannot manage other workers. [@claim:clm_4897f815bb90c844c68b4e1e38184a56a3c1109b24a4677708c5d674c6d8e6c6]
- The design targets two deployment modes: K8s incluster via Helm, and backward-compatible embedded mode where the controller manages worker containers through the Docker socket and runs an embedded kube-apiserver plus kine (SQLite) as a K8s API compatibility layer. [@claim:clm_b8704347047e463dd3187992c90c92b5d3cdbc3f7b393bab11d5c84481f5a1a3]
<!-- rcw:end owner=source:src_16b0962d5925536dae9f69f37e20b85e block=evidence -->

## Researcher notes

