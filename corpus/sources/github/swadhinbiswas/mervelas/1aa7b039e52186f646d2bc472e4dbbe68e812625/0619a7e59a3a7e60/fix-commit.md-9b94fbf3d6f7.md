Fixed the OpenAI compatible tools format to send `function` nested object in the tools array instead of putting function properties at the top-level. 
This resolves the 400 Bad Request `Field required` validation error for models connecting via OpenRouter/OpenAI API like `qwen/qwen3.5-122b-a10b`.

Also removed `strict: false` parameter to maximize compatibility with third-party models since many models strictly validate the JSON schema but don't recognize the `strict` field itself.
