<div align="center">

<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/empryo-mote-dark.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/empryo-mote-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="assets/empryo-mote-dark-normal.gif" />
  <source media="(prefers-color-scheme: light)" srcset="assets/empryo-mote-light-normal.gif" />
  <img src="assets/empryo-mote-light-normal.gif" width="150" height="150" alt="Empryo" />
</picture>

# Empryo

<sub>previously **SoulForge**</sub>

**Code in context.**

AI coding with a map of your codebase.

[Website](https://empryo.com) · [Download](https://empryo.com/download) · [Benchmarks](https://empryo.com/benchmarks) · [Changelog](https://empryo.com/changelog) · [Discussions](https://github.com/proxysoul/soulforge/discussions) · [Discord](https://discord.gg/fX4H7GYSMJ)

<img alt="Empryo in action" src="assets/intro_picture.png" width="880" />

</div>

---

**SoulForge is now Empryo** — the same symbol-level, graph-powered agent, rebuilt with a desktop app, a faster engine, and a composable core. This repository is Empryo's public home for issues and discussions.

## Install

```bash
# macOS / Linux
curl -fsSL https://empryo.com/install.sh | bash

# Windows (PowerShell)
irm https://empryo.com/install.ps1 | iex
```

Official installers and direct downloads are available only from [empryo.com/download](https://empryo.com/download). Empryo is not distributed through Homebrew, WinGet, or npm.

```bash
empryo --set-key anthropic sk-ant-...   # or run locally with Ollama — no key required
cd your-project
empryo
```

Desktop app and prebuilt binaries: [empryo.com/download](https://empryo.com/download). Runs on **macOS, Linux, and Windows**. Do not download Empryo binaries from GitHub Releases or third-party package managers.

## Why Empryo

Most coding agents grep, read whole files, and patch strings — they never know what depends on the code they just changed. Empryo builds understanding before it mutates anything:

- **It maps before it reads.** On launch, tree-sitter parses your repo into a live graph — every symbol, import, and call site, ranked by PageRank and git co-change. Graph queries answer in milliseconds and cost zero LLM tokens.
- **It knows the blast radius.** Before an edit, the agent sees what imports a file, what historically changes with it, and how far a change ripples — "what breaks if I touch this?" is answered before the first keystroke.
- **It edits through the AST.** 65+ symbol-level operations, atomic batches with all-or-nothing rollback, structural edits across 30+ languages, and a typecheck as the gate. Nothing breaks on whitespace.
- **It treats tokens as spend.** The graph does the navigation models usually burn context on — fewer reads, fewer steps, smaller bills at any scale.

## What's inside

| | |
|---|---|
| **Code genome** | live dependency graph: tree-sitter across 30+ languages, PageRank + git co-change ranking, blast-radius tags, millisecond search |
| **Symbol-level editing** | 65+ AST operations (atomic, with rollback) + structural edits in 30+ languages |
| **Multi-agent** | parallel explore/edit agents with a shared I/O cache — cheap models scout, strong models write |
| **Task router** | ten routable roles, any model in any seat, per tab — your own mixture of experts |
| **Time machine** | every prompt is a git checkpoint; rewind code and conversation together, land on any turn |
| **Three surfaces** | native desktop app, full terminal UI, headless CLI for scripts and CI — one genome, three phenotypes |
| **LSP + MCP** | 576+ language servers via Mason, any MCP server, 13 lifecycle hooks |
| **Free compaction** | structural context compaction with no LLM call — long sessions stay cheap |

## One agent, many brains

Empryo isn't one model in a loop — it's a crew, and you assign the seats. Every role is a routable slot that takes any model from any of the 22 providers:

<div align="center">

`brain` · `spark` <sub>scout</sub> · `ember` <sub>code</sub> · `explore` · `verify` <sub>review</sub> · `goal review` · `desloppify` · `summarize` · `compact` · `web search`

</div>

- **Per tab.** Each workspace tab carries its own routing — a frontier model writing code in one tab, a fast cheap one triaging issues in the next, a local model on a private repo in a third.
- **Per config.** Set defaults globally or per project; override any slot from the tab. Cheap models scout, strong models write, reviewers judge with clean context.
- **Custom agents.** Define your own agents — a prompt, a model, a tool policy — and dispatch them alongside the built-ins. Mix and match providers freely inside a single run.
- **Cache-aware by design.** Routing keeps prompt-cache prefixes stable — sub-agents inherit their parent's cache line, so repeated context bills at cache-read rates instead of full price.
- **Costs, itemized.** Live spend tracking per model, per sub-agent, per tab, per session, per day — you always know where the tokens went.

## Benchmarks

Head-to-head against pi — same models, same repositories, same tasks. The graph does more with less:

| | Round 1 <sub>3 bugs × 3 models</sub> | Round 2 <sub>5 real bugs · hono / zod / ky</sub> |
|---|:---:|:---:|
| Bugs fixed | **8/9** vs 7/9 | **7/10** vs 6/10 |
| Cost | **28% lower** — $1.13 vs $1.58 | **23% lower** — $7.08 vs $9.19 |
| Wall-clock | **57% faster** — 4m 16s vs 10m | **32% faster** — 22m 30s vs 32m 55s |
| Efficiency | **5.7× fewer input tokens** — 1.09M vs 6.21M | **28% fewer steps** — 274 vs 382 |

Round 2 used real bugs from merged PRs (post-training-cutoff, history scrubbed, regression tests injected after each run). Full methodology and transcripts: [empryo.com/benchmarks](https://empryo.com/benchmarks) · reproduce at [proxysoul/pi-vs-empryo-bench](https://github.com/proxysoul/pi-vs-empryo-bench).

## Private by design

Empryo runs entirely on your machine. Bring your own key — Anthropic, OpenAI, Google, Groq, DeepSeek, Bedrock, and 16 more, or any OpenAI-compatible endpoint — or run fully local with Ollama / LM Studio. No proxy in the middle, no code leaving your machine, no per-seat fee. **Free to use.**

## SoulForge

SoulForge remains available to download and install, and continues to receive fixes for bugs and critical issues. New features and active development have moved to Empryo.

```bash
brew tap proxysoul/tap && brew install soulforge
# or
bun install -g @proxysoul/soulforge
```

## This repository

- **[Issues](https://github.com/proxysoul/soulforge/issues)** and **[Discussions](https://github.com/proxysoul/soulforge/discussions)** — the home for Empryo bug reports, questions, and ideas.
- The SoulForge source remains archived here under its existing license (see [`LICENSE`](LICENSE)).

## Sponsors

<div align="center">

<a href="https://llmgateway.io/dashboard?ref=6tjJR2H3X4E9RmVQiQwK" title="LLM Gateway">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/llmg-white.svg" />
    <source media="(prefers-color-scheme: light)" srcset="assets/llmg-dark.svg" />
    <img alt="LLM Gateway" src="assets/llmg-dark.svg" height="52" />
  </picture>
</a>

<sub>One API, 200+ models, up to 30% off frontier. Wired in as the <code>llmgateway</code> provider.</sub>

<sub><a href="https://github.com/sponsors/proxysoul">Sponsor</a> · <a href="https://paypal.me/waeru">PayPal</a> · <a href="BACKERS.md">Featured sponsors and all backers</a></sub>

</div>
