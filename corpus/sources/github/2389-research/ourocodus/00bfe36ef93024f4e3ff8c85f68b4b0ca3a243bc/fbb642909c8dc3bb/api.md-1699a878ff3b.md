# API Server - Product Requirements Document

## Purpose

HTTP control plane for Ourocodus system. Provides REST endpoints for session management, agent lifecycle, and system observability.

## Responsibilities

1. Session lifecycle management (create, list, stop)
2. Agent status queries
3. Event log access (tail, filter)
4. System health checks
5. Serve static web UI files

## Non-Responsibilities

- Message routing (NATS handles this)
- Workflow orchestration (Coordinator handles this)
- Agent execution (Docker handles this)
- State persistence (Event log handles this)

## Technical Approach

**Language:** Go
**Framework:** `net/http` stdlib (no framework needed for POC)
**Port:** 8080 (configurable via env)
**Dependencies:** NATS client, Docker SDK (for agent queries)

## API Specification

### Session Management

#### Create Session

```http
POST /api/sessions
Content-Type: application/json

{
  "name": "my-project",
  "graph": "config/graph.yaml"
}

Response 201:
{
  "id": "sess_abc123",
  "name": "my-project",
  "status": "created",
  "created_at": "2025-10-22T10:00:00Z"
}
```http

#### List Sessions

```http
GET /api/sessions

Response 200:
{
  "sessions": [
    {
      "id": "sess_abc123",
      "name": "my-project",
      "status": "active",
      "created_at": "2025-10-22T10:00:00Z"
    }
  ]
}
```http

#### Get Session

```http
GET /api/sessions/{id}

Response 200:
{
  "id": "sess_abc123",
  "name": "my-project",
  "status": "active",
  "created_at": "2025-10-22T10:00:00Z",
  "current_chunk": "chunk_1",
  "chunks_completed": 0,
  "chunks_total": 5
}
```http

#### Stop Session

```http
DELETE /api/sessions/{id}

Response 204: (no content)
```http

### Agent Management

#### List Agents

```http
GET /api/agents

Response 200:
{
  "agents": [
    {
      "id": "agent_xyz789",
      "session_id": "sess_abc123",
      "role": "coding",
      "status": "running",
      "container_id": "docker_abc",
      "started_at": "2025-10-22T10:05:00Z"
    }
  ]
}
```http

#### Get Agent Status

```http
GET /api/agents/{id}

Response 200:
{
  "id": "agent_xyz789",
  "session_id": "sess_abc123",
  "role": "coding",
  "status": "running",
  "container_id": "docker_abc",
  "started_at": "2025-10-22T10:05:00Z",
  "last_message_at": "2025-10-22T10:10:00Z"
}
```http

#### Stop Agent

```http
DELETE /api/agents/{id}

Response 204: (no content)
```http

### Event Log

#### Tail Events

```http
GET /api/events?session={id}&limit=100&since={timestamp}

Response 200:
{
  "events": [
    {
      "id": "evt_123",
      "session_id": "sess_abc123",
      "timestamp": "2025-10-22T10:10:00Z",
      "type": "message.sent",
      "topic": "sessions.sess_abc123.work",
      "payload": {...}
    }
  ]
}
```http

#### Stream Events (SSE)

```http
GET /api/events/stream?session={id}
Accept: text/event-stream

Response 200:
(Server-Sent Events stream)
```http

### Health & Status

#### Health Check

```http
GET /health

Response 200:
{
  "status": "healthy",
  "nats": "connected",
  "docker": "available"
}
```http

#### System Info

```http
GET /api/info

Response 200:
{
  "version": "0.1.0",
  "nats_url": "nats://localhost:4222",
  "active_sessions": 1,
  "active_agents": 2
}
```http

### Static Files

```http
GET /              → web/index.html
GET /assets/*      → web/assets/*
```http

## Data Models

### Session

```go
type Session struct {
    ID              string    `json:"id"`
    Name            string    `json:"name"`
    GraphPath       string    `json:"graph_path"`
    Status          string    `json:"status"` // created, active, paused, completed, failed
    CreatedAt       time.Time `json:"created_at"`
    CurrentChunk    string    `json:"current_chunk,omitempty"`
    ChunksCompleted int       `json:"chunks_completed"`
    ChunksTotal     int       `json:"chunks_total"`
}
```http

### Agent

```go
type Agent struct {
    ID            string    `json:"id"`
    SessionID     string    `json:"session_id"`
    Role          string    `json:"role"` // coding, testing, review
    Status        string    `json:"status"` // starting, running, stopped, error
    ContainerID   string    `json:"container_id"`
    StartedAt     time.Time `json:"started_at"`
    LastMessageAt time.Time `json:"last_message_at,omitempty"`
}
```http

### Event

```go
type Event struct {
    ID        string                 `json:"id"`
    SessionID string                 `json:"session_id"`
    Timestamp time.Time              `json:"timestamp"`
    Type      string                 `json:"type"`
    Topic     string                 `json:"topic"`
    Payload   map[string]interface{} `json:"payload"`
}
```http

## State Management

**POC Approach:** In-memory state with reconstruction from event log

```go
type APIServer struct {
    sessions map[string]*Session
    agents   map[string]*Agent
    nats     *nats.Conn
    docker   *client.Client
}
```http

**On startup:**

1. Connect to NATS
2. Connect to Docker daemon
3. Query Docker for running agent containers
4. Reconstruct session state from event log (if exists)
5. Subscribe to NATS topics for real-time updates

## Configuration

```go
type Config struct {
    Port           int    // Default: 8080
    NATSUrl        string // Default: nats://localhost:4222
    DockerHost     string // Default: unix:///var/run/docker.sock
    EventLogPath   string // Default: ./events.log
    WebRoot        string // Default: ./web
}
```http

**Environment Variables:**

- `OUROCODUS_PORT`
- `OUROCODUS_NATS_URL`
- `OUROCODUS_DOCKER_HOST`
- `OUROCODUS_EVENT_LOG_PATH`
- `OUROCODUS_WEB_ROOT`

## Error Handling

**HTTP Status Codes:**

- `200` - Success
- `201` - Created
- `204` - No Content (successful deletion)
- `400` - Bad Request (invalid input)
- `404` - Not Found
- `500` - Internal Server Error
- `503` - Service Unavailable (NATS or Docker unavailable)

**Error Response Format:**

```json
{
  "error": "session not found",
  "code": "SESSION_NOT_FOUND",
  "details": "Session 'sess_abc123' does not exist"
}
```http

## Security (Deferred for POC)

**POC:** No authentication, localhost only
**Post-POC:** API keys, CORS configuration, rate limiting

## Logging

Use structured logging (JSON format):

```json
{
  "timestamp": "2025-10-22T10:00:00Z",
  "level": "info",
  "component": "api",
  "message": "Session created",
  "session_id": "sess_abc123"
}
```http

## Testing

**Unit Tests:**

- HTTP handler tests with `httptest`
- Mock NATS and Docker clients

**Integration Tests:**

- Real NATS server (test container)
- Real Docker daemon

## Implementation Notes

1. **Keep it simple** - No ORM, no complex routing, stdlib only
2. **Event log format** - JSON lines (one event per line)
3. **CORS** - Allow all origins for POC (localhost dev)
4. **Graceful shutdown** - Handle SIGTERM, close NATS/Docker connections

## Dependencies

```http
go.mod:
  - github.com/nats-io/nats.go
  - github.com/docker/docker/client
```http

## File Structure

```http
cmd/api/
  main.go           # Entry point
  handlers.go       # HTTP handlers
  middleware.go     # CORS, logging middleware
  state.go          # In-memory state management
  events.go         # Event log reader/subscriber
```http

## Success Criteria

API server is complete when:

1. Can create/list/stop sessions via REST
2. Can query agent status
3. Can tail event log
4. Serves web UI files
5. Health check endpoint works
6. Graceful shutdown implemented
7. Basic tests pass
