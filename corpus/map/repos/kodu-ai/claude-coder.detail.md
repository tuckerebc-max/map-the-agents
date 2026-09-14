# kodu-ai/claude-coder -- full detail

[Back to orientation](claude-coder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kodu-ai/claude-coder/60c1a717992c1a597850d1e3671dc0491eab02ed/181d9051e841effc.json](../../../wiki/dossiers/kodu-ai/claude-coder/60c1a717992c1a597850d1e3671dc0491eab02ed/181d9051e841effc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] An ExtensionStateProvider sets up listeners for extension messages and supplies state to child components, while a useExtensionState hook exposes state and setters. -- evidence: [extension-state-summary.md#L34-L41](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L34-L41) (`clm_53723a697dc23761d725c70ca0df7d1d0ca0792c3199b81858f1ad9ba5baf68d`)

## design-choices (2 claim(s))

- [observation/documented] The extension's webview state is managed with Jotai, where individual atoms are combined into a single derived extensionStateAtom. -- evidence: [extension-state-summary.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L3-L3), [extension-state-summary.md#L7-L7](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L7-L7) (`clm_c258088d05443334a23937994268570faa424df4a5934146c6d91c3f54599a90`)
- [observation/documented] Task processing follows a Reasoning-Acting-Observing (ReAct) loop: analyze and plan, execute actions with tools, then evaluate results and adjust. -- evidence: [prompt-crafting-guide.md#L7-L7](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L7-L7), [prompt-crafting-guide.md#L9-L11](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L9-L11) (`clm_ac88ee7d0dc7042fe609130742d2fe14d3949f34877d8625b898209a6ec9b3f0`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm run install:all in the extension folder, launch with F5, and submit pull requests; webview hot-reloads but extension host changes need a full reload. -- evidence: [README.md#L91-L92](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L91-L92), [README.md#L83-L87](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L83-L87), [README.md#L94-L94](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L94-L94) (`clm_7aff0b3d36564b3c5e9734ed23832f9b8aca85ca9ac64990ffea525b6b103ca7`)

## skills-patterns (1 claim(s))

- [observation/documented] The prompt guide recommends decomposing large tasks by spawning a SubTask agent for planning, additional SubTask agents for components, and letting the main agent coordinate. -- evidence: [prompt-crafting-guide.md#L76-L79](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L76-L79), [prompt-crafting-guide.md#L89-L91](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L89-L91) (`clm_b742646e9127708a0cb58ac37ce9f7ab4f9b38126214ab1991b6880ee261733d`)

## interfaces (1 claim(s))

- [observation/documented] Claude Coder is distributed as a VS Code extension installable from the marketplace, per the README's download link and install instructions. -- evidence: [README.md#L44-L53](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L44-L53), [README.md#L1-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L1-L3) (`clm_cd282f43a2497609f28e7dc0a4ec85779eb3cea9914f918d6eef026647dd50f7`)

## memory-state (1 claim(s))

- [observation/documented] Extension state includes fields such as claudeMessages, taskHistory, currentTask, apiConfiguration, maxRequestsPerTask, customInstructions, and alwaysAllowReadOnly/WriteOnly flags. -- evidence: [extension-state-summary.md#L9-L30](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L9-L30) (`clm_d4dd2550a8b463c0ffc1ab7c2097f6e980390e3dc8f86789989ca8ead3f4ff9e`)

## orchestration (1 claim(s))

- [observation/documented] The prompt guide describes a multi-agent system with a main Kodu agent that follows a ReAct pattern and can spawn specialized sub-agents. -- evidence: [prompt-crafting-guide.md#L38-L42](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L38-L42), [prompt-crafting-guide.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L3-L3) (`clm_c2c7db8d6129b7d437bf1724914e0efb2f7808bf706431e505bf50c1b347d30d`)

## tools-permissions (1 claim(s))

- [observation/documented] The guide references an add_interested_file tool used to track files relevant to the current task. -- evidence: [prompt-crafting-guide.md#L83-L85](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L83-L85) (`clm_f24a94be275bef03277ecc31cb1617aefb8c9a4122c1e7546a46cd4137a093ce`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The extension's UI appears to depend on React and the Jotai state library, based on the state-management summary's description. -- evidence: [extension-state-summary.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L3-L3) (`clm_6ad6a1d30c438363a1775097394a4e3a9f2c0f9225b2a0b97f2d0786b3427def`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project credits Claude Dev and Aider as inspirations, indicating it builds on the Claude Dev extension lineage. -- evidence: [README.md#L67-L68](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L67-L68) (`clm_4a0c85c362469069bd43eaf8b6bf71106699f6180b73bb2900f4d0c10f3a1e8e`)

