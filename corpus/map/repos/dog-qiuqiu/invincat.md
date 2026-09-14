# dog-qiuqiu/invincat

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8a026ea3579a @ aeb151f89aa5de23

## Summary (orientation draft, not independently verified)

The package is distributed on PyPI as invincat-cli, requires Python 3.11+, and can also be installed from source via an editable pip install. The product exposes slash commands including /model, /plan, /goal, /memory, /schedule, /mcp, /threads, and /help, plus a wecombot subcommand to start the WeCom daemon. Evidence coverage: 104 of 108 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The runtime is a Textual TUI over a DeepAgents/LangGraph agent: cli assembles startup, agent builds the agent with tools/middleware/backend/system prompt, textual_adapter converts agent streams to UI messages, and widgets render chat, tool calls, approvals, and selectors. -- evidence: [doc/ARCHITECTURE_EN.md#L9-L15](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L9-L15), [doc/ARCHITECTURE.md#L9-L15](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L9-L15)
  - [observation/documented] Middleware includes approve_plan and ask_user interrupt protocols, auto memory refresh, project-scoped file management tools (file_info, mkdir, move_file, copy_file, delete_file), micro_compaction of old messages, and token state tracking. -- evidence: [doc/ARCHITECTURE_EN.md#L152-L160](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L152-L160), [doc/ARCHITECTURE.md#L152-L160](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L152-L160)
- design-choices (2 claim(s)):
  - [observation/documented] Model selection is per-call switchable through LangGraph runtime context via configurable_model, and model profiles persist as TOML configuration with thread-level model preferences. -- evidence: [doc/ARCHITECTURE_EN.md#L250-L265](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L250-L265), [doc/ARCHITECTURE.md#L250-L265](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L250-L265)
  - [observation/documented] MCP integration includes server loading/connection, tool wrapping, and an MCP server trust policy module (mcp/trust.py). -- evidence: [doc/ARCHITECTURE.md#L269-L275](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L269-L275), [doc/ARCHITECTURE_EN.md#L269-L275](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L269-L275)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are capability packs loaded when a task matches their description; built-in skills include docx, pdf, pptx, xlsx, and skill-creator, and custom skills can live at user, user-shared, project, or project-shared scope with project overriding user and custom overriding built-in. -- evidence: [README.md#L180-L182](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L180-L182), [README.md#L197-L203](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L197-L203), [README.md#L205-L207](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L205-L207), [README.md#L184-L190](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L184-L190)
- interfaces (4 claim(s)):
  - [observation/documented] The product exposes slash commands including /model, /plan, /goal, /memory, /schedule, /mcp, /threads, and /help, plus a wecombot subcommand to start the WeCom daemon. -- evidence: [README.md#L249-L252](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L249-L252), [README.md#L95-L104](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L95-L104)
  - [observation/documented] Model configuration is done via a /model manager (Ctrl+N to register provider, model name, API key, optional base URL) or through provider environment variables such as OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, DEEPSEEK_API_KEY, and OPENROUTER_API_KEY. -- evidence: [README.md#L66-L66](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L66-L66), [README.md#L68-L74](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L68-L74), [README.md#L62-L64](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L62-L64)
- memory-state (2 claim(s)):
  - [observation/documented] Durable memory has two scopes: user memory at ~/.invincat/<agent>/memory_user.json and project memory at .invincat/memory_project.json; a background memory agent extracts updates after non-trivial turns, and /memory opens a manager UI. -- evidence: [README.md#L138-L142](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L138-L142), [README.md#L133-L136](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L133-L136), [README.md#L144-L147](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L144-L147)
More evidence: [full detail](invincat.detail.md)

Metadata and full claim list: [full detail](invincat.detail.md)
Human notes ([notes](invincat.notes.md), never overwritten by build)

[Back to map index](../../index.md)
