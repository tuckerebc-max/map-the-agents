# Gemini Code

A powerful AI coding assistant for your terminal, powered by Gemini 2.5 Pro with support for other LLM models.
More information [here](https://blossom-tarsier-434.notion.site/Gemini-Code-1c6c13716ff180db86a0c7f4b2da13ab?pvs=4)

## Features

- Interactive chat sessions in your terminal
- Multiple model support (Gemini 2.5 Pro, Gemini 1.5 Pro, and more)
- Basic history management (prevents excessive length)
- Markdown rendering in the terminal
- Automatic tool usage by the assistant:
  - File operations (view, edit, list, grep, glob)
  - Directory operations (ls, tree, create_directory)
  - System commands (bash)
  - Quality checks (linting, formatting)
  - Test running capabilities (pytest, etc.)

## Installation

### Method 1: Install from PyPI (Recommended)

```bash
# Install directly from PyPI
pip install gemini-code
```

### Method 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/raizamartin/gemini-code.git
cd gemini-code

# Install the package
pip install -e .
```

## Setup

Before using Gemini CLI, you need to set up your API keys:

```bash
# Set up Google API key for Gemini models
gemini setup YOUR_GOOGLE_API_KEY
```

## Usage

```bash
# Start an interactive session with the default model
gemini

# Start a session with a specific model
gemini --model models/gemini-2.5-pro-exp-03-25

# Set default model
gemini set-default-model models/gemini-2.5-pro-exp-03-25

# List all available models
gemini list-models
```

## Interactive Commands

During an interactive session, you can use these commands:

- `/exit` - Exit the chat session
- `/help` - Display help information

## How It Works

### Tool Usage

Unlike direct command-line tools, the Gemini CLI's tools are used automatically by the assistant to help answer your questions. For example:

1. You ask: "What files are in the current directory?"
2. The assistant uses the `ls` tool behind the scenes
3. The assistant provides you with a formatted response

This approach makes the interaction more natural and similar to how Claude Code works.

## Development

This project is under active development. More models and features will be added soon!

### Recent Changes in v0.1.69

- Added test_runner tool to execute automated tests (e.g., pytest)
- Fixed syntax issues in the tool definitions
- Improved error handling in tool execution
- Updated status displays during tool execution with more informative messages
- Added additional utility tools (directory_tools, quality_tools, task_complete_tool, summarizer_tool)

### Recent Changes in v0.1.21

- Implemented native Gemini function calling for much more reliable tool usage
- Rewritten the tool execution system to use Gemini's built-in function calling capability
- Enhanced the edit tool to better handle file creation and content updating
- Updated system prompt to encourage function calls instead of text-based tool usage
- Fixed issues with Gemini not actively creating or modifying files
- Simplified the BaseTool interface to support both legacy and function call modes

### Recent Changes in v0.1.20

- Fixed error with Flask version check in example code
- Improved error handling in system prompt example code

### Recent Changes in v0.1.19

- Improved system prompt to encourage more active tool usage
- Added thinking/planning phase to help Gemini reason about solutions
- Enhanced response format to prioritize creating and modifying files over printing code
- Filtered out thinking stages from final output to keep responses clean
- Made Gemini more proactive as a coding partner, not just an advisor

### Recent Changes in v0.1.18

- Updated default model to Gemini 2.5 Pro Experimental (models/gemini-2.5-pro-exp-03-25)
- Updated system prompts to reference Gemini 2.5 Pro
- Improved model usage and documentation

### Recent Changes in v0.1.17

- Added `list-models` command to show all available Gemini models
- Improved error handling for models that don't exist or require permission
- Added model initialization test to verify model availability
- Updated help documentation with new commands

### Recent Changes in v0.1.16

- Fixed file creation issues: The CLI now properly handles creating files with content
- Enhanced tool pattern matching: Added support for more formats that Gemini might use
- Improved edit tool handling: Better handling of missing arguments when creating files
- Added special case for natural language edit commands (e.g., "edit filename with content: ...")

### Recent Changes in v0.1.15

- Fixed tool execution issues: The CLI now properly processes tool calls and executes Bash commands correctly
- Fixed argument parsing for Bash tool: Commands are now passed as a single argument to avoid parsing issues
- Improved error handling in tools: Better handling of failures and timeouts
- Updated model name throughout the codebase to use `gemini-1.5-pro` consistently

### Known Issues

- If you created a config file with earlier versions, you may need to delete it to get the correct defaults:
  ```bash
  rm -rf ~/.config/gemini-code
  ```

## License

MIT
