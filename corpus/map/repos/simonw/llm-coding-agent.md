# simonw/llm-coding-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 01dbde5897fc @ 0a77211a52823127

## Summary (orientation draft, not independently verified)

The evidence describes llm-coding-agent, an LLM-plugin coding agent exposing an `llm code` CLI and a Python CodingAgent/CodingTools API with file, search, and shell tools, an approval-based permission system, and SQLite session logging. Most content is specification/README documentation rather than inspected code.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] CodingTools is an llm.Toolbox confined to a root directory providing read_file, write_file, edit_file, list_files, search_files, and execute_command tools. -- evidence: [README.md#L111-L113](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L111-L113), [README.md#L102-L105](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L102-L105), [README.md#L86-L86](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L86-L86), [README.md#L91-L96](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L91-L96)
- design-choices (3 claim(s)):
  - [observation/documented] edit_file performs exact string replacement requiring old_string to appear exactly once unless replace_all is set, and returns a unified diff so the model can verify its edit. -- evidence: [README.md#L98-L98](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L98-L98), [spec.md#L125-L130](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L125-L130)
  - [observation/documented] All file access is confined to the session root: paths escaping via '..', absolute paths, or symlinks return an 'Error:' string instead of content, letting the model self-correct. -- evidence: [spec.md#L99-L103](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L99-L103), [README.md#L117-L117](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L117-L117)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors create a virtualenv, install with `python -m pip install -e '.[test]'`, and run tests via `python -m pytest`. -- evidence: [README.md#L121-L134](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L121-L134)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Installing the package as an LLM plugin adds an `llm code` command that starts an interactive coding agent session in the current directory with any tool-capable model LLM supports. -- evidence: [README.md#L30-L30](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L30-L30)
  - [observation/documented] The `llm code` CLI accepts options including an initial prompt, -m/--model, -s/--system, -d/--directory, --yolo, repeatable --allow glob patterns, --no-tool, -c/--continue, --cid, -o model options, and --chain-limit. -- evidence: [spec.md#L56-L68](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L56-L68), [README.md#L32-L38](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L32-L38)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are logged to LLM's SQLite database like `llm chat`, so `llm logs` shows full transcripts including tool calls, and conversations can be resumed via -c or --cid. -- evidence: [spec.md#L87-L88](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L87-L88), [README.md#L42-L42](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L42-L42), [README.md#L44-L48](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L44-L48)
- orchestration (1 claim(s)):
  - [observation/documented] The agent loop uses conversation.chain with a chain_limit (default 25) bounding tool-execution rounds per run; hitting the limit sets result.hit_limit and returns control to the user. -- evidence: [README.md#L82-L82](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L82-L82), [spec.md#L209-L216](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L209-L216)
- tools-permissions (2 claim(s)):
  - [observation/documented] Read-only tools run freely, while writes, edits, and shell commands require approval; 'y' approves once, 'a' approves similar actions for the session, and denial is reported back to the model. -- evidence: [spec.md#L173-L183](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L173-L183), [README.md#L40-L40](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L40-L40)
More evidence: [full detail](llm-coding-agent.detail.md)

Metadata and full claim list: [full detail](llm-coding-agent.detail.md)
Human notes ([notes](llm-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
