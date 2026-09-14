---
access: public
aliases: []
claim_ids:
- clm_0c80a46056aec90c887962663eb117275288b568e1b63f27f87c879813995a53
- clm_39f29d021fe53d75d1fbf63f98aefd0da98544a82f616f291dd9b957ea17659a
- clm_a7cdae4ec2134903d7234aee4c6c6b2ed3b05331c292212b4154e1b2c1952088
- clm_b3675f3d00a4347391610dd9563ff390ec30845ff2261464da3dc18a400df504
- clm_cf0b98befba12dcf131c8b19b71e45bf94eb40028c21ca31a9eaa4168b12cf4b
- clm_d535373a82465b57b854512d9094172028f7d24f96a0abdc3c882f983b4ef1af
- clm_db344ba69b818fe8a89da5de9a96c3e7d701b4e42a91a40f706cdd60449a730c
- clm_f8231f521c334c5e98ee8a021ecb07ab70e823a923b3271ffac70bda32b1bfea
maturity: draft
page_id: pg_55f373b1e9eb5d7c8e6deea8e81d10a3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_651b7edb07565b6eaae257d702831efa
title: hofstadter-io/hof/README.md @ 52feda8ce076
updated_at: '2026-09-14T03:57:29Z'
---

# hofstadter-io/hof/README.md @ 52feda8ce076

<!-- rcw:begin owner=source:src_651b7edb07565b6eaae257d702831efa block=evidence -->
- Repository development practice: contributors build the binary with 'make build', run tests with 'make test', and serve docs locally with 'make docs-serve'. [@claim:clm_0c80a46056aec90c887962663eb117275288b568e1b63f27f87c879813995a53]
- hof is built on CUE, which the project treats as the language for schemas, configuration, and declarative sources of truth, powering both developer experience and implementation. [@claim:clm_39f29d021fe53d75d1fbf63f98aefd0da98544a82f616f291dd9b957ea17659a]
- Core features include technology-agnostic code generation from data plus templates, evolvable data models with checkpoint and diff support, an extensible DAG task engine based on cue/flow, and LLM-assisted chat combined with code generation. [@claim:clm_a7cdae4ec2134903d7234aee4c6c6b2ed3b05331c292212b4154e1b2c1952088]
- The repository is organized around a Go CLI entrypoint (cmd/hof), core logic in lib/, a CUE-based task engine in flow/, docs site source, and CI scripts. [@claim:clm_b3675f3d00a4347391610dd9563ff390ec30845ff2261464da3dc18a400df504]
- hof exposes two interfaces: a CLI suited to scripting and automation, and a TUI for exploring and designing, the latter with a built-in help system. [@claim:clm_cf0b98befba12dcf131c8b19b71e45bf94eb40028c21ca31a9eaa4168b12cf4b]
- The CLI offers main commands including chat, create, datamodel, def, eval, export, flow, fmt, gen, mod, tui, and vet, plus additional commands like update, version, completion, and feedback. [@claim:clm_d535373a82465b57b854512d9094172028f7d24f96a0abdc3c882f983b4ef1af]
- Repository development practice: contributions follow a standard fork, pull request, and review process with labels organizing issues and PRs; the project follows the CNCF Code of Conduct. [@claim:clm_db344ba69b818fe8a89da5de9a96c3e7d701b4e42a91a40f706cdd60449a730c]
- hof is relevant to teams wanting schema-driven, deterministic or agentic code generation, data model management, and CUE-based workflow orchestration from a single CLI tool. [@claim:clm_f8231f521c334c5e98ee8a021ecb07ab70e823a923b3271ffac70bda32b1bfea]
<!-- rcw:end owner=source:src_651b7edb07565b6eaae257d702831efa block=evidence -->

## Researcher notes

