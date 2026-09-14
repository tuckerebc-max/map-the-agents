# OCode Architecture

This document describes the internal architecture of OCode, its components, and how they interact.

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         CLI Layer                             │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│  │   CLI   │  │ Commands │  │ Options  │  │ Interactive │  │
│  │ (click) │  │  (init,  │  │ (model,  │  │    Mode     │  │
│  │         │  │   mcp)   │  │ verbose) │  │             │  │
│  └────┬────┘  └────┬─────┘  └────┬─────┘  └──────┬──────┘  │
└───────┼────────────┼──────────────┼───────────────┼─────────┘
        │            │              │               │
        ▼            ▼              ▼               ▼
┌─────────────────────────────────────────────────────────────┐
│                      Engine Layer                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    OCodeEngine                       │   │
│  │  ┌─────────────┐  ┌──────────────┐  ┌────────────┐ │   │
│  │  │   Context   │  │    Tools     │  │   Session  │ │   │
│  │  │  Manager    │  │   Registry   │  │  Manager   │ │   │
│  │  └─────────────┘  └──────────────┘  └────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
        │                      │                     │
        ▼                      ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Service Layer                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐ │
│  │   API    │  │   Auth   │  │ Security │  │    MCP     │ │
│  │  Client  │  │ Manager  │  │  Manager │  │  Manager   │ │
│  └──────────┘  └──────────┘  └──────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────┘
        │                                           │
        ▼                                           ▼
┌──────────────┐                          ┌──────────────────┐
│   Ollama     │                          │   File System    │
│   Server     │                          │   & External     │
└──────────────┘                          └──────────────────┘
```

## Core Components

### 1. CLI Layer (`ocode_python/core/cli.py`)

The command-line interface built with Click framework.

**Responsibilities:**
- Parse command-line arguments
- Handle user input/output
- Manage interactive sessions
- Route commands to appropriate handlers

**Key Features:**
- Streaming output support
- Multiple output formats (text, JSON)
- Session continuation
- Configuration management commands

### 2. Engine (`ocode_python/core/engine.py`)

The main orchestration component that coordinates all operations.

**Responsibilities:**
- Process user queries
- Manage conversation flow
- Handle tool execution
- Coordinate with AI model
- Implement continuation logic

**Key Classes:**
```python
class OCodeEngine:
    def __init__(self, model, api_key, output_format, ...):
        self.api_client = OllamaAPIClient()
        self.context_manager = ContextManager()
        self.tool_registry = ToolRegistry()
        self.session_manager = SessionManager()

    async def process(self, query: str) -> AsyncGenerator[str, None]:
        # Main processing loop
        context = await self._prepare_context(query)
        messages = self._prepare_messages(query, context)
        async for chunk in self.api_client.stream_chat(request):
            # Handle streaming responses and tool calls
```

**Continuation Logic:**
- Detects incomplete responses
- Automatically continues generation
- Prevents infinite loops
- Maintains response coherence

### 3. Context Manager (`ocode_python/core/context_manager.py`)

Intelligent file analysis and project understanding system.

**Responsibilities:**
- Analyze project structure
- Build relevant context for queries
- Cache file information
- Calculate file relevance scores

**Key Features:**
```python
class ContextManager:
    async def build_context(self, query: str) -> ProjectContext:
        # 1. Identify relevant files based on query
        # 2. Extract symbols and dependencies
        # 3. Build comprehensive context
        # 4. Cache results for performance
```

**Caching Strategy:**
- SQLite-based cache
- File hash validation
- TTL-based expiration
- Smart invalidation

### 4. Tool System (`ocode_python/tools/`)

Modular tool architecture for extensibility.

**Base Architecture:**
```python
class Tool(ABC):
    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """Tool metadata and parameters"""

    @abstractmethod
    async def execute(self, **kwargs) -> ToolResult:
        """Execute tool with given parameters"""

class ToolRegistry:
    def register_tool(self, tool: Tool):
        """Register a tool for use"""

    def get_tool_definitions(self) -> List[Dict]:
        """Get Ollama-compatible tool definitions"""
```

**Tool Categories:**
- File Operations (read, write, edit, ops)
- Text Processing (grep, diff, sort)
- System Operations (bash, env, process)
- Development (git, test, notebook)
- Analysis (architect, think)
- Integration (mcp, curl, agent)

### 5. API Client (`ocode_python/core/api_client.py`)

Async client for Ollama API communication.

**Features:**
- Streaming responses
- Tool/function calling
- Error handling
- Health checks

**Key Methods:**
```python
class OllamaAPIClient:
    async def stream_chat(self, request) -> AsyncGenerator[StreamChunk]:
        """Stream chat completions with tool support"""

    async def check_health(self) -> bool:
        """Verify Ollama server availability"""
```

### 6. Session Management (`ocode_python/core/session.py`)

Persistent conversation and context storage.

**Features:**
- Session creation and loading
- Conversation history
- Context preservation
- JSON serialization

**Storage Structure:**
```
.ocode/sessions/
├── session-id-1.json
├── session-id-2.json
└── session-id-3.json
```

### 7. Security System (`ocode_python/utils/security.py`)

Multi-layer security implementation.

**Security Layers:**
1. **Path Validation**: Restrict file operations
2. **Command Sanitization**: Validate shell commands
3. **Permission System**: Enable/disable features
4. **Confirmation Prompts**: User approval for dangerous operations

**Security Flow:**
```python
async def validate_operation(operation, path, permissions):
    # 1. Check if operation type is allowed
    # 2. Validate path against allowed/blocked lists
    # 3. Check specific command patterns
    # 4. Request user confirmation if needed
```

### 8. Language Support (`ocode_python/languages/`)

Language-specific code analysis.

**Architecture:**
```python
class LanguageAnalyzer(ABC):
    @abstractmethod
    def extract_symbols(self, content: str) -> List[Symbol]:
        """Extract symbols from code"""

    @abstractmethod
    def extract_imports(self, content: str) -> List[str]:
        """Extract import statements"""
```

**Supported Languages:**
- Python (AST-based analysis)
- JavaScript/TypeScript
- Go, Rust, Java
- YAML, JSON, Terraform

### 9. MCP Integration (`ocode_python/mcp/`)

Model Context Protocol support.

**Components:**
- Protocol implementation
- Server management
- Resource handling
- Tool bridging

## Data Flow

### Query Processing Flow

```
User Query
    │
    ▼
Query Analysis ──────► LLM determines if tools needed
    │                            │
    ▼                            ▼
Context Building          Direct Response
    │                            │
    ▼                            │
File Analysis                    │
    │                            │
    ▼                            │
Message Preparation ◄────────────┘
    │
    ▼
LLM Processing
    │
    ├──► Text Response ──► Streaming Output
    │
    └──► Tool Call ──► Tool Execution ──► Result Integration
```

### Tool Execution Flow

```
Tool Request
    │
    ▼
Registry Lookup
    │
    ▼
Parameter Validation
    │
    ▼
Security Check ──────► Denied ──► Error Response
    │                              ▲
    ▼                              │
Permission Check ─────► Denied ────┘
    │
    ▼
User Confirmation ───► Denied ─────┘
(if required)
    │
    ▼
Tool Execution
    │
    ▼
Result Processing
    │
    ▼
Response Integration
```

## Key Design Patterns

### 1. Async-First Architecture

All I/O operations are asynchronous:
```python
async def read_file(path: Path) -> str:
    async with aiofiles.open(path) as f:
        return await f.read()
```

### 2. Generator-Based Streaming

Efficient memory usage for large responses:
```python
async def process(query: str) -> AsyncGenerator[str, None]:
    async for chunk in api_response:
        yield process_chunk(chunk)
```

### 3. Plugin Architecture

Tools are self-contained plugins:
```python
class CustomTool(Tool):
    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="custom",
            description="Custom tool",
            parameters=[...]
        )
```

### 4. Decorator-Based Security

Security checks via decorators:
```python
@requires_permission("file_write")
@validate_path
async def write_file(path: str, content: str):
    # Implementation
```

### 5. Factory Pattern for Languages

Dynamic language analyzer creation:
```python
def get_analyzer(file_path: Path) -> LanguageAnalyzer:
    extension = file_path.suffix
    return LANGUAGE_REGISTRY.get(extension, DefaultAnalyzer)()
```

## Performance Optimizations

### 1. Caching Strategy
- File content caching with hash validation
- Symbol extraction results cached
- LRU cache for recent operations

### 2. Concurrent Operations
- Parallel file analysis
- Concurrent tool execution where safe
- Async I/O throughout

### 3. Streaming Architecture
- Stream LLM responses
- Progressive file reading
- Chunked output delivery

### 4. Selective Context
- Relevance-based file selection
- Query-aware context building
- Smart truncation strategies

## Extension Points

### 1. Adding New Tools

Create new tool in `ocode_python/tools/`:
```python
from .base import Tool, ToolDefinition, ToolParameter

class MyTool(Tool):
    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="my_tool",
            description="Description",
            parameters=[
                ToolParameter(
                    name="param1",
                    description="Parameter description",
                    type="string",
                    required=True
                )
            ]
        )

    async def execute(self, **kwargs) -> ToolResult:
        # Implementation
        return ToolResult(success=True, output="Result")
```

### 2. Adding Language Support

Create analyzer in `ocode_python/languages/`:
```python
from .base import LanguageAnalyzer

class MyLangAnalyzer(LanguageAnalyzer):
    def extract_symbols(self, content: str) -> List[Symbol]:
        # Parse and extract symbols

    def extract_imports(self, content: str) -> List[str]:
        # Extract import statements
```

### 3. Custom Security Policies

Extend security configuration:
```python
class CustomSecurityPolicy(SecurityPolicy):
    def validate_operation(self, operation, context):
        # Custom validation logic
```

## Testing Architecture

### Unit Tests
- Individual component testing
- Mocked dependencies
- Fast execution

### Integration Tests
- Component interaction testing
- Real file operations
- End-to-end workflows

### Performance Tests
- Load testing for context building
- Memory usage monitoring
- Response time benchmarks

## Deployment Considerations

### Resource Requirements
- Memory: 2-8GB depending on model
- CPU: Benefits from multiple cores
- Storage: Cache and session storage
- Network: Ollama API connectivity

### Configuration Management
- Environment variables
- Configuration files
- Runtime overrides
- Security policies

### Monitoring Points
- API response times
- Tool execution duration
- Cache hit rates
- Error frequencies

## Future Architecture Directions

### Planned Enhancements
1. **Distributed Tool Execution**: Run tools on remote workers
2. **Multi-Model Support**: Use different models for different tasks
3. **Enhanced Caching**: Redis support for distributed cache
4. **WebSocket Support**: Real-time bidirectional communication

### Extension Possibilities
1. **IDE Plugins**: Direct IDE integration
2. **Web Interface**: Browser-based UI
3. **API Server**: RESTful API for remote access
4. **Cloud Functions**: Serverless tool execution
