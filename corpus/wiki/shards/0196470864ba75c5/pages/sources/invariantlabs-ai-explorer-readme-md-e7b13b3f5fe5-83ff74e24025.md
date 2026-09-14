---
access: public
aliases: []
claim_ids:
- clm_17dcf28f7f6c0c5f4f06fbc57568236cb80d7613bc52c5625549ed7560812ad6
- clm_1c85fdf6c36a5259f4e726cee7559993bb9aab3434481831f2c7a46a77b5f774
- clm_417a3891df3e9767208a05851a534d42a3e4de8f27ac683cd675d510bc0ec739
- clm_6da308e3d8a6cda59296bedbc282b04876accca9863d461dff7adb95c4ac6258
- clm_777bc9b958fe9c5967914d3a8c21d6cdfb0cb8da905ef8a0537dc70663c552d3
- clm_7cc7caa57c341238c661ad1aba4bf1d9a7f4b759ef1be1f0b9d9f5adb075d002
- clm_88bc536582bf03b1f23ca67f925d5cf56daf06192ee724aa9962eadbd86ab315
- clm_af97723df7ee43bf1882f3967880c711a9f9cbd71f7000536a444870455c3572
- clm_dd283a1e9c2df971f001cdd557a1fc26ff01e47bb1231f3b4acd67b8485b2859
- clm_f35060f240e2715cfaf9235c818b252df0e1296849aa90a23f2e4b80a1b77b78
maturity: draft
page_id: pg_b9261ae404cb54b9bb1f83ff74e24025
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0769ddbaf7f45b70b2c4f6e9e1f76548
title: invariantlabs-ai/explorer/README.md @ e7b13b3f5fe5
updated_at: '2026-09-14T03:59:37Z'
---

# invariantlabs-ai/explorer/README.md @ e7b13b3f5fe5

<!-- rcw:begin owner=source:src_0769ddbaf7f45b70b2c4f6e9e1f76548 block=evidence -->
- The hosted version of Invariant Explorer was shut down in January 2026, with readers pointed to Snyk's AI Security offering for Invariant Labs' continued AI security work. [@claim:clm_17dcf28f7f6c0c5f4f06fbc57568236cb80d7613bc52c5625549ed7560812ad6]
- Repository development practice: ./run.sh down fully tears down the testing environment and is needed before ./run.sh up again, but can be skipped when rerunning tests consecutively. [@claim:clm_1c85fdf6c36a5259f4e726cee7559993bb9aab3434481831f2c7a46a77b5f774]
- Repository development practice: new api or tester dependencies go into app-api/requirements.in or tests/requirements.in, followed by ./run.sh compile-requirements. [@claim:clm_417a3891df3e9767208a05851a534d42a3e4de8f27ac683cd675d510bc0ec739]
- Repository development practice: service logs can be streamed with ./run.sh logs and stopped with Ctrl+C. [@claim:clm_6da308e3d8a6cda59296bedbc282b04876accca9863d461dff7adb95c4ac6258]
- Users install the invariant-ai pip package and launch Explorer with the 'invariant explorer' command, then access the instance at http://localhost. [@claim:clm_777bc9b958fe9c5967914d3a8c21d6cdfb0cb8da905ef8a0537dc70663c552d3]
- Invariant Explorer is described as a tool for visualizing and exploring agent traces. [@claim:clm_7cc7caa57c341238c661ad1aba4bf1d9a7f4b759ef1be1f0b9d9f5adb075d002]
- Repository development practice: local development setup uses ./run.sh up to launch the stack, with Docker Compose installed beforehand. [@claim:clm_88bc536582bf03b1f23ca67f925d5cf56daf06192ee724aa9962eadbd86ab315]
- Explorer stores data in a ./data directory of the current working directory; deleting that directory resets the data. [@claim:clm_af97723df7ee43bf1882f3967880c711a9f9cbd71f7000536a444870455c3572]
- Docker Compose is listed as a prerequisite for running Explorer. [@claim:clm_dd283a1e9c2df971f001cdd557a1fc26ff01e47bb1231f3b4acd67b8485b2859]
- Repository development practice: tests run via ./run.sh tests-local after stopping the app with ./run.sh down, and can target a folder, a file, or a single test. [@claim:clm_f35060f240e2715cfaf9235c818b252df0e1296849aa90a23f2e4b80a1b77b78]
<!-- rcw:end owner=source:src_0769ddbaf7f45b70b2c4f6e9e1f76548 block=evidence -->

## Researcher notes

