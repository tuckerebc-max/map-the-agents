# django-completion (`django-completion`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: soldatov-ss
- License: MIT
- Language: Python
- Interface: install=pip install django-completion or uv add django-completion; add django_completion to INSTALLED_APPS; then python manage.py autocomplete install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: False (reported)

Repository map entry: [soldatov-ss/django-completion](../../repos/soldatov-ss/django-completion.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Django manage.py context tool for coding agents and tab completion. Provides a cache file (.django-completion-cache.json) that AI agents read to learn all management commands, flags, and migration names without booting Django (readable in under a millisecond). Works even when settings are broken or dependencies are missing. No telemetry, network calls, or database access. Also provides project-aware bash/zsh tab completion for ...

(captured site page body (agents/django-completion.md), not a verified repo-code finding)
Coding agents routinely misinvoke django-admin because the available commands, flags, and migration names live only in --help output, which is expensive to discover at runtime. django-completion pre-computes that inventory into a JSON cache in the repo, so an agent reads one small file and emits correct manage.py commands and migration references on the first try. The same cache powers zsh/bash tab completion for human developers, which keeps the tool useful outside agent workflows. It is aimed at Django maintainers who wire context files into their agents' system prompts or toolchains.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/django-completion.md)
