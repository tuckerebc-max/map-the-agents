# Needle2 (`needle2`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: cactus-compute
- License: Apache-2.0
- Language: Python
- Interface: install=Python package or single dependency-free C++ binary from the repo
- Model providers: locked
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [cactus-compute/needle](../../repos/cactus-compute/needle.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A 45M-parameter open-weights model shipped as a single 14MB dependency-free C++ binary purpose-built for tool calling, device use, and structured extraction on tiny hardware — trained natively at CQ2-bit quantization with a hashed n-gram engram memory and grammar-constrained decoding, running from Raspberry Pi 5 and Quest 3S down to ESP32-S3 microcontrollers and WebAssembly.

(captured site page body (agents/needle2.md), not a verified repo-code finding)
Needle2 is Cactus Compute's foundation model for tiny devices — phones, wearables, smart home, and robots — not a coding agent or framework. It is a 45M-parameter model specialized for agentic tool calling, device use, and schema-driven structured extraction, distributed as a single dependency-free C++ binary (~28MB session RAM) that auto-selects CPU kernels for NEON, SDOT, AVX2, RISC-V, and WASM SIMD, and it runs everywhere from a Raspberry Pi 5 at roughly 500 tokens per second to Meta Quest headsets, sub-$200 phones, STM32 microcontrollers, and the browser via WebAssembly. It is trained natively at CQ2-bit quantization rather than post-hoc, returns an empty call plus a learned confidence score for off-topic requests so apps can escalate to the cloud, and is designed for local fine-tuning via the needle finetune command. It belongs in the census as a model an agent harness could call rather than a harness itself.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/needle2.md)
