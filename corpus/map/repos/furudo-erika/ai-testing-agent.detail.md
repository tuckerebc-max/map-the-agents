# furudo-erika/ai-testing-agent -- full detail

[Back to orientation](ai-testing-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/furudo-erika/ai-testing-agent/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/9e7a156f697edc7b.json](../../../wiki/dossiers/furudo-erika/ai-testing-agent/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/9e7a156f697edc7b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project comprises main.py (a sample FastAPI app), api_tester.py (CLI logic for plan/generate/run/feedback), agent_tools.py, agent.py, and generated_tests.py. -- evidence: [README.md#L49-L58](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L49-L58) (`clm_82abb1410525838df3370e0fc34fba9bc7b342aa9c55cbc5af4bdfd9281dbf1b`)

## design-choices (3 claim(s))

- [observation/documented] By default the agent assumes the target API has specific REST routes like /api/endpoint, but users can customize this via prompts. -- evidence: [README.md#L10-L10](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L10-L10) (`clm_0ec4f1864ea1df81abc4350f7db662fba130a7c1bfec7893dcffd8327d81d84a`)
- [observation/documented] Generated tests target TEST_API_URL if set, otherwise defaulting to http://localhost:8000. -- evidence: [README.md#L78-L81](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L78-L81), [README.md#L71-L72](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L71-L72) (`clm_07e1c93d49d31ce6288d8e82d222bed09a892e7b2b2d9fc8217b37808565b401`)
- [observation/documented] The README suggests setting temperature to 0.0 in api_tester.py to reduce randomness and obtain more deterministic LLM output. -- evidence: [README.md#L143-L144](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L143-L144) (`clm_f7a986a587365d9051db61fe4529228e363262057fb45cbb633d4ea973b8b220`)

## workflows (2 claim(s))

- [observation/documented] Documented usage workflow: start the API with uvicorn on port 8000, run python agent.py in a second terminal, then issue Plan/Generate/Run/Feedback commands. -- evidence: [README.md#L89-L89](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L89-L89), [README.md#L97-L97](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L97-L97), [README.md#L91-L91](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L91-L91), [README.md#L99-L99](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L99-L99), [README.md#L109-L116](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L109-L116) (`clm_04db88fb63a2efe1ef38ef689517acf615396ebce448d789cec943d943850f39`)
- [observation/documented] Troubleshooting guidance covers missing OPENROUTER_API_KEY, unexpected 401 responses needing an Authorization header, and mismatched generated routes, suggesting explicit prompts or feedback. -- evidence: [README.md#L155-L156](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L155-L156), [README.md#L158-L159](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L158-L159), [README.md#L161-L162](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L161-L162), [README.md#L164-L165](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L164-L165) (`clm_55e8736a2fb6f34fd32cb93f9ce01a2bc4215fc526cb95629c9015fcd287e12c`)

## skills-patterns (1 claim(s))

- [observation/documented] Prompting guidance advises explicitly describing endpoints, specifying desired test names and structure, and providing example test-code skeletons to steer output. -- evidence: [README.md#L133-L135](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L133-L135), [README.md#L140-L141](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L140-L141), [README.md#L137-L138](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L137-L138) (`clm_d3dc4b18bbf3f1aca95d741cb9625569498d2e8887fcbec0ea5005f19e9b1c98`)

## interfaces (2 claim(s))

- [observation/documented] api_tester.py exposes a command-line interface with subcommands plan, generate, run, and feedback, usable directly without the chat agent. -- evidence: [README.md#L122-L125](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L122-L125), [README.md#L109-L116](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L109-L116) (`clm_6b70563049e3fd3bbd9ac81b3757869ecb3dc00b4105630f289cb0d4e15f5477`)
- [observation/documented] Running python agent.py starts an interactive prompt where the user types commands or instructions, with 'quit' or 'exit' to stop. -- evidence: [README.md#L105-L105](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L105-L105), [README.md#L99-L99](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L99-L99), [README.md#L101-L103](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L101-L103) (`clm_ac2acb17d2057bccb2fb785b33b632d3b18a8513d532d502e94f29cb2a3a0cee`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] agent.py is a LangChain chatbot whose actions (Plan, Generate, Run, Feedback) invoke tools in agent_tools.py, which run api_tester.py commands in subprocesses. -- evidence: [README.md#L39-L43](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L39-L43) (`clm_79b2770a077d8ef0ec6678dcc1dad579d5c5c8a8f7f403dfaac97f04dbb58a0c`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README's example install lists fastapi, uvicorn, requests, pytest, langchain, and openai as pip dependencies, and requires an OpenRouter API key. -- evidence: [README.md#L64-L66](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L64-L66), [README.md#L68-L69](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L68-L69) (`clm_1e85ccd13fce97bd1a1bf72dd5d76ea778cabcec5ea42a7ae8b01c94f646ae4d`)

## limitations (1 claim(s))

- [inference/documented] Generated test quality appears heavily dependent on user prompting; the README notes LLM output quality depends heavily on how it is prompted and may invent routes not present in the real API. -- evidence: [README.md#L158-L159](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L158-L159), [README.md#L131-L131](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L131-L131) (`clm_9896ac42d13832ca47b3f02b068423d4bed36ab030c8a6514b454a41493ee773`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

