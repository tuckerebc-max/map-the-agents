# Amplify WebSocket Workflow Configuration

This document provides a comprehensive breakdown of the AWS Amplify WebSocket workflow implementation in this project, including file paths, message formats, connection management, and overall architecture.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Key Components](#key-components)
- [Connection Flow](#connection-flow)
- [Message Format](#message-format)
- [Frontend WebSocket Management](#frontend-websocket-management)
- [Backend Implementation](#backend-implementation)
- [GraphQL Schema](#graphql-schema)
- [Trace Data Processing](#trace-data-processing)
- [Error Handling & Retry Logic](#error-handling--retry-logic)
- [Agent Workflow Visualization](#agent-workflow-visualization)

## Architecture Overview

The WebSocket implementation uses AWS AppSync subscriptions over GraphQL for bi-directional communication between the frontend and backend. This enables real-time communication for chat messages and agent trace data, powering the interactive agent workflow visualization.

Key features:
- Real-time streaming of Bedrock Agent responses
- Trace data transfer for agent visualization
- Connection management with automatic retries
- Subscription-based message delivery

## Key Components

### Frontend Files

| File | Path | Purpose |
|------|------|---------|
| WebSocket Manager | `src/frontend/src/utilities/multiWebsocket.ts` | Core WebSocket management utility |
| Chat Component | `src/frontend/src/pages/Home/Chat/index.tsx` | Main chat interface with WebSocket subscription |
| Agent Trace Storage | `src/frontend/src/utilities/agentTraceStorage.ts` | Stores and manages agent trace data |
| Trace Parser | `src/frontend/src/utilities/traceParser.ts` | Parses trace data from WebSocket messages |

### Backend Files

| File | Path | Purpose |
|------|------|---------|
| API Stack | `src/backend/lib/stacks/backend/streaming-api/index.ts` | AppSync API infrastructure configuration |
| GraphQL Schema | `src/backend/lib/stacks/backend/streaming-api/schema.graphql` | Defines subscription and mutation types |
| Lambda Function | `src/backend/lib/stacks/backend/streaming-api/resolver-function/index.ts` | Backend resolver handling requests |
| GraphQL Mutations | `src/backend/lib/stacks/backend/streaming-api/resolver-function/mutations.ts` | GraphQL mutation definitions |

## Connection Flow

1. **Connection Establishment**:
   - Frontend generates a session ID using UUID
   - `connectWebSocket()` function creates a WebSocket connection
   - Connection URL is determined based on environment (development vs production)
   - Connection includes session ID in the path for user identification

2. **Connection Message**:
   ```json
   {
     "type": "connect",
     "sessionId": "[UUID]",
     "modelId": "[optional model ID]",
     "timestamp": 1234567890
   }
   ```

3. **Connection Management**:
   - Connections stored by unique connection ID (combining session ID and model ID)
   - Maximum of 3 retry attempts with exponential backoff
   - 5-second connection timeout
   - Heartbeat checks to detect disconnections

## Message Format

### User Message (Frontend to Backend)

The frontend sends chat messages through a GraphQL mutation:

```graphql
mutation SendChat(
  $sessionId: String!
  $human: String!
  $sessionAttributes: AWSJSON
) {
  sendChat(
    sessionId: $sessionId
    human: $human
    sessionAttributes: $sessionAttributes
  )
}
```

### Assistant Message (Backend to Frontend)

Response messages use GraphQL subscriptions with this structure:

```json
{
  "onUpdateChat": {
    "assistant": "Message content from the assistant",
    "trace": "[JSON trace data or string]"
  }
}
```

### Trace Data Format

Trace data can be in multiple formats:
- JSON object directly in `onUpdateChat.trace`
- String that needs JSON parsing
- Object with collaborator metadata

Example trace structure:
```json
{
  "collaboratorName": "AgentName",
  "agentId": "agent-identifier",
  "tasks": [
    {
      "stepNumber": 1,
      "title": "Processing request",
      "content": "Task details",
      "timestamp": 1234567890
    }
  ]
}
```

## Frontend WebSocket Management

File: `src/frontend/src/utilities/multiWebsocket.ts`

### Key Functions

1. **Connection Management**:
   - `generateConnectionId(sessionId, modelId)`: Creates a stable connection identifier
   - `connectWebSocket(sessionId, modelId, onConnect)`: Establishes WebSocket connection
   - `isWebSocketConnected()`: Checks if any WebSocket connections are open

2. **Message Handling**:
   - `registerMessageHandler(connectionId, type, handler)`: Registers message callback
   - `unregisterMessageHandler(connectionId, type, handler)`: Removes message handler
   - `parseTraceData(data)`: Extracts and parses trace data from messages

### Connection States

- `WebSocket.CONNECTING` (0): Connection in progress
- `WebSocket.OPEN` (1): Connection established
- `WebSocket.CLOSING` (2): Connection closing
- `WebSocket.CLOSED` (3): Connection closed

## Backend Implementation

File: `src/backend/lib/stacks/backend/streaming-api/index.ts`

The backend stack uses:
- AWS AppSync for GraphQL API
- Cognito user pools for authentication
- Lambda resolver for processing requests and invoking Bedrock agents

### Lambda Resolver Flow

File: `src/backend/lib/stacks/backend/streaming-api/resolver-function/index.ts`

1. **Request Processing**:
   - Receives the `sendChat` mutation from frontend
   - Extracts `sessionId`, `human` (message), and optional `sessionAttributes`
   - Gets user identity from Cognito

2. **Bedrock Agent Invocation**:
   - Invokes Bedrock Agent with user message
   - Sets `enableTrace` to true for collecting trace data
   - Configures streaming for chunked responses

3. **Response Streaming**:
   - Creates initial chat record in DynamoDB
   - Processes agent response chunks asynchronously
   - For each chunk:
     - Decodes the response bytes
     - Updates chat record with latest response and trace data
     - Updates are sent to frontend via subscription

## GraphQL Schema

File: `src/backend/lib/stacks/backend/streaming-api/schema.graphql`

### Type Definitions

```graphql
type Chat @model @auth(rules: [{ allow: owner, ownerField: "userId", identityClaim: "sub" }]) {
    userId: ID
    sessionId: String! @index(name: "bySessionId")
    human: String
    assistant: String
    trace: AWSJSON
    expiration: AWSTimestamp
}

type Session @model @auth(rules: [{ allow: owner, ownerField: "userId", identityClaim: "sub" }]) {
    userId: ID
    chats: [Chat] @hasMany(indexName: "bySessionId")
    expiration: AWSTimestamp
}

type Mutation {
    sendChat(sessionId: String!, human: String!, sessionAttributes: AWSJSON): String
        @aws_cognito_user_pools
}
```

The schema includes:
- `Chat` model to store individual messages
- `Session` model to group related chats
- Custom `sendChat` mutation accepting user message
- Built-in subscriptions (generated by Amplify)

## Trace Data Processing

File: `src/frontend/src/pages/Home/Chat/index.tsx`

Trace data processing flow:
1. WebSocket receives message with trace data
2. `parseTraceData()` extracts and normalizes trace object
3. `handleTraceMessage()` processes trace into structured format
4. Trace is organized into "trace groups" by agent/collaborator
5. Each trace group contains tasks and subtasks with timing info
6. Agent flow visualization uses trace data to animate nodes

### TraceGroup Structure

```typescript
interface TraceGroup {
  id: string;
  type: 'trace-group';
  sender: 'bot';
  dropdownTitle: string;
  agentId: string;
  originalAgentType: string;
  tasks: Array<{
    stepNumber: number;
    title: string;
    content: string;
    timestamp: number;
    subTasks?: Array<{
      stepNumber: number;
      title: string; 
      content: string;
      timestamp: number;
    }>;
  }>;
  startTime: number;
  lastUpdateTime: number;
}
```

## Error Handling & Retry Logic

- **Connection Errors**:
  - Maximum 3 retries with exponential backoff
  - 5-second connection timeout
  - Failure logging and state management
  
- **Message Processing Errors**:
  - Error boundaries for trace processing
  - Fallback to graceful degradation when trace parsing fails
  - Lambda timeout handling with flashbar notifications

## Agent Workflow Visualization

File: `src/frontend/src/common/components/react_flow/AgentFlowPanel.tsx`

The WebSocket trace data powers the interactive agent workflow visualization:

1. WebSocket delivers trace data via subscription
2. Custom events (`agentTraceEvent`, `agentNodeUpdate`) transmit data to flow components
3. Trace data activates nodes in the flow diagram
4. Agent nodes animate based on processing status
5. Completion events update the entire workflow

### Key Events

- `agentTraceEvent`: General trace notifications
- `agentNodeUpdate`: Updates specific node with trace data
- `agentProcessingUpdate`: Changes node processing state
- `agentNodeSelected`: Triggered when user selects node in diagram

### Node Mapping

Agent traces are mapped to flow nodes using the collaborator name:
```typescript
const nodeMapping: Record<string, string> = {
  'OrderManagement': 'order-mgmt-agent',
  'ProductRecommendation': 'product-rec-agent',
  'Personalization': 'personalization-agent',
  'Troubleshoot': 'ts-agent',
  'ROUTING_CLASSIFIER': 'routing-classifier',
  'Supervisor': 'supervisor-agent'
};
```

---

This documentation provides a comprehensive overview of the Amplify WebSocket implementation in this project. For detailed implementation, refer to the specific files mentioned throughout this document.
