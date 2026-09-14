---
access: public
aliases: []
claim_ids:
- clm_0ef56bd52ff2bf8205a1a36f75be03098f132cdb4686b54255baec8170b14aec
- clm_1ba4e3d95ad2157d7ab1d5e9a8b16acafcc9e7575b5ecf7620b3470880328033
- clm_2a264bdbc6cf7163747479e2563d2228f99b90f244d17babfdf5157d928a6687
- clm_46969869d5117528e88af70833f12218724ee8f9b629dc8ba5408d72b9f51c67
- clm_564a3e27b3b8e5aa588df1507c7b532302b9daf74f19c5773dd2d7036aa38347
- clm_59a33dbb925a14a8fbe3d177e149e105fa0e75556ea8ff4bdb6514de67cc0801
- clm_657c66e3b5e815c686d892e912afcd550d020ee23108a4b89c83e268f42d7bb5
- clm_ac540355f2735fe65cf002c40adb78b1a4296b55c27a4b2df42bce2c6f52b610
- clm_b2ebb52efb770194de9e23493e8876977bfbf858ba75e5de184bac5f92c854fd
- clm_be401918ae212601f9cda08dc2055f173efdb60890bd1a5a5be51c93279a548a
- clm_c5ae0912b8e34c7e43b1d00d5502955ab37192f70074d5ffe7c83d78183ba3cb
- clm_c80f2ec2b4c6b97e415d39d84c23f1409741682ebcba03ae75f09919f7239cf1
maturity: draft
page_id: pg_d7d63e6ce88b55b696959be0c56f3da2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7f0ef24dc5485eed9310fc0f989cfc1b
title: HarnessRouter/harnessrouter/README.md @ 5637717816b5
updated_at: '2026-09-14T02:03:14Z'
---

# HarnessRouter/harnessrouter/README.md @ 5637717816b5

<!-- rcw:begin owner=source:src_7f0ef24dc5485eed9310fc0f989cfc1b block=evidence -->
- The API surface supports starting tasks, continuing sessions with previous_response_id, streaming progress, file attach/retrieve, cancellation, and structured errors/traces. [@claim:clm_0ef56bd52ff2bf8205a1a36f75be03098f132cdb4686b54255baec8170b14aec]
- Running the Community Edition requires Docker, about 4 GB of disk, and a user-supplied provider API key; no bundled model or trial key is included. [@claim:clm_1ba4e3d95ad2157d7ab1d5e9a8b16acafcc9e7575b5ecf7620b3470880328033]
- One Docker container runs three parts: Console on :3000 (only published port, entry point for UI and API), Gateway on :8080 (Responses API and harness lifecycle), and Runner on :8081 (runs harnesses in session workspaces). [@claim:clm_2a264bdbc6cf7163747479e2563d2228f99b90f244d17babfdf5157d928a6687]
- The product exposes an OpenAI Responses-compatible API; callers select a harness via metadata.harness_id and can set stream:true for server-sent events. [@claim:clm_46969869d5117528e88af70833f12218724ee8f9b629dc8ba5408d72b9f51c67]
- The project implements the Unified Harness Protocol (UHP), a versioned public contract whose task surface is deliberately compatible with the OpenAI Responses API, with spec, schemas, and conformance suite in the repo. [@claim:clm_564a3e27b3b8e5aa588df1507c7b532302b9daf74f19c5773dd2d7036aa38347]
- Community Edition disables the Console analytics pipeline, and provider keys, sessions, files, and workspaces remain under the self-hosting operator's control. [@claim:clm_59a33dbb925a14a8fbe3d177e149e105fa0e75556ea8ff4bdb6514de67cc0801]
- Sessions use separate workspaces and operating-system users rather than separate containers; the Console and Gateway run unprivileged while the entrypoint and Runner need root to manage per-session users. [@claim:clm_657c66e3b5e815c686d892e912afcd550d020ee23108a4b89c83e268f42d7bb5]
- A /data volume persists the database, files, secrets, installed harness CLIs, and workspaces across container restarts. [@claim:clm_ac540355f2735fe65cf002c40adb78b1a4296b55c27a4b2df42bce2c6f52b610]
- The Runner executes harnesses inside per-session workspaces, and the first container launch installs the enabled harness CLIs. [@claim:clm_b2ebb52efb770194de9e23493e8876977bfbf858ba75e5de184bac5f92c854fd]
- README benchmark figures compare eight harness-and-model configurations on the same task, reporting best-vs-worst cost (223 to 0.47 credits) and end-to-end latency (4m36s to 1m25s), with methodology linked externally. [@claim:clm_be401918ae212601f9cda08dc2055f173efdb60890bd1a5a5be51c93279a548a]
- The product handles persistent sessions: follow-up instructions can be sent with previous_response_id, and tasks with transcripts appear in the same Console workspace. [@claim:clm_c5ae0912b8e34c7e43b1d00d5502955ab37192f70074d5ffe7c83d78183ba3cb]
- Agent harness CLIs are installed on first launch and remain governed by their respective upstream licenses; the edition itself is Apache 2.0. [@claim:clm_c80f2ec2b4c6b97e415d39d84c23f1409741682ebcba03ae75f09919f7239cf1]
<!-- rcw:end owner=source:src_7f0ef24dc5485eed9310fc0f989cfc1b block=evidence -->

## Researcher notes

