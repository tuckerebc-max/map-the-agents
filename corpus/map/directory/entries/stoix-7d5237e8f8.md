# Stoix (`stoix`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: EdanToledo
- License: Apache-2.0
- Language: Python
- Interface: install=git clone https://github.com/EdanToledo/Stoix.git, cd Stoix, pipx install uv, uv sync, source .venv/bin/activate
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [edantoledo/stoix](../../repos/edantoledo/stoix.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): NOTE: This is a distributed single-agent reinforcement learning library in JAX (not an AI coding agent harness). Fully end-to-end JAX compilation (jit + pmap for multi-device distribution); two system paradigms (Anakin for pure JAX, Sebulba for non-JAX environments); Hydra config system; statistically robust evaluation with RLiable plots

(captured site page body (agents/stoix.md), not a verified repo-code finding)
Stoix provides research-grade baselines for distributed single-agent reinforcement learning, compiled end-to-end in JAX so experiments run with jit/pmap across devices rather than through Python loops. It ships two architectures — Anakin for fully compiled JAX environments and Sebulba for separate acting and learning devices with non-JAX environments such as Envpool and Gymnasium — plus Hydra configuration, Optuna sweeps, logging to TensorBoard/WandB/Neptune in RLiable-compatible form, and a SLURM launcher. Algorithm implementations (DQN variants, PPO, SAC, TD3, IMPALA, AlphaZero, MuZero-style) are deliberately hackable single files descended from CleanRL, PureJaxRL, and InstaDeep's Mava. It appears in this census only as a name collision from the sweep; nothing in it builds or modifies software.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stoix.md)
