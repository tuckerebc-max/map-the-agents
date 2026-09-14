# Installing and Using Gemini Code

This guide explains how to install, configure, and use Gemini Code.

## Installation Options

### Option 1: Quick Install (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/raizamartin/gemini-code/main/install.sh | bash
```

This will install Gemini Code and set up a shortcut for easy access.

### Option 2: Install from PyPI

```bash
pip install gemini-code
```

### Option 3: Install from Source

```bash
git clone https://github.com/raizamartin/gemini-code.git
cd gemini-code
pip install -e .
```

## Setting Up Your API Key

Before using Gemini Code, you need to set up your Google API key:

```bash
gemini setup YOUR_GOOGLE_API_KEY
```

To get a Google API key for Gemini:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key or use an existing one
3. Copy the key and use it in the setup command above

Your API key is stored securely in `~/.config/gemini-code/config.yaml`.

## Using Gemini Code

### Starting a Session

```bash
# Start with default model (e.g., Gemini 2.5 Pro Experimental)
gemini

# Start with a specific model
gemini --model gemini-1.5-pro-latest # Or another available model
```

### Available Commands

During an interactive session, you can use these commands:

- `/help` - Display help information
- `/exit` - Exit the chat session

### Configuration Options

Set your default model:

```bash
gemini set-default-model gemini-1.5-pro-latest # Or your preferred default
```

## Where Files Are Stored

- Configuration: `~/.config/gemini-code/config.yaml`
- API Keys: Stored in the configuration file
- Logs: Currently not persistent between sessions

## Troubleshooting

If you encounter issues:

1. Verify your API key is correct: `cat ~/.config/gemini-code/config.yaml`
2. Ensure you have a working internet connection
3. Check that you have Python 3.8+ installed: `python --version`
4. Make sure the required packages are installed: `pip list | grep gemini-code`

For more help, visit: https://github.com/raizamartin/gemini-code