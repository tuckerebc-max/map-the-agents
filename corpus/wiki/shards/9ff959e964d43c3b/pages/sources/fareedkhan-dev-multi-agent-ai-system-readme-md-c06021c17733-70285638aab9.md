---
access: public
aliases: []
claim_ids:
- clm_432a07bb8b0ddf8bb086a756f76716b11ced88368c0f2be47a174acfe7308d97
- clm_45d8cf652329bec812da23d73cac938f42c78b4924f220927be40d6f3bd9041e
- clm_6273801a3204f8d797a26d5475095c54cea2a065d28467f3e5d0228bb41354de
- clm_6c752678cbe90c5c1e258a76632ff514f71e174c50b93b560c30cf0367e42e28
- clm_824ed249cbb2d4f468fbc714aa33ee2932ba3d2be49ef290ff114821d9e49bf4
- clm_8c527f6a7d91ff7832384e8d2836590ed11c7bfac39d99a3af5b2d5a190bdc35
- clm_a20b88e3fc059344e7bfc5a6a2fadf283cfe11349f707c8935b6ffec0de9408d
- clm_aac7a4bff5198798068bc5b6ae565e6c235d0f37273b8808c3bc60b921d1f4ad
- clm_af3e3c1510716cfe1bc8b485fc76733878f279025bc16149bd0a8e63bb20ed23
- clm_dbdb59143ea8fb42d63aa2ef0198df69bb01545ca246862eedb2ed1132eb95ef
- clm_f99676bfc1e921b36386624f2c57c50907a5b6297194531b4ef95ae1d8f5287a
- clm_fcfae181c622f5a16452cf80a573a8cb38804c052c93155320e7eca1a19b6752
maturity: draft
page_id: pg_390ad91554515889a6a070285638aab9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_31265d9e6af65f058524de83dd65b691
title: FareedKhan-dev/Multi-Agent-AI-System/README.md @ c06021c17733
updated_at: '2026-09-14T03:50:20Z'
---

# FareedKhan-dev/Multi-Agent-AI-System/README.md @ c06021c17733

<!-- rcw:begin owner=source:src_31265d9e6af65f058524de83dd65b691 block=evidence -->
- The workflow runs through human_input, verify_info, load_memory, a supervisor coordinating music_catalog and invoice_info sub-agents, and finally create_memory, which updates the user's memory from the interaction. [@claim:clm_432a07bb8b0ddf8bb086a756f76716b11ced88368c0f2be47a174acfe7308d97]
- The music assistant's system prompt embeds prior saved user preferences for personalized responses and instructs that the agent is routed only for music-catalog questions, ignoring others. [@claim:clm_45d8cf652329bec812da23d73cac938f42c78b4924f220927be40d6f3bd9041e]
- The shared State is a TypedDict with customer_id, messages annotated with add_messages, loaded_memory, and a remaining_steps counter described as preventing infinite recursion in the workflow. [@claim:clm_6273801a3204f8d797a26d5475095c54cea2a065d28467f3e5d0228bb41354de]
- The project builds a customer-support multi-agent workflow in LangGraph with two specialized ReAct sub-agents (music catalog and invoice info) coordinated by a supervisor, plus human-in-the-loop and long-term memory steps. [@claim:clm_6c752678cbe90c5c1e258a76632ff514f71e174c50b93b560c30cf0367e42e28]
- The music catalog sub-agent is a StateGraph with a music_assistant reasoning node and a prebuilt ToolNode execution node; a conditional edge routes to the tool node when tool calls are present and otherwise ends, with tool results looping back to the assistant. [@claim:clm_824ed249cbb2d4f468fbc714aa33ee2932ba3d2be49ef290ff114821d9e49bf4]
- The Chinook sample SQL script is downloaded from GitHub and loaded into an in-memory SQLite database, exposed through a SQLAlchemy engine using StaticPool with check_same_thread=False for cross-thread use. [@claim:clm_8c527f6a7d91ff7832384e8d2836590ed11c7bfac39d99a3af5b2d5a190bdc35]
- Repository development practice: setup instructions say to clone the repo, enter its directory, and run pip install -r requirements.txt, with API keys set as environment variables including LANGSMITH_TRACING=true to enable tracing. [@claim:clm_a20b88e3fc059344e7bfc5a6a2fadf283cfe11349f707c8935b6ffec0de9408d]
- OpenAI models are used for both text generation and embeddings; the README notes the original notebook may reference other providers such as Nebius AI or Together AI. [@claim:clm_aac7a4bff5198798068bc5b6ae565e6c235d0f37273b8808c3bc60b921d1f4ad]
- The project requires Python 3.10+ and uses LangGraph, LangSmith, OpenAI models, and SQLite, with dependencies installed via pip from requirements.txt. [@claim:clm_af3e3c1510716cfe1bc8b485fc76733878f279025bc16149bd0a8e63bb20ed23]
- The table of contents includes an 'Evaluating our Multi-AI Agent' section, suggesting the guide covers agent performance evaluation, likely via LangSmith, though the evaluation content itself is not shown in the evidence. [@claim:clm_dbdb59143ea8fb42d63aa2ef0198df69bb01545ca246862eedb2ed1132eb95ef]
- Short-term memory uses a LangGraph MemorySaver checkpointer to keep the current conversation's context, while long-term memory uses an InMemoryStore to save user preferences after a conversation ends. [@claim:clm_f99676bfc1e921b36386624f2c57c50907a5b6297194531b4ef95ae1d8f5287a]
- Four @tool-decorated functions are exposed to the LLM via bind_tools: get_albums_by_artist, get_tracks_by_artist, get_songs_by_genre, and check_for_songs, each executing a SQL query against the database wrapper. [@claim:clm_fcfae181c622f5a16452cf80a573a8cb38804c052c93155320e7eca1a19b6752]
<!-- rcw:end owner=source:src_31265d9e6af65f058524de83dd65b691 block=evidence -->

## Researcher notes

