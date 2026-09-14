# Better Coding Agents

This is a really dumb but incredibly effective way to get better coding agent responses for libraries and frameworks.

Basically you just clone the entire source repo for the library/framework as a git subtree, and then you can ask the agent to search the codebase for the answer to a question, and it works really well.

This project has this setup for:

- svelte & sveltekit
- effect.ts
- neverthrow
- opencode

## getting started

1. clone the repo into your home directory, it should be called `~/.better-coding-agents`
2. copy paste the following command into opencode (while it's open in your home directory)

And now you have slash commands for these libraries/frameworks in opencode and cursor. as well as a special agent in opencode that can search the codebase for the answer to a question.

_I also included the color theme I like ported to opencode as well lol_

````md
# Init Command

This command sets up opencode commands and agents, as well as cursor commands on the user's machine. It works as an upsert operation - updating existing files or creating new ones as needed.

## Instructions

Execute the following steps to initialize the configurations:

### 1. Setup OpenCode Configuration

Create the OpenCode directories if they don't exist and copy all files from @OPENCODE_ASSETS/:

```bash
# Create directories if they don't exist
mkdir -p ~/.config/opencode/agent
mkdir -p ~/.config/opencode/command
mkdir -p ~/.config/opencode/themes

# Copy agent files
cp -u ./.better-coding-agents/OPENCODE_ASSETS/agent/*.md ~/.config/opencode/agent/

# Copy command files
cp -u ./.better-coding-agents/OPENCODE_ASSETS/command/*.md ~/.config/opencode/command/

# Copy theme files
cp -u ./.better-coding-agents/OPENCODE_ASSETS/themes/*.json ~/.config/opencode/themes/
```

### 2. Setup Cursor Configuration

Create the Cursor commands directory if it doesn't exist and copy all files from @CURSOR_ASSETS/commands/:

```bash
# Create directory if it doesn't exist
mkdir -p ~/.cursor/commands

# Copy cursor command files
cp -u ./.better-coding-agents/CURSOR_ASSETS/commands/*.md ~/.cursor/commands/
```

## Notes

- The `cp -u` flag ensures existing files are only overwritten if the source is newer
- All necessary parent directories will be created if they don't already exist
- After setup, users can run OpenCode commands and Cursor commands from their respective directories
````
