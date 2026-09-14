# meltylabs/melty -- full detail

[Back to orientation](melty.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/meltylabs/melty/3b7046ff22539168ae480918445ad704bdd4d5c4/53899bace69fad19.json](../../../wiki/dossiers/meltylabs/melty/3b7046ff22539168ae480918445ad704bdd4d5c4/53899bace69fad19.json)

## specifications (1 claim(s))

- [observation/documented] The README describes Melty as an AI code editor whose chats can be reverted, branched, reset, and squashed, with Melty staying in sync like a pair programmer. -- evidence: [README.md#L3-L3](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L3-L3) (`clm_44d3de57aa5b45cf04fe9e6cf1c6fa3541fc332dc4b708dc2b33c450278f5171`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Stated design goals: help users understand their code, watch every change like a pair programmer, learn and adapt to the codebase, and integrate with compiler, terminal, debugger, Linear, and GitHub. -- evidence: [README.md#L45-L48](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L45-L48) (`clm_098d7ae4a8889ae5edb9793dd50f0c08220493afaf0b58fef7487694cb1d3cce`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: local development involves cloning the repo, running yarn run melty:install and yarn run melty:extension-dev, then the default debug configuration; changes to extensions/spectacular are watched and require reloading the editor. -- evidence: [CONTRIBUTING.md#L37-L37](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L32-L33](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L32-L33), [CONTRIBUTING.md#L35-L35](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L35-L35), [CONTRIBUTING.md#L25-L25](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L25-L25), [CONTRIBUTING.md#L29-L29](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L29-L29) (`clm_063fe1d5a089e9181f2bf2eb75e42222e81b0a22c20d0cfea074543feab4b13c`)
- [observation/documented] Repository development practice: contributors are asked to reach out before adding features, and bug reports should include the Melty version, operating system, and Dev Tools console errors. -- evidence: [CONTRIBUTING.md#L15-L17](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L15-L17), [CONTRIBUTING.md#L21-L21](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L21-L21) (`clm_c6c88762fc3550cd07c5b1e122cb640ba1acdf8d7f268e8c9f18fe5f3f17cbce`)
- [observation/documented] Repository development practice: a CHARLIE_README gives React conventions for RPC calls (wrap in useCallback, avoid putting rpcClient in dependency arrays) and troubleshooting tips such as restarting VS Code or running yarn watch. -- evidence: [CHARLIE_README.md#L11-L11](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L11-L11), [CHARLIE_README.md#L7-L9](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L7-L9), [CHARLIE_README.md#L29-L29](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L29-L29), [CHARLIE_README.md#L33-L33](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L33-L33) (`clm_f931f884ba739f10f429abf787110e4b23bfff55f4501774d530f56aa5c7bee5`)
- [observation/documented] Repository development practice: contributors may need to set the melty.anthropicApiKey setting via preferences, indicating the product uses Claude. -- evidence: [CONTRIBUTING.md#L41-L41](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L41-L41), [CONTRIBUTING.md#L43-L45](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CONTRIBUTING.md#L43-L45) (`clm_cff194588240d8463d1d611bc7eeafbd6d70fa0c10020c40dfb009e807ba4209`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A webview contract documents calling humanXYZ() on user actions, then startBotTurn() to return control, with stopBotTurn() as needed; task updates flow via updateTask, and an endBotTurn notification is planned but not yet needed. -- evidence: [CHARLIE_README.md#L17-L19](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L17-L19), [CHARLIE_README.md#L21-L21](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/CHARLIE_README.md#L21-L21) (`clm_87eb83b0ca6b6e4c891d19c7825809074573c1830398b74b08169a6725705e6a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] The README indicates version 0.2 was not yet generally released and access was gated through a waitlist and early-access signup form. -- evidence: [README.md#L5-L5](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L5-L5), [README.md#L50-L50](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/README.md#L50-L50) (`clm_1794d4d21e930c5113cd14c004fd40bea290d549c525a1e02da4469bda578aaa`)

## relevance (1 claim(s))

- [observation/documented] The repository is licensed under the MIT License, with the license text carrying a Microsoft Corporation copyright notice. -- evidence: [LICENSE.txt#L3-L3](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/LICENSE.txt#L3-L3), [LICENSE.txt#L1-L1](https://github.com/meltylabs/melty/blob/3b7046ff22539168ae480918445ad704bdd4d5c4/LICENSE.txt#L1-L1) (`clm_788afe073f25e59ef0a4a3d25ea3dac332328e26af2ed6394c83be81aaefaa7b`)

