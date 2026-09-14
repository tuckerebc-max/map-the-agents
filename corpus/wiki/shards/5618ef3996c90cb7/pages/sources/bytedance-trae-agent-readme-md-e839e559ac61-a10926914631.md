---
access: public
aliases: []
claim_ids:
- clm_09ada320ed13dd01fc2804f81599c947be57293b75ae911202cf134863e3cd45
- clm_315cd9521dd2c6c9451354643db30468aeceae472210d97cc83e7f8aed617aaf
- clm_4c1c0ed4bfeb22f77eba3e07d6269683a6455300477ad669d76b989484861497
- clm_5f4ea45a578e90e98c1c9e8b44a9e9618eacb5e3f31fe248a94104c48be1b214
- clm_7e215360a0f8501095e3442584814ada2d5210f20dbb44f5f834fc596642c8f0
- clm_86c140ba7873adb0ac6a36f922803eb3960d54f520556769c4adabc65631bf25
- clm_8d9ff2c67a48ee2a2c3b4a821249a2bbb6eed4ff32372fa96ea5ca31a47cdf1a
- clm_d7eb1a524c542c93c47858311d242af219b64d3e5a806b9a2bdc230205ce3b66
- clm_df4d90838ec52f5314868ac18a482200b4650e3375b05a8e16c542d70154cb11
- clm_eb247ec09709d329a23be035d2983ddc4b67b035123a2f218d23dde3d5ee2cea
- clm_f39b61fedd65ad044dc0b7bf6aefdd90db70bb13d1c9a703fceb6ce178b59368
- clm_f44b4c51de4deb55a9aac3e6e970147178370bc2f6cb47411d791cd4edff3fae
maturity: draft
page_id: pg_d8531a16f164529cb2f9a10926914631
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2dd451d5cc685cebbc75003c27380295
title: bytedance/trae-agent/README.md @ e839e559ac61
updated_at: '2026-09-14T02:00:03Z'
---

# bytedance/trae-agent/README.md @ e839e559ac61

<!-- rcw:begin owner=source:src_2dd451d5cc685cebbc75003c27380295 block=evidence -->
- Trajectory recording captures LLM interactions, agent steps, tool usage, and metadata into JSON files, saved continuously during execution with auto-generated or custom filenames. [@claim:clm_09ada320ed13dd01fc2804f81599c947be57293b75ae911202cf134863e3cd45]
- The example YAML config enables Lakeview step summarization, sets max_steps (e.g. 200), and selects tools such as bash, str_replace_based_edit_tool, sequentialthinking, and task_done. [@claim:clm_315cd9521dd2c6c9451354643db30468aeceae472210d97cc83e7f8aed617aaf]
- The project positions itself as a research-friendly, modular agent platform aimed at studying agent architectures, ablation studies, and novel agent capabilities. [@claim:clm_4c1c0ed4bfeb22f77eba3e07d6269683a6455300477ad669d76b989484861497]
- The project requires Python 3.12+ and UV, and setup uses 'uv sync --all-extras' with a virtualenv; an API key for the chosen provider is also needed. [@claim:clm_5f4ea45a578e90e98c1c9e8b44a9e9618eacb5e3f31fe248a94104c48be1b214]
- Configuration is YAML-based (JSON is deprecated legacy), with priority order: command-line arguments > config file > environment variables > defaults; base_url overrides are supported. [@claim:clm_7e215360a0f8501095e3442584814ada2d5210f20dbb44f5f834fc596642c8f0]
- Tasks can execute inside Docker: via an image, an existing container ID, a Dockerfile path, or a local tar image file, with an option to keep or remove the container afterward; Docker must be configured in the environment. [@claim:clm_86c140ba7873adb0ac6a36f922803eb3960d54f520556769c4adabc65631bf25]
- CLI options include --provider/--model, --working-dir, --trajectory-file, --must-patch, and --max-steps for interactive mode. [@claim:clm_8d9ff2c67a48ee2a2c3b4a821249a2bbb6eed4ff32372fa96ea5ca31a47cdf1a]
- Optional MCP services can be enabled via an mcp_servers config section, e.g. launching a Playwright MCP server through npx. [@claim:clm_d7eb1a524c542c93c47858311d242af219b64d3e5a806b9a2bdc230205ce3b66]
- Repository development practice: the repo runs pre-commit and unit-test GitHub Actions workflows, and contributors are directed to CONTRIBUTING.md and docs/roadmap.md. [@claim:clm_df4d90838ec52f5314868ac18a482200b4650e3375b05a8e16c542d70154cb11]
- Interactive mode supports typed task descriptions plus commands: status, help, clear, and exit/quit. [@claim:clm_eb247ec09709d329a23be035d2983ddc4b67b035123a2f218d23dde3d5ee2cea]
- Trae Agent provides a CLI (trae-cli) that accepts natural-language task instructions and runs software engineering workflows, with 'run' and 'interactive' subcommands. [@claim:clm_f39b61fedd65ad044dc0b7bf6aefdd90db70bb13d1c9a703fceb6ce178b59368]
- Trae Agent supports multiple LLM providers (OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini), and the trajectory docs reference a dedicated client module for each of these providers. [@claim:clm_f44b4c51de4deb55a9aac3e6e970147178370bc2f6cb47411d791cd4edff3fae]
<!-- rcw:end owner=source:src_2dd451d5cc685cebbc75003c27380295 block=evidence -->

## Researcher notes

