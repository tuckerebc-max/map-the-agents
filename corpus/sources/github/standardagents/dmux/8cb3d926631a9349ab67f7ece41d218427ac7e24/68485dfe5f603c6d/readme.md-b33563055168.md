<p align="center">
  <img src="./dmux.png" alt="dmux logo" width="400" />
</p>

<h3 align="center">Parallel agents with tmux and worktrees</h3>

<p align="center">
  Manage multiple AI coding agents in isolated git worktrees.<br/>
  Branch, develop, and merge &mdash; all in parallel.
</p>

<p align="center">
  <a href="https://dmux.ai"><strong>Documentation</strong></a> &nbsp;&middot;&nbsp;
  <a href="https://dmux.ai#getting-started"><strong>Getting Started</strong></a> &nbsp;&middot;&nbsp;
  <a href="https://github.com/formkit/dmux/issues"><strong>Issues</strong></a>
</p>

<p align="center">
  <strong>Language:</strong>
  <a href="./README.md">English</a> |
  <a href="./README.ja.md">日本語</a>
</p>

---

<img src="./dmux.webp" alt="dmux demo" width="100%" />

## Install

```bash
npm install -g dmux
```

## Quick Start

```bash
cd /path/to/your/project
dmux
```

Press `n` to create a new pane, type a prompt, pick one or more agents (or none for a plain terminal), and dmux handles the rest &mdash; worktree, branch, and agent launch.

On first run, dmux can configure a primary inference provider/model and an optional backup. It discovers models from the provider when possible and supports API-key providers, custom OpenAI-compatible endpoints, a Codex login backed by your ChatGPT subscription, or a Grok Build login backed by your SpaceXAI subscription. Reopen the flow with `s` → **Inference Providers**.

## What it does

dmux creates a tmux pane for each task. Every pane gets its own git worktree and branch so agents work in complete isolation. When a task is done, open the pane menu with `m` and choose Merge to bring it back into your main branch, or Create GitHub PR to push the branch and file a pull request.

- **Worktree isolation** &mdash; each pane is a full working copy, no conflicts between agents
- **Agent support** &mdash; Claude Code, Codex, OpenCode, Cline CLI, Gemini CLI, Qwen CLI, Amp CLI, pi CLI, Cursor CLI, Copilot CLI, and Crush CLI
- **Goal launches** &mdash; optionally start supported agents in goal mode from the initial prompt
- **Multi-select launches** &mdash; choose any combination of enabled agents per prompt
- **AI naming** &mdash; branches, commit messages, and active terminal panes named automatically
- **Durable terminals** &mdash; regular terminals restore in their last observed directory; if Codex, Claude, or another supported agent was running, dmux tracks it and resumes that conversation when the pane is recreated
- **Smart merging** &mdash; auto-commit, merge, and clean up in one step
- **macOS notifications** &mdash; background panes can send native attention alerts when they settle and need you, with a global off switch
- **Built-in file browser** &mdash; inspect a pane's worktree, search files, and preview code or diffs without leaving dmux
- **Pane visibility controls** &mdash; hide individual panes, isolate one project, or restore everything later without stopping work
- **Multi-project** &mdash; add multiple repos to the same session
- **Lifecycle hooks** &mdash; run scripts on worktree create, pre-merge, post-merge, and more

## Git Branch Controls

dmux can use default branch behavior or let you override branch details when creating a pane.

- Keep the default flow for fast creation, where dmux automatically picks the worktree and git branch names.
- Optionally choose a different base branch per pane.
- Optionally provide an explicit branch/worktree name (useful for issue-tracker ticket naming).
- Multi-agent launches still use shared naming with agent-specific suffixes.

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `n` | New pane (worktree + agent) |
| `t` | New terminal pane |
| `j` / `Enter` | Jump to pane |
| `m` | Open pane menu |
| `f` | Browse files in selected pane's worktree |
| `x` | Close pane |
| `h` | Hide/show selected pane |
| `H` | Hide/show all other panes |
| `p` | New pane in another project |
| `P` | Show only the selected project's panes, then show all |
| `s` | Settings |
| `q` | Quit |

## Requirements

- tmux 3.0+
- Node.js 18+
- Git 2.20+
- At least one supported agent CLI (for example [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [Grok Build](https://docs.x.ai/build/overview), [OpenCode](https://github.com/opencode-ai/opencode), [Cline CLI](https://docs.cline.bot/cline-cli/getting-started), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Qwen CLI](https://github.com/QwenLM/qwen-code), [Amp CLI](https://ampcode.com/manual), [pi CLI](https://www.npmjs.com/package/@mariozechner/pi-coding-agent), [Cursor CLI](https://docs.cursor.com/en/cli/overview), [Copilot CLI](https://github.com/github/copilot-cli), [Crush CLI](https://github.com/charmbracelet/crush))
- An inference provider API key, a Codex CLI login backed by a ChatGPT subscription, or a Grok Build CLI login backed by a SpaceXAI subscription (optional, for AI naming, summaries, and pane analysis)

## Documentation

Full documentation is available at **[dmux.ai](https://dmux.ai)**, including setup guides, configuration, and hooks.

## Contributing

See **[CONTRIBUTING.md](./CONTRIBUTING.md)** for the recommended local "dmux-on-dmux" development loop, hook setup, and PR workflow.

## License

MIT
