[![Crates.io](https://img.shields.io/crates/v/oli-server?style=flat-square)](https://crates.io/crates/oli-server)
[![Docs.rs](https://img.shields.io/badge/docs.rs-latest-blue?style=flat-square)](https://docs.rs/oli-server)
[![License](https://img.shields.io/badge/license-Apache_2.0-blue?style=flat-square)](https://opensource.org/license/apache-2-0)
[![Codecov](https://img.shields.io/codecov/c/github/amrit110/oli?style=flat-square)](https://codecov.io/github/amrit110/oli)
[![Rust](https://img.shields.io/badge/built%20with-Rust-orange.svg?logo=rust&style=flat-square)](https://www.rust-lang.org)

# oli - Open Local Intelligent assistant

![oli_demo](https://github.com/user-attachments/assets/bf7e8bf1-cdac-4256-886a-e1780f779f65)

---

oli is an open-source alternative to Claude Code with powerful agentic capabilities for coding assistance. Features:

- A modern hybrid architecture:
  - Rust backend for performance and core functionality
  - React/Ink frontend for a beautiful, interactive terminal UI
- Support for both cloud APIs (Anthropic Claude Sonnet 3.7, OpenAI GPT4o and Google Gemini) and local LLMs (via Ollama)
- Strong agentic capabilities including file search, edit, and command execution
- Tool use support across all model providers (Anthropic, OpenAI, Google and Ollama)

⚠️ This project is in a very early stage and is prone to bugs and issues! Please post your issues as you encounter them.

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/amrit110/oli
cd oli

# Build both backend and frontend
./build.sh

# Run the hybrid application
./run.sh
```

## Environment Setup

### Development Setup

The development environment can be set up using
[uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). Hence, make sure it is
installed and then run:


```bash
uv sync --dev
source .venv/bin/activate
```

# Run linting and formatting

```bash
pre-commit run --all-files
```

### Cloud API Models

For API-based features, set up your environment variables:

```bash
# Create a .env file in the project root
echo "ANTHROPIC_API_KEY=your_key_here" > .env
# OR
echo "OPENAI_API_KEY=your_key_here" > .env
# OR
echo "GEMINI_API_KEY=your_key_here" > .env
```

### Using Anthropic Claude 3.7 Sonnet (Recommended)

Claude 3.7 Sonnet provides the most reliable and advanced agent capabilities:

1. Obtain an API key from [Anthropic](https://www.anthropic.com/)
2. Set the ANTHROPIC_API_KEY environment variable
3. Select the "Claude 3.7 Sonnet" model in the UI

This implementation includes:
- Optimized system prompts for Claude 3.7
- JSON schema output formatting for structured responses
- Improved error handling and retry mechanisms

### Using Ollama Models

oli supports local models through Ollama:

1. Install [Ollama](https://ollama.com/) if you haven't already
2. Start the Ollama server:
   ```bash
   ollama serve
   ```
3. Pull the model you want to use (we recommend models with tool use capabilities):
   ```bash
   # Examples of compatible models
   ollama pull qwen2.5-coder:14b
   ollama pull qwen2.5-coder:3b
   ollama pull llama3:8b
   ```
4. Start oli and select the Ollama model from the model selection menu

Note: For best results with tool use and agent capabilities, use models like Qwen 2.5 Coder which support function calling.

Note: You can also use a remote Ollama instance by setting the OLLAMA_API_BASE environment variable.

## Usage

1. Start the application:
```bash
./run.sh
```

2. Select a model:
   - Cloud models (Claude 3 Sonnet, GPT-4o, Gemini 2.5) for full agent capabilities
   - Local models via Ollama (Qwen, Llama, etc.)

3. Make your coding query in the chat interface:
   - Ask for file searches
   - Request code edits
   - Execute shell commands
   - Get explanations of code

## Architecture

The application uses a hybrid architecture:

```
┌───────────────┐        ┌───────────────┐
│ React + Ink UI│◄───────┤ Rust Backend  │
│               │  JSON  │               │
│ - UI          │  RPC   │ - Agent       │
│ - Task Display│        │ - Tool Exec   │
│ - Loading     │        │ - Code Parse  │
└───────────────┘        └───────────────┘
```

- **Rust Backend**: Handles agent functionality, tool execution, and API calls
- **React/Ink Frontend**: Provides a modern, interactive terminal interface with smooth animations

## Examples

Here are some example queries to try:

- "Explain the codebase and how to get started"
- "List all files in the project"
- "Summarize the Cargo.toml file"
- "Show me all files that import the 'anyhow' crate"

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgments

- This project is inspired by Claude Code and similar AI assistants
- Uses Anthropic's Claude 3.7 Sonnet model for optimal agent capabilities
- Backend built with Rust for performance and reliability
- Frontend built with React and Ink for a modern terminal UI experience
- Special thanks to the Rust and React communities for excellent libraries and tools
