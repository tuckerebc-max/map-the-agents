---
access: public
aliases: []
claim_ids:
- clm_124900f3f00d2970d83b13989bd7708f49f0ac731879f2417617b915d0cd354a
- clm_1ef55058eaa5af441283f0aa7ce56f72037b415fee3605f5f858efeb0e0bdfeb
- clm_43536b8aa7915a83c820323539f577462ae87d81b00d35f279ef3cfd4dcb35fa
- clm_71d27dbda41d22032771baf9f574d618039ffae7ce5e285eb3e22374d4fc1cdb
- clm_8d719611548e97507af863eb63b7345df2535ce2844445e091bc489b84fc8f8e
- clm_9018ebaf615f3d694de988564c4036e3d225d0747f5ee6edab34e9ad5ee4df2d
- clm_cc8356b39eeaca8bbde504b8228cd4e5bb38b69b9701a28f98dbbe0f25aa9c9d
- clm_dc45547fad417bdf6267a9bfe966031549c2ad51c5e6eb3a05227b051f309765
- clm_ebeef8cb079b3e5094b22e8563fe21bbce0e7e2d0f87f1ac74c0036b9e03e320
- clm_eecabb6f369aa66ce410267c0bc161692dcdde771473aa18ac54c99cb7237ae7
- clm_f69c99bfb54e2748ec1d192cd6938fed6f98d631fc92a2a01db1261118dae131
maturity: draft
page_id: pg_88d2b5efb546554d8d8ad221f5c0c42f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_64b1511ef2e3545ca9cb7962adaf7658
title: Doriandarko/deepseek-engineer/README.md @ 9aa7a2d3611b
updated_at: '2026-09-14T02:00:38Z'
---

# Doriandarko/deepseek-engineer/README.md @ 9aa7a2d3611b

<!-- rcw:begin owner=source:src_64b1511ef2e3545ca9cb7962adaf7658 block=evidence -->
- The tool requires a DeepSeek API key, configured via a DEEPSEEK_API_KEY entry in a .env file. [@claim:clm_124900f3f00d2970d83b13989bd7708f49f0ac731879f2417617b915d0cd354a]
- Repository development practice: the project is described as experimental, showcasing DeepSeek reasoning model capabilities, with contributions welcome. [@claim:clm_1ef55058eaa5af441283f0aa7ce56f72037b415fee3605f5f858efeb0e0bdfeb]
- Documented safety constraints include path normalization and validation, directory traversal protection, a 5MB per-file size limit, and binary file detection and exclusion. [@claim:clm_43536b8aa7915a83c820323539f577462ae87d81b00d35f279ef3cfd4dcb35fa]
- The rich and prompt_toolkit dependencies suggest the color-coded, streaming terminal UI described in the README is likely built on those libraries. [@claim:clm_71d27dbda41d22032771baf9f574d618039ffae7ce5e285eb3e22374d4fc1cdb]
- Version 2.0 replaced structured JSON output with native function calling, citing natural conversation, automatic file operations, visible chain-of-thought reasoning, and better error handling. [@claim:clm_8d719611548e97507af863eb63b7345df2535ce2844445e091bc489b84fc8f8e]
- The product is an interactive terminal coding assistant integrating DeepSeek reasoning models, offering file operations, code analysis, and assistance via natural conversation and function calling. [@claim:clm_9018ebaf615f3d694de988564c4036e3d225d0747f5ee6edab34e9ad5ee4df2d]
- Repository development practice: setup is via git clone, uv venv/uv sync (or pip install -r requirements.txt), and running deepseek-eng.py with uv run or python3. [@claim:clm_cc8356b39eeaca8bbde504b8228cd4e5bb38b69b9701a28f98dbbe0f25aa9c9d]
- Context management includes automatic file detection from user messages, conversation cleanup to prevent token overflow, and file content preservation across history. [@claim:clm_dc45547fad417bdf6267a9bfe966031549c2ad51c5e6eb3a05227b051f309765]
- An /add command lets users preload a single file or an entire directory (with smart filtering) into conversation context, complementing the AI's automatic file reading. [@claim:clm_ebeef8cb079b3e5094b22e8563fe21bbce0e7e2d0f87f1ac74c0036b9e03e320]
- requirements.txt lists openai, pydantic, python-dotenv, rich, and prompt_toolkit; the README states Python 3.11+ is required for optimal performance. [@claim:clm_eecabb6f369aa66ce410267c0bc161692dcdde771473aa18ac54c99cb7237ae7]
- The architecture streams three channels (reasoning, content, tool_calls), executes tools in real time during streaming, and automatically follows up after tool completion. [@claim:clm_f69c99bfb54e2748ec1d192cd6938fed6f98d631fc92a2a01db1261118dae131]
<!-- rcw:end owner=source:src_64b1511ef2e3545ca9cb7962adaf7658 block=evidence -->

## Researcher notes

