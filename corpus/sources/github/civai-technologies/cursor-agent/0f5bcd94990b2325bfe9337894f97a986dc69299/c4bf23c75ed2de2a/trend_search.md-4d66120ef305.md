# Trend Search Documentation

The trend search feature allows you to discover and analyze trending topics across different categories and countries using Google Trends data.

## Prerequisites

You need Google API credentials for the underlying web search functionality:

1. Create a Google Cloud project and enable Custom Search API
2. Create API key: https://console.cloud.google.com/apis/credentials
3. Create a Custom Search Engine: https://programmablesearchengine.google.com/
4. Add these to your `.env` file:
   ```ini
   GOOGLE_API_KEY=your_api_key
   GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
   ```

## Usage

There are two ways to use the trend search feature:

### 1. Through the Agent Chat Interface (Recommended)

```python
import asyncio
from cursor_agent_tools import create_agent

async def main():
    # Create an agent instance
    agent = create_agent(model='claude-3-5-sonnet-latest')
    
    # Ask about trends through chat
    response = await agent.chat(
        "What are the current trending topics in AI technology? "
        "Please focus on the last 7 days and show me the top 3 trends."
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Direct Tool Usage

```python
from cursor_agent_tools.tools.search_tools import trend_search

# Search for trends
trends = await trend_search(
    query="What's trending in technology?",
    country_code="GB",  # United Kingdom
    max_results=3,
    days=7
)
```

## Parameters

The trend search tool accepts the following parameters:

- `query` (str, required): The user's query about trends
- `explanation` (str, optional): One sentence explanation of why this search is being performed
- `country_code` (str, optional): Country code for trends (default: "US")
- `days` (int, optional): Number of days to look back for trends (default: 7)
- `max_results` (int, optional): Maximum number of trends to return (default: 3)
- `lookback_hours` (int, optional): Number of hours to look back for Google Trends data (default: 48)
- `agent` (Optional[Any], optional): Reference to the agent instance for categorizing the query

## Available Categories

The trend search can find trends in these categories:

- All Categories
- Science
- Technology
- Jobs & Education
- Entertainment
- Food & Drink
- Business & Finance
- Beauty & Fashion
- Sports
- Autos & Vehicles
- Climate
- Games
- Health
- Hobbies & Leisure
- Law & Government
- Politics
- Shopping
- Travel & Transportation

## Response Format

The trend search returns a dictionary with the following structure:

```python
{
    "query": "your search query",
    "category": "Technology",  # Determined category
    "category_id": 18,        # Internal category ID
    "country_code": "US",
    "days": 7,
    "trends": [
        {
            "name": "Trending Topic Name",
            "snippet": "Brief description of the trend...",
            "sources": ["https://example.com/article1", "https://example.com/article2"],
            "content": {
                "https://example.com/article1": "Full article content...",
                "https://example.com/article2": "Full article content..."
            }
        },
        # More trends...
    ],
    "total_trends": 3
}
```

## Example with Full Error Handling

```python
import asyncio
from cursor_agent_tools.tools.search_tools import trend_search
from typing import Dict, Any

async def get_tech_trends() -> Dict[str, Any]:
    try:
        # Search for technology trends
        trends = await trend_search(
            query="What's trending in AI and machine learning?",
            country_code="US",
            max_results=3,
            days=7
        )
        
        # Check for errors
        if "error" in trends:
            print(f"Error: {trends['error']}")
            return trends
            
        # Process results
        if trends.get("trends"):
            print(f"\nFound {len(trends['trends'])} trends in {trends['category']}:")
            for i, trend in enumerate(trends['trends'], 1):
                print(f"\n{i}. {trend['name']}")
                print(f"   Summary: {trend['snippet'][:200]}...")
                print(f"   Sources: {len(trend['sources'])} articles")
                
        return trends
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    asyncio.run(get_tech_trends())
```

## Best Practices

1. **Category Selection**
   - Let the agent determine the appropriate category
   - Use specific queries for better category matching
   - Consider the context of your search

2. **Result Processing**
   - Always check for errors in the response
   - Handle missing or incomplete data gracefully
   - Process trend snippets appropriately

3. **Performance**
   - Use appropriate lookback periods
   - Limit max_results to necessary amount
   - Consider caching results for repeated queries

4. **Content Analysis**
   - Verify trend relevance to query
   - Cross-reference multiple sources
   - Consider trend volume and recency

## Common Issues

1. **No Trends Found**
   ```
   Warning: No trends found in category Technology
   ```
   Solution: Try broadening your search or using a different category.

2. **API Key Errors**
   ```
   Error: Google API keys are required for trend search
   ```
   Solution: Set up Google API credentials as described in Prerequisites.

3. **Invalid Country Code**
   ```
   Error: Invalid country code specified
   ```
   Solution: Use valid ISO 3166-1 alpha-2 country codes (e.g., "US", "GB", "DE").

## See Also

- [Google Trends API Documentation](https://trends.google.com/trends/explore)
- [Cursor Agent Tools Documentation](../README.md)
- [Web Search Documentation](./web_search.md) 