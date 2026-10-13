# Ollama Integration

The Cursor Agent supports local open-source models through [Ollama](https://ollama.ai/), providing a cost-effective alternative to cloud-based AI services while maintaining privacy and control over your data.

## Overview

Ollama allows you to run powerful large language models locally on your machine. The Cursor Agent natively integrates with Ollama, supporting the full range of agent capabilities including:

- Basic chat functionality
- Tool calling and function execution
- Multimodal capabilities (for supported models)
- File operations and code generation

## Prerequisites

1. **Install Ollama**: Follow the installation instructions on the [Ollama website](https://ollama.ai/).
2. **Pull Models**: Download the models you want to use:
   ```bash
   ollama pull llama3     # Meta's Llama 3 model
   ollama pull mistral    # Mistral AI's model
   ollama pull gemma3     # Google's Gemma model
   ```
3. **Install Python Package**:
   ```bash
   pip install ollama
   ```

## Configuration

### Basic Setup

```python
from cursor_agent_tools import create_agent

# Create an Ollama agent
agent = create_agent(
    model="ollama-llama3",  # Prefix with "ollama-" followed by model name
    host="http://localhost:11434",  # Optional, this is the default
    temperature=0.2  # Optional temperature setting
)
```

### Environment Variables

You can set the Ollama host using environment variables:

```bash
# In your .env file or shell
OLLAMA_HOST=http://localhost:11434
```

The Cursor Agent will use the following priority order for determining the Ollama host:
1. Explicit `host` parameter in `create_agent()`
2. `OLLAMA_HOST` environment variable
3. Default value: `http://localhost:11434`

## Supported Models

The agent works with any model available in Ollama. Some popular options include:

| Model | Description | Command |
|-------|-------------|---------|
| llama3 | Meta's Llama 3 8B model | `ollama pull llama3` |
| llama3.1 | Meta's Llama 3.1 8B model | `ollama pull llama3.1` |
| mistral | Mistral AI's 7B model | `ollama pull mistral` |
| gemma3 | Google's Gemma 7B model | `ollama pull gemma3` |
| phi4 | Microsoft's 7B model | `ollama pull phi4` |
| qwen2.5 | Qwen's 7B model | `ollama pull qwen2.5` |

For a complete list of available models, visit the [Ollama Library](https://ollama.com/library).

## Usage Examples

### Basic Chat

```python
import asyncio
from cursor_agent_tools import create_agent

async def main():
    # Create an Ollama agent
    agent = create_agent(model="ollama-llama3")
    
    # Chat with the agent
    response = await agent.chat("Write a Python function to calculate prime numbers")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### Tool Calling

```python
import asyncio
import os
from cursor_agent_tools import create_agent

async def main():
    # Create an Ollama agent
    agent = create_agent(model="ollama-llama3")
    
    # Register default tools
    agent.register_default_tools()
    
    # Create user context
    user_info = {
        "workspace_path": os.getcwd(),
        "os": os.name
    }
    
    # Use tool calling capabilities
    query = "Create a file called 'hello.py' that prints 'Hello, World!'"
    response = await agent.chat(query, user_info)
    
    # Display response
    if isinstance(response, dict):
        print(response["message"])
        if response.get("tool_calls"):
            print(f"\nTool calls: {len(response['tool_calls'])}")
            for i, tool in enumerate(response["tool_calls"], 1):
                print(f"Tool {i}: {tool['name']}")
    else:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### Image Queries (for models with vision capabilities)

```python
import asyncio
from cursor_agent_tools import create_agent

async def main():
    # Create an Ollama agent with a model that supports vision
    # For example, after running: ollama pull llava
    agent = create_agent(model="ollama-llava")
    
    # Query an image
    image_path = "path/to/your/image.jpg"
    response = await agent.query_image(
        image_paths=[image_path],
        query="What does this image show?"
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

## Performance Considerations

When using Ollama with the Cursor Agent, keep in mind:

1. **Hardware Requirements**: Performance depends on your hardware. Larger models require more RAM and a better GPU.
2. **Response Time**: Local models may be slower than cloud-based alternatives, especially on consumer hardware.
3. **Tool Calling Support**: Not all models support structured tool calling equally well. Models specifically trained for function calling will perform better.
4. **Vision Support**: Only specific models (like LLaVA) support image processing capabilities.

## Troubleshooting

### Common Issues

1. **Connection Errors**:
   - Ensure Ollama is running with `ollama serve`
   - Verify the correct host in configuration
   - Check firewall settings if using a remote Ollama server

2. **Model Not Found**:
   - Ensure you've pulled the model: `ollama list` to see available models
   - Pull missing models with `ollama pull MODEL_NAME`

3. **Memory Issues**:
   - If you encounter out-of-memory errors, try a smaller model
   - Close other applications to free up resources

### Logging

Enable verbose logging to debug Ollama integration issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Advanced Configuration

### Custom Model Parameters

You can pass additional parameters to Ollama models:

```python
agent = create_agent(
    model="ollama-llama3",
    extra_kwargs={
        "num_ctx": 4096,  # Context window size
        "num_gpu": 1      # Number of GPUs to use
    }
)
```

### Custom Tools

Registering custom tools works the same way as with cloud-based models:

```python
def my_custom_tool(param1, param2):
    # Tool implementation
    return {"output": f"Processed {param1} and {param2}"}

agent.register_tool(
    name="my_custom_tool",
    function=my_custom_tool,
    description="A custom tool that processes two parameters",
    parameters={
        "properties": {
            "param1": {"type": "string", "description": "First parameter"},
            "param2": {"type": "string", "description": "Second parameter"}
        },
        "required": ["param1", "param2"]
    }
)
``` 