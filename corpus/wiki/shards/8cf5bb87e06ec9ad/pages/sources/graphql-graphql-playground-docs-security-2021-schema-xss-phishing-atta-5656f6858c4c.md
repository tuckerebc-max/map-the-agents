---
access: public
aliases: []
claim_ids:
- clm_274c2197b0b289771ea55ccbbc7f8b863db8423592e9d83dc70f78115556b852
maturity: draft
page_id: pg_ef8eaaf11bd3580685b55656f6858c4c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e4f4e85133105009b4fc6d8d8cbf1307
title: graphql/graphql-playground/docs/security/2021-schema-xss-phishing-attack.md
  @ 05861783f778
updated_at: '2026-09-14T03:55:02Z'
---

# graphql/graphql-playground/docs/security/2021-schema-xss-phishing-attack.md @ 05861783f778

<!-- rcw:begin owner=source:src_e4f4e85133105009b4fc6d8d8cbf1307 block=evidence -->
- graphql-playground-react versions before 1.7.28 are vulnerable to XSS via compromised introspection responses or malicious schema prop type names, exploitable on autocomplete; 1.7.28 fixes it via HTML escaping and schema validation. [@claim:clm_274c2197b0b289771ea55ccbbc7f8b863db8423592e9d83dc70f78115556b852]
<!-- rcw:end owner=source:src_e4f4e85133105009b4fc6d8d8cbf1307 block=evidence -->

## Researcher notes

