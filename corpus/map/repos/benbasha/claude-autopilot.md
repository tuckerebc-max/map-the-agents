# benbasha/claude-autopilot

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eaeea24d49bc @ da246a5f4d928dea

## Summary (orientation draft, not independently verified)

The snapshot documents Claude Autopilot v0.1.6, an MIT-licensed VS Code/Cursor extension that queues and automatically processes Claude Code tasks, with auto-resume on usage-limit resets, a mobile web interface, and a documented contributor workflow. Evidence is almost entirely README/CHANGELOG/COLLABORATION documentation; no source code slices are present.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Claude Autopilot is a VS Code extension (version 0.1.6, MIT licensed) for automated Claude Code task management, published on the VS Code Marketplace. -- evidence: [README.md#L7-L7](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L7-L7), [README.md#L3-L5](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L3-L5)
- components (1 claim(s)):
  - [observation/documented] Key components include a Queue Manager for message queueing and processing, a Claude Integration managing the Claude Code process, a Dependency Checker, and a Configuration System with validation. -- evidence: [README.md#L149-L152](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L149-L152)
- design-choices (1 claim(s)):
  - [observation/documented] The codebase follows a modular architecture with src/ directories for core, claude CLI integration, queue, services, ui, and utils, described as a separation of concerns. -- evidence: [README.md#L137-L145](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L137-L145), [README.md#L135-L135](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L135-L135)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors follow a guide covering fork/clone setup, npm install and compile, F5 Extension Development Host testing, a develop/feature branch strategy, and a PR checklist with tests, changelog, and version bump. -- evidence: [COLLABORATION.md#L53-L56](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L53-L56), [COLLABORATION.md#L15-L29](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L15-L29), [COLLABORATION.md#L194-L199](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L194-L199), [COLLABORATION.md#L59-L64](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L59-L64), [COLLABORATION.md#L66-L71](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L66-L71)
  - [observation/documented] Repository development practice: TypeScript strict mode, interface-first typing, camelCase/PascalCase/SCREAMING_SNAKE_CASE naming conventions, and JSDoc for public APIs are the stated coding standards. -- evidence: [COLLABORATION.md#L117-L124](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L117-L124)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The extension exposes Command Palette commands such as Claude: Start/Stop Claude Autopilot, Add Message to Queue, and Start/Stop Web Interface plus a QR-code display command. -- evidence: [README.md#L74-L81](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L74-L81)
  - [observation/documented] A webview UI manages queues and shows real-time progress via WebSocket, and a mobile web interface with QR-code access supports remote control, history browsing, and filtering. -- evidence: [README.md#L42-L47](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L42-L47)
- memory-state (1 claim(s)):
  - [observation/documented] Each VS Code workspace maintains its own persistent message queue and processing history, allowing independent management of multiple projects. -- evidence: [README.md#L222-L222](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L222-L222), [README.md#L236-L236](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L236-L236), [README.md#L226-L226](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L226-L226)
- orchestration (1 claim(s)):
  - [observation/documented] When Claude Code hits usage limits, the extension detects it and schedules the queue to auto-resume when limits reset, including parsing of 'X-hour limit reached' reset messages. -- evidence: [CHANGELOG.md#L12-L14](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/CHANGELOG.md#L12-L14), [README.md#L224-L224](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L224-L224)
- tools-permissions (1 claim(s)):
  - [observation/documented] The tool can run Claude Code with --dangerously-skip-permissions for automation; documentation says it should be used only in trusted environments and disabled for sensitive data, with a skipPermissions setting. -- evidence: [README.md#L272-L274](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L272-L274), [README.md#L156-L159](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L156-L159), [README.md#L97-L103](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L97-L103)
More evidence: [full detail](claude-autopilot.detail.md)

Metadata and full claim list: [full detail](claude-autopilot.detail.md)
Human notes ([notes](claude-autopilot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
