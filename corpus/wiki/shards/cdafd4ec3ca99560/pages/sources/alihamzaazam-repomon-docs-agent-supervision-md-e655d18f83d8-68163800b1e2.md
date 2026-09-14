---
access: public
aliases: []
claim_ids:
- clm_0c93d16ffc6c42fa8cf73a911418a0b992c8f7b8034f7383dba3350375d9c919
- clm_0d9583528c0eb2effcd94126de2120503c10542ba6e69be3ffcbfa9117777403
- clm_441fa662b21ce733bb38dd8462d6e533adc012ee6712f76cff3829b152b497a3
- clm_6cb0005c4f3bbe77e2cb89d994ccb59743ee7f108488d2f602832152233747f1
- clm_95053e1125715e34605a2c8e58ce8c0483e90e29a7b70e1ba5280aadf078fed3
- clm_bbc6ea2fa91e6b90bdd70dd3b8b41d2cf8944fc73499770c312450d8921cfdd9
maturity: draft
page_id: pg_c818bb2b86ed5013b0a668163800b1e2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8da6221407295cef9e079f0870952adf
title: AliHamzaAzam/repomon/docs/agent-supervision.md @ e655d18f83d8
updated_at: '2026-09-14T01:59:20Z'
---

# AliHamzaAzam/repomon/docs/agent-supervision.md @ e655d18f83d8

<!-- rcw:begin owner=source:src_8da6221407295cef9e079f0870952adf block=evidence -->
- Default supervision policy auto-approves only repo-scoped command_exec and file_write dialogs; network, credential, deletion, push, install, device, and unknown classes default to hold, and nothing auto-denies out of the box. [@claim:clm_0c93d16ffc6c42fa8cf73a911418a0b992c8f7b8034f7383dba3350375d9c919]
- A hardcoded always-escalate veto (force pushes, rm -rf-shaped deletions, git reset --hard, git clean -f, sudo rm) overrides any policy, including explicit auto_approve mappings and learned rules. [@claim:clm_0d9583528c0eb2effcd94126de2120503c10542ba6e69be3ffcbfa9117777403]
- supervision.set is deliberately excluded from the remote WebSocket bridge allowlist, so granting auto-approval authority is a local-only decision; agents' MCP tools are read-only with no approval power. [@claim:clm_441fa662b21ce733bb38dd8462d6e533adc012ee6712f76cff3829b152b497a3]
- Supervision is off by default globally and per lane; enabling requires both the master switch in config.toml and an enabled lane policy, with the master switch overriding every lane. [@claim:clm_6cb0005c4f3bbe77e2cb89d994ccb59743ee7f108488d2f602832152233747f1]
- Every supervision action or skipped action writes exactly one row to a durable supervision_log SQLite table recording trigger, decision, keys sent, outcome, and pane excerpt. [@claim:clm_95053e1125715e34605a2c8e58ce8c0483e90e29a7b70e1ba5280aadf078fed3]
- Supervision methods live under a `supervision.*` JSON-RPC namespace (get, set, audit, status, nudge) on the local daemon socket. [@claim:clm_bbc6ea2fa91e6b90bdd70dd3b8b41d2cf8944fc73499770c312450d8921cfdd9]
<!-- rcw:end owner=source:src_8da6221407295cef9e079f0870952adf block=evidence -->

## Researcher notes

