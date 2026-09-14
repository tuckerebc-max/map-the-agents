# prorise-cool/claude-code-multi-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0dc13057c17f @ f6186454c59968b4

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework runs a Python hooks system that executes intelligent actions automatically across the Claude Code session lifecycle, using Ollama for smart decisions. The layout includes .claude/hooks (core modules base_hook.py, ollama_client.py, document_manager.py, config.py, logger.py plus handler entry scripts), .claude/commands, .claude/skills, and settings.json for hooks configuration.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The framework runs a Python hooks system that executes intelligent actions automatically across the Claude Code session lifecycle, using Ollama for smart decisions. -- evidence: [README.md#L358-L358](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L358-L358), [README.md#L23-L23](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L23-L23)
  - [observation/documented] The layout includes .claude/hooks (core modules base_hook.py, ollama_client.py, document_manager.py, config.py, logger.py plus handler entry scripts), .claude/commands, .claude/skills, and settings.json for hooks configuration. -- evidence: [README.md#L879-L919](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L879-L919)
- design-choices (2 claim(s)):
  - [observation/documented] The design is document-driven: three core documents (DEVELOPMENT.md, KNOWLEDGE.md, CHANGELOG.md) are read and injected at session start, replacing Memory MCP to avoid context explosion. -- evidence: [README.md#L360-L363](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L360-L363), [README.md#L93-L93](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L93-L93)
  - [observation/documented] All prompt templates are stored in .claude/hooks/prompts.json with variable placeholders, grouped by hook type, for tuning and version control; edits load on the next hook run without restart. -- evidence: [README.md#L1031-L1031](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1031-L1031), [README.md#L496-L501](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L496-L501)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to fork the repo, create a feature branch, commit, push, and open a pull request, and to set up the dev environment with uv sync. -- evidence: [README.md#L1071-L1071](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1071-L1071), [README.md#L1041-L1054](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1041-L1054)
- skills-patterns (1 claim(s)):
  - [observation/documented] Each skill requires a SKILL.md with YAML frontmatter (shown fields: name, description, version, author) and may include a references/ directory; example skills include code-review, test-generator, api-designer, database-optimizer, and doc-writer. -- evidence: [README.md#L700-L701](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L700-L701), [README.md#L558-L564](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L558-L564), [README.md#L532-L550](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L532-L550), [README.md#L556-L556](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L556-L556), [README.md#L820-L821](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L820-L821), [README.md#L766-L767](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L766-L767), [README.md#L594-L595](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L594-L595), [README.md#L645-L646](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L645-L646)
- interfaces (2 claim(s)):
  - [observation/documented] Hooks return JSON with an exit_code where 0 allows the operation to continue and 2 blocks it, e.g. when a dangerous command is detected. -- evidence: [README.md#L409-L410](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L409-L410), [README.md#L382-L382](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L382-L382)
  - [observation/documented] Skills are invoked via slash commands like /backend-specialist; the flow reads the skill's SKILL.md, parses YAML frontmatter, and uses Ollama to optimize the prompt before executing as an expert persona. -- evidence: [README.md#L288-L290](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L288-L290), [README.md#L520-L528](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L520-L528)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] On session start, the SessionStart hook detects the project type via Ollama, scans and loads skills, initializes the document system, and checks Git configuration such as .gitignore and branch strategy. -- evidence: [README.md#L445-L445](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L445-L445), [README.md#L441-L441](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L441-L441), [README.md#L455-L455](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L455-L455), [README.md#L258-L262](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L258-L262), [README.md#L437-L437](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L437-L437), [README.md#L449-L451](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L449-L451)
- tools-permissions (1 claim(s)):
More evidence: [full detail](claude-code-multi-agent.detail.md)

Metadata and full claim list: [full detail](claude-code-multi-agent.detail.md)
Human notes ([notes](claude-code-multi-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
