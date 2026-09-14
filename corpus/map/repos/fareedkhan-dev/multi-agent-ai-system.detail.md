# fareedkhan-dev/multi-agent-ai-system -- full detail

[Back to orientation](multi-agent-ai-system.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fareedkhan-dev/multi-agent-ai-system/c06021c1773359ec7192706c3259b52948e00b20/eab6fbcb1bc8c158.json](../../../wiki/dossiers/fareedkhan-dev/multi-agent-ai-system/c06021c1773359ec7192706c3259b52948e00b20/eab6fbcb1bc8c158.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The project builds a customer-support multi-agent workflow in LangGraph with two specialized ReAct sub-agents (music catalog and invoice info) coordinated by a supervisor, plus human-in-the-loop and long-term memory steps. -- evidence: [README.md#L216-L216](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L216-L216), [README.md#L224-L229](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L224-L229), [README.md#L222-L222](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L222-L222), [README.md#L218-L218](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L218-L218) (`clm_6c752678cbe90c5c1e258a76632ff514f71e174c50b93b560c30cf0367e42e28`)
- [observation/documented] The music catalog sub-agent is a StateGraph with a music_assistant reasoning node and a prebuilt ToolNode execution node; a conditional edge routes to the tool node when tool calls are present and otherwise ends, with tool results looping back to the assistant. -- evidence: [README.md#L620-L620](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L620-L620), [README.md#L607-L617](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L607-L617), [README.md#L594-L594](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L594-L594), [README.md#L433-L434](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L433-L434), [README.md#L547-L548](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L547-L548), [README.md#L598-L598](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L598-L598), [README.md#L600-L600](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L600-L600) (`clm_824ed249cbb2d4f468fbc714aa33ee2932ba3d2be49ef290ff114821d9e49bf4`)

## design-choices (2 claim(s))

- [observation/documented] The music assistant's system prompt embeds prior saved user preferences for personalized responses and instructs that the agent is routed only for music-catalog questions, ignoring others. -- evidence: [README.md#L472-L477](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L472-L477), [README.md#L463-L470](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L463-L470), [README.md#L494-L494](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L494-L494) (`clm_45d8cf652329bec812da23d73cac938f42c78b4924f220927be40d6f3bd9041e`)
- [observation/documented] The Chinook sample SQL script is downloaded from GitHub and loaded into an in-memory SQLite database, exposed through a SQLAlchemy engine using StaticPool with check_same_thread=False for cross-thread use. -- evidence: [README.md#L145-L151](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L145-L151), [README.md#L171-L171](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L171-L171), [README.md#L153-L155](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L153-L155), [README.md#L169-L169](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L169-L169), [README.md#L160-L167](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L160-L167) (`clm_8c527f6a7d91ff7832384e8d2836590ed11c7bfac39d99a3af5b2d5a190bdc35`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: setup instructions say to clone the repo, enter its directory, and run pip install -r requirements.txt, with API keys set as environment variables including LANGSMITH_TRACING=true to enable tracing. -- evidence: [README.md#L80-L84](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L80-L84), [README.md#L34-L34](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L34-L34), [README.md#L40-L41](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L40-L41), [README.md#L37-L37](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L37-L37) (`clm_a20b88e3fc059344e7bfc5a6a2fadf283cfe11349f707c8935b6ffec0de9408d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Four @tool-decorated functions are exposed to the LLM via bind_tools: get_albums_by_artist, get_tracks_by_artist, get_songs_by_genre, and check_for_songs, each executing a SQL query against the database wrapper. -- evidence: [README.md#L286-L286](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L286-L286), [README.md#L420-L421](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L420-L421), [README.md#L413-L413](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L413-L413), [README.md#L423-L423](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L423-L423), [README.md#L417-L417](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L417-L417), [README.md#L408-L411](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L408-L411) (`clm_fcfae181c622f5a16452cf80a573a8cb38804c052c93155320e7eca1a19b6752`)

## memory-state (2 claim(s))

- [observation/documented] Short-term memory uses a LangGraph MemorySaver checkpointer to keep the current conversation's context, while long-term memory uses an InMemoryStore to save user preferences after a conversation ends. -- evidence: [README.md#L212-L212](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L212-L212), [README.md#L207-L208](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L207-L208), [README.md#L204-L204](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L204-L204), [README.md#L210-L210](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L210-L210), [README.md#L194-L195](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L194-L195) (`clm_f99676bfc1e921b36386624f2c57c50907a5b6297194531b4ef95ae1d8f5287a`)
- [observation/documented] The shared State is a TypedDict with customer_id, messages annotated with add_messages, loaded_memory, and a remaining_steps counter described as preventing infinite recursion in the workflow. -- evidence: [README.md#L273-L274](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L273-L274), [README.md#L270-L271](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L270-L271), [README.md#L276-L278](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L276-L278), [README.md#L264-L268](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L264-L268), [README.md#L260-L262](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L260-L262) (`clm_6273801a3204f8d797a26d5475095c54cea2a065d28467f3e5d0228bb41354de`)

## orchestration (1 claim(s))

- [observation/documented] The workflow runs through human_input, verify_info, load_memory, a supervisor coordinating music_catalog and invoice_info sub-agents, and finally create_memory, which updates the user's memory from the interaction. -- evidence: [README.md#L224-L229](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L224-L229) (`clm_432a07bb8b0ddf8bb086a756f76716b11ced88368c0f2be47a174acfe7308d97`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The table of contents includes an 'Evaluating our Multi-AI Agent' section, suggesting the guide covers agent performance evaluation, likely via LangSmith, though the evaluation content itself is not shown in the evidence. -- evidence: [README.md#L48-L64](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L48-L64) (`clm_dbdb59143ea8fb42d63aa2ef0198df69bb01545ca246862eedb2ed1132eb95ef`)

## dependencies (2 claim(s))

- [observation/documented] The project requires Python 3.10+ and uses LangGraph, LangSmith, OpenAI models, and SQLite, with dependencies installed via pip from requirements.txt. -- evidence: [README.md#L30-L30](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L30-L30), [README.md#L7-L7](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L7-L7), [README.md#L40-L41](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L40-L41) (`clm_af3e3c1510716cfe1bc8b485fc76733878f279025bc16149bd0a8e63bb20ed23`)
- [observation/documented] OpenAI models are used for both text generation and embeddings; the README notes the original notebook may reference other providers such as Nebius AI or Together AI. -- evidence: [README.md#L86-L86](https://github.com/FareedKhan-dev/Multi-Agent-AI-System/blob/c06021c1773359ec7192706c3259b52948e00b20/README.md#L86-L86) (`clm_aac7a4bff5198798068bc5b6ae565e6c235d0f37273b8808c3bc60b921d1f4ad`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

