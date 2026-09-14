---
access: public
aliases: []
claim_ids:
- clm_0376cb9dc1e4e5382f9316a143c5abb01fdd241ae52f39f4aae24c0426d57661
- clm_0cbd08a771b8296897647ddfd461fc3e6888d57b48c7d99de9159ad2aadd9598
- clm_6e22ef057fda910ee0e87b17b2ee20fd68a37cf0429878214ecf9f8f4a44e473
- clm_9fa9a915c32de59faea3bc7abde5774307efafd0cc54a1f1b389fa2352fc5bb5
- clm_ab7e1510af2897fcc01b0870d5de99ed98701b21ec245f46ff92e20ea52ea3e9
- clm_bf256486053b36ff38b0f85aa8e9d829fe29d2a531e09a20927bda49a84ed054
- clm_d2b7cb21345ad8a16acaf4d91a6e01487d384ea065d42a579f3337e120f6fb30
- clm_e571918b9f911e09e41297784035a7abce80eb813e933cfa8f90394559e46b12
maturity: draft
page_id: pg_5060600077165a769ef9273e6281e114
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5254ed58687b593e9bbd66c99f4a2a50
title: Touchpoint-Labs/Gadfly/spec.md @ 2798406b5d27
updated_at: '2026-09-14T04:27:36Z'
---

# Touchpoint-Labs/Gadfly/spec.md @ 2798406b5d27

<!-- rcw:begin owner=source:src_5254ed58687b593e9bbd66c99f4a2a50 block=evidence -->
- An autonomy dial (autonomous, balanced, collaborative) controls how often undiscussed decisions surface to the user; irreversible operations always ask regardless of the setting. [@claim:clm_0376cb9dc1e4e5382f9316a143c5abb01fdd241ae52f39f4aae24c0426d57661]
- Two isolated, read-only supervisors review each action: an Architect (default Opus) catching spec drift and undiscussed decisions, and a Code Reviewer (default Sonnet) catching real defects. [@claim:clm_0cbd08a771b8296897647ddfd461fc3e6888d57b48c7d99de9159ad2aadd9598]
- A deterministic first pass auto-allows reads and safe commands without any model call, so LLM supervisors only engage for consequential actions. [@claim:clm_6e22ef057fda910ee0e87b17b2ee20fd68a37cf0429878214ecf9f8f4a44e473]
- Stated v1 non-goals include no post-hoc QA practitioner, no taskmaster, no full interactive or training mode, no daemon, and no adapters for other agents; supervisors never write code or run commands. [@claim:clm_9fa9a915c32de59faea3bc7abde5774307efafd0cc54a1f1b389fa2352fc5bb5]
- The agent can read the memory files but is denied direct writes to spec.md, claude.md, and decisions.md; those files change only via the human or Gadfly. [@claim:clm_ab7e1510af2897fcc01b0870d5de99ed98701b21ec245f46ff92e20ea52ea3e9]
- Supervision is grounded in five project files: spec.md (human, required), claude.md (human, optional), codemap.md (builder), decisions.md and memory.md (Gadfly-owned), with a defined trust order. [@claim:clm_bf256486053b36ff38b0f85aa8e9d829fe29d2a531e09a20927bda49a84ed054]
- Architecture is a pure, agent- and LLM-agnostic core wrapped by two swappable adapters (host-agent format and LLM provider); supervisors call a provider-neutral client with models set in config. [@claim:clm_d2b7cb21345ad8a16acaf4d91a6e01487d384ea065d42a579f3337e120f6fb30]
- An append-only edit-ledger records agent edits; out-of-band human edits are diffed against them by a separate idle-time extractor that distills generalizable corrections into durable rules. [@claim:clm_e571918b9f911e09e41297784035a7abce80eb813e933cfa8f90394559e46b12]
<!-- rcw:end owner=source:src_5254ed58687b593e9bbd66c99f4a2a50 block=evidence -->

## Researcher notes

