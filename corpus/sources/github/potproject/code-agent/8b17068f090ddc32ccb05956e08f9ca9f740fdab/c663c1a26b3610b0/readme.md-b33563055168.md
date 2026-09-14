#  Code Agent

An AI Agent that operates [Claude Code](https://github.com/anthropics/claude-code) and [Codex](https://github.com/openai/codex) on GitHub Actions. By using this action, you can directly invoke Claude Code or Codex from GitHub Issues or Pull Request comments and automate code changes.

## Features

- Start Claude Code with the `/claude` command from GitHub Issues or PR comments
- Start Codex with the `/codex` command from GitHub Issues or PR comments
- Automatically create a Pull Request or commit changes if the AI modifies code
- Post AI output as a comment if there are no changes

## Usage

### Project Settings

#### Settings -> Actions -> General -> Workflow permissions

* Read and write permissions
* ✔ Allow GitHub Actions to create and approve pull requests

![image](https://github.com/user-attachments/assets/e78e60d0-9e16-425e-bcad-264c8f81b878)

#### Settings -> Secrets and variables -> Actions -> Secrets

* Repository secrets: Set `ANTHROPIC_API_KEY` (for Claude Code) or `OPENAI_API_KEY` (for Codex)

![image](https://github.com/user-attachments/assets/fdfb1d5a-9605-4d2d-9f7b-0bd65bc7a3fd)

### Workflow Configuration

```yaml
name: Code Agent

permissions:
  contents: write
  pull-requests: write
  issues: write

on:
  issues:
    types: [opened]
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  code-agent:
    runs-on: ubuntu-latest
    if: ${{ github.event.sender.type != 'Bot' }}
    steps:
      - uses: potproject/code-agent@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}

          # [Claude Code Settings]
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}

          # [Optional Claude Code Settings]
          # anthropic-base-url: "https://api.anthropic.com"
          # anthropic-model: "claude-3-7-sonnet-20250219"
          # anthropic-small-fast-model: "claude-3-5-haiku-20241022"
          # claude-code-use-bedrock: "1"
          # anthropic-bedrock-base-url: "https://bedrock.us-east-1.amazonaws.com"
          # aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          # aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          # aws-region: "us-east-1"
          # disable-prompt-caching: "1"
          
          # [Codex Settings]
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}

          # [Optional Codex Settings]
          # openai-base-url: "https://api.openai.com"
```

## Example

View on [code-agent-example Issues](https://github.com/potproject/code-agent-example/issues) / [code-agent-example Pulls](https://github.com/potproject/code-agent-example/pulls)

### Example Usage in Issues

Create a new Issue and add the following to the body:

```
/claude Please create a new API endpoint. This should be an endpoint that handles GET requests to retrieve user information.
```

```
/codex Please create a new API endpoint. This should be an endpoint that handles GET requests to retrieve user information.
```

Claude Code or Codex will analyze the request and create a new Pull Request with the code changes. The AI will also post a comment with the generated code.

### Example Usage in PRs


Comment on an existing Pull Request to request code modifications:

```
/claude Please add unit tests to this code.
```

```
/codex Please add unit tests to this code.
```

Claude Code or Codex will analyze the request and create a new Pull Request with the code changes. The AI will also post a comment with the generated code.

## Inputs Settings
### Basic Configuration

| Input Name | Description |
|------------|-------------|
| `github-token` | **Required** GitHub token for authentication |
| `event-path` | Path to the event file (default: `${{ github.event_path }}`) |
| `timeout` | Timeout for AI processing in seconds (default: 600) |

### Claude Code Configuration

| Input Name | Description |
|------------|-------------|
| `anthropic-api-key` | **Required for Claude Code** Anthropic API key for authentication |

### Advanced Claude Code Configuration

| Input Name | Description |
|------------|-------------|
| `anthropic-base-url` | Anthropic API base URL |
| `anthropic-model` | Anthropic model to use |
| `anthropic-small-fast-model` | Small and fast model for commit message generation etc. |
| `claude-code-use-bedrock` | Use AWS Bedrock for Claude Code (0 or 1) |
| `anthropic-bedrock-base-url` | Anthropic Bedrock API base URL |
| `aws-access-key-id` | AWS Access Key ID (when using Bedrock) |
| `aws-secret-access-key` | AWS Secret Access Key (when using Bedrock) |
| `aws-region` | AWS region (when using Bedrock) |
| `disable-prompt-caching` | Disable prompt caching (0 or 1) |

### Codex Configuration

| Input Name | Description |
|------------|-------------|
| `openai-api-key` | **Required for Codex** OpenAI API key for authentication |


### Advanced Codex Configuration

| Input Name | Description |
|------------|-------------|
| `openai-base-url` | OpenAI API base URL |

## Security

* **Permission Checks:** Before executing core logic, the action verifies if the triggering user (`github.context.actor`) has `write` or `admin` permissions for the repository.
* **Sensitive Information Masking:** Any occurrences of the provided `github-token` and `anthropic-api-key`, `AWS Credentials`, `openai-api-key` within the output posted to GitHub are automatically masked (replaced with `***`) to prevent accidental exposure.
