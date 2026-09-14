# sourcegraph/cody-public-snapshot -- full detail

[Back to orientation](cody-public-snapshot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sourcegraph/cody-public-snapshot/8e20ac6c1460c08b0db581c0204658112a246eda/04923e036f317313.json](../../../wiki/dossiers/sourcegraph/cody-public-snapshot/8e20ac6c1460c08b0db581c0204658112a246eda/04923e036f317313.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] Documented features include chat with codebase context, single- and multi-line autocomplete, inline edit/refactor, and customizable prompts such as Document, Explain, and Generate Unit Tests. -- evidence: [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50) (`clm_b7c2c2bb3d9a781b155c4b0b0391ed7025df41b829b747485faacf7190f19b98`)
- [observation/documented] The edit workflow applies changes with code lenses for Show diff, Accept All, Retry, Undo, Accept, and Reject, and shows a 'Cody is working...' notification while edits apply. -- evidence: [TESTING.md#L43-L55](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L43-L55) (`clm_7acf56d7059983d5ce9970c193c162614488a9fc3e9a5442d7e91ea2dc46ba57`)
- [observation/documented] Custom commands can be defined in user or workspace settings JSON with a prompt and context (e.g. currentFile or selection) and run from the Custom Commands menu. -- evidence: [TESTING.md#L257-L260](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L257-L260), [TESTING.md#L202-L211](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L202-L211), [TESTING.md#L222-L233](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L222-L233), [TESTING.md#L242-L253](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L242-L253) (`clm_8b32793d9a4ce4b22050998856df63e307ac1120cd9ec1ff8a1ceed907c87dff`)
- [inference/documented] A Storybook story for 'agentic/AllToolCells' suggests the webview UI renders tool-state cells for file views, file diffs, terminal output, and generic status output. -- evidence: [restored.txt#L81-L97](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/restored.txt#L81-L97), [restored.txt#L62-L79](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/restored.txt#L62-L79), [restored.txt#L11-L15](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/restored.txt#L11-L15), [restored.txt#L143-L160](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/restored.txt#L143-L160), [restored.txt#L126-L141](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/restored.txt#L126-L141) (`clm_2f18016b5a7bf52c5c6c92468483b12833d5c07bde3be2bc0f449094f098ea8c`)

## design-choices (2 claim(s))

- [observation/documented] Cody retrieves context from local and remote codebases via advanced/semantic search, and supports @-mentioning files to target specific context. -- evidence: [README.md#L37-L37](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L37-L37), [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50) (`clm_9a23ccc1daf791046f47a113476e7b7814f1078b393ce2a53211b53284609b87`)
- [observation/documented] The product advertises swappable LLMs, naming Anthropic Claude Sonnet 4, OpenAI GPT-4o, Mixtral, and Gemini 1.5 among supported models. -- evidence: [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50) (`clm_68a66527d33b1384059d12d8a675ada3f13364cac63f1077e4f671799410ac79`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: AGENT.md lists build (pnpm build), lint/format via Biome, and unit, integration, and E2E test commands such as pnpm test:unit and pnpm -C vscode run test:integration. -- evidence: [AGENT.md#L4-L10](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/AGENT.md#L4-L10) (`clm_936b5d6da33bf136105b6d340e3a29fb2115e521d03b8af2bb8f6e141b393de0`)
- [observation/documented] Repository development practice: AGENT.md prescribes code style including 4-space indentation, 105-character lines, avoiding 'as' casts outside tests, and telemetry event names of the form cody.<feature>. -- evidence: [AGENT.md#L13-L25](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/AGENT.md#L13-L25) (`clm_ad807913e79800c47c0521049d253b076ddf801c8b3432aa492f161c58e94450`)
- [observation/documented] Repository development practice: ARCHITECTURE.md gives async-pattern guidance—Promises for single async results, Observables for changing values, and generators for demand-driven multiple values. -- evidence: [ARCHITECTURE.md#L44-L49](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/ARCHITECTURE.md#L44-L49) (`clm_c64831fcb52d835985c3ea6dc918cde1504789919dd7175e259a5277700baa1c`)
- [observation/documented] Repository development practice: telemetry rules require transcript data to go only in privateMetadata with a recordsPrivateMetadataTranscript flag, and only for DotCom (Free) users. -- evidence: [ARCHITECTURE.md#L61-L73](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/ARCHITECTURE.md#L61-L73) (`clm_1d8854f3cfb6b107b191e949ef69ae37637537ac90099409d4f3b1e807311764`)
- [observation/documented] Repository development practice: TESTING.md is a manual QA checklist covering commands (Explain, Edit, Test, Document, Smell), chat UX, LLM selection, and autocomplete behaviors. -- evidence: [TESTING.md#L3-L21](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L3-L21) (`clm_df35acfc3095456ac75aeb7bedd245f63631101fed14aab6338f5bb5ab97f0e8`)
- [observation/documented] Repository development practice: token-counting guidance says to express limits in tokens, apply limits after model selection, and count tokens after appending strings when possible. -- evidence: [ARCHITECTURE.md#L134-L135](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/ARCHITECTURE.md#L134-L135), [ARCHITECTURE.md#L137-L139](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/ARCHITECTURE.md#L137-L139), [ARCHITECTURE.md#L132-L132](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/ARCHITECTURE.md#L132-L132) (`clm_6556f5b9db4e6c95095816dab85a8d96a87549be7e70f98638033981995bdc1f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Cody is available as a VS Code extension, a JetBrains plugin, and a web chat client. -- evidence: [README.md#L39-L39](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L39-L39) (`clm_b4754a85be718fff8371fae7171a76c67de77ad9ed76d3dd76f2f0b6e9ad595b`)
- [observation/documented] The editor extensions work with Sourcegraph Cloud and self-hosted Sourcegraph Enterprise Server instances on version 5.1 or later. -- evidence: [README.md#L91-L92](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L91-L92) (`clm_2c49048bb653102bb7c490f9977842436e86043d5e402b5ca7da4e841e393b60`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Individual usage currently requires a free Sourcegraph.com account, which the README says exists to prevent abuse of free Anthropic/OpenAI LLM usage. -- evidence: [README.md#L81-L81](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L81-L81) (`clm_1a59f460494d0fbc6bfaf1a6aacee77224f48ab04929e15309aa46707496ce58`)

## limitations (1 claim(s))

- [observation/documented] Per the QA checklist, Free users' chat defaults to Claude 2 with no LLM switching without upgrading to Pro, while Pro users can switch and enterprise users cannot change the LLM. -- evidence: [TESTING.md#L276-L278](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L276-L278) (`clm_b623466d176947f8bb5d4c93d9a67928fb4940c6e10b6a93fe50357352e0f8f1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

