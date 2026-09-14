# presstab/jrdev -- full detail

[Back to orientation](jrdev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/presstab/jrdev/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/e89fbd92ce10e510.json](../../../wiki/dossiers/presstab/jrdev/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/e89fbd92ce10e510.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] JrDev uses named model profiles (advanced_reasoning, advanced_coding, intermediate_reasoning, quick_reasoning, intent_router, low_cost_search) to match model cost and capability to each task; defaults depend on the provided API key and are customizable. -- evidence: [README.md#L70-L70](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L70-L70), [README.md#L72-L77](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L72-L77), [README.md#L79-L79](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L79-L79) (`clm_17e4b85ab737f1088da52831ac5693893f077b83799472b3db792e4029c3c504`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] JrDev runs in the user's current working directory, started by entering 'jrdev' in a project directory, with commands like /init and /code typed into a Command Input field. -- evidence: [README.md#L36-L36](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L36-L36), [docs/code.md#L6-L8](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L6-L8) (`clm_3aeb69d5a95d2257952df8e7216efcc09db6703b4d78f23ac799b587d89a08e9`)
- [observation/documented] The /projectcontext command supports subcommands on|off, status, list, view <filepath>, update, refresh <filepath>, add <filepath>, and remove <filepath> for managing project context. -- evidence: [docs/project_context.md#L23-L29](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L23-L29) (`clm_426a84bdac74b688192cf0b1631beb17609fb60c06034f6f1b59cb1480019ab5`)
- [observation/documented] Thread commands include /thread new [NAME], list, switch THREAD_ID, name-all, info, and view [COUNT]; the active thread is indicated in the prompt. -- evidence: [docs/threads.md#L7-L14](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/threads.md#L7-L14), [docs/threads.md#L25-L28](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/threads.md#L25-L28) (`clm_c4ce6139859d9ec23a9d3f4043cdcf61322a2b029a877baa0c1ef5d567963102`)

## memory-state (3 claim(s))

- [observation/documented] The /init command builds persistent project context: a file tree scan, AI-selected key files (up to 20), machine-readable file summaries in .jrdev/context/, plus generated jrdev_conventions.md and jrdev_overview.md in .jrdev. -- evidence: [docs/project_context.md#L13-L17](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L13-L17) (`clm_eb69fd348ee217f0bd0a37562962196fffc520cb0e68a89881920b27879d1f59`)
- [observation/documented] An index.json in .jrdev tracks context files, their last modification times, and summary file paths; /projectcontext update and refresh handle outdated files. -- evidence: [docs/project_context.md#L35-L38](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L35-L38), [docs/project_context.md#L23-L29](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L23-L29) (`clm_18d5627d2211c8599bc39302273b1f50d3d3ce8fb81175ea2ef46e6c2512ce76`)
- [observation/documented] Chat threads are isolated: each thread keeps its own message history and context files, and a main thread is created by default when JrDev starts. -- evidence: [docs/threads.md#L18-L21](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/threads.md#L18-L21), [docs/threads.md#L25-L28](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/threads.md#L25-L28), [docs/threads.md#L3-L3](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/threads.md#L3-L3) (`clm_09442a3f2d32647a39236a415866c2f7418af75267d1c5ced65296ea12ee5650`)

## orchestration (3 claim(s))

- [observation/documented] The /code agent runs a six-phase pipeline: Analyze, Fetch Context, Plan, Execute, Review, and Validate, ending with files updated on disk. -- evidence: [docs/code.md#L40-L75](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L40-L75) (`clm_873d656b10fdc5e96fc4ad47e7ec24e948d552a22db668fb4078a2978ca71a17`)
- [observation/documented] If the Review phase finds changes insufficient, the pipeline returns to the Analyze phase with the failed review, forming an agentic loop; a passing review proceeds to validation. -- evidence: [docs/code.md#L164-L168](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L164-L168) (`clm_d51c758a2fa42ddb1ac8ca5620779caf3aa72a2986e7391fb9c06e0006937ef9`)
- [observation/documented] The Plan phase produces an ordered JSON plan of file-modification steps, validates each filename against loaded files, and offers accept, edit, accept-all, reprompt (restarting at Analyze), or cancel. -- evidence: [docs/code.md#L117-L127](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L117-L127) (`clm_8bde0e16789966adb0e710ef3dede923d7116834fe2dba46e41274fed2a22144`)

## tools-permissions (1 claim(s))

- [observation/documented] The tool can modify project files and prompts for confirmation unless in 'Accept All' mode; execute-phase diffs offer Accept, Accept All, Edit, No, or Request Change options. -- evidence: [README.md#L83-L83](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L83-L83), [docs/code.md#L138-L150](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L138-L150) (`clm_54b74496b779163e5a040a56e6932b84535403d1dff4c43b3fd51202f64b8357`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt lists openai, anthropic, google-genai, pydantic, httpx, textual[syntax], tiktoken and others, with pyreadline3, windows-curses, and colorama gated to Windows. -- evidence: [requirements.txt#L1-L14](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/requirements.txt#L1-L14) (`clm_35d83bd06d87b30e3a02d225c11144021bdb3ff81ff91cd2b7f5748a0f5bad7c`)

## limitations (1 claim(s))

- [observation/documented] The README marks JrDev as early-access software subject to rapid changes including breaking changes and experimental features, and strongly recommends committing work under version control before use. -- evidence: [README.md#L83-L83](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L83-L83) (`clm_c809ea76ef676bc5213c63292fd1740acc7d25dd3498c997c4bba325b151d8cd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

