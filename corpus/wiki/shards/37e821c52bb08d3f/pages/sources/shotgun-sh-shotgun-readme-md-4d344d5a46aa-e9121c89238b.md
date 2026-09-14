---
access: public
aliases: []
claim_ids:
- clm_040e22b3eb948f4668f1332a875f3149005ef39721dd769c2b8aca0070d1f5ef
- clm_44ad574cf9b9121fe5a6ad9ef72908997f7519cf88e3f3aeda7452349213480c
- clm_47ddd1ae8467f7be96a97695d56c45ff34ad9028c0bf9da8ca38d8069eb5cb22
- clm_5f6f7f2bfcd7279a4e02c023558757a3b9c8fb22ad1d8650485edc200fc459b7
- clm_77571a0f2de0d4af5d0ad6d9076ba71dc0fa5f53972c5c5a94a554396d601999
- clm_870dcb4e0d70138c7db12e6e236616b85f246a5be147737561e5a75d967ad90e
- clm_8df1d931bdb2261cdf91dcfcc816469147bd78c479a618093881da892e8dfe5f
- clm_a5c1b216c29d31b9179623560b2f58bafc001c7b3ef489e42b96f9da4d720d04
- clm_b7966cd9bce6febff9fd6e88692784866d379d3ff15884ac345056398f6dde81
- clm_bf1e3d45dca2818e5e4e6aaa8935aab5b327ca3b878bd33aea79a99a259e5582
- clm_da039d8b31fc7b68a6a652c0b282b46542bf848061d2f8d73e79deb3f12ed034
maturity: draft
page_id: pg_cf5c8641455550b58ac3e9121c89238b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d37a3dd78c8d54ea88edb73d8bc52f28
title: shotgun-sh/shotgun/README.md @ 4d344d5a46aa
updated_at: '2026-09-14T04:21:04Z'
---

# shotgun-sh/shotgun/README.md @ 4d344d5a46aa

<!-- rcw:begin owner=source:src_d37a3dd78c8d54ea88edb73d8bc52f28 block=evidence -->
- The FAQ states only minimal anonymous event telemetry (e.g., install, server start, tool call) is collected via PostHog, without collecting event content. [@claim:clm_040e22b3eb948f4668f1332a875f3149005ef39721dd769c2b8aca0070d1f5ef]
- A Router internally dispatches specialized sub-agents across Research, Specify, Plan, Tasks, and Export phases; users control only the Planning and Drafting execution modes. [@claim:clm_44ad574cf9b9121fe5a6ad9ef72908997f7519cf88e3f3aeda7452349213480c]
- Specs can be exported as AGENTS.md files for tools like Cursor, Claude Code, Windsurf, and Lovable, and shared to a workspace as versioned snapshots on paid plans, leaving local .shotgun/*.md files unchanged. [@claim:clm_47ddd1ae8467f7be96a97695d56c45ff34ad9028c0bf9da8ca38d8069eb5cb22]
- Codebase indexing runs locally using tree-sitter parsing, producing a searchable code graph stored under ~/.shotgun-sh/codebases/ that the FAQ says is never sent to a server. [@claim:clm_5f6f7f2bfcd7279a4e02c023558757a3b9c8fb22ad1d8650485edc200fc459b7]
- Keyboard shortcuts include Shift+Tab for mode switching, Ctrl+C to cancel, Escape to exit Q&A or stop an agent, and Ctrl+U to view usage stats. [@claim:clm_77571a0f2de0d4af5d0ad6d9076ba71dc0fa5f53972c5c5a94a554396d601999]
- Planning mode proposes a plan with confirmation checkpoints before file-changing agents run, while Drafting runs the full plan without intermediate prompts; Shift+Tab switches modes and '/' opens the command palette. [@claim:clm_870dcb4e0d70138c7db12e6e236616b85f246a5be147737561e5a75d967ad90e]
- Repository development practice: the README points contributors to a Contributing Guide, Git Hooks (Lefthook, trufflehog, security scanning), CI/CD via GitHub Actions, observability, and Docker docs, and welcomes bug/feature/doc issue templates. [@claim:clm_8df1d931bdb2261cdf91dcfcc816469147bd78c479a618093881da892e8dfe5f]
- Supported LLM providers are OpenAI, Anthropic (Claude), and Google Gemini; local LLM support is stated as planned, and internet access is required for LLM API calls. [@claim:clm_a5c1b216c29d31b9179623560b2f58bafc001c7b3ef489e42b96f9da4d720d04]
- Each phase (research, spec, plan, tasks, export) uses a separate specialized agent with phase-tailored prompts rather than a single general-purpose agent. [@claim:clm_b7966cd9bce6febff9fd6e88692784866d379d3ff15884ac345056398f6dde81]
- Shotgun is described as a spec-driven development CLI that reads the whole codebase, plans features upfront, and splits work into staged PRs with file-by-file instructions for AI coding agents. [@claim:clm_bf1e3d45dca2818e5e4e6aaa8935aab5b327ca3b878bd33aea79a99a259e5582]
- Installation uses uv (via Homebrew or curl) and running 'uvx shotgun-sh@latest'; on Windows, PowerShell is required with x64 and Python 3.11-3.13 supported, while 32-bit Python and 3.14+ are not supported. [@claim:clm_da039d8b31fc7b68a6a652c0b282b46542bf848061d2f8d73e79deb3f12ed034]
<!-- rcw:end owner=source:src_d37a3dd78c8d54ea88edb73d8bc52f28 block=evidence -->

## Researcher notes

