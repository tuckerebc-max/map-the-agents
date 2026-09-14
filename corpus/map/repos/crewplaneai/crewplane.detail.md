# crewplaneai/crewplane -- full detail

[Back to orientation](crewplane.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/crewplaneai/crewplane/bc0b5eef57622a66e79bf70a2274016c4445c19a/321edf963f9ad975.json](../../../wiki/dossiers/crewplaneai/crewplane/bc0b5eef57622a66e79bf70a2274016c4445c19a/321edf963f9ad975.json)

## specifications (1 claim(s))

- [observation/documented] Crewplane is described as an open-source workflow runner for reviewable, resumable coding-agent workflows, with the whole process defined in Markdown including prompts, stages, agents, handoffs, and next-step rules. -- evidence: [README.md#L1-L19](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L1-L19) (`clm_2097423a5b15a0d09a3fe784f43bc14792a4af0bf8ff78ab2c2ed6d31cbe9b9d`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Handoffs between stages are explicit template references such as {{plan.output}} rather than hidden session context, and sequential nodes can pair an executor with a reviewer role that may send blocking feedback into bounded fix attempts. -- evidence: [README.md#L276-L276](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L276-L276), [README.md#L295-L302](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L295-L302) (`clm_03e64fa90e8731dbf40bddf209ad340750e74ab4e704c9f392d624d115e39c55`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENTS.md is described as the canonical repository instructions for coding agents, and contributors are directed to CONTRIBUTING.md and a development guide for local checkout setup. -- evidence: [AGENTS.md#L3-L3](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/AGENTS.md#L3-L3), [README.md#L522-L525](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L522-L525) (`clm_930ff87ba453a3e25d72297d775febe2a93cf1b162a2ccb57f60b9469f80fe84`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product provides CLI commands including init, validate, run, onboarding, --update, and --version, and supports running specific task files via a --tasks flag. -- evidence: [README.md#L482-L490](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L482-L490), [README.md#L149-L152](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L149-L152), [README.md#L420-L423](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L420-L423), [README.md#L123-L127](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L123-L127) (`clm_cb13ab07e3d1071d9ec134facf6c950a1b69d698c6252942611da723356e21e9`)
- [observation/documented] Workflows are Markdown files whose YAML frontmatter declares an execution graph with nodes, needs dependencies, parallel or sequential modes, and provider assignments, while Markdown sections define per-stage instructions. -- evidence: [README.md#L262-L266](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L262-L266), [README.md#L253-L260](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L253-L260), [README.md#L235-L237](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L235-L237), [README.md#L248-L251](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L248-L251) (`clm_536cea016495516b40d8a7d6d5f1d1594d086146c340637900964582f18c0f6e`)
- [observation/documented] When output is attached to a terminal and tmux is available, a compact live dashboard shows DAG progress, node status, and live log tails; --no-live omits it. -- evidence: [README.md#L170-L170](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L170-L170), [README.md#L164-L165](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L164-L165) (`clm_048a57322fbfc3bea8dcc5dcb3b8ff6ca4654a5fa845cef163bbb4846566672f`)

## memory-state (1 claim(s))

- [observation/documented] Each run writes artifacts under .crewplane/ with execution-results per run-key for findings and final results and execution-stages for per-node inputs, outputs, logs, events, and manifests; identical inputs reuse the saved result unless --force is passed. -- evidence: [README.md#L135-L139](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L135-L139), [README.md#L194-L196](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L194-L196), [README.md#L174-L188](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L174-L188) (`clm_abc395e1c2d81ab4d164329e3a99c71d797b67c029053ff0eb58acb2fe1bbb77`)

## orchestration (1 claim(s))

- [observation/documented] Crewplane validates and runs the declared workflow graph, fans work out in parallel, routes stages to different provider CLIs, enforces review gates, and reuses completed stages it can validate when resuming. -- evidence: [README.md#L384-L405](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L384-L405), [README.md#L370-L382](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L370-L382) (`clm_2f977548128704bc9a291e9302be520ca307bef5ec8f682dbef1d13c9279afab`)

## tools-permissions (1 claim(s))

- [observation/documented] Crewplane invokes existing coding-agent CLIs but does not install, authenticate, or sandbox them; providers run with their own configuration and whatever permissions the user's environment grants, keeping models, tools, and credentials under native control. -- evidence: [README.md#L434-L437](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L434-L437), [README.md#L70-L73](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L70-L73) (`clm_35162a525805f55b402a5c849bd6d0eff163cdc6ec44496cbc007451d2211ea2`)

## evaluation (1 claim(s))

- [observation/documented] A companion Crewplane Lab repository publishes recorded experiments, such as eight Codex model/reasoning configurations on one algorithm challenge, with workflow definitions, responses, comparison output, telemetry, and logs; the README notes it is one recorded experiment, not a general model benchmark. -- evidence: [README.md#L110-L113](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L110-L113), [README.md#L77-L79](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L77-L79), [README.md#L81-L83](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L81-L83) (`clm_f328397fdd474b8c2dba1bf8be8880abc6a3584b931041404418cefa048ca6b4`)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Python 3.13 or later, supports Linux, macOS, and WSL, and does not currently support native Windows; recommended installation is via uv tool install, with pip, pipx, Homebrew, an install script, and an npm wrapper also listed. -- evidence: [README.md#L414-L416](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L414-L416), [README.md#L430-L432](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L430-L432), [README.md#L425-L428](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L425-L428) (`clm_30b827d434ad6b42434a3ba46ebcbf785d44482b0456ad16c7638884755bcb2e`)

## limitations (1 claim(s))

- [observation/documented] Token usage figures appear in run summaries and runtime logs only when the provider reports them, and run summaries separate normalized provider token totals from a visible-text lower-bound estimate. -- evidence: [README.md#L344-L347](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L344-L347), [CHANGELOG.md#L175-L177](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/CHANGELOG.md#L175-L177) (`clm_511b3204727a2a5faf8231d67b237d87bb0ceab513cad664f2ec320627eaa882`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

