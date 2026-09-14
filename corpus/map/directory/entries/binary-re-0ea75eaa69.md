# Binary RE (`binary-re`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: unknown
- Interface: platforms=IDE; install=/plugin marketplace add 2389-research/claude-plugins, then /plugin install binary-re@2389-research
- Model providers: Claude (via Claude Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Claude Code skill/plugin) (yes)
  - claude_code_plugin: yes (yes)
  - subagents: no (no)
  - hooks: yes (human-in-the-loop gates for risky operations) (yes)
  - plan_mode: yes (hypothesis-driven analysis workflow) (yes)

Repository map entry: [2389-research/binary-re](../../repos/2389-research/binary-re.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic binary reverse engineering Claude Code plugin for ELF binaries (ARM64, ARMv7, x86_64, MIPS) using radare2, Ghidra, GDB, and QEMU. Hypothesis-driven analysis where the LLM forms hypotheses from evidence, designs experiments, and a human approves risky operations via human-in-the-loop gates. Targets firmware/IoT binary analysis when source code is unavailable.

(captured site page body (agents/binary-re.md), not a verified repo-code finding)
Binary RE is a Claude Code skill that turns the agent into an agentic binary reverse engineer for ELF binaries across ARM64, ARMv7, x86_64, and MIPS. The loop belongs to Claude Code; this plugin supplies the domain method. Analysis is hypothesis-driven: the LLM forms a hypothesis from the evidence it has, designs an experiment to test it, and a human-in-the-loop gate approves any risky operation before it runs. External tools — radare2, Ghidra, GDB, and QEMU — are the instruments the agent drives, and the skill knows how to invoke them and read their output. The target is firmware and IoT binary analysis when source code is unavailable, the kind of work that is otherwise slow and manual. The audience is security researchers and reverse engineers who want Claude Code to carry the tedious parts of a structured RE workflow.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/binary-re.md)
