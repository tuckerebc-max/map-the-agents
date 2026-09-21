# Sessions

Postal writes the conversation to disk after every turn, so closing the terminal does not kill your conversation. All conversations are resume-able and can be accessed by running a command shown below.

```bash
postal --continue        # resume the most recent session in this directory
postal --resume 3f2a1c   # resume a specific session (a prefix of the id is enough)
postal sessions          # what is saved for this directory
postal sessions --all    # every directory
postal sessions rm 3f2a1c
```

Inside the TUI, `/sessions` lists what is saved and `/resume` loads one into the running agent, transcript and token totals included. The system prompt is not restored: it is rebuilt from the current config and tool set, so a resumed session picks up any model, approval, or `AGENTS.md` changes you have made since.

## Checkpoints

Each save is a checkpoint, a full snapshot of the conversation at that point. Turns are checkpointed automatically, and `/checkpoint <label>` marks one by hand before you try something risky:

```text
❯ /checkpoint before the refactor
Saved before the refactor · 24 messages · session 3f2a1c8b

❯ /checkpoints
1  a41f9c02  turn 3                 18 msgs  22m ago
2  7d2b1e55  turn 4                 24 msgs  4m ago
3  e0c34a91  before the refactor    24 msgs  just now

❯ /rewind 1
Rewound to turn 3 · 18 messages · turn 3
```

Rewinding replaces the conversation the model sees, which makes it the way out of a turn that went sideways: roll back to before the detour and take another run at it. **It only rewinds the conversation, not your files** — anything already written to disk stays written.

## On disk

Sessions live in `~/.config/postal/sessions/<id>/`, one directory per session, with the transcripts in a JSONL file next to a small `meta.json`. Old checkpoints are trimmed once a session passes `max_checkpoints` (autosaves go first, named ones are kept), and the oldest sessions are dropped past `max_sessions`. Set `enabled = false` under `[session]` to keep conversations off disk entirely — see [Configuration](configuration.md).
