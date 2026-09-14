# furudo-erika/ai-testing-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 051b0888e9d3 @ 9e7a156f697edc7b

## Summary (orientation draft, not independently verified)

The snapshot is a README-only view of an AI Testing Agent that uses an LLM via OpenRouter to plan, generate, run, and iteratively refine pytest tests for a user's API. Evidence covers architecture, CLI commands, environment variables, and prompting guidance; no code or contributor/eval evidence is present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project comprises main.py (a sample FastAPI app), api_tester.py (CLI logic for plan/generate/run/feedback), agent_tools.py, agent.py, and generated_tests.py. -- evidence: [README.md#L49-L58](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L49-L58)
- design-choices (3 claim(s)):
  - [observation/documented] By default the agent assumes the target API has specific REST routes like /api/endpoint, but users can customize this via prompts. -- evidence: [README.md#L10-L10](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L10-L10)
  - [observation/documented] Generated tests target TEST_API_URL if set, otherwise defaulting to http://localhost:8000. -- evidence: [README.md#L78-L81](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L78-L81), [README.md#L71-L72](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L71-L72)
- workflows (2 claim(s)):
  - [observation/documented] Documented usage workflow: start the API with uvicorn on port 8000, run python agent.py in a second terminal, then issue Plan/Generate/Run/Feedback commands. -- evidence: [README.md#L89-L89](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L89-L89), [README.md#L97-L97](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L97-L97), [README.md#L91-L91](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L91-L91), [README.md#L99-L99](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L99-L99), [README.md#L109-L116](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L109-L116)
  - [observation/documented] Troubleshooting guidance covers missing OPENROUTER_API_KEY, unexpected 401 responses needing an Authorization header, and mismatched generated routes, suggesting explicit prompts or feedback. -- evidence: [README.md#L155-L156](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L155-L156), [README.md#L158-L159](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L158-L159), [README.md#L161-L162](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L161-L162), [README.md#L164-L165](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L164-L165)
- skills-patterns (1 claim(s)):
  - [observation/documented] Prompting guidance advises explicitly describing endpoints, specifying desired test names and structure, and providing example test-code skeletons to steer output. -- evidence: [README.md#L133-L135](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L133-L135), [README.md#L140-L141](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L140-L141), [README.md#L137-L138](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L137-L138)
- interfaces (2 claim(s)):
  - [observation/documented] api_tester.py exposes a command-line interface with subcommands plan, generate, run, and feedback, usable directly without the chat agent. -- evidence: [README.md#L122-L125](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L122-L125), [README.md#L109-L116](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L109-L116)
  - [observation/documented] Running python agent.py starts an interactive prompt where the user types commands or instructions, with 'quit' or 'exit' to stop. -- evidence: [README.md#L105-L105](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L105-L105), [README.md#L99-L99](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L99-L99), [README.md#L101-L103](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L101-L103)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] agent.py is a LangChain chatbot whose actions (Plan, Generate, Run, Feedback) invoke tools in agent_tools.py, which run api_tester.py commands in subprocesses. -- evidence: [README.md#L39-L43](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L39-L43)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README's example install lists fastapi, uvicorn, requests, pytest, langchain, and openai as pip dependencies, and requires an OpenRouter API key. -- evidence: [README.md#L64-L66](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L64-L66), [README.md#L68-L69](https://github.com/furudo-erika/ai-testing-agent/blob/051b0888e9d381e7ba3940ec4d7a52e3e7e61f9c/README.md#L68-L69)
- limitations (1 claim(s)):
More evidence: [full detail](ai-testing-agent.detail.md)

Metadata and full claim list: [full detail](ai-testing-agent.detail.md)
Human notes ([notes](ai-testing-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
