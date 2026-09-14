# Ourocodus - Product Requirements Document

## Overview

Ourocodus is an infrastructure system for orchestrating AI coding agents to build software from ideas. Users provide a high-level concept, and the system decomposes it into manageable chunks, coordinates AI agents to develop each chunk through iterative PR-based workflows, and validates the resulting software through automated testing and evaluation.

## Vision

Enable anyone to transform ideas into working software through AI agent orchestration, with human guidance at critical decision points.

## Core Principles

1. **Ruthlessly simple** - Use existing tools, build only necessary glue logic
2. **Clean separation** - Infrastructure layer is generic, orchestration layer is domain-specific
3. **Human-in-the-loop** - Approval gates at key phases
4. **Pragmatic** - Start sequential, architect for parallel
5. **Greenfield POC** - Validate approach before scaling complexity

## Target Users

- Developers wanting AI assistance on existing projects (future)
- Product managers validating ideas through rapid prototyping
- Technical founders building MVPs
- **POC focus:** Technical users comfortable with CLI/local deployment

## Core Workflow (Long-term Vision)

**Note:** Phase 1 validates concurrent agent communication. Sequential workflow comes in Phase 3.

```text
User Idea
    ↓
[Decomposition Phase]
    ↓
Hierarchical breakdown with user Q&A
    ↓
[Development Phase - Can be Sequential or Concurrent]
    ↓
Concurrent agents work on different aspects:
  → Agent 1 (auth) works on authentication
  → Agent 2 (db) works on database
  → Agent 3 (tests) writes tests
  ↓ (with approval gates at merge points)
    ↓
[Evaluation Phase]
  → Run completed software
  → Specialized agents evaluate (performance, security, UX)
  → Report findings
```text

**Phase 1 Reality:** Multiple agents work concurrently (no hard limit), user directs each manually via WebSocket
**Phase 3+:** Coordinator automates workflow, can be sequential or parallel based on dependencies

## System Architecture

### Infrastructure Layer (Generic, Reusable)

**Purpose:** Message routing, container orchestration, workspace management

**Components:**

- **NATS** - Message bus (external dependency)
- **Docker** - Container runtime (external dependency)
- **API Server** (Go) - HTTP control plane
- **Git** - Worktree management (direct commands)
- **Event Log** - Structured logging (stdout/file)

**Key Characteristic:** Zero knowledge of "coding agents" or "development workflows"

### Orchestration Layer (Development-Specific)

**Purpose:** Drive software development workflow

**Components:**

- **Coordinator** (Go) - Workflow driver, reads graph, sends ACP messages via relay
- **ACP Relay** - Routes ACP protocol messages between coordinator and agent containers
- **Agent Containers** - Run Claude Code, OpenAI Codex, etc. (existing ACP servers)
- **Graph Definition** (YAML) - Workflow specification
- **Approvals** - Blocking mechanism (HTTP endpoint or stdin)

## Technical Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Services (API, Coordinator, CLI) | **Go** | Single language, static binaries, excellent stdlib |
| Messaging | **NATS** | Mature pub/sub, minimal config, built-in observability |
| Containers | **Docker** | Standard, rootless mode available |
| **AI Agents** | **Claude Code, OpenAI Codex** (via ACP) | Existing ACP servers do the work |
| Protocol | **ACP (Agent Client Protocol)** | Zed/Google protocol for AI agents |
| UI | **Vanilla JS or minimal React** | Keep frontend simple |
| Storage | **JSON logs + optional SQLite** | Start simple, upgrade if needed |

## POC Scope

### Must Have (POC Validation)

1. **Message routing** - NATS topics route messages between components
2. **Agent lifecycle** - Launch agent in Docker, connect to NATS, process work
3. **Basic workflow** - Coordinator sends work, agent responds, results logged
4. **Observability** - Web UI shows message log and agent status
5. **Human control** - CLI can send messages, trigger agents
6. **Single chunk** - Hardcoded workflow for one development chunk

### Explicitly Deferred

- Full graph engine (hardcode one chunk for POC)
- Multiple agents per chunk (one agent processes work end-to-end)
- Error recovery (manual restart acceptable)
- Parallel execution (sequential only)
- PRD decomposition engine (manual workflow definition)
- GitHub integration (local git only)

### Success Criteria

POC is successful if:

1. User can start system locally (`make run`)
2. User can submit work via CLI
3. Agent processes work in isolated container
4. Results appear in web UI
5. Event log captures all interactions
6. System demonstrates clean boundaries (infrastructure usable for non-dev workflows)

## Directory Structure

**Phase 1 (Current):**
```text
ourocodus/
  cmd/
    relay/        # WebSocket relay server (implemented)
    cli/          # CLI tool (implemented)
    echo-agent/   # Test agent (implemented)
  pkg/
    relay/        # Relay implementation
    acp/          # ACP protocol client
  scripts/
    demo/         # Interactive demos
    smoketest/    # Integration tests
  docs/
    prd/          # Component PRDs
    PROTOCOLS.md
    ACP.md
    SESSION_LIFECYCLE.md
    ERROR_HANDLING.md
```

**Long-term (Planned):**
```text
Additional components:
  cmd/
    api/          # HTTP API server
    coordinator/  # Workflow driver
  pkg/
    nats/         # NATS client wrapper
    graph/        # YAML graph parser
    events/       # Event logging
  containers/
    claude-code/  # Dockerfile for Claude Code
  config/
    graph.yaml    # Workflow definition
  web/
    index.html    # PWA frontend
```

## Non-Goals (For POC)

- Production deployment (Docker Compose acceptable)
- Authentication/authorization
- Multi-tenancy
- Distributed execution
- Advanced error recovery
- Metrics/monitoring beyond basic logging
- CI/CD integration
- Cost optimization

## Future Directions (Post-POC)

1. **Parallel execution** - Graph engine schedules independent chunks simultaneously
2. **Autonomous mode** - Remove approval gates, let agents self-coordinate
3. **PRD generation** - LLM-assisted decomposition from user ideas
4. **GitHub integration** - Automated PR creation
5. **Multi-agent collaboration** - Real-time cooperation on same chunk
6. **Persistent sessions** - Resume after coordinator restart

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| NATS adds complexity | Medium | Well-documented, single binary, can replace with Redis if needed |
| Docker overhead | Low | Rootless mode reduces security concerns, acceptable for POC |
| Agent cost (API calls) | Medium | Implement token limits, use caching |
| State management complexity | High | Start with event sourcing, add snapshots only if startup slow |
| Scope creep | High | Ruthlessly defer non-essentials, document for post-POC |

## Open Questions

1. Approval mechanism: HTTP endpoint vs stdin vs web UI button?
2. Event log: When to migrate from files to SQLite?
3. Agent isolation: One container per agent or reuse containers?
4. NATS deployment: Embedded or external service?
5. Graph definition: How much expressiveness needed for POC?

## Timeline Estimate

**Phase 1: Infrastructure (Week 1)**

- NATS integration
- Docker agent launcher
- API server skeleton
- Event logging

**Phase 2: Basic Orchestration (Week 2)**

- Coordinator implementation
- Simple graph parser
- Agent scaffold (echo service)

**Phase 3: Real Agent (Week 3)**

- Anthropic API integration
- Git worktree setup
- Agent processes real coding tasks

**Phase 4: UI & Polish (Week 4)**

- Web UI for monitoring
- CLI improvements
- Documentation

**Total: ~4 weeks for working POC**

## References

- [API Server PRD](./docs/prd/api.md)
- [Coordinator PRD](./docs/prd/coordinator.md)
- [CLI PRD](./docs/prd/cli.md)
- [Relay PRD](./docs/prd/relay.md)
