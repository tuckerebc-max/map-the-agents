# oli Server API Reference

This document provides comprehensive documentation for the oli server JSON-RPC API.
The oli server can be integrated with any client that supports JSON-RPC 2.0 over stdio.
The API allows for interaction with various language models, task management, and event
notifications.

## API Overview

The oli server implements a JSON-RPC 2.0 API over stdio. All communication follows the
JSON-RPC standard with method calls and event notifications.

### Connection and Communication

The server reads JSON-RPC requests from stdin and writes responses to stdout. Each request and response is a single-line JSON object.

## API Methods

### Model Interaction

#### `run`

Send a prompt to the LLM model and get a response. This runs the agent to process your query.

**Parameters:**
- `prompt` (string, required): The prompt to send to the model
- `model_index` (number, optional): Index of the model to use (defaults to 0)
- `use_agent` (boolean, optional): Whether to use agent mode (defaults to current setting)

**Returns:**
- `response` (string): The model's response

**Events:**
- `processing_started`: Emitted when processing begins
- `processing_progress`: Emitted during processing (when in agent mode)
- `processing_complete`: Emitted when processing completes
- `processing_error`: Emitted if an error occurs

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "run",
  "params": {
    "prompt": "Write a function to calculate Fibonacci numbers",
    "model_index": 0,
    "use_agent": true
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "response": "Here's a function to calculate Fibonacci numbers..."
  }
}
```

### Agent Control

#### `set_agent_mode`

Enable or disable agent mode for model interactions.

**Parameters:**
- `use_agent` (boolean, required): Whether to enable agent mode

**Returns:**
- `success` (boolean): Whether the operation was successful
- `agent_mode` (boolean): The current agent mode setting

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "set_agent_mode",
  "params": {
    "use_agent": true
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "success": true,
    "agent_mode": true
  }
}
```

### Model Discovery

#### `get_available_models`

Get a list of available models.

**Parameters:** None

**Returns:**
- `models` (array): List of available models with their details
  - `name` (string): Human-readable model name
  - `id` (string): Model identifier
  - `description` (string): Model description
  - `supports_agent` (boolean): Whether the model supports agent mode

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "get_available_models",
  "params": {}
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "models": [
      {
        "name": "Claude 3.5 Sonnet",
        "id": "claude-3-5-sonnet-20240307",
        "description": "Claude 3.5 Sonnet by Anthropic",
        "supports_agent": true
      },
      {
        "name": "GPT-4o",
        "id": "gpt-4o",
        "description": "GPT-4o by OpenAI",
        "supports_agent": true
      }
    ]
  }
}
```

### Task Management

#### `get_tasks`

Get a list of tasks and their statuses.

**Parameters:** None

**Returns:**
- `tasks` (array): List of tasks with their details
  - `id` (string): Task identifier
  - `description` (string): Task description
  - `status` (string): Current status (in_progress, completed, failed)
  - `tool_count` (number): Number of tools used
  - `input_tokens` (number): Input token count
  - `output_tokens` (number): Output token count
  - `created_at` (number): Unix timestamp when task was created

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "get_tasks",
  "params": {}
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tasks": [
      {
        "id": "task-123",
        "description": "Write a function to calculate Fibonacci numbers",
        "status": "completed",
        "tool_count": 2,
        "input_tokens": 128,
        "output_tokens": 256,
        "created_at": 1687654321
      }
    ]
  }
}
```

#### `cancel_task`

Cancel a running task.

**Parameters:**
- `task_id` (string, optional): ID of the task to cancel (cancels the current task if omitted)

**Returns:**
- `success` (boolean): Whether the operation was successful
- `message` (string): Status message

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "cancel_task",
  "params": {
    "task_id": "task-123"
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "success": true,
    "message": "Task canceled"
  }
}
```

### Conversation Management

#### `clear_conversation`

Clear the conversation history.

**Parameters:** None

**Returns:**
- `success` (boolean): Whether the operation was successful
- `message` (string): Status message

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "clear_conversation",
  "params": {}
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "success": true,
    "message": "Conversation history cleared"
  }
}
```

### System Information

#### `get_version`

Get the server version.

**Parameters:** None

**Returns:**
- `version` (string): Server version

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "get_version",
  "params": {}
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "version": "0.1.0"
  }
}
```

## Event Notifications

The server sends event notifications to clients to report status changes and progress updates.

### Subscription Management

#### `subscribe`

Subscribe to events of a specific type.

**Parameters:**
- `event_type` (string, required): The type of event to subscribe to

**Returns:**
- `subscription_id` (number): Unique identifier for the subscription

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "subscribe",
  "params": {
    "event_type": "processing_progress"
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "subscription_id": 42
  }
}
```

#### `unsubscribe`

Unsubscribe from events of a specific type.

**Parameters:**
- `event_type` (string, required): The type of event to unsubscribe from
- `subscription_id` (number, required): The subscription ID to unsubscribe

**Returns:**
- `success` (boolean): Whether the operation was successful

**Example:**
```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "unsubscribe",
  "params": {
    "event_type": "processing_progress",
    "subscription_id": 42
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "success": true
  }
}
```

### Event Types

#### `processing_started`

Emitted when the server starts processing a model query.

```json
{
  "jsonrpc": "2.0",
  "method": "processing_started",
  "params": {
    "model_index": 0,
    "use_agent": true
  }
}
```

#### `processing_progress`

Emitted during processing to provide progress updates (primarily in agent mode).

```json
{
  "jsonrpc": "2.0",
  "method": "processing_progress",
  "params": {
    "task_id": "task-123",
    "message": "Searching for files..."
  }
}
```

#### `processing_complete`

Emitted when processing is complete.

```json
{
  "jsonrpc": "2.0",
  "method": "processing_complete",
  "params": {}
}
```

#### `processing_error`

Emitted when an error occurs during processing.

```json
{
  "jsonrpc": "2.0",
  "method": "processing_error",
  "params": {
    "error": "API rate limit exceeded"
  }
}
```

#### `tool_status`

Emitted when a tool's status changes (started, updated, completed).

```json
{
  "jsonrpc": "2.0",
  "method": "tool_status",
  "params": {
    "type": "started",
    "execution": {
      "id": "tool-View-abc123",
      "task_id": "task-123",
      "name": "View",
      "status": "running",
      "start_time": 1687654321000,
      "end_time": null,
      "message": "Reading file",
      "metadata": {
        "file_path": "/path/to/file.js",
        "description": "Reading file"
      }
    }
  }
}
```

## Integration Examples

### Basic Client Implementation

```typescript
import { spawn } from 'child_process';
import { v4 as uuidv4 } from 'uuid';

class oliClient {
  private process;
  private messageCallbacks = new Map();
  private eventListeners = new Map();
  private nextId = 1;

  constructor() {
    this.process = spawn('./oli_server', [], {
      stdio: ['pipe', 'pipe', 'inherit']
    });

    this.process.stdout.on('data', (data) => {
      const messages = data.toString().trim().split('\n');
      for (const msg of messages) {
        try {
          const parsed = JSON.parse(msg);
          if (parsed.id) {
            // This is a response to a request
            const callback = this.messageCallbacks.get(parsed.id);
            if (callback) {
              callback(parsed);
              this.messageCallbacks.delete(parsed.id);
            }
          } else if (parsed.method) {
            // This is an event notification
            const listeners = this.eventListeners.get(parsed.method) || [];
            for (const listener of listeners) {
              listener(parsed.params);
            }
          }
        } catch (e) {
          console.error('Failed to parse JSON:', e);
        }
      }
    });
  }

  async callMethod(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.nextId++;
      const request = {
        jsonrpc: '2.0',
        id,
        method,
        params
      };

      this.messageCallbacks.set(id, (response) => {
        if (response.error) {
          reject(new Error(response.error.message));
        } else {
          resolve(response.result);
        }
      });

      this.process.stdin.write(JSON.stringify(request) + '\n');
    });
  }

  on(eventType, callback) {
    if (!this.eventListeners.has(eventType)) {
      this.eventListeners.set(eventType, []);
    }
    this.eventListeners.get(eventType).push(callback);

    // Subscribe to this event type
    this.callMethod('subscribe', { event_type: eventType })
      .catch(e => console.error(`Failed to subscribe to ${eventType}:`, e));
  }

  async run(prompt, modelIndex = 0, useAgent = true) {
    return this.callMethod('run', {
      prompt,
      model_index: modelIndex,
      use_agent: useAgent
    });
  }

  async getAvailableModels() {
    return this.callMethod('get_available_models');
  }

  async clearConversation() {
    return this.callMethod('clear_conversation');
  }

  close() {
    this.process.kill();
  }
}

// Example usage
async function main() {
  const client = new oliClient();

  // Listen for events
  client.on('processing_progress', (params) => {
    console.log('Progress:', params.message);
  });

  client.on('tool_status', (params) => {
    console.log('Tool status:', params.type, params.execution.name);
  });

  try {
    // Get available models
    const models = await client.getAvailableModels();
    console.log('Available models:', models);

    // Run the model
    const result = await client.run('Write a function to calculate the factorial of a number');
    console.log('Result:', result.response);
  } catch (e) {
    console.error('Error:', e);
  } finally {
    client.close();
  }
}

main();
```

## Error Handling

The server follows the JSON-RPC 2.0 specification for error handling. Errors are returned as objects with code, message, and optional data fields.

### Standard Error Codes

- `-32700`: Parse error - Invalid JSON was received
- `-32600`: Invalid Request - The JSON sent is not a valid Request object
- `-32601`: Method not found - The method does not exist / is not available
- `-32602`: Invalid params - Invalid method parameter(s)
- `-32603`: Internal error - Internal JSON-RPC error
- `-32000` to `-32099`: Server error - Implementation-defined server errors

## Security Considerations

- The oli server should be treated as a trusted component in your application architecture
- No built-in authentication is provided; the client is responsible for security
- Consider running the server in a sandboxed environment for additional security
- API keys for language models are passed via environment variables

## Extending the API

The oli server can be extended with additional methods by modifying the main.rs file and registering new API methods. This allows for customization to support specific use cases like language server protocol integration or MCP server capabilities.
