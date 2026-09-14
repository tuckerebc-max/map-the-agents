# llm-coding-agent specification

A Claude Code style coding agent built on [LLM](https://llm.datasette.io/). It runs an
interactive terminal session in which a model can read and edit files, search a project
and execute shell commands, with a permission system that keeps the human in control.

## Goals

- A terminal coding agent in the style of Claude Code: you describe a task, the model
  works on it using tools, streaming its reasoning and actions to the terminal.
- Work with **any model supported by LLM** that can handle tool calling, including
  models provided by plugins (`llm-anthropic`, `llm-gemini`, local models, etc).
- Ship as an **LLM plugin**: installing it adds an `llm code` subcommand and registers
  the tools so they can also be used with `llm chat` and `llm prompt --tool`.
- Provide a clean **Python API** so other applications can embed the agent loop.
- Safe by default: file writes and shell commands require user approval unless
  explicitly pre-approved.

## Non-goals (for the initial release)

- No sandboxing or containerization - the agent runs with the invoking user's
  permissions. Safety comes from the approval flow, not isolation.
- No MCP support, sub-agents, git integration or IDE integration - these are future
  work, listed at the end.
- No Windows-specific shell handling in the first release (commands run via
  `subprocess` with `shell=True`; POSIX shells are the target).

## Dependencies

- Python 3.10+
- `llm>=0.32a3` - the agent depends on APIs introduced in the 0.32 alpha series:
  - `model.chain()` / `conversation.chain()` for the tool-execution loop
  - `llm.Toolbox` for bundling the coding tools as a stateful class
  - `before_call` + `llm.CancelToolCall` for the permission system
  - `llm.PauseChain` for pausing a chain pending approval in embedded (non-CLI) use
  - guaranteed unique `tool_call_id` on every tool call
  - `response.to_dict()` / `messages=` for persisting and resuming sessions

  Until 0.32 is stable, `pyproject.toml` pins `llm>=0.32a3` and installation requires
  `pip install --pre llm-coding-agent` (or an explicit `llm>=0.32a3` pin). When 0.32
  final ships the pin becomes `llm>=0.32`.
- No other runtime dependencies beyond what `llm` already brings in (`click`,
  `pydantic`, etc). The terminal UI uses `click` styling only - no `rich`/`textual`.

## Installation and invocation

```bash
llm install llm-coding-agent      # or: pip install --pre llm-coding-agent
llm code                          # start an interactive session in the current directory
llm code "add type hints to utils.py"   # start with an initial prompt
llm code -m claude-fable-5        # choose a model (defaults to the llm default model)
```

### `llm code` options

| Option | Description |
| --- | --- |
| `PROMPT` (argument, optional) | Initial task. If omitted, start an interactive prompt. |
| `-m/--model MODEL` | Model ID, defaults to the configured LLM default model. |
| `-s/--system TEXT` | Append extra instructions to the built-in system prompt. |
| `-d/--directory PATH` | Root directory for the session (default: cwd). All tool access is confined to this tree. |
| `--yolo` | Auto-approve every tool call (no prompts). |
| `--allow PATTERN` | Pre-approve commands matching a glob-style pattern, e.g. `--allow "pytest*"` `--allow "git diff*"`. Repeatable. |
| `--no-tool TOOL` | Disable a named tool, e.g. `--no-tool execute_command`. Repeatable. |
| `-c/--continue` | Continue the most recent `llm code` conversation (uses LLM's conversation log). |
| `--cid ID` | Continue a specific logged conversation. |
| `-o/--option KEY VALUE` | Pass model options through, matching `llm prompt -o`. |
| `--chain-limit N` | Maximum tool-execution rounds per prompt (default 25, `0` = unlimited). |

### Interactive session

The session is a read-eval loop:

1. Read a prompt from the user.
2. Run `conversation.chain(prompt)` with the toolbox attached.
3. Stream model text to stdout as it arrives; render each tool call and its result as
   a compact one-line summary (tool name + key arguments, then truncated output).
4. When the chain finishes, prompt for the next input.

Session commands (lines starting with `!` are not sent to the model):

- `!quit` / Ctrl-D - exit
- `!model MODEL` - switch models mid-session (conversation history carries over)
- `!tokens` - show cumulative token usage for the session
- `!yolo` - toggle auto-approval

Everything is logged to LLM's SQLite database exactly like `llm chat`, so `llm logs`
shows full transcripts including tool calls and results.

## The toolbox

All tools live on a single `CodingTools(llm.Toolbox)` class, constructed with the
session's root directory. Non-underscore methods become tools automatically. The
plugin also registers it via the `register_tools` hook so users can run
`llm chat --tool CodingTools` without the `llm code` UI.

Path rules shared by all file tools:

- Relative paths resolve against the session root.
- Absolute paths are allowed but must resolve (after `..` and symlink resolution) to a
  location inside the session root; anything else returns an error string.
- Errors are returned as strings prefixed `Error:` rather than raised, so the model
  can read them and self-correct.

### `read_file(path, offset=0, limit=2000)`

Read a text file. Returns content in `cat -n` style with line numbers starting at 1,
which gives the model stable line references for editing.

- `offset`: first line to read (0-based); `limit`: maximum number of lines.
- Lines longer than 2,000 characters are truncated with a marker.
- If the result would exceed ~50 KB, return the truncated portion plus a note telling
  the model to page with `offset`/`limit`.
- Binary files return `Error: binary file` with the file size.

### `write_file(path, content)`

Create or overwrite a file, creating parent directories as needed. Returns a
confirmation with the byte count. *Requires approval.*

### `edit_file(path, old_string, new_string, replace_all=False)`

Exact string replacement, the Claude Code editing model:

- `old_string` must appear in the file; if it appears more than once and
  `replace_all` is false, return
  `Error: old_string occurs N times - provide more context or pass replace_all=true`.
- `old_string` must differ from `new_string`.
- On success return a small unified-diff style snippet of the changed region so the
  model can verify its edit. *Requires approval.*

### `list_files(pattern="**/*", path=".")`

Glob for files under a directory. Returns matching relative paths sorted by
modification time (newest first), capped at 200 entries with a `... and N more`
marker. Respects `.gitignore` when the root is a git repository (implemented by
delegating to `git ls-files` when available, falling back to `pathlib` globbing that
skips `.git`, `node_modules`, `__pycache__`, and hidden directories).

### `search_files(pattern, path=".", glob=None, max_results=100)`

Content search. Uses `rg` (ripgrep) when available, falling back to a pure-Python
regex scan. Returns `path:line_number: line` matches, capped at `max_results` with a
truncation marker. `glob` filters candidate files (e.g. `*.py`).

### `execute_command(command, timeout=120)`

Run a shell command with the session root as working directory. *Requires approval*
(subject to `--allow` patterns).

- Captures stdout and stderr combined, returns them with the exit code appended as a
  final `Exit code: N` line.
- Output over ~30 KB is truncated from the middle, keeping head and tail.
- `timeout` is in seconds, capped at 600; on timeout the process group is killed and
  `Error: command timed out after Ns` is returned with any partial output.
- Runs via `subprocess.run(..., shell=True, start_new_session=True)` so timeouts can
  kill the whole process tree.

## Permission system

Implemented as a `before_call` callback passed to the chain - no tool-side logic:

```python
def before_call(tool, tool_call):
    if not policy.allows(tool, tool_call):
        decision = ui.confirm(tool, tool_call)   # y / n / a(lways)
        if decision is Deny:
            raise llm.CancelToolCall("User declined this tool call")
        if decision is Always:
            policy.remember(tool, tool_call)
```

- Read-only tools (`read_file`, `list_files`, `search_files`) never prompt.
- `write_file` and `edit_file` prompt with the target path and a preview (full content
  for writes under 40 lines, a diff for edits). Answering `a` approves all future
  writes/edits for the session.
- `execute_command` prompts with the exact command. Answering `a` adds a prefix
  pattern for that command's first token (e.g. approving `pytest -x` with `a` allows
  `pytest*` for the rest of the session). `--allow` patterns and `--yolo` skip the
  prompt.
- A denied call raises `llm.CancelToolCall`, which LLM reports back to the model as a
  cancelled tool result - the model sees the refusal and can propose an alternative.
- Approval decisions are session-scoped and never persisted to disk in this release.

In embedded (Python API) use, where there is no terminal to prompt, the default policy
instead raises `llm.PauseChain` from `before_call`-adjacent tool wrappers so the host
application can record the pending `tool_call`, obtain approval out-of-band, and
resume the chain later by re-running it with the persisted message history (LLM
executes unresolved tool calls on resume, matched by `tool_call_id`).

## System prompt

A built-in system prompt (stored as `llm_coding_agent/system_prompt.md`, loaded as
package data) that:

- names the tools and states the workflow: explore with `list_files`/`search_files`/
  `read_file` before editing; prefer `edit_file` over `write_file` for existing files;
  verify changes by running tests or the relevant command.
- instructs the model to always `read_file` before `edit_file`, keep edits minimal and
  match existing code style.
- tells it to report failures honestly (include failing output) and to stop and ask
  rather than guess when the task is ambiguous.
- includes the session root path, the platform, and today's date.

`-s/--system` appends to (never replaces) this prompt.

## Agent loop details

- The loop is `conversation.chain(prompt, chain_limit=N)`; LLM handles executing tool
  calls and feeding results back until the model stops calling tools.
- `chain_limit` (default 25) bounds runaway loops; on hitting the limit the CLI prints
  a notice and returns control to the user, who can say "continue".
- Streaming: iterate `chain.responses()`, printing text chunks as they arrive; tool
  calls/results are rendered between responses via the `after_call` callback.
- Ctrl-C during a chain cancels the in-flight request, prints any pending tool calls
  as "interrupted", and returns to the prompt without exiting the session.

## Python API

```python
from llm_coding_agent import CodingAgent

agent = CodingAgent(
    model="claude-fable-5",        # or an llm model instance
    root="/path/to/project",
    approve=lambda tool, tool_call: True,   # or a callable returning bool
    chain_limit=25,
)
result = agent.run("Fix the failing test in tests/test_parser.py")
print(result.text)          # final model text
print(result.tool_calls)    # list of (ToolCall, ToolResult) pairs
agent.run("Now add a changelog entry")   # same conversation continues
```

- `approve=None` (default) auto-approves read-only tools and raises `llm.PauseChain`
  for mutating ones; `approve=True` approves everything.
- `CodingAgent.resume(messages, ...)` reconstructs a session from persisted messages
  (`response.to_dict()` output), re-executing any unresolved tool calls.
- `CodingTools` is importable directly for use with plain `model.chain(...,
  tools=[CodingTools(root)])`.

## Project layout

```
llm_coding_agent/
    __init__.py        # CodingAgent, CodingTools re-exports, plugin hooks
    plugin.py          # register_commands (llm code) and register_tools hooks
    tools.py           # CodingTools(llm.Toolbox)
    agent.py           # CodingAgent - loop, permissions, resume
    cli.py             # interactive session UI
    system_prompt.md
tests/
```

`pyproject.toml` gains:

```toml
dependencies = ["llm>=0.32a3"]

[project.entry-points.llm]
coding_agent = "llm_coding_agent.plugin"
```

## Testing

- Tool unit tests run against a `tmp_path` project fixture: path confinement
  (including `..` and symlink escapes), read paging and truncation, edit uniqueness
  errors, command timeout and exit-code reporting. No model or network required.
- Agent-loop tests use LLM's echo/mock model utilities to script tool-call sequences
  and assert: chain-limit enforcement, `CancelToolCall` on denial reaching the model,
  `PauseChain` surfacing pending calls, and resume executing unresolved calls exactly
  once.
- CLI tests drive `llm code` via `click.testing.CliRunner` with a mocked model.
- CI (existing GitHub Actions workflow) tests Python 3.10-3.13, installing `llm` with
  `--pre`.

## Future work

Explicitly out of scope for the first release, in rough priority order:

1. Persistent per-project config and approvals (`.llm-code.toml`)
2. A `todo`/plan tool and progress rendering for long tasks
3. Sub-agents (a `spawn_agent` tool running a nested chain with its own budget)
4. MCP server support once LLM grows it
5. Git-aware tools (commit, diff review) and a non-interactive `llm code --print`
   mode for scripting/CI
