# Hex Tool System Reference

Complete reference for Hex's tool execution system and available tools.

## Table of Contents

- [Overview](#overview)
- [Tool Approval](#tool-approval)
- [Available Tools](#available-tools)
- [Read Tool](#read-tool)
- [Write Tool](#write-tool)
- [Bash Tool](#bash-tool)
- [Edit Tool](#edit-tool)
- [Grep Tool](#grep-tool)
- [Glob Tool](#glob-tool)
- [Phase 4: Extended Capabilities](#phase-4-extended-capabilities)
  - [AskUserQuestion Tool](#askuserquestion-tool)
  - [TodoWrite Tool](#todowrite-tool)
  - [WebFetch Tool](#webfetch-tool)
  - [WebSearch Tool](#websearch-tool)
  - [Task Tool](#task-tool)
  - [BashOutput Tool](#bashoutput-tool)
  - [KillShell Tool](#killshell-tool)
- [Safety Features](#safety-features)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Overview

Hex implements Claude's tool use capability, allowing Claude to:
- Read files from your filesystem
- Write or modify files
- Execute shell commands

All tool operations require explicit user approval for safety.

### How Tools Work

1. **Claude requests a tool** based on your conversation
2. **Hex intercepts the request** and shows you the details
3. **You approve or deny** the execution
4. **Tool executes** (if approved) and returns results
5. **Claude sees the results** and continues the conversation

### Tool Execution Flow

```
You: "Read config.yaml and explain it"
    │
    ▼
Claude: [Requests read_file tool]
    │
    ▼
Hex: ┌──────────────────────────────┐
      │ Tool Approval Required:       │
      │                              │
      │ Tool: read_file              │
      │ Path: /path/to/config.yaml   │
      │ Size: 1.2 KB                 │
      │                              │
      │ Approve? [y/N]               │
      └──────────────────────────────┘
    │
    ▼
You: y
    │
    ▼
Tool executes ──> Returns content
    │
    ▼
Claude: [Analyzes content and responds]
    │
    ▼
"This config file sets up..."
```

## Tool Approval

### Approval Prompt

When a tool requires approval, you'll see:

```
┌─────────────────────────────────────────┐
│ Tool Execution Request                  │
│                                         │
│ Tool: <tool_name>                       │
│ Parameters:                              │
│   param1: value1                        │
│   param2: value2                        │
│                                         │
│ Approve execution? [y/N]                │
└─────────────────────────────────────────┘
```

### Responding to Approval

**Approve**: Type `y` or `yes` and press Enter
**Deny**: Type `n`, `no`, or just press Enter

### When Approval Is Required

Different tools have different approval rules:

**Read Tool**:
- Always approved for normal files
- Requires approval for sensitive paths:
  - `/etc/*` (system config)
  - `/sys/*` (system internals)
  - `/proc/*` (process info)
  - `/dev/*` (device files)
  - `/boot/*` (boot files)
  - `/root/*` (root home)
  - `/var/log/*` (system logs)

**Write Tool**:
- All write operations require approval
- Create mode: Requires approval
- Overwrite mode: Requires approval (destructive)
- Append mode: Requires approval

**Bash Tool**:
- All bash commands require approval
- Dangerous commands flagged with extra warning (rm -rf, sudo, curl, etc.)
- Long-running commands (timeout > 60s): Requires approval

### Approval Security

**Hex never**:
- Executes tools without showing you details first
- Remembers approval decisions across sessions
- Runs dangerous operations silently

**You always**:
- See full tool parameters before execution
- Have final say on tool execution
- Can deny any operation

## Available Tools

### Summary

Hex provides 15 tools (13 core tools plus Skill and SlashCommand meta-tools) for file operations, code editing, search, and advanced capabilities:

| Tool | Purpose | Approval Rules | Timeout |
|------|---------|----------------|---------|
| `read_file` | Read file contents | Sensitive paths only | N/A |
| `write_file` | Create/modify files | Overwrites only | N/A |
| `bash` | Execute commands | Dangerous commands | 30s default, 5min max |
| `edit` | Replace strings in files | Always | N/A |
| `grep` | Search code with ripgrep | Never (read-only) | N/A |
| `glob` | Find files by pattern | Never (read-only) | N/A |
| `ask_user_question` | Interactive decision-making | Always | N/A |
| `todo_write` | Task list management | Never (display-only) | N/A |
| `web_fetch` | Fetch web content | Always | 30s |
| `web_search` | Search DuckDuckGo | Always | 30s |
| `task` | Launch sub-agents | Always | 5min default, 30min max |
| `bash_output` | Read background process output | Never (read-only) | N/A |
| `kill_shell` | Terminate background processes | Always | N/A |

## Read Tool

**Tool Name**: `read_file`

**Purpose**: Safely read file contents and return to Claude

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Absolute or relative path to file |

### Example Request

```json
{
  "tool": "read_file",
  "parameters": {
    "path": "/path/to/file.txt"
  }
}
```

### Safety Features

**Path Validation**:
- Resolves relative paths to absolute
- Prevents directory traversal (`../../../etc/passwd`)
- Checks file exists and is readable

**Size Limits**:
- Maximum file size: 1MB (configurable)
- Prevents memory exhaustion from huge files

**Content Validation**:
- UTF-8 encoding check
- Returns error for binary files

**Sensitive Path Detection**:
Requires approval for:
- `/etc/*` - System configuration
- `/sys/*` - System internals
- `/proc/*` - Process information
- `/dev/*` - Device files
- `/boot/*` - Boot files
- `/root/*` - Root home directory
- `/var/log/*` - System logs

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "file contents here...",
  "metadata": {
    "size": 1234,
    "path": "/absolute/path/to/file.txt"
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "file not found: /path/to/file.txt"
}
```

### Example Usage

**User**: "Read package.json and tell me what dependencies we use"

**Claude**: [Requests read_file with path: package.json]

**Hex**: Shows approval prompt

**User**: Approves

**Tool**: Returns package.json contents

**Claude**: "Based on package.json, you're using: React, Tailwind, TypeScript..."

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| File not found | Path doesn't exist | Check path spelling |
| Permission denied | No read access | Check file permissions |
| File too large | Size > 1MB | Read in chunks or use bash tool |
| Binary file | Non-UTF-8 content | Use bash tool with hexdump |

## Write Tool

**Tool Name**: `write_file`

**Purpose**: Create new files or modify existing files

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Path to write to |
| `content` | string | Yes | Content to write |
| `mode` | string | No | Operation mode (default: create) |

### Modes

**create** (default):
- Creates new file
- Fails if file already exists
- Requires approval

**overwrite**:
- Replaces existing file
- Creates file if doesn't exist
- Requires approval (destructive)

**append**:
- Adds to end of existing file
- Creates file if doesn't exist
- Requires approval

### Example Request

```json
{
  "tool": "write_file",
  "parameters": {
    "path": "/path/to/output.txt",
    "content": "Hello, world!",
    "mode": "create"
  }
}
```

### Safety Features

**Atomic Writes**:
- Writes to temp file first
- Moves to final location only on success
- Prevents partial writes on error

**Directory Creation**:
- Creates parent directories if needed
- Uses 0755 permissions

**Validation**:
- Checks write permissions
- Validates content encoding
- Returns detailed errors

**Confirmation for Overwrites**:
```
┌─────────────────────────────────────────┐
│ Write Tool: Overwrite Confirmation      │
│                                         │
│ File: /path/to/existing.txt             │
│ Current size: 1.5 KB                    │
│ New size: 2.3 KB                        │
│                                         │
│ This will REPLACE the existing file.    │
│ Approve? [y/N]                          │
└─────────────────────────────────────────┘
```

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "File written successfully",
  "metadata": {
    "path": "/absolute/path/to/file.txt",
    "size": 1234,
    "mode": "create"
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "file already exists (use mode=overwrite to replace)"
}
```

### Example Usage

**User**: "Create a README.md with a basic project description"

**Claude**: [Requests write_file with README.md content]

**Hex**: Requires approval (create mode)

**Tool**: Creates README.md

**Claude**: "I've created README.md with..."

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| File exists | Create mode, file exists | Use overwrite or append mode |
| Permission denied | No write access | Check directory permissions |
| Disk full | Out of space | Free up disk space |
| Invalid path | Bad file path | Check path syntax |

## Bash Tool

**Tool Name**: `bash`

**Purpose**: Execute shell commands and capture output

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `command` | string | Yes | Shell command to execute |
| `working_dir` | string | No | Working directory (default: current) |
| `timeout` | number | No | Timeout in seconds (default: 30, max: 300) |

### Example Request

```json
{
  "tool": "bash",
  "parameters": {
    "command": "ls -la",
    "working_dir": "/path/to/dir",
    "timeout": 10
  }
}
```

### Safety Features

**Sandboxing**:
- No interactive shells
- No shell variable expansion (unless needed)
- Controlled environment

**Timeout Protection**:
- Default: 30 seconds
- Maximum: 5 minutes (300 seconds)
- Prevents hung processes

**Dangerous Command Detection**:
Requires approval for:
- `rm -rf` (recursive delete)
- `sudo` (privilege escalation)
- `curl`, `wget` (network access)
- `dd` (low-level disk operations)
- `mkfs`, `fdisk` (disk formatting)
- `kill`, `pkill` (process termination)
- `chmod 777` (insecure permissions)
- `> /dev/sda` (disk writing)

**All commands require approval**, including read-only operations like:
- `ls`, `pwd`, `echo`, `cat`, `grep`
- `find`, `wc`, `head`, `tail`
- `git status`, `git log`, `git diff`

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "command output here...\n",
  "metadata": {
    "exit_code": 0,
    "duration_ms": 123,
    "command": "ls -la",
    "working_dir": "/path/to/dir"
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "command failed with exit code 1",
  "output": "stderr output here...",
  "metadata": {
    "exit_code": 1
  }
}
```

### Example Usage

**User**: "List all Go files in the current directory"

**Claude**: [Requests bash with command: find . -name "*.go"]

**Hex**: Requires approval

**Tool**: Executes and returns file list

**Claude**: "Found 12 Go files: main.go, client.go, ..."

### Timeout Handling

**Default timeout (30s)**:
```
Command: ls -la
Timeout: 30s (default)
Status: Requires approval
```

**Long timeout (requires approval)**:
```
┌─────────────────────────────────────────┐
│ Bash Tool: Long-Running Command         │
│                                         │
│ Command: npm install                    │
│ Timeout: 300s (5 minutes)               │
│                                         │
│ This may run for a while.               │
│ Approve? [y/N]                          │
└─────────────────────────────────────────┘
```

**Timeout exceeded**:
```json
{
  "success": false,
  "error": "command timeout after 30s",
  "output": "partial output before timeout...",
  "metadata": {
    "timeout": true,
    "duration_ms": 30000
  }
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Command not found | Binary not in PATH | Check command spelling, install if needed |
| Permission denied | No execute access | Check permissions or use sudo (with approval) |
| Timeout | Command too slow | Increase timeout or optimize command |
| Exit code != 0 | Command failed | Check stderr output for error details |

---

## Edit Tool

The Edit tool performs exact string replacements in files - Claude's primary method for making code changes.

### Purpose

- Replace exact strings in files
- Support single or multiple occurrences
- Preserve file encoding and formatting
- Ensure changes are intentional (not ambiguous)

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | string | ✅ | Path to file to edit (absolute or relative) |
| `old_string` | string | ✅ | Exact string to find and replace |
| `new_string` | string | ✅ | Replacement string (must differ from old_string) |
| `replace_all` | boolean | ❌ | Replace all occurrences (default: false, requires unique match) |

### Behavior

**Single Replacement (default)**:
- `old_string` must appear EXACTLY ONCE in the file
- Fails if not found or appears multiple times
- Forces Claude to be specific and unambiguous

**Replace All Mode**:
- Replaces ALL occurrences of `old_string`
- Useful for renaming variables, updating imports, etc.
- Use when intentional bulk replacement is needed

### Approval

**ALWAYS requires approval** - editing files is destructive.

### Examples

#### Basic Edit
```json
{
  "file_path": "src/config.go",
  "old_string": "MaxRetries = 3",
  "new_string": "MaxRetries = 5"
}
```

#### Multiline Edit
```json
{
  "file_path": "main.go",
  "old_string": "func old() {\n\treturn nil\n}",
  "new_string": "func updated() {\n\treturn errors.New(\"not implemented\")\n}"
}
```

#### Replace All
```json
{
  "file_path": "package.json",
  "old_string": "\"version\": \"1.0.0\"",
  "new_string": "\"version\": \"1.1.0\"",
  "replace_all": true
}
```

#### Variable Rename
```json
{
  "file_path": "app.js",
  "old_string": "oldVariableName",
  "new_string": "newVariableName",
  "replace_all": true
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| String not found | `old_string` doesn't exist | Verify exact string (including whitespace) |
| Ambiguous match | Multiple occurrences found | Use more context or set `replace_all: true` |
| Identical strings | `old_string` == `new_string` | Must actually change something |
| File not found | Path doesn't exist | Check file path |
| Permission denied | No write access | Check file permissions |

### Safety Notes

- Edit preserves exact indentation from `old_string`
- Supports Unicode characters
- Respects line endings (LF/CRLF)
- No regex - exact literal matching only
- Changes are atomic (write succeeds or fails completely)

### Common Patterns

**Fix typo**:
```json
{
  "file_path": "README.md",
  "old_string": "recieve",
  "new_string": "receive"
}
```

**Update import**:
```json
{
  "file_path": "main.go",
  "old_string": "import \"old/package\"",
  "new_string": "import \"new/package\"",
  "replace_all": true
}
```

**Change function signature**:
```json
{
  "file_path": "api.go",
  "old_string": "func Process(data string) error {",
  "new_string": "func Process(ctx context.Context, data string) error {"
}
```

---

## Grep Tool

The Grep tool searches code using ripgrep - fast, powerful code search.

### Purpose

- Search code with regex patterns
- Filter by file type or glob pattern
- View context around matches
- Count occurrences

### Requirements

- **ripgrep must be installed**: `brew install ripgrep` (macOS) or `apt install ripgrep` (Linux)

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pattern` | string | ✅ | Regex pattern to search for |
| `path` | string | ❌ | Directory to search (default: current directory) |
| `output_mode` | string | ❌ | Output format: `content`, `files_with_matches`, `count` (default: `files_with_matches`) |
| `glob` | string | ❌ | Filter files by glob pattern (e.g., `*.go`) |
| `type` | string | ❌ | Filter by file type (e.g., `go`, `js`, `py`) |
| `-i` | boolean | ❌ | Case insensitive search |
| `-A` | number | ❌ | Lines of context after match (content mode only) |
| `-B` | number | ❌ | Lines of context before match (content mode only) |
| `-C` | number | ❌ | Lines of context around match (content mode only) |

### Output Modes

**`files_with_matches` (default)**:
- Shows only file paths containing matches
- Fast overview of where pattern appears
- Best for "where is X used?"

**`content`**:
- Shows matching lines with line numbers
- Supports context lines (`-A`, `-B`, `-C`)
- Best for seeing actual usage

**`count`**:
- Shows match count per file
- Best for statistics and coverage

### Approval

**Does NOT require approval** - grep is read-only.

### Examples

#### Find Function Definitions
```json
{
  "pattern": "func.*Test",
  "path": "internal/",
  "type": "go",
  "output_mode": "files_with_matches"
}
```

#### Search with Context
```json
{
  "pattern": "TODO",
  "glob": "*.go",
  "output_mode": "content",
  "-B": 2,
  "-A": 2
}
```

#### Case-Insensitive Search
```json
{
  "pattern": "error",
  "-i": true,
  "output_mode": "count"
}
```

#### Filter by File Type
```json
{
  "pattern": "import.*react",
  "type": "js",
  "output_mode": "files_with_matches"
}
```

#### Complex Regex
```json
{
  "pattern": "func \\w+\\(.*context\\.Context",
  "type": "go",
  "output_mode": "content"
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| ripgrep not installed | Binary not found | Install: `brew install ripgrep` |
| Invalid regex | Pattern syntax error | Check regex syntax |
| Path not found | Directory doesn't exist | Verify path |
| No matches | Pattern not found | Success with empty output |

### Output Format Examples

**files_with_matches**:
```
src/main.go
src/config.go
test/main_test.go
```

**content** (with line numbers):
```
src/main.go:15:func main() {
src/main.go:23:	return nil
src/config.go:8:const MaxRetries = 3
```

**count**:
```
src/main.go:5
src/config.go:2
test/main_test.go:8
```

### Common Patterns

**Find all TODOs**:
```json
{
  "pattern": "TODO|FIXME|HACK",
  "output_mode": "content",
  "-C": 1
}
```

**Find error handling**:
```json
{
  "pattern": "if err != nil",
  "type": "go",
  "output_mode": "count"
}
```

**Find API endpoints**:
```json
{
  "pattern": "router\\.(GET|POST|PUT|DELETE)",
  "type": "go",
  "output_mode": "content"
}
```

---

## Glob Tool

The Glob tool finds files by pattern matching - Claude's way to discover files.

### Purpose

- Find files by glob patterns
- Support recursive matching (`**`)
- Support brace expansion (`*.{ts,tsx}`)
- Sorted by modification time (newest first)

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pattern` | string | ✅ | Glob pattern (e.g., `*.go`, `**/*.test.js`) |
| `path` | string | ❌ | Directory to search (default: current directory) |

### Pattern Syntax

**Simple patterns**:
- `*.go` - All .go files in directory
- `test_*.py` - Files starting with test_
- `*.{js,ts}` - Files ending with .js OR .ts

**Recursive patterns**:
- `**/*.go` - All .go files in any subdirectory
- `src/**/*.tsx` - All .tsx files under src/
- `**/test/*.js` - All .js files in any test/ directory

**Brace expansion**:
- `*.{ts,tsx}` expands to `*.ts` and `*.tsx`
- `{foo,bar}/*.go` expands to `foo/*.go` and `bar/*.go`

### Approval

**Does NOT require approval** - glob is read-only.

### Examples

#### Find All Go Files
```json
{
  "pattern": "*.go",
  "path": "internal/"
}
```

#### Recursive Test Files
```json
{
  "pattern": "**/*_test.go"
}
```

#### Multiple Extensions
```json
{
  "pattern": "*.{ts,tsx}",
  "path": "src/components"
}
```

#### Specific Directory Pattern
```json
{
  "pattern": "src/**/*.test.js"
}
```

#### Find Config Files
```json
{
  "pattern": "**/{config,settings}.{json,yaml,yml}"
}
```

### Output Format

Results are sorted by modification time (newest first):

```
src/components/Button.tsx
src/components/Input.tsx
src/App.tsx
src/index.tsx
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Invalid pattern | Syntax error | Check glob syntax |
| Path not found | Directory doesn't exist | Verify path |
| No matches | Pattern matched nothing | Success with empty output |

### Common Patterns

**Find all source files**:
```json
{
  "pattern": "**/*.{go,js,ts,py}"
}
```

**Find test files**:
```json
{
  "pattern": "**/*{_test.go,.test.js,.spec.ts}"
}
```

**Find config files**:
```json
{
  "pattern": "**/*.{json,yaml,yml,toml}"
}
```

**Find modified components**:
```json
{
  "pattern": "src/components/**/*.tsx"
}
```

### Comparison with Grep

Use **Glob** when you need to:
- Find files by name/extension
- Get newest files first
- Work with file paths (not content)

Use **Grep** when you need to:
- Search file contents
- Use regex patterns
- See actual code context

---

## Phase 4: Extended Capabilities

Phase 4 adds 7 new tools that extend Hex's capabilities into interactive workflows, task management, web research, and advanced process control.

### Tool Categories

**Phase 4A: Interactive Tools**
- `ask_user_question` - Gather user input through multiple-choice questions
- `todo_write` - Create and manage structured task lists

**Phase 4B: Research Tools**
- `web_fetch` - Fetch and process web content
- `web_search` - Search the web via DuckDuckGo

**Phase 4C: Advanced Execution**
- `task` - Launch sub-agents for complex tasks
- `bash_output` - Monitor background process output
- `kill_shell` - Terminate background processes

---

## AskUserQuestion Tool

**Tool Name**: `ask_user_question`

**Purpose**: Prompt users with 1-4 multiple-choice questions to gather information or clarify ambiguity. Supports both single-select and multi-select questions with 2-4 options each. Users always have the option to provide custom "Other: ..." answers.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `questions` | array | Yes | Array of 1-4 question objects |
| `answers` | object | Yes | Map of header to answer (filled by UI) |

### Question Object Structure

Each question in the `questions` array must have:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `question` | string | Yes | The complete question text (e.g., "Which library should we use?") |
| `header` | string | Yes | Short label (max 12 chars) used as answer key (e.g., "Library") |
| `options` | array | Yes | Array of 2-4 option objects |
| `multiSelect` | boolean | Yes | If true, user can select multiple options |

### Option Object Structure

Each option must have:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `label` | string | Yes | Display text (1-5 words) shown to user |
| `description` | string | Yes | Explanation of what this option means |

### Approval Rules

**ALWAYS requires approval** - this tool is inherently interactive and waits for user input.

### Examples

#### Single Question, Single Select
```json
{
  "questions": [
    {
      "question": "Which testing framework should we use?",
      "header": "Framework",
      "multiSelect": false,
      "options": [
        {
          "label": "Jest",
          "description": "Popular, batteries-included testing framework with built-in mocking"
        },
        {
          "label": "Vitest",
          "description": "Fast Vite-native testing with Jest-compatible API"
        },
        {
          "label": "Mocha",
          "description": "Flexible framework requiring separate assertion and mocking libraries"
        }
      ]
    }
  ]
}
```

#### Multiple Questions with Multi-Select
```json
{
  "questions": [
    {
      "question": "Which API method should we implement first?",
      "header": "API Method",
      "multiSelect": false,
      "options": [
        {
          "label": "GET /users",
          "description": "List all users with pagination"
        },
        {
          "label": "POST /users",
          "description": "Create a new user"
        }
      ]
    },
    {
      "question": "Which features do you want to enable?",
      "header": "Features",
      "multiSelect": true,
      "options": [
        {
          "label": "Authentication",
          "description": "JWT-based user authentication"
        },
        {
          "label": "Rate limiting",
          "description": "Per-IP request rate limiting"
        },
        {
          "label": "Caching",
          "description": "Redis-based response caching"
        }
      ]
    }
  ]
}
```

#### Technology Selection
```json
{
  "questions": [
    {
      "question": "Which database should we use for this project?",
      "header": "Database",
      "multiSelect": false,
      "options": [
        {
          "label": "PostgreSQL",
          "description": "Robust relational database with JSON support"
        },
        {
          "label": "MongoDB",
          "description": "Document database for flexible schemas"
        },
        {
          "label": "SQLite",
          "description": "Lightweight embedded database"
        }
      ]
    }
  ]
}
```

#### Architecture Decision
```json
{
  "questions": [
    {
      "question": "How should we structure the API routes?",
      "header": "Structure",
      "multiSelect": false,
      "options": [
        {
          "label": "RESTful",
          "description": "Traditional REST endpoints (/api/v1/resource/:id)"
        },
        {
          "label": "GraphQL",
          "description": "Single endpoint with flexible queries"
        }
      ]
    },
    {
      "question": "Which deployment platforms are we targeting?",
      "header": "Platforms",
      "multiSelect": true,
      "options": [
        {
          "label": "AWS",
          "description": "Amazon Web Services (EC2, Lambda, etc.)"
        },
        {
          "label": "Vercel",
          "description": "Serverless platform optimized for Next.js"
        },
        {
          "label": "Docker",
          "description": "Containerized deployment anywhere"
        }
      ]
    }
  ]
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Missing questions parameter | No questions provided | Include questions array |
| Empty questions array | Zero questions provided | Provide at least 1 question |
| Too many questions | More than 4 questions | Split into multiple tool calls |
| Invalid question structure | Missing required fields | Check question/header/options |
| Invalid option count | Not 2-4 options | Provide 2-4 options per question |
| Missing answer | User didn't answer a question | All questions require answers |
| Invalid answer | Answer not in options | Answer must match option label or "Other: ..." |

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "User responses:\n\nWhich testing framework should we use?: Jest\nWhich features do you want to enable?: Authentication, Rate limiting"
}
```

**Failure**:
```json
{
  "success": false,
  "error": "question 1 must have 2-4 options"
}
```

### Common Patterns

**Clarify ambiguity**:
Use when user request could be interpreted multiple ways
```json
{
  "question": "What did you mean by 'optimize'?",
  "header": "Optimization",
  "multiSelect": false,
  "options": [
    {"label": "Performance", "description": "Reduce execution time and memory usage"},
    {"label": "Code quality", "description": "Improve readability and maintainability"}
  ]
}
```

**Technology selection**:
Get user preference for libraries/frameworks
```json
{
  "question": "Which state management library?",
  "header": "State Mgmt",
  "multiSelect": false,
  "options": [
    {"label": "Redux", "description": "Predictable state container with middleware"},
    {"label": "MobX", "description": "Reactive state management with observables"},
    {"label": "Zustand", "description": "Minimal state management with hooks"}
  ]
}
```

**Feature prioritization**:
Determine implementation order
```json
{
  "question": "Which features are most important? (select multiple)",
  "header": "Priorities",
  "multiSelect": true,
  "options": [
    {"label": "User auth", "description": "Login and registration system"},
    {"label": "Search", "description": "Full-text search functionality"},
    {"label": "Export", "description": "Export data to CSV/JSON"}
  ]
}
```

### Safety Notes

- Headers must be unique within a single tool call
- Option labels must be unique within a single question
- "Other: ..." answers are always allowed automatically
- User can select multiple options only when multiSelect is true
- All questions must be answered (no partial responses)

---

## TodoWrite Tool

**Tool Name**: `todo_write`

**Purpose**: Create and manage structured task lists for tracking progress during complex operations. Displays formatted todo items with status indicators and provides progress metrics. This tool is display-only and does not persist tasks.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `todos` | array | Yes | Array of todo item objects |

### Todo Item Structure

Each todo item must have:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | string | Yes | Imperative form: "Run tests", "Build project" |
| `activeForm` | string | Yes | Present continuous: "Running tests", "Building project" |
| `status` | string | Yes | One of: `pending`, `in_progress`, `completed` |

### Status Icons

| Status | Icon | Display Text | Meaning |
|--------|------|--------------|---------|
| `pending` | ☐ | Uses `content` | Task not yet started |
| `in_progress` | ⏳ | Uses `activeForm` | Currently working on this task |
| `completed` | ✅ | Uses `content` | Task finished successfully |

### Approval Rules

**Does NOT require approval** - this is a read-only display tool that doesn't modify state.

### Examples

#### Basic Task List
```json
{
  "todos": [
    {
      "content": "Install dependencies",
      "activeForm": "Installing dependencies",
      "status": "completed"
    },
    {
      "content": "Run tests",
      "activeForm": "Running tests",
      "status": "in_progress"
    },
    {
      "content": "Build project",
      "activeForm": "Building project",
      "status": "pending"
    }
  ]
}
```

Output:
```
✅ Install dependencies
⏳ Running tests
☐ Build project
```

#### Multi-Phase Feature Implementation
```json
{
  "todos": [
    {
      "content": "Design API schema",
      "activeForm": "Designing API schema",
      "status": "completed"
    },
    {
      "content": "Implement database models",
      "activeForm": "Implementing database models",
      "status": "completed"
    },
    {
      "content": "Create API endpoints",
      "activeForm": "Creating API endpoints",
      "status": "in_progress"
    },
    {
      "content": "Write integration tests",
      "activeForm": "Writing integration tests",
      "status": "pending"
    },
    {
      "content": "Update API documentation",
      "activeForm": "Updating API documentation",
      "status": "pending"
    }
  ]
}
```

#### Bug Fix Workflow
```json
{
  "todos": [
    {
      "content": "Reproduce the bug",
      "activeForm": "Reproducing the bug",
      "status": "completed"
    },
    {
      "content": "Write failing test case",
      "activeForm": "Writing failing test case",
      "status": "completed"
    },
    {
      "content": "Identify root cause",
      "activeForm": "Identifying root cause",
      "status": "in_progress"
    },
    {
      "content": "Implement fix",
      "activeForm": "Implementing fix",
      "status": "pending"
    },
    {
      "content": "Verify all tests pass",
      "activeForm": "Verifying all tests pass",
      "status": "pending"
    }
  ]
}
```

#### Code Review Checklist
```json
{
  "todos": [
    {
      "content": "Check code formatting",
      "activeForm": "Checking code formatting",
      "status": "completed"
    },
    {
      "content": "Verify test coverage",
      "activeForm": "Verifying test coverage",
      "status": "completed"
    },
    {
      "content": "Review error handling",
      "activeForm": "Reviewing error handling",
      "status": "in_progress"
    },
    {
      "content": "Check documentation",
      "activeForm": "Checking documentation",
      "status": "pending"
    }
  ]
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Missing todos parameter | No todos array provided | Include todos array |
| Empty todos array | Array has no items | Add at least one todo item |
| Missing content field | Todo missing content | Add content to all todos |
| Missing activeForm field | Todo missing activeForm | Add activeForm to all todos |
| Missing status field | Todo missing status | Add status to all todos |
| Empty content | Content is empty string | Provide non-empty content |
| Empty activeForm | activeForm is empty string | Provide non-empty activeForm |
| Invalid status | Status not pending/in_progress/completed | Use valid status value |
| Wrong parameter type | todos is not an array | Use array for todos |
| Invalid todo structure | Todo is not an object | Each todo must be object |

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "✅ Install dependencies\n⏳ Running tests\n☐ Build project",
  "metadata": {
    "total_count": 3,
    "pending_count": 1,
    "in_progress_count": 1,
    "completed_count": 1
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "todo at index 2: status must be one of: pending, in_progress, completed"
}
```

### Common Patterns

**Track multi-step operations**:
```json
{
  "todos": [
    {"content": "Analyze requirements", "activeForm": "Analyzing requirements", "status": "completed"},
    {"content": "Design solution", "activeForm": "Designing solution", "status": "in_progress"},
    {"content": "Implement solution", "activeForm": "Implementing solution", "status": "pending"},
    {"content": "Test solution", "activeForm": "Testing solution", "status": "pending"}
  ]
}
```

**Update progress incrementally**:
Start with all pending, update as work progresses:
```json
// Initial state
{"todos": [
  {"content": "Step 1", "activeForm": "Doing step 1", "status": "pending"},
  {"content": "Step 2", "activeForm": "Doing step 2", "status": "pending"}
]}

// After starting step 1
{"todos": [
  {"content": "Step 1", "activeForm": "Doing step 1", "status": "in_progress"},
  {"content": "Step 2", "activeForm": "Doing step 2", "status": "pending"}
]}

// After completing step 1
{"todos": [
  {"content": "Step 1", "activeForm": "Doing step 1", "status": "completed"},
  {"content": "Step 2", "activeForm": "Doing step 2", "status": "in_progress"}
]}
```

**Complex project tracking**:
```json
{
  "todos": [
    {"content": "Set up project structure", "activeForm": "Setting up project structure", "status": "completed"},
    {"content": "Configure build system", "activeForm": "Configuring build system", "status": "completed"},
    {"content": "Implement core functionality", "activeForm": "Implementing core functionality", "status": "in_progress"},
    {"content": "Add error handling", "activeForm": "Adding error handling", "status": "pending"},
    {"content": "Write unit tests", "activeForm": "Writing unit tests", "status": "pending"},
    {"content": "Write integration tests", "activeForm": "Writing integration tests", "status": "pending"},
    {"content": "Update documentation", "activeForm": "Updating documentation", "status": "pending"}
  ]
}
```

### Safety Notes

- Tool output is ephemeral - it's displayed but not persisted
- Exactly ONE task should be in_progress at a time
- Use content field for static description, activeForm for action in progress
- Status transitions should go: pending → in_progress → completed
- Never mark task completed if it failed - add error handling todo instead

---

## WebFetch Tool

**Tool Name**: `web_fetch`

**Purpose**: Fetch content from a URL via HTTP GET and return it (optionally converted to markdown). Supports HTML-to-markdown conversion for web pages and has a 30-second timeout. This tool makes network requests and must respect user privacy.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Full URL to fetch (must include http:// or https://) |
| `prompt` | string | Yes | Description of what you're looking for (used for logging) |

### Approval Rules

**ALWAYS requires approval** - makes network requests that:
- Send data from user's IP address
- May cost bandwidth
- Could access sensitive internal URLs
- May be logged by remote servers

### Examples

#### Fetch Documentation Page
```json
{
  "url": "https://docs.example.com/api/overview",
  "prompt": "Get API overview documentation"
}
```

#### Check API Status
```json
{
  "url": "https://status.example.com/api/v1/status.json",
  "prompt": "Check current API status"
}
```

#### Read Blog Post
```json
{
  "url": "https://blog.example.com/new-feature-announcement",
  "prompt": "Read announcement about new features"
}
```

#### Fetch Package Info
```json
{
  "url": "https://registry.npmjs.org/express/latest",
  "prompt": "Get latest Express.js version information"
}
```

#### Download Configuration Template
```json
{
  "url": "https://raw.githubusercontent.com/user/repo/main/config.template.json",
  "prompt": "Download configuration template from GitHub"
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Invalid url | Missing or malformed URL | Provide full URL with scheme |
| Missing scheme | URL lacks http:// or https:// | Add http:// or https:// prefix |
| Connection failed | Network unreachable or DNS failure | Check internet connection and URL |
| HTTP error: 404 | Page not found | Verify URL is correct |
| HTTP error: 403 | Access forbidden | URL may require authentication |
| HTTP error: 500 | Server error | Try again later or contact site admin |
| Timeout | Request took longer than 30s | Server is slow or unreachable |
| Context cancelled | User or system cancelled request | Retry if needed |
| Conversion failed | HTML-to-markdown error | Content might be malformed |

### Return Value

**Success (HTML converted to markdown)**:
```json
{
  "success": true,
  "output": "# Page Title\n\nContent in markdown format...\n\n## Section\n\nMore content..."
}
```

**Success (non-HTML content)**:
```json
{
  "success": true,
  "output": "{\"status\": \"ok\", \"version\": \"1.2.3\"}"
}
```

**Failure**:
```json
{
  "success": false,
  "error": "http error: 404 Not Found"
}
```

### Content Type Handling

The tool automatically detects content type and processes accordingly:

**HTML content** (`text/html`, `application/xhtml+xml`):
- Converted to markdown
- Preserves headings, links, lists, code blocks
- Removes most HTML formatting
- Returns clean, readable markdown

**Other content types**:
- Returned as-is
- JSON: raw JSON string
- Plain text: raw text
- XML: raw XML string

### Common Patterns

**Check API documentation**:
```json
{
  "url": "https://api.example.com/docs",
  "prompt": "Fetch API documentation to understand endpoints"
}
```

**Get release notes**:
```json
{
  "url": "https://github.com/owner/repo/releases/latest",
  "prompt": "Read latest release notes"
}
```

**Fetch data file**:
```json
{
  "url": "https://example.com/data/config.json",
  "prompt": "Download configuration data"
}
```

**Research library usage**:
```json
{
  "url": "https://docs.library.com/getting-started",
  "prompt": "Learn how to get started with this library"
}
```

### Safety Notes

- Always prompts user before making request
- Respects context cancellation
- 30-second timeout prevents hanging
- User-Agent is set to "Hex/1.0"
- No cookies or authentication headers sent
- Redirects are followed automatically
- HTTPS is supported (certificates validated)
- Does NOT execute JavaScript (static content only)

---

## WebSearch Tool

**Tool Name**: `web_search`

**Purpose**: Search the web using DuckDuckGo and return formatted results. Supports result limiting and domain filtering (allowed/blocked lists). Returns results as formatted markdown with title, URL, and snippet for each result.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query (e.g., "golang best practices") |
| `limit` | number | No | Maximum results to return (default: 10) |
| `allowed_domains` | array | No | Only include results from these domains |
| `blocked_domains` | array | No | Exclude results from these domains |

### Approval Rules

**ALWAYS requires approval** - makes network requests to DuckDuckGo from user's IP address.

### Examples

#### Basic Search
```json
{
  "query": "golang error handling patterns",
  "limit": 5
}
```

#### Search Specific Domains
```json
{
  "query": "react hooks tutorial",
  "allowed_domains": ["reactjs.org", "react.dev"],
  "limit": 10
}
```

#### Search with Blocked Domains
```json
{
  "query": "typescript generics",
  "blocked_domains": ["stackoverflow.com"],
  "limit": 8
}
```

#### Research Latest News
```json
{
  "query": "claude 3.5 sonnet release features",
  "limit": 5
}
```

#### Find Official Documentation
```json
{
  "query": "fastapi documentation",
  "allowed_domains": ["fastapi.tiangolo.com"],
  "limit": 3
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Query required | Missing or empty query | Provide non-empty query string |
| Invalid limit | Limit is not a number or is <= 0 | Use positive number for limit |
| Search failed | Network error or DuckDuckGo unavailable | Check internet connection, retry |
| HTTP error | Non-200 status from DuckDuckGo | Service might be down, try again later |
| Parse error | Failed to parse HTML results | DuckDuckGo might have changed format |
| No results | Query matched nothing | Try different search terms |

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "# Search Results for: golang best practices\n\nFound 5 results:\n\n### 1. Effective Go\n**URL**: https://golang.org/doc/effective_go\n\nA guide to writing clear, idiomatic Go code...\n\n---\n\n### 2. Go Code Review Comments\n**URL**: https://github.com/golang/go/wiki/CodeReviewComments\n\nCommon mistakes and best practices...\n\n---\n\n..."
}
```

**Failure**:
```json
{
  "success": false,
  "error": "query parameter is required and must be a non-empty string"
}
```

### Output Format

Results are formatted as markdown:

```markdown
# Search Results for: <query>

Found N results:

### 1. <Title>
**URL**: <url>

<snippet>

---

### 2. <Title>
**URL**: <url>

<snippet>

---
```

### Domain Filtering

**Allowed domains** (whitelist):
```json
{
  "query": "python asyncio tutorial",
  "allowed_domains": ["python.org", "realpython.com"]
}
```
Only includes results from python.org or realpython.com.

**Blocked domains** (blacklist):
```json
{
  "query": "javascript promises",
  "blocked_domains": ["w3schools.com"]
}
```
Excludes any results from w3schools.com.

**Combined filtering**:
```json
{
  "query": "machine learning",
  "allowed_domains": ["arxiv.org", "papers.nips.cc"],
  "blocked_domains": ["arxiv.org/abs/old-paper"]
}
```
Includes arxiv.org and papers.nips.cc, but blocked domains take precedence.

### Common Patterns

**Find official documentation**:
```json
{
  "query": "postgresql json functions",
  "allowed_domains": ["postgresql.org"],
  "limit": 5
}
```

**Research best practices**:
```json
{
  "query": "kubernetes deployment strategies",
  "limit": 10
}
```

**Find recent articles**:
```json
{
  "query": "rust async await 2024",
  "limit": 8
}
```

**Avoid low-quality sources**:
```json
{
  "query": "python tutorial",
  "blocked_domains": ["w3schools.com", "tutorialspoint.com"],
  "limit": 10
}
```

**Academic research**:
```json
{
  "query": "transformer architecture attention mechanism",
  "allowed_domains": ["arxiv.org", "papers.nips.cc", "proceedings.mlr.press"],
  "limit": 15
}
```

### Safety Notes

- User-Agent set to "Mozilla/5.0 (compatible; Hex/1.0)"
- Uses DuckDuckGo's HTML interface (no JavaScript required)
- No cookies or tracking
- Results are parsed from HTML (may break if DuckDuckGo changes format)
- Domain filtering is case-insensitive
- Respects context cancellation
- Returns empty results if nothing found (not an error)

---

## Task Tool

**Tool Name**: `task`

**Purpose**: Launch a sub-agent (Hex subprocess) to handle complex, multi-step tasks autonomously. Sub-agents inherit environment variables (API keys) and run in the same working directory. Useful for delegating independent work that requires multiple tool calls or complex reasoning.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | Task description/instruction for sub-agent |
| `description` | string | Yes | Human-readable description of what task does |
| `subagent_type` | string | Yes | Type of sub-agent (used for logging/tracking) |
| `model` | string | No | Model to use (e.g., "claude-3-5-sonnet-20241022") |
| `resume` | string | No | Conversation ID to resume from |
| `timeout` | number | No | Timeout in seconds (default: 300, max: 1800) |

### Approval Rules

**ALWAYS requires approval** because sub-agents:
- Spawn new processes (resource usage)
- Use API calls (costs money)
- Can perform arbitrary actions through tool use
- May run for extended periods

### Examples

#### Delegate Code Review
```json
{
  "prompt": "Review the authentication module in src/auth/ and suggest improvements",
  "description": "Code review of authentication module",
  "subagent_type": "code_reviewer"
}
```

#### Research Task
```json
{
  "prompt": "Research the top 3 JavaScript testing frameworks and create a comparison table",
  "description": "Research testing frameworks",
  "subagent_type": "researcher",
  "timeout": 600
}
```

#### Complex Implementation
```json
{
  "prompt": "Implement a rate limiting middleware for the Express.js API with Redis backend",
  "description": "Implement rate limiting",
  "subagent_type": "implementer",
  "model": "claude-3-5-sonnet-20241022"
}
```

#### Bug Investigation
```json
{
  "prompt": "Investigate why the login endpoint is returning 500 errors. Check logs, database, and recent code changes.",
  "description": "Debug login endpoint errors",
  "subagent_type": "debugger",
  "timeout": 900
}
```

#### Documentation Generation
```json
{
  "prompt": "Generate API documentation for all endpoints in src/routes/ in OpenAPI 3.0 format",
  "description": "Generate API documentation",
  "subagent_type": "documenter"
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Missing prompt | No prompt provided | Include prompt parameter |
| Missing description | No description provided | Include description parameter |
| Missing subagent_type | No subagent type provided | Include subagent_type parameter |
| Invalid prompt | Prompt is not a string | Use string for prompt |
| Invalid model | Model is not a string | Use string for model name |
| Invalid resume | Resume ID is not a string | Use string for resume ID |
| Hex binary not found | Hex not in PATH and can't build | Install hex or ensure go.mod exists |
| Build failed | Failed to build hex from source | Check Go toolchain and go.mod |
| Task timeout | Exceeded timeout limit | Increase timeout or simplify task |
| Task cancelled | Context cancelled by user/system | Normal cancellation |
| Exit code != 0 | Sub-agent encountered error | Check output for error details |
| Execution failed | Command not found or other exec error | Verify hex is executable |

### Return Value

**Success**:
```json
{
  "success": true,
  "output": "Sub-agent output here...\n\nCompleted authentication module review.\nSuggestions:\n1. Add rate limiting...\n2. Use bcrypt for passwords...",
  "metadata": {
    "exit_code": 0,
    "duration": 45.2,
    "prompt": "Review the authentication module...",
    "description": "Code review of authentication module",
    "subagent_type": "code_reviewer"
  }
}
```

**Failure (timeout)**:
```json
{
  "success": false,
  "error": "task timed out after 5m0s",
  "metadata": {
    "timeout": 300,
    "duration": 300.1,
    "prompt": "...",
    "description": "...",
    "subagent_type": "..."
  }
}
```

**Failure (non-zero exit)**:
```json
{
  "success": false,
  "output": "Error: API key not configured\n",
  "error": "sub-agent exited with code 1",
  "metadata": {
    "exit_code": 1,
    "duration": 2.3,
    "prompt": "...",
    "description": "...",
    "subagent_type": "..."
  }
}
```

### Timeouts

**Default timeout**: 5 minutes (300 seconds)
**Maximum timeout**: 30 minutes (1800 seconds)

Timeout is enforced at the OS process level - sub-agent will be killed if it exceeds limit.

### Sub-Agent Execution

The tool:
1. Finds hex binary (in PATH or builds from source)
2. Executes: `hex [--model MODEL] [--resume ID] --print "PROMPT"`
3. Inherits environment (ANTHROPIC_API_KEY, etc.)
4. Runs in current working directory
5. Captures stdout and stderr
6. Returns combined output

### Common Patterns

**Parallel research**:
Spawn multiple sub-agents for independent research:
```json
// Agent 1
{"prompt": "Research PostgreSQL JSON performance", "description": "PostgreSQL research", "subagent_type": "researcher"}

// Agent 2
{"prompt": "Research MongoDB query performance", "description": "MongoDB research", "subagent_type": "researcher"}
```

**Complex multi-step task**:
Delegate tasks that require many tool calls:
```json
{
  "prompt": "1. Search codebase for TODO comments\n2. Group by file\n3. Create GitHub issues for each TODO\n4. Update code to reference issue numbers",
  "description": "Convert TODOs to GitHub issues",
  "subagent_type": "task_automator",
  "timeout": 1200
}
```

**Resume long conversation**:
Continue work from previous session:
```json
{
  "prompt": "Continue implementing the OAuth2 flow",
  "description": "Resume OAuth implementation",
  "subagent_type": "implementer",
  "resume": "conv_abc123xyz"
}
```

**Use specific model**:
Select model for task requirements:
```json
{
  "prompt": "Analyze this large codebase and identify architectural issues",
  "description": "Architecture analysis",
  "subagent_type": "analyzer",
  "model": "claude-3-5-sonnet-20241022"
}
```

### Safety Notes

- Sub-agent inherits full environment (API keys, credentials)
- Sub-agent can use ALL tools available to parent
- No automatic approval - sub-agent will prompt user for tool approvals
- Output is captured but may be very large (no size limit)
- Process is killed on timeout (may leave partial work)
- Exit code 0 = success, non-zero = failure
- Sub-agent shares same working directory
- Binary auto-build requires Go toolchain and go.mod

---

## BashOutput Tool

**Tool Name**: `bash_output`

**Purpose**: Retrieve output from background bash processes started with the bash tool. Returns only new output since last read (incremental). Supports optional regex filtering to extract specific lines. This is a read-only tool for monitoring long-running processes.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `bash_id` | string | Yes | ID of background bash process |
| `filter` | string | No | Regex pattern to filter output lines |

### Approval Rules

**Does NOT require approval** - this is a read-only monitoring tool that doesn't modify state.

### Examples

#### Basic Output Retrieval
```json
{
  "bash_id": "bash_abc123"
}
```

#### Filter for Errors Only
```json
{
  "bash_id": "bash_abc123",
  "filter": "ERROR|FATAL|WARN"
}
```

#### Monitor Test Results
```json
{
  "bash_id": "bash_test_runner",
  "filter": "PASS|FAIL|✓|✗"
}
```

#### Watch Build Progress
```json
{
  "bash_id": "bash_build_prod",
  "filter": "\\[\\d+%\\]|Building|Compiling"
}
```

#### Extract Specific Metrics
```json
{
  "bash_id": "bash_benchmark",
  "filter": "\\d+\\.\\d+ ops/sec|took \\d+ms"
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Missing bash_id | No bash_id provided | Include bash_id parameter |
| Process not found | bash_id doesn't exist | Check process ID, may have been cleaned up |
| Invalid regex | Filter regex syntax error | Fix regex pattern |

### Return Value

**Success (with new output)**:
```json
{
  "success": true,
  "output": "STDOUT:\nLine 1\nLine 2\n\nSTDERR:\nWarning: something",
  "metadata": {
    "bash_id": "bash_abc123",
    "command": "npm run build",
    "done": false,
    "stdout_lines": 2,
    "stderr_lines": 1
  }
}
```

**Success (no new output)**:
```json
{
  "success": true,
  "output": "(no new output)",
  "metadata": {
    "bash_id": "bash_abc123",
    "command": "npm run build",
    "done": false,
    "stdout_lines": 0,
    "stderr_lines": 0
  }
}
```

**Success (process finished)**:
```json
{
  "success": true,
  "output": "STDOUT:\nBuild complete!",
  "metadata": {
    "bash_id": "bash_abc123",
    "command": "npm run build",
    "done": true,
    "exit_code": 0,
    "stdout_lines": 1,
    "stderr_lines": 0
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "background process 'bash_xyz' not found"
}
```

### Output Format

Output is formatted with clear sections:

```
STDOUT:
stdout line 1
stdout line 2

STDERR:
stderr line 1
```

If only stdout or stderr has content, only that section is shown.

### Incremental Reading

The tool tracks read position per process:
- First call: returns all output so far
- Second call: returns only new output since first call
- Third call: returns only new output since second call
- Etc.

This prevents seeing the same output multiple times.

### Regex Filtering

When filter is provided:
- Applied to BOTH stdout and stderr
- Only matching lines are returned
- Non-matching lines are DISCARDED (can't be retrieved later)
- Use carefully - filtered lines are lost forever

**Filter examples**:
- `ERROR` - lines containing "ERROR"
- `^\\[INFO\\]` - lines starting with "[INFO]"
- `\\d{4}-\\d{2}-\\d{2}` - lines with dates (YYYY-MM-DD)
- `PASS|FAIL` - lines containing "PASS" or "FAIL"

### Common Patterns

**Poll for completion**:
```json
// Check periodically until done
{
  "bash_id": "bash_deploy"
}

// When metadata.done is true, process finished
```

**Monitor errors during build**:
```json
{
  "bash_id": "bash_npm_install",
  "filter": "ERR!|WARN|deprecated"
}
```

**Extract test results**:
```json
{
  "bash_id": "bash_pytest",
  "filter": "PASSED|FAILED|ERROR|\\d+ passed"
}
```

**Watch server startup**:
```json
{
  "bash_id": "bash_server",
  "filter": "listening|started|ready|error"
}
```

**Debug specific module**:
```json
{
  "bash_id": "bash_app",
  "filter": "\\[auth\\]|authentication"
}
```

### Safety Notes

- Read-only operation (no approval needed)
- Incremental reading is automatic (tracks position)
- Filtered lines are permanently discarded
- Process must exist in background registry
- Returns metadata about process state (done, exit_code)
- Thread-safe (multiple readers won't corrupt state)
- Empty reads are normal (process hasn't produced more output)

---

## KillShell Tool

**Tool Name**: `kill_shell`

**Purpose**: Terminate a running background bash process. Attempts graceful shutdown (SIGTERM) first, then falls back to force-kill (SIGKILL) if needed. Cleans up the background process registry.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `shell_id` | string | Yes | ID of background bash process to kill |

### Approval Rules

**ALWAYS requires approval** - killing processes is destructive and may:
- Interrupt important work
- Leave partial state
- Lose unsaved data
- Affect dependent processes

### Examples

#### Kill Long-Running Build
```json
{
  "shell_id": "bash_build_123"
}
```

#### Stop Server Process
```json
{
  "shell_id": "bash_dev_server"
}
```

#### Terminate Hung Test
```json
{
  "shell_id": "bash_test_runner"
}
```

#### Clean Up Failed Job
```json
{
  "shell_id": "bash_migration_xyz"
}
```

### Error Handling

| Error | Reason | Solution |
|-------|--------|----------|
| Missing shell_id | No shell_id provided | Include shell_id parameter |
| Shell not found | shell_id doesn't exist in registry | Process may have already terminated |
| Invalid shell_id | shell_id is not a string | Use string for shell_id |

### Return Value

**Success (process killed)**:
```json
{
  "success": true,
  "output": "Successfully killed shell bash_build_123",
  "metadata": {
    "shell_id": "bash_build_123"
  }
}
```

**Success (already terminated)**:
```json
{
  "success": true,
  "output": "Shell bash_build_123 was already terminated. Cleaned up registry.",
  "metadata": {
    "shell_id": "bash_build_123"
  }
}
```

**Failure**:
```json
{
  "success": false,
  "error": "shell 'bash_xyz' not found"
}
```

### Kill Process

The tool performs a two-stage kill:

1. **SIGTERM** (graceful shutdown):
   - Allows process to clean up
   - Wait 100ms for termination

2. **Check if alive**:
   - Send signal 0 (non-destructive check)

3. **SIGKILL** (force kill) if still alive:
   - Immediate termination
   - No cleanup possible
   - Wait 50ms

4. **Registry cleanup**:
   - Remove from background process registry
   - Free resources

### Common Patterns

**Stop runaway process**:
```json
{
  "shell_id": "bash_infinite_loop"
}
```

**Cancel long operation**:
```json
// Started: npm install (taking too long)
{
  "shell_id": "bash_npm_install"
}
```

**Clean up after error**:
```json
// Server failed to start but process still running
{
  "shell_id": "bash_server_start"
}
```

**Terminate test suite**:
```json
// Tests hanging, need to kill
{
  "shell_id": "bash_integration_tests"
}
```

**Stop background watcher**:
```json
// File watcher no longer needed
{
  "shell_id": "bash_file_watcher"
}
```

### Safety Notes

- Requires approval (destructive operation)
- Graceful shutdown attempted first (SIGTERM)
- Force kill used if needed (SIGKILL)
- Registry is always cleaned up
- Safe to call on already-dead processes
- Cannot kill processes not started by Hex
- Works only on processes in background registry
- No output capture after kill signal

### Related Tools

**Start background process**: Use `bash` tool with background flag
**Monitor process**: Use `bash_output` tool
**Kill process**: Use `kill_shell` tool

### Workflow Example

```
1. Start process in background
   bash(command="npm run dev", run_in_background=true)
   → Returns: bash_id "bash_abc123"

2. Monitor output
   bash_output(bash_id="bash_abc123")
   → Returns: incremental output

3. Decide to terminate
   kill_shell(shell_id="bash_abc123")
   → Process killed, registry cleaned
```

---

## MCP (Model Context Protocol) Tools

**Overview**: MCP integration allows Hex to use external tools from MCP servers, dramatically extending capabilities beyond built-in tools.

### What is MCP?

MCP (Model Context Protocol) is an open standard that enables AI assistants to securely connect to external data sources and tools. MCP servers can provide:

- File system operations
- Database queries
- Web scraping and API access
- Custom business logic
- Cloud service integrations
- And much more

### Why Use MCP?

**Extensibility**: Add new capabilities without modifying Hex's source code

**Ecosystem**: Use community-built servers from the MCP marketplace

**Customization**: Build your own MCP servers for domain-specific needs

**Standardization**: MCP is an open protocol supported across multiple AI tools

### Configuration File (.mcp.json)

MCP servers are configured in `.mcp.json` in your project root:

```json
{
  "version": "1.0",
  "servers": {
    "filesystem": {
      "name": "filesystem",
      "transport": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"]
    },
    "fetch": {
      "name": "fetch",
      "transport": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

### CLI Commands

#### hex mcp add

Add a new MCP server configuration:

```bash
# Basic syntax
hex mcp add <name> <command> [args...]

# Examples
hex mcp add weather node weather-server.js
hex mcp add database python -m database_server --port 8080
hex mcp add files npx -y @modelcontextprotocol/server-filesystem /data
```

**Parameters**:
- `name`: Unique identifier for the server
- `command`: Executable to launch the server
- `args`: Command-line arguments (optional)

The server configuration is saved to `.mcp.json` in the current directory.

#### hex mcp list

List all configured MCP servers:

```bash
hex mcp list
```

**Output**:
```
Configured MCP servers:

  filesystem
    Transport: stdio
    Command:   npx -y @modelcontextprotocol/server-filesystem /data

  fetch
    Transport: stdio
    Command:   npx -y @modelcontextprotocol/server-fetch

Total: 2 server(s)
Config: /path/to/project/.mcp.json
```

#### hex mcp remove

Remove an MCP server configuration:

```bash
hex mcp remove <name>

# Example
hex mcp remove weather
```

This removes the server from `.mcp.json` but doesn't affect the server binary or scripts.

### Using MCP Tools in Conversations

Once configured, MCP tools are automatically available in conversations:

**Example workflow**:

1. **Configure server**:
   ```bash
   hex mcp add filesystem npx -y @modelcontextprotocol/server-filesystem ~/Documents
   ```

2. **Start Hex**:
   ```bash
   hex
   ```

3. **MCP tools load automatically** at startup

4. **Use tools naturally**:
   ```
   You: "List all markdown files in my Documents directory"

   Claude: [Uses filesystem MCP tool to list files]

   "I found 23 markdown files:
   - notes.md
   - project-plan.md
   - ..."
   ```

### Tool Naming Convention

MCP tools are prefixed with their server name to avoid collisions:

```
Built-in tool:    read_file
MCP tool:         filesystem_read_file
                  ^^^^^^^^^ server name prefix
```

This ensures clarity about which tools come from which sources.

### Example: Filesystem Server

**Setup**:
```bash
# Install the official filesystem server
npm install -g @modelcontextprotocol/server-filesystem

# Configure it
hex mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /path/to/dir
```

**Available tools**:
- `filesystem_read_file` - Read file contents
- `filesystem_write_file` - Write file contents
- `filesystem_list_directory` - List directory contents
- `filesystem_create_directory` - Create directories
- `filesystem_move_file` - Move/rename files

**Usage**:
```
You: "Read the contents of config.json in the project directory"

Claude: [Uses filesystem_read_file tool]

"The config.json file contains:
{
  'database': 'postgres',
  'port': 5432,
  ..."
```

### Example: Fetch Server

**Setup**:
```bash
hex mcp add fetch npx -y @modelcontextprotocol/server-fetch
```

**Available tools**:
- `fetch_fetch` - Fetch content from URLs
- `fetch_post` - HTTP POST requests
- `fetch_get_json` - Fetch and parse JSON

**Usage**:
```
You: "Fetch the latest release info from https://api.github.com/repos/anthropics/anthropic-sdk-python/releases/latest"

Claude: [Uses fetch_fetch tool]

"The latest release is v0.18.1, released on 2024-03-15..."
```

### Troubleshooting

#### Server Not Starting

**Symptom**: Tools not appearing, connection errors

**Solutions**:
- Verify command is correct: `hex mcp list`
- Test command manually: `npx -y @modelcontextprotocol/server-filesystem /path`
- Check server is installed: `npm list -g @modelcontextprotocol/server-filesystem`
- Review server logs (stderr output)

#### Tools Not Appearing

**Symptom**: Hex starts but MCP tools aren't available

**Solutions**:
- Verify `.mcp.json` exists in project directory
- Check JSON syntax: `cat .mcp.json | jq`
- Ensure server supports `tools/list` method
- Check Hex output for initialization errors

#### Permission Errors

**Symptom**: "Permission denied" when MCP tool executes

**Solutions**:
- For filesystem server: verify allowed directory is accessible
- Check file/directory permissions
- Ensure server user has required access
- Use absolute paths in server configuration

#### Protocol Version Mismatch

**Symptom**: "Unsupported protocol version" error

**Solutions**:
- Update MCP server to latest version
- Check server documentation for supported MCP versions
- Verify server implements MCP correctly

### Writing Custom MCP Servers

You can create custom MCP servers for your specific needs:

**Basic structure** (Node.js example):
```javascript
// my-server.js
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-custom-server",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {}
  }
});

// Define a tool
server.setRequestHandler("tools/list", async () => ({
  tools: [{
    name: "my_tool",
    description: "Does something useful",
    inputSchema: {
      type: "object",
      properties: {
        param: { type: "string", description: "A parameter" }
      },
      required: ["param"]
    }
  }]
}));

// Handle tool execution
server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "my_tool") {
    return {
      content: [{
        type: "text",
        text: `Result for: ${request.params.arguments.param}`
      }]
    };
  }
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

**Add to Hex**:
```bash
hex mcp add custom node my-server.js
```

**See [MCP_INTEGRATION.md](MCP_INTEGRATION.md) for detailed server development guide.**

### Security Considerations

**MCP tools run with your user permissions**:
- Filesystem server: can read/write files in allowed directories
- Fetch server: makes network requests from your IP
- Database server: accesses databases with your credentials

**Best practices**:
1. **Review server code** before trusting it
2. **Use allowlists** for filesystem and network access
3. **Limit server scope** to specific directories/APIs
4. **Monitor tool usage** in Hex conversations
5. **Remove unused servers** to reduce attack surface

### Official MCP Servers

Anthropic provides several official MCP servers:

**@modelcontextprotocol/server-filesystem**
- File and directory operations
- Safe by default (requires allowed directory list)

**@modelcontextprotocol/server-fetch**
- HTTP GET/POST requests
- JSON parsing and response handling

**@modelcontextprotocol/server-sqlite**
- SQLite database queries
- Read and write operations

**@modelcontextprotocol/server-postgres**
- PostgreSQL database access
- Schema inspection and queries

Find more at: https://github.com/modelcontextprotocol

### Advanced Configuration

**Environment variables in server commands**:
```json
{
  "servers": {
    "api": {
      "name": "api",
      "transport": "stdio",
      "command": "node",
      "args": ["api-server.js"],
      "env": {
        "API_KEY": "${API_KEY}",
        "DEBUG": "true"
      }
    }
  }
}
```

**Note**: Environment variable support is planned for a future release.

### See Also

- **[MCP_INTEGRATION.md](MCP_INTEGRATION.md)** - Architecture and server development
- **[MCP Specification](https://spec.modelcontextprotocol.io/)** - Official protocol docs
- **[examples/mcp/](../examples/mcp/)** - Example configurations and use cases

---

## Safety Features

### Overall Security Model

**Principle**: User has full control, always

**Implementation**:
1. **Explicit approval** for dangerous operations
2. **Detailed prompts** showing exactly what will happen
3. **No persistence** of approval decisions
4. **Atomic operations** where possible (write tool)
5. **Timeouts** to prevent hung processes
6. **Validation** before execution

### Permission Levels

**Auto-approved** (safe operations):
- Reading normal files (non-sensitive paths)

**Requires approval** (most operations):
- Reading sensitive files (/etc, /sys, /proc, /dev, /boot, /root, /var/log)
- All write operations (create, overwrite, append)
- All bash commands
- Long-running commands (>60s timeout)

**Never allowed** (blocked):
- None currently (user can approve anything)
- Future: Could add blocklist for extremely dangerous ops

### Audit Trail

**Current**:
- Tool requests logged to console
- Approval/denial visible in UI
- Results saved to conversation history

**Future** (v0.3.0+):
- Tool execution log file
- Approval history
- Replay protection

## Examples

### Example 1: Code Review

**User**: "Review main.go and suggest improvements"

**Flow**:
1. Claude requests `read_file(main.go)`
2. User approves
3. Claude reads code
4. Claude analyzes and provides feedback
5. User: "Apply those changes"
6. Claude requests `write_file(main.go, improved_code, overwrite)`
7. User approves overwrite
8. File updated

### Example 2: Project Setup

**User**: "Set up a new Go project with basic structure"

**Flow**:
1. Claude requests `bash(mkdir -p cmd/app internal pkg)`
2. User approves
3. Claude requests `write_file(cmd/app/main.go, boilerplate_code, create)`
4. User approves
5. Claude requests `write_file(go.mod, module_config, create)`
6. User approves
7. Structure created

### Example 3: Log Analysis

**User**: "Check the error logs and summarize issues"

**Flow**:
1. Claude requests `bash(tail -100 /var/log/app.log)`
2. Approval required (/var/log is sensitive)
3. User approves
4. Claude reads logs
5. Claude requests `bash(grep ERROR /var/log/app.log | wc -l)`
6. User approves
7. Claude summarizes findings

### Example 4: Bulk File Operations

**User**: "Find all TODOs in Go files and list them"

**Flow**:
1. Claude requests `bash(find . -name "*.go" -exec grep -Hn TODO {} \;)`
2. User approves
3. Returns list of TODOs
4. Claude formats and presents results

### Example 5: Configuration Update

**User**: "Add a new database connection to config.yaml"

**Flow**:
1. Claude requests `read_file(config.yaml)`
2. User approves
3. Claude reads current config
4. Claude generates updated config
5. Claude requests `write_file(config.yaml, updated_config, overwrite)`
6. Approval required (overwrite)
7. User approves
8. Config updated

## Troubleshooting

### Tool Not Available

**Symptom**: "Tool not found: <tool_name>"

**Cause**: Tool not registered

**Solution**: Check tool name spelling, verify Hex version supports tool

### Permission Denied

**Symptom**: "Permission denied" in tool result

**Cause**: Insufficient filesystem or execution permissions

**Solution**:
- Check file/directory permissions
- For bash: verify command is in PATH
- For write: check directory is writable

### Timeout Issues

**Symptom**: "Command timeout after Xs"

**Cause**: Command takes longer than timeout

**Solution**:
- For bash: increase timeout parameter
- Optimize command (e.g., limit grep search scope)
- Break into smaller operations

### Large File Issues

**Symptom**: "File too large" or "Out of memory"

**Cause**: File exceeds 1MB limit

**Solution**:
- Use bash tool with `head -n 100 largefile.txt`
- Process file in chunks
- Use specialized tools (grep, awk) via bash

### Approval Not Working

**Symptom**: Tool denied even after typing "y"

**Cause**: Typo in approval response

**Solution**:
- Type exactly `y` or `yes`
- Check for extra spaces
- Press Enter after typing

### Binary File Errors

**Symptom**: "Invalid UTF-8 encoding"

**Cause**: Trying to read binary file with read_file

**Solution**:
- Use bash tool with `hexdump` or `xxd`
- Use `file` command to check file type first
- Use appropriate binary tools

---

## Advanced Topics

### Tool Composition

Claude can chain multiple tools:

```
User: "Find all Python files, read each one, and create a summary document"

Flow:
1. bash: find . -name "*.py"
2. read_file: file1.py
3. read_file: file2.py
4. ...
5. write_file: SUMMARY.md (with aggregated analysis)
```

### Custom Tool Timeout

Adjust timeout for long-running operations:

```
User: "Run the test suite (it takes 2 minutes)"

Claude: bash(
  command: "go test ./...",
  timeout: 150  # 2.5 minutes
)
```

### Working Directory Control

Execute commands in specific directories:

```
Claude: bash(
  command: "git status",
  working_dir: "/path/to/repo"
)
```

---

**See Also**:
- [USER_GUIDE.md](USER_GUIDE.md) - General usage guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - Tool system architecture
- [CHANGELOG.md](../CHANGELOG.md) - Version history
