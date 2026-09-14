---
access: public
aliases: []
claim_ids:
- clm_16169b53e2cc0e4832f4a8f9eee939ee0aa5b6f4c8d37ddc2a7e78cae1340972
- clm_2cb762dd951f0df0bc2aa614f13ca8aa4c7feaf13a95ec1136cdf1683d910641
maturity: draft
page_id: pg_71c1b5ba40585300afd4d3eda87cf2ba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c2d21531c29051979a0326fc4156b243
title: kenn-io/kata/docs/design/autostart-idle-shutdown.md @ f41a33383aba
updated_at: '2026-09-14T04:02:20Z'
---

# kenn-io/kata/docs/design/autostart-idle-shutdown.md @ f41a33383aba

<!-- rcw:begin owner=source:src_c2d21531c29051979a0326fc4156b243 block=evidence -->
- Clients auto-start a local daemon when none is reachable; an autostart_idle_timeout lets such a narrowly scoped daemon exit after foreground use stops, while explicit daemons remain long-running. [@claim:clm_16169b53e2cc0e4832f4a8f9eee939ee0aa5b6f4c8d37ddc2a7e78cae1340972]
- On an idle-enabled auto-start daemon, scheduled work is opportunistic: timers do not keep the process resident, so continuous sync, federation, timed claims, embeddings, or hooks need an explicit service-managed daemon. [@claim:clm_2cb762dd951f0df0bc2aa614f13ca8aa4c7feaf13a95ec1136cdf1683d910641]
<!-- rcw:end owner=source:src_c2d21531c29051979a0326fc4156b243 block=evidence -->

## Researcher notes

