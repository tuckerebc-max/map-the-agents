# Zentara Code — AI Coding Assistant for VS Code

Zentara Code turns chat instructions into precise, auditable changes in your codebase. It is optimized for speed, safety, and correctness through parallel execution, LSP semantics, and integrated runtime debugging.

## 🎥 Demo

Watch Zentara Code in action:

[![Zentara Code Release Demo](https://img.youtube.com/vi/YWezcsj-CHc/0.jpg)](https://youtu.be/YWezcsj-CHc)

## What Makes Zentara Different

- **Parallel subagents**: Independent workers run simultaneously with strict scope separation, opt‑in write permissions, and per‑agent timeouts for high throughput without conflicts.
- **Integrated LSP tools**: Operations use the Language Server Protocol for file structure, semantic references, call hierarchy, safe renames, workspace‑wide symbol discovery, and targeted snippets.
- **Runtime debugging**: Launch, control, and inspect debug sessions from tasks to reproduce, instrument, step, and validate before concluding changes.

## Getting Started

Zentara Code is a VS Code extension. Here's how you can get started:

> **Quick Start Tip**: Once installed, try the `/init` command in any project to automatically analyze your codebase and generate AI-friendly documentation. This helps Zentara understand your project's patterns and conventions for better assistance. See the [/init Command Guide](docs/init-command-overview.md) for details.

**1. Install from VS Code Marketplace (Recommended for Users)**

- Install latest VS Code. The extension is build for VS Code 1.96.4 and later
- Open VS Code.
- Install the necessary language extension and language debugger extension. For example for Python, just install Microsoft Python extension, it will automatically install debugpy debugger. Check the debugger manually on any of your script to make sure it works.
- **Configure `launch.json` (Optional but Recommended):** For a more streamlined experience, you can define debug configurations in your `.vscode/launch.json` file. This allows you to launch complex debugging scenarios with a simple name (e.g., "Run Extension", "Debug Current Test File"). You can then instruct Zentara to use these configurations directly, e.g., "Zentara, launch the debugger with the 'Run Extension' config". For TypeScript files, install npm and tsx (by running `npm install -g tsx`).
-  For Zentara Code to effectively debug Python projects, especially those using Conda environments or specific `pytest` installations, ensure the correct Python interpreter is configured in your VS Code settings (`.vscode/settings.json`):

```json
{
	"python.defaultInterpreterPath": "/path/to/your/conda/env/bin/python"
}
```

Replace `/path/to/your/conda/env/bin/python` with the actual path to your Python interpreter.
- For python pytest tests: install pytest. If you would like to install pytest in a conda enviroment,remember to point the python interperter in settings.json(see the above point) 
- Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X).
- Search for "Zentara Code".
- Click "Install".
- Once installed, Zentara Code will be available to assist you.
  

For more detailed installation instruction, please visit https://zentar.ai, click on the "Install for free" button.

**2. Build and Install from Source (For Developers/Contributors)**

If you want to contribute or run the latest development version:

- **Clone the repository:**

    ```sh
    git clone https://github.com/Zentar-Ai/Zentara-Code.git
    cd zentara-code
    ```

- **Install dependencies:**
  This project uses pnpm. Ensure you have Node.js npm , pnpm installed.
    ```sh
    pnpm install
    ```
- **Build the extension:**

    ```sh
    pnpm vsix
    ```

    This will typically compile the TypeScript code and package the extension into a `.vsix` file in a `bin/` directory.

- **Install the .vsix file in VS Code:**
    1.  Go to the Extensions view in VS Code.
    2.  Click the "..." (More Actions) menu in the top-right corner of the Extensions view.
    3.  Select "Install from VSIX..."
    4.  Navigate to and select the generated `.vsix` file.

## LLM Provider
We recommend subscribe for Claude Max plan  to use Zentara Code. If you have Claude Max subscription already, in the Setting > API Provider, choose Claude Max (not Claude Code option) to get the best and fastest performance


## Workflow Model

- **Plan**: Zentara decomposes your request into small, independent steps and proposes safe execution order.
- **Approvals**: Potentially impactful actions (file writes, network, long operations) require explicit approval.
- **Execute**: Steps are distributed to parallel subagents when independent to reduce wall‑clock time.
- **Analyze**: Code understanding is LSP‑first (document symbols → usages → call hierarchy → targeted snippets).
- **Verify**: Integrated debugging provides breakpoints, stepping, state inspection, and evaluation to confirm behavior.

## Core Capabilities

### Code Understanding & Analysis
- File and module structure analysis via LSP document symbols
- True semantic usages across the workspace (not text matches)
- Caller/callee relationships via call hierarchy
- Targeted code snippets for precise context
- 25+ LSP tools for semantic code intelligence

### Parallel Task Execution
- Independent subagents with isolated contexts
- Scope separation to prevent conflicts
- Predefined agents for common workflows (code review, bug investigation)
- General subagents for custom tasks
- Available across all modes for maximum flexibility

### Code Generation & Editing
- Feature implementation, bug fixes, refactors
- Safe, reviewable diffs with minimal surface area
- Style‑ and framework‑aware changes
- Safe refactoring with semantic rename and impact analysis

### Runtime Debugging
- Complete debug session management (launch, restart, quit)
- Execution control (continue, step, jump, until)
- Comprehensive breakpoint management
- State inspection (stack traces, variables, evaluation)
- 35+ debugging operations for thorough validation

### Documentation & Testing
- Generate READMEs, API docs, and test scaffolds
- Propose focused unit/integration tests

### Project Automation
- Script generation, config updates, and task runners

## Detailed Guides

For comprehensive information on Zentara's advanced features:

- **[`/init` Command Guide](docs/init-command-overview.md)** - Complete overview of the `/init` slash command for intelligent project analysis and AI documentation generation
- **[LSP Tools Guide](docs/lsp-tools-overview.md)** - Complete reference for all 25+ Language Server Protocol tools, including discovery, navigation, analysis, and modification operations
- **[Subagent System Guide](docs/subagent-tool-overview.md)** - In-depth guide to parallel task execution, scope separation, and performance optimization
- **[Predefined Agents Guide](docs/predefined-agents-user-guide.md)** - How to create, use, and manage template-based subagents for standardized workflows
- **[Slash Commands Guide](docs/SLASH_COMMANDS_DOCUMENTATION.md)** - Complete guide to creating and customizing slash commands, including AI-driven execution, configuration system, and best practices
- **[Debugging Guide](docs/Debugging.md)** - Comprehensive debugging operations, session management, and runtime validation techniques
- **[Tool Integration Guide](docs/integrating-new-tools.md)** - Developer guide for extending Zentara with custom tools and integrations

## Parallel Subagents (Performance and Safety)

- **Isolation**: Each worker runs with its own context and is assigned non‑overlapping scope (files, features, layers).
- **Permissions**: Writes are opt‑in and constrained to allowed paths; read‑only by default.
- **Timeouts**: Per‑agent execution is time‑bounded to prevent runaway tasks.
- **Determinism**: Plans enumerate inputs/outputs; results are merged with conflict avoidance.
- **Observability**: You can inspect each subtask's plan and results before moving on.

*→ See [Subagent System Guide](docs/subagent-tool-overview.md) for advanced patterns and best practices*

## LSP‑First Code Intelligence (Accuracy)

- **Structure**: Get symbol trees without reading entire files.
- **Usages**: Find real references, not text matches.
- **Call graph**: See who calls what to understand flows and side effects.
- **Safety**: Use semantic information to avoid dangerous edits and hidden couplings.
- **Scope**: Ask for just the code that matters via targeted snippets to reduce noise.

*→ See [LSP Tools Guide](docs/lsp-tools-overview.md) for complete tool reference and workflows*

## Runtime Debugging (Validation)

- **Control**: Launch sessions, continue, step, and stop from within Zentara tasks.
- **Breakpoints**: Add, remove, enable/disable, conditional, and temporary breakpoints.
- **Inspection**: View stack traces, active frame variables, arguments, and source context.
- **Evaluation**: Evaluate expressions and run statements in the current context where supported.
- **Integration**: Use debugging during or after code edits to verify correctness before finalizing.

*→ See [Debugging Guide](docs/Debugging.md) for detailed operations and troubleshooting*





## Prompting Tips

- **Be goal‑oriented**: describe the outcome, constraints, and acceptance criteria.
- **Provide guardrails**: performance budgets, API boundaries, style preferences.
- **Embrace iteration**: accept partial progress and refine.
- **Let Zentara plan**: approve or edit its proposed steps rather than dictating line‑level changes.

## Debugging & Troubleshooting

### Viewing Zentara Debug Logs

To observe all conversations between the LLM and Zentara, including detailed execution logs and debugging information:

1. **Open the Output Panel**:
   - **Method 1**: Use the keyboard shortcut `Ctrl+Shift+U` (Windows/Linux) or `Cmd+Shift+U` (Mac)
   - **Method 2**: Go to the top menu bar → **View** → **Output**
   - **Method 3**: Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and type "View: Toggle Output"

2. **Select Zentara Debug Channel**:
   - In the Output panel (usually appears at the bottom of VS Code), look for a dropdown menu on the right side
   - Click the dropdown and select **"Zentara Debug"** from the list of available output channels
   - If you don't see "Zentara Debug", make sure Zentara Code extension is active and try interacting with it first

3. **What You'll See**:
   - Real-time conversation logs between you and the AI
   - Tool execution details and results
   - Error messages and debugging information
   - Subagent communications and parallel task execution logs
   - LSP operation details and responses

**Tip**: Keep the Output panel open while working with Zentara to monitor its operations and troubleshoot any issues in real-time.

## Roadmap & Changelog

We're constantly evolving Zentara Code. Check out our [issue tracker](https://github.com/Zentar-Ai/Zentara-code/issues?q=is%3Aopen+is%3Aissue+label%3Aroadmap) for our public roadmap and planned features. If you're looking to contribute, `good first issue` labels are a great place to start!

## Contributing

Zentara Code thrives on community involvement! We welcome contributions of all kinds.

- **[Issue Tracker](https://github.com/Zentar-Ai/zentara-code/issues)**
- **[Code of Conduct](CODE_OF_CONDUCT.md)**

## Follow Us

Follow us on Twitter: [@ZentaraCode](https://twitter.com/ZentaraCode)

## License

Zentara Code is licensed under the [Apache License 2.0](./LICENSE).

© 2025 ZentarAI

## Acknowledgments

Zentara Code is a mod from the great [Roo-Code](https://github.com/RooCodeInc/Roo-Code). We greatly thank the contributors of the RooCode community and the original Cline community that RooCode developed from.
