---
access: public
aliases: []
claim_ids:
- clm_065f2fe477a18683bce6f91d9a58df7e4fa9e1f865d7b3d715ea1823dd1dd085
- clm_1c50d5a0b542952087f765f2d08359e99c69a7f20db29f7786ad6d65ee7cf463
- clm_2f6e4ed21fe4740b106ff75adc7cfaf94200325c793442e6835caac4b0afa56b
- clm_4487cb3d0b9c46823931d6da034bedda3370f0ef42f8b51e41df96cb30944dfa
- clm_65c69b9d8c0b6a1ca9722907e644442d7645ad39a8242fe08bfaca3f5f36504b
- clm_7e7429d39d5824217c3c5522aecdd1ad5e1cf43414c23621966a5af0faaf5129
- clm_7fb3923df2fd1b7b5ae8fa22654da66957d938d8fd53d35ec51545b4ac3ad5cc
- clm_9fd792a930f63d154ac48393eb5a42389b2fd4925b49c959d2e4c000b006deea
- clm_bc05466cf9f537bf91f1aaed05978117d6b15f6ff52d762484349a3b989231e9
maturity: draft
page_id: pg_a8a0884bbcca5ba482332ae7ae2e4c7b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e744b8d896d35341bc34a342fa2260a3
title: spikonado/sprocket/ARCHITECTURE.md @ f705b4375ade
updated_at: '2026-09-14T02:42:13Z'
---

# spikonado/sprocket/ARCHITECTURE.md @ f705b4375ade

<!-- rcw:begin owner=source:src_e744b8d896d35341bc34a342fa2260a3 block=evidence -->
- Agent runs use idempotent creation keyed by a submission identifier, renewable run claims that reject stale workers, durable tool-job records taken before and after execution, and cancellation propagated from durable state to local operations. [@claim:clm_065f2fe477a18683bce6f91d9a58df7e4fa9e1f865d7b3d715ea1823dd1dd085]
- State is split by owner: Convex holds users, threads, durable transcript parts, runs, and tool-job records, while the local server keeps a thread summary cache, transcript replica, folder list, and pairing credentials; the WorkOS refresh token lives in the OS credential store. [@claim:clm_1c50d5a0b542952087f765f2d08359e99c69a7f20db29f7786ad6d65ee7cf463]
- Workspace patches and shell commands are not sandboxed; they run with the permissions of the local Sprocket process and are confined only by the OS user. [@claim:clm_2f6e4ed21fe4740b106ff75adc7cfaf94200325c793442e6835caac4b0afa56b]
- The product depends on an external private AI gateway (spikonado/ai-gateway) at https://ai-gateway.spikonado.com for model routing and quota checks, plus Convex and WorkOS AuthKit for state and identity. [@claim:clm_4487cb3d0b9c46823931d6da034bedda3370f0ef42f8b51e41df96cb30944dfa]
- The system has three planes: a Svelte/Electron/CLI client plane, a local Rust execution plane that authenticates requests and runs tools, and a Convex cloud coordination plane with an AI gateway for completions. [@claim:clm_65c69b9d8c0b6a1ca9722907e644442d7645ad39a8242fe08bfaca3f5f36504b]
- Artifact-bound files must be UTF-8 text within 500,000 bytes; missing or unreadable files report an error while keeping their last readable content, and the server does not recreate missing files from the cloud copy. [@claim:clm_7e7429d39d5824217c3c5522aecdd1ad5e1cf43414c23621966a5af0faaf5129]
- Artifact tools include add_artifact, edit_artifact, list_artifacts, and save_artifact; save_artifact accepts an existing file only when its content is identical and never overwrites differing content. [@claim:clm_7fb3923df2fd1b7b5ae8fa22654da66957d938d8fd53d35ec51545b4ac3ad5cc]
- Stated design principles include local execution of file and shell operations by a Rust process, durable coordination that survives interruptions, and layered implementation where workspace primitives avoid HTTP, Convex, and provider dependencies. [@claim:clm_9fd792a930f63d154ac48393eb5a42389b2fd4925b49c959d2e4c000b006deea]
- The native authentication migration is incomplete: thread-cache registration, thread commands, cancellation, lifecycle, transcript synchronization, and attachments still pass browser access tokens or user IDs to Rust. [@claim:clm_bc05466cf9f537bf91f1aaed05978117d6b15f6ff52d762484349a3b989231e9]
<!-- rcw:end owner=source:src_e744b8d896d35341bc34a342fa2260a3 block=evidence -->

## Researcher notes

