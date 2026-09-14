# stagewise-io/stagewise -- full detail

[Back to orientation](stagewise.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stagewise-io/stagewise/18ac8a27b18c5de4e2d76d03b515cf10186631ca/389bf292978597bd.json](../../../wiki/dossiers/stagewise-io/stagewise/18ac8a27b18c5de4e2d76d03b515cf10186631ca/389bf292978597bd.json)

## specifications (2 claim(s))

- [observation/documented] Stagewise is described as an open-source agentic IDE for developers with a coding agent built in. -- evidence: [README.md#L41-L41](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L41-L41) (`clm_9e0c21fc0516a7b0fd91e199459584f4dee66bd565d4d57e4aca0bde881c5da0`)
- [observation/documented] A stagewise Account offers Free, Pro ($20/mo), and Ultra ($200/mo) plans with differing model access and usage limits. -- evidence: [README.md#L82-L86](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L82-L86) (`clm_141ddc97ea628b2dff42cc6c20422bbaaccfc7fb171cca998f2a974577eafff8`)

## components (2 claim(s))

- [observation/documented] Recent release notes list features such as provider usage-limit display, external coding agent integrations, Codex worktree support, chat archiving, and isolated dev instances. -- evidence: [.release-notes.md#L5-L13](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/.release-notes.md#L5-L13) (`clm_739486d78b6a70522c5520f3115cf7762f4508e63b288d727a3867a1fe1a837c`)
- [observation/documented] Release notes mention ACP session, lifecycle, and approval handling fixes, suggesting the product integrates agents over the ACP protocol. -- evidence: [.release-notes.md#L17-L39](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/.release-notes.md#L17-L39) (`clm_37ef27fa560d12fbc2d12ee0ffb65ff7bc7ce43eba725f34f735d5f4e6be49c0`)

## design-choices (1 claim(s))

- [observation/documented] The product supports bring-your-own-key for all AI providers, including registering fully custom providers such as local inference and defining custom models. -- evidence: [README.md#L43-L48](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L43-L48), [README.md#L56-L56](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L56-L56) (`clm_9268d1fd3bd3de6efa18672a572c259350fccf3c73646a4510db68276bf69387`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs AI coding agents on pnpm/Turborepo commands, Biome linting, Vitest tests, Electron app scripts, and pre-commit hooks (Lefthook, commitlint). -- evidence: [AGENTS.md#L23-L24](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L23-L24), [AGENTS.md#L8-L9](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L8-L9), [AGENTS.md#L131-L135](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L131-L135), [AGENTS.md#L27-L33](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L27-L33), [AGENTS.md#L17-L20](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L17-L20) (`clm_e08a9ad404624a685c9e7b04eb208c2f8fde9115366196bf530e4be4ac7aa57d`)
- [observation/documented] Repository development practice: commits must follow Conventional Commits with a mandatory workspace-package scope, and releases run via a two-step GitHub Actions workflow with nightly builds separate. -- evidence: [VERSIONING.md#L151-L151](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L151-L151), [VERSIONING.md#L7-L7](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L7-L7), [VERSIONING.md#L140-L140](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L140-L140), [VERSIONING.md#L149-L149](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L149-L149), [VERSIONING.md#L142-L145](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L142-L145) (`clm_b69b02a995f5ea15e35e79e4798c2b83324c2688e58e843976a6a4d445783cd1`)
- [observation/documented] Repository development practice: prerelease versions use a no-dot channel+counter format (e.g. 1.0.1-alpha001, counter capped at 999) to stay compatible with Squirrel.Windows' NuGet parser. -- evidence: [VERSIONING.md#L74-L74](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L74-L74), [VERSIONING.md#L72-L72](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L72-L72), [VERSIONING.md#L76-L76](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L76-L76) (`clm_2ec51d669c0c406ff7cd07ea4a132be7dd68b8cb351211723cd947eb0d912cb4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product lets users work with a coding agent that has access to the browser tab's console and debugger, and supports IDE integration to view and apply code changes. -- evidence: [README.md#L43-L48](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L43-L48) (`clm_942b279636b539922f7565ab05eb92094356585979b38b5180834ccd7aed80ad`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Documented provider integrations include Moonshot Kimi, Alibaba Qwen, MiniMax, Xiaomi MiMo, Mistral, and OpenRouter access to 345+ models via one API key. -- evidence: [README.md#L72-L72](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L72-L72), [README.md#L62-L68](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L62-L68) (`clm_31abc05228e515e9f81c9383413b7945e397357f0ef0fc74408125cc92db5967`)
- [observation/documented] The account plans include open-weight models (Kimi, Qwen, DeepSeek, GLM, MiniMax, MiMo, Mistral) and proprietary models from Anthropic, OpenAI, Google, and xAI. -- evidence: [README.md#L102-L105](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L102-L105), [README.md#L92-L98](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L92-L98) (`clm_04a98cac8e4fc7c8e9db652046fe608912d50bba946e90c2d257d7946adc6a48`)

## limitations (1 claim(s))

- [observation/documented] Stagewise is developed by stagewise GmbH and offered under the AGPLv3 license, with out-of-scope use cases handled by contacting sales. -- evidence: [README.md#L113-L113](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L113-L113), [README.md#L109-L109](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L109-L109) (`clm_9cd993e3677fd0a308661d28ddc7d4416f03e53d69c903c2d274a1e261939900`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

