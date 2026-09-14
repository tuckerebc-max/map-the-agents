---
access: public
aliases: []
claim_ids:
- clm_067578336e57aff5da169d9072c7647040d46ad411072e438f50e541efb240a8
- clm_0f3235d2e61cb0fcd90c541c743035609fc5f0683eb1477a21907406edde1be6
- clm_24353849ad0ed947a8ad3f4840c791e69c33d4cc228fc4d3dae90461387469b5
- clm_255fef59932579011fbb349995b5c32192b222fe37186815f0789074119438aa
- clm_308942903fd7f609a53ce97e769f5c6d0f4e5f9994ea5876403db915cd756216
- clm_3b0a98f1549298b6ec64e89cb797ebfcfa19117dca8e14c2482e1a2ee22f2fe4
- clm_5153fe7e95e306e1ea78fea87d7fdc04b96c6cb12bf9b20409fccd6c616e5f20
- clm_5792c66312ba36d97aaf6feb35e6458f98eac19d66c140ce8970b00519f94949
maturity: draft
page_id: pg_473b8069080f5aca9ab7f53202fc566d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f31d81881f61550b9f2cc60fb4886bf0
title: guanyilun/agent-sh/docs/agent.md @ 8038ae7730eb
updated_at: '2026-09-14T01:52:03Z'
---

# guanyilun/agent-sh/docs/agent.md @ 8038ae7730eb

<!-- rcw:begin owner=source:src_f31d81881f61550b9f2cc60fb4886bf0 block=evidence -->
- Core tools include bash, read_file, write_file, edit_file, grep (via ripgrep), glob, ls, and list_skills; conversation_recall is registered by the rolling-history extension rather than being a core tool. [@claim:clm_067578336e57aff5da169d9072c7647040d46ad411072e438f50e541efb240a8]
- Conversation state is an OpenAI-compatible messages array; ash auto-compacts when estimated prompt tokens cross autoCompactThreshold (default 0.5) of the model's context window, and older turns are evicted to a persistent rolling-history store browsable via conversation_recall. [@claim:clm_0f3235d2e61cb0fcd90c541c743035609fc5f0683eb1477a21907406edde1be6]
- Tools implement a `ToolDefinition` interface with name, description, JSON Schema input_schema, an execute function with optional streaming onChunk callback, and flags like modifiesFiles, readOnly, and showOutput. [@claim:clm_24353849ad0ed947a8ad3f4840c791e69c33d4cc228fc4d3dae90461387469b5]
- The agent runs a tool loop with no hard iteration limit; side-effect-free tools run in parallel via Promise.all while side-effecting tools run sequentially, and results over maxResultBytes (default 100KB) are head+tail truncated. [@claim:clm_255fef59932579011fbb349995b5c32192b222fe37186815f0789074119438aa]
- The bundled frontend is a shell on top of node-pty, and the grep tool searches file contents via ripgrep; ash works with any OpenAI-compatible API including built-in providers openrouter, openai, deepseek, ollama, zai-coding-plan, and opencode. [@claim:clm_308942903fd7f609a53ce97e769f5c6d0f4e5f9994ea5876403db915cd756216]
- By default every tool runs without gating ('yolo mode'); the kernel has no permission opinion, and gating extensions can interpose confirmation or policy checks via tool advisors. [@claim:clm_3b0a98f1549298b6ec64e89cb797ebfcfa19117dca8e14c2482e1a2ee22f2fe4]
- Skills follow the Agent Skills standard: directories with a SKILL.md containing YAML frontmatter (required name and description); only metadata enters the system prompt, and the agent loads full content via read_file when needed. [@claim:clm_5153fe7e95e306e1ea78fea87d7fdc04b96c6cb12bf9b20409fccd6c616e5f20]
- The default backend `ash` resolves providers, configures an LlmClient, calls any OpenAI-compatible API directly, and executes tools in a loop until the LLM finishes; it only activates once an apiKey and model are resolved. [@claim:clm_5792c66312ba36d97aaf6feb35e6458f98eac19d66c140ce8970b00519f94949]
<!-- rcw:end owner=source:src_f31d81881f61550b9f2cc60fb4886bf0 block=evidence -->

## Researcher notes

