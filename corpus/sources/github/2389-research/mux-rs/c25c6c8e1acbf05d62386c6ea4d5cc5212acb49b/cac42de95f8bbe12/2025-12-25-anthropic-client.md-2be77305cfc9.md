# Anthropic Client Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement AnthropicClient that connects to Claude API and implements the LlmClient trait.

**Architecture:** HTTP client using reqwest with SSE streaming support. Serialize our Request type to Anthropic's format, deserialize responses back. Handle both synchronous and streaming modes.

**Tech Stack:** reqwest (already in deps), futures-util for streaming, serde for (de)serialization.

---

## Task 1: Create Anthropic request/response types

**Files:**
- Create: `src/llm/anthropic.rs`
- Modify: `src/llm/mod.rs`

**Step 1: Create the Anthropic module with API types**

```rust
// ABOUTME: Anthropic Claude API client implementation.
// ABOUTME: Implements LlmClient trait for Claude models.

use serde::{Deserialize, Serialize};

/// Anthropic API request format.
#[derive(Debug, Serialize)]
pub struct AnthropicRequest {
    pub model: String,
    pub messages: Vec<AnthropicMessage>,
    pub max_tokens: u32,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub system: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub temperature: Option<f64>,
    #[serde(skip_serializing_if = "Vec::is_empty")]
    pub tools: Vec<AnthropicTool>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub stream: Option<bool>,
}

/// Anthropic message format.
#[derive(Debug, Serialize)]
pub struct AnthropicMessage {
    pub role: String,
    pub content: Vec<AnthropicContent>,
}

/// Anthropic content block.
#[derive(Debug, Serialize, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum AnthropicContent {
    Text { text: String },
    ToolUse { id: String, name: String, input: serde_json::Value },
    ToolResult { tool_use_id: String, content: String, #[serde(default)] is_error: bool },
}

/// Anthropic tool definition.
#[derive(Debug, Serialize)]
pub struct AnthropicTool {
    pub name: String,
    pub description: String,
    pub input_schema: serde_json::Value,
}

/// Anthropic API response format.
#[derive(Debug, Deserialize)]
pub struct AnthropicResponse {
    pub id: String,
    pub content: Vec<AnthropicContent>,
    pub stop_reason: String,
    pub model: String,
    pub usage: AnthropicUsage,
}

/// Anthropic usage stats.
#[derive(Debug, Deserialize)]
pub struct AnthropicUsage {
    pub input_tokens: u32,
    pub output_tokens: u32,
}

/// Anthropic API error response.
#[derive(Debug, Deserialize)]
pub struct AnthropicError {
    #[serde(rename = "type")]
    pub error_type: String,
    pub error: AnthropicErrorDetail,
}

#[derive(Debug, Deserialize)]
pub struct AnthropicErrorDetail {
    #[serde(rename = "type")]
    pub error_type: String,
    pub message: String,
}
```

**Step 2: Update src/llm/mod.rs**

Add to the module declarations:
```rust
mod anthropic;
pub use anthropic::AnthropicClient;
```

**Step 3: Run cargo check**

Run: `cargo check`
Expected: Compiles (warnings about unused ok)

**Step 4: Commit**

```bash
git add -A
git commit -m "feat(llm): add Anthropic API types"
```

---

## Task 2: Add conversion functions

**Files:**
- Modify: `src/llm/anthropic.rs`

**Step 1: Add From implementations for type conversion**

Add after the type definitions:

```rust
use super::{ContentBlock, Message, Request, Response, StopReason, ToolDefinition, Usage};

impl From<&ContentBlock> for AnthropicContent {
    fn from(block: &ContentBlock) -> Self {
        match block {
            ContentBlock::Text { text } => AnthropicContent::Text { text: text.clone() },
            ContentBlock::ToolUse { id, name, input } => AnthropicContent::ToolUse {
                id: id.clone(),
                name: name.clone(),
                input: input.clone(),
            },
            ContentBlock::ToolResult { tool_use_id, content, is_error } => {
                AnthropicContent::ToolResult {
                    tool_use_id: tool_use_id.clone(),
                    content: content.clone(),
                    is_error: *is_error,
                }
            }
        }
    }
}

impl From<AnthropicContent> for ContentBlock {
    fn from(content: AnthropicContent) -> Self {
        match content {
            AnthropicContent::Text { text } => ContentBlock::Text { text },
            AnthropicContent::ToolUse { id, name, input } => ContentBlock::ToolUse { id, name, input },
            AnthropicContent::ToolResult { tool_use_id, content, is_error } => {
                ContentBlock::ToolResult { tool_use_id, content, is_error }
            }
        }
    }
}

impl From<&Message> for AnthropicMessage {
    fn from(msg: &Message) -> Self {
        AnthropicMessage {
            role: match msg.role {
                super::Role::User => "user".to_string(),
                super::Role::Assistant => "assistant".to_string(),
            },
            content: msg.content.iter().map(AnthropicContent::from).collect(),
        }
    }
}

impl From<&ToolDefinition> for AnthropicTool {
    fn from(tool: &ToolDefinition) -> Self {
        AnthropicTool {
            name: tool.name.clone(),
            description: tool.description.clone(),
            input_schema: tool.input_schema.clone(),
        }
    }
}

impl From<&Request> for AnthropicRequest {
    fn from(req: &Request) -> Self {
        AnthropicRequest {
            model: req.model.clone(),
            messages: req.messages.iter().map(AnthropicMessage::from).collect(),
            max_tokens: req.max_tokens.unwrap_or(4096),
            system: req.system.clone(),
            temperature: req.temperature,
            tools: req.tools.iter().map(AnthropicTool::from).collect(),
            stream: None,
        }
    }
}

fn parse_stop_reason(s: &str) -> StopReason {
    match s {
        "end_turn" => StopReason::EndTurn,
        "tool_use" => StopReason::ToolUse,
        "max_tokens" => StopReason::MaxTokens,
        _ => StopReason::EndTurn,
    }
}

impl From<AnthropicResponse> for Response {
    fn from(resp: AnthropicResponse) -> Self {
        Response {
            id: resp.id,
            content: resp.content.into_iter().map(ContentBlock::from).collect(),
            stop_reason: parse_stop_reason(&resp.stop_reason),
            model: resp.model,
            usage: Usage {
                input_tokens: resp.usage.input_tokens,
                output_tokens: resp.usage.output_tokens,
            },
        }
    }
}
```

**Step 2: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 3: Commit**

```bash
git add -A
git commit -m "feat(llm): add type conversions for Anthropic API"
```

---

## Task 3: Implement AnthropicClient struct

**Files:**
- Modify: `src/llm/anthropic.rs`

**Step 1: Add the client struct and constructor**

Add at the end of the file:

```rust
use crate::error::LlmError;

const ANTHROPIC_API_URL: &str = "https://api.anthropic.com/v1/messages";
const ANTHROPIC_VERSION: &str = "2023-06-01";

/// Client for the Anthropic Claude API.
#[derive(Debug, Clone)]
pub struct AnthropicClient {
    api_key: String,
    http: reqwest::Client,
}

impl AnthropicClient {
    /// Create a new Anthropic client with the given API key.
    pub fn new(api_key: impl Into<String>) -> Self {
        Self {
            api_key: api_key.into(),
            http: reqwest::Client::new(),
        }
    }

    /// Create a new Anthropic client from the ANTHROPIC_API_KEY environment variable.
    pub fn from_env() -> Result<Self, LlmError> {
        let api_key = std::env::var("ANTHROPIC_API_KEY").map_err(|_| LlmError::Api {
            status: 0,
            message: "ANTHROPIC_API_KEY environment variable not set".to_string(),
        })?;
        Ok(Self::new(api_key))
    }
}
```

**Step 2: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 3: Commit**

```bash
git add -A
git commit -m "feat(llm): add AnthropicClient struct"
```

---

## Task 4: Implement create_message (non-streaming)

**Files:**
- Modify: `src/llm/anthropic.rs`

**Step 1: Add the LlmClient trait implementation**

Add the imports at the top:
```rust
use async_trait::async_trait;
use futures::Stream;
use std::pin::Pin;
use super::client::StreamEvent;
```

Add the implementation:

```rust
#[async_trait]
impl super::client::LlmClient for AnthropicClient {
    async fn create_message(&self, req: &Request) -> Result<Response, LlmError> {
        let anthropic_req = AnthropicRequest::from(req);

        let response = self
            .http
            .post(ANTHROPIC_API_URL)
            .header("x-api-key", &self.api_key)
            .header("anthropic-version", ANTHROPIC_VERSION)
            .header("content-type", "application/json")
            .json(&anthropic_req)
            .send()
            .await?;

        let status = response.status();
        if !status.is_success() {
            let error: AnthropicError = response.json().await?;
            return Err(LlmError::Api {
                status: status.as_u16(),
                message: error.error.message,
            });
        }

        let anthropic_resp: AnthropicResponse = response.json().await?;
        Ok(Response::from(anthropic_resp))
    }

    fn create_message_stream(
        &self,
        _req: &Request,
    ) -> Pin<Box<dyn Stream<Item = Result<StreamEvent, LlmError>> + Send + 'static>> {
        // TODO: Implement streaming in next task
        Box::pin(futures::stream::empty())
    }
}
```

**Step 2: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 3: Commit**

```bash
git add -A
git commit -m "feat(llm): implement create_message for AnthropicClient"
```

---

## Task 5: Add tests for Anthropic client

**Files:**
- Create: `src/llm/anthropic_test.rs`
- Modify: `src/llm/mod.rs`

**Step 1: Create test file**

```rust
// ABOUTME: Tests for Anthropic client type conversions.
// ABOUTME: Verifies serialization matches Anthropic API format.

use super::*;
use anthropic::*;

#[test]
fn test_request_serialization() {
    let req = Request::new("claude-sonnet-4-20250514")
        .message(Message::user("Hello"))
        .system("You are helpful")
        .max_tokens(1024);

    let anthropic_req = AnthropicRequest::from(&req);

    assert_eq!(anthropic_req.model, "claude-sonnet-4-20250514");
    assert_eq!(anthropic_req.max_tokens, 1024);
    assert_eq!(anthropic_req.system, Some("You are helpful".to_string()));
    assert_eq!(anthropic_req.messages.len(), 1);
    assert_eq!(anthropic_req.messages[0].role, "user");
}

#[test]
fn test_request_json_format() {
    let req = Request::new("claude-sonnet-4-20250514")
        .message(Message::user("Hello"));

    let anthropic_req = AnthropicRequest::from(&req);
    let json = serde_json::to_value(&anthropic_req).unwrap();

    assert_eq!(json["model"], "claude-sonnet-4-20250514");
    assert_eq!(json["messages"][0]["role"], "user");
    assert_eq!(json["messages"][0]["content"][0]["type"], "text");
    assert_eq!(json["messages"][0]["content"][0]["text"], "Hello");
}

#[test]
fn test_tool_serialization() {
    let tool = ToolDefinition {
        name: "greet".to_string(),
        description: "Greet someone".to_string(),
        input_schema: serde_json::json!({
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        }),
    };

    let anthropic_tool = AnthropicTool::from(&tool);
    let json = serde_json::to_value(&anthropic_tool).unwrap();

    assert_eq!(json["name"], "greet");
    assert_eq!(json["description"], "Greet someone");
    assert!(json["input_schema"]["properties"]["name"].is_object());
}

#[test]
fn test_response_deserialization() {
    let json = r#"{
        "id": "msg_123",
        "content": [{"type": "text", "text": "Hello!"}],
        "stop_reason": "end_turn",
        "model": "claude-sonnet-4-20250514",
        "usage": {"input_tokens": 10, "output_tokens": 5}
    }"#;

    let anthropic_resp: AnthropicResponse = serde_json::from_str(json).unwrap();
    let response = Response::from(anthropic_resp);

    assert_eq!(response.id, "msg_123");
    assert_eq!(response.text(), "Hello!");
    assert_eq!(response.stop_reason, StopReason::EndTurn);
    assert_eq!(response.usage.input_tokens, 10);
}

#[test]
fn test_tool_use_response() {
    let json = r#"{
        "id": "msg_456",
        "content": [
            {"type": "text", "text": "Let me greet you."},
            {"type": "tool_use", "id": "tu_1", "name": "greet", "input": {"name": "Alice"}}
        ],
        "stop_reason": "tool_use",
        "model": "claude-sonnet-4-20250514",
        "usage": {"input_tokens": 20, "output_tokens": 15}
    }"#;

    let anthropic_resp: AnthropicResponse = serde_json::from_str(json).unwrap();
    let response = Response::from(anthropic_resp);

    assert!(response.has_tool_use());
    assert_eq!(response.stop_reason, StopReason::ToolUse);
    assert_eq!(response.tool_uses().len(), 1);
}

#[test]
fn test_tool_result_message() {
    let msg = Message::tool_results(vec![
        ContentBlock::tool_result("tu_1", "Hello, Alice!"),
    ]);

    let anthropic_msg = AnthropicMessage::from(&msg);
    let json = serde_json::to_value(&anthropic_msg).unwrap();

    assert_eq!(json["role"], "user");
    assert_eq!(json["content"][0]["type"], "tool_result");
    assert_eq!(json["content"][0]["tool_use_id"], "tu_1");
    assert_eq!(json["content"][0]["content"], "Hello, Alice!");
}

#[test]
fn test_client_from_env_missing() {
    // Temporarily unset the env var if it exists
    let original = std::env::var("ANTHROPIC_API_KEY").ok();
    std::env::remove_var("ANTHROPIC_API_KEY");

    let result = AnthropicClient::from_env();
    assert!(result.is_err());

    // Restore if it was set
    if let Some(val) = original {
        std::env::set_var("ANTHROPIC_API_KEY", val);
    }
}
```

**Step 2: Update src/llm/mod.rs**

Add the test module:
```rust
#[cfg(test)]
mod anthropic_test;
```

**Step 3: Run tests**

Run: `cargo test anthropic`
Expected: All tests pass

**Step 4: Commit**

```bash
git add -A
git commit -m "test(llm): add Anthropic client tests"
```

---

## Task 6: Implement streaming support

**Files:**
- Modify: `src/llm/anthropic.rs`

**Step 1: Add streaming event types**

Add after AnthropicError:

```rust
/// Server-sent event from Anthropic streaming API.
#[derive(Debug, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum AnthropicStreamEvent {
    MessageStart {
        message: AnthropicMessageStart,
    },
    ContentBlockStart {
        index: usize,
        content_block: AnthropicContent,
    },
    ContentBlockDelta {
        index: usize,
        delta: AnthropicDelta,
    },
    ContentBlockStop {
        index: usize,
    },
    MessageDelta {
        delta: AnthropicMessageDeltaData,
        usage: AnthropicUsage,
    },
    MessageStop,
    Ping,
    Error {
        error: AnthropicErrorDetail,
    },
}

#[derive(Debug, Deserialize)]
pub struct AnthropicMessageStart {
    pub id: String,
    pub model: String,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum AnthropicDelta {
    TextDelta { text: String },
    InputJsonDelta { partial_json: String },
}

#[derive(Debug, Deserialize)]
pub struct AnthropicMessageDeltaData {
    pub stop_reason: Option<String>,
}
```

**Step 2: Update create_message_stream implementation**

Replace the streaming implementation:

```rust
fn create_message_stream(
    &self,
    req: &Request,
) -> Pin<Box<dyn Stream<Item = Result<StreamEvent, LlmError>> + Send + 'static>> {
    let mut anthropic_req = AnthropicRequest::from(req);
    anthropic_req.stream = Some(true);

    let api_key = self.api_key.clone();
    let http = self.http.clone();

    Box::pin(async_stream::try_stream! {
        let response = http
            .post(ANTHROPIC_API_URL)
            .header("x-api-key", &api_key)
            .header("anthropic-version", ANTHROPIC_VERSION)
            .header("content-type", "application/json")
            .json(&anthropic_req)
            .send()
            .await?;

        let status = response.status();
        if !status.is_success() {
            let error: AnthropicError = response.json().await?;
            Err(LlmError::Api {
                status: status.as_u16(),
                message: error.error.message,
            })?;
        }

        let mut stream = response.bytes_stream();
        let mut buffer = String::new();

        while let Some(chunk) = futures::StreamExt::next(&mut stream).await {
            let chunk = chunk?;
            buffer.push_str(&String::from_utf8_lossy(&chunk));

            // Process complete SSE events
            while let Some(pos) = buffer.find("\n\n") {
                let event_str = buffer[..pos].to_string();
                buffer = buffer[pos + 2..].to_string();

                if let Some(event) = parse_sse_event(&event_str) {
                    yield event;
                }
            }
        }
    })
}
```

**Step 3: Add SSE parsing helper**

```rust
fn parse_sse_event(event_str: &str) -> Option<StreamEvent> {
    let mut event_type = None;
    let mut data = None;

    for line in event_str.lines() {
        if let Some(rest) = line.strip_prefix("event: ") {
            event_type = Some(rest.to_string());
        } else if let Some(rest) = line.strip_prefix("data: ") {
            data = Some(rest.to_string());
        }
    }

    let data = data?;
    let anthropic_event: AnthropicStreamEvent = serde_json::from_str(&data).ok()?;

    match anthropic_event {
        AnthropicStreamEvent::MessageStart { message } => Some(StreamEvent::MessageStart {
            id: message.id,
            model: message.model,
        }),
        AnthropicStreamEvent::ContentBlockStart { index, content_block } => {
            Some(StreamEvent::ContentBlockStart {
                index,
                block: ContentBlock::from(content_block),
            })
        }
        AnthropicStreamEvent::ContentBlockDelta { index, delta } => {
            let text = match delta {
                AnthropicDelta::TextDelta { text } => text,
                AnthropicDelta::InputJsonDelta { partial_json } => partial_json,
            };
            Some(StreamEvent::ContentBlockDelta { index, text })
        }
        AnthropicStreamEvent::ContentBlockStop { index } => {
            Some(StreamEvent::ContentBlockStop { index })
        }
        AnthropicStreamEvent::MessageDelta { delta, usage } => Some(StreamEvent::MessageDelta {
            stop_reason: delta.stop_reason.map(|s| parse_stop_reason(&s)),
            usage: Usage {
                input_tokens: usage.input_tokens,
                output_tokens: usage.output_tokens,
            },
        }),
        AnthropicStreamEvent::MessageStop => Some(StreamEvent::MessageStop),
        AnthropicStreamEvent::Ping => None,
        AnthropicStreamEvent::Error { error } => {
            // Log error but don't yield - let the stream end
            eprintln!("Stream error: {}", error.message);
            None
        }
    }
}
```

**Step 4: Add async-stream dependency**

Run: `cargo add async-stream`

**Step 5: Run cargo check**

Run: `cargo check`
Expected: Compiles successfully

**Step 6: Commit**

```bash
git add -A
git commit -m "feat(llm): implement streaming for AnthropicClient"
```

---

## Task 7: Update prelude and run final tests

**Files:**
- Modify: `src/prelude.rs`

**Step 1: Add AnthropicClient to prelude**

Add to the llm re-exports:
```rust
pub use crate::llm::AnthropicClient;
```

**Step 2: Run all tests**

Run: `cargo test`
Expected: All tests pass

**Step 3: Run clippy**

Run: `cargo clippy`
Expected: No warnings

**Step 4: Format**

Run: `cargo fmt`

**Step 5: Commit**

```bash
git add -A
git commit -m "feat: add AnthropicClient to prelude"
```

---

## Task 8: Add integration test with mock (optional)

**Files:**
- Modify: `tests/integration.rs`

**Step 1: Add Anthropic client construction test**

Add to integration tests:

```rust
#[test]
fn test_anthropic_client_construction() {
    let client = mux::llm::AnthropicClient::new("test-api-key");
    // Just verify it constructs without panicking
    let _ = client;
}
```

**Step 2: Run tests**

Run: `cargo test`
Expected: All tests pass

**Step 3: Commit**

```bash
git add -A
git commit -m "test: add Anthropic client integration test"
```
