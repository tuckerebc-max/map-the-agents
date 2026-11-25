# Testing Guide

This guide is the user-facing test checklist for the current Python implementation.

It is organized by runtime surface, not by source file. Every implemented feature should have at least one concrete command here.

All commands below assume you are inside the repository root:

```bash
cd /path/to/claw-code-agent
```

## 1. Backend Setup

### 1.1 `vLLM` with Qwen3-Coder

```bash
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen3-Coder-30B-A3B-Instruct \
  --host 127.0.0.1 \
  --port 8000 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_xml
```

Verify the server:

```bash
curl http://127.0.0.1:8000/v1/models
```

### 1.2 `Ollama`

```bash
ollama serve
ollama pull qwen3
```

### 1.3 `LiteLLM Proxy`

```bash
pip install "litellm[proxy]"
litellm --model ollama/qwen3
```

### 1.4 Runtime environment variables

Use one backend at a time.

For `vLLM`:

```bash
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export OPENAI_API_KEY=local-token
export OPENAI_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct
```

For `Ollama`:

```bash
export OPENAI_BASE_URL=http://127.0.0.1:11434/v1
export OPENAI_API_KEY=ollama
export OPENAI_MODEL=qwen3
```

For `LiteLLM Proxy`:

```bash
export OPENAI_BASE_URL=http://127.0.0.1:4000
export OPENAI_API_KEY=anything
export OPENAI_MODEL=ollama/qwen3
```

If your cluster wraps `python3`, use an explicit interpreter path such as `/usr/bin/python3.9 -m ...` for the commands below.

### 1.5 Run the full unit test suite

```bash
python3 -m unittest discover -s tests -v
```

### 1.6 Run focused runtime suites

```bash
python3 -m unittest tests.test_agent_runtime -v
python3 -m unittest tests.test_query_engine_runtime -v
python3 -m unittest tests.test_mcp_runtime -v
python3 -m unittest tests.test_search_runtime -v
python3 -m unittest tests.test_task_runtime -v
python3 -m unittest tests.test_plan_runtime -v
python3 -m unittest tests.test_background_runtime -v
python3 -m unittest tests.test_remote_runtime -v
python3 -m unittest tests.test_config_runtime -v
python3 -m unittest tests.test_lsp_runtime -v
python3 -m unittest tests.test_account_runtime -v
python3 -m unittest tests.test_ask_user_runtime -v
python3 -m unittest tests.test_team_runtime -v
python3 -m unittest tests.test_tokenizer_runtime -v
python3 -m unittest tests.test_extended_tools -v
python3 -m unittest tests.test_porting_workspace -v
```

## 2. Installation And CLI Help

### 2.1 Editable install

```bash
pip install -e .
```

### 2.2 Main help

```bash
python3 -m src.main --help
python3 -m src.main agent --help
python3 -m src.main agent-chat --help
python3 -m src.main agent-resume --help
python3 -m src.main agent-bg --help
python3 -m src.main daemon --help
```

### 2.3 Packaged entrypoint

```bash
claw-code-agent agent "/help"
```

## 3. Mirrored Workspace And Inventory Commands

These commands do not depend on the live model backend.

### 3.1 Summary and audit commands

```bash
python3 -m src.main summary
python3 -m src.main manifest
python3 -m src.main parity-audit
python3 -m src.main setup-report
python3 -m src.main command-graph
python3 -m src.main tool-pool
python3 -m src.main bootstrap-graph
```

### 3.2 Inventory indexes

```bash
python3 -m src.main subsystems --limit 20
python3 -m src.main commands --limit 10 --query review
python3 -m src.main commands --limit 10 --no-plugin-commands
python3 -m src.main commands --limit 10 --no-skill-commands
python3 -m src.main tools --limit 10 --query MCP
python3 -m src.main tools --limit 10 --simple-mode
python3 -m src.main tools --limit 10 --no-mcp
python3 -m src.main tools --limit 10 --deny-prefix mcp
python3 -m src.main tools --limit 10 --deny-tool BashTool
```

### 3.3 Show exact mirrored entries

```bash
python3 -m src.main show-command review
python3 -m src.main show-tool MCPTool
```

### 3.4 Route and bootstrap reports

```bash
python3 -m src.main route "review MCP tool" --limit 5
python3 -m src.main bootstrap "review MCP tool" --limit 5
python3 -m src.main turn-loop "review MCP tool" --limit 5 --max-turns 2
python3 -m src.main turn-loop "review MCP tool" --limit 5 --max-turns 2 --structured-output
```

### 3.5 Mirrored execution shims

```bash
python3 -m src.main exec-command review "inspect security review"
python3 -m src.main exec-tool MCPTool "fetch resource list"
```

### 3.6 Flush and load mirrored sessions

```bash
python3 -m src.main flush-transcript "temporary mirrored transcript"
python3 -m src.main load-session <session-id>
```

## 4. Prepare Local Test Workspaces

Create reusable workspaces:

```bash
mkdir -p ./test_cases/.claude
mkdir -p ./test_cases_policy
mkdir -p ./test_cases_budget
mkdir -p ./test_cases_plugins/plugins/demo
mkdir -p ./test_cases_mcp
mkdir -p ./test_cases_tasks
mkdir -p ./test_cases_notebooks
```

### 4.1 Config fixtures

```bash
cat > ./test_cases/.claude/settings.json <<'EOF'
{
  "model": {
    "name": "project-model",
    "temperature": 0.1
  },
  "review": {
    "strict": false
  }
}
EOF

cat > ./test_cases/.claude/settings.local.json <<'EOF'
{
  "model": {
    "temperature": 0.0
  },
  "review": {
    "strict": true
  }
}
EOF
```

### 4.2 Account fixtures

```bash
cat > ./test_cases/.claw-account.json <<'EOF'
{
  "profiles": [
    {
      "name": "local",
      "provider": "openai",
      "identity": "dev@example.com",
      "authMode": "api_key"
    },
    {
      "name": "team",
      "provider": "anthropic",
      "identity": "team@example.com",
      "org": "Harness"
    }
  ]
}
EOF
```

### 4.2b Ask-user fixtures

```bash
cat > ./test_cases/.claw-ask-user.json <<'EOF'
{
  "answers": [
    {
      "question": "Approve deploy?",
      "answer": "yes"
    },
    {
      "question": "Choose rollout mode",
      "answer": "safe"
    }
  ]
}
EOF
```

### 4.2c Team fixtures

```bash
cat > ./test_cases/.claw-teams.json <<'EOF'
{
  "teams": [
    {
      "name": "reviewers",
      "description": "Code review group",
      "members": ["alice", "bob"]
    },
    {
      "name": "release",
      "description": "Release coordination group",
      "members": ["ops", "qa"]
    }
  ]
}
EOF
```

### 4.2d Notebook fixture

```bash
cat > ./test_cases_notebooks/demo.ipynb <<'EOF'
{
 "cells": [
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["print(1)\n"],
   "outputs": [],
   "execution_count": null
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
EOF
```

### 4.2e LSP fixture

```bash
cat > ./test_cases/sample.py <<'EOF'
def helper(value):
    """Double a numeric value."""
    return value * 2


def orchestrate(item):
    return helper(item)


class Greeter:
    def greet(self, name):
        return helper(len(name))
EOF

cat > ./test_cases/broken.py <<'EOF'
def broken(:
    pass
EOF
```

### 4.3 Remote fixtures

```bash
cat > ./test_cases/.claw-remote.json <<'EOF'
{
  "profiles": [
    {
      "name": "staging",
      "mode": "ssh",
      "target": "dev@staging",
      "workspaceCwd": "/srv/app",
      "sessionUrl": "wss://remote/session"
    },
    {
      "name": "preview",
      "mode": "deep-link",
      "target": "preview://session"
    },
    {
      "name": "tele",
      "mode": "teleport",
      "target": "teleport://workspace"
    },
    {
      "name": "direct",
      "mode": "direct-connect",
      "target": "direct://workspace"
    }
  ]
}
EOF
```

### 4.4 Search fixtures

```bash
cat > ./test_cases/.claw-search.json <<'EOF'
{
  "providers": [
    {
      "name": "local-search",
      "provider": "searxng",
      "baseUrl": "http://127.0.0.1:8080"
    },
    {
      "name": "backup-search",
      "provider": "tavily",
      "apiKeyEnv": "TAVILY_API_KEY"
    }
  ]
}
EOF
```

### 4.5 Hook and policy fixtures

```bash
cat > ./test_cases_policy/.claw-policy.json <<'EOF'
{
  "trusted": false,
  "managedSettings": {
    "reviewMode": "strict"
  },
  "safeEnv": ["HOOK_SAFE_TOKEN"],
  "hooks": {
    "beforePrompt": ["Respect workspace policy before acting."],
    "afterTurn": ["Persist the policy decision after each turn."],
    "beforeTool": {
      "read_file": ["Validate the path before reading."]
    }
  }
}
EOF

export HOOK_SAFE_TOKEN=demo-secret
```

### 4.6 Plugin fixtures

```bash
cat > ./test_cases_plugins/plugins/demo/plugin.json <<'EOF'
{
  "name": "demo-plugin",
  "hooks": {
    "beforePrompt": "Inject plugin prompt guidance.",
    "afterTurn": "Attach plugin after-turn guidance.",
    "onResume": "Reapply plugin state on resume.",
    "beforePersist": "Persist plugin state before saving.",
    "beforeDelegate": "Add plugin guidance before delegated children run.",
    "afterDelegate": "Add plugin guidance after delegated children finish."
  },
  "blockedTools": ["bash"],
  "toolAliases": [
    {
      "name": "plugin_read",
      "baseTool": "read_file",
      "description": "Plugin alias for reading files."
    }
  ],
  "virtualTools": [
    {
      "name": "demo_virtual",
      "description": "Return a rendered plugin response.",
      "responseTemplate": "plugin topic: {topic}"
    }
  ],
  "toolHooks": {
    "read_file": {
      "beforeTool": "Validate the path before reading.",
      "afterResult": "Summarize the file before the next action."
    }
  }
}
EOF

printf 'hello plugin\n' > ./test_cases_plugins/hello.txt
```

### 4.7 MCP fixtures

```bash
printf 'mcp notes\n' > ./test_cases_mcp/notes.txt

cat > ./test_cases_mcp/fake_stdio_mcp.py <<'EOF'
import json
import sys

RESOURCES = [
    {
        "uri": "mcp://remote/notes",
        "name": "Remote Notes",
        "mimeType": "text/plain"
    }
]

TOOLS = [
    {
        "name": "echo",
        "description": "Echo text",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string"}
            }
        }
    }
]

for raw in sys.stdin:
    raw = raw.strip()
    if not raw:
        continue
    message = json.loads(raw)
    method = message.get("method")
    if method == "initialize":
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {
                "protocolVersion": "2025-11-25",
                "capabilities": {"resources": {}, "tools": {}},
                "serverInfo": {"name": "fake-remote", "version": "1.0.0"}
            }
        }), flush=True)
        continue
    if method == "notifications/initialized":
        continue
    if method == "resources/list":
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {"resources": RESOURCES}
        }), flush=True)
        continue
    if method == "resources/read":
        uri = message.get("params", {}).get("uri")
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/plain",
                        "text": "remote notes via stdio"
                    }
                ]
            }
        }), flush=True)
        continue
    if method == "tools/list":
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {"tools": TOOLS}
        }), flush=True)
        continue
    if method == "tools/call":
        text = message.get("params", {}).get("arguments", {}).get("text", "")
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {
                "content": [{"type": "text", "text": "echo:" + text}],
                "isError": False
            }
        }), flush=True)
        continue
EOF

cat > ./test_cases_mcp/.claw-mcp.json <<'EOF'
{
  "servers": [
    {
      "name": "workspace",
      "resources": [
        {
          "uri": "mcp://workspace/notes",
          "name": "Notes",
          "path": "notes.txt",
          "mimeType": "text/plain"
        },
        {
          "uri": "mcp://workspace/inline",
          "name": "Inline",
          "text": "inline body"
        }
      ]
    }
  ],
  "mcpServers": {
    "remote": {
      "command": "python3",
      "args": ["-u", "./fake_stdio_mcp.py"]
    }
  }
}
EOF
```

### 4.8 Task workspace cleanup

```bash
mkdir -p ./test_cases_tasks
```

### 4.9 Custom agent definitions

```bash
mkdir -p ./test_cases_agents/.claude/agents

cat > ./test_cases_agents/.claude/agents/reviewer.md <<'EOF'
---
name: reviewer
description: "Review implementation changes carefully."
tools: read_file, grep_search
model: Qwen/Qwen3-Coder-30B-A3B-Instruct
initialPrompt: Start by identifying the highest-risk files.
---

Inspect code changes and summarize correctness risks, regressions, and missing tests.
EOF
```

## 5. Slash Command Matrix

Slash commands are handled locally before the model loop.

### 5.1 Core local slash commands

```bash
python3 -m src.main agent "/help" --cwd ./test_cases
python3 -m src.main agent "/commands" --cwd ./test_cases
python3 -m src.main agent "/context" --cwd ./test_cases
python3 -m src.main agent "/usage summarize current session" --cwd ./test_cases
python3 -m src.main agent "/context-raw" --cwd ./test_cases
python3 -m src.main agent "/env" --cwd ./test_cases
python3 -m src.main agent "/token-budget" --cwd ./test_cases
python3 -m src.main agent "/budget" --cwd ./test_cases
python3 -m src.main agent "/prompt" --cwd ./test_cases
python3 -m src.main agent "/system-prompt" --cwd ./test_cases
python3 -m src.main agent "/permissions" --cwd ./test_cases
python3 -m src.main agent "/model" --cwd ./test_cases
python3 -m src.main agent "/model demo-model" --cwd ./test_cases
python3 -m src.main agent "/tools" --cwd ./test_cases
python3 -m src.main agent "/agents" --cwd ./test_cases_agents
python3 -m src.main agent "/agents show reviewer" --cwd ./test_cases_agents
python3 -m src.main agent "/agents create reviewer-temp :: Review temporary code changes. :: Inspect code and summarize risks." --cwd ./test_cases_agents
python3 -m src.main agent "/agents update reviewer-temp Updated temp reviewer :: Focus on regressions and missing tests." --cwd ./test_cases_agents
python3 -m src.main agent "/agents delete reviewer-temp" --cwd ./test_cases_agents
python3 -m src.main agent "/memory" --cwd ./test_cases
python3 -m src.main agent "/status" --cwd ./test_cases
python3 -m src.main agent "/session" --cwd ./test_cases
python3 -m src.main agent "/clear" --cwd ./test_cases
```

### 5.2 Hook, policy, trust, config, and account slash commands

```bash
python3 -m src.main agent "/hooks" --cwd ./test_cases_policy
python3 -m src.main agent "/policy" --cwd ./test_cases_policy
python3 -m src.main agent "/trust" --cwd ./test_cases_policy
python3 -m src.main agent "/config" --cwd ./test_cases
python3 -m src.main agent "/config effective" --cwd ./test_cases
python3 -m src.main agent "/config source local" --cwd ./test_cases
python3 -m src.main agent "/config get review.strict" --cwd ./test_cases
python3 -m src.main agent "/settings" --cwd ./test_cases
python3 -m src.main agent "/account" --cwd ./test_cases
python3 -m src.main agent "/account profiles" --cwd ./test_cases
python3 -m src.main agent "/account profile local" --cwd ./test_cases
python3 -m src.main agent "/ask" --cwd ./test_cases
python3 -m src.main agent "/ask history" --cwd ./test_cases
python3 -m src.main agent "/login local" --cwd ./test_cases
python3 -m src.main agent "/logout" --cwd ./test_cases
```

### 5.3 Remote, search, team, task, and plan slash commands

```bash
python3 -m src.main agent "/remote" --cwd ./test_cases
python3 -m src.main agent "/remote staging" --cwd ./test_cases
python3 -m src.main agent "/remotes" --cwd ./test_cases
python3 -m src.main agent "/ssh staging" --cwd ./test_cases
python3 -m src.main agent "/teleport tele" --cwd ./test_cases
python3 -m src.main agent "/direct-connect direct" --cwd ./test_cases
python3 -m src.main agent "/deep-link preview" --cwd ./test_cases
python3 -m src.main agent "/disconnect" --cwd ./test_cases
python3 -m src.main agent "/remote-disconnect" --cwd ./test_cases
python3 -m src.main agent "/search" --cwd ./test_cases
python3 -m src.main agent "/search providers" --cwd ./test_cases
python3 -m src.main agent "/search provider local-search" --cwd ./test_cases
python3 -m src.main agent "/search use local-search" --cwd ./test_cases
python3 -m src.main agent "/search python argparse tutorial" --cwd ./test_cases
python3 -m src.main agent "/teams" --cwd ./test_cases
python3 -m src.main agent "/team reviewers" --cwd ./test_cases
python3 -m src.main agent "/messages" --cwd ./test_cases
python3 -m src.main agent "/messages reviewers" --cwd ./test_cases
python3 -m src.main agent "/plan" --cwd ./test_cases_tasks
python3 -m src.main agent "/planner" --cwd ./test_cases_tasks
python3 -m src.main agent "/tasks" --cwd ./test_cases_tasks
python3 -m src.main agent "/todo" --cwd ./test_cases_tasks
python3 -m src.main agent "/task missing-task-id" --cwd ./test_cases_tasks
python3 -m src.main agent "/task-next" --cwd ./test_cases_tasks
python3 -m src.main agent "/next-task" --cwd ./test_cases_tasks
```

### 5.4 MCP slash commands

```bash
python3 -m src.main agent "/mcp" --cwd ./test_cases_mcp
python3 -m src.main agent "/mcp tools" --cwd ./test_cases_mcp
python3 -m src.main agent "/mcp tool echo" --cwd ./test_cases_mcp
python3 -m src.main agent "/resources" --cwd ./test_cases_mcp
python3 -m src.main agent "/resource mcp://workspace/notes" --cwd ./test_cases_mcp
python3 -m src.main agent "/resource mcp://remote/notes" --cwd ./test_cases_mcp
python3 -m src.main agent "/mcp (MCP)" --cwd ./test_cases_mcp
```

## 6. Prompt, Context, And Token Accounting

### 6.1 Prompt and context reports

```bash
python3 -m src.main agent-prompt --cwd ./test_cases
python3 -m src.main agent-context --cwd ./test_cases
python3 -m src.main agent-context-raw --cwd ./test_cases
python3 -m src.main token-budget --cwd ./test_cases
python3 -m src.main agents --cwd ./test_cases_agents
python3 -m src.main agents reviewer --cwd ./test_cases_agents
python3 -m src.main agents-create reviewer-cli --cwd ./test_cases_agents --description "CLI-created reviewer agent." --prompt "Inspect code changes and summarize risks."
python3 -m src.main agents-update reviewer-cli --cwd ./test_cases_agents --description "Updated CLI reviewer." --prompt "Focus on regressions and missing tests."
python3 -m src.main agents-delete reviewer-cli --cwd ./test_cases_agents --source project
```

### 6.2 Extra working directories and `CLAUDE.md` toggle

```bash
python3 -m src.main agent-context --cwd ./test_cases --add-dir ./src
python3 -m src.main agent-context --cwd ./test_cases --disable-claude-md
```

### 6.3 Custom system prompt flags

```bash
python3 -m src.main agent-prompt \
  --cwd ./test_cases \
  --system-prompt "You are a strict review assistant."

python3 -m src.main agent-prompt \
  --cwd ./test_cases \
  --append-system-prompt "Always mention the active config source."

python3 -m src.main agent-prompt \
  --cwd ./test_cases \
  --override-system-prompt "Only output terse bullet points."
```

### 6.4 Tokenizer-aware context accounting

```bash
python3 -m src.main agent "/status" --cwd ./test_cases
python3 -m src.main agent-context --cwd ./test_cases
python3 -m src.main token-budget --cwd ./test_cases
```

Override the tokenizer backend:

```bash
export CLAW_CODE_TOKENIZER_PATH=/path/to/local/tokenizer
# or
export CLAW_CODE_TOKENIZER_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct

python3 -m src.main agent "/status" --cwd ./test_cases
python3 -m src.main agent-context --cwd ./test_cases
python3 -m src.main token-budget --cwd ./test_cases
```

If no tokenizer backend is available, the runtime will fall back to the heuristic counter and `/status` will report that.

## 7. Core Agent Loop And Chat

### 7.1 Read-only run

```bash
python3 -m src.main agent \
  "Read src/agent_runtime.py and summarize how the loop works." \
  --cwd .
```

### 7.2 Show transcript output

```bash
python3 -m src.main agent \
  "Read src/agent_session.py and summarize the session model." \
  --cwd . \
  --show-transcript
```

### 7.3 Streaming model responses

```bash
python3 -m src.main agent \
  "Inspect the repository and summarize the architecture." \
  --cwd . \
  --stream \
  --show-transcript
```

### 7.4 Interactive chat

```bash
python3 -m src.main agent-chat --cwd .
```

### 7.5 Interactive chat with an initial prompt

```bash
python3 -m src.main agent-chat \
  "Inspect the repository and tell me where the runtime loop lives." \
  --cwd .
```

Inside chat mode:

- type normal prompts to continue the same session
- use `/exit` or `/quit` to leave

### 7.6 Resume directly into chat mode

```bash
python3 -m src.main agent-chat \
  --resume-session-id <session-id> \
  --cwd .
```

## 8. Tool Execution

### 8.1 Read files

```bash
python3 -m src.main agent \
  "Read src/agent_tools.py and summarize the implemented tools." \
  --cwd .
```

### 8.2 Write files

```bash
python3 -m src.main agent \
  "Create TEST_WRITE.md in the current directory with one line: write test ok" \
  --cwd ./test_cases \
  --allow-write
```

### 8.3 Edit files

```bash
python3 -m src.main agent \
  "Create demo.txt with 'hello world', then replace 'world' with 'agent'." \
  --cwd ./test_cases \
  --allow-write
```

### 8.4 Glob and grep

```bash
python3 -m src.main agent \
  "Find Python files in the current directory, search for LocalCodingAgent, and summarize the matches." \
  --cwd .
```

### 8.5 Shell commands

```bash
python3 -m src.main agent \
  "Run pwd and ls in the current working directory, then summarize the result." \
  --cwd . \
  --allow-shell \
  --show-transcript
```

### 8.6 Unsafe shell mode

```bash
python3 -m src.main agent \
  "Explain whether destructive shell commands are currently allowed." \
  --cwd . \
  --allow-shell \
  --unsafe
```

### 8.7 Tool search

```bash
python3 -m src.main agent \
  "Use tool_search to find file-related tools and summarize the best options for reading and editing files." \
  --cwd .
```

### 8.8 Web fetch

```bash
python3 -m src.main agent \
  "Use web_fetch on file://$(pwd)/README.md and summarize the first section." \
  --cwd .
```

### 8.9 Sleep

```bash
python3 -m src.main agent \
  "Call the sleep tool for 0.1 seconds, then tell me it completed." \
  --cwd ./test_cases
```

### 8.10 Scratchpad root

```bash
python3 -m src.main agent \
  "Use the scratchpad if needed while inspecting the workspace, then summarize what you did." \
  --cwd ./test_cases \
  --allow-write \
  --scratchpad-root ./test_cases/.scratchpad \
  --show-transcript

ls -la ./test_cases/.scratchpad
```

## 9. Session Persistence, Resume, And File History

### 9.1 Create a saved session

```bash
python3 -m src.main agent \
  "Create a short TODO file in the current directory and explain what you wrote." \
  --cwd ./test_cases \
  --allow-write
```

At the end of the run, note:

```text
session_id=...
session_path=...
```

### 9.2 Resume a saved session

```bash
python3 -m src.main agent-resume \
  <session-id> \
  "Continue the previous task and improve the file." \
  --allow-write \
  --show-transcript
```

### 9.3 Inspect saved sessions

```bash
ls -lt .port_sessions/agent
```

### 9.4 File history replay on resume

```bash
python3 -m src.main agent \
  "Create notes.txt with one line, then update that line to mention file history." \
  --cwd ./test_cases \
  --allow-write

python3 -m src.main agent-resume \
  <session-id> \
  "Continue the previous work and tell me what files were changed before this turn." \
  --allow-write \
  --show-transcript
```

Look for `file_history_replay` messages in the transcript.

## 10. Background Sessions And Daemon Mode

### 10.1 Launch a background session

```bash
python3 -m src.main agent-bg "/help" --cwd ./test_cases
```

This prints:

- `background_id=...`
- `pid=...`
- `log_path=...`
- `record_path=...`

### 10.2 List background sessions

```bash
python3 -m src.main agent-ps
python3 -m src.main agent-ps --tail 20
```

### 10.3 Read background logs

```bash
python3 -m src.main agent-logs <background-id>
python3 -m src.main agent-logs <background-id> --tail 40
```

### 10.4 Attach to the current output snapshot

```bash
python3 -m src.main agent-attach <background-id>
python3 -m src.main agent-attach <background-id> --tail 40
```

### 10.5 Kill a background session

```bash
python3 -m src.main agent-kill <background-id>
```

### 10.6 Daemon wrappers

```bash
python3 -m src.main daemon start "/help" --cwd ./test_cases
python3 -m src.main daemon ps
python3 -m src.main daemon ps --tail 20
python3 -m src.main daemon logs <background-id>
python3 -m src.main daemon attach <background-id>
python3 -m src.main daemon kill <background-id>
```

## 11. Structured Output, Budgets, And Context Reduction

### 11.1 Structured output / JSON schema

Create a schema file:

```bash
cat > /tmp/claw_schema.json <<'EOF'
{
  "type": "object",
  "properties": {
    "status": { "type": "string" },
    "summary": { "type": "string" }
  },
  "required": ["status", "summary"],
  "additionalProperties": false
}
EOF
```

Run the agent with schema mode:

```bash
python3 -m src.main agent \
  "Inspect the current repository and respond in the requested JSON format." \
  --cwd . \
  --response-schema-file /tmp/claw_schema.json \
  --response-schema-name claw_summary \
  --response-schema-strict
```

### 11.2 Token budgets

```bash
python3 -m src.main agent \
  "Give a very long answer about the current repository." \
  --cwd . \
  --max-total-tokens 50

python3 -m src.main agent \
  "Read several files and explain them in detail." \
  --cwd . \
  --max-input-tokens 80 \
  --max-output-tokens 80
```

### 11.3 Reasoning, tool, delegation, model-call, and session-turn budgets

```bash
python3 -m src.main agent \
  "Solve a multi-step task and explain the result." \
  --cwd . \
  --max-reasoning-tokens 10

python3 -m src.main agent \
  "Read multiple files, search for symbols, and summarize the repo." \
  --cwd . \
  --max-tool-calls 1

python3 -m src.main agent \
  "Delegate two subtasks to inspect and summarize the repo." \
  --cwd . \
  --max-delegated-tasks 1

python3 -m src.main agent \
  "Continue inspecting the repository until you are done." \
  --cwd . \
  --max-model-calls 1

python3 -m src.main agent \
  "Work through the repository across multiple turns and keep going." \
  --cwd . \
  --max-session-turns 1
```

### 11.4 Cost budget

```bash
python3 -m src.main agent \
  "Inspect the repository and summarize it." \
  --cwd . \
  --input-cost-per-million 0.15 \
  --output-cost-per-million 0.60 \
  --max-budget-usd 0.000001
```

### 11.5 Budget override from local policy

```bash
cat > ./test_cases_budget/.claw-policy.json <<'EOF'
{
  "budget": {
    "max_model_calls": 0
  }
}
EOF

python3 -m src.main agent \
  "Say hello once." \
  --cwd ./test_cases_budget
```

Expected result: the run stops with a model-call budget exceeded message even though you did not pass `--max-model-calls`.

### 11.6 Streaming assistant output

```bash
python3 -m src.main agent \
  "Produce a long explanation of the current repository architecture." \
  --cwd . \
  --stream \
  --show-transcript
```

### 11.7 Automatic continuation after truncation

```bash
python3 -m src.main agent \
  "Write a long, structured explanation of the current repository." \
  --cwd . \
  --max-output-tokens 32 \
  --show-transcript
```

### 11.8 Snipping and compaction

```bash
python3 -m src.main agent \
  "Read src/agent_runtime.py, src/agent_session.py, src/query_engine.py, and src/plugin_runtime.py, then summarize all of them in detail." \
  --cwd . \
  --auto-snip-threshold 120 \
  --compact-preserve-messages 0 \
  --show-transcript

python3 -m src.main agent \
  "Read several large files from src and keep explaining the repository until the context gets compacted." \
  --cwd . \
  --auto-compact-threshold 120 \
  --compact-preserve-messages 1 \
  --show-transcript
```

## 12. Hook, Policy, And Trust Runtime

### 12.1 Inspect hook and trust state

```bash
python3 -m src.main agent "/hooks" --cwd ./test_cases_policy
python3 -m src.main agent "/policy" --cwd ./test_cases_policy
python3 -m src.main agent "/trust" --cwd ./test_cases_policy
python3 -m src.main agent "/permissions" --cwd ./test_cases_policy
python3 -m src.main agent "/tools" --cwd ./test_cases_policy
python3 -m src.main agent-context-raw --cwd ./test_cases_policy
python3 -m src.main agent-prompt --cwd ./test_cases_policy
```

### 12.2 Safe environment values in shell tools

```bash
python3 -m src.main agent \
  "Run bash and print HOOK_SAFE_TOKEN, then explain where it came from." \
  --cwd ./test_cases_policy \
  --allow-shell \
  --show-transcript
```

### 12.3 Tool blocking through policy

```bash
cat > ./test_cases_policy/.claw-policy.json <<'EOF'
{
  "trusted": false,
  "denyTools": ["bash"],
  "hooks": {
    "beforePrompt": ["Respect workspace policy before acting."],
    "afterTurn": ["Persist the policy decision after each turn."]
  }
}
EOF

python3 -m src.main agent \
  "Try to run bash and then explain what was blocked." \
  --cwd ./test_cases_policy \
  --allow-shell \
  --show-transcript
```

Look for:

- `hook_policy_tool_block`
- `tool_permission_denial`
- transcript guidance around the blocked tool

## 13. Config Runtime

### 13.1 CLI status and inspection

```bash
python3 -m src.main config-status --cwd ./test_cases
python3 -m src.main config-effective --cwd ./test_cases
python3 -m src.main config-source project --cwd ./test_cases
python3 -m src.main config-source local --cwd ./test_cases
python3 -m src.main config-get review.strict --cwd ./test_cases
python3 -m src.main config-get model.temperature --cwd ./test_cases --source local
```

### 13.2 Config writes

```bash
python3 -m src.main config-set review.mode '"strict"' --cwd ./test_cases
python3 -m src.main config-set review.enabled true --cwd ./test_cases
python3 -m src.main config-effective --cwd ./test_cases
```

### 13.3 Slash commands

```bash
python3 -m src.main agent "/config" --cwd ./test_cases
python3 -m src.main agent "/config effective" --cwd ./test_cases
python3 -m src.main agent "/config source local" --cwd ./test_cases
python3 -m src.main agent "/config get review.mode" --cwd ./test_cases
python3 -m src.main agent "/settings" --cwd ./test_cases
```

### 13.4 Real tool loop

```bash
python3 -m src.main agent \
  "List the current config keys, set review.mode to strict in local config, then read it back." \
  --cwd ./test_cases \
  --allow-write \
  --show-transcript
```

## 14. Account Runtime

### 14.1 CLI status and profile inspection

```bash
python3 -m src.main account-status --cwd ./test_cases
python3 -m src.main account-profiles --cwd ./test_cases
python3 -m src.main account-profiles --cwd ./test_cases --query local
```

### 14.2 Login and logout

```bash
python3 -m src.main account-login local --cwd ./test_cases
python3 -m src.main account-status --cwd ./test_cases
python3 -m src.main account-logout --cwd ./test_cases
```

### 14.3 Ephemeral account identity

```bash
python3 -m src.main account-login dev@example.com \
  --provider openai \
  --auth-mode api_key \
  --cwd ./test_cases
```

### 14.4 Slash commands

```bash
python3 -m src.main agent "/account" --cwd ./test_cases
python3 -m src.main agent "/account profiles" --cwd ./test_cases
python3 -m src.main agent "/account profile local" --cwd ./test_cases
python3 -m src.main agent "/login local" --cwd ./test_cases
python3 -m src.main agent "/logout" --cwd ./test_cases
```

### 14.5 Real tool loop

```bash
python3 -m src.main agent \
  "List the configured account profiles, activate the local profile, then report the active account session." \
  --cwd ./test_cases \
  --show-transcript
```

## 14B. LSP Runtime

### 14B.1 CLI status and code intelligence reports

```bash
python3 -m src.main lsp-status --cwd ./test_cases
python3 -m src.main lsp-symbols sample.py --cwd ./test_cases
python3 -m src.main lsp-workspace-symbols helper --cwd ./test_cases
python3 -m src.main lsp-definition sample.py 6 12 --cwd ./test_cases
python3 -m src.main lsp-references sample.py 6 12 --cwd ./test_cases
python3 -m src.main lsp-hover sample.py 1 5 --cwd ./test_cases
python3 -m src.main lsp-diagnostics --cwd ./test_cases
python3 -m src.main lsp-diagnostics --cwd ./test_cases --file-path broken.py
python3 -m src.main lsp-call-hierarchy sample.py 6 12 --cwd ./test_cases
python3 -m src.main lsp-incoming-calls sample.py 1 5 --cwd ./test_cases
python3 -m src.main lsp-outgoing-calls sample.py 6 12 --cwd ./test_cases
```

### 14B.2 Slash commands

```bash
python3 -m src.main agent "/lsp" --cwd ./test_cases
python3 -m src.main agent "/lsp symbols sample.py" --cwd ./test_cases
python3 -m src.main agent "/lsp workspace helper" --cwd ./test_cases
python3 -m src.main agent "/lsp definition sample.py 6 12" --cwd ./test_cases
python3 -m src.main agent "/lsp references sample.py 6 12" --cwd ./test_cases
python3 -m src.main agent "/lsp hover sample.py 1 5" --cwd ./test_cases
python3 -m src.main agent "/lsp diagnostics broken.py" --cwd ./test_cases
python3 -m src.main agent "/lsp hierarchy sample.py 6 12" --cwd ./test_cases
```

### 14B.3 Real tool loop

```bash
python3 -m src.main agent \
  "Use the LSP tool to find the definition of helper in sample.py, then summarize the result." \
  --cwd ./test_cases \
  --show-transcript
```

## 14A. Ask-user Runtime

### 14A.1 CLI status and history

```bash
python3 -m src.main ask-status --cwd ./test_cases
python3 -m src.main ask-history --cwd ./test_cases
```

### 14A.2 Slash commands

```bash
python3 -m src.main agent "/ask" --cwd ./test_cases
python3 -m src.main agent "/ask history" --cwd ./test_cases
```

### 14A.3 Real tool loop

```bash
python3 -m src.main agent \
  "Use ask_user_question to answer 'Approve deploy?' and then summarize the decision." \
  --cwd ./test_cases \
  --show-transcript
```

## 15. Search Runtime And Real Web Search

### 15.1 Provider status and activation

```bash
python3 -m src.main search-status --cwd ./test_cases
python3 -m src.main search-providers --cwd ./test_cases
python3 -m src.main search-providers --cwd ./test_cases --query local
python3 -m src.main search-status --cwd ./test_cases --provider local-search
python3 -m src.main search-activate local-search --cwd ./test_cases
```

### 15.2 Real search from the CLI

```bash
python3 -m src.main search \
  "python argparse mutually exclusive group" \
  --cwd ./test_cases \
  --provider local-search \
  --max-results 5

python3 -m src.main search \
  "OpenAI Responses API" \
  --cwd ./test_cases \
  --domain openai.com \
  --domain platform.openai.com
```

### 15.3 Slash commands

```bash
python3 -m src.main agent "/search" --cwd ./test_cases
python3 -m src.main agent "/search providers" --cwd ./test_cases
python3 -m src.main agent "/search provider local-search" --cwd ./test_cases
python3 -m src.main agent "/search use local-search" --cwd ./test_cases
python3 -m src.main agent "/search python unittest mock patch examples" --cwd ./test_cases
```

### 15.4 Real search through the model loop

```bash
python3 -m src.main agent \
  "Use web_search to find Python unittest mocking references, then summarize the top results." \
  --cwd ./test_cases \
  --show-transcript
```

## 16. Remote Runtime

### 16.1 CLI runtime modes

```bash
python3 -m src.main remote-mode staging --cwd ./test_cases
python3 -m src.main ssh-mode staging --cwd ./test_cases
python3 -m src.main teleport-mode tele --cwd ./test_cases
python3 -m src.main direct-connect-mode direct --cwd ./test_cases
python3 -m src.main deep-link-mode preview --cwd ./test_cases
```

### 16.2 Status and disconnect

```bash
python3 -m src.main remote-status --cwd ./test_cases
python3 -m src.main remote-profiles --cwd ./test_cases
python3 -m src.main remote-profiles --cwd ./test_cases --query stag
python3 -m src.main remote-disconnect --cwd ./test_cases
python3 -m src.main remote-status --cwd ./test_cases
```

### 16.3 Slash commands

```bash
python3 -m src.main agent "/remote" --cwd ./test_cases
python3 -m src.main agent "/remote staging" --cwd ./test_cases
python3 -m src.main agent "/remotes" --cwd ./test_cases
python3 -m src.main agent "/ssh staging" --cwd ./test_cases
python3 -m src.main agent "/teleport tele" --cwd ./test_cases
python3 -m src.main agent "/direct-connect direct" --cwd ./test_cases
python3 -m src.main agent "/deep-link preview" --cwd ./test_cases
python3 -m src.main agent "/disconnect" --cwd ./test_cases
```

### 16.4 Real tool loop

```bash
python3 -m src.main agent \
  "List the configured remote profiles, connect to staging, then report the active remote status." \
  --cwd ./test_cases \
  --show-transcript
```

## 17. MCP Runtime

### 17.1 Local resource inspection

```bash
python3 -m src.main mcp-status --cwd ./test_cases_mcp
python3 -m src.main mcp-resources --cwd ./test_cases_mcp
python3 -m src.main mcp-resources --cwd ./test_cases_mcp --query notes
python3 -m src.main mcp-resource mcp://workspace/notes --cwd ./test_cases_mcp
python3 -m src.main mcp-resource mcp://workspace/inline --cwd ./test_cases_mcp
```

### 17.2 Transport-backed MCP tools

```bash
python3 -m src.main mcp-tools --cwd ./test_cases_mcp
python3 -m src.main mcp-tools --cwd ./test_cases_mcp --query echo
python3 -m src.main mcp-tools --cwd ./test_cases_mcp --server remote
python3 -m src.main mcp-call-tool echo --arguments-json '{"text":"hello"}' --cwd ./test_cases_mcp
python3 -m src.main mcp-call-tool echo --arguments-json '{"text":"hello"}' --server remote --cwd ./test_cases_mcp
```

### 17.3 Slash commands

```bash
python3 -m src.main agent "/mcp" --cwd ./test_cases_mcp
python3 -m src.main agent "/mcp tools" --cwd ./test_cases_mcp
python3 -m src.main agent "/mcp tool echo" --cwd ./test_cases_mcp
python3 -m src.main agent "/resources" --cwd ./test_cases_mcp
python3 -m src.main agent "/resource mcp://remote/notes" --cwd ./test_cases_mcp
```

### 17.4 Real tool loop

```bash
python3 -m src.main agent \
  "List the available MCP tools, call the remote echo tool with text=hello, then summarize the result." \
  --cwd ./test_cases_mcp \
  --show-transcript
```

## 18. Task And Plan Runtime

### 18.1 Slash commands

```bash
python3 -m src.main agent "/tasks" --cwd ./test_cases_tasks
python3 -m src.main agent "/todo" --cwd ./test_cases_tasks
python3 -m src.main agent "/task missing-task-id" --cwd ./test_cases_tasks
python3 -m src.main agent "/task-next" --cwd ./test_cases_tasks
python3 -m src.main agent "/plan" --cwd ./test_cases_tasks
python3 -m src.main agent "/planner" --cwd ./test_cases_tasks
python3 -m src.main agent-context-raw --cwd ./test_cases_tasks
python3 -m src.main agent-prompt --cwd ./test_cases_tasks
```

## 18A. Team Runtime

### 18A.1 CLI status and inspection

```bash
python3 -m src.main team-status --cwd ./test_cases
python3 -m src.main team-list --cwd ./test_cases
python3 -m src.main team-get reviewers --cwd ./test_cases
python3 -m src.main team-messages --cwd ./test_cases
```

### 18A.2 Create and delete teams

```bash
python3 -m src.main team-create docs --member alice --member bob --cwd ./test_cases
python3 -m src.main team-list --cwd ./test_cases
python3 -m src.main team-delete docs --cwd ./test_cases
```

### 18A.3 Slash commands

```bash
python3 -m src.main agent "/teams" --cwd ./test_cases
python3 -m src.main agent "/team reviewers" --cwd ./test_cases
python3 -m src.main agent "/messages" --cwd ./test_cases
python3 -m src.main agent "/messages reviewers" --cwd ./test_cases
```

### 18A.4 Real tool loop

```bash
python3 -m src.main agent \
  "Create a local team called docs with members alice and bob, send a message to that team asking for notebook review, then show the team messages." \
  --cwd ./test_cases \
  --allow-write \
  --show-transcript
```

## 18B. Notebook Edit Tool

### 18B.1 Direct notebook edit through the agent loop

```bash
python3 -m src.main agent \
  "Use notebook_edit to update demo.ipynb cell 0 so it prints 2, then read back the notebook file and summarize the change." \
  --cwd ./test_cases_notebooks \
  --allow-write \
  --show-transcript
```

## 18C. Workflow Runtime

### 18C.1 Prepare a workflow manifest

```bash
cat > ./test_cases/.claw-workflows.json <<'EOF'
{
  "workflows": [
    {
      "name": "review",
      "description": "Review the current patch.",
      "steps": [
        {"title": "Inspect diff", "detail": "Read {path}"},
        {"title": "Summarize findings"}
      ],
      "prompt": "Review changes under {path}"
    }
  ]
}
EOF
```

### 18C.2 CLI inspection and run

```bash
python3 -m src.main workflow-list --cwd ./test_cases
python3 -m src.main workflow-get review --cwd ./test_cases
python3 -m src.main workflow-run review --arguments-json '{"path":"src/"}' --cwd ./test_cases
```

### 18C.3 Slash commands

```bash
python3 -m src.main agent "/workflows" --cwd ./test_cases
python3 -m src.main agent "/workflow review" --cwd ./test_cases
python3 -m src.main agent "/workflow run review" --cwd ./test_cases
```

## 18D. Remote Trigger Runtime

### 18D.1 Prepare a trigger manifest

```bash
cat > ./test_cases/.claw-triggers.json <<'EOF'
{
  "triggers": [
    {
      "trigger_id": "nightly",
      "name": "Nightly",
      "workflow": "review",
      "schedule": "0 0 * * *",
      "body": {"depth": "full"}
    }
  ]
}
EOF
```

### 18D.2 CLI inspection, create, update, and run

```bash
python3 -m src.main trigger-list --cwd ./test_cases
python3 -m src.main trigger-get nightly --cwd ./test_cases
python3 -m src.main trigger-create --body-json '{"trigger_id":"adhoc","name":"Adhoc","workflow":"review"}' --cwd ./test_cases
python3 -m src.main trigger-update adhoc --body-json '{"schedule":"manual"}' --cwd ./test_cases
python3 -m src.main trigger-run nightly --body-json '{"depth":"quick"}' --cwd ./test_cases
```

### 18D.3 Slash commands

```bash
python3 -m src.main agent "/triggers" --cwd ./test_cases
python3 -m src.main agent "/trigger nightly" --cwd ./test_cases
python3 -m src.main agent "/trigger run nightly" --cwd ./test_cases
```

## 18E. Worktree Runtime

### 18E.1 Prepare a git workspace

```bash
cd ./test_cases
git init
git config user.email test@example.com
git config user.name "Test User"
printf 'hello\n' > README.md
git add README.md
git commit -m "init"
cd ..
```

### 18E.2 CLI worktree flow

```bash
python3 -m src.main worktree-status --cwd ./test_cases
python3 -m src.main worktree-enter preview --cwd ./test_cases
python3 -m src.main worktree-status --cwd ./test_cases
python3 -m src.main worktree-exit --action keep --cwd ./test_cases
```

### 18E.3 Slash commands

```bash
python3 -m src.main agent "/worktree" --cwd ./test_cases
python3 -m src.main agent "/worktree enter preview" --cwd ./test_cases
python3 -m src.main agent "/worktree history" --cwd ./test_cases
python3 -m src.main agent "/worktree exit remove discard" --cwd ./test_cases
```

### 18E.4 Real agent cwd switch

```bash
python3 -m src.main agent \
  "Create a managed worktree called preview, then write note.txt in the current working directory and summarize where the file was created." \
  --cwd ./test_cases \
  --allow-write \
  --show-transcript
```

### 18.2 Create and inspect tasks

```bash
python3 -m src.main agent \
  "Create a task called Review runtime tasks, then list the current tasks." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript

cat ./test_cases_tasks/.port_sessions/task_runtime.json
```

### 18.3 Replace the todo list

```bash
python3 -m src.main agent \
  "Replace the current todo list with three tasks: inspect runtime, verify tests, and update docs. Mark inspect runtime as done and the others as todo." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript
```

### 18.4 Plan update and task sync

```bash
python3 -m src.main agent \
  "Use update_plan to create three steps: inspect runtime, verify tests, update docs. Mark inspect runtime completed and sync to tasks." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript

python3 -m src.main agent "/plan" --cwd ./test_cases_tasks
python3 -m src.main agent "/tasks" --cwd ./test_cases_tasks
cat ./test_cases_tasks/.port_sessions/plan_runtime.json
```

### 18.5 Dependency-aware task execution

```bash
python3 -m src.main agent \
  "Use todo_write to create two tasks: scan with status pending, and patch with status blocked and blocked_by scan. Then show the next actionable tasks." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript

python3 -m src.main agent \
  "Mark task scan as completed, then show the next actionable tasks and start task patch with active_form 'Patching files'." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript

python3 -m src.main agent \
  "Block task patch with reason waiting on review, then cancel task patch and summarize the final task state." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript
```

### 18.6 Task execution tools directly

```bash
python3 -m src.main agent \
  "Use todo_write to create task scan and task patch where patch is blocked_by scan. Then use task_next, task_complete for scan, task_start for patch, task_block for patch, and task_cancel for patch." \
  --cwd ./test_cases_tasks \
  --allow-write \
  --show-transcript
```

## 19. Plugin Runtime

### 19.1 Plugin prompt and context discovery

```bash
python3 -m src.main agent-prompt --cwd ./test_cases_plugins
python3 -m src.main agent-context-raw --cwd ./test_cases_plugins
```

### 19.2 Plugin alias tool

```bash
python3 -m src.main agent \
  "Use the plugin_read tool to read hello.txt and summarize it." \
  --cwd ./test_cases_plugins \
  --show-transcript
```

### 19.3 Plugin virtual tool

```bash
python3 -m src.main agent \
  "Use the demo_virtual tool with topic plugins and return the result." \
  --cwd ./test_cases_plugins \
  --show-transcript
```

### 19.4 Plugin before and after tool guidance

```bash
python3 -m src.main agent \
  "Read hello.txt and follow the plugin guidance around the read_file tool." \
  --cwd ./test_cases_plugins \
  --show-transcript
```

### 19.5 Plugin block behavior

```bash
python3 -m src.main agent \
  "Try to run bash and explain what the plugin blocked." \
  --cwd ./test_cases_plugins \
  --allow-shell \
  --show-transcript
```

### 19.6 Plugin lifecycle with resume and persist

```bash
python3 -m src.main agent \
  "Use the plugin system and create a saved session." \
  --cwd ./test_cases_plugins

python3 -m src.main agent-resume \
  <session-id> \
  "Continue and mention any plugin lifecycle guidance you received." \
  --cwd ./test_cases_plugins \
  --show-transcript
```

Look for:

- `plugin_before_persist`
- `Plugin resume hooks:`
- `Plugin runtime state:`

## 20. Delegation, Batching, And Query Engine Runtime

### 20.1 Basic delegated subtask

```bash
python3 -m src.main agent \
  "Delegate a subtask to inspect src/agent_runtime.py and return the summary." \
  --cwd . \
  --show-transcript
```

### 20.2 Multiple delegated subtasks

```bash
python3 -m src.main agent \
  "Delegate one subtask to scan the repository and another to summarize it after the scan." \
  --cwd . \
  --show-transcript
```

### 20.3 Resume a delegated child session

```bash
python3 -m src.main agent \
  "Inspect src/agent_tools.py and give a short summary." \
  --cwd .

python3 -m src.main agent \
  "Delegate a subtask that resumes session <session-id> and continues it." \
  --cwd . \
  --show-transcript
```

### 20.4 Topological dependency batches

```bash
python3 -m src.main agent \
  "Delegate two subtasks: one named scan, and one named summarize that depends on scan. Use topological batching and then return the final summary." \
  --cwd . \
  --show-transcript
```

Look for:

- `delegate_batch_result`
- `delegate_group_result`
- `batch_index=...`

### 20.5 Query-engine style helper commands

```bash
python3 -m src.main summary
python3 -m src.main manifest
python3 -m src.main route "inspect the runtime and tools" --limit 10
python3 -m src.main bootstrap "inspect the runtime and tools" --limit 10
python3 -m src.main turn-loop "inspect the runtime and tools" --limit 5 --max-turns 3
python3 -m src.main turn-loop "inspect the runtime and tools" --limit 5 --max-turns 3 --structured-output
```

## 21. Maintenance Rules

Use this every time a new feature lands:

```bash
python3 -m unittest discover -s tests -v
```

Then update:

- `PARITY_CHECKLIST.md`
- `TESTING_GUIDE.md`

Rule for future work:

- every new implemented feature should add a checked item in `PARITY_CHECKLIST.md`
- every user-testable feature should add at least one concrete command example in `TESTING_GUIDE.md`
