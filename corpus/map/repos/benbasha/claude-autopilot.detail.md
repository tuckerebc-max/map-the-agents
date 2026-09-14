# benbasha/claude-autopilot -- full detail

[Back to orientation](claude-autopilot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/benbasha/claude-autopilot/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/da246a5f4d928dea.json](../../../wiki/dossiers/benbasha/claude-autopilot/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/da246a5f4d928dea.json)

## specifications (1 claim(s))

- [observation/documented] Claude Autopilot is a VS Code extension (version 0.1.6, MIT licensed) for automated Claude Code task management, published on the VS Code Marketplace. -- evidence: [README.md#L7-L7](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L7-L7), [README.md#L3-L5](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L3-L5) (`clm_b1fd25417518d3c69578b1a584346d4eee37e07d5ad76d65f0c35a8409636020`)

## components (1 claim(s))

- [observation/documented] Key components include a Queue Manager for message queueing and processing, a Claude Integration managing the Claude Code process, a Dependency Checker, and a Configuration System with validation. -- evidence: [README.md#L149-L152](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L149-L152) (`clm_71559255ef2fe78f4efab7771752f88f71f52b4c11c2dc494fd4b745710c7711`)

## design-choices (1 claim(s))

- [observation/documented] The codebase follows a modular architecture with src/ directories for core, claude CLI integration, queue, services, ui, and utils, described as a separation of concerns. -- evidence: [README.md#L137-L145](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L137-L145), [README.md#L135-L135](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L135-L135) (`clm_10d3250b779c2dab44548b2bf1c3f7be834a2ff1b79e46d0aa6a2ca0fa917f4c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors follow a guide covering fork/clone setup, npm install and compile, F5 Extension Development Host testing, a develop/feature branch strategy, and a PR checklist with tests, changelog, and version bump. -- evidence: [COLLABORATION.md#L53-L56](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L53-L56), [COLLABORATION.md#L15-L29](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L15-L29), [COLLABORATION.md#L194-L199](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L194-L199), [COLLABORATION.md#L59-L64](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L59-L64), [COLLABORATION.md#L66-L71](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L66-L71) (`clm_65fcd41b4618018a51cb5cf791e973f0ec7b9dd84db997023e4be123ec312e0f`)
- [observation/documented] Repository development practice: TypeScript strict mode, interface-first typing, camelCase/PascalCase/SCREAMING_SNAKE_CASE naming conventions, and JSDoc for public APIs are the stated coding standards. -- evidence: [COLLABORATION.md#L117-L124](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/COLLABORATION.md#L117-L124) (`clm_0108e81bf7acb9d8448f275fd2c19062f4c5f9e572087365d0361a5f179c64e3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The extension exposes Command Palette commands such as Claude: Start/Stop Claude Autopilot, Add Message to Queue, and Start/Stop Web Interface plus a QR-code display command. -- evidence: [README.md#L74-L81](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L74-L81) (`clm_b96080879e3f57a0cd85cdc1a888b3d923c5b869c7d9da105082a3b84079c1a9`)
- [observation/documented] A webview UI manages queues and shows real-time progress via WebSocket, and a mobile web interface with QR-code access supports remote control, history browsing, and filtering. -- evidence: [README.md#L42-L47](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L42-L47) (`clm_6068639f9fd51b9cc5fcc39189ac80101c2bb2a198cb6b7cd5eccf070473a208`)

## memory-state (1 claim(s))

- [observation/documented] Each VS Code workspace maintains its own persistent message queue and processing history, allowing independent management of multiple projects. -- evidence: [README.md#L222-L222](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L222-L222), [README.md#L236-L236](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L236-L236), [README.md#L226-L226](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L226-L226) (`clm_6004fc8ac3f9726a8ef2f510eee801584fe35e1bb5292f693473e73e9e25d44f`)

## orchestration (1 claim(s))

- [observation/documented] When Claude Code hits usage limits, the extension detects it and schedules the queue to auto-resume when limits reset, including parsing of 'X-hour limit reached' reset messages. -- evidence: [CHANGELOG.md#L12-L14](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/CHANGELOG.md#L12-L14), [README.md#L224-L224](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L224-L224) (`clm_7d1f459e4e67bf8ee23c52ad1cf89cfb9a549be55001139623ed604347d65fe6`)

## tools-permissions (1 claim(s))

- [observation/documented] The tool can run Claude Code with --dangerously-skip-permissions for automation; documentation says it should be used only in trusted environments and disabled for sensitive data, with a skipPermissions setting. -- evidence: [README.md#L272-L274](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L272-L274), [README.md#L156-L159](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L156-L159), [README.md#L97-L103](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L97-L103) (`clm_50a327e66ecb1aa9cac04bc3e113a831b38dd7c9fdd65cf45ac4f22f94493660`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Claude Code installed and on PATH, Python 3.8+ for process management, and VS Code 1.74.0+ or Cursor; the extension validates these dependencies before starting. -- evidence: [README.md#L53-L55](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L53-L55), [README.md#L228-L228](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/README.md#L228-L228) (`clm_9c2f18f00e6e3f1c4e67ff5bf36bbd772c3604e99e7f8889975220ed18004ef3`)

## limitations (1 claim(s))

- [inference/documented] The changelog lists a comprehensive test suite as a planned future enhancement, suggesting the project likely lacked a full automated test suite at the documented releases. -- evidence: [CHANGELOG.md#L289-L296](https://github.com/benbasha/Claude-Autopilot/blob/eaeea24d49bc9ccdeb63faee181fab99619d7a3f/CHANGELOG.md#L289-L296) (`clm_3995555fb0f9345cee5b6bc89a1dbea845a08c32a8de2200c1ab7b6f4e43650a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

