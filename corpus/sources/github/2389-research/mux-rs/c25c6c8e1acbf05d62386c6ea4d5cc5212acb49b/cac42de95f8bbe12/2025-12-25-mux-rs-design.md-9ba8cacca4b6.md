# mux-rs Design

Rust-first redesign of [mux](https://github.com/2389-research/mux) - agentic infrastructure with tool execution, MCP integration, and permission-gated approval flows.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Approach | Rust-first redesign | Leverage Rust strengths rather than direct translation |
| Tool definition | Derive macro + trait | Ergonomic for common cases, flexible for advanced |
| Async runtime | Tokio-native | Ecosystem compatibility, pragmatic choice |
| Error handling | thiserror + anyhow | Typed library errors, flexible tool errors |
| Permissions | Policy engine | Expressive rules with patterns and conditions |
| MCP scope | Client only | Connect to servers, proxy tools into registry |
| LLM providers | Multi-provider | Anthropic + OpenAI from day one |

## Crate Structure

```
mux/
├── Cargo.toml
├── src/
│   ├── lib.rs
│   ├── llm/
│   │   ├── mod.rs
│   │   ├── types.rs      # Message, ContentBlock, Request, Response
│   │   ├── client.rs     # LlmClient trait
│   │   ├── anthropic.rs  # Claude implementation
│   │   └── openai.rs     # GPT implementation
│   ├── tool/
│   │   ├── mod.rs
│   │   ├── trait.rs      # Tool trait, ToolExecute trait
│   │   ├── registry.rs   # Thread-safe tool storage
│   │   └── result.rs     # ToolResult type
│   ├── permission/
│   │   ├── mod.rs
│   │   ├── policy.rs     # Policy, PolicyRule, Decision
│   │   └── handler.rs    # ApprovalHandler trait
│   ├── mcp/
│   │   ├── mod.rs
│   │   ├── types.rs      # JSON-RPC types, MCP protocol types
│   │   ├── client.rs     # McpClient
│   │   └── proxy.rs      # McpProxyTool
│   └── error.rs          # MuxError, LlmError, ToolError, etc.
└── mux-derive/
    ├── Cargo.toml
    └── src/lib.rs        # #[derive(Tool)] proc macro
```

## Core Dependencies

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
thiserror = "2"
anyhow = "1"
async-trait = "0.1"
reqwest = { version = "0.12", features = ["json", "stream"] }
futures = "0.3"
glob = "0.3"

[dev-dependencies]
tokio-test = "0.4"
```

## LLM Module

### Types

```rust
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Role {
    User,
    Assistant,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum ContentBlock {
    Text { text: String },
    ToolUse { id: String, name: String, input: serde_json::Value },
    ToolResult { tool_use_id: String, content: String, is_error: bool },
}

#[derive(Debug, Clone)]
pub struct Message {
    pub role: Role,
    pub content: Vec<ContentBlock>,
}

#[derive(Debug, Clone)]
pub struct ToolDefinition {
    pub name: String,
    pub description: String,
    pub input_schema: serde_json::Value,
}

#[derive(Debug, Clone, Default)]
pub struct Request {
    pub model: String,
    pub messages: Vec<Message>,
    pub tools: Vec<ToolDefinition>,
    pub max_tokens: Option<u32>,
    pub system: Option<String>,
    pub temperature: Option<f64>,
}

#[derive(Debug, Clone)]
pub struct Response {
    pub id: String,
    pub content: Vec<ContentBlock>,
    pub stop_reason: StopReason,
    pub model: String,
    pub usage: Usage,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum StopReason {
    EndTurn,
    ToolUse,
    MaxTokens,
}

#[derive(Debug, Clone, Default)]
pub struct Usage {
    pub input_tokens: u32,
    pub output_tokens: u32,
}
```

### Client Trait

```rust
#[async_trait]
pub trait LlmClient: Send + Sync {
    async fn create_message(&self, req: &Request) -> Result<Response, LlmError>;

    fn create_message_stream(&self, req: &Request)
        -> Pin<Box<dyn Stream<Item = Result<StreamEvent, LlmError>> + Send>>;
}

pub enum StreamEvent {
    MessageStart { id: String, model: String },
    ContentBlockStart { index: usize, block: ContentBlock },
    ContentBlockDelta { index: usize, delta: ContentDelta },
    ContentBlockStop { index: usize },
    MessageDelta { stop_reason: Option<StopReason>, usage: Usage },
    MessageStop,
}
```

## Tool Module

### Tool Trait

```rust
#[async_trait]
pub trait Tool: Send + Sync {
    fn name(&self) -> &str;
    fn description(&self) -> &str;
    fn schema(&self) -> serde_json::Value;

    fn requires_approval(&self, params: &serde_json::Value) -> bool {
        false
    }

    async fn execute(&self, params: serde_json::Value) -> Result<ToolResult, anyhow::Error>;
}

pub trait ToolExecute: Send + Sync {
    async fn execute(&self) -> Result<ToolResult, anyhow::Error>;
}
```

### Derive Macro Usage

```rust
#[derive(Tool)]
#[tool(name = "read_file", description = "Read contents of a file")]
pub struct ReadFile {
    #[tool(description = "Path to the file")]
    path: String,

    #[tool(description = "Starting line", default = 0)]
    offset: Option<u32>,
}

#[async_trait]
impl ToolExecute for ReadFile {
    async fn execute(&self) -> Result<ToolResult, anyhow::Error> {
        let content = tokio::fs::read_to_string(&self.path).await?;
        Ok(ToolResult::text(content))
    }
}
```

The derive macro generates:
- `Tool::name()` from `#[tool(name = "...")]`
- `Tool::description()` from `#[tool(description = "...")]`
- `Tool::schema()` as JSON Schema from struct fields
- `Tool::execute()` that deserializes params and calls `ToolExecute::execute()`

### ToolResult

```rust
pub struct ToolResult {
    pub content: String,
    pub is_error: bool,
    pub metadata: HashMap<String, serde_json::Value>,
}

impl ToolResult {
    pub fn text(content: impl Into<String>) -> Self { ... }
    pub fn error(message: impl Into<String>) -> Self { ... }
    pub fn with_metadata(mut self, key: &str, value: impl Serialize) -> Self { ... }
}
```

### Registry

```rust
pub struct Registry {
    tools: Arc<RwLock<HashMap<String, Arc<dyn Tool>>>>,
}

impl Registry {
    pub fn new() -> Self;
    pub fn register<T: Tool + 'static>(&self, tool: T);
    pub fn register_arc(&self, tool: Arc<dyn Tool>);
    pub fn unregister(&self, name: &str);
    pub async fn get(&self, name: &str) -> Option<Arc<dyn Tool>>;
    pub async fn list(&self) -> Vec<String>;
    pub async fn all(&self) -> Vec<Arc<dyn Tool>>;
    pub async fn to_definitions(&self) -> Vec<ToolDefinition>;
    pub async fn merge_mcp(&self, mcp: &McpClient, prefix: Option<&str>) -> Result<(), McpError>;
}
```

## Permission Module

### Policy Rules

```rust
pub enum Decision {
    Allow,
    Deny,
    Ask,
}

pub enum PolicyRule {
    Allow(String),
    Deny(String),
    AllowPattern(glob::Pattern),
    DenyPattern(glob::Pattern),
    Conditional {
        tool: String,
        condition: Box<dyn Fn(&serde_json::Value) -> Decision + Send + Sync>,
    },
}

pub struct Policy {
    rules: Vec<PolicyRule>,
    default: Decision,
}

impl Policy {
    pub fn builder() -> PolicyBuilder;
    pub fn evaluate(&self, tool: &str, params: &serde_json::Value) -> Decision;
}
```

### Policy Builder

```rust
pub struct PolicyBuilder { ... }

impl PolicyBuilder {
    pub fn allow(self, tool: &str) -> Self;
    pub fn deny(self, tool: &str) -> Self;
    pub fn allow_pattern(self, pattern: &str) -> Self;
    pub fn deny_pattern(self, pattern: &str) -> Self;
    pub fn conditional<F>(self, tool: &str, f: F) -> Self
    where
        F: Fn(&serde_json::Value) -> Decision + Send + Sync + 'static;
    pub fn default(self, decision: Decision) -> Self;
    pub fn build(self) -> Policy;
}
```

### Approval Handler

```rust
pub struct ApprovalContext {
    pub tool_description: String,
    pub request_id: String,
}

#[async_trait]
pub trait ApprovalHandler: Send + Sync {
    async fn request_approval(
        &self,
        tool: &str,
        params: &serde_json::Value,
        context: &ApprovalContext,
    ) -> Result<bool, anyhow::Error>;
}
```

## MCP Module

### Types

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpRequest {
    pub jsonrpc: String,  // "2.0"
    pub id: u64,
    pub method: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub params: Option<serde_json::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpResponse {
    pub jsonrpc: String,
    pub id: u64,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub result: Option<serde_json::Value>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub error: Option<McpRpcError>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpToolInfo {
    pub name: String,
    pub description: String,
    #[serde(rename = "inputSchema")]
    pub input_schema: serde_json::Value,
}

#[derive(Debug, Clone)]
pub struct McpServerConfig {
    pub name: String,
    pub transport: McpTransport,
}

pub enum McpTransport {
    Stdio {
        command: String,
        args: Vec<String>,
        env: HashMap<String, String>,
    },
    Sse {
        url: String,
    },
}
```

### Client

```rust
pub struct McpClient { ... }

impl McpClient {
    pub async fn connect(config: McpServerConfig) -> Result<Self, McpError>;
    pub async fn initialize(&self) -> Result<ServerCapabilities, McpError>;
    pub async fn list_tools(&self) -> Result<Vec<McpToolInfo>, McpError>;
    pub async fn call_tool(&self, name: &str, args: serde_json::Value)
        -> Result<McpToolResult, McpError>;
    pub async fn shutdown(&self) -> Result<(), McpError>;
}
```

### Proxy Tool

```rust
pub struct McpProxyTool {
    client: Arc<McpClient>,
    info: McpToolInfo,
}

#[async_trait]
impl Tool for McpProxyTool {
    fn name(&self) -> &str { &self.info.name }
    fn description(&self) -> &str { &self.info.description }
    fn schema(&self) -> serde_json::Value { self.info.input_schema.clone() }

    async fn execute(&self, params: serde_json::Value) -> Result<ToolResult, anyhow::Error> {
        let result = self.client.call_tool(&self.info.name, params).await?;
        Ok(result.into())
    }
}
```

## Error Types

```rust
#[derive(Debug, thiserror::Error)]
pub enum MuxError {
    #[error("LLM error: {0}")]
    Llm(#[from] LlmError),

    #[error("Tool error: {0}")]
    Tool(#[from] ToolError),

    #[error("Permission denied: {0}")]
    Permission(#[from] PermissionError),

    #[error("MCP error: {0}")]
    Mcp(#[from] McpError),
}

#[derive(Debug, thiserror::Error)]
pub enum LlmError {
    #[error("HTTP error: {0}")]
    Http(#[from] reqwest::Error),

    #[error("API error ({status}): {message}")]
    Api { status: u16, message: String },

    #[error("Stream closed unexpectedly")]
    StreamClosed,

    #[error("Deserialization error: {0}")]
    Deserialize(#[from] serde_json::Error),
}

#[derive(Debug, thiserror::Error)]
pub enum ToolError {
    #[error("Tool not found: {0}")]
    NotFound(String),

    #[error("Invalid parameters: {0}")]
    InvalidParams(String),

    #[error("Execution failed: {0}")]
    Execution(#[source] anyhow::Error),
}

#[derive(Debug, thiserror::Error)]
pub enum PermissionError {
    #[error("Tool '{0}' denied by policy")]
    Denied(String),

    #[error("Approval rejected for tool '{0}'")]
    Rejected(String),

    #[error("Approval handler error: {0}")]
    Handler(#[source] anyhow::Error),
}

#[derive(Debug, thiserror::Error)]
pub enum McpError {
    #[error("Connection failed: {0}")]
    Connection(String),

    #[error("Protocol error: {0}")]
    Protocol(String),

    #[error("RPC error ({code}): {message}")]
    Rpc { code: i32, message: String },

    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
}
```

## Usage Example

```rust
use mux::{
    llm::{AnthropicClient, Request, Message, Role},
    tool::{Registry, Tool, ToolResult},
    permission::{Policy, Decision},
    mcp::McpClient,
};

#[derive(Tool)]
#[tool(name = "greet", description = "Greet a person")]
struct Greet {
    #[tool(description = "Name to greet")]
    name: String,
}

#[async_trait]
impl ToolExecute for Greet {
    async fn execute(&self) -> Result<ToolResult, anyhow::Error> {
        Ok(ToolResult::text(format!("Hello, {}!", self.name)))
    }
}

#[tokio::main]
async fn main() -> Result<(), mux::MuxError> {
    // Set up tools
    let registry = Registry::new();
    registry.register(Greet { name: String::new() });

    // Add MCP tools
    let mcp = McpClient::connect(config).await?;
    registry.merge_mcp(&mcp, Some("mcp")).await?;

    // Set up permissions
    let policy = Policy::builder()
        .allow("greet")
        .allow_pattern("mcp_*")
        .deny_pattern("dangerous_*")
        .default(Decision::Ask)
        .build();

    // Create LLM client
    let client = AnthropicClient::new(api_key);

    // Make request with tools
    let req = Request {
        model: "claude-sonnet-4-20250514".into(),
        messages: vec![Message::user("Greet Alice")],
        tools: registry.to_definitions().await,
        ..Default::default()
    };

    let response = client.create_message(&req).await?;

    Ok(())
}
```
