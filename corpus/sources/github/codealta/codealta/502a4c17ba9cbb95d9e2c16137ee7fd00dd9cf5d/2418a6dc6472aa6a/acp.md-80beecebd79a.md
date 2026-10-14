# ACP integration

CodeAlta currently keeps the ACP protocol libraries (`src/CodeAlta.Acp` and `src/CodeAlta.Acp.Generator`) for future server-side integration work. The previous external ACP CLI provider adapter has been removed: the app no longer builds `src/CodeAlta.Agent.Acp`, launches ACP child processes, registers `acp:` model providers, exposes ACP management commands/dialogs, or reads `[acp]` provider definitions as active configuration.

Existing user `[acp]` configuration is intentionally ignored, not migrated or deleted. Config saves preserve existing `[acp]` and `[acp.*]` TOML blocks as compatibility data so users do not lose local notes or legacy provider definitions while the ACP path is unavailable.

## Future ACP server design note

Future ACP exposure should run in the opposite direction: CodeAlta can act as an ACP server adapter over the existing runtime and catalog instead of acting as a client to external ACP CLIs. A server adapter should:

- use `IAgentRuntime`/`SessionRuntimeService` as the single execution boundary for starting, steering, aborting, and observing sessions;
- use `IAgentSessionCatalog` for session discovery, load/resume, and metadata projection;
- map ACP requests/events to existing command/event contracts without introducing a second session owner;
- keep protocol serialization and generated model code in `CodeAlta.Acp`, with hosting/orchestration logic outside the TUI project;
- preserve existing permission, filesystem, terminal, and plugin boundaries rather than exposing host services directly from protocol handlers.

This note documents the intended direction only; it does not implement an ACP server.
