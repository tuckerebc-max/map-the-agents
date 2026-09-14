---
access: public
aliases: []
claim_ids:
- clm_3ebecac6d2c2ef8b24fdad97feae964bc5f1f9d5f2bb8fca855285e3a2a5899f
- clm_5f074ab5b4c50963369dcd51fc8e9853f5571046eb318299442ed63cfdff038e
- clm_6f5411b8c7a55f2cf10ddaf47c3f2a726f7e2e064f1c513f8c7aefbd6ddb9e6a
- clm_85b8d7c10e6cdeff1f76449391c3adc777b5bb21bb6ba95008d87c03e8a9178b
- clm_8e621931587e82991be770db96578a73805046d928f621a3aa1aca5ce56e4ee7
maturity: draft
page_id: pg_912e69b7f1235239bed389e58c6be0a4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b5b6b389adf9566c940070ab77081194
title: talmetis-labs/aizen/docs/SANDBOX.md @ 997bdd3bbba4
updated_at: '2026-09-14T04:25:49Z'
---

# talmetis-labs/aizen/docs/SANDBOX.md @ 997bdd3bbba4

<!-- rcw:begin owner=source:src_b5b6b389adf9566c940070ab77081194 block=evidence -->
- Approval (ask/smart/yolo plus a cmd_guard hard floor) is separate from the sandbox: even approved commands get no secrets, no network, and no out-of-workspace writes where kernel backends exist. [@claim:clm_3ebecac6d2c2ef8b24fdad97feae964bc5f1f9d5f2bb8fca855285e3a2a5899f]
- Sandbox modes are auto (default), strict, guarded, and off; strict refuses spawns rather than downgrading, and unattended runs fail closed unless sandbox.allow_guarded_fallback is true. [@claim:clm_5f074ab5b4c50963369dcd51fc8e9853f5571046eb318299442ed63cfdff038e]
- The sandbox runs commands without inheriting API keys, denies network by default, and enforces filesystem policy via Landlock+seccomp on Linux and Seatbelt on macOS; Windows uses Job-Object containment and reports 'partial'. [@claim:clm_6f5411b8c7a55f2cf10ddaf47c3f2a726f7e2e064f1c513f8c7aefbd6ddb9e6a]
- The sandbox code is organized under src/sandbox with modules for policy, capabilities, a single runner that builds sandboxed commands, audit logging, and per-platform backends (guarded, linux, windows, macos). [@claim:clm_85b8d7c10e6cdeff1f76449391c3adc777b5bb21bb6ba95008d87c03e8a9178b]
- The sandbox explicitly does not protect against kernel exploits, an already-compromised user account or machine, secrets placed inside the workspace, or a human approving a harmful command. [@claim:clm_8e621931587e82991be770db96578a73805046d928f621a3aa1aca5ce56e4ee7]
<!-- rcw:end owner=source:src_b5b6b389adf9566c940070ab77081194 block=evidence -->

## Researcher notes

