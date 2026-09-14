# aestheticsuraj234/vibecode-playground

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 035a02f5855a @ a66a8b982bd24efe

## Summary (orientation draft, not independently verified)

The evidence is a README describing Vibecode Editor, a browser-based AI-integrated web IDE built with Next.js, WebContainers, Monaco Editor, and local Ollama LLMs. Claims below rest on documentation only; no code was inspected.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vibecode Editor is described as an AI-integrated web IDE running entirely in the browser, built with Next.js App Router, WebContainers, Monaco Editor, and local LLMs via Ollama. -- evidence: [README.md#L5-L5](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L5-L5)
- components (3 claim(s)):
  - [observation/documented] The README lists a tech stack of Next.js 15 (App Router), TailwindCSS/ShadCN UI, TypeScript, NextAuth, Monaco Editor, Ollama, WebContainers, xterm.js, and MongoDB. -- evidence: [README.md#L26-L36](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L26-L36)
  - [observation/documented] WebContainers integration lets frontend and backend apps run directly in the browser, with an interactive terminal powered by xterm.js. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20)
- design-choices (1 claim(s)):
  - [observation/documented] The project is licensed under the MIT License. -- evidence: [README.md#L136-L136](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L136-L136)
- workflows (3 claim(s)):
  - [observation/documented] Setup involves cloning the repo, running npm install, copying .env.example to .env.local, and filling in auth, GitHub/Google OAuth, and MongoDB credentials. -- evidence: [README.md#L51-L53](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L51-L53), [README.md#L44-L47](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L44-L47), [README.md#L65-L73](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L65-L73), [README.md#L59-L61](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L59-L61), [README.md#L57-L57](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L57-L57)
  - [observation/documented] To enable AI features, the README instructs installing Ollama and Docker and running a local model such as 'ollama run codellama' or any preferred code-generation model. -- evidence: [README.md#L83-L83](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L83-L83), [README.md#L77-L77](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L77-L77), [README.md#L79-L81](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L79-L81)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The editor supports OAuth login via NextAuth with Google and GitHub providers. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20), [README.md#L26-L36](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L26-L36)
  - [observation/documented] Users can pick project templates for React, Next.js, Express, Hono, Vue, or Angular, and manage files and folders through a custom file explorer. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Environment variables required include AUTH_SECRET, Google and GitHub OAuth credentials, DATABASE_URL for MongoDB, and NEXTAUTH_URL. -- evidence: [README.md#L65-L73](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L65-L73)
- limitations (1 claim(s)):
  - [observation/documented] The roadmap marks GitHub repo import/export, DB-backed save/load, real-time collaboration, a plugin system, and one-click deploy as not yet completed. -- evidence: [README.md#L121-L130](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L121-L130)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](vibecode-playground.detail.md) for every claim.)

Metadata and full claim list: [full detail](vibecode-playground.detail.md)
Human notes ([notes](vibecode-playground.notes.md), never overwritten by build)

[Back to map index](../../index.md)
