# Web Search Documentation

The web search feature allows you to search the internet for up-to-date information using Google's Custom Search API.

## Prerequisites

You need to set up Google API credentials:

1. Create a Google Cloud project and enable Custom Search API
2. Create API key: https://console.cloud.google.com/apis/credentials
3. Create a Custom Search Engine: https://programmablesearchengine.google.com/
4. Add these to your `.env` file:
   ```ini
   GOOGLE_API_KEY=your_api_key
   GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
   ```

## Usage

There are two ways to use the web search feature:

### 1. Through the Agent Chat Interface (Recommended)

```python
import asyncio
from cursor_agent_tools import create_agent

async def main():
    # Create an agent instance
    agent = create_agent(model='claude-3-5-sonnet-latest')
    
    # Ask your question through chat
    response = await agent.chat(
        "What are the latest developments in quantum computing?"
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Direct Tool Usage

```python
from cursor_agent_tools.tools.search_tools import web_search

# Perform a web search
results = web_search(
    search_term="latest developments in quantum computing",
    force=True,  # Force web search even if not required
    max_results=5  # Number of results to return
)
```

## Parameters

The web search tool accepts the following parameters:

- `search_term` (str, required): The search term to look up on the web
- `explanation` (str, optional): One sentence explanation of why this search is being performed
- `force` (bool, optional): Force internet access even if not required
- `objective` (str, optional): User objective to determine if up-to-date data is needed
- `max_results` (int, optional): Maximum number of results to return (default: 3)

## Response Format

The web search returns a dictionary with the following structure:

```python
{
    "query": "your search term",
    "results": [
        {
            "title": "Article Title",
            "url": "https://example.com/article",
            "content": "Article content snippet..."
        },
        # More results...
    ],
    "total_results": 5
}
```

## Example with Full Error Handling

```python
import asyncio
from cursor_agent_tools import create_agent
from typing import Dict, Any

async def run_web_search() -> Dict[str, Any]:
    try:
        # Initialize agent
        agent = create_agent(model='claude-3-5-sonnet-latest')
        
        # Create user context
        user_info = {
            "os": "darwin",
            "workspace_path": "/path/to/workspace"
        }
        
        # Perform search
        response = await agent.chat(
            "What are the latest developments in quantum computing?",
            user_info=user_info
        )
        
        # Process response
        if isinstance(response, dict):
            if "error" in response:
                print(f"Error: {response['error']}")
                return response
                
            if response.get("tool_calls"):
                for call in response["tool_calls"]:
                    if call["name"] == "web_search":
                        print(f"Search term: {call['parameters'].get('search_term')}")
                        if call.get('result', {}).get('results'):
                            print(f"Found {len(call['result']['results'])} results")
                            
        return response
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    asyncio.run(run_web_search())
```

## Best Practices

1. **API Key Security**
   - Never commit API keys to version control
   - Use environment variables or secure key management
   - Rotate keys periodically

2. **Error Handling**
   - Always check for API errors in responses
   - Handle rate limiting gracefully
   - Provide meaningful error messages

3. **Performance**
   - Cache results when appropriate
   - Limit max_results to reduce API costs
   - Use force=True only when necessary

4. **Content Processing**
   - Validate and sanitize search terms
   - Handle HTML content appropriately
   - Consider implementing retry logic

## Common Issues

1. **Missing API Keys**
   ```
   Error: Google API keys are required. Please set GOOGLE_API_KEY and GOOGLE_SEARCH_ENGINE_ID environment variables.
   ```
   Solution: Set up Google API credentials as described in Prerequisites.

2. **Rate Limiting**
   ```
   Error: Quota exceeded for quota metric 'Queries' and limit 'Queries per day'
   ```
   Solution: Check your Google Cloud Console quotas and billing status.

3. **Invalid Search Engine ID**
   ```
   Error: Invalid Value: The custom search engine ID is invalid
   ```
   Solution: Verify your Search Engine ID in the Programmable Search Engine dashboard.

## See Also

- [Google Custom Search API Documentation](https://developers.google.com/custom-search/v1/overview)
- [Cursor Agent Tools Documentation](../README.md)
- [Trend Search Documentation](./trend_search.md) 