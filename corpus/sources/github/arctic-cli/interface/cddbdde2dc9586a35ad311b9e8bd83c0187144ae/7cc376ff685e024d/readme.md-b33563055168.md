<p align="center">
  <img src="https://www.usearctic.sh/arctic-logo.png" alt="Arctic logo" width="200">
</p>
<p align="center">
<a href="https://discord.gg/B4HqXxNynG"><img alt="Discord" src="https://img.shields.io/badge/discord-join-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
<a href="https://github.com/arctic-cli/interface"><img alt="GitHub" src="https://img.shields.io/github/stars/arctic-cli/interface?style=flat-square" /></a>
</p>

Arctic is for developers who want to use AI coding agents without losing track of their usage limits or juggling between personal and work accounts.

- Real-time usage tracking for all your coding plans
- Multiple accounts per provider (personal + work)
- Switch models mid-conversation
- Imports your existing Claude Code and OpenCode config

[![Arctic Terminal UI](https://www.usearctic.sh/session_interface.png)](https://usearctic.sh)

## Get Started

```bash
curl -fsSL https://usearctic.sh/install | bash
```

```bash
source ~/.bashrc  # or ~/.zshrc, or restart your terminal
```

```bash
arctic
```

## Supported Providers

**Coding Plans:** Claude Code • Codex • Gemini CLI • Antigravity • GitHub Copilot • Z.AI • Kimi • Amp Code • Qwen Code • MiniMax

**API Providers:** OpenAI • Anthropic • Google • Perplexity • Openrouter • Ollama • [and more](https://usearctic.sh/docs/providers)

## FAQ

<details>
<summary><strong>Coming from Claude Code?</strong></summary>

Arctic automatically imports your Claude Code setup—custom commands, agents from `~/.claude/agents/`, and MCP servers work out of the box.

</details>

<details>
<summary><strong>Is my data private?</strong></summary>

Yes. Arctic runs on your machine and connects directly to your AI provider. Your conversations and data are stored locally on your device and never sent to external servers. We do collect anonymous telemetry to understand how Arctic is used, but this is temporary while Arctic is early in development. You can disable telemetry anytime with `arctic telemetry disable`.

</details>

<details>
<summary><strong>Can I use my own API keys?</strong></summary>

Yes. Arctic supports API keys for OpenAI, Anthropic, Google, Perplexity, Openrouter, Ollama, and more.

</details>

<details>
<summary><strong>What about telemetry?</strong></summary>

Arctic uses anonymous telemetry to understand how the tool is used and improve the experience. This is temporary while Arctic is early in development. You can opt out at any time:

```bash
arctic telemetry disable
```

To check the current telemetry status:

```bash
arctic telemetry status
```

</details>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and guidelines.

---

[Documentation](https://usearctic.sh/docs) • [Discord](https://discord.gg/B4HqXxNynG) • [License](LICENSE)
