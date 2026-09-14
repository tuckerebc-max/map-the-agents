# axflow/axflow -- full detail

[Back to orientation](axflow.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/axflow/axflow/46ed2a000a4418c85704ca04a6a6ae93f17bf230/c40d8b59470d8c68.json](../../../wiki/dossiers/axflow/axflow/46ed2a000a4418c85704ca04a6a6ae93f17bf230/c40d8b59470d8c68.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Axflow ships as a set of modules: @axflow/models (an SDK with React hooks and streaming utilities), axgen (connecting data to LLMs), and axeval (evaluating LLM output quality). -- evidence: [docs/documentation.md#L23-L25](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L23-L25), [README.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L13-L15) (`clm_1f283c213d58c1c4264ab1067d69a80940167b8713e59866908e6fe22f211f52`)
- [observation/documented] Additional modules are planned but in progress: extract (document loading/transform/chunking for vector search), serve (LLM serving with throttling, analytics, logging middleware), and finetune. -- evidence: [README.md#L17-L17](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L17-L17), [README.md#L19-L21](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L19-L21) (`clm_988b67cf7efa11b03be8b9c76c850aa9d429f263a32dd08fca8bb11d25da9e03`)

## design-choices (2 claim(s))

- [observation/documented] The framework takes a code-first approach emphasizing developer flexibility and control, aiming to break LLM workflows into manageable, intuitive components. -- evidence: [docs/documentation.md#L17-L19](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L17-L19), [README.md#L27-L29](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L27-L29) (`clm_0c8b1d11d0dda7f91b093e1a17fb76ea47307498b572a4f5978c28d5a3f0cc09`)
- [observation/documented] Modules are designed for incremental, independent adoption, which also minimizes bundle size; together they form an end-to-end AI application framework. -- evidence: [docs/documentation.md#L29-L29](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L29-L29), [README.md#L8-L9](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L8-L9) (`clm_e24304db9ceb9a808d0c3d113785e84433afb70608f2297b841cb9fc541e20dd`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the repository displays a GitHub CI workflow badge, indicating a CI pipeline for the repo. -- evidence: [README.md#L5-L6](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L5-L6) (`clm_c4143edb1b4e6c3f0d19bb876ce43c8501b1635e5a2ecd0d3a1557c3c9794265`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Axeval's API centers on EvalCases (prompt plus one or more evaluators), evaluators that score a prompt/response pair from 0 to 1, EvalResults with metadata like score and latency, Reports, and a Runner that executes suites against models. -- evidence: [docs/documentation/axeval.md#L39-L39](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L39-L39), [docs/documentation/axeval.md#L27-L27](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L27-L27), [docs/documentation/axeval.md#L47-L47](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L47-L47), [docs/documentation/axeval.md#L23-L23](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L23-L23), [docs/documentation/axeval.md#L43-L43](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L43-L43), [docs/documentation/axeval.md#L19-L19](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L19-L19) (`clm_1cef0102433248f9b952289a6deb3bb9621ebcad25da374b84dc7cc2c454d4aa`)
- [observation/documented] Built-in evaluators include match, includes, isValidJSON, and llmRubric, and users can write custom evaluators. -- evidence: [docs/documentation/axeval.md#L29-L33](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L29-L33), [docs/documentation/axeval.md#L35-L35](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L35-L35) (`clm_c1c7d0002a9a44688b55054083c625bd2bfba24388d47cf3ecbe7832715dd7bf`)
- [observation/documented] The Runner API lets users register named test suites bound to specific models (e.g., AnthropicCompletion 'claude-2', OpenAICompletion 'text-davinci-003') and run them, producing a report that can be output to formats such as stdout. -- evidence: [docs/documentation/axeval.md#L92-L93](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L92-L93), [docs/documentation/axeval.md#L99-L101](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L99-L101), [docs/documentation/axeval.md#L43-L43](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L43-L43), [docs/documentation/axeval.md#L95-L97](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L95-L97), [docs/documentation/axeval.md#L103-L105](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L103-L105) (`clm_fa69ee4b9c919429de4b8b5e20c4efd472a0d31159c3250e03fbe5d7ef2a8f92`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Axeval is a framework for test-driven LLM engineering: it supports unit-testing prompts, data-driven prompt iteration, and comparing models on latency, cost, and accuracy. -- evidence: [docs/documentation/axeval.md#L5-L7](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L5-L7), [docs/documentation/axeval.md#L3-L3](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L3-L3) (`clm_6db913c302b502e925f1e8e876d8e95ebcbf3ca835cb451a098a59e4de9979fa`)

## dependencies (2 claim(s))

- [observation/documented] The @axflow/models SDK is documented as zero-dependency and modular. -- evidence: [docs/documentation.md#L23-L25](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L23-L25), [docs/index.md#L17-L24](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/index.md#L17-L24), [README.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L13-L15) (`clm_f4d8ff03d004e6159f9fa1e7b10647596bf72c862df2425e8e192b8996fca55a`)
- [observation/documented] Modules are installed independently via npm (npm i axeval; npm install @axflow/models, axgen, axeval). -- evidence: [docs/documentation.md#L31-L35](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L31-L35), [docs/documentation/axeval.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L13-L15) (`clm_05cc58f2eda14f098414c627032783f3f317cccd92de46297fb8ecaf7130d824`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets TypeScript developers building natural-language/LLM applications, with tutorials such as building a streaming React/Next.js chat app using @axflow/models with OpenAI token streaming. -- evidence: [README.md#L27-L29](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L27-L29), [docs/tutorials.md#L7-L7](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/tutorials.md#L7-L7) (`clm_83d130d5e84cca0be292bab5c3d0f9e266ff1eafd411c67336732d50d5f523cc`)

