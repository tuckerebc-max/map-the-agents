# Multi-Agent Features Guide

Hex now includes comprehensive multi-agent capabilities for tracking, analyzing, and visualizing agent execution.

## Features Overview

### 📊 Event-Sourcing

All agent activities are recorded to an event file for complete audit trails.

**Automatic Recording:**
- Session start/end
- Tool calls and results
- Agent spawn/terminate
- Errors and warnings

**Event File Location:**
```bash
# Enable debug mode to see event file location
HEX_DEBUG=1 hex -p "Your prompt"
# Output: 📊 Recording events to: /tmp/hex_events_20251208_143022.jsonl
```

### 💰 Cost Tracking

Automatic cost calculation based on Anthropic API pricing.

**Session Summary:**
```bash
hex -p "Analyze this codebase"
# ... execution ...
# 💰 Session Cost: $0.1234
#    Input tokens: 12500, Output tokens: 3200
```

**Per-Agent Breakdown:**
Use `hex visualize` with cost view to see cost by agent.

### 🔍 Visualization

**Tree View** - See agent hierarchy:
```bash
hex visualize /tmp/hex_events_*.jsonl --view tree
```

Output:
```
root
├── Task: "Analyze codebase"
├── Cost: $0.09
└── Duration: 2m 15s
  ├─ root.1
  │ ├── Task: "Search imports"
  │ ├── Cost: $0.04
  │ └── Duration: 45s
```

**Timeline View** - Chronological events:
```bash
hex visualize /tmp/hex_events_*.jsonl --view timeline
```

**Cost View** - Financial breakdown:
```bash
hex visualize /tmp/hex_events_*.jsonl --view cost
```

**HTML Export** - Interactive visualization:
```bash
hex visualize events.jsonl --html report.html
```

### 🔄 Event Replay

View event timeline:
```bash
hex replay /tmp/hex_events_*.jsonl
```

**Filtering:**
```bash
# Only events from specific agent
hex replay events.jsonl --agent root.1

# Only specific event types
hex replay events.jsonl --type ToolCall
```

### 🛡️ Process Management

**Graceful Shutdown:**
Press Ctrl+C to cleanly stop all child agents:
```
🛑 Interrupt received, shutting down gracefully...
```

All spawned processes are tracked and cleaned up properly.

## Environment Variables

- `HEX_DEBUG=1` - Show event file location and debug info
- `HEX_AGENT_ID` - Current agent identifier (auto-set)
- `HEX_MAX_AGENT_DEPTH` - Maximum agent recursion depth (default: 5)

## Examples

### Basic Session with Visualization

```bash
# Run a task
HEX_DEBUG=1 hex -p "Refactor this code using subagents"

# Note the event file location from output
# Example: /tmp/hex_events_20251208_143022.jsonl

# Visualize the execution tree
hex visualize /tmp/hex_events_20251208_143022.jsonl

# See the cost breakdown
hex visualize /tmp/hex_events_20251208_143022.jsonl --view cost

# Export to HTML
hex visualize /tmp/hex_events_20251208_143022.jsonl --html execution.html
```

### Analyzing Multi-Agent Performance

```bash
# Run complex task with multiple agents
hex -p "Analyze codebase, run tests, and create documentation"

# View event timeline
hex replay /tmp/hex_events_*.jsonl

# Filter to specific agent
hex visualize /tmp/hex_events_*.jsonl --agent root.2

# Check cost by agent
hex visualize /tmp/hex_events_*.jsonl --view cost
```

## Architecture

All features integrate seamlessly:

1. **Event Store** - Records all events to JSON Lines file
2. **Cost Tracker** - Calculates costs from API usage
3. **Process Registry** - Tracks parent-child relationships
4. **Visualization** - Renders events in multiple views

Events are recorded automatically without performance impact.
