# OCode Configuration Guide

This guide covers all configuration options for OCode, including project settings, security configuration, and environment variables.

## Configuration Hierarchy

OCode uses a hierarchical configuration system:

1. **Default Configuration** - Built-in defaults
2. **User Configuration** - `~/.ocode/settings.json`
3. **Project Configuration** - `.ocode/settings.json`
4. **Environment Variables** - Override any setting
5. **Command Line Arguments** - Highest priority

Settings are merged with later sources overriding earlier ones.

## Project Configuration (.ocode/settings.json)

### Complete Schema

```json
{
  "model": "MFDoom/deepseek-coder-v2-tool-calling:latest",
  "max_tokens": 200000,
  "context_window": 4096,
  "temperature": 0.7,
  "max_context_files": 20,
  "chunk_size": 8192,
  "max_continuations": 10,
  "ollama_host": "http://localhost:11434",
  "permissions": {
    "allow_file_read": true,
    "allow_file_write": true,
    "allow_shell_exec": false,
    "allowed_paths": [
      "/home/user/projects",
      "/tmp/ocode"
    ],
    "blocked_paths": [
      "/etc",
      "/sys",
      "/proc"
    ],
    "allowed_commands": [
      "ls",
      "cat",
      "grep",
      "find"
    ],
    "blocked_commands": [
      "rm -rf",
      "sudo",
      "chmod"
    ]
  },
  "ignore_patterns": [
    ".git",
    "node_modules",
    "__pycache__",
    "*.pyc",
    ".env",
    ".venv",
    "venv",
    "dist",
    "build"
  ],
  "memory": {
    "cache_ttl": 3600,
    "max_cache_size": 100,
    "persistent_store": true
  },
  "output": {
    "format": "text",
    "color": true,
    "verbose": false,
    "max_line_length": 88
  },
  "tools": {
    "enabled": [
      "file_read",
      "file_write",
      "grep",
      "find"
    ],
    "disabled": [
      "bash"
    ],
    "timeout": 30
  }
}
```

### Setting Descriptions

#### Model Configuration
- **model**: Ollama model to use for completions
  - Default: `"MFDoom/deepseek-coder-v2-tool-calling:latest"`
  - Options: Any Ollama model that supports function calling
  - Examples: `"llama3:8b"`, `"codellama:13b"`, `"mistral:latest"`

- **max_tokens**: Maximum tokens for model response
  - Default: `200000`
  - Range: 1000-500000
  - Higher values allow longer responses but use more memory

- **context_window**: Maximum context size for model
  - Default: `4096`
  - Range: 2048-32768
  - Should not exceed model's native context window

- **temperature**: Model temperature for response randomness
  - Default: `0.7`
  - Range: 0.0-2.0
  - Lower = more deterministic, Higher = more creative

#### Context Management
- **max_context_files**: Maximum files to include in context
  - Default: `20`
  - Range: 1-100
  - More files = better context but slower processing

- **chunk_size**: Size of response chunks in streaming
  - Default: `8192`
  - Range: 1024-65536
  - Larger chunks = fewer updates but less responsive

- **max_continuations**: Maximum automatic response continuations
  - Default: `10`
  - Range: 0-50
  - Prevents infinite loops in long responses

#### Ollama Connection
- **ollama_host**: Ollama API endpoint
  - Default: `"http://localhost:11434"`
  - Format: `"http://hostname:port"`
  - Can point to remote Ollama instance

#### Security Configuration

##### Permissions
- **allow_file_read**: Enable file reading operations
  - Default: `true`
  - Set to `false` to disable all file reading

- **allow_file_write**: Enable file writing operations
  - Default: `true`
  - Set to `false` for read-only mode

- **allow_shell_exec**: Enable shell command execution
  - Default: `false`
  - ⚠️ **Security Risk**: Only enable if necessary

##### Path Restrictions
- **allowed_paths**: Paths where file operations are permitted
  - Default: `["."]` (current directory)
  - Use absolute paths for clarity
  - Supports glob patterns: `"/home/*/projects"`

- **blocked_paths**: Paths where operations are forbidden
  - Default: System directories
  - Always blocks: `/etc`, `/sys`, `/proc`, `/boot`
  - Takes precedence over allowed_paths

##### Command Restrictions
- **allowed_commands**: Shell commands that can be executed
  - Default: Safe read-only commands
  - Only applies if `allow_shell_exec` is true
  - Use full command or prefix matching

- **blocked_commands**: Shell commands that are forbidden
  - Default: Dangerous commands
  - Pattern matching: `"rm -rf"` blocks `"rm -rf /"`
  - Takes precedence over allowed_commands

#### File Filtering
- **ignore_patterns**: Files/directories to exclude from context
  - Default: Common build artifacts and caches
  - Supports glob patterns
  - Improves performance by skipping irrelevant files

#### Memory Configuration
- **cache_ttl**: Cache time-to-live in seconds
  - Default: `3600` (1 hour)
  - Range: 0-86400
  - Set to 0 to disable caching

- **max_cache_size**: Maximum cache entries
  - Default: `100`
  - Range: 10-1000
  - Older entries evicted when limit reached

- **persistent_store**: Enable persistent memory storage
  - Default: `true`
  - Stores memory across sessions

#### Output Configuration
- **format**: Default output format
  - Default: `"text"`
  - Options: `"text"`, `"json"`, `"markdown"`

- **color**: Enable colored output
  - Default: `true`
  - Auto-disabled in non-TTY environments

- **verbose**: Enable verbose logging
  - Default: `false`
  - Shows detailed operation information

- **max_line_length**: Maximum line length for output
  - Default: `88`
  - Range: 40-200
  - Used for formatting and wrapping

#### Tool Configuration
- **enabled**: List of explicitly enabled tools
  - Default: All tools enabled
  - Use to create tool allowlist

- **disabled**: List of explicitly disabled tools
  - Default: `[]`
  - Use to block specific tools

- **timeout**: Default timeout for tool operations in seconds
  - Default: `30`
  - Range: 5-300
  - Prevents hanging operations

## Environment Variables

Override any configuration setting using environment variables:

```bash
# Model configuration
export OCODE_MODEL="llama3:latest"
export OCODE_MAX_TOKENS="100000"
export OCODE_TEMPERATURE="0.5"

# Connection settings
export OLLAMA_HOST="http://gpu-server:11434"

# Security settings
export OCODE_ALLOW_SHELL_EXEC="true"
export OCODE_ALLOWED_PATHS="/home/user/safe,/tmp"

# Output settings
export OCODE_VERBOSE="true"
export OCODE_OUTPUT_FORMAT="json"
```

### Environment Variable Rules
1. Prefix setting names with `OCODE_`
2. Convert to uppercase
3. Replace dots with underscores
4. Lists use comma separation
5. Booleans use "true"/"false"

## Command Line Arguments

Override settings for a single run:

```bash
# Model selection
ocode --model llama3:70b -p "Complex analysis task"

# Verbose output
ocode -v -p "Debug this error"

# Output format
ocode --out json -p "List all Python files"

# Continue previous session
ocode -c -p "Continue the analysis"
```

### Available Arguments
- `-m, --model`: Override model selection
- `-v, --verbose`: Enable verbose output
- `--out`: Set output format (text/json/stream-json)
- `-c, --continue`: Continue previous session
- `--config`: Use specific config file

## Security Best Practices

### Recommended Production Settings

```json
{
  "permissions": {
    "allow_file_read": true,
    "allow_file_write": false,
    "allow_shell_exec": false,
    "allowed_paths": [
      "/home/project/src"
    ],
    "blocked_paths": [
      "/home/project/.env",
      "/home/project/secrets"
    ]
  }
}
```

### Path Security
1. Use absolute paths in allowed_paths
2. Never allow root directory access
3. Block sensitive file patterns
4. Regularly audit allowed paths

### Command Security
1. Default to `allow_shell_exec: false`
2. Use explicit command allowlists
3. Block command combinations
4. Avoid sudo/admin commands

## Configuration Examples

### Read-Only Analysis

```json
{
  "permissions": {
    "allow_file_read": true,
    "allow_file_write": false,
    "allow_shell_exec": false
  },
  "tools": {
    "disabled": ["file_write", "file_edit", "file_ops", "bash"]
  }
}
```

### Development Environment

```json
{
  "model": "codellama:13b",
  "max_context_files": 50,
  "permissions": {
    "allow_file_read": true,
    "allow_file_write": true,
    "allow_shell_exec": true,
    "allowed_paths": ["~/projects"],
    "allowed_commands": ["npm", "pytest", "git"]
  }
}
```

### CI/CD Integration

```json
{
  "output": {
    "format": "json",
    "color": false
  },
  "permissions": {
    "allow_file_read": true,
    "allow_file_write": false,
    "allow_shell_exec": true,
    "allowed_commands": ["pytest", "npm test", "cargo test"]
  },
  "tools": {
    "timeout": 300
  }
}
```

### Minimal Configuration

```json
{
  "model": "llama3:8b",
  "allowed_paths": ["."]
}
```

## Initializing Configuration

### Create Default Configuration

```bash
# Initialize in current directory
ocode init

# Creates:
# .ocode/
# ├── settings.json
# ├── memory/
# └── commands/
```

### Copy from Template

```bash
# Copy example configuration
cp /usr/share/ocode/config.example.json .ocode/settings.json

# Edit as needed
nano .ocode/settings.json
```

### Validate Configuration

```bash
# Check current configuration
ocode config --list

# Test specific setting
ocode config --get model

# Validate security settings
ocode config --validate
```

## Troubleshooting

### Configuration Not Loading
1. Check file exists: `.ocode/settings.json`
2. Validate JSON syntax
3. Check file permissions
4. Look for parse errors in verbose mode

### Settings Not Applied
1. Check configuration hierarchy
2. Environment variables override files
3. Command line args override everything
4. Use `--verbose` to see active config

### Permission Denied
1. Path not in allowed_paths
2. Path explicitly blocked
3. Operation disabled
4. Check parent directory permissions

## Advanced Configuration

### Dynamic Configuration

Use scripts to generate configuration:

```bash
#!/bin/bash
# generate-config.sh
cat > .ocode/settings.json <<EOF
{
  "model": "${OCODE_MODEL:-llama3:8b}",
  "allowed_paths": ["$(pwd)"]
}
EOF
```

### Per-Directory Settings

Create directory-specific configurations:

```
project/
├── .ocode/settings.json      # Project root
├── src/
│   └── .ocode/settings.json  # Src-specific
└── tests/
    └── .ocode/settings.json  # Test-specific
```

### Configuration Inheritance

Child configurations inherit from parents:

```json
// project/.ocode/settings.json
{
  "model": "codellama:13b",
  "allowed_paths": ["/project"]
}

// project/tests/.ocode/settings.json
{
  "tools": {
    "enabled": ["test_runner", "file_read"]
  }
}
```

## Migration Guide

### From v1.x to v2.x

1. Rename `max_files` to `max_context_files`
2. Move `ollama_host` out of `connection` object
3. Update tool names (snake_case)
4. Migrate security settings to `permissions`

### Future Compatibility

- Keep configuration minimal
- Use latest schema version
- Test after updates
- Backup before migration
