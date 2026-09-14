# kodu-ai/claude-coder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 60c1a717992c @ 181d9051e841effc

## Summary (orientation draft, not independently verified)

Selected evidence records: Claude Coder is distributed as a VS Code extension installable from the marketplace, per the README's download link and install instructions. The extension's webview state is managed with Jotai, where individual atoms are combined into a single derived extensionStateAtom.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] An ExtensionStateProvider sets up listeners for extension messages and supplies state to child components, while a useExtensionState hook exposes state and setters. -- evidence: [extension-state-summary.md#L34-L41](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L34-L41)
- design-choices (2 claim(s)):
  - [observation/documented] The extension's webview state is managed with Jotai, where individual atoms are combined into a single derived extensionStateAtom. -- evidence: [extension-state-summary.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L3-L3), [extension-state-summary.md#L7-L7](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L7-L7)
  - [observation/documented] Task processing follows a Reasoning-Acting-Observing (ReAct) loop: analyze and plan, execute actions with tools, then evaluate results and adjust. -- evidence: [prompt-crafting-guide.md#L7-L7](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L7-L7), [prompt-crafting-guide.md#L9-L11](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L9-L11)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm run install:all in the extension folder, launch with F5, and submit pull requests; webview hot-reloads but extension host changes need a full reload. -- evidence: [README.md#L91-L92](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L91-L92), [README.md#L83-L87](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L83-L87), [README.md#L94-L94](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L94-L94)
- skills-patterns (1 claim(s)):
  - [observation/documented] The prompt guide recommends decomposing large tasks by spawning a SubTask agent for planning, additional SubTask agents for components, and letting the main agent coordinate. -- evidence: [prompt-crafting-guide.md#L76-L79](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L76-L79), [prompt-crafting-guide.md#L89-L91](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L89-L91)
- interfaces (1 claim(s)):
  - [observation/documented] Claude Coder is distributed as a VS Code extension installable from the marketplace, per the README's download link and install instructions. -- evidence: [README.md#L44-L53](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L44-L53), [README.md#L1-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L1-L3)
- memory-state (1 claim(s)):
  - [observation/documented] Extension state includes fields such as claudeMessages, taskHistory, currentTask, apiConfiguration, maxRequestsPerTask, customInstructions, and alwaysAllowReadOnly/WriteOnly flags. -- evidence: [extension-state-summary.md#L9-L30](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L9-L30)
- orchestration (1 claim(s)):
  - [observation/documented] The prompt guide describes a multi-agent system with a main Kodu agent that follows a ReAct pattern and can spawn specialized sub-agents. -- evidence: [prompt-crafting-guide.md#L38-L42](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L38-L42), [prompt-crafting-guide.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L3-L3)
- tools-permissions (1 claim(s)):
  - [observation/documented] The guide references an add_interested_file tool used to track files relevant to the current task. -- evidence: [prompt-crafting-guide.md#L83-L85](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/prompt-crafting-guide.md#L83-L85)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [inference/documented] The extension's UI appears to depend on React and the Jotai state library, based on the state-management summary's description. -- evidence: [extension-state-summary.md#L3-L3](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/extension-state-summary.md#L3-L3)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The project credits Claude Dev and Aider as inspirations, indicating it builds on the Claude Dev extension lineage. -- evidence: [README.md#L67-L68](https://github.com/kodu-ai/claude-coder/blob/60c1a717992c1a597850d1e3671dc0491eab02ed/README.md#L67-L68)
More evidence: [full detail](claude-coder.detail.md)

Metadata and full claim list: [full detail](claude-coder.detail.md)
Human notes ([notes](claude-coder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
