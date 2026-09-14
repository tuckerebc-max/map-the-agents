---
access: public
aliases: []
claim_ids:
- clm_2c4f5657f926b0d8587c99ff25c11ef08b959c6e2af1641c2ab0b1cfe4849d42
- clm_64995ba91e0cfddc951404233511f0b11cb53da4b5972692b22b337e8b30e6d6
- clm_6d89d3aa8ebdbd1f4a057a1a098d05d3c6fd97d75d016fb584c80a29fb2989ac
- clm_95d91e9bdd23f93ed0d1357e3367f872766d741981e2f487a1c59fd5aee0df64
- clm_f77e93194bca2d26a0a0bb68a939caeb6084a33c3c6bc7c6d3c077a86bb95328
maturity: draft
page_id: pg_5a35f740a4f950d49d1515060558b414
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2af4acfd73f952daa1d0ade3ed316e28
title: chaitin/MonkeyCode/CONTEXT.md @ a67aef068778
updated_at: '2026-09-14T01:39:55Z'
---

# chaitin/MonkeyCode/CONTEXT.md @ a67aef068778

<!-- rcw:begin owner=source:src_2af4acfd73f952daa1d0ade3ed316e28 block=evidence -->
- Users are organized in a tree expanding from a unique root group; group authorization covers descendant groups, and quotas inherit from the nearest parent group when unset. [@claim:clm_2c4f5657f926b0d8587c99ff25c11ef08b959c6e2af1641c2ab0b1cfe4849d42]
- The MonkeyAI admin console manages user identity, AI resources, session usage, credit billing, and admin audit within a single instance, explicitly without multi-tenancy. [@claim:clm_64995ba91e0cfddc951404233511f0b11cb53da4b5972692b22b337e8b30e6d6]
- Billing uses an internal credit unit with per-cycle quotas, credit accounts, and immutable ledger records for deductions, grants, refunds, resets, and manual adjustments. [@claim:clm_6d89d3aa8ebdbd1f4a057a1a098d05d3c6fd97d75d016fb584c80a29fb2989ac]
- AI resources include models, skills, rules, MCP services, individually toggleable MCP tools, and Experts (system-level agent presets combining role prompts, MCP tools, rules, and skills). [@claim:clm_95d91e9bdd23f93ed0d1357e3367f872766d741981e2f487a1c59fd5aee0df64]
- Resource sharing supports read-only and read-write levels; read-write excludes sharing, deletion, or ownership transfer, and system rules can be forced onto target users or groups. [@claim:clm_f77e93194bca2d26a0a0bb68a939caeb6084a33c3c6bc7c6d3c077a86bb95328]
<!-- rcw:end owner=source:src_2af4acfd73f952daa1d0ade3ed316e28 block=evidence -->

## Researcher notes

