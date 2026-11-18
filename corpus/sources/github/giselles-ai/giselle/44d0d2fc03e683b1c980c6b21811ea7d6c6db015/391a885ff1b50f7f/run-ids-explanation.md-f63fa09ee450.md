# Run ID Types: `runId` vs `flowRunId`

This document clarifies the distinction between two important identifier types in the Giselle system.

## Overview

The Giselle system uses two distinct types of run identifiers that serve different purposes:

- **`runId`** (prefix: `rn-`) - Execution context identifier
- **`flowRunId`** (prefix: `flrn-`) - Flow instance identifier

## `runId` (Execution Context)

**Purpose**: Tracks execution context for tracing and generation origin

**Format**: `rn-{16 alphanumeric characters}`  
**Example**: `rn-1a2b3c4d5e6f7g8h`

### Key Characteristics:
- **Ephemeral**: Not stored in database
- **Tracing**: Used to track which execution triggered a generation
- **Context**: Passed through flow execution pipeline for debugging/analytics
- **Generation Origin**: Links generated content back to its source execution

### Usage Locations:
- Generation context tracking (`packages/data-type/src/generation/context.ts`)
- Flow execution context (`packages/giselle-engine/src/core/flows/run-flow.ts`)
- HTTP API validation (`packages/giselle-engine/src/http/router.ts`)
- Stage page execution (`apps/studio.giselles.ai/app/stage/page.tsx`)

## `flowRunId` (Flow Instance)

**Purpose**: Uniquely identifies a flow run instance with persistent storage

**Format**: `flrn-{16 alphanumeric characters}`  
**Example**: `flrn-9z8y7x6w5v4u3t2s`

### Key Characteristics:
- **Persistent**: Stored in database with indexing
- **Primary Key**: Main identifier for flow run objects
- **Storage**: Used in file system paths and database records
- **API**: Core to flow management endpoints
- **UI Integration**: Used in React hooks for flow control

### Usage Locations:
- Database schema (`apps/studio.giselles.ai/drizzle/schema.ts`)
- Flow run objects (`packages/giselle-engine/src/core/flows/run/object.ts`)
- Storage paths (`packages/giselle-engine/src/core/flows/run/paths.ts`)
- API endpoints (`packages/giselle-engine/src/http/router.ts`)
- UI hooks (`internal-packages/workflow-designer-ui/src/hooks/use-flow-controller.tsx`)

## Relationship

```
Execution Context (runId)
    ↓
Flow Instance (flowRunId)
    ↓
Database Storage & UI
```

- A single `runId` may trigger multiple flow instances
- Each flow instance gets a unique `flowRunId`
- `runId` provides execution tracing context
- `flowRunId` provides persistent flow management

## When to Use Which

### Use `runId` when:
- Tracking execution context
- Linking generations to their source
- Debugging flow execution
- Passing execution context through the pipeline

### Use `flowRunId` when:
- Storing flow run data
- Querying flow run status
- Managing flow runs via API
- Building UI components for flow control
- Creating storage paths

## Code Examples

### Creating IDs:
```typescript
// Create execution context ID
const runId = RunId.generate(); // "rn-1a2b3c4d5e6f7g8h"

// Create flow instance ID  
const flowRunId = FlowRunId.generate(); // "flrn-9z8y7x6w5v4u3t2s"
```

### Validation:
```typescript
// Validate execution context ID
const runIdResult = RunId.safeParse(inputId);

// Validate flow instance ID
const flowRunIdResult = FlowRunId.safeParse(inputId);
```

## Architecture Benefits

This dual-ID system provides:

1. **Clean Separation**: Different concerns handled by different IDs
2. **Traceability**: Execution context preserved through runId
3. **Persistence**: Flow instances managed via flowRunId
4. **Flexibility**: Can track multiple flow instances per execution
5. **Type Safety**: Distinct types prevent ID confusion