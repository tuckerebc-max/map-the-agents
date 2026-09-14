# ag2ai/fastagency

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: airtai/fastagency (github id 829825571).
Latest snapshot: commit f353682dffc6 @ 5673688867519c3b

## Summary (orientation draft, not independently verified)

Evidence consists mostly of the FastAgency README and docs navigation, describing a framework for deploying AG2 (AutoGen) multi-agent workflows via console/web UIs, CLI, and network adapters, plus cookiecutter-based project setup and deployment guidance.

## Source coverage

Source coverage (partial): 6 of 223 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] FastAgency supports importing an OpenAPI specification and connecting it to agents with minimal additional code, enabling external API integration in workflows. -- evidence: [README.md#L71-L71](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L71-L71)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] FastAgency positions itself not as another agentic framework but as a deployment layer over AG2, scaling notebook prototypes to production applications. -- evidence: [README.md#L60-L61](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L60-L61), [README.md#L63-L63](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L63-L63)
  - [observation/documented] The architecture uses chainable network adapters intended to build scalable production architectures for serving workflows. -- evidence: [README.md#L97-L99](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L97-L99)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the README strongly recommends Cookiecutter for project setup, which scaffolds structure, dependencies, a devcontainer, and generated tests verified by running pytest. -- evidence: [README.md#L157-L157](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L157-L157), [README.md#L110-L110](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L110-L110), [README.md#L159-L161](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L159-L161)
  - [observation/documented] Repository development practice: cookiecutter-generated projects include scripts to build and run Docker images and to deploy to Fly.io, with GitHub Actions auto-deployment on push to main using FLY_API_TOKEN and OPENAI_API_KEY secrets. -- evidence: [README.md#L286-L286](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L286-L286), [README.md#L258-L260](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L258-L260), [README.md#L256-L256](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L256-L256), [README.md#L288-L289](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L288-L289), [README.md#L280-L282](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L280-L282), [README.md#L266-L268](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L266-L268), [README.md#L284-L284](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L284-L284)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] FastAgency offers a common programming interface so the same workflow can run in console apps via ConsoleUI and web apps via MesopUI without rewriting code. -- evidence: [README.md#L91-L91](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L91-L91), [README.md#L69-L69](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L69-L69), [README.md#L93-L93](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L93-L93)
  - [observation/documented] The product includes a command-line interface for running workflows, passing parameters, and monitoring agent interactions from the terminal. -- evidence: [README.md#L75-L75](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L75-L75)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] FastAgency ships a Tester Class for writing and executing tests of multi-agent workflows, verifying agent behavior and integrating with CI pipelines. -- evidence: [README.md#L73-L73](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L73-L73)
- dependencies (2 claim(s)):
  - [observation/documented] AG2 (formerly AutoGen) is currently the only supported runtime for defining workflows. -- evidence: [README.md#L85-L85](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L85-L85), [README.md#L89-L89](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L89-L89)
  - [observation/documented] Running LLM-based applications requires an LLM API key; the docs use OpenAI's key set via the OPENAI_API_KEY environment variable, and the example workflow configures gpt-4o-mini. -- evidence: [README.md#L144-L146](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L144-L146), [README.md#L142-L142](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L142-L142), [README.md#L193-L197](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L193-L197)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](fastagency.detail.md)

Metadata and full claim list: [full detail](fastagency.detail.md)
Human notes ([notes](fastagency.notes.md), never overwritten by build)

[Back to map index](../../index.md)
