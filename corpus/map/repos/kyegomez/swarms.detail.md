# kyegomez/swarms -- full detail

[Back to orientation](swarms.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kyegomez/swarms/9f51ebc3dd702d71a28f75c308631506b8e00cc0/aa32ac6bb13251a7.json](../../../wiki/dossiers/kyegomez/swarms/9f51ebc3dd702d71a28f75c308631506b8e00cc0/aa32ac6bb13251a7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Swarms is a Python multi-agent orchestration framework whose fundamental building block is an Agent combining an LLM, tools, and memory. -- evidence: [README.md#L120-L120](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L120-L120), [README.md#L52-L52](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L52-L52), [README.md#L49-L50](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L49-L50) (`clm_6f75de20cc0a2d338ab99fa852024b212bc62e048cbed21cedf0c24cefe2ee82`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agents are configured via parameters such as model_name, max_loops, system_prompt, agent_name, autosave, and verbose; max_loops='auto' lets the agent decide when its task is complete. -- evidence: [README.md#L144-L155](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L144-L155), [README.md#L126-L131](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L126-L131), [README.md#L139-L139](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L139-L139) (`clm_26aa81bc9175b0a72cd767f02ed4cb77af1513f3212b8fef134a7ecc7aaad29c`)
- [observation/documented] Agents can consume external tools via MCP by setting mcp_url or mcp_urls, gaining tools from one or many MCP servers without manual configuration. -- evidence: [README.md#L182-L190](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L182-L190), [README.md#L177-L177](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L177-L177) (`clm_0dcec379c6a583af97efb6c3c21430aca0dc1d70ba890715abbe13dc9037d06a`)
- [observation/documented] MCPDeployer exposes any agent or swarm as an MCP server where each target becomes one tool, supporting streamable HTTP (default), SSE, and stdio transports. -- evidence: [README.md#L214-L215](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L214-L215), [README.md#L232-L232](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L232-L232), [README.md#L201-L201](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L201-L201) (`clm_58042663931f4bf7906cc98c9c1f302ab7f707f9eb8919bb08fe474ee8fa30c4`)
- [observation/documented] SocialAlgorithms lets users supply an arbitrary callable defining a custom sequence of communication between agents, with the run result exposing final_outputs. -- evidence: [README.md#L762-L767](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L762-L767), [README.md#L722-L722](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L722-L722), [README.md#L770-L772](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L770-L772), [README.md#L728-L730](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L728-L730) (`clm_b97324d89b494b5aecacea5633c42f4099248a2bc421187688106f2f952c7b9d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (10 claim(s))

- [observation/documented] The framework ships prebuilt multi-agent architectures including SequentialWorkflow, ConcurrentWorkflow, AgentRearrange, GraphWorkflow, MixtureOfAgents, GroupChat, and ForestSwarm. -- evidence: [README.md#L52-L52](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L52-L52), [README.md#L279-L290](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L279-L290) (`clm_08b8665d877a70035e03a9d4595d18a368fc6605f497bfa2e679ed63283609b4`)
- [observation/documented] SequentialWorkflow runs agents in a strict linear pipeline where each agent's output feeds the next agent's input. -- evidence: [README.md#L265-L265](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L265-L265), [README.md#L318-L318](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L318-L318), [README.md#L298-L298](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L298-L298) (`clm_5e8a31df2bdd8ebaed5892ae9a93701c9173fccc950a1b27837c2ceb30697282`)
- [observation/documented] ConcurrentWorkflow executes multiple agents simultaneously on the same task for parallel, high-throughput processing. -- evidence: [README.md#L330-L330](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L330-L330), [README.md#L358-L361](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L358-L361), [README.md#L364-L366](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L364-L366) (`clm_b5b7a74117483051b24cb93bfb973bf10de86d1dc615b2fdb925baf81dc63aa6`)
- [observation/documented] AgentRearrange uses an einsum-inspired string syntax (e.g. 'researcher -> writer, editor') to define non-linear agent relationships and dynamic routing. -- evidence: [README.md#L390-L393](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L390-L393), [README.md#L387-L387](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L387-L387), [README.md#L375-L375](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L375-L375) (`clm_41715de8b2b446cedfe97a2721d4ecfd36713dd96dc4a56690d7e49eb8ae7752`)
- [observation/documented] GraphWorkflow orchestrates agents as DAG nodes with dependency edges, topological ordering, and automatic parallel execution of independent branches. -- evidence: [README.md#L417-L421](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L417-L421), [README.md#L403-L403](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L403-L403), [README.md#L435-L438](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L435-L438) (`clm_9a86fe602b3f7a669d84285f4c71deda6e12e940474ae17805410b88d484f82c`)
- [observation/documented] SwarmRouter provides a single interface to run different swarm types by changing the swarm_type parameter, including SequentialWorkflow, ConcurrentWorkflow, and MixtureOfAgents. -- evidence: [README.md#L444-L444](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L444-L444), [README.md#L469-L471](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L469-L471), [README.md#L462-L465](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L462-L465), [README.md#L478-L491](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L478-L491) (`clm_7dd58262a7b7bd32aa04b9542be2a0c11212e44016f7b347e1be9de582740c97`)
- [observation/documented] AutoSwarmBuilder automatically generates specialized agents and workflow configurations from a natural-language task description. -- evidence: [README.md#L500-L500](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L500-L500), [README.md#L530-L534](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L530-L534), [README.md#L517-L522](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L517-L522) (`clm_9728abf0138f4665701dc0c994861b9afae7149172719c1b32a720d84e28820a`)
- [observation/documented] HierarchicalSwarm implements a director-worker pattern where a director plans, distributes tasks to workers, evaluates results, and can issue feedback-loop orders. -- evidence: [README.md#L662-L666](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L662-L666), [README.md#L612-L612](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L612-L612), [README.md#L643-L649](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L643-L649) (`clm_79eef036929e3ac921edc959c46f9e79e52bc1177b8451622242c1f92daef386`)
- [observation/documented] HeavySwarm runs a five-phase workflow (question generation, research, analysis, alternatives, verification) using specialized agents with optional dashboard visualization. -- evidence: [README.md#L680-L690](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L680-L690), [README.md#L672-L672](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L672-L672), [README.md#L712-L712](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L712-L712), [README.md#L706-L706](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L706-L706) (`clm_b0a1a7cff6ad2828323a97e886ac53a98db2ea73f4afdca8da22edacd0eb850d`)
- [observation/documented] GroupChat is an asynchronous, self-selecting chat where every agent carries RESPOND_TOOL and uses a forced respond(score, message) call with a score threshold to decide whether to reply, ending on max_loops or an idle timeout. -- evidence: [README.md#L597-L602](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L597-L602), [README.md#L574-L574](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L574-L574), [README.md#L576-L577](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L576-L577) (`clm_a01cb6c1fc9996071c5121827391d951e4efda94db51b1505c7d22ebe0113503`)

## tools-permissions (1 claim(s))

- [observation/documented] MCPDeployer servers support static API keys, a custom auth callable reading request headers, or an MCP TokenVerifier with required scopes; servers refuse to start without auth unless allow_anonymous=True is passed. -- evidence: [README.md#L214-L215](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L214-L215), [README.md#L232-L232](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L232-L232) (`clm_0fcc350359fc917b4448bd2a7af2572b2cdba29c5b079a2c89efe353871e38bb`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The package is installable via pip, uv, or poetry, and from source by cloning the repository and installing requirements.txt; a prebuilt Docker image kyegomez/swarms is also published. -- evidence: [README.md#L73-L75](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L73-L75), [README.md#L92-L93](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L92-L93), [README.md#L67-L69](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L67-L69), [README.md#L81-L84](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L81-L84), [README.md#L59-L61](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L59-L61) (`clm_25d14cd5e8dfadd6a6cb6a3a71b092bb7e72fc752aa3f71e4a2f3e4f193f3928`)
- [observation/documented] Configuration uses environment variables including OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY, and WORKSPACE_DIR, with further setup documented externally. -- evidence: [README.md#L108-L108](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L108-L108), [README.md#L110-L115](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L110-L115) (`clm_99cb018d1ac9621f71bda330b1f2aaf2e384dfd4557ffffab88f4b3a5f71eebc`)
- [inference/documented] HeavySwarm examples import tooling from a separate swarms_tools package (e.g. exa_search), suggesting web-search tools live outside the core library. -- evidence: [README.md#L680-L690](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L680-L690), [README.md#L678-L678](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L678-L678) (`clm_3cf2105d151c433a18f5ef13dd36b71a8d615bc74d4781fd7bc58d2170fbd7ef`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

