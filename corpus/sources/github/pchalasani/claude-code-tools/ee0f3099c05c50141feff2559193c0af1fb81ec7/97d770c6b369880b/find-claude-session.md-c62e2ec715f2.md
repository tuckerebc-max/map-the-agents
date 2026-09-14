# find-claude-session Documentation

## Overview

`find-claude-session` is a command-line utility that searches through Claude Code session files to find sessions containing specific keywords. It provides an interactive UI for session selection and automatic resumption.

## Features

- **Interactive UI**: Rich terminal interface showing session previews
- **Global Search**: Search across all Claude projects with `-g/--global` flag
- **Smart Selection**: Automatically resume sessions with `claude -r`
- **Cross-project Navigation**: Switch to different project directories when needed
- **Shell Integration**: Persistent directory changes with the `fcs` wrapper function

## Usage

### Basic Command
```bash
find-claude-session "keyword1,keyword2,keyword3"
```
- Accepts comma-separated keywords as a single argument
- Searches for sessions containing ALL keywords (AND operation)
- Case-insensitive matching

### Global Search
```bash
find-claude-session "keywords" --global
find-claude-session "keywords" -g
```

### Shell Function (Recommended)
```bash
# Add to .bashrc/.zshrc
fcs() { eval "$(find-claude-session --shell "$@" | sed '/^$/d')"; }

# Usage
fcs "keywords"         # Local search
fcs "keywords" -g      # Global search
```

## How It Works

1. **Directory Mapping**:
   - Current directory: `/Users/username/projects/myapp`
   - Maps to: `~/.claude/projects/-Users-username-projects-myapp/`
   - Rule: Replace all `/` with `-` in the path

2. **Search Process**:
   - Reads JSONL files line by line (memory efficient)
   - Checks if ALL keywords exist in the session
   - Sorts by modification time (newest first)
   - Displays top 10 matches in interactive UI

3. **Session Selection**:
   - Shows session ID, project name, date, and preview
   - Enter a number (1-10) to select
   - Automatically runs `claude -r SESSION_ID`
   - For cross-project sessions, changes directory first

## Installation

### Via uv tool
```bash
uv tool install git+https://github.com/username/claude-code-tools
```

### For Development
```bash
git clone https://github.com/username/claude-code-tools
cd claude-code-tools
make install  # Installs in editable mode
```

## Technical Details

### File Format
Claude Code stores sessions as JSONL files:
- Each line is a separate JSON object
- Contains messages, timestamps, and metadata
- Located in `~/.claude/projects/PROJECT_PATH/`

### Dependencies
- Python 3.11+
- click (CLI framework)
- rich (optional, for interactive UI)

### Performance
- Memory efficient: streams files line by line
- Early exit when all keywords found
- Parallel search in global mode
- Progress indicator for large searches

## Advanced Features

### Progress Indicators
- Shows search progress in global mode
- Displays number of projects searched
- Real-time match counter

### Fallback Mode
If `rich` library is not available:
- Falls back to simple text interface
- Still fully functional
- Plain numbered list for selection

### Cross-project Sessions
When selecting a session from a different project:
1. Prompts to change directory
2. Changes to project directory
3. Resumes the session
4. With `fcs` wrapper, directory change persists

## Examples

```bash
# Find sessions about a specific error
fcs "TypeError,undefined,function"

# Find sessions about a feature across all projects
fcs "authentication,JWT,middleware" -g

# Find sessions with specific library discussions
fcs "langroid,MCP,sampling"

# Direct usage without shell function
find-claude-session "docker,compose" --global
```

## Tips and Tricks

1. **Keyword Selection**: Use specific, unique terms for better results
2. **Multiple Keywords**: More keywords = more precise matches
3. **Global Search**: Use `-g` when you can't remember which project
4. **Shell Function**: Always use `fcs` for better workflow
5. **Recent Sessions**: Results are sorted by modification time

## Troubleshooting

### No Claude directory found
- Ensure you're in a directory with Claude Code history
- Check if `~/.claude/projects/` exists

### No matches found
- Try fewer or more general keywords
- Use global search (`-g`) to search all projects

### Directory changes don't persist
- Make sure you're using the `fcs` shell function
- Check that the function is properly sourced in your shell config