# mistralai/mistral-vibe

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d4b3223bbd74 @ da3e2ef6099117de

## Summary (orientation draft, not independently verified)

Selected evidence records: Mistral Vibe is a command-line coding assistant powered by Mistral's models, providing a conversational interface to explore, modify, and interact with codebases using natural language. The CLI offers interactive chat via `vibe`, a one-shot prompt argument, and non-interactive programmatic mode through `--prompt` or piped input for scripting.

## Source coverage

Source coverage (partial): 6 of 23 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Built-in tools include read, write_file, edit, grep (with ripgrep support), todo list management, ask_user_question, and task delegation; shell tools exist in a legacy one-shot bash variant and a managed variant with session, stdin, and log-file tools. -- evidence: [README.md#L95-L111](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L95-L111), [README.md#L590-L593](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L590-L593), [README.md#L579-L588](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L579-L588)
- design-choices (1 claim(s)):
  - [observation/documented] Vibe includes a trust folder system: directories containing a .vibe subfolder may prompt for trust confirmation, trusted folders are remembered in ~/.vibe/trusted_folders.toml, and AGENTS.md instructions and project-local skills load only for trusted folders. -- evidence: [README.md#L260-L260](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L260-L260), [README.md#L514-L514](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L514-L514), [README.md#L258-L258](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L258-L258), [README.md#L400-L403](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L400-L403)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are directories with a SKILL.md using YAML frontmatter, following the Agent Skills specification; they can add tools, slash commands, and behaviors, and are discovered from config skill_paths, .agents/skills/, .vibe/skills/, and ~/.vibe/skills/. -- evidence: [README.md#L370-L370](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L370-L370), [README.md#L372-L372](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L372-L372), [README.md#L376-L376](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L376-L376), [README.md#L400-L403](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L400-L403)
- interfaces (4 claim(s)):
  - [observation/documented] Mistral Vibe is a command-line coding assistant powered by Mistral's models, providing a conversational interface to explore, modify, and interact with codebases using natural language. -- evidence: [README.md#L22-L22](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L22-L22), [README.md#L20-L20](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L20-L20)
  - [observation/documented] The CLI offers interactive chat via `vibe`, a one-shot prompt argument, and non-interactive programmatic mode through `--prompt` or piped input for scripting. -- evidence: [README.md#L252-L254](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L252-L254), [README.md#L268-L270](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L268-L270), [README.md#L232-L232](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L232-L232), [README.md#L266-L266](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L266-L266)
- memory-state (1 claim(s)):
  - [observation/documented] Compaction uses a built-in prompt at prompts/compact.md by default, keeps the same session and visible conversation, and later model requests use the compacted context followed by newer messages; custom compaction prompts are supported. -- evidence: [README.md#L531-L531](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L531-L531), [README.md#L542-L543](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L542-L543)
- orchestration (1 claim(s)):
  - [observation/documented] A `task` tool delegates work to subagents that run independently without user interaction; a built-in read-only `explore` subagent exists, and custom subagents are defined with agent_type = "subagent". -- evidence: [README.md#L146-L146](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L146-L146), [README.md#L158-L158](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L158-L158), [README.md#L148-L148](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L148-L148)
- tools-permissions (2 claim(s)):
  - [observation/documented] Vibe ships built-in agent profiles governing tool approval: ask (approval required), plan (read-only, auto-approves safe tools), accept-edits (default, auto-approves file edits), and auto-approve (approves all tool executions). -- evidence: [README.md#L117-L120](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L117-L120)
More evidence: [full detail](mistral-vibe.detail.md)

Metadata and full claim list: [full detail](mistral-vibe.detail.md)
Human notes ([notes](mistral-vibe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
