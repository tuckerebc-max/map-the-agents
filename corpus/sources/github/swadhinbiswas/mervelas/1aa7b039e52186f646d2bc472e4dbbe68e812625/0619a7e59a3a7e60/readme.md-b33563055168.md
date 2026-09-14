<div align="center">

<pre>
 █▄   ▄█
 ███████
 █ ▀ ▀ █
</pre>

# Mervelas

**The Fast, Unlocked, Local-First AI Coding Assistant.**

[![Bun Built](https://img.shields.io/badge/Built_with-Bun-black)](https://bun.sh)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#license)

_Note: Mervelas is currently in active development. We have not published to NPM yet. You need to build the project locally and carefully use your own API keys. Stay tuned for official releases!_

</div>

---

## 🌟 Welcome to Mervelas

Mervelas is an independent, open-source AI coding CLI built from the ground up to guarantee freedom, zero telemetry, and maximum performance.

Many enterprise assistants try to force developers into a single closed ecosystem or silently harvest usage telemetry. We firmly believe your code, your terminal, and your prompts belong to you.

### Why Choose Mervelas?

1. **Provider Independence:** We break the chains. Mervelas fully supports OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, and locally hosted models out of the box.
2. **Unified Native Commands:** Forget heavily patched forks that break `/skills` or `/login`. Mervelas provides flawlessly integrated commands deeply connected to the local event loop.
3. **Extremely Lightweight:** Compiled natively with `bun` and rendered via a highly optimized custom React Ink abstraction. It has almost **zero idle CPU usage** and lightning-quick startup latencies.
4. **Absolute Privacy:** Session architectures are strictly localized. Your conversational history is written securely to `~/.mervelas/projects/` locally via JSONL formatting, ensuring sensitive projects never leak metadata.

---

## 📸 See It In Action

<div align="center">
  <table>
    <tr>
      <td align="center">
        <b>Launch Interface</b><br>
        <img src="images/lunchpage.png" alt="Mervelas Launch Page" width="400"/>
      </td>
      <td align="center">
        <b>Smart Context Management</b><br>
        <img src="images/context.png" alt="Mervelas Context" width="400"/>
      </td>
    </tr>
    <tr>
       <td align="center">
        <b>Configuration & Settings</b><br>
        <img src="images/config.png" alt="Mervelas Config" width="400"/>
      </td>
      <td align="center">
        <b>Custom Agent Creation</b><br>
        <img src="images/agentcreate.png" alt="Mervelas Custom Agents" width="400"/>
      </td>
    </tr>
  </table>
</div>

---

## 🚀 Compile & Run Locally

To get started with Mervelas today, you'll need to compile it from the source using Bun.

### 1. Prerequisites

Mervelas requires [Bun](https://bun.sh) to compile gracefully and run smoothly on your local machine.

### 2. Setup Guide

```bash
# Clone the repository
git clone https://github.com/swadhinbiswas/Mervelas.git
cd Mervelas

# Install native dependencies
bun install

# Compile the CLI via the internal bundler
bun run scripts/build.ts

# Execute Mervelas
node dist/cli.mjs
```

### 3. Provider Configuration

Once running, simply execute `/config` or `/login` in the prompt to set up your LLM provider and paste your API key. That's it!

---

## 🛠️ Essential Commands

Mervelas offers a rich suite of integrated workflows. Inside the CLI, try out:

- `/config` — Configure your LLM providers, manage API keys, and tweak models.
- `/context` — View exact token usage and visualize your context window limits cleanly.
- `/agents` — Create and switch between highly specific local coding agents seamlessly.
- `/mcp` — Integrate **Model Context Protocol** (MCP) servers locally to give your model superpowered access to other applications.
- `/status` — View your local development state or system resource consumption.
- `/login` — Swiftly swap backends and models locally.

---

## 💻 Environment Configuration

For headless setups and CI workflows, rely on environment variables:

```bash
# OpenAI or NIM setup
MERVELAS_API_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.openai.com/v1

# OpenRouter setup
MERVELAS_API_PROVIDER=openroute
OPENROUTER_API_KEY=your_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api
```

---

## 🏗️ Contributing & Development Boundaries

If you are contributing patches or developing advanced features for Mervelas, please adhere to these core rules to avoid DMCA cross-overs or architectural regressions:

- **Custom UI System:** Never directly import `ink` blindly from npm. Mervelas relies securely on layout structures (`Box`, `Text`) routed strictly through `src/ink.ts`.
- **Top-Level Pure Behavior:** Do _not_ instantiate blocking state singletons or file reads on file-load. Tools and execute loops must use the `load: () => import(...)` delay abstraction so that the CLI footprint remains completely idle until actively invoked.
- **Type Checking:** Continuously test strict ES2023 adherence using `npm run typecheck` (`tsc --noEmit`).

<br>

<div align="center">
<i>Built for developers who demand complete sovereignty over their workflows.</i>
</div>
