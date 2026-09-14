# vim_codex (`vim-codex`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tom-doerr
- License: MIT
- Language: Python, Vim script
- Interface: platforms=IDE; install=Install as Vim bundle (Pathogen, Vundle) via git clone, then pip3 install openai
- Model providers: OpenAI (Codex API)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tom-doerr/vim_codex](../../repos/tom-doerr/vim_codex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI plugin for Vim that enables OpenAI Codex-powered code completion directly in the editor; provides CreateCompletion and CreateCompletionLine commands. Uses deprecated OpenAI Codex API.

(captured site page body (agents/vim-codex.md), not a verified repo-code finding)
vim_codex comes from the first wave of API-based AI coding tools, when OpenAI's Codex models were the state of the art and editor integration meant one completion request per trigger. The plugin added two commands — CreateCompletion, which sends the current buffer context to the Codex API and inserts the result (optionally sized by a token-count argument), and CreateCompletionLine for completing the current line — with configuration in ~/.config/openaiapirc and installation through any Vim bundle manager. It served Vim users who wanted Codex completions without leaving the editor, before agentic tools existed. OpenAI deprecated and shut down the Codex models in March 2023, so the plugin no longer works; with no releases and no updates, it remains only as a historical example of early editor-AI integration.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vim-codex.md)
