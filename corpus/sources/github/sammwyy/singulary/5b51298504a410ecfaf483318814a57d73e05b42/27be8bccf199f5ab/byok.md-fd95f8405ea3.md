# Bring Your Own Keys (BYOK)

Singulary does not force a specific AI provider on you. You can connect and use your own API keys. 

## Supported Providers
You can connect keys from:
- OpenAI
- Anthropic
- OpenRouter
- Google Gemini
- Mistral
- Groq
- xAI
- DeepSeek
- Ollama / LM Studio (or any custom OpenAI-compatible endpoints)

## How It Works
Keys can be configured at multiple levels:
- **Personal user keys** (your own BYOK)
- **Workspace keys**
- **Organization keys**
- **Global admin-managed keys**

All keys (provider keys, service credentials, etc.) are AES-GCM encrypted at rest to ensure security.
