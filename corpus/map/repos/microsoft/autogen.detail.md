# microsoft/autogen -- full detail

[Back to orientation](autogen.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/microsoft/autogen/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/60762d77b55bc1fd.json](../../../wiki/dossiers/microsoft/autogen/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/60762d77b55bc1fd.json)

## specifications (2 claim(s))

- [observation/documented] AutoGen is a framework for building multi-agent AI applications that can act autonomously or work alongside humans. -- evidence: [README.md#L16-L16](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L16-L16) (`clm_9d40236228cc60a339508b86c97c2817f585d7b6889615fc496a7c53b1b06654`)
- [observation/documented] AutoGen 0.4 is a ground-up rewrite featuring asynchronous messaging, scalable distributed agents, modular design, cross-language (.NET/Python) support, and full typing. -- evidence: [FAQ.md#L5-L10](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L5-L10), [FAQ.md#L56-L56](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L56-L56) (`clm_6bdca59a416cee2be145e17241c009046405d30d7fa89f30835f0eefc98949ca`)

## components (1 claim(s))

- [observation/documented] The framework is layered: Core API (message passing, event-driven agents, local/distributed runtime), AgentChat API (higher-level prototyping), and Extensions API (LLM clients, code execution). -- evidence: [README.md#L181-L183](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L181-L183), [README.md#L179-L179](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L179-L179) (`clm_47a6e7c39c21669081cecbc3d27337519f68ac4fc69fedbbfecd056c957147bc`)

## design-choices (2 claim(s))

- [observation/documented] The programming model is publish-subscribe: agents subscribe to and publish events defined per the CloudEvents specification, with handlers matching event types. -- evidence: [docs/design/01 - Programming Model.md#L5-L5](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L5-L5), [docs/design/01 - Programming Model.md#L18-L18](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L18-L18), [docs/design/01 - Programming Model.md#L9-L9](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L9-L9) (`clm_3300529caab7892a61581202da8184613ab1db4b99756c1b816dc6b27024f247`)
- [observation/documented] Topics route published messages to agents; a TopicId has type and source, subscriptions use side-effect-free matcher and mapper functions, and the runtime instantiates agents on demand. -- evidence: [docs/design/02 - Topics.md#L44-L44](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L44-L44), [docs/design/02 - Topics.md#L48-L48](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L48-L48), [docs/design/02 - Topics.md#L19-L24](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L19-L24), [docs/design/02 - Topics.md#L7-L7](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L7-L7), [docs/design/02 - Topics.md#L41-L42](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L41-L42) (`clm_bd4505dee201110d7c9836be244985bad7c075cbafaa9466bfa51ccb6317d424`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are limited to bug fixes, security patches, and documentation improvements due to maintenance mode; feature work is directed to Microsoft Agent Framework. -- evidence: [README.md#L216-L216](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L216-L216) (`clm_2d55bf39fbae7b9453b0e80a99c41da8aa3016114ca53170050ed206aa1ba9bc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] AssistantAgent accepts a model client, optional workbench or tools, streaming flag, and max_tool_iterations; agents run via async run/run_stream with Console output. -- evidence: [README.md#L56-L60](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L56-L60), [README.md#L138-L147](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L138-L147), [README.md#L78-L95](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L78-L95) (`clm_35c00beb1130a998359aa5e584296e03aaac4d5f1c02c554cbed8cf3d82e6cc6`)
- [observation/documented] AutoGen Studio provides a no-code GUI for prototyping multi-agent workflows, launched with 'autogenstudio ui --port 8080 --appdir ./my-app'; it is explicitly not production-ready. -- evidence: [README.md#L40-L41](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L40-L41), [README.md#L158-L158](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L158-L158), [README.md#L168-L169](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L168-L169), [README.md#L160-L164](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L160-L164) (`clm_bb3d0a08c6a284c4f9a748e158fa74040034b7dde946ed3e72e17f6ed5ef9fd9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] AgentTool wraps an agent as a tool so a coordinator agent can invoke expert agents, enabling basic multi-agent orchestration with up to max_tool_iterations tool calls. -- evidence: [README.md#L120-L127](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L120-L127), [README.md#L138-L147](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L138-L147), [README.md#L129-L136](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L129-L136), [README.md#L106-L106](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L106-L106) (`clm_b63b4de204995b0ed3faaadccda99af5155dcf4e1b5980d0213ccc94c9a90b96`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents can use MCP servers via McpWorkbench with StdioServerParams; the docs warn to connect only to trusted MCP servers since they may execute commands locally or expose sensitive data. -- evidence: [README.md#L101-L102](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L101-L102), [README.md#L71-L75](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L71-L75), [README.md#L78-L95](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L78-L95), [README.md#L67-L67](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L67-L67) (`clm_546ca5cf8918e1fb8d375053658ed3d7f71b450d1dbfc0877fcea093d30d330d`)

## evaluation (1 claim(s))

- [observation/documented] Per the transparency FAQs, AutoGen was evaluated on six applications using success-based metrics, tested for prompt-injection harms, and achieved SOTA on the GAIA benchmark as of March 1, 2024. -- evidence: [TRANSPARENCY_FAQS.md#L31-L33](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/TRANSPARENCY_FAQS.md#L31-L33) (`clm_addeb9b4bcdf65773dcc06914a548a91a8386420c500ae08c94b05e55dcaa6a7`)

## dependencies (2 claim(s))

- [observation/documented] AutoGen requires Python 3.10 or later; AgentChat and the OpenAI extension are installed via pip packages autogen-agentchat and autogen-ext[openai]. -- evidence: [README.md#L33-L34](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L33-L34), [README.md#L29-L29](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L29-L29) (`clm_efbf992a5888069ec2fbe2e14fa1d69bf14a4dbf97fdc6926b448bc3d8f31519`)
- [observation/documented] The project uses the MIT license for code and CC-BY-4.0 for documentation; releases to the pyautogen PyPI package were blocked by a package-ownership change, moving to multiple packages. -- evidence: [FAQ.md#L84-L84](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L84-L84), [FAQ.md#L88-L88](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L88-L88), [README.md#L222-L225](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L222-L225) (`clm_330836a4a50bbb767c6e49ba6e95a1b1b97b00314b4f17d49583b1fc38df6ba9`)

## limitations (2 claim(s))

- [observation/documented] The project is in maintenance mode: no new features or enhancements, community-managed, with Microsoft Agent Framework recommended for new users. -- evidence: [README.md#L18-L25](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L18-L25), [README.md#L177-L177](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L177-L177) (`clm_a54b1a255c8ff6bff0a44e46b6f8a297017157bca813c06a2f907d7f83157c77`)
- [observation/documented] Documented limitations include inherited LLM weaknesses (bias, limited contextual understanding, hallucination) and multi-agent risks around privacy, accountability, and code execution safety. -- evidence: [TRANSPARENCY_FAQS.md#L47-L51](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/TRANSPARENCY_FAQS.md#L47-L51), [TRANSPARENCY_FAQS.md#L37-L37](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/TRANSPARENCY_FAQS.md#L37-L37), [TRANSPARENCY_FAQS.md#L39-L44](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/TRANSPARENCY_FAQS.md#L39-L44) (`clm_3ca4af0aa5f57ad4fcd451626872f05a37578096bb03d80ea0fec9f83d2f66bb`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

