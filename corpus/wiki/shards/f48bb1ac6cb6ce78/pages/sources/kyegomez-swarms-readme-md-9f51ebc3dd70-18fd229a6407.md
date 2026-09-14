---
access: public
aliases: []
claim_ids:
- clm_08b8665d877a70035e03a9d4595d18a368fc6605f497bfa2e679ed63283609b4
- clm_0dcec379c6a583af97efb6c3c21430aca0dc1d70ba890715abbe13dc9037d06a
- clm_0fcc350359fc917b4448bd2a7af2572b2cdba29c5b079a2c89efe353871e38bb
- clm_25d14cd5e8dfadd6a6cb6a3a71b092bb7e72fc752aa3f71e4a2f3e4f193f3928
- clm_26aa81bc9175b0a72cd767f02ed4cb77af1513f3212b8fef134a7ecc7aaad29c
- clm_3cf2105d151c433a18f5ef13dd36b71a8d615bc74d4781fd7bc58d2170fbd7ef
- clm_41715de8b2b446cedfe97a2721d4ecfd36713dd96dc4a56690d7e49eb8ae7752
- clm_58042663931f4bf7906cc98c9c1f302ab7f707f9eb8919bb08fe474ee8fa30c4
- clm_5e8a31df2bdd8ebaed5892ae9a93701c9173fccc950a1b27837c2ceb30697282
- clm_6f75de20cc0a2d338ab99fa852024b212bc62e048cbed21cedf0c24cefe2ee82
- clm_79eef036929e3ac921edc959c46f9e79e52bc1177b8451622242c1f92daef386
- clm_7dd58262a7b7bd32aa04b9542be2a0c11212e44016f7b347e1be9de582740c97
- clm_9728abf0138f4665701dc0c994861b9afae7149172719c1b32a720d84e28820a
- clm_99cb018d1ac9621f71bda330b1f2aaf2e384dfd4557ffffab88f4b3a5f71eebc
- clm_9a86fe602b3f7a669d84285f4c71deda6e12e940474ae17805410b88d484f82c
- clm_a01cb6c1fc9996071c5121827391d951e4efda94db51b1505c7d22ebe0113503
- clm_b0a1a7cff6ad2828323a97e886ac53a98db2ea73f4afdca8da22edacd0eb850d
- clm_b5b7a74117483051b24cb93bfb973bf10de86d1dc615b2fdb925baf81dc63aa6
- clm_b97324d89b494b5aecacea5633c42f4099248a2bc421187688106f2f952c7b9d
maturity: draft
page_id: pg_bcc72c5d61b858f9a0f818fd229a6407
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_66e48c717da254ed924c9621529c32d7
title: kyegomez/swarms/README.md @ 9f51ebc3dd70
updated_at: '2026-09-14T02:11:22Z'
---

# kyegomez/swarms/README.md @ 9f51ebc3dd70

<!-- rcw:begin owner=source:src_66e48c717da254ed924c9621529c32d7 block=evidence -->
- The framework ships prebuilt multi-agent architectures including SequentialWorkflow, ConcurrentWorkflow, AgentRearrange, GraphWorkflow, MixtureOfAgents, GroupChat, and ForestSwarm. [@claim:clm_08b8665d877a70035e03a9d4595d18a368fc6605f497bfa2e679ed63283609b4]
- Agents can consume external tools via MCP by setting mcp_url or mcp_urls, gaining tools from one or many MCP servers without manual configuration. [@claim:clm_0dcec379c6a583af97efb6c3c21430aca0dc1d70ba890715abbe13dc9037d06a]
- MCPDeployer servers support static API keys, a custom auth callable reading request headers, or an MCP TokenVerifier with required scopes; servers refuse to start without auth unless allow_anonymous=True is passed. [@claim:clm_0fcc350359fc917b4448bd2a7af2572b2cdba29c5b079a2c89efe353871e38bb]
- The package is installable via pip, uv, or poetry, and from source by cloning the repository and installing requirements.txt; a prebuilt Docker image kyegomez/swarms is also published. [@claim:clm_25d14cd5e8dfadd6a6cb6a3a71b092bb7e72fc752aa3f71e4a2f3e4f193f3928]
- Agents are configured via parameters such as model_name, max_loops, system_prompt, agent_name, autosave, and verbose; max_loops='auto' lets the agent decide when its task is complete. [@claim:clm_26aa81bc9175b0a72cd767f02ed4cb77af1513f3212b8fef134a7ecc7aaad29c]
- HeavySwarm examples import tooling from a separate swarms_tools package (e.g. exa_search), suggesting web-search tools live outside the core library. [@claim:clm_3cf2105d151c433a18f5ef13dd36b71a8d615bc74d4781fd7bc58d2170fbd7ef]
- AgentRearrange uses an einsum-inspired string syntax (e.g. 'researcher -> writer, editor') to define non-linear agent relationships and dynamic routing. [@claim:clm_41715de8b2b446cedfe97a2721d4ecfd36713dd96dc4a56690d7e49eb8ae7752]
- MCPDeployer exposes any agent or swarm as an MCP server where each target becomes one tool, supporting streamable HTTP (default), SSE, and stdio transports. [@claim:clm_58042663931f4bf7906cc98c9c1f302ab7f707f9eb8919bb08fe474ee8fa30c4]
- SequentialWorkflow runs agents in a strict linear pipeline where each agent's output feeds the next agent's input. [@claim:clm_5e8a31df2bdd8ebaed5892ae9a93701c9173fccc950a1b27837c2ceb30697282]
- Swarms is a Python multi-agent orchestration framework whose fundamental building block is an Agent combining an LLM, tools, and memory. [@claim:clm_6f75de20cc0a2d338ab99fa852024b212bc62e048cbed21cedf0c24cefe2ee82]
- HierarchicalSwarm implements a director-worker pattern where a director plans, distributes tasks to workers, evaluates results, and can issue feedback-loop orders. [@claim:clm_79eef036929e3ac921edc959c46f9e79e52bc1177b8451622242c1f92daef386]
- SwarmRouter provides a single interface to run different swarm types by changing the swarm_type parameter, including SequentialWorkflow, ConcurrentWorkflow, and MixtureOfAgents. [@claim:clm_7dd58262a7b7bd32aa04b9542be2a0c11212e44016f7b347e1be9de582740c97]
- AutoSwarmBuilder automatically generates specialized agents and workflow configurations from a natural-language task description. [@claim:clm_9728abf0138f4665701dc0c994861b9afae7149172719c1b32a720d84e28820a]
- Configuration uses environment variables including OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY, and WORKSPACE_DIR, with further setup documented externally. [@claim:clm_99cb018d1ac9621f71bda330b1f2aaf2e384dfd4557ffffab88f4b3a5f71eebc]
- GraphWorkflow orchestrates agents as DAG nodes with dependency edges, topological ordering, and automatic parallel execution of independent branches. [@claim:clm_9a86fe602b3f7a669d84285f4c71deda6e12e940474ae17805410b88d484f82c]
- GroupChat is an asynchronous, self-selecting chat where every agent carries RESPOND_TOOL and uses a forced respond(score, message) call with a score threshold to decide whether to reply, ending on max_loops or an idle timeout. [@claim:clm_a01cb6c1fc9996071c5121827391d951e4efda94db51b1505c7d22ebe0113503]
- HeavySwarm runs a five-phase workflow (question generation, research, analysis, alternatives, verification) using specialized agents with optional dashboard visualization. [@claim:clm_b0a1a7cff6ad2828323a97e886ac53a98db2ea73f4afdca8da22edacd0eb850d]
- ConcurrentWorkflow executes multiple agents simultaneously on the same task for parallel, high-throughput processing. [@claim:clm_b5b7a74117483051b24cb93bfb973bf10de86d1dc615b2fdb925baf81dc63aa6]
- SocialAlgorithms lets users supply an arbitrary callable defining a custom sequence of communication between agents, with the run result exposing final_outputs. [@claim:clm_b97324d89b494b5aecacea5633c42f4099248a2bc421187688106f2f952c7b9d]
<!-- rcw:end owner=source:src_66e48c717da254ed924c9621529c32d7 block=evidence -->

## Researcher notes

