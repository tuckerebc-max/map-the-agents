# aidermacs (`aidermacs`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: MatthewZMD
- License: Apache-2.0
- Language: Emacs Lisp
- Interface: platforms=IDE; install=emacs
- Model providers: OpenAI, Anthropic, DeepSeek, Google Gemini, OpenRouter, Ollama, LiteLLM
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes — aidermacs-before-run-backend-hook for custom setup before starting Aider backend (yes)
  - plan_mode: yes — Architect Mode uses two specialized models (Architect for reasoning/planning, Editor for code generation); requires explicit confirmation before applying changes (yes)

Repository map entry: [matthewzmd/aidermacs](../../repos/matthewzmd/aidermacs.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Emacs-native AI pair programming integrating Aider with built-in Ediff integration for reviewing AI-generated changes, Architect Mode (dual-model approach achieving SOTA on code editing benchmarks), and native multiline input.

(captured site page body (agents/aidermacs.md), not a verified repo-code finding)
The package is a community-driven fork of aider.el that rebuilt the integration to be Emacs-native: Magit-style transient menus, comint or vterm backends, Tramp support for remote files, and file watching for AI! comment markers under vterm. Diff review defaults to Ediff so changes are inspected with the editor's own tooling rather than a custom UI. It targets Emacs 26.1+ with Aider installed via uv, discovers models dynamically from OpenAI, Anthropic, DeepSeek, Gemini, OpenRouter, or any OpenAI-compatible endpoint through Ollama or LiteLLM. Distributed via MELPA and NonGNU ELPA with CI, it is the actively maintained Emacs front end for Aider (660 commits, Apache-2.0).
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/aidermacs.md)
