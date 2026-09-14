---
access: public
aliases: []
claim_ids:
- clm_0376cb9dc1e4e5382f9316a143c5abb01fdd241ae52f39f4aae24c0426d57661
- clm_0cbd08a771b8296897647ddfd461fc3e6888d57b48c7d99de9159ad2aadd9598
- clm_2b5fca4fbdb8f61b809b951035372c2ae3c4e8d8a38433bd8551ab5727e836ea
- clm_6e22ef057fda910ee0e87b17b2ee20fd68a37cf0429878214ecf9f8f4a44e473
- clm_882b5a009d20356626caeca0fce2ef4dea0809cb8f0957a34a4b5c2818a6f74e
- clm_ab7e1510af2897fcc01b0870d5de99ed98701b21ec245f46ff92e20ea52ea3e9
- clm_b4ccc116b835aebcec2404e3f20b46b41253febeaa4e61885b1a909b70420d37
- clm_bf256486053b36ff38b0f85aa8e9d829fe29d2a531e09a20927bda49a84ed054
- clm_d2b7cb21345ad8a16acaf4d91a6e01487d384ea065d42a579f3337e120f6fb30
- clm_d62a014318873671a1dfa88b3cdb168357da3e9f8df32c2eb7e4ff12429dbd5e
- clm_e571918b9f911e09e41297784035a7abce80eb813e933cfa8f90394559e46b12
maturity: draft
page_id: pg_cf3f573f6be957af8128eb138a2c13e0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f6eb8d6767735207bb507b7ed060384d
title: Touchpoint-Labs/Gadfly/README.md @ 2798406b5d27
updated_at: '2026-09-14T04:27:36Z'
---

# Touchpoint-Labs/Gadfly/README.md @ 2798406b5d27

<!-- rcw:begin owner=source:src_f6eb8d6767735207bb507b7ed060384d block=evidence -->
- An autonomy dial (autonomous, balanced, collaborative) controls how often undiscussed decisions surface to the user; irreversible operations always ask regardless of the setting. [@claim:clm_0376cb9dc1e4e5382f9316a143c5abb01fdd241ae52f39f4aae24c0426d57661]
- Two isolated, read-only supervisors review each action: an Architect (default Opus) catching spec drift and undiscussed decisions, and a Code Reviewer (default Sonnet) catching real defects. [@claim:clm_0cbd08a771b8296897647ddfd461fc3e6888d57b48c7d99de9159ad2aadd9598]
- CLI commands include gadfly init (requires spec.md), status, config, disable/enable, and uninstall; configuration lives in gadfly.toml with optional keys and defaults. [@claim:clm_2b5fca4fbdb8f61b809b951035372c2ae3c4e8d8a38433bd8551ab5727e836ea]
- A deterministic first pass auto-allows reads and safe commands without any model call, so LLM supervisors only engage for consequential actions. [@claim:clm_6e22ef057fda910ee0e87b17b2ee20fd68a37cf0429878214ecf9f8f4a44e473]
- Gadfly is a Socratic supervision layer that sits inside an AI coding agent's live tool-call loop, questioning consequential moves before they happen. [@claim:clm_882b5a009d20356626caeca0fce2ef4dea0809cb8f0957a34a4b5c2818a6f74e]
- The agent can read the memory files but is denied direct writes to spec.md, claude.md, and decisions.md; those files change only via the human or Gadfly. [@claim:clm_ab7e1510af2897fcc01b0870d5de99ed98701b21ec245f46ff92e20ea52ea3e9]
- Reviews produce four verdicts: silent allow, a question sent back to the agent, a surface that pauses and asks the user, and a block on spec-violating or buggy actions. [@claim:clm_b4ccc116b835aebcec2404e3f20b46b41253febeaa4e61885b1a909b70420d37]
- Supervision is grounded in five project files: spec.md (human, required), claude.md (human, optional), codemap.md (builder), decisions.md and memory.md (Gadfly-owned), with a defined trust order. [@claim:clm_bf256486053b36ff38b0f85aa8e9d829fe29d2a531e09a20927bda49a84ed054]
- Architecture is a pure, agent- and LLM-agnostic core wrapped by two swappable adapters (host-agent format and LLM provider); supervisors call a provider-neutral client with models set in config. [@claim:clm_d2b7cb21345ad8a16acaf4d91a6e01487d384ea065d42a579f3337e120f6fb30]
- The project advertises zero dependencies, targets Python 3.11+, is MIT licensed, and in v1 supervises only Claude Code, running on the user's existing subscription without an API key. [@claim:clm_d62a014318873671a1dfa88b3cdb168357da3e9f8df32c2eb7e4ff12429dbd5e]
- An append-only edit-ledger records agent edits; out-of-band human edits are diffed against them by a separate idle-time extractor that distills generalizable corrections into durable rules. [@claim:clm_e571918b9f911e09e41297784035a7abce80eb813e933cfa8f90394559e46b12]
<!-- rcw:end owner=source:src_f6eb8d6767735207bb507b7ed060384d block=evidence -->

## Researcher notes

