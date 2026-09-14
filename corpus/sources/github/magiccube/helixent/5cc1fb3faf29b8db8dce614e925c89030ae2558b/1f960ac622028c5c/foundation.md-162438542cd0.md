# Foundation

The `foundation` layer (`src/foundation/`) provides the core primitives that the rest of Helixent builds on: **messages**, **models**, and **tools**.

## Messages

`src/foundation/messages/`

A single `Message` union type flows end-to-end through the system. Every message has a **role** and typed **content**:

| Role | Type | Content |
|---|---|---|
| `system` | `SystemMessage` | `TextContent[]` |
| `user` | `UserMessage` | `TextContent \| ImageURLContent` |
| `assistant` | `AssistantMessage` | `TextContent`, `ThinkingContent`, `ToolUseContent` |
| `tool` | `ToolMessage` | `ToolResultContent[]` |

Key content types:

- **`TextContent`** — plain UTF-8 text.
- **`ImageURLContent`** — image reference with URL and optional detail level (`auto | high | low`).
- **`ThinkingContent`** — model chain-of-thought / reasoning.
- **`ToolUseContent<T>`** — a tool invocation (`id`, `name`, typed `input`).
- **`ToolResultContent`** — the string result of a tool call, keyed by `tool_use_id`.

`AssistantMessage` also carries optional `TokenUsage` (`promptTokens`, `completionTokens`, `totalTokens`) and a `streaming` flag.

## Models

`src/foundation/models/`

### `ModelProvider` (interface)

The provider-facing contract. Implement this to add a new backend:

```ts
interface ModelProvider {
  invoke(params: ModelProviderInvokeParams): Promise<AssistantMessage>
  stream(params: ModelProviderInvokeParams): AsyncGenerator<AssistantMessage>
}
```

`ModelProviderInvokeParams` bundles `model`, `messages`, optional `tools`, provider-specific `options`, and an `AbortSignal`.

### `Model` (class)

A thin orchestration wrapper. Constructed with a name, a `ModelProvider`, and optional provider-specific options. Exposes two methods:

- `invoke(context: ModelContext)` — single completion.
- `stream(context: ModelContext)` — streaming completion.

`ModelContext` carries the system `prompt`, the `NonSystemMessage[]` transcript, optional `tools`, and an `AbortSignal`.

## Tools

`src/foundation/tools/`

### `FunctionTool<P, R>`

A typed tool definition:

```ts
interface FunctionTool<P extends ZodType, R> {
  name: string
  description: string
  parameters: P          // Zod schema
  invoke: (input: z.infer<P>, signal?: AbortSignal) => Promise<R>
}
```

Use the `defineTool()` helper to create tools with full type inference.

## Community: OpenAI Provider

`src/community/openai/`

`OpenAIModelProvider` implements `ModelProvider` using the `openai` SDK (Chat Completions with function tools). It accepts optional `baseURL` and `apiKey` and defaults to `temperature: 0`, `top_p: 0`.

Internals:

- **`convertToOpenAIMessages`** — maps foundation messages to OpenAI's `ChatCompletionMessageParam[]`. Thinking content is dropped; `ToolUseContent` becomes `tool_calls`.
- **`convertToOpenAITools`** — converts `FunctionTool` definitions via `parameters.toJSONSchema()`.
- **`parseAssistantMessage`** — extracts `reasoning_content` as thinking, text, tool calls, and usage from an OpenAI response.
- **`StreamAccumulator`** — incrementally merges streaming chunks into an `AssistantMessage` snapshot, handling partial tool-call JSON and token usage.
