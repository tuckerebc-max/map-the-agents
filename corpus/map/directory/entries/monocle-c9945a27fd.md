# Monocle (`monocle`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: arphanetx
- License: GPL-3.0
- Language: Python
- Interface: install=pip install -r requirements.txt && python -m pip install . (requires Nvidia CUDA and Ghidra)
- Model providers: Mistral AI (Mistral-7B-Instruct-v0.2)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [arphanetx/monocle](../../repos/arphanetx/monocle.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM-backed natural-language search over compiled target binaries; uses Ghidra headless decompilation plus an in-built Mistral-7B-Instruct model to identify and score (0-10) functions matching natural-language search criteria, with an explanation for each finding.

(captured site page body (agents/monocle.md), not a verified repo-code finding)
Monocle addresses the cold-start problem in reverse engineering: facing an unknown binary, an analyst needs to locate code of interest — authentication logic, vulnerability patterns, password handling — without any prior map of the program. The tool runs Ghidra in headless mode to decompile the target, then passes the decompiled functions through a locally hosted Mistral-7B-Instruct model that scores each function 0-10 against the user's natural-language criteria and explains every nonzero score. Output arrives as a live-sorted table, so an analyst can steer the investigation as results appear rather than waiting for a batch run. It targets security researchers and reverse engineers with GPU-equipped workstations (Nvidia CUDA recommended, 16 GB RAM), and it runs entirely offline — an intentional property for analyzing untrusted or sensitive binaries. The repository saw a single burst of activity in April 2024 with no releases since, so it survives as a niche research artifact.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/monocle.md)
