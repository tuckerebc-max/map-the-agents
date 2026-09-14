# aestheticsuraj234/vibecode-playground -- full detail

[Back to orientation](vibecode-playground.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aestheticsuraj234/vibecode-playground/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/a66a8b982bd24efe.json](../../../wiki/dossiers/aestheticsuraj234/vibecode-playground/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/a66a8b982bd24efe.json)

## specifications (1 claim(s))

- [observation/documented] Vibecode Editor is described as an AI-integrated web IDE running entirely in the browser, built with Next.js App Router, WebContainers, Monaco Editor, and local LLMs via Ollama. -- evidence: [README.md#L5-L5](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L5-L5) (`clm_3360de7cd3a1079dcb0c21799b2052c3c21275219b783bc992068a5fbfdb4796`)

## components (3 claim(s))

- [observation/documented] The README lists a tech stack of Next.js 15 (App Router), TailwindCSS/ShadCN UI, TypeScript, NextAuth, Monaco Editor, Ollama, WebContainers, xterm.js, and MongoDB. -- evidence: [README.md#L26-L36](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L26-L36) (`clm_0565831e3bfdbc200761156feec912e3fc6aff2e39dbfe13fa61f1bd48bfc2b3`)
- [observation/documented] WebContainers integration lets frontend and backend apps run directly in the browser, with an interactive terminal powered by xterm.js. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20) (`clm_06f298714c0f0bba7b9c6d14e9d07d41fe68940be006999ecb3cbb209eea1d88`)
- [observation/documented] An AI chat assistant lets users share files with the AI to get help, refactors, or explanations. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20) (`clm_f0b0b7844d771f7cd79e3292cfaff2857569b8b5c7b4d6fbca8876abeb884f7d`)

## design-choices (1 claim(s))

- [observation/documented] The project is licensed under the MIT License. -- evidence: [README.md#L136-L136](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L136-L136) (`clm_9de13ec3ce8a15329957b898d6484db462fd5e5f62dfb2527ea8f201afe9f34c`)

## workflows (3 claim(s))

- [observation/documented] Setup involves cloning the repo, running npm install, copying .env.example to .env.local, and filling in auth, GitHub/Google OAuth, and MongoDB credentials. -- evidence: [README.md#L51-L53](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L51-L53), [README.md#L44-L47](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L44-L47), [README.md#L65-L73](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L65-L73), [README.md#L59-L61](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L59-L61), [README.md#L57-L57](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L57-L57) (`clm_74ccd97f24d993ba307b954cc6754ea451a7e7182768a87a0437ca8926c51018`)
- [observation/documented] To enable AI features, the README instructs installing Ollama and Docker and running a local model such as 'ollama run codellama' or any preferred code-generation model. -- evidence: [README.md#L83-L83](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L83-L83), [README.md#L77-L77](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L77-L77), [README.md#L79-L81](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L79-L81) (`clm_ec2d41b4ab23d5def6480b30facf89fdf40751c51d413ee2c698d7ca3f1af738`)
- [observation/documented] The development server is started with npm run dev and accessed at http://localhost:3000. -- evidence: [README.md#L91-L91](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L91-L91), [README.md#L87-L89](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L87-L89) (`clm_e5376353305534324f87fea4303d22650e7c65b54f0a7628cb2e07d7749cb358`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The editor supports OAuth login via NextAuth with Google and GitHub providers. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20), [README.md#L26-L36](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L26-L36) (`clm_c721e731963407f914481aedead2b9308bf446478aea6e7fce3440205a8cb18e`)
- [observation/documented] Users can pick project templates for React, Next.js, Express, Hono, Vue, or Angular, and manage files and folders through a custom file explorer. -- evidence: [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20) (`clm_d489f9df4e3068b84824e744ece727332e7a426c67a8e9a66fd56310df2eee4f`)
- [observation/documented] AI suggestions from local Ollama models are triggered with Ctrl+Space or double Enter and accepted with Tab; a slash key opens a command palette if implemented. -- evidence: [README.md#L113-L115](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L113-L115), [README.md#L11-L20](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L11-L20) (`clm_6c649cef6b2c8329fd3ff2a3921abbe912abaa512ce5f30175e8fb19c6c5040b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Environment variables required include AUTH_SECRET, Google and GitHub OAuth credentials, DATABASE_URL for MongoDB, and NEXTAUTH_URL. -- evidence: [README.md#L65-L73](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L65-L73) (`clm_b61f7d9204af24221a5e458d7fd3fc60de488047ddc55e509d77108c8ed75486`)

## limitations (1 claim(s))

- [observation/documented] The roadmap marks GitHub repo import/export, DB-backed save/load, real-time collaboration, a plugin system, and one-click deploy as not yet completed. -- evidence: [README.md#L121-L130](https://github.com/Aestheticsuraj234/vibecode-playground/blob/035a02f5855a10f28e4a6d73897ad11e3b9a1ba5/README.md#L121-L130) (`clm_0b616b2848b77334a27c13963e6c4dd295ea8e07af308255ab5a51baf68dee1d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

