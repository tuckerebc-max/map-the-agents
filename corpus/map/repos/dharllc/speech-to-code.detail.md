# dharllc/speech-to-code -- full detail

[Back to orientation](speech-to-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dharllc/speech-to-code/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/e79515a2712eb4a0.json](../../../wiki/dossiers/dharllc/speech-to-code/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/e79515a2712eb4a0.json)

## specifications (1 claim(s))

- [observation/documented] Speech-to-Code is a web application that uses LLMs to convert spoken language into executable code, letting developers express ideas verbally and get functional code. -- evidence: [README.md#L3-L3](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L3-L3) (`clm_8b80dbff67625ef20d9d5f1d3704621617b0b027716c3ddb5eb1fe68fe78e364`)

## components (2 claim(s))

- [observation/documented] The project structure includes a backend (main.py, llm_interaction.py, model_config.py, system_prompts.json, context_maps, utils) and a frontend with components, services, and config directories, plus a logs/chat_sessions directory. -- evidence: [README.md#L151-L170](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L151-L170) (`clm_47d3ed3cd63c58204181cf4d11fabb4fc93f1f9d652075aec6d364dbaa691244`)
- [observation/documented] A git utility module /backend/utils/git_operations.py provides get_git_info(repo_path), running git rev-parse commands with a 5-second timeout and returning branch, commit_hash, and error fields; the checklist marks it created. -- evidence: [git-branch-implementation-checklist.md#L6-L18](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-implementation-checklist.md#L6-L18), [git-branch-display-implementation-plan.md#L43-L50](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L43-L50), [git-branch-display-implementation-plan.md#L66-L76](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L66-L76), [git-branch-display-implementation-plan.md#L33-L41](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L33-L41), [git-branch-display-implementation-plan.md#L55-L62](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L55-L62) (`clm_a7ea26407b3a277f6f6dac37c6b53ba34812d167a8288425a04edd41b152ee72`)

## design-choices (1 claim(s))

- [observation/documented] The git feature's security design calls for validating repository names against path traversal, read-only git commands only, a 5-second subprocess timeout, and no user input passed directly to git commands. -- evidence: [git-branch-display-implementation-plan.md#L203-L206](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L203-L206), [git-branch-display-implementation-plan.md#L199-L200](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L199-L200) (`clm_59243b31246af23729037ed7284a7ef67e14fb15a0c4b49ac6b7fd2ad27f7a4f`)

## workflows (2 claim(s))

- [observation/documented] Setup involves cloning the repo, making build.sh executable, and running it to install dependencies, create a Python virtual environment, generate .env placeholder files, and create log/chat-session directories; the frontend starts with npm start and the backend with uvicorn main:app. -- evidence: [README.md#L140-L145](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L140-L145), [README.md#L96-L99](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L96-L99), [README.md#L90-L94](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L90-L94), [README.md#L134-L138](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L134-L138), [README.md#L101-L110](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L101-L110) (`clm_35fb5586ddefbb4b236be76f64453144509f6a85585853c0da4d5dce272f0bbf`)
- [observation/documented] Troubleshooting guidance covers macOS build failures for grpcio/tiktoken/tokenizers (upgrade pip and build tools, or install precompiled wheels), missing uvicorn, and setting REPO_PATH in backend/.env. -- evidence: [README.md#L200-L203](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L200-L203), [README.md#L179-L184](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L179-L184), [README.md#L196-L198](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L196-L198), [README.md#L186-L189](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L186-L189), [README.md#L176-L177](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L176-L177) (`clm_3dcb709ed199436d512bcc16fcbf274857e0af3f645f283a436e1d45f47c4b8e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The backend is a FastAPI server exposing endpoints such as /directories, /tree, and /file_content, with the repository root configured via the REPO_PATH environment variable. -- evidence: [git-branch-display-implementation-plan.md#L16-L19](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L16-L19) (`clm_86abb0cee1c0bc2ee8d0144c8f68d41248aa84efaf55f30cdafb5e46e77f6134`)
- [observation/documented] A GET /git-info/{repository} endpoint returns git branch and short commit hash for a repository, with 404 for missing repositories and 500 on failure; the checklist marks it implemented. -- evidence: [git-branch-display-implementation-plan.md#L103-L104](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L103-L104), [git-branch-implementation-checklist.md#L21-L29](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-implementation-checklist.md#L21-L29), [git-branch-display-implementation-plan.md#L92-L98](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L92-L98), [git-branch-display-implementation-plan.md#L106-L108](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L106-L108), [git-branch-display-implementation-plan.md#L100-L101](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L100-L101) (`clm_d683b121f2f8d511491627e5047f2e4bcdbf7ded920164d222e02e7068f23bde`)

## memory-state (1 claim(s))

- [observation/documented] The app offers persistent chat history with automatic saving, session organization, soft delete of chat sessions, automatic chat naming, and session logs stored under a logs directory. -- evidence: [README.md#L151-L170](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L151-L170), [README.md#L74-L77](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L74-L77), [README.md#L44-L48](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L44-L48) (`clm_9b6a72385d861ab0495bfe8797415ccbbbc1adc2f004d0b9108ba1a5c2e315d9`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Backend dependencies include uvicorn, fastapi, python-dotenv, openai, anthropic, and google-generativeai; the app integrates multiple LLM providers including OpenAI and Anthropic. -- evidence: [README.md#L191-L194](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L191-L194), [README.md#L32-L35](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L32-L35) (`clm_aa5986dff1328f15da2ee44c6c8ce3005e74cc5c895bb0f9dc9b6283963d7b4c`)
- [observation/documented] Prerequisites are Node.js with npm (latest version) and Python 3.7 or later on a Windows/Linux/Mac machine with command line access. -- evidence: [README.md#L83-L86](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L83-L86) (`clm_7adc3d98ad6f69c336a727f0a924c7b5525ea684b3ef818bf163c3515bebecdf`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

