# Patchwork (`patchwork`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: patched-codes
- License: AGPL-3.0
- Language: Python
- Interface: platforms=Autonomous, CLI; install=pip install 'patchwork-cli\[all\]' --upgrade
- Model providers: OpenAI, Google Gemini, any OpenAI-compatible endpoint (Groq, Together, Hugging Face), local llama.cpp/Ollama/vLLM/TGI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [patched-codes/patchwork](../../repos/patched-codes/patchwork.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Development gruntwork is codified as six predefined 'patchflows' (AutoFix, ResolveIssue, PRReview, GenerateDocstring, GenerateREADME, DependencyUpgrade) built from reusable Steps and prompt templates, runnable locally, in the IDE, or in CI, and extensible by composing new flows from an Apache-2.0 template repo.

(captured site page body (agents/patchwork.md), not a verified repo-code finding)
Patchwork was built by Patched Codes to automate the repetitive maintenance work — dependency upgrades, PR reviews, docstring generation, security fixes — that piles up between feature projects. Instead of a free-form chat loop, it executes predefined patchflows: pipelines of reusable steps (scan code, call an LLM, edit files, open a PR) driven by customizable prompt templates, with six flows shipped out of the box including AutoFix, PRReview, and DependencyUpgrade. The same patchflows run from the CLI, inside an IDE, or in CI pipelines, and custom patchflows compose existing steps or new ones contributed through an Apache-2.0 template repository, while the core stays AGPL-3.0. Model access is flexible, spanning OpenAI, Gemini, Groq, Together, and local llama.cpp, Ollama, or vLLM endpoints configured by CLI arguments or YAML. Its users are engineering teams automating code-maintenance workflows in CI rather than developers seeking an interactive coding partner.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/patchwork.md)
