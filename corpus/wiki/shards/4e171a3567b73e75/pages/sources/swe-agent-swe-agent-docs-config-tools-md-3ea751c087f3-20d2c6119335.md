---
access: public
aliases: []
claim_ids:
- clm_067eb2c8014a11d047985bcfee103453e823e2032d7943c8f2b8b103657f6cb5
- clm_0c956de854f8cbabd045791f03675d66251abc1fb1bb9055d34eda330edbe0b8
maturity: draft
page_id: pg_ebe9286bde235af1ae6420d2c6119335
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3ed4e6b3352552d19bc4a4a9b495cac5
title: SWE-agent/SWE-agent/docs/config/tools.md @ 3ea751c087f3
updated_at: '2026-09-14T03:16:49Z'
---

# SWE-agent/SWE-agent/docs/config/tools.md @ 3ea751c087f3

<!-- rcw:begin owner=source:src_3ed4e6b3352552d19bc4a4a9b495cac5 block=evidence -->
- Agent tools are organized into tool bundles, each a folder containing bin/ executables, a config.yaml, install.sh, README.md and pyproject.toml; typical tools include bash, code inspection, and editors. [@claim:clm_067eb2c8014a11d047985bcfee103453e823e2032d7943c8f2b8b103657f6cb5]
- A special 'state' command runs after every action and returns a JSON string (e.g. current working directory and open file) that is parsed and used to format prompt templates. [@claim:clm_0c956de854f8cbabd045791f03675d66251abc1fb1bb9055d34eda330edbe0b8]
<!-- rcw:end owner=source:src_3ed4e6b3352552d19bc4a4a9b495cac5 block=evidence -->

## Researcher notes

