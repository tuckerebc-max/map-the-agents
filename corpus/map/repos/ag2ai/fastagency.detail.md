# ag2ai/fastagency -- full detail

[Back to orientation](fastagency.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/ag2ai/fastagency/f353682dffc61962e6450eb9be3eaf69579d39bd/5673688867519c3b.json](../../../wiki/dossiers/ag2ai/fastagency/f353682dffc61962e6450eb9be3eaf69579d39bd/5673688867519c3b.json)

## specifications (1 claim(s))

- [observation/documented] FastAgency supports importing an OpenAPI specification and connecting it to agents with minimal additional code, enabling external API integration in workflows. -- evidence: [README.md#L71-L71](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L71-L71) (`clm_08a267477013d7f53e927cca781a0e549ca39855294d032f57c51fc238363e31`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] FastAgency positions itself not as another agentic framework but as a deployment layer over AG2, scaling notebook prototypes to production applications. -- evidence: [README.md#L60-L61](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L60-L61), [README.md#L63-L63](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L63-L63) (`clm_cc3026f0496da0adfc997066380c99ea09bb20ff2380cad77e004c041832ac0c`)
- [observation/documented] The architecture uses chainable network adapters intended to build scalable production architectures for serving workflows. -- evidence: [README.md#L97-L99](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L97-L99) (`clm_6f36ef407729bf6347b64a695cf33f5113f2dc597e53e87cbd96ccf4018e3f81`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the README strongly recommends Cookiecutter for project setup, which scaffolds structure, dependencies, a devcontainer, and generated tests verified by running pytest. -- evidence: [README.md#L157-L157](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L157-L157), [README.md#L110-L110](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L110-L110), [README.md#L159-L161](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L159-L161) (`clm_234968941a9f795f1d8bdee7911c48f3587db5c2ef4031fe68a172505abb39fc`)
- [observation/documented] Repository development practice: cookiecutter-generated projects include scripts to build and run Docker images and to deploy to Fly.io, with GitHub Actions auto-deployment on push to main using FLY_API_TOKEN and OPENAI_API_KEY secrets. -- evidence: [README.md#L286-L286](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L286-L286), [README.md#L258-L260](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L258-L260), [README.md#L256-L256](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L256-L256), [README.md#L288-L289](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L288-L289), [README.md#L280-L282](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L280-L282), [README.md#L266-L268](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L266-L268), [README.md#L284-L284](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L284-L284) (`clm_36b279565ba93fbdfbb8280de0775cd0544268a2b646fc8a3bc56db6c8b01c5d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] FastAgency offers a common programming interface so the same workflow can run in console apps via ConsoleUI and web apps via MesopUI without rewriting code. -- evidence: [README.md#L91-L91](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L91-L91), [README.md#L69-L69](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L69-L69), [README.md#L93-L93](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L93-L93) (`clm_23a6c0522968dbab65aa5eeee084bf925f856408097cbdf3d4b843c64cdeee74`)
- [observation/documented] The product includes a command-line interface for running workflows, passing parameters, and monitoring agent interactions from the terminal. -- evidence: [README.md#L75-L75](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L75-L75) (`clm_a3342aa1445caad62c76e04f4e46c4cc0574b481ca5cfa5659a96d5a7c41ffb7`)
- [observation/documented] A FastAPIAdapter lets workflows be served as a REST API on a FastAPI ASGI server across multiple workers. -- evidence: [README.md#L101-L101](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L101-L101) (`clm_1926e186f0c6bbaf6e1eac59109872f296e61fb593fef7bb56b453261d066403`)
- [observation/documented] A NatsAdapter uses NATS.io via FastStream as a message broker for scalable deployments, optionally combined with FastAPIAdapter for authenticated public workflows. -- evidence: [README.md#L103-L103](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L103-L103) (`clm_46274608dad0efd505278025dbc2895ed9984e5bea9527ecde9a464dd87c7f17`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] FastAgency ships a Tester Class for writing and executing tests of multi-agent workflows, verifying agent behavior and integrating with CI pipelines. -- evidence: [README.md#L73-L73](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L73-L73) (`clm_61d377a861d3a03447c3cad621cf10b0e457764a2309bc5252cb693a740e88ed`)

## dependencies (2 claim(s))

- [observation/documented] AG2 (formerly AutoGen) is currently the only supported runtime for defining workflows. -- evidence: [README.md#L85-L85](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L85-L85), [README.md#L89-L89](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L89-L89) (`clm_db63b0f8007debe477351a782ceb3c9282b06f0dd27350eec78c7c42f5eddaf5`)
- [observation/documented] Running LLM-based applications requires an LLM API key; the docs use OpenAI's key set via the OPENAI_API_KEY environment variable, and the example workflow configures gpt-4o-mini. -- evidence: [README.md#L144-L146](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L144-L146), [README.md#L142-L142](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L142-L142), [README.md#L193-L197](https://github.com/ag2ai/fastagency/blob/f353682dffc61962e6450eb9be3eaf69579d39bd/README.md#L193-L197) (`clm_1606d92df48c54c3114efb793334d68a2b4add2c604083f22f2cfb581e848725`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

