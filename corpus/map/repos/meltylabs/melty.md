# meltylabs/melty

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3b7046ff2253 @ 53899bace69fad19

## Summary (orientation draft, not independently verified)

README describes Melty as an AI code editor with chat-level git operations (revert, branch, reset, squash) and lists design goals; CHARLIE_README documents a webview contract; CONTRIBUTING gives contributor setup instructions; the repo carries an MIT license attributed to Microsoft Corporation.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes Melty as an AI code editor whose chats can be reverted, branched, reset, and squashed, with Melty staying in sync like a pair programmer. -- evidence: [README.md#L3-L3](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Stated design goals: help users understand their code, watch every change like a pair programmer, learn and adapt to the codebase, and integrate with compiler, terminal, debugger, Linear, and GitHub. -- evidence: [README.md#L45-L48](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L45-L48)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: local development involves cloning the repo, running yarn run melty:install and yarn run melty:extension-dev, then the default debug configuration; changes to extensions/spectacular are watched and require reloading the editor. -- evidence: [CONTRIBUTING.md#L37-L37](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L32-L33](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L32-L33), [CONTRIBUTING.md#L35-L35](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L35-L35), [CONTRIBUTING.md#L25-L25](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L25-L25), [CONTRIBUTING.md#L29-L29](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L29-L29)
  - [observation/documented] Repository development practice: contributors are asked to reach out before adding features, and bug reports should include the Melty version, operating system, and Dev Tools console errors. -- evidence: [CONTRIBUTING.md#L15-L17](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L15-L17), [CONTRIBUTING.md#L21-L21](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L21-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A webview contract documents calling humanXYZ() on user actions, then startBotTurn() to return control, with stopBotTurn() as needed; task updates flow via updateTask, and an endBotTurn notification is planned but not yet needed. -- evidence: [CHARLIE_README.md#L17-L19](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L17-L19), [CHARLIE_README.md#L21-L21](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L21-L21)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [inference/documented] The README indicates version 0.2 was not yet generally released and access was gated through a waitlist and early-access signup form. -- evidence: [README.md#L5-L5](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L5-L5), [README.md#L50-L50](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L50-L50)
- relevance (1 claim(s)):
  - [observation/documented] The repository is licensed under the MIT License, with the license text carrying a Microsoft Corporation copyright notice. -- evidence: [LICENSE.txt#L3-L3](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/LICENSE.txt#L3-L3), [LICENSE.txt#L1-L1](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/LICENSE.txt#L1-L1)

(2 additional claim(s) omitted for length; see [full detail](melty.detail.md) for every claim.)

Metadata and full claim list: [full detail](melty.detail.md)
Human notes ([notes](melty.notes.md), never overwritten by build)

[Back to map index](../../index.md)
