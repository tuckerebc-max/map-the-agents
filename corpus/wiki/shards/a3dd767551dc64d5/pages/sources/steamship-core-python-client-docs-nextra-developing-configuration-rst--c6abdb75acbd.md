---
access: public
aliases: []
claim_ids:
- clm_6102697f93661c6927175ba582af73ed1f6e77450acadcdc40df59cbc1f5fc80
- clm_918d29d190d877c5d04f0ef359ac5f7c0d931809ba166d9854f8186125c01137
- clm_e88ca0424a4007d1da77308888dbc86d1eb06a25c035bfc265b5ad8a6e6dfb71
maturity: draft
page_id: pg_4dfba4ff676558d6b8e2c6abdb75acbd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4166b4860b005808898e487c5e0ec4ca
title: steamship-core/python-client/docs/nextra/developing/configuration.rst @ 62b3f9659fd4
updated_at: '2026-09-14T02:43:24Z'
---

# steamship-core/python-client/docs/nextra/developing/configuration.rst @ 62b3f9659fd4

<!-- rcw:begin owner=source:src_4166b4860b005808898e487c5e0ec4ca block=evidence -->
- Configuration parameters without defaults are mandatory: instance creation fails if the user omits them or supplies a wrong type, so packages receive structurally matching config; there are no optional parameters. [@claim:clm_6102697f93661c6927175ba582af73ed1f6e77450acadcdc40df59cbc1f5fc80]
- Packages and plugins define configuration by subclassing Config with typed fields (boolean, string, or number), a description, and an optional default, returned via a config_cls class method. [@claim:clm_918d29d190d877c5d04f0ef359ac5f7c0d931809ba166d9854f8186125c01137]
- Config values are exposed to package/plugin code via self.config and are automatically populated by Steamship at invocation time. [@claim:clm_e88ca0424a4007d1da77308888dbc86d1eb06a25c035bfc265b5ad8a6e6dfb71]
<!-- rcw:end owner=source:src_4166b4860b005808898e487c5e0ec4ca block=evidence -->

## Researcher notes

