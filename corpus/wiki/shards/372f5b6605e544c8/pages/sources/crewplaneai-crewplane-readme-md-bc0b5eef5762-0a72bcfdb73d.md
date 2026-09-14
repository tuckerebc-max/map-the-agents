---
access: public
aliases: []
claim_ids:
- clm_03e64fa90e8731dbf40bddf209ad340750e74ab4e704c9f392d624d115e39c55
- clm_048a57322fbfc3bea8dcc5dcb3b8ff6ca4654a5fa845cef163bbb4846566672f
- clm_2097423a5b15a0d09a3fe784f43bc14792a4af0bf8ff78ab2c2ed6d31cbe9b9d
- clm_2f977548128704bc9a291e9302be520ca307bef5ec8f682dbef1d13c9279afab
- clm_30b827d434ad6b42434a3ba46ebcbf785d44482b0456ad16c7638884755bcb2e
- clm_35162a525805f55b402a5c849bd6d0eff163cdc6ec44496cbc007451d2211ea2
- clm_511b3204727a2a5faf8231d67b237d87bb0ceab513cad664f2ec320627eaa882
- clm_536cea016495516b40d8a7d6d5f1d1594d086146c340637900964582f18c0f6e
- clm_930ff87ba453a3e25d72297d775febe2a93cf1b162a2ccb57f60b9469f80fe84
- clm_abc395e1c2d81ab4d164329e3a99c71d797b67c029053ff0eb58acb2fe1bbb77
- clm_cb13ab07e3d1071d9ec134facf6c950a1b69d698c6252942611da723356e21e9
- clm_f328397fdd474b8c2dba1bf8be8880abc6a3584b931041404418cefa048ca6b4
maturity: draft
page_id: pg_c37cbd6735395e719c0e0a72bcfdb73d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_88c84ae00995594c80ff83d17aa6305a
title: crewplaneai/crewplane/README.md @ bc0b5eef5762
updated_at: '2026-09-14T01:44:09Z'
---

# crewplaneai/crewplane/README.md @ bc0b5eef5762

<!-- rcw:begin owner=source:src_88c84ae00995594c80ff83d17aa6305a block=evidence -->
- Handoffs between stages are explicit template references such as {{plan.output}} rather than hidden session context, and sequential nodes can pair an executor with a reviewer role that may send blocking feedback into bounded fix attempts. [@claim:clm_03e64fa90e8731dbf40bddf209ad340750e74ab4e704c9f392d624d115e39c55]
- When output is attached to a terminal and tmux is available, a compact live dashboard shows DAG progress, node status, and live log tails; --no-live omits it. [@claim:clm_048a57322fbfc3bea8dcc5dcb3b8ff6ca4654a5fa845cef163bbb4846566672f]
- Crewplane is described as an open-source workflow runner for reviewable, resumable coding-agent workflows, with the whole process defined in Markdown including prompts, stages, agents, handoffs, and next-step rules. [@claim:clm_2097423a5b15a0d09a3fe784f43bc14792a4af0bf8ff78ab2c2ed6d31cbe9b9d]
- Crewplane validates and runs the declared workflow graph, fans work out in parallel, routes stages to different provider CLIs, enforces review gates, and reuses completed stages it can validate when resuming. [@claim:clm_2f977548128704bc9a291e9302be520ca307bef5ec8f682dbef1d13c9279afab]
- The tool requires Python 3.13 or later, supports Linux, macOS, and WSL, and does not currently support native Windows; recommended installation is via uv tool install, with pip, pipx, Homebrew, an install script, and an npm wrapper also listed. [@claim:clm_30b827d434ad6b42434a3ba46ebcbf785d44482b0456ad16c7638884755bcb2e]
- Crewplane invokes existing coding-agent CLIs but does not install, authenticate, or sandbox them; providers run with their own configuration and whatever permissions the user's environment grants, keeping models, tools, and credentials under native control. [@claim:clm_35162a525805f55b402a5c849bd6d0eff163cdc6ec44496cbc007451d2211ea2]
- Token usage figures appear in run summaries and runtime logs only when the provider reports them, and run summaries separate normalized provider token totals from a visible-text lower-bound estimate. [@claim:clm_511b3204727a2a5faf8231d67b237d87bb0ceab513cad664f2ec320627eaa882]
- Workflows are Markdown files whose YAML frontmatter declares an execution graph with nodes, needs dependencies, parallel or sequential modes, and provider assignments, while Markdown sections define per-stage instructions. [@claim:clm_536cea016495516b40d8a7d6d5f1d1594d086146c340637900964582f18c0f6e]
- Repository development practice: AGENTS.md is described as the canonical repository instructions for coding agents, and contributors are directed to CONTRIBUTING.md and a development guide for local checkout setup. [@claim:clm_930ff87ba453a3e25d72297d775febe2a93cf1b162a2ccb57f60b9469f80fe84]
- Each run writes artifacts under .crewplane/ with execution-results per run-key for findings and final results and execution-stages for per-node inputs, outputs, logs, events, and manifests; identical inputs reuse the saved result unless --force is passed. [@claim:clm_abc395e1c2d81ab4d164329e3a99c71d797b67c029053ff0eb58acb2fe1bbb77]
- The product provides CLI commands including init, validate, run, onboarding, --update, and --version, and supports running specific task files via a --tasks flag. [@claim:clm_cb13ab07e3d1071d9ec134facf6c950a1b69d698c6252942611da723356e21e9]
- A companion Crewplane Lab repository publishes recorded experiments, such as eight Codex model/reasoning configurations on one algorithm challenge, with workflow definitions, responses, comparison output, telemetry, and logs; the README notes it is one recorded experiment, not a general model benchmark. [@claim:clm_f328397fdd474b8c2dba1bf8be8880abc6a3584b931041404418cefa048ca6b4]
<!-- rcw:end owner=source:src_88c84ae00995594c80ff83d17aa6305a block=evidence -->

## Researcher notes

