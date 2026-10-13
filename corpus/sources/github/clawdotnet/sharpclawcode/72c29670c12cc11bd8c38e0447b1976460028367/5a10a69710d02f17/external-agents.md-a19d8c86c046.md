# External Agents

SharpClaw can run external agent CLIs as supervised, session-aware operations. External agents do not replace SharpClaw's runtime; they are child processes that must pass permission policy before mutating runs.

## Configure

Use `.sharpclaw/config.jsonc`:

```jsonc
{
  "externalAgents": {
    "enabled": true,
    "requireApprovalForMutatingRuns": true,
    "adapters": {
      "codex": {
        "executablePath": "codex",
        "defaultArgs": []
      }
    }
  }
}
```

Built-in adapters are `claude`, `opencode`, `gemini`, and `codex`.

## Use

```bash
sharpclaw external list
sharpclaw external status
sharpclaw external run --adapter codex --prompt "Review this repository"
```

In the REPL:

```text
/agents external list
/agents external run codex Review this repository
```

MVP support is text-mode process execution. Structured streaming is deferred until external CLIs expose stable machine-readable streams. Prompts are currently passed through each CLI's text-mode argument surface, so very large prompts should be run from a SharpClaw session or skill context rather than pasted as a single command argument.
