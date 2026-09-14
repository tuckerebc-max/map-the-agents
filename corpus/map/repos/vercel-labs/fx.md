# vercel-labs/fx

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e3ad6d8d645d @ 323053b52be3fa84

## Summary (orientation draft, not independently verified)

Evidence covers the README and CHANGELOG for fx, a Zig-based coding agent CLI, plus contributor instructions in AGENTS.md. Claims below describe the shipped CLI/agent product and its embedding SDK, with contributor guidance kept under workflows. Evidence coverage: 92 of 394 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] fx is a coding agent CLI written in Zig, distributed as a roughly 6.17 MiB native binary under the Apache-2.0 license, described as model-agnostic and embeddable. -- evidence: [README.md#L14-L14](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L14-L14), [README.md#L85-L85](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L85-L85)
- components (1 claim(s)):
  - [observation/documented] Extensibility comprises skills (reusable instructions loaded on invocation), MCP for connecting external tools and servers, and subagents for delegating independent work. -- evidence: [README.md#L62-L64](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L62-L64)
- design-choices (2 claim(s)):
  - [observation/documented] The interface is designed to stay closer to a Unix shell than an IDE in the terminal. -- evidence: [README.md#L14-L14](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L14-L14)
  - [observation/documented] Recent releases reduced the shell tool to three actions (down from twelve) and cut the subagent command surface to two commands, with Enter steering the active turn rather than queuing follow-ups. -- evidence: [CHANGELOG.md#L51-L58](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L51-L58)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source requires Zig 0.16.0+, tests run with `zig build test`, and AGENTS.md requires contributors to run the built binary end to end and pass full CI before declaring work ready. -- evidence: [README.md#L81-L81](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L81-L81), [README.md#L74-L79](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L74-L79), [README.md#L72-L72](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L72-L72), [AGENTS.md#L11-L15](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/AGENTS.md#L11-L15), [AGENTS.md#L7-L7](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/AGENTS.md#L7-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Users sign in via `fx login` (Vercel AI Gateway), `fx login codex` (ChatGPT/Codex OAuth), `fx login grok` (xAI OAuth), or `fx setup` with an AI Gateway API key. -- evidence: [README.md#L26-L29](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L26-L29)
  - [observation/documented] The CLI supports an interactive shell launched by running `fx` in a project, one-shot requests via `fx ask`, and `/help` inside the shell to browse interactive commands. -- evidence: [README.md#L44-L44](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L44-L44), [README.md#L31-L31](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L31-L31), [README.md#L33-L36](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L33-L36), [README.md#L40-L42](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L40-L42)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Subagents can run with their own model and reasoning effort, keep running while the user steers, and accept mid-task feedback without interrupting their current tool. -- evidence: [CHANGELOG.md#L15-L20](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L15-L20), [CHANGELOG.md#L7-L7](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L7-L7)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product has an auto mode that reviews each pending action, blocks cautioned or untrusted-output-derived actions, and supports full-access mode via `--full-access` or `/permissions full-access`. -- evidence: [CHANGELOG.md#L291-L298](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L291-L298), [CHANGELOG.md#L62-L74](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L62-L74), [CHANGELOG.md#L39-L41](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L39-L41)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](fx.detail.md)

Metadata and full claim list: [full detail](fx.detail.md)
Human notes ([notes](fx.notes.md), never overwritten by build)

[Back to map index](../../index.md)
