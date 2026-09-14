---
access: public
aliases: []
claim_ids:
- clm_35fb5586ddefbb4b236be76f64453144509f6a85585853c0da4d5dce272f0bbf
- clm_3dcb709ed199436d512bcc16fcbf274857e0af3f645f283a436e1d45f47c4b8e
- clm_47d3ed3cd63c58204181cf4d11fabb4fc93f1f9d652075aec6d364dbaa691244
- clm_7adc3d98ad6f69c336a727f0a924c7b5525ea684b3ef818bf163c3515bebecdf
- clm_8b80dbff67625ef20d9d5f1d3704621617b0b027716c3ddb5eb1fe68fe78e364
- clm_9b6a72385d861ab0495bfe8797415ccbbbc1adc2f004d0b9108ba1a5c2e315d9
- clm_aa5986dff1328f15da2ee44c6c8ce3005e74cc5c895bb0f9dc9b6283963d7b4c
maturity: draft
page_id: pg_83f8ca47ae01587fac9ec742b5c4a066
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d9cabfc21fe25342a7777a716d1277b5
title: dharllc/speech-to-code/README.md @ c2756161e3ce
updated_at: '2026-09-14T03:47:02Z'
---

# dharllc/speech-to-code/README.md @ c2756161e3ce

<!-- rcw:begin owner=source:src_d9cabfc21fe25342a7777a716d1277b5 block=evidence -->
- Setup involves cloning the repo, making build.sh executable, and running it to install dependencies, create a Python virtual environment, generate .env placeholder files, and create log/chat-session directories; the frontend starts with npm start and the backend with uvicorn main:app. [@claim:clm_35fb5586ddefbb4b236be76f64453144509f6a85585853c0da4d5dce272f0bbf]
- Troubleshooting guidance covers macOS build failures for grpcio/tiktoken/tokenizers (upgrade pip and build tools, or install precompiled wheels), missing uvicorn, and setting REPO_PATH in backend/.env. [@claim:clm_3dcb709ed199436d512bcc16fcbf274857e0af3f645f283a436e1d45f47c4b8e]
- The project structure includes a backend (main.py, llm_interaction.py, model_config.py, system_prompts.json, context_maps, utils) and a frontend with components, services, and config directories, plus a logs/chat_sessions directory. [@claim:clm_47d3ed3cd63c58204181cf4d11fabb4fc93f1f9d652075aec6d364dbaa691244]
- Prerequisites are Node.js with npm (latest version) and Python 3.7 or later on a Windows/Linux/Mac machine with command line access. [@claim:clm_7adc3d98ad6f69c336a727f0a924c7b5525ea684b3ef818bf163c3515bebecdf]
- Speech-to-Code is a web application that uses LLMs to convert spoken language into executable code, letting developers express ideas verbally and get functional code. [@claim:clm_8b80dbff67625ef20d9d5f1d3704621617b0b027716c3ddb5eb1fe68fe78e364]
- The app offers persistent chat history with automatic saving, session organization, soft delete of chat sessions, automatic chat naming, and session logs stored under a logs directory. [@claim:clm_9b6a72385d861ab0495bfe8797415ccbbbc1adc2f004d0b9108ba1a5c2e315d9]
- Backend dependencies include uvicorn, fastapi, python-dotenv, openai, anthropic, and google-generativeai; the app integrates multiple LLM providers including OpenAI and Anthropic. [@claim:clm_aa5986dff1328f15da2ee44c6c8ce3005e74cc5c895bb0f9dc9b6283963d7b4c]
<!-- rcw:end owner=source:src_d9cabfc21fe25342a7777a716d1277b5 block=evidence -->

## Researcher notes

