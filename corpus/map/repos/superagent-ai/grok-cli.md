# superagent-ai/grok-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fb97af83f06d @ d13dd57301adcd9f

## Summary (orientation draft, not independently verified)

Selected evidence records: The CLI supports headless runs via --prompt with options such as --directory, --max-tool-rounds, --format json, --batch-api, and --verify, plus session resume via --session latest or -s <session-id>. With --format json, headless output becomes a newline-delimited JSON event stream of semantic step-level events such as step_start, text, tool_use, step_finish, and error.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Custom sub-agents can be defined in user settings with name, model, and instruction; the names general, explore, vision, verify, and computer are reserved for built-in sub-agents. -- evidence: [README.md#L238-L238](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L238-L238), [README.md#L226-L236](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L226-L236), [README.md#L224-L224](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L224-L224)
  - [observation/documented] A built-in computer sub-agent backed by agent-desktop performs host desktop automation on macOS via a snapshot-refs-action-snapshot workflow with tools like computer_snapshot, computer_click, computer_type, and computer_scroll; screenshots default to .grok/computer/. -- evidence: [README.md#L114-L119](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L114-L119), [README.md#L103-L103](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L103-L103)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The CLI supports headless runs via --prompt with options such as --directory, --max-tool-rounds, --format json, --batch-api, and --verify, plus session resume via --session latest or -s <session-id>. -- evidence: [README.md#L69-L76](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L69-L76), [README.md#L84-L87](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L84-L87)
  - [observation/documented] With --format json, headless output becomes a newline-delimited JSON event stream of semantic step-level events such as step_start, text, tool_use, step_finish, and error. -- evidence: [README.md#L97-L99](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L97-L99)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be resumed with 'grok --session latest' or 'grok -s <session-id>' (also in interactive mode), and /compact in the TUI compresses accumulated conversation history. -- evidence: [README.md#L453-L454](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L453-L454), [README.md#L84-L87](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L84-L87), [README.md#L89-L89](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L89-L89)
- orchestration (1 claim(s)):
  - [observation/documented] Sub-agents are on by default: foreground task delegation (e.g. explore, general, computer) plus background delegate for read-only deep dives. -- evidence: [README.md#L11-L11](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L11-L11), [README.md#L174-L189](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L174-L189)
- tools-permissions (1 claim(s)):
  - [observation/documented] Shell commands can run inside a Shuru microVM sandbox (--sandbox or /sandbox) isolating host filesystem and network; network is off by default with --allow-net/--allow-host controls, plus port forwards, resource limits, checkpoints, and secret injection. -- evidence: [README.md#L345-L349](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L345-L349), [README.md#L335-L335](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L335-L335), [README.md#L339-L339](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L339-L339)
- evaluation (1 claim(s)):
  - [inference/documented] No agent-performance benchmark or scored eval harness appears in the provided evidence; the --verify command produces build/run verification reports with screenshots and video, which is a runtime feature rather than a scored evaluation. -- evidence: [README.md#L355-L355](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L355-L355), [README.md#L362-L362](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L362-L362)
- dependencies (2 claim(s)):
More evidence: [full detail](grok-cli.detail.md)

Metadata and full claim list: [full detail](grok-cli.detail.md)
Human notes ([notes](grok-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
