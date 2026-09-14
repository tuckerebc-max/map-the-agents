# PaperBanana-Pro (`paperbanana-pro`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: elpsykongloo
- License: Apache-2.0
- Language: Python
- Interface: platforms=Autonomous; install=git clone, uv sync --locked, uv tool install --editable . --force
- Model providers: Gemini, OpenAI, OpenRouter, Evolink, custom OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [elpsykongloo/paperbanana-pro](../../repos/elpsykongloo/paperbanana-pro.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Production-grade multi-agent academic illustration engine (full Chinese UI) that generates scientific illustrations and statistical plots from paper method sections; 6 sub-agents (Retriever, Planner, Stylist, Visualizer, Critic, Polish); 21 rounds of engineering polish + 70+ unit tests; Bundle v1 portable format (.bundle.json); 2K/4K refinement with tree-structured version chains and rollback; fault-tolerant retry with Pro-to-Flash model tier degradation; Pipeline Registry for one-line ...

(captured site page body (agents/paperbanana-pro.md), not a verified repo-code finding)
PaperBanana-Pro automates the illustrations and statistical plots researchers otherwise draw by hand from a paper's method section. Six pipeline stages retrieve few-shot references, plan a structured visual description, enforce stylistic consistency, render images or Matplotlib code, critique across multiple rounds, and apply final polish, with a full-Chinese Streamlit GUI and CLI front ends. Outputs ship in a portable Bundle v1 format with tree-structured 2K/4K refinement chains and rollback, and a registry allows new pipelines to be registered in one line. The project is Apache-2.0 licensed but non-commercial, since the multi-agent pipeline methodology was developed during the author's Google internship and is patent-pending by Google. Its users are researchers preparing figures, mostly in Chinese-language academia.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/paperbanana-pro.md)
