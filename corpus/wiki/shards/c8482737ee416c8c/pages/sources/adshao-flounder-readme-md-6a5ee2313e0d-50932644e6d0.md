---
access: public
aliases: []
claim_ids:
- clm_19297ec6ba05c9f5cfc3414eadc801aea4623d280ececd53e8237b74caf2ed1f
- clm_3bac6df4dc881f94c3b8ee6d4e9a4e92b6f4b8eb0d84314c6974fab02dde376d
- clm_3dfb7167b74b95d3a06e253d2b9dd2dba6705134f181672214d0b221ef575e40
- clm_541f2c766c9b30d0924308e8155dae2739710f46f440cb9ec5803133b8f17393
- clm_755d4e61039b07d71f4dc4340f0e010907d883680488da0f4a9dffbc41ea021e
- clm_77f15a067e4760369291d98862ba8f48c68e23086de29386187112d5ad7370e0
- clm_78e1d538ff4347db8e484a073c0e57ee0addbbf7b3a7ce206996f7dc21433806
- clm_b3560f1a3f119e2ea1771326c211fdb718ebfdb9208d899fd87e00e87c6db1b9
- clm_b9d00738b8440a3debae05969c6aeb71559d19ee52dec04b3e55224247806b0b
- clm_cf24230463cecc8d68dd3e029e3dcd63fc1a9fffcfa329a1b7bf283d82013982
- clm_e75e6dd772d3236c18b9cbe5b4354b303e7e9b7a23dc02c3aeb12fd2a053b174
- clm_fd77a43e868dfd2fadb6c290e738ebd6ff5e8b812bb485ff922dd847159121ae
maturity: draft
page_id: pg_1d15263a391f55cc8e4f50932644e6d0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ac45032e236a5490a6b26fe328a0de98
title: adshao/flounder/README.md @ 6a5ee2313e0d
updated_at: '2026-09-14T03:31:01Z'
---

# adshao/flounder/README.md @ 6a5ee2313e0d

<!-- rcw:begin owner=source:src_ac45032e236a5490a6b26fe328a0de98 block=evidence -->
- Model-generated commands execute in a sandbox; the default `--sandbox-backend auto` prefers Apple's container runtime on Apple silicon, falls back to Docker-backed OCI, and fails closed if no sandbox engine is ready rather than running on the host. [@claim:clm_19297ec6ba05c9f5cfc3414eadc801aea4623d280ececd53e8237b74caf2ed1f]
- Findings must be execution-grounded: a finding is upgraded only when a cited local command exercises the vulnerable path, with statuses like confirmed-differential, confirmed-executable, suspected, and refuted. [@claim:clm_3bac6df4dc881f94c3b8ee6d4e9a4e92b6f4b8eb0d84314c6974fab02dde376d]
- The framework is deliberately stack-agnostic: it encodes no Solidity, ZK, Rust, Go, or crypto-specific audit strategy; the model decides strategy while Flounder supplies sandbox, command policy, durable state, and reporting. [@claim:clm_3dfb7167b74b95d3a06e253d2b9dd2dba6705134f181672214d0b221ef575e40]
- The white-hat boundary forbids broadcasting transactions, moving funds, submitting writes, persisting access, or targeting systems outside the declared boundary; open-world confirmation is limited to fetch, search, fork, and read. [@claim:clm_541f2c766c9b30d0924308e8155dae2739710f46f440cb9ec5803133b8f17393]
- The tracked workflow runs prepare -> map -> dig -> synthesize -> verify -> confirm -> report, with each phase's purpose documented (e.g. Map enumerates and scores the audit surface without producing findings). [@claim:clm_755d4e61039b07d71f4dc4340f0e010907d883680488da0f4a9dffbc41ea021e]
- Host execution is gated: `--sandbox-backend host --allow-host-execution` or FLOUNDER_ALLOW_HOST_EXECUTION=1 enables it, but host mode cannot enforce network sealing or kernel-level filesystem isolation and is not for untrusted targets. [@claim:clm_77f15a067e4760369291d98862ba8f48c68e23086de29386187112d5ad7370e0]
- The product includes an Evaluations control plane for durable audit, benchmark, regression, and verification run groups, with lifecycle and evidence axes kept separate so a build failure cannot count as a safe control pass. [@claim:clm_78e1d538ff4347db8e484a073c0e57ee0addbbf7b3a7ce206996f7dc21433806]
- The product exposes a CLI with workflow verbs (prepare, run, map, audit, verify, confirm, report), a dashboard via `flounder ui`, a REST API where GET /api returns a self-describing catalog, and pi extension tools like flounder_prepare and flounder_run. [@claim:clm_b3560f1a3f119e2ea1771326c211fdb718ebfdb9208d899fd87e00e87c6db1b9]
- Local state lives under ~/.flounder: a SQLite tracking database (flounder.db), per-run artifact directories, durable history/memory per target, a daemon workspace, and daemon-local provider auth. [@claim:clm_b9d00738b8440a3debae05969c6aeb71559d19ee52dec04b3e55224247806b0b]
- A daemon/control-plane split exists: remote daemons connect with minted tokens (`flounder server daemon-token mint`), providers are authenticated per executor machine, and projects pin to a daemon and provider profile. [@claim:clm_cf24230463cecc8d68dd3e029e3dcd63fc1a9fffcfa329a1b7bf283d82013982]
- Flounder is described as an autonomous white-hat security auditor providing security automation for target prep, audit, exploit construction, and execution proof. [@claim:clm_e75e6dd772d3236c18b9cbe5b4354b303e7e9b7a23dc02c3aeb12fd2a053b174]
- The default sandbox image is described as a baseline, not a promise to cover every target stack; specialized targets should supply a daemon- or operator-provided image with the exact toolchain. [@claim:clm_fd77a43e868dfd2fadb6c290e738ebd6ff5e8b812bb485ff922dd847159121ae]
<!-- rcw:end owner=source:src_ac45032e236a5490a6b26fe328a0de98 block=evidence -->

## Researcher notes

