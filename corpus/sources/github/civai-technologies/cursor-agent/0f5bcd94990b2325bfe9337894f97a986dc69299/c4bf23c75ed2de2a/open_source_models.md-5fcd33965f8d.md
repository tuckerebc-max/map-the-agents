# Open-Source Model Support

The Cursor Agent provides robust support for open-source language models, giving you alternatives to proprietary cloud-based AI services. This allows for more control over your data, reduced costs, and flexibility in your AI stack.

## Supported Open-Source Integrations

Currently, the Cursor Agent supports the following open-source model providers:

### [Ollama](https://ollama.ai)

Ollama provides a simple way to run open-source large language models locally. The Cursor Agent has native integration with Ollama, supporting the full range of features including chat, tool calling, and multimodal capabilities.

For comprehensive documentation on using Ollama with the Cursor Agent, see our [Ollama Integration Guide](ollama_integration.md).

**Key Features:**
- Run models locally for complete privacy
- No API keys or quotas to manage
- Support for a wide range of open-source models
- Multimodal capabilities with supported models
- Full access to all agent tools and functions

**Popular Models:**
- Llama 3/3.1 (Meta)
- Mistral (Mistral AI)
- Gemma 3 (Google)
- Phi-4 (Microsoft)
- Qwen 2.5 (Alibaba)

## Benefits of Open-Source Models

### Privacy and Data Security

When using open-source models locally, your data never leaves your device. This makes them suitable for handling sensitive or proprietary information that shouldn't be shared with external services.

### Cost Efficiency

Local models don't incur per-token or per-query costs, making them more economical for high-volume use cases.

### Offline Capability

Local models can operate without an internet connection, making them suitable for environments with limited connectivity.

### Customization

Open-source models can be fine-tuned or adapted to specific domains and use cases.

## Getting Started

To get started with open-source models in the Cursor Agent, follow these steps:

1. Choose your preferred model provider (currently Ollama)
2. Set up the provider according to their documentation
3. Install the required packages for the Cursor Agent
4. Configure the agent to use your chosen model

For detailed instructions on setting up and using Ollama, please see the [Ollama Integration Guide](ollama_integration.md).

## Example Usage

```python
import asyncio
from cursor_agent_tools import create_agent

async def main():
    # Create an agent with an open-source model
    agent = create_agent(model="ollama-llama3")
    
    # Use it just like any other model
    response = await agent.chat("Explain the advantages of open-source AI models")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

## Future Integrations

We plan to expand our support for open-source models in the future, potentially including:

- Direct GGUF model loading
- vLLM integration
- Text Generation Inference (TGI) support
- LocalAI compatibility

If there's a specific open-source model provider you'd like to see supported, please open an issue on our GitHub repository.

## Limitations

While open-source models provide many benefits, there are some trade-offs to consider:

1. **Resource Requirements**: Local models require sufficient hardware resources (RAM, GPU, etc.)
2. **Performance**: Some open-source models may not match the capabilities of state-of-the-art proprietary models
3. **Tool Support**: Not all models support structured tool calling equally well
4. **Multimodal Support**: Vision capabilities are limited to specific models

For more specific limitations related to Ollama, refer to the [Ollama Integration Guide](ollama_integration.md). 