# dharllc/speech-to-code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c2756161e3ce @ e79515a2712eb4a0

## Summary (orientation draft, not independently verified)

Selected evidence records: Speech-to-Code is a web application that uses LLMs to convert spoken language into executable code, letting developers express ideas verbally and get functional code. The project structure includes a backend (main.py, llm_interaction.py, model_config.py, system_prompts.json, context_maps, utils) and a frontend with components, services, and config directories, plus a logs/chat_sessions directory.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Speech-to-Code is a web application that uses LLMs to convert spoken language into executable code, letting developers express ideas verbally and get functional code. -- evidence: [README.md#L3-L3](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] The project structure includes a backend (main.py, llm_interaction.py, model_config.py, system_prompts.json, context_maps, utils) and a frontend with components, services, and config directories, plus a logs/chat_sessions directory. -- evidence: [README.md#L151-L170](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L151-L170)
  - [observation/documented] A git utility module /backend/utils/git_operations.py provides get_git_info(repo_path), running git rev-parse commands with a 5-second timeout and returning branch, commit_hash, and error fields; the checklist marks it created. -- evidence: [git-branch-implementation-checklist.md#L6-L18](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-implementation-checklist.md#L6-L18), [git-branch-display-implementation-plan.md#L43-L50](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L43-L50), [git-branch-display-implementation-plan.md#L66-L76](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L66-L76), [git-branch-display-implementation-plan.md#L33-L41](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L33-L41), [git-branch-display-implementation-plan.md#L55-L62](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L55-L62)
- design-choices (1 claim(s)):
  - [observation/documented] The git feature's security design calls for validating repository names against path traversal, read-only git commands only, a 5-second subprocess timeout, and no user input passed directly to git commands. -- evidence: [git-branch-display-implementation-plan.md#L203-L206](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L203-L206), [git-branch-display-implementation-plan.md#L199-L200](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L199-L200)
- workflows (2 claim(s)):
  - [observation/documented] Setup involves cloning the repo, making build.sh executable, and running it to install dependencies, create a Python virtual environment, generate .env placeholder files, and create log/chat-session directories; the frontend starts with npm start and the backend with uvicorn main:app. -- evidence: [README.md#L140-L145](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L140-L145), [README.md#L96-L99](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L96-L99), [README.md#L90-L94](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L90-L94), [README.md#L134-L138](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L134-L138), [README.md#L101-L110](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L101-L110)
  - [observation/documented] Troubleshooting guidance covers macOS build failures for grpcio/tiktoken/tokenizers (upgrade pip and build tools, or install precompiled wheels), missing uvicorn, and setting REPO_PATH in backend/.env. -- evidence: [README.md#L200-L203](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L200-L203), [README.md#L179-L184](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L179-L184), [README.md#L196-L198](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L196-L198), [README.md#L186-L189](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L186-L189), [README.md#L176-L177](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L176-L177)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The backend is a FastAPI server exposing endpoints such as /directories, /tree, and /file_content, with the repository root configured via the REPO_PATH environment variable. -- evidence: [git-branch-display-implementation-plan.md#L16-L19](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L16-L19)
  - [observation/documented] A GET /git-info/{repository} endpoint returns git branch and short commit hash for a repository, with 404 for missing repositories and 500 on failure; the checklist marks it implemented. -- evidence: [git-branch-display-implementation-plan.md#L103-L104](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L103-L104), [git-branch-implementation-checklist.md#L21-L29](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-implementation-checklist.md#L21-L29), [git-branch-display-implementation-plan.md#L92-L98](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L92-L98), [git-branch-display-implementation-plan.md#L106-L108](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L106-L108), [git-branch-display-implementation-plan.md#L100-L101](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/git-branch-display-implementation-plan.md#L100-L101)
- memory-state (1 claim(s)):
  - [observation/documented] The app offers persistent chat history with automatic saving, session organization, soft delete of chat sessions, automatic chat naming, and session logs stored under a logs directory. -- evidence: [README.md#L151-L170](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L151-L170), [README.md#L74-L77](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L74-L77), [README.md#L44-L48](https://github.com/dharllc/speech-to-code/blob/c2756161e3cef9379bd16d9d1f57a78b3bd08b5f/README.md#L44-L48)
More evidence: [full detail](speech-to-code.detail.md)

Metadata and full claim list: [full detail](speech-to-code.detail.md)
Human notes ([notes](speech-to-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
