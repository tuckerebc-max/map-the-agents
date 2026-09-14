# entropy-research/devon -- full detail

[Back to orientation](devon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/entropy-research/devon/8f68f1d7467161562d64138aefee7d26c7e68130/48b598ca7c27ac23.json](../../../wiki/dossiers/entropy-research/devon/8f68f1d7467161562d64138aefee7d26c7e68130/48b598ca7c27ac23.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Architecture comprises Environments (LocalShell, User), Tools, Agents (TaskAgent, ConversationalAgent), a Session orchestrator, and a config object, each with base classes in devon_agent modules. -- evidence: [contributor.md#L5-L10](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/contributor.md#L5-L10) (`clm_348cda2931101d5673d42b601d317ea466ed39fb8446eecf32b69cd47543f265`)

## design-choices (1 claim(s))

- [observation/documented] The agent is documented to only access files and folders in the directory it was started from, and users can correct it mid-action. -- evidence: [README.md#L111-L112](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L111-L112) (`clm_410eeadab9a9b048927a2028c47e957cdbbbbf3257edf51cf73ab659ddc5e955`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, branch, commit descriptively, and open pull requests; PRs should include a descriptive title, rationale, test steps, and screenshots, and a maintainer reviews before merging. -- evidence: [CONTRIBUTING.md#L63-L66](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L63-L66), [CONTRIBUTING.md#L68-L68](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L68-L68), [CONTRIBUTING.md#L15-L20](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L15-L20) (`clm_a1f55bc5e366107fde5d04645190cca2e4a4ed6bfee71d3d310fdce72324f995`)
- [observation/documented] Repository development practice: coding conventions require 4-space indentation, PEP 8 style, docstrings for public code, and descriptive names; local setup runs build.sh with DEVON_TELEMETRY_DISABLED=true. -- evidence: [CONTRIBUTING.md#L32-L33](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L32-L33), [CONTRIBUTING.md#L28-L30](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L28-L30), [CONTRIBUTING.md#L54-L57](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L54-L57) (`clm_f9c3de81a775341853e5f1ad9f418729260f7b379e065e4381fd1064b60fb732`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product ships as a backend installed via pipx (devon_agent) with a main UI run through npx devon-ui. -- evidence: [README.md#L45-L45](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L45-L45), [README.md#L60-L63](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L60-L63), [README.md#L48-L49](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L48-L49) (`clm_5280e2df4fdd745487c5c948e11ef64520db7c71d29424aa8094cc6601c5065a`)
- [observation/documented] A terminal interface exists, installed globally via npm as devon-tui and launched with the devon-tui command. -- evidence: [README.md#L73-L76](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L73-L76), [README.md#L78-L85](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L78-L85), [README.md#L104-L107](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L104-L107) (`clm_58c0f27c4120df079fda8b4c48ce40d10dbdcad9802cd44e542f7ce3a55a0d79`)
- [observation/documented] The TUI offers a --debug mode and a --help flag listing available commands. -- evidence: [README.md#L116-L119](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L116-L119), [README.md#L153-L156](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L153-L156) (`clm_4d0f083011863f5728f4354129479fe11e18c08aaa4aca9fbd4c93a4cf0924bf`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Communication between agents, tools, and environments happens via an event handler/emitter system whose handlers are declared in the Session; registering tools and environments requires no handler changes. -- evidence: [contributor.md#L13-L15](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/contributor.md#L13-L15) (`clm_0350cf7218bee21d88c2524379173949ac9df7d9b1094114483ee4d8033e0c62`)

## tools-permissions (1 claim(s))

- [observation/documented] The product collects basic event-type and failure telemetry, which users can disable by setting DEVON_TELEMETRY_DISABLED=true. -- evidence: [README.md#L249-L249](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L249-L249), [README.md#L251-L254](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L251-L254) (`clm_520f54ca532d02a216d8f5b8e6315fafea568ace62a747186ed375a6af5b7e94`)

## evaluation (1 claim(s))

- [inference/documented] The project appears to track agent performance via SWE-bench Lite, citing a past milestone of beating AutoCodeRover and a goal to set SOTA there. -- evidence: [README.md#L177-L185](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L177-L185), [README.md#L198-L207](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L198-L207) (`clm_52b2a6d0924693977e4520fce30b98f172bebb599ceb0d5bd0ed15039db38f41`)

## dependencies (2 claim(s))

- [observation/documented] Running Devon requires node.js/npm, pipx, and at least one API key from Anthropic or OpenAI. -- evidence: [README.md#L28-L32](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L28-L32) (`clm_3a35abc0ab3886c491577e5428afa1e059f7c475970138a961f111750923fb56`)
- [observation/documented] Supported models include Claude 3.5 Sonnet, GPT4-o, Groq llama3-70b, and Ollama deepseek-coder:6.7b, with Gemini 1.5 Pro planned but unchecked. -- evidence: [README.md#L177-L185](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L177-L185), [README.md#L138-L144](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L138-L144) (`clm_d624435eb0f1d70e5354ad13d8fe8e4ce0eae579dca448c886587106cbb67096`)

## limitations (2 claim(s))

- [observation/documented] Documented limitations: minimal functionality for non-Python languages, sometimes needing to specify the target file, and immature local mode with significantly degraded performance. -- evidence: [README.md#L123-L125](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L123-L125), [README.md#L168-L170](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L168-L170) (`clm_4d0d33b3d19d15a490dc413142a8253f34c807ea17b37ff3c25c282a85b44c74`)
- [observation/documented] Windows support is not yet available; the README says the team is currently working on it. -- evidence: [README.md#L34-L34](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L34-L34) (`clm_a29750042a02082d9c8efc55eaa24d128ea90fa21bb813c68f30cc30023641ac`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

