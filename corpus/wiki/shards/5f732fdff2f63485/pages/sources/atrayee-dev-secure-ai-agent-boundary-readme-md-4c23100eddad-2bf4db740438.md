---
access: public
aliases: []
claim_ids:
- clm_001604271bdae2a9af449ffe9b1217b0ec65c65f9ebbbc3dc9c934533268fff1
- clm_064297d1f673aee996b989a02163d9e296554c50057dc4d65890217de91c79d3
- clm_277a71ec135d91e705431fac4a18cd068217db1fd5990249f7852b76325ac122
- clm_34b9b311a6ef775190fb0be996c219f21bf56cc61a471842843eda038f403b0d
- clm_3d7a05b84c717a4173ee472f4097b1d885163265179f1c4dad51c5e080c4342b
- clm_7ddbe2efa17f631cbc88fe30dcda9258170a684ac38587de544c4886cef2840d
- clm_9cd113858aebf4b2f6ac0392362c0c8383ae29dba1ad398344a60334768cacde
- clm_ac1b5cda3007c5e6fee52cd8c10e1b8db36c243f8bbdd1acc3a774b012105c76
- clm_cdf9165a326ce97d1c3437735199293e95d8b49efe3a9c77eaa75d1a79d9acd4
- clm_d41f32b73134ab69bde4227b6b64838d1a633ac7b5b7be78c9ced7693ae07189
- clm_dc203cdfaec97747e1029fdc095126ff4ece85270009e76edba74d593ad69251
maturity: draft
page_id: pg_42c2126a44f15296b6222bf4db740438
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f7df6f4e7f27556a9bb945bea9de1d99
title: Atrayee-dev/secure-ai-agent-boundary/README.md @ 4c23100eddad
updated_at: '2026-09-14T03:36:02Z'
---

# Atrayee-dev/secure-ai-agent-boundary/README.md @ 4c23100eddad

<!-- rcw:begin owner=source:src_f7df6f4e7f27556a9bb945bea9de1d99 block=evidence -->
- The project targets organizations integrating frontier AI or local LLMs into engineering workflows that must avoid leaking proprietary code or secrets to model endpoints. [@claim:clm_001604271bdae2a9af449ffe9b1217b0ec65c65f9ebbbc3dc9c934533268fff1]
- The tool is described as editor-agnostic, integrating with any tool that can run a CLI command before and after an edit or any IDE extension supporting LSP-like hook callbacks. [@claim:clm_064297d1f673aee996b989a02163d9e296554c50057dc4d65890217de91c79d3]
- The framework is positioned as a decoupled configuration layer requiring no daemon, kernel patching, or heavyweight control plane, overlaying an existing Git workflow. [@claim:clm_277a71ec135d91e705431fac4a18cd068217db1fd5990249f7852b76325ac122]
- CodeBoundary is described as a zero-trust compartment model in which each third-party model runs in an ephemeral container with strictly bounded data exposure, rather than sharing context across a common environment. [@claim:clm_34b9b311a6ef775190fb0be996c219f21bf56cc61a471842843eda038f403b0d]
- The core mechanism is a data-boundary contract: a YAML/JSON configuration stored with the source that defines scope, redaction rules, visibility level, and output filters for model sessions. [@claim:clm_3d7a05b84c717a4173ee472f4097b1d885163265179f1c4dad51c5e080c4342b]
- The README explicitly disclaims that the software is a security enhancement, not a guarantee: it cannot prevent all leakage such as side-channel attacks or undocumented model behaviors, and authors disclaim liability for data exfiltration. [@claim:clm_7ddbe2efa17f631cbc88fe30dcda9258170a684ac38587de544c4886cef2840d]
- The primary entry point is a .codeboundary.yml file at the repository root, defining a default contract, an allowed-models list with names and fingerprints, and an audit log destination such as a local .cb-audit/ directory. [@claim:clm_9cd113858aebf4b2f6ac0392362c0c8383ae29dba1ad398344a60334768cacde]
- Hybrid sessions route low-sensitivity tasks to a fast local model and high-complexity tasks to a frontier API under one contract, with context stripped and rehydrated between models. [@claim:clm_ac1b5cda3007c5e6fee52cd8c10e1b8db36c243f8bbdd1acc3a774b012105c76]
- The architecture uses a 'diplomat's pouch' metaphor: the engineer declares contract contents, the model receives only declared data, and output stays sealed until the engineer unseals it; extra context requests are logged as boundary violation attempts. [@claim:clm_cdf9165a326ce97d1c3437735199293e95d8b49efe3a9c77eaa75d1a79d9acd4]
- Each model invocation runs in an isolated context bubble that starts clean, and model output goes to a staging area rather than the working tree until an engineer explicitly approves it. [@claim:clm_d41f32b73134ab69bde4227b6b64838d1a633ac7b5b7be78c9ced7693ae07189]
- The boundary engine is language-aware, claiming syntax-tree understanding for 12+ languages including Python, TypeScript, Rust, Go, Java, C#, C++, Ruby, PHP, Swift, Kotlin, and Shell. [@claim:clm_dc203cdfaec97747e1029fdc095126ff4ece85270009e76edba74d593ad69251]
<!-- rcw:end owner=source:src_f7df6f4e7f27556a9bb945bea9de1d99 block=evidence -->

## Researcher notes

