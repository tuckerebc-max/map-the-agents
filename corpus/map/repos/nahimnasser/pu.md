# nahimnasser/pu

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9be54622ba1b @ 07d31fc542e82339

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a single shell script, pu.sh, described as under 50KB with zero package dependencies, relying on curl, awk, common Unix tools, and an API key. The agent exposes seven tools: bash, read, write, edit, grep, find, and ls, described as a Pi-shaped tool surface.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product is a single shell script, pu.sh, described as under 50KB with zero package dependencies, relying on curl, awk, common Unix tools, and an API key. -- evidence: [README.md#L14-L14](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L14-L14), [README.md#L5-L5](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L5-L5), [README.md#L166-L166](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L166-L166)
- design-choices (2 claim(s)):
  - [observation/documented] JSON handling uses targeted awk parsing rather than a general JSON parser or jq, a deliberate choice to keep the install dependency-free. -- evidence: [README.md#L211-L217](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L211-L217), [README.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L168-L168), [README.md#L79-L87](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L79-L87)
  - [observation/documented] File writes and edits use mktemp temp files, preserve trailing newlines via sentinel capture, keep executable mode on edits, and edit requires a unique oldText match. -- evidence: [bugs.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L168-L168), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [bugs.md#L265-L265](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L265-L265), [bugs.md#L180-L180](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L180-L180)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The agent exposes seven tools: bash, read, write, edit, grep, find, and ls, described as a Pi-shaped tool surface. -- evidence: [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L221-L221](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L221-L221)
  - [observation/documented] It offers an interactive REPL with commands including /model, /effort, /login, /logout, /flush, /compact, /export, /skill:name, /quit, and !cmd for inline shell execution. -- evidence: [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L133-L146](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L133-L146)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions persist to .pu-history.json for resumable memory and .pu-events.jsonl for event replay/export; long sessions auto-compact by summarizing older transcript entries while keeping a bounded recent tail. -- evidence: [README.md#L178-L178](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L178-L178), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The bash tool executes model-provided commands unsandboxed via a temp script; AGENT_CONFIRM=1 can be set to ask before each tool call. -- evidence: [README.md#L107-L129](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L107-L129), [bugs.md#L368-L368](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L368-L368)
- evaluation (1 claim(s)):
  - [inference/documented] The README references 30+ experiments in final_report.md on harness portability and an eval/COMPARISON.md feature-by-feature comparison against Pi, suggesting evaluation effort beyond unit tests, though no scored agent benchmarks appear in the provided slices. -- evidence: [README.md#L44-L44](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L44-L44), [README.md#L223-L223](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L223-L223)
- dependencies (1 claim(s)):
  - [observation/documented] It targets two providers: Anthropic via /v1/messages and OpenAI via /v1/responses, with API keys supplied via environment variables or a first-run login wizard saving ~/.pu.env. -- evidence: [README.md#L38-L40](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L38-L40), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L168-L168)
- limitations (3 claim(s)):
More evidence: [full detail](pu.detail.md)

Metadata and full claim list: [full detail](pu.detail.md)
Human notes ([notes](pu.notes.md), never overwritten by build)

[Back to map index](../../index.md)
