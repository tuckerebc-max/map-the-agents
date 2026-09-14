# mux-rs Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Rust agentic infrastructure library with tool execution, MCP integration, and permission-gated approval flows.

**Architecture:** Modular crate with `llm/`, `tool/`, `permission/`, `mcp/` submodules. Proc-macro crate (`mux-derive`) for `#[derive(Tool)]`. Tokio-native async, thiserror for typed errors, anyhow for tool impl flexibility.

**Tech Stack:** Rust 2024 edition, tokio, serde, thiserror, anyhow, reqwest, async-trait, glob

**Reference:** See `docs/plans/2025-12-25-mux-rs-design.md` for full API design.

---

## Phase 1: Project Scaffold & Error Types

### Task 1: Set up workspace structure

**Files:**
- Modify: `Cargo.toml`
- Create: `src/lib.rs`
- Create: `src/error.rs`
- Delete: `src/main.rs`

**Step 1: Update Cargo.toml with dependencies**

```toml
[package]
name = "mux"
version = "0.1.0"
edition = "2024"
description = "Agentic infrastructure for Rust"
license = "MIT"

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

**Step 2: Delete src/main.rs and create src/lib.rs**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;

pub use error::MuxError;
```

**Step 3: Create src/error.rs with error types**

```rust
// ABOUTME: Defines all error types for the mux library using thiserror.
// ABOUTME: Each submodule has its own error enum, unified under MuxError.

/// Top-level error type for the mux library.
#[derive(Debug, thiserror::Error)]
pub enum MuxError {
    #[error("LLM error: {0}")]
    Llm(#[from] LlmError),

    #[error("Tool error: {0}")]
    Tool(#[from] ToolError),

    #[error("Permission error: {0}")]
    Permission(#[from] PermissionError),

    #[error("MCP error: {0}")]
    Mcp(#[from] McpError),
}

/// Errors from LLM client operations.
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

/// Errors from tool operations.
#[derive(Debug, thiserror::Error)]
pub enum ToolError {
    #[error("Tool not found: {0}")]
    NotFound(String),

    #[error("Invalid parameters: {0}")]
    InvalidParams(String),

    #[error("Execution failed: {0}")]
    Execution(#[source] anyhow::Error),
}

/// Errors from permission checks.
#[derive(Debug, thiserror::Error)]
pub enum PermissionError {
    #[error("Tool '{0}' denied by policy")]
    Denied(String),

    #[error("Approval rejected for tool '{0}'")]
    Rejected(String),

    #[error("Approval handler error: {0}")]
    Handler(#[source] anyhow::Error),
}

/// Errors from MCP operations.
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

**Step 4: Run cargo check to verify**

Run: `cargo check`
Expected: Compiles successfully

**Step 5: Commit**

```bash
git add -A
git commit -m "feat: scaffold project with error types"
```

---

## Phase 2: LLM Types

### Task 2: Create LLM types module

**Files:**
- Create: `src/llm/mod.rs`
- Create: `src/llm/types.rs`
- Modify: `src/lib.rs`

**Step 1: Create src/llm/mod.rs**

```rust
// ABOUTME: LLM module - client abstraction for language model providers.
// ABOUTME: Defines types, traits, and provider implementations.

mod types;

pub use types::*;
```

**Step 2: Create src/llm/types.rs with core types**

```rust
// ABOUTME: Core types for LLM communication - messages, content blocks,
// ABOUTME: tool definitions, requests, and responses.

use serde::{Deserialize, Serialize};

/// Role of a message sender.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum Role {
    User,
    Assistant,
}

/// Why the model stopped generating.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum StopReason {
    EndTurn,
    ToolUse,
    MaxTokens,
}

/// A block of content within a message.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum ContentBlock {
    Text {
        text: String,
    },
    ToolUse {
        id: String,
        name: String,
        input: serde_json::Value,
    },
    ToolResult {
        tool_use_id: String,
        content: String,
        #[serde(default)]
        is_error: bool,
    },
}

impl ContentBlock {
    /// Create a text content block.
    pub fn text(text: impl Into<String>) -> Self {
        Self::Text { text: text.into() }
    }

    /// Create a tool result content block.
    pub fn tool_result(tool_use_id: impl Into<String>, content: impl Into<String>) -> Self {
        Self::ToolResult {
            tool_use_id: tool_use_id.into(),
            content: content.into(),
            is_error: false,
        }
    }

    /// Create an error tool result content block.
    pub fn tool_error(tool_use_id: impl Into<String>, error: impl Into<String>) -> Self {
        Self::ToolResult {
            tool_use_id: tool_use_id.into(),
            content: error.into(),
            is_error: true,
        }
    }
}

/// A conversation message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Message {
    pub role: Role,
    pub content: Vec<ContentBlock>,
}

impl Message {
    /// Create a user message with text content.
    pub fn user(text: impl Into<String>) -> Self {
        Self {
            role: Role::User,
            content: vec![ContentBlock::text(text)],
        }
    }

    /// Create an assistant message with text content.
    pub fn assistant(text: impl Into<String>) -> Self {
        Self {
            role: Role::Assistant,
            content: vec![ContentBlock::text(text)],
        }
    }

    /// Create a user message with tool results.
    pub fn tool_results(results: Vec<ContentBlock>) -> Self {
        Self {
            role: Role::User,
            content: results,
        }
    }
}

/// Definition of a tool for the LLM.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ToolDefinition {
    pub name: String,
    pub description: String,
    pub input_schema: serde_json::Value,
}

/// Token usage statistics.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct Usage {
    pub input_tokens: u32,
    pub output_tokens: u32,
}

/// Request to create a message.
#[derive(Debug, Clone, Default)]
pub struct Request {
    pub model: String,
    pub messages: Vec<Message>,
    pub tools: Vec<ToolDefinition>,
    pub max_tokens: Option<u32>,
    pub system: Option<String>,
    pub temperature: Option<f64>,
}

impl Request {
    /// Create a new request with the given model.
    pub fn new(model: impl Into<String>) -> Self {
        Self {
            model: model.into(),
            ..Default::default()
        }
    }

    /// Add a message to the request.
    pub fn message(mut self, message: Message) -> Self {
        self.messages.push(message);
        self
    }

    /// Add messages to the request.
    pub fn messages(mut self, messages: impl IntoIterator<Item = Message>) -> Self {
        self.messages.extend(messages);
        self
    }

    /// Add a tool definition.
    pub fn tool(mut self, tool: ToolDefinition) -> Self {
        self.tools.push(tool);
        self
    }

    /// Add tool definitions.
    pub fn tools(mut self, tools: impl IntoIterator<Item = ToolDefinition>) -> Self {
        self.tools.extend(tools);
        self
    }

    /// Set the system prompt.
    pub fn system(mut self, system: impl Into<String>) -> Self {
        self.system = Some(system.into());
        self
    }

    /// Set max tokens.
    pub fn max_tokens(mut self, max_tokens: u32) -> Self {
        self.max_tokens = Some(max_tokens);
        self
    }

    /// Set temperature.
    pub fn temperature(mut self, temperature: f64) -> Self {
        self.temperature = Some(temperature);
        self
    }
}

/// Response from creating a message.
#[derive(Debug, Clone)]
pub struct Response {
    pub id: String,
    pub content: Vec<ContentBlock>,
    pub stop_reason: StopReason,
    pub model: String,
    pub usage: Usage,
}

impl Response {
    /// Check if the response contains tool use blocks.
    pub fn has_tool_use(&self) -> bool {
        self.content.iter().any(|b| matches!(b, ContentBlock::ToolUse { .. }))
    }

    /// Extract all tool use blocks from the response.
    pub fn tool_uses(&self) -> Vec<&ContentBlock> {
        self.content
            .iter()
            .filter(|b| matches!(b, ContentBlock::ToolUse { .. }))
            .collect()
    }

    /// Extract concatenated text content from the response.
    pub fn text(&self) -> String {
        self.content
            .iter()
            .filter_map(|b| match b {
                ContentBlock::Text { text } => Some(text.as_str()),
                _ => None,
            })
            .collect::<Vec<_>>()
            .join("")
    }
}
```

**Step 3: Update src/lib.rs to include llm module**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;
pub mod llm;

pub use error::MuxError;
```

**Step 4: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 5: Commit**

```bash
git add -A
git commit -m "feat(llm): add core LLM types"
```

---

### Task 3: Add LLM types tests

**Files:**
- Create: `src/llm/types_test.rs`
- Modify: `src/llm/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for LLM types - serialization, deserialization, helpers.
// ABOUTME: Verifies JSON format matches provider APIs.

use super::*;

#[test]
fn test_role_serialization() {
    assert_eq!(serde_json::to_string(&Role::User).unwrap(), "\"user\"");
    assert_eq!(serde_json::to_string(&Role::Assistant).unwrap(), "\"assistant\"");
}

#[test]
fn test_role_deserialization() {
    assert_eq!(serde_json::from_str::<Role>("\"user\"").unwrap(), Role::User);
    assert_eq!(serde_json::from_str::<Role>("\"assistant\"").unwrap(), Role::Assistant);
}

#[test]
fn test_content_block_text_serialization() {
    let block = ContentBlock::text("Hello");
    let json = serde_json::to_value(&block).unwrap();
    assert_eq!(json["type"], "text");
    assert_eq!(json["text"], "Hello");
}

#[test]
fn test_content_block_tool_use_deserialization() {
    let json = r#"{
        "type": "tool_use",
        "id": "123",
        "name": "read_file",
        "input": {"path": "/tmp/test.txt"}
    }"#;
    let block: ContentBlock = serde_json::from_str(json).unwrap();
    match block {
        ContentBlock::ToolUse { id, name, input } => {
            assert_eq!(id, "123");
            assert_eq!(name, "read_file");
            assert_eq!(input["path"], "/tmp/test.txt");
        }
        _ => panic!("Expected ToolUse"),
    }
}

#[test]
fn test_content_block_tool_result_serialization() {
    let block = ContentBlock::tool_result("123", "file contents");
    let json = serde_json::to_value(&block).unwrap();
    assert_eq!(json["type"], "tool_result");
    assert_eq!(json["tool_use_id"], "123");
    assert_eq!(json["content"], "file contents");
    assert_eq!(json["is_error"], false);
}

#[test]
fn test_content_block_tool_error_serialization() {
    let block = ContentBlock::tool_error("123", "file not found");
    let json = serde_json::to_value(&block).unwrap();
    assert_eq!(json["type"], "tool_result");
    assert_eq!(json["is_error"], true);
}

#[test]
fn test_message_user_helper() {
    let msg = Message::user("Hello");
    assert_eq!(msg.role, Role::User);
    assert_eq!(msg.content.len(), 1);
    match &msg.content[0] {
        ContentBlock::Text { text } => assert_eq!(text, "Hello"),
        _ => panic!("Expected Text"),
    }
}

#[test]
fn test_request_builder() {
    let req = Request::new("claude-sonnet-4-20250514")
        .message(Message::user("Hi"))
        .system("You are helpful")
        .max_tokens(1024)
        .temperature(0.7);

    assert_eq!(req.model, "claude-sonnet-4-20250514");
    assert_eq!(req.messages.len(), 1);
    assert_eq!(req.system, Some("You are helpful".to_string()));
    assert_eq!(req.max_tokens, Some(1024));
    assert_eq!(req.temperature, Some(0.7));
}

#[test]
fn test_response_has_tool_use() {
    let response = Response {
        id: "123".to_string(),
        content: vec![
            ContentBlock::text("I'll read that file"),
            ContentBlock::ToolUse {
                id: "456".to_string(),
                name: "read_file".to_string(),
                input: serde_json::json!({"path": "/tmp/test.txt"}),
            },
        ],
        stop_reason: StopReason::ToolUse,
        model: "claude-sonnet-4-20250514".to_string(),
        usage: Usage::default(),
    };

    assert!(response.has_tool_use());
    assert_eq!(response.tool_uses().len(), 1);
    assert_eq!(response.text(), "I'll read that file");
}

#[test]
fn test_response_no_tool_use() {
    let response = Response {
        id: "123".to_string(),
        content: vec![ContentBlock::text("Hello!")],
        stop_reason: StopReason::EndTurn,
        model: "claude-sonnet-4-20250514".to_string(),
        usage: Usage::default(),
    };

    assert!(!response.has_tool_use());
    assert!(response.tool_uses().is_empty());
}

#[test]
fn test_stop_reason_serialization() {
    assert_eq!(serde_json::to_string(&StopReason::EndTurn).unwrap(), "\"end_turn\"");
    assert_eq!(serde_json::to_string(&StopReason::ToolUse).unwrap(), "\"tool_use\"");
    assert_eq!(serde_json::to_string(&StopReason::MaxTokens).unwrap(), "\"max_tokens\"");
}
```

**Step 2: Update src/llm/mod.rs to include tests**

```rust
// ABOUTME: LLM module - client abstraction for language model providers.
// ABOUTME: Defines types, traits, and provider implementations.

mod types;

pub use types::*;

#[cfg(test)]
mod types_test;
```

**Step 3: Run tests**

Run: `cargo test llm`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(llm): add tests for LLM types"
```

---

### Task 4: Add LLM client trait

**Files:**
- Create: `src/llm/client.rs`
- Modify: `src/llm/mod.rs`

**Step 1: Create src/llm/client.rs**

```rust
// ABOUTME: Defines the LlmClient trait - the abstraction layer that allows
// ABOUTME: mux to work with any LLM provider (Anthropic, OpenAI, etc.)

use std::pin::Pin;

use async_trait::async_trait;
use futures::Stream;

use super::{Request, Response};
use crate::error::LlmError;

/// Event types for streaming responses.
#[derive(Debug, Clone)]
pub enum StreamEvent {
    /// Message creation started.
    MessageStart { id: String, model: String },

    /// A content block started.
    ContentBlockStart {
        index: usize,
        block: super::ContentBlock,
    },

    /// Delta for a content block (usually text).
    ContentBlockDelta { index: usize, text: String },

    /// A content block finished.
    ContentBlockStop { index: usize },

    /// Message metadata update.
    MessageDelta {
        stop_reason: Option<super::StopReason>,
        usage: super::Usage,
    },

    /// Message complete.
    MessageStop,
}

/// Trait for LLM client implementations.
#[async_trait]
pub trait LlmClient: Send + Sync {
    /// Create a message (non-streaming).
    async fn create_message(&self, req: &Request) -> Result<Response, LlmError>;

    /// Create a message with streaming response.
    fn create_message_stream(
        &self,
        req: &Request,
    ) -> Pin<Box<dyn Stream<Item = Result<StreamEvent, LlmError>> + Send + 'static>>;
}
```

**Step 2: Update src/llm/mod.rs**

```rust
// ABOUTME: LLM module - client abstraction for language model providers.
// ABOUTME: Defines types, traits, and provider implementations.

mod client;
mod types;

pub use client::*;
pub use types::*;

#[cfg(test)]
mod types_test;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 4: Commit**

```bash
git add -A
git commit -m "feat(llm): add LlmClient trait with streaming support"
```

---

## Phase 3: Tool System

### Task 5: Create tool result type

**Files:**
- Create: `src/tool/mod.rs`
- Create: `src/tool/result.rs`
- Modify: `src/lib.rs`

**Step 1: Create src/tool/result.rs**

```rust
// ABOUTME: Defines the ToolResult type - a unified structure for tool
// ABOUTME: execution outcomes with content, error state, and metadata.

use std::collections::HashMap;

use serde::Serialize;

/// Result of a tool execution.
#[derive(Debug, Clone)]
pub struct ToolResult {
    /// The output content.
    pub content: String,

    /// Whether this result represents an error.
    pub is_error: bool,

    /// Optional metadata about the execution.
    pub metadata: HashMap<String, serde_json::Value>,
}

impl ToolResult {
    /// Create a successful text result.
    pub fn text(content: impl Into<String>) -> Self {
        Self {
            content: content.into(),
            is_error: false,
            metadata: HashMap::new(),
        }
    }

    /// Create an error result.
    pub fn error(message: impl Into<String>) -> Self {
        Self {
            content: message.into(),
            is_error: true,
            metadata: HashMap::new(),
        }
    }

    /// Add metadata to the result.
    pub fn with_metadata(mut self, key: impl Into<String>, value: impl Serialize) -> Self {
        if let Ok(v) = serde_json::to_value(value) {
            self.metadata.insert(key.into(), v);
        }
        self
    }
}

impl Default for ToolResult {
    fn default() -> Self {
        Self::text("")
    }
}
```

**Step 2: Create src/tool/mod.rs**

```rust
// ABOUTME: Tool module - defines tools, registry, and execution.
// ABOUTME: Core abstraction for agent capabilities.

mod result;

pub use result::*;
```

**Step 3: Update src/lib.rs**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;
pub mod llm;
pub mod tool;

pub use error::MuxError;
```

**Step 4: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 5: Commit**

```bash
git add -A
git commit -m "feat(tool): add ToolResult type"
```

---

### Task 6: Add tool result tests

**Files:**
- Create: `src/tool/result_test.rs`
- Modify: `src/tool/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for ToolResult - constructors, metadata, defaults.
// ABOUTME: Verifies result structure works correctly.

use super::*;

#[test]
fn test_text_result() {
    let result = ToolResult::text("Hello, world!");
    assert_eq!(result.content, "Hello, world!");
    assert!(!result.is_error);
    assert!(result.metadata.is_empty());
}

#[test]
fn test_error_result() {
    let result = ToolResult::error("Something went wrong");
    assert_eq!(result.content, "Something went wrong");
    assert!(result.is_error);
}

#[test]
fn test_with_metadata() {
    let result = ToolResult::text("output")
        .with_metadata("bytes_read", 1024)
        .with_metadata("cached", true);

    assert_eq!(result.metadata["bytes_read"], 1024);
    assert_eq!(result.metadata["cached"], true);
}

#[test]
fn test_default() {
    let result = ToolResult::default();
    assert_eq!(result.content, "");
    assert!(!result.is_error);
}
```

**Step 2: Update src/tool/mod.rs**

```rust
// ABOUTME: Tool module - defines tools, registry, and execution.
// ABOUTME: Core abstraction for agent capabilities.

mod result;

pub use result::*;

#[cfg(test)]
mod result_test;
```

**Step 3: Run tests**

Run: `cargo test tool`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(tool): add tests for ToolResult"
```

---

### Task 7: Create Tool trait

**Files:**
- Create: `src/tool/traits.rs`
- Modify: `src/tool/mod.rs`

**Step 1: Create src/tool/traits.rs**

```rust
// ABOUTME: Defines the Tool trait - the core abstraction for agent capabilities.
// ABOUTME: Tools have a name, description, schema, and async execute method.

use async_trait::async_trait;

use super::ToolResult;

/// A tool that can be executed by an agent.
#[async_trait]
pub trait Tool: Send + Sync {
    /// Returns the unique name of this tool.
    fn name(&self) -> &str;

    /// Returns a human-readable description for the LLM.
    fn description(&self) -> &str;

    /// Returns the JSON Schema for the tool's input parameters.
    fn schema(&self) -> serde_json::Value;

    /// Check if this invocation requires user approval.
    ///
    /// Override this to implement context-sensitive approval requirements.
    /// Default returns false (no approval needed).
    fn requires_approval(&self, _params: &serde_json::Value) -> bool {
        false
    }

    /// Execute the tool with the given parameters.
    async fn execute(&self, params: serde_json::Value) -> Result<ToolResult, anyhow::Error>;
}

/// Trait for typed tool execution.
///
/// Implement this trait for tools defined with `#[derive(Tool)]`.
/// The derive macro will generate the `Tool` trait implementation
/// that deserializes params and calls this method.
#[async_trait]
pub trait ToolExecute: Send + Sync {
    /// Execute the tool with typed parameters (struct fields).
    async fn execute(&self) -> Result<ToolResult, anyhow::Error>;
}
```

**Step 2: Update src/tool/mod.rs**

```rust
// ABOUTME: Tool module - defines tools, registry, and execution.
// ABOUTME: Core abstraction for agent capabilities.

mod result;
mod traits;

pub use result::*;
pub use traits::*;

#[cfg(test)]
mod result_test;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 4: Commit**

```bash
git add -A
git commit -m "feat(tool): add Tool and ToolExecute traits"
```

---

### Task 8: Create tool registry

**Files:**
- Create: `src/tool/registry.rs`
- Modify: `src/tool/mod.rs`

**Step 1: Create src/tool/registry.rs**

```rust
// ABOUTME: Implements the Registry - a thread-safe container for discovering
// ABOUTME: and managing available tools at runtime.

use std::collections::HashMap;
use std::sync::Arc;

use tokio::sync::RwLock;

use super::Tool;
use crate::llm::ToolDefinition;

/// A thread-safe registry of tools.
#[derive(Default)]
pub struct Registry {
    tools: Arc<RwLock<HashMap<String, Arc<dyn Tool>>>>,
}

impl Registry {
    /// Create a new empty registry.
    pub fn new() -> Self {
        Self::default()
    }

    /// Register a tool.
    pub async fn register<T: Tool + 'static>(&self, tool: T) {
        self.register_arc(Arc::new(tool)).await;
    }

    /// Register a tool from an Arc.
    pub async fn register_arc(&self, tool: Arc<dyn Tool>) {
        let mut tools = self.tools.write().await;
        tools.insert(tool.name().to_string(), tool);
    }

    /// Unregister a tool by name.
    pub async fn unregister(&self, name: &str) {
        let mut tools = self.tools.write().await;
        tools.remove(name);
    }

    /// Get a tool by name.
    pub async fn get(&self, name: &str) -> Option<Arc<dyn Tool>> {
        let tools = self.tools.read().await;
        tools.get(name).cloned()
    }

    /// List all tool names, sorted alphabetically.
    pub async fn list(&self) -> Vec<String> {
        let tools = self.tools.read().await;
        let mut names: Vec<_> = tools.keys().cloned().collect();
        names.sort();
        names
    }

    /// Get all registered tools.
    pub async fn all(&self) -> Vec<Arc<dyn Tool>> {
        let tools = self.tools.read().await;
        tools.values().cloned().collect()
    }

    /// Get the number of registered tools.
    pub async fn count(&self) -> usize {
        let tools = self.tools.read().await;
        tools.len()
    }

    /// Convert all tools to LLM tool definitions.
    pub async fn to_definitions(&self) -> Vec<ToolDefinition> {
        let tools = self.tools.read().await;
        tools
            .values()
            .map(|t| ToolDefinition {
                name: t.name().to_string(),
                description: t.description().to_string(),
                input_schema: t.schema(),
            })
            .collect()
    }
}

impl Clone for Registry {
    fn clone(&self) -> Self {
        Self {
            tools: Arc::clone(&self.tools),
        }
    }
}
```

**Step 2: Update src/tool/mod.rs**

```rust
// ABOUTME: Tool module - defines tools, registry, and execution.
// ABOUTME: Core abstraction for agent capabilities.

mod registry;
mod result;
mod traits;

pub use registry::*;
pub use result::*;
pub use traits::*;

#[cfg(test)]
mod result_test;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 4: Commit**

```bash
git add -A
git commit -m "feat(tool): add thread-safe tool Registry"
```

---

### Task 9: Add registry tests

**Files:**
- Create: `src/tool/registry_test.rs`
- Modify: `src/tool/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for tool Registry - registration, lookup, thread safety.
// ABOUTME: Uses a mock tool for testing.

use super::*;

/// A simple test tool.
struct EchoTool;

#[async_trait::async_trait]
impl Tool for EchoTool {
    fn name(&self) -> &str {
        "echo"
    }

    fn description(&self) -> &str {
        "Echoes input back"
    }

    fn schema(&self) -> serde_json::Value {
        serde_json::json!({
            "type": "object",
            "properties": {
                "message": { "type": "string" }
            },
            "required": ["message"]
        })
    }

    async fn execute(&self, params: serde_json::Value) -> Result<ToolResult, anyhow::Error> {
        let message = params["message"].as_str().unwrap_or("");
        Ok(ToolResult::text(message))
    }
}

#[tokio::test]
async fn test_register_and_get() {
    let registry = Registry::new();
    registry.register(EchoTool).await;

    let tool = registry.get("echo").await;
    assert!(tool.is_some());
    assert_eq!(tool.unwrap().name(), "echo");
}

#[tokio::test]
async fn test_get_nonexistent() {
    let registry = Registry::new();
    let tool = registry.get("nonexistent").await;
    assert!(tool.is_none());
}

#[tokio::test]
async fn test_unregister() {
    let registry = Registry::new();
    registry.register(EchoTool).await;
    assert_eq!(registry.count().await, 1);

    registry.unregister("echo").await;
    assert_eq!(registry.count().await, 0);
    assert!(registry.get("echo").await.is_none());
}

#[tokio::test]
async fn test_list() {
    let registry = Registry::new();
    registry.register(EchoTool).await;

    let names = registry.list().await;
    assert_eq!(names, vec!["echo"]);
}

#[tokio::test]
async fn test_to_definitions() {
    let registry = Registry::new();
    registry.register(EchoTool).await;

    let defs = registry.to_definitions().await;
    assert_eq!(defs.len(), 1);
    assert_eq!(defs[0].name, "echo");
    assert_eq!(defs[0].description, "Echoes input back");
}

#[tokio::test]
async fn test_clone_shares_state() {
    let registry = Registry::new();
    let clone = registry.clone();

    registry.register(EchoTool).await;
    assert_eq!(clone.count().await, 1);
}
```

**Step 2: Update src/tool/mod.rs**

```rust
// ABOUTME: Tool module - defines tools, registry, and execution.
// ABOUTME: Core abstraction for agent capabilities.

mod registry;
mod result;
mod traits;

pub use registry::*;
pub use result::*;
pub use traits::*;

#[cfg(test)]
mod registry_test;
#[cfg(test)]
mod result_test;
```

**Step 3: Run tests**

Run: `cargo test tool`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(tool): add tests for Registry"
```

---

## Phase 4: Permission System

### Task 10: Create permission types

**Files:**
- Create: `src/permission/mod.rs`
- Create: `src/permission/policy.rs`
- Modify: `src/lib.rs`

**Step 1: Create src/permission/policy.rs**

```rust
// ABOUTME: Defines the policy engine - rules, decisions, and evaluation.
// ABOUTME: Supports globs, conditionals, and default policies.

use std::sync::Arc;

/// The decision made by a policy rule.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Decision {
    /// Allow the tool execution.
    Allow,
    /// Deny the tool execution.
    Deny,
    /// Ask the user for approval.
    Ask,
}

/// A condition function for conditional rules.
pub type ConditionFn = Arc<dyn Fn(&serde_json::Value) -> Decision + Send + Sync>;

/// A rule in the policy.
pub enum PolicyRule {
    /// Allow a specific tool by exact name.
    Allow(String),

    /// Deny a specific tool by exact name.
    Deny(String),

    /// Allow tools matching a glob pattern.
    AllowPattern(glob::Pattern),

    /// Deny tools matching a glob pattern.
    DenyPattern(glob::Pattern),

    /// Conditional rule based on parameters.
    Conditional {
        tool: String,
        condition: ConditionFn,
    },
}

/// A policy that evaluates tool execution requests.
pub struct Policy {
    rules: Vec<PolicyRule>,
    default: Decision,
}

impl Policy {
    /// Create a new policy builder.
    pub fn builder() -> PolicyBuilder {
        PolicyBuilder::new()
    }

    /// Evaluate whether a tool should be allowed.
    pub fn evaluate(&self, tool: &str, params: &serde_json::Value) -> Decision {
        for rule in &self.rules {
            match rule {
                PolicyRule::Allow(name) if name == tool => return Decision::Allow,
                PolicyRule::Deny(name) if name == tool => return Decision::Deny,
                PolicyRule::AllowPattern(pattern) if pattern.matches(tool) => {
                    return Decision::Allow
                }
                PolicyRule::DenyPattern(pattern) if pattern.matches(tool) => return Decision::Deny,
                PolicyRule::Conditional { tool: t, condition } if t == tool => {
                    return condition(params)
                }
                _ => continue,
            }
        }
        self.default
    }
}

impl Default for Policy {
    fn default() -> Self {
        Self {
            rules: Vec::new(),
            default: Decision::Deny,
        }
    }
}

/// Builder for constructing policies.
#[derive(Default)]
pub struct PolicyBuilder {
    rules: Vec<PolicyRule>,
    default: Decision,
}

impl PolicyBuilder {
    /// Create a new builder with default deny.
    pub fn new() -> Self {
        Self {
            rules: Vec::new(),
            default: Decision::Deny,
        }
    }

    /// Allow a tool by exact name.
    pub fn allow(mut self, tool: impl Into<String>) -> Self {
        self.rules.push(PolicyRule::Allow(tool.into()));
        self
    }

    /// Deny a tool by exact name.
    pub fn deny(mut self, tool: impl Into<String>) -> Self {
        self.rules.push(PolicyRule::Deny(tool.into()));
        self
    }

    /// Allow tools matching a glob pattern.
    pub fn allow_pattern(mut self, pattern: &str) -> Self {
        if let Ok(p) = glob::Pattern::new(pattern) {
            self.rules.push(PolicyRule::AllowPattern(p));
        }
        self
    }

    /// Deny tools matching a glob pattern.
    pub fn deny_pattern(mut self, pattern: &str) -> Self {
        if let Ok(p) = glob::Pattern::new(pattern) {
            self.rules.push(PolicyRule::DenyPattern(p));
        }
        self
    }

    /// Add a conditional rule.
    pub fn conditional<F>(mut self, tool: impl Into<String>, condition: F) -> Self
    where
        F: Fn(&serde_json::Value) -> Decision + Send + Sync + 'static,
    {
        self.rules.push(PolicyRule::Conditional {
            tool: tool.into(),
            condition: Arc::new(condition),
        });
        self
    }

    /// Set the default decision for unmatched tools.
    pub fn default(mut self, decision: Decision) -> Self {
        self.default = decision;
        self
    }

    /// Build the policy.
    pub fn build(self) -> Policy {
        Policy {
            rules: self.rules,
            default: self.default,
        }
    }
}
```

**Step 2: Create src/permission/mod.rs**

```rust
// ABOUTME: Permission module - policy engine for tool execution control.
// ABOUTME: Supports rules, patterns, conditionals, and approval handlers.

mod policy;

pub use policy::*;
```

**Step 3: Update src/lib.rs**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;
pub mod llm;
pub mod permission;
pub mod tool;

pub use error::MuxError;
```

**Step 4: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 5: Commit**

```bash
git add -A
git commit -m "feat(permission): add Policy and PolicyBuilder"
```

---

### Task 11: Add policy tests

**Files:**
- Create: `src/permission/policy_test.rs`
- Modify: `src/permission/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for Policy - rules, patterns, conditionals, defaults.
// ABOUTME: Verifies policy evaluation works correctly.

use super::*;

#[test]
fn test_allow_exact() {
    let policy = Policy::builder().allow("read_file").build();

    assert_eq!(
        policy.evaluate("read_file", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("write_file", &serde_json::json!({})),
        Decision::Deny
    );
}

#[test]
fn test_deny_exact() {
    let policy = Policy::builder()
        .deny("dangerous_tool")
        .default(Decision::Allow)
        .build();

    assert_eq!(
        policy.evaluate("dangerous_tool", &serde_json::json!({})),
        Decision::Deny
    );
    assert_eq!(
        policy.evaluate("safe_tool", &serde_json::json!({})),
        Decision::Allow
    );
}

#[test]
fn test_allow_pattern() {
    let policy = Policy::builder().allow_pattern("read_*").build();

    assert_eq!(
        policy.evaluate("read_file", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("read_dir", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("write_file", &serde_json::json!({})),
        Decision::Deny
    );
}

#[test]
fn test_deny_pattern() {
    let policy = Policy::builder()
        .deny_pattern("dangerous_*")
        .default(Decision::Allow)
        .build();

    assert_eq!(
        policy.evaluate("dangerous_delete", &serde_json::json!({})),
        Decision::Deny
    );
    assert_eq!(
        policy.evaluate("safe_operation", &serde_json::json!({})),
        Decision::Allow
    );
}

#[test]
fn test_conditional() {
    let policy = Policy::builder()
        .conditional("bash", |params| {
            let cmd = params["command"].as_str().unwrap_or("");
            if cmd.contains("rm -rf") {
                Decision::Ask
            } else {
                Decision::Allow
            }
        })
        .build();

    assert_eq!(
        policy.evaluate("bash", &serde_json::json!({"command": "ls -la"})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("bash", &serde_json::json!({"command": "rm -rf /"})),
        Decision::Ask
    );
}

#[test]
fn test_rule_order() {
    // First matching rule wins
    let policy = Policy::builder()
        .allow("tool")
        .deny("tool") // Should not be reached
        .build();

    assert_eq!(
        policy.evaluate("tool", &serde_json::json!({})),
        Decision::Allow
    );
}

#[test]
fn test_default_decision() {
    let allow_default = Policy::builder().default(Decision::Allow).build();
    let ask_default = Policy::builder().default(Decision::Ask).build();

    assert_eq!(
        allow_default.evaluate("any", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        ask_default.evaluate("any", &serde_json::json!({})),
        Decision::Ask
    );
}

#[test]
fn test_complex_policy() {
    let policy = Policy::builder()
        .allow("read_file")
        .allow("list_dir")
        .deny_pattern("dangerous_*")
        .allow_pattern("mcp_*")
        .conditional("bash", |params| {
            let cmd = params["command"].as_str().unwrap_or("");
            if cmd.starts_with("sudo") {
                Decision::Deny
            } else if cmd.contains("rm") {
                Decision::Ask
            } else {
                Decision::Allow
            }
        })
        .default(Decision::Ask)
        .build();

    assert_eq!(
        policy.evaluate("read_file", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("dangerous_delete", &serde_json::json!({})),
        Decision::Deny
    );
    assert_eq!(
        policy.evaluate("mcp_fetch", &serde_json::json!({})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("bash", &serde_json::json!({"command": "sudo rm -rf /"})),
        Decision::Deny
    );
    assert_eq!(
        policy.evaluate("bash", &serde_json::json!({"command": "rm file.txt"})),
        Decision::Ask
    );
    assert_eq!(
        policy.evaluate("unknown_tool", &serde_json::json!({})),
        Decision::Ask
    );
}
```

**Step 2: Update src/permission/mod.rs**

```rust
// ABOUTME: Permission module - policy engine for tool execution control.
// ABOUTME: Supports rules, patterns, conditionals, and approval handlers.

mod policy;

pub use policy::*;

#[cfg(test)]
mod policy_test;
```

**Step 3: Run tests**

Run: `cargo test permission`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(permission): add tests for Policy"
```

---

### Task 12: Add approval handler trait

**Files:**
- Create: `src/permission/handler.rs`
- Modify: `src/permission/mod.rs`

**Step 1: Create src/permission/handler.rs**

```rust
// ABOUTME: Defines the ApprovalHandler trait for async user approval.
// ABOUTME: Called when policy returns Decision::Ask.

use async_trait::async_trait;

/// Context provided to approval handlers.
#[derive(Debug, Clone)]
pub struct ApprovalContext {
    /// Description of the tool being executed.
    pub tool_description: String,

    /// Unique identifier for this approval request.
    pub request_id: String,
}

/// Trait for handling approval requests.
#[async_trait]
pub trait ApprovalHandler: Send + Sync {
    /// Request approval for a tool execution.
    ///
    /// Returns `Ok(true)` if approved, `Ok(false)` if rejected.
    async fn request_approval(
        &self,
        tool: &str,
        params: &serde_json::Value,
        context: &ApprovalContext,
    ) -> Result<bool, anyhow::Error>;
}

/// An approval handler that always approves.
pub struct AlwaysApprove;

#[async_trait]
impl ApprovalHandler for AlwaysApprove {
    async fn request_approval(
        &self,
        _tool: &str,
        _params: &serde_json::Value,
        _context: &ApprovalContext,
    ) -> Result<bool, anyhow::Error> {
        Ok(true)
    }
}

/// An approval handler that always rejects.
pub struct AlwaysReject;

#[async_trait]
impl ApprovalHandler for AlwaysReject {
    async fn request_approval(
        &self,
        _tool: &str,
        _params: &serde_json::Value,
        _context: &ApprovalContext,
    ) -> Result<bool, anyhow::Error> {
        Ok(false)
    }
}
```

**Step 2: Update src/permission/mod.rs**

```rust
// ABOUTME: Permission module - policy engine for tool execution control.
// ABOUTME: Supports rules, patterns, conditionals, and approval handlers.

mod handler;
mod policy;

pub use handler::*;
pub use policy::*;

#[cfg(test)]
mod policy_test;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 4: Commit**

```bash
git add -A
git commit -m "feat(permission): add ApprovalHandler trait"
```

---

## Phase 5: MCP Client

### Task 13: Create MCP types

**Files:**
- Create: `src/mcp/mod.rs`
- Create: `src/mcp/types.rs`
- Modify: `src/lib.rs`

**Step 1: Create src/mcp/types.rs**

```rust
// ABOUTME: Defines MCP protocol types - JSON-RPC 2.0 messages, tool info,
// ABOUTME: and server configuration structures.

use std::collections::HashMap;
use std::sync::atomic::{AtomicU64, Ordering};

use serde::{Deserialize, Serialize};

static REQUEST_ID: AtomicU64 = AtomicU64::new(1);

/// A JSON-RPC 2.0 request.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpRequest {
    pub jsonrpc: String,
    pub id: u64,
    pub method: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub params: Option<serde_json::Value>,
}

impl McpRequest {
    /// Create a new request with an auto-incrementing ID.
    pub fn new(method: impl Into<String>, params: Option<serde_json::Value>) -> Self {
        Self {
            jsonrpc: "2.0".to_string(),
            id: REQUEST_ID.fetch_add(1, Ordering::SeqCst),
            method: method.into(),
            params,
        }
    }
}

/// A JSON-RPC 2.0 response.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpResponse {
    pub jsonrpc: String,
    pub id: u64,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub result: Option<serde_json::Value>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub error: Option<McpRpcError>,
}

/// A JSON-RPC 2.0 error.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpRpcError {
    pub code: i32,
    pub message: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub data: Option<serde_json::Value>,
}

/// Information about an MCP tool.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpToolInfo {
    pub name: String,
    pub description: String,
    #[serde(rename = "inputSchema")]
    pub input_schema: serde_json::Value,
}

/// Result of listing tools.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpToolsListResult {
    pub tools: Vec<McpToolInfo>,
}

/// Parameters for calling a tool.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpToolCallParams {
    pub name: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub arguments: Option<serde_json::Value>,
}

/// Content block in a tool result.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum McpContentBlock {
    #[serde(rename = "text")]
    Text { text: String },
    #[serde(rename = "image")]
    Image {
        data: String,
        #[serde(rename = "mimeType")]
        mime_type: String,
    },
}

/// Result of calling a tool.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpToolResult {
    pub content: Vec<McpContentBlock>,
    #[serde(default, rename = "isError")]
    pub is_error: bool,
}

/// Transport configuration for MCP.
#[derive(Debug, Clone)]
pub enum McpTransport {
    /// Stdio transport - spawn a subprocess.
    Stdio {
        command: String,
        args: Vec<String>,
        env: HashMap<String, String>,
    },
    /// SSE transport - connect to HTTP endpoint.
    Sse { url: String },
}

/// Configuration for an MCP server.
#[derive(Debug, Clone)]
pub struct McpServerConfig {
    pub name: String,
    pub transport: McpTransport,
}

/// Client info for MCP handshake.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpClientInfo {
    pub name: String,
    pub version: String,
}

/// Parameters for MCP initialize.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpInitializeParams {
    #[serde(rename = "protocolVersion")]
    pub protocol_version: String,
    pub capabilities: serde_json::Value,
    #[serde(rename = "clientInfo")]
    pub client_info: McpClientInfo,
}

/// Server capabilities returned from initialize.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct McpServerCapabilities {
    #[serde(default)]
    pub tools: Option<serde_json::Value>,
    #[serde(default)]
    pub resources: Option<serde_json::Value>,
    #[serde(default)]
    pub prompts: Option<serde_json::Value>,
}

/// Initialize result.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpInitializeResult {
    #[serde(rename = "protocolVersion")]
    pub protocol_version: String,
    pub capabilities: McpServerCapabilities,
    #[serde(rename = "serverInfo")]
    pub server_info: Option<McpClientInfo>,
}
```

**Step 2: Create src/mcp/mod.rs**

```rust
// ABOUTME: MCP module - Model Context Protocol client implementation.
// ABOUTME: Connects to MCP servers and proxies their tools.

mod types;

pub use types::*;
```

**Step 3: Update src/lib.rs**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;
pub mod llm;
pub mod mcp;
pub mod permission;
pub mod tool;

pub use error::MuxError;
```

**Step 4: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 5: Commit**

```bash
git add -A
git commit -m "feat(mcp): add MCP protocol types"
```

---

### Task 14: Add MCP types tests

**Files:**
- Create: `src/mcp/types_test.rs`
- Modify: `src/mcp/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for MCP types - serialization, deserialization.
// ABOUTME: Verifies JSON format matches MCP protocol.

use super::*;

#[test]
fn test_request_serialization() {
    let req = McpRequest::new("tools/list", None);
    let json = serde_json::to_value(&req).unwrap();

    assert_eq!(json["jsonrpc"], "2.0");
    assert_eq!(json["method"], "tools/list");
    assert!(json["id"].as_u64().is_some());
}

#[test]
fn test_request_with_params() {
    let params = serde_json::json!({"name": "read_file", "arguments": {"path": "/tmp"}});
    let req = McpRequest::new("tools/call", Some(params.clone()));
    let json = serde_json::to_value(&req).unwrap();

    assert_eq!(json["params"], params);
}

#[test]
fn test_response_deserialization_success() {
    let json = r#"{
        "jsonrpc": "2.0",
        "id": 1,
        "result": {"tools": []}
    }"#;

    let resp: McpResponse = serde_json::from_str(json).unwrap();
    assert!(resp.result.is_some());
    assert!(resp.error.is_none());
}

#[test]
fn test_response_deserialization_error() {
    let json = r#"{
        "jsonrpc": "2.0",
        "id": 1,
        "error": {
            "code": -32600,
            "message": "Invalid Request"
        }
    }"#;

    let resp: McpResponse = serde_json::from_str(json).unwrap();
    assert!(resp.result.is_none());
    assert!(resp.error.is_some());
    assert_eq!(resp.error.unwrap().code, -32600);
}

#[test]
fn test_tool_info_deserialization() {
    let json = r#"{
        "name": "read_file",
        "description": "Read a file",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"}
            }
        }
    }"#;

    let info: McpToolInfo = serde_json::from_str(json).unwrap();
    assert_eq!(info.name, "read_file");
    assert_eq!(info.description, "Read a file");
}

#[test]
fn test_tool_result_deserialization() {
    let json = r#"{
        "content": [
            {"type": "text", "text": "file contents here"}
        ],
        "isError": false
    }"#;

    let result: McpToolResult = serde_json::from_str(json).unwrap();
    assert_eq!(result.content.len(), 1);
    assert!(!result.is_error);

    match &result.content[0] {
        McpContentBlock::Text { text } => assert_eq!(text, "file contents here"),
        _ => panic!("Expected text block"),
    }
}

#[test]
fn test_initialize_params_serialization() {
    let params = McpInitializeParams {
        protocol_version: "2024-11-05".to_string(),
        capabilities: serde_json::json!({}),
        client_info: McpClientInfo {
            name: "mux".to_string(),
            version: "0.1.0".to_string(),
        },
    };

    let json = serde_json::to_value(&params).unwrap();
    assert_eq!(json["protocolVersion"], "2024-11-05");
    assert_eq!(json["clientInfo"]["name"], "mux");
}

#[test]
fn test_request_ids_increment() {
    let req1 = McpRequest::new("test1", None);
    let req2 = McpRequest::new("test2", None);

    assert!(req2.id > req1.id);
}
```

**Step 2: Update src/mcp/mod.rs**

```rust
// ABOUTME: MCP module - Model Context Protocol client implementation.
// ABOUTME: Connects to MCP servers and proxies their tools.

mod types;

pub use types::*;

#[cfg(test)]
mod types_test;
```

**Step 3: Run tests**

Run: `cargo test mcp`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(mcp): add tests for MCP types"
```

---

## Phase 6: Integration & Cleanup

### Task 15: Add prelude module

**Files:**
- Create: `src/prelude.rs`
- Modify: `src/lib.rs`

**Step 1: Create src/prelude.rs**

```rust
// ABOUTME: Prelude module - convenient imports for common use cases.
// ABOUTME: Use `use mux::prelude::*;` to get started quickly.

pub use crate::error::{LlmError, McpError, MuxError, PermissionError, ToolError};
pub use crate::llm::{
    ContentBlock, LlmClient, Message, Request, Response, Role, StopReason, StreamEvent,
    ToolDefinition, Usage,
};
pub use crate::mcp::{McpServerConfig, McpToolInfo, McpToolResult, McpTransport};
pub use crate::permission::{
    AlwaysApprove, AlwaysReject, ApprovalContext, ApprovalHandler, Decision, Policy, PolicyBuilder,
};
pub use crate::tool::{Registry, Tool, ToolExecute, ToolResult};
```

**Step 2: Update src/lib.rs**

```rust
// ABOUTME: Root module for mux - agentic infrastructure library.
// ABOUTME: Re-exports all public types from submodules.

pub mod error;
pub mod llm;
pub mod mcp;
pub mod permission;
pub mod prelude;
pub mod tool;

pub use error::MuxError;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 4: Commit**

```bash
git add -A
git commit -m "feat: add prelude module for convenient imports"
```

---

### Task 16: Add integration test

**Files:**
- Create: `tests/integration.rs`

**Step 1: Create integration test**

```rust
// ABOUTME: Integration tests verifying modules work together.
// ABOUTME: Tests the full workflow without external dependencies.

use mux::prelude::*;

/// A test tool for integration testing.
struct GreetTool;

#[async_trait::async_trait]
impl Tool for GreetTool {
    fn name(&self) -> &str {
        "greet"
    }

    fn description(&self) -> &str {
        "Greet a person by name"
    }

    fn schema(&self) -> serde_json::Value {
        serde_json::json!({
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name to greet"
                }
            },
            "required": ["name"]
        })
    }

    async fn execute(&self, params: serde_json::Value) -> Result<ToolResult, anyhow::Error> {
        let name = params["name"]
            .as_str()
            .ok_or_else(|| anyhow::anyhow!("Missing name parameter"))?;
        Ok(ToolResult::text(format!("Hello, {}!", name)))
    }
}

#[tokio::test]
async fn test_registry_with_policy() {
    // Create registry and register tool
    let registry = Registry::new();
    registry.register(GreetTool).await;

    // Create policy
    let policy = Policy::builder()
        .allow("greet")
        .deny_pattern("dangerous_*")
        .default(Decision::Deny)
        .build();

    // Get tool and check policy
    let tool = registry.get("greet").await.expect("Tool should exist");
    let params = serde_json::json!({"name": "World"});

    let decision = policy.evaluate(tool.name(), &params);
    assert_eq!(decision, Decision::Allow);

    // Execute tool
    let result = tool.execute(params).await.expect("Execution should succeed");
    assert_eq!(result.content, "Hello, World!");
    assert!(!result.is_error);
}

#[tokio::test]
async fn test_tool_definitions_for_llm() {
    let registry = Registry::new();
    registry.register(GreetTool).await;

    let definitions = registry.to_definitions().await;
    assert_eq!(definitions.len(), 1);

    let def = &definitions[0];
    assert_eq!(def.name, "greet");
    assert_eq!(def.description, "Greet a person by name");
    assert!(def.input_schema["properties"]["name"].is_object());
}

#[tokio::test]
async fn test_message_construction() {
    let user_msg = Message::user("Hello");
    let assistant_msg = Message::assistant("Hi there!");

    assert_eq!(user_msg.role, Role::User);
    assert_eq!(assistant_msg.role, Role::Assistant);
}

#[tokio::test]
async fn test_request_building() {
    let registry = Registry::new();
    registry.register(GreetTool).await;

    let request = Request::new("claude-sonnet-4-20250514")
        .message(Message::user("Greet Alice"))
        .tools(registry.to_definitions().await)
        .system("You are helpful")
        .max_tokens(1024);

    assert_eq!(request.model, "claude-sonnet-4-20250514");
    assert_eq!(request.messages.len(), 1);
    assert_eq!(request.tools.len(), 1);
    assert_eq!(request.system, Some("You are helpful".to_string()));
}

#[tokio::test]
async fn test_conditional_policy() {
    let policy = Policy::builder()
        .conditional("greet", |params| {
            let name = params["name"].as_str().unwrap_or("");
            if name.is_empty() {
                Decision::Deny
            } else {
                Decision::Allow
            }
        })
        .default(Decision::Deny)
        .build();

    assert_eq!(
        policy.evaluate("greet", &serde_json::json!({"name": "Alice"})),
        Decision::Allow
    );
    assert_eq!(
        policy.evaluate("greet", &serde_json::json!({"name": ""})),
        Decision::Deny
    );
}
```

**Step 2: Run integration tests**

Run: `cargo test --test integration`
Expected: All tests pass

**Step 3: Commit**

```bash
git add -A
git commit -m "test: add integration tests"
```

---

### Task 17: Run all tests and verify

**Step 1: Run full test suite**

Run: `cargo test`
Expected: All tests pass

**Step 2: Run clippy**

Run: `cargo clippy -- -D warnings`
Expected: No warnings

**Step 3: Check formatting**

Run: `cargo fmt -- --check`
Expected: No formatting issues (or run `cargo fmt` to fix)

**Step 4: Final commit if any fixes needed**

```bash
git add -A
git commit -m "chore: fix clippy and formatting issues"
```

---

### Task 18: Update README

**Files:**
- Create: `README.md`

**Step 1: Create README.md**

```markdown
# mux

Agentic infrastructure for Rust. Tool execution, MCP integration, permission-gated approval flows, and orchestration.

## Installation

```toml
[dependencies]
mux = "0.1"
```

## Features

- **Tool Execution**: Define and execute tools with structured input/output handling
- **MCP Integration**: Model Context Protocol client for connecting to external tool servers
- **Permission-Gated Approvals**: Policy engine with patterns, conditionals, and async approval handlers
- **Type Safety**: Leverages Rust's type system for reliable tool definitions
- **Async-First**: Built on tokio for high-performance async operations

## Quick Start

```rust
use mux::prelude::*;

#[derive(Tool)]
#[tool(name = "greet", description = "Greet a person")]
struct Greet {
    #[tool(description = "Name to greet")]
    name: String,
}

#[async_trait::async_trait]
impl ToolExecute for Greet {
    async fn execute(&self) -> Result<ToolResult, anyhow::Error> {
        Ok(ToolResult::text(format!("Hello, {}!", self.name)))
    }
}

#[tokio::main]
async fn main() -> Result<(), mux::MuxError> {
    let registry = Registry::new();
    registry.register(Greet { name: String::new() }).await;

    let policy = Policy::builder()
        .allow("greet")
        .default(Decision::Deny)
        .build();

    Ok(())
}
```

## Status

Under active development. API subject to change.

## License

MIT
```

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add README"
```

---

### Task 19: Merge to main

**Step 1: Check all tests pass**

Run: `cargo test`
Expected: All tests pass

**Step 2: Merge feature branch**

```bash
git checkout main
git merge feature/initial-implementation
```

**Step 3: Verify**

Run: `cargo test`
Expected: All tests pass on main

---

## Future Phases (Not in this plan)

These are documented for reference but will be separate implementation plans:

- **Phase 7**: Anthropic LLM client implementation
- **Phase 8**: OpenAI LLM client implementation
- **Phase 9**: MCP client implementation (stdio transport)
- **Phase 10**: `#[derive(Tool)]` proc macro
- **Phase 11**: MCP SSE transport
