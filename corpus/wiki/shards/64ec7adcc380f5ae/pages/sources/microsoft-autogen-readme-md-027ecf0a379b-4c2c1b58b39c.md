---
access: public
aliases: []
claim_ids:
- clm_2d55bf39fbae7b9453b0e80a99c41da8aa3016114ca53170050ed206aa1ba9bc
- clm_330836a4a50bbb767c6e49ba6e95a1b1b97b00314b4f17d49583b1fc38df6ba9
- clm_35c00beb1130a998359aa5e584296e03aaac4d5f1c02c554cbed8cf3d82e6cc6
- clm_47a6e7c39c21669081cecbc3d27337519f68ac4fc69fedbbfecd056c957147bc
- clm_546ca5cf8918e1fb8d375053658ed3d7f71b450d1dbfc0877fcea093d30d330d
- clm_9d40236228cc60a339508b86c97c2817f585d7b6889615fc496a7c53b1b06654
- clm_a54b1a255c8ff6bff0a44e46b6f8a297017157bca813c06a2f907d7f83157c77
- clm_b63b4de204995b0ed3faaadccda99af5155dcf4e1b5980d0213ccc94c9a90b96
- clm_bb3d0a08c6a284c4f9a748e158fa74040034b7dde946ed3e72e17f6ed5ef9fd9
- clm_efbf992a5888069ec2fbe2e14fa1d69bf14a4dbf97fdc6926b448bc3d8f31519
maturity: draft
page_id: pg_a36f78820bdf5cc696434c2c1b58b39c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1ae8718794c45b7b83c6c1a7cfef43d9
title: microsoft/autogen/README.md @ 027ecf0a379b
updated_at: '2026-09-14T02:18:45Z'
---

# microsoft/autogen/README.md @ 027ecf0a379b

<!-- rcw:begin owner=source:src_1ae8718794c45b7b83c6c1a7cfef43d9 block=evidence -->
- Repository development practice: contributions are limited to bug fixes, security patches, and documentation improvements due to maintenance mode; feature work is directed to Microsoft Agent Framework. [@claim:clm_2d55bf39fbae7b9453b0e80a99c41da8aa3016114ca53170050ed206aa1ba9bc]
- The project uses the MIT license for code and CC-BY-4.0 for documentation; releases to the pyautogen PyPI package were blocked by a package-ownership change, moving to multiple packages. [@claim:clm_330836a4a50bbb767c6e49ba6e95a1b1b97b00314b4f17d49583b1fc38df6ba9]
- AssistantAgent accepts a model client, optional workbench or tools, streaming flag, and max_tool_iterations; agents run via async run/run_stream with Console output. [@claim:clm_35c00beb1130a998359aa5e584296e03aaac4d5f1c02c554cbed8cf3d82e6cc6]
- The framework is layered: Core API (message passing, event-driven agents, local/distributed runtime), AgentChat API (higher-level prototyping), and Extensions API (LLM clients, code execution). [@claim:clm_47a6e7c39c21669081cecbc3d27337519f68ac4fc69fedbbfecd056c957147bc]
- Agents can use MCP servers via McpWorkbench with StdioServerParams; the docs warn to connect only to trusted MCP servers since they may execute commands locally or expose sensitive data. [@claim:clm_546ca5cf8918e1fb8d375053658ed3d7f71b450d1dbfc0877fcea093d30d330d]
- AutoGen is a framework for building multi-agent AI applications that can act autonomously or work alongside humans. [@claim:clm_9d40236228cc60a339508b86c97c2817f585d7b6889615fc496a7c53b1b06654]
- The project is in maintenance mode: no new features or enhancements, community-managed, with Microsoft Agent Framework recommended for new users. [@claim:clm_a54b1a255c8ff6bff0a44e46b6f8a297017157bca813c06a2f907d7f83157c77]
- AgentTool wraps an agent as a tool so a coordinator agent can invoke expert agents, enabling basic multi-agent orchestration with up to max_tool_iterations tool calls. [@claim:clm_b63b4de204995b0ed3faaadccda99af5155dcf4e1b5980d0213ccc94c9a90b96]
- AutoGen Studio provides a no-code GUI for prototyping multi-agent workflows, launched with 'autogenstudio ui --port 8080 --appdir ./my-app'; it is explicitly not production-ready. [@claim:clm_bb3d0a08c6a284c4f9a748e158fa74040034b7dde946ed3e72e17f6ed5ef9fd9]
- AutoGen requires Python 3.10 or later; AgentChat and the OpenAI extension are installed via pip packages autogen-agentchat and autogen-ext[openai]. [@claim:clm_efbf992a5888069ec2fbe2e14fa1d69bf14a4dbf97fdc6926b448bc3d8f31519]
<!-- rcw:end owner=source:src_1ae8718794c45b7b83c6c1a7cfef43d9 block=evidence -->

## Researcher notes

