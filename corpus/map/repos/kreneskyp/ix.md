# kreneskyp/ix

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d5868fc1d56d @ c9dbd6f0b700a064

## Summary (orientation draft, not independently verified)

IX is described as a platform for designing and deploying autonomous and semi-autonomous LLM agents and workflows that can run in parallel and communicate with each other. The product includes a no-code agent editor where users drop and connect nodes into a graph representing an agent's cognitive logic, with embedded chat for testing and debugging.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] IX is described as a platform for designing and deploying autonomous and semi-autonomous LLM agents and workflows that can run in parallel and communicate with each other. -- evidence: [README.md#L31-L36](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L31-L36)
- components (2 claim(s)):
  - [observation/documented] IX implements a component config layer mapping LangChain components to a configuration graph, which dynamically renders nodes and forms in the no-code editor. -- evidence: [README.md#L84-L86](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L84-L86)
  - [observation/documented] Custom chains include LLMToolChain, ParseJSON, IxSequence, MapSubchain, ToolChooser, LLMToolChooser, ChatModerator, and Planner v3 for planning and executing task sequences. -- evidence: [CHANGELOG.md#L43-L45](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L43-L45), [CHANGELOG.md#L31-L35](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L31-L35), [CHANGELOG.md#L37-L41](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L37-L41)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: agent fixtures can be dumped with the dump_agent Django management command, which gathers the agent, chain, and component graph. -- evidence: [README.md#L304-L311](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L304-L311), [README.md#L301-L302](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L301-L302)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product includes a no-code agent editor where users drop and connect nodes into a graph representing an agent's cognitive logic, with embedded chat for testing and debugging. -- evidence: [README.md#L55-L56](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L55-L56)
  - [observation/documented] A multi-agent chat interface lets users interact with teams of agents; a default IX moderator agent delegates tasks, and specific agents can be targeted via @mentions. -- evidence: [README.md#L61-L63](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L61-L63)
- memory-state (1 claim(s)):
  - [observation/documented] The changelog describes an artifact system storing task results in the database, giving agents object permanence; artifacts can be viewed by users or reused in future tasks. -- evidence: [CHANGELOG.md#L76-L78](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L76-L78)
- orchestration (1 claim(s)):
  - [observation/documented] The agent runner backend is dockerized and triggered via a celery message queue, allowing horizontal scaling of agents running in parallel. -- evidence: [README.md#L76-L77](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L76-L77)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Supported model providers are listed as OpenAI, with Google PaLM, Anthropic, and Llama marked experimental. -- evidence: [README.md#L49-L52](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L49-L52)
- limitations (1 claim(s)):
More evidence: [full detail](ix.detail.md)

Metadata and full claim list: [full detail](ix.detail.md)
Human notes ([notes](ix.notes.md), never overwritten by build)

[Back to map index](../../index.md)
