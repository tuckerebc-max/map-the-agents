# tencentqqgylab/appagent -- full detail

[Back to orientation](appagent.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/tencentqqgylab/appagent/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/cbf24173f142265b.json](../../../wiki/dossiers/tencentqqgylab/appagent/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/cbf24173f142265b.json)

## specifications (1 claim(s))

- [observation/documented] AppAgent is described as a novel LLM-based multimodal agent framework designed to operate smartphone applications. -- evidence: [README.md#L42-L42](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L42-L42) (`clm_98612d7fe81ad42500dd03c68479f5d61780664736b189c2c90231412b154135`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The agent acts through a simplified action space mimicking human interactions like tapping and swiping, avoiding the need for system back-end access so it works across diverse apps. -- evidence: [README.md#L44-L44](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L44-L44) (`clm_616a7f39b408dbe9499745569b5e7aa77f9f077ae99045f382427ed015115c08`)
- [observation/documented] An optional grid overlay can be brought up on the screen so the agent can tap or swipe anywhere, useful for UI elements lacking a numeric tag. -- evidence: [README.md#L31-L37](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L31-L37), [README.md#L59-L59](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L59-L59) (`clm_02e4d74770b65c3b2719c7caf70acc5720976c3ce1529c16df7cf718bfc8ce14`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The agent learns to use new apps either by autonomous exploration or by observing human demonstrations, producing a knowledge base it later consults for complex tasks. -- evidence: [README.md#L46-L46](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L46-L46) (`clm_60af8cd4579a340bfacf3cf6b182f6046a72708daaf82f27d5a31e940a40067b`)

## interfaces (2 claim(s))

- [observation/documented] Users run `learn.py` to enter autonomous exploration or human demonstration mode, and `run.py` for deployment, supplying app name and task description via prompts. -- evidence: [README.md#L143-L147](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L143-L147), [README.md#L157-L161](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L157-L161), [README.md#L129-L132](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L129-L132) (`clm_e3423a2dc4b68357bbb647fb9a04996bec4ca654ed5da0e07b3ee1b2607f2f30`)
- [observation/documented] The agent communicates with the Android device through Android Debug Bridge (adb) from a PC, with USB debugging enabled on the device; an Android Studio emulator is also supported and auto-detected. -- evidence: [README.md#L70-L71](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L70-L71), [README.md#L77-L81](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L77-L81), [README.md#L73-L73](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L73-L73) (`clm_1a56f924f5030c9f015928c4d1b462d8a119993d7d1ee8c0b32746959bb2af4d`)

## memory-state (1 claim(s))

- [observation/documented] During exploration or demonstration, the agent generates documentation for interacted UI elements and saves it for use in the deployment phase; deployment can auto-detect an existing documentation base for an app. -- evidence: [README.md#L157-L161](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L157-L161), [README.md#L118-L122](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L118-L122) (`clm_4f4d961868003efe652726f09c98a7d9555b6d94508e80e18523074c6e4bf423`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README links to an evaluation benchmark (testset.md) that was released in January 2024 and used during the team's testing of AppAgent. -- evidence: [README.md#L174-L174](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L174-L174), [README.md#L31-L37](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L31-L37) (`clm_2d201c7f6b500375e234eeb825d3be5cd8fca958b61e5144e3414bb6478bbc3d`)

## dependencies (2 claim(s))

- [observation/documented] The project requires Python 3 and dependencies installed via requirements.txt, which lists packages including argparse, colorama, dashscope, opencv-python, pyshine, pyyaml, and requests. -- evidence: [requirements.txt#L1-L7](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/requirements.txt#L1-L7), [README.md#L85-L86](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L85-L86), [README.md#L88-L91](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L88-L91) (`clm_f94df984a6b57a91217bef48eb35e4679207381ba92dbf0bca70092826aaa908`)
- [observation/documented] The agent is powered by a multimodal model such as GPT-4V (gpt-4-vision-preview) or the alternative qwen-vl-max, configured via config.yaml with an API key and request interval. -- evidence: [README.md#L95-L96](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L95-L96), [README.md#L108-L109](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L108-L109), [README.md#L98-L102](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L98-L102) (`clm_2ea065a1e416ed0da84c1ba7b3be598e14bd560daa6cf7d83eeff152edc802d0`)

## limitations (2 claim(s))

- [observation/documented] The qwen-vl-max alternative model is free but reportedly performs poorer than GPT-4V in the AppAgent context, and each GPT-4V request/response pair costs around $0.03. -- evidence: [README.md#L106-L106](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L106-L106), [README.md#L108-L109](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L108-L109) (`clm_ea4c4365622c3628ce30c5701e52cfe9cea5fade4c24db0fa0f98015883594c2`)
- [observation/documented] In deployment, if no documentation base exists for an app, the agent can run without documentation but success rate is not guaranteed. -- evidence: [README.md#L157-L161](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L157-L161) (`clm_cde3da9aeef81b3504198ca0c1712a41655e78a32c15975afdaf4f23ff8e86aa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

