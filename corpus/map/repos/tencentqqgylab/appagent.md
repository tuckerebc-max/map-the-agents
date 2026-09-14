# tencentqqgylab/appagent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: mnotgod96/appagent (github id 733899994).
Latest snapshot: commit 2c1900422caf @ cbf24173f142265b

## Summary (orientation draft, not independently verified)

AppAgent is an LLM-based multimodal agent framework that operates Android smartphone apps via tapping/swiping, with an exploration phase (autonomous or human demonstration) that builds element documentation used in a deployment phase. Evidence is README-only; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AppAgent is described as a novel LLM-based multimodal agent framework designed to operate smartphone applications. -- evidence: [README.md#L42-L42](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L42-L42)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The agent acts through a simplified action space mimicking human interactions like tapping and swiping, avoiding the need for system back-end access so it works across diverse apps. -- evidence: [README.md#L44-L44](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L44-L44)
  - [observation/documented] An optional grid overlay can be brought up on the screen so the agent can tap or swipe anywhere, useful for UI elements lacking a numeric tag. -- evidence: [README.md#L31-L37](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L31-L37), [README.md#L59-L59](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L59-L59)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The agent learns to use new apps either by autonomous exploration or by observing human demonstrations, producing a knowledge base it later consults for complex tasks. -- evidence: [README.md#L46-L46](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L46-L46)
- interfaces (2 claim(s)):
  - [observation/documented] Users run `learn.py` to enter autonomous exploration or human demonstration mode, and `run.py` for deployment, supplying app name and task description via prompts. -- evidence: [README.md#L143-L147](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L143-L147), [README.md#L157-L161](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L157-L161), [README.md#L129-L132](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L129-L132)
  - [observation/documented] The agent communicates with the Android device through Android Debug Bridge (adb) from a PC, with USB debugging enabled on the device; an Android Studio emulator is also supported and auto-detected. -- evidence: [README.md#L70-L71](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L70-L71), [README.md#L77-L81](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L77-L81), [README.md#L73-L73](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L73-L73)
- memory-state (1 claim(s)):
  - [observation/documented] During exploration or demonstration, the agent generates documentation for interacted UI elements and saves it for use in the deployment phase; deployment can auto-detect an existing documentation base for an app. -- evidence: [README.md#L157-L161](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L157-L161), [README.md#L118-L122](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L118-L122)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README links to an evaluation benchmark (testset.md) that was released in January 2024 and used during the team's testing of AppAgent. -- evidence: [README.md#L174-L174](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L174-L174), [README.md#L31-L37](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L31-L37)
- dependencies (2 claim(s)):
  - [observation/documented] The project requires Python 3 and dependencies installed via requirements.txt, which lists packages including argparse, colorama, dashscope, opencv-python, pyshine, pyyaml, and requests. -- evidence: [requirements.txt#L1-L7](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/requirements.txt#L1-L7), [README.md#L85-L86](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L85-L86), [README.md#L88-L91](https://github.com/TencentQQGYLab/AppAgent/blob/2c1900422caf6f9e94e96d5dd984b530e5a5fbf8/README.md#L88-L91)
More evidence: [full detail](appagent.detail.md)

Metadata and full claim list: [full detail](appagent.detail.md)
Human notes ([notes](appagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
