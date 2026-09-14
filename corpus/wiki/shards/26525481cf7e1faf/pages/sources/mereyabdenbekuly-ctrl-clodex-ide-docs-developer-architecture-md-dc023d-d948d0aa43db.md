---
access: public
aliases: []
claim_ids:
- clm_226cec2acb27c79a2c00c6b04d314b3071e58a90b501809865ccfa5cdb3d418a
- clm_2cbd53cdbeb29c7344d0475b65510bf224de84d40ecbd488857fe59d45f83b37
- clm_5ac382a6e2aa2ff252643d7e68c1533b38961fc9d909b67d46913bd2923d696b
- clm_5bae3851a4151b76a2451f2fce10a7ecedd2eee4e4a1e88a9397000d4cb32729
- clm_6a0282749fda3cf2336879deab8f2c22bec9957ef06cf320c47649291cc71636
- clm_87fa17da62037bef5f17293e6f21b3713d68c88b4a3464da6a18ab1f99394347
- clm_e5c32bb22106681f850eeaf27cd60a2bac5714c6fdecefd4385eb2ff4451a6df
maturity: draft
page_id: pg_2c6759bc918e59a29ea9d948d0aa43db
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_daeebe89215b5df3bd0dc2edab1a66e2
title: mereyabdenbekuly-ctrl/clodex-ide/docs/developer/architecture.md @ dc023d1f6fea
updated_at: '2026-09-14T02:17:32Z'
---

# mereyabdenbekuly-ctrl/clodex-ide/docs/developer/architecture.md @ dc023d1f6fea

<!-- rcw:begin owner=source:src_daeebe89215b5df3bd0dc2edab1a66e2 block=evidence -->
- The application is an Electron app split into isolated runtime lanes including main, renderer, agent host, MCP host, sandbox worker, and a headless CLI host, each with documented source paths. [@claim:clm_226cec2acb27c79a2c00c6b04d314b3071e58a90b501809865ccfa5cdb3d418a]
- Utility-process crashes reject in-flight work, apply bounded restart policies, and do not replay side effects, with the main process owning supervision. [@claim:clm_2cbd53cdbeb29c7344d0475b65510bf224de84d40ecbd488857fe59d45f83b37]
- The main process composes backend service groups such as task, file-tree, terminal, Git, diff, credentials, model providers, MCP, skills, plugins, network policy, and telemetry services. [@claim:clm_5ac382a6e2aa2ff252643d7e68c1533b38961fc9d909b67d46913bd2923d696b]
- Communication contracts include Karton for typed browser state and procedures, an Agent Host protocol, an MCP runtime normalizing stdio/HTTP/OAuth, runner contracts, and an Artifact Bridge with principal-scoped sessions and two-phase privileged writes. [@claim:clm_5bae3851a4151b76a2451f2fce10a7ecedd2eee4e4a1e88a9397000d4cb32729]
- Agent turns run in an isolated Agent Host outside the main process: the Agent Core resolves goal, workspace, memory, and prompt, selects a model, and streams events back through the main process to the UI. [@claim:clm_6a0282749fda3cf2336879deab8f2c22bec9957ef06cf320c47649291cc71636]
- Requested side effects are assessed by a policy component that either grants capability-bound approval for tool execution or denies/escalates; extension runtimes receive explicit capabilities rather than arbitrary host access. [@claim:clm_87fa17da62037bef5f17293e6f21b3713d68c88b4a3464da6a18ab1f99394347]
- The product offers searchable task history, workspace-aware context, restart recovery, and continued work across sessions, with session continuity and workspace snapshot services listed in the architecture. [@claim:clm_e5c32bb22106681f850eeaf27cd60a2bac5714c6fdecefd4385eb2ff4451a6df]
<!-- rcw:end owner=source:src_daeebe89215b5df3bd0dc2edab1a66e2 block=evidence -->

## Researcher notes

