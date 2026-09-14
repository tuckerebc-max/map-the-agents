# maruakshay/miii-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0a712d9f2d68 @ 5960cfd3fa980381

## Summary (orientation draft, not independently verified)

README-documented product: miii is a local, offline terminal AI coding agent running on Ollama or OpenAI-compatible local servers, with built-in tools, permission modes, custom slash commands, sessions, output spill, and an miii doctor model grader; development commands are documented separately as contributor workflows.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] miii is a local terminal AI coding agent that runs against Ollama with no API keys or cloud, positioned as an offline alternative to cloud coding assistants. -- evidence: [README.md#L3-L7](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L3-L7), [README.md#L1-L1](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L1-L1)
- components (1 claim(s)):
  - [observation/documented] Built-in agent tools include read_file, write_file, edit_file, glob, grep, run_bash, and write_todos for tracking multi-step work. -- evidence: [README.md#L74-L82](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L74-L82)
- design-choices (2 claim(s)):
  - [observation/documented] Tool output over ~10K bytes is spilled to ~/.miii/output/<id>.txt with a head/tail preview inline; the model pages through the file with ranged reads and spill files are garbage-collected after 24 hours. -- evidence: [README.md#L209-L209](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L209-L209), [README.md#L217-L218](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L217-L218)
  - [observation/documented] The agent repairs malformed tool calls from small models and sizes its prompt to the model's context window, and a MIII.md file in the repo is read every turn to teach project conventions. -- evidence: [README.md#L58-L65](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L58-L65)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install && npm run dev, and use npm run build, npm run typecheck, npm test, and npm run eval (a regression gate powering miii doctor); npm run build && npm link runs the working tree as the global miii. -- evidence: [README.md#L236-L239](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L236-L239), [README.md#L248-L249](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L248-L249), [README.md#L241-L246](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L241-L246)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes slash commands (/plan, /permissions, /models, /sessions, /compact, /copy, /clear, /exit), a command palette on '/', and keyboard shortcuts such as Shift+Tab for permission modes and Ctrl+V for image paste. -- evidence: [README.md#L152-L164](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L152-L164), [README.md#L134-L150](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L134-L150)
  - [observation/documented] Custom slash commands are Markdown files in .miii/commands/ (project scope) or ~/.miii/commands/ (personal), supporting $ARGUMENTS and $1-$9 substitution, with project commands shadowing personal ones but never built-ins. -- evidence: [README.md#L126-L126](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L126-L126), [README.md#L117-L117](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L117-L117), [README.md#L128-L129](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L128-L129)
- memory-state (1 claim(s)):
  - [observation/documented] Saved approval rules live in .miii/permissions.json per project (with an optional global ~/.miii/permissions.json), and sessions can be saved and resumed via /new and /sessions. -- evidence: [README.md#L152-L164](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L152-L164), [README.md#L94-L94](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L94-L94)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] File tools reject ../ traversal and absolute paths outside the workspace, while run_bash is not path-confined and is bounded only by the permission prompt. -- evidence: [README.md#L84-L85](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L84-L85)
More evidence: [full detail](miii-cli.detail.md)

Metadata and full claim list: [full detail](miii-cli.detail.md)
Human notes ([notes](miii-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
