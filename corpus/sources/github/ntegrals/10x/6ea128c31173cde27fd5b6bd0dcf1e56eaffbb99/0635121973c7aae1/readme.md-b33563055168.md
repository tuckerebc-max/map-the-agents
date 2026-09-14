<h1 align="center">10x</h1>

<p align="center">
  <b>Up to 20x faster coding - with Superpowers.</b>
</p>

<p align="center">
  <a href="https://github.com/0xCrunchyy/10x/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://www.npmjs.com/package/10x-cli"><img src="https://img.shields.io/npm/v/10x-cli.svg" alt="npm version"></a>
  <a href="https://github.com/0xCrunchyy/10x"><img src="https://img.shields.io/github/stars/0xCrunchyy/10x?style=social" alt="GitHub stars"></a>
</p>

<p align="center">
  <img src="media/header.webp" alt="10x - Up to 20x faster, with Superpowers" width="100%">
</p>

---

## Quick Start

```bash
npm install -g 10x-cli

10x
```

## Why 10x?

| Feature                                | 10x                                | Claude Code       | Cursor            | GitHub Copilot    |
| -------------------------------------- | ---------------------------------- | ----------------- | ----------------- | ----------------- |
| **Superpowers (Multi-Step Pipelines)** | Chain models for complex workflows | No                | No                | No                |
| **Smart Model Routing**                | Auto-picks fastest model per task  | Single model      | Single model      | Single model      |
| **Speed**                              | Up to 20x faster                   | 1x                | ~1x               | ~1x               |
| **Open Source**                        | MIT Licensed                       | Closed source     | Closed source     | Closed source     |
| **BYOK (Bring Your Own Key)**          | Full control over costs            | Subscription only | Subscription only | Subscription only |

## Superpowers

Multi-step AI workflows that chain different models together. Each step can use a different model tier, automatically routing to the fastest model that can handle it.

| Command            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `/review <path>`   | Code review with security, performance, and style analysis |
| `/pr`              | Generate PR description from staged/committed changes      |
| `/refactor <file>` | Guided refactoring with analysis and implementation        |
| `/debug <issue>`   | Step-by-step debugging: reproduce, analyze, fix            |
| `/explain <path>`  | Deep dive explanation of code architecture                 |
| `/test <file>`     | Generate comprehensive test suite                          |

### Custom Superpowers

Define workflows in `.10x/superpowers/` or `~/.config/10x/superpowers/`:

```markdown
---
name: debug
trigger: /debug
---

## Step 1: Understand (model: fast)

{{input}} - Find and read the relevant code.

## Step 2: Fix (model: smart)

Based on {{previous}}, implement a fix.
```

## Model Tiers

| Tier           | Model         | Speed | Best For                        |
| -------------- | ------------- | ----- | ------------------------------- |
| ⚡⚡ Superfast | GPT OSS 20B   | 20x   | Simple queries, explanations    |
| ⚡ Fast        | Kimi K2 1T    | 4x    | Code generation, refactoring    |
| ◆ Smart        | Claude Opus 4 | 1x    | Complex reasoning, architecture |

## Configuration

### Project Context

Create `10X.md` in your project root:

```markdown
# Project: MyApp

Tech: TypeScript, React, PostgreSQL
Conventions: Functional components, named exports
```

### Custom Skills

Create prompts in `.10x/skills/` or `~/.config/10x/skills/`:

```markdown
---
name: commit
---

Analyze staged changes and generate a conventional commit message.
```

Invoke with `/<skill-name>`.

## CLI

```
10x                      Start interactive session
10x --byok               Use your own OpenRouter API key
10x --model <tier>       Set model tier (superfast, fast, smart)
10x --resume <name>      Resume a session
10x -x "<prompt>"        Execute prompt and exit
```

## License

[MIT](LICENSE)
