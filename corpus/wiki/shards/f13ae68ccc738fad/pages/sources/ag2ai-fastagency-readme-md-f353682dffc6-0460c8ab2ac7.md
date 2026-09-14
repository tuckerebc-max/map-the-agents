---
access: public
aliases: []
claim_ids:
- clm_08a267477013d7f53e927cca781a0e549ca39855294d032f57c51fc238363e31
- clm_1606d92df48c54c3114efb793334d68a2b4add2c604083f22f2cfb581e848725
- clm_1926e186f0c6bbaf6e1eac59109872f296e61fb593fef7bb56b453261d066403
- clm_234968941a9f795f1d8bdee7911c48f3587db5c2ef4031fe68a172505abb39fc
- clm_23a6c0522968dbab65aa5eeee084bf925f856408097cbdf3d4b843c64cdeee74
- clm_36b279565ba93fbdfbb8280de0775cd0544268a2b646fc8a3bc56db6c8b01c5d
- clm_46274608dad0efd505278025dbc2895ed9984e5bea9527ecde9a464dd87c7f17
- clm_61d377a861d3a03447c3cad621cf10b0e457764a2309bc5252cb693a740e88ed
- clm_6f36ef407729bf6347b64a695cf33f5113f2dc597e53e87cbd96ccf4018e3f81
- clm_a3342aa1445caad62c76e04f4e46c4cc0574b481ca5cfa5659a96d5a7c41ffb7
- clm_cc3026f0496da0adfc997066380c99ea09bb20ff2380cad77e004c041832ac0c
- clm_db63b0f8007debe477351a782ceb3c9282b06f0dd27350eec78c7c42f5eddaf5
maturity: draft
page_id: pg_251152bf12fa59cb8f090460c8ab2ac7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca7cd471a0695bf7a3835ebb264c4130
title: ag2ai/fastagency/README.md @ f353682dffc6
updated_at: '2026-09-14T03:30:41Z'
---

# ag2ai/fastagency/README.md @ f353682dffc6

<!-- rcw:begin owner=source:src_ca7cd471a0695bf7a3835ebb264c4130 block=evidence -->
- FastAgency supports importing an OpenAPI specification and connecting it to agents with minimal additional code, enabling external API integration in workflows. [@claim:clm_08a267477013d7f53e927cca781a0e549ca39855294d032f57c51fc238363e31]
- Running LLM-based applications requires an LLM API key; the docs use OpenAI's key set via the OPENAI_API_KEY environment variable, and the example workflow configures gpt-4o-mini. [@claim:clm_1606d92df48c54c3114efb793334d68a2b4add2c604083f22f2cfb581e848725]
- A FastAPIAdapter lets workflows be served as a REST API on a FastAPI ASGI server across multiple workers. [@claim:clm_1926e186f0c6bbaf6e1eac59109872f296e61fb593fef7bb56b453261d066403]
- Repository development practice: the README strongly recommends Cookiecutter for project setup, which scaffolds structure, dependencies, a devcontainer, and generated tests verified by running pytest. [@claim:clm_234968941a9f795f1d8bdee7911c48f3587db5c2ef4031fe68a172505abb39fc]
- FastAgency offers a common programming interface so the same workflow can run in console apps via ConsoleUI and web apps via MesopUI without rewriting code. [@claim:clm_23a6c0522968dbab65aa5eeee084bf925f856408097cbdf3d4b843c64cdeee74]
- Repository development practice: cookiecutter-generated projects include scripts to build and run Docker images and to deploy to Fly.io, with GitHub Actions auto-deployment on push to main using FLY_API_TOKEN and OPENAI_API_KEY secrets. [@claim:clm_36b279565ba93fbdfbb8280de0775cd0544268a2b646fc8a3bc56db6c8b01c5d]
- A NatsAdapter uses NATS.io via FastStream as a message broker for scalable deployments, optionally combined with FastAPIAdapter for authenticated public workflows. [@claim:clm_46274608dad0efd505278025dbc2895ed9984e5bea9527ecde9a464dd87c7f17]
- FastAgency ships a Tester Class for writing and executing tests of multi-agent workflows, verifying agent behavior and integrating with CI pipelines. [@claim:clm_61d377a861d3a03447c3cad621cf10b0e457764a2309bc5252cb693a740e88ed]
- The architecture uses chainable network adapters intended to build scalable production architectures for serving workflows. [@claim:clm_6f36ef407729bf6347b64a695cf33f5113f2dc597e53e87cbd96ccf4018e3f81]
- The product includes a command-line interface for running workflows, passing parameters, and monitoring agent interactions from the terminal. [@claim:clm_a3342aa1445caad62c76e04f4e46c4cc0574b481ca5cfa5659a96d5a7c41ffb7]
- FastAgency positions itself not as another agentic framework but as a deployment layer over AG2, scaling notebook prototypes to production applications. [@claim:clm_cc3026f0496da0adfc997066380c99ea09bb20ff2380cad77e004c041832ac0c]
- AG2 (formerly AutoGen) is currently the only supported runtime for defining workflows. [@claim:clm_db63b0f8007debe477351a782ceb3c9282b06f0dd27350eec78c7c42f5eddaf5]
<!-- rcw:end owner=source:src_ca7cd471a0695bf7a3835ebb264c4130 block=evidence -->

## Researcher notes

