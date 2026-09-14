# ivy-interactive/ivy-tendril -- full detail

[Back to orientation](ivy-tendril.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ivy-interactive/ivy-tendril/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/59bc3ebe842b1475.json](../../../wiki/dossiers/ivy-interactive/ivy-tendril/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/59bc3ebe842b1475.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (6 claim(s))

- [observation/documented] The product runs agents in isolated git worktrees so the main branch stays clean until changes are reviewed, approved, and merged. -- evidence: [README.md#L35-L35](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L35-L35) (`clm_0bb494bd6a68b6f8ca0813be09b8f9ee5a3383f5299678fa2a38a30f9f55ad75`)
- [observation/documented] Tendril can expose its server via Cloudflare Quick Tunnels so agent runs can be monitored and steered remotely. -- evidence: [README.md#L49-L49](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L49-L49) (`clm_7b619f7c29fae38bfaedd91ded997b1072895de7b01625647669ef8917e59655`)
- [observation/documented] The app includes built-in Whisper voice dictation for prompts and drag-and-drop attachment of text files, logs, or documents. -- evidence: [README.md#L63-L63](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L63-L63) (`clm_370b8a129d9eadc207a787e6be9d0c4e73e412120a6d3a1024bac35b08b35936`)
- [observation/documented] Users can annotate plan drafts inline to automatically update plans with revised agent goals. -- evidence: [README.md#L77-L77](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L77-L77) (`clm_648ac6698be2ac3e9e1657a24713f2851a92cb3050b02dd5bd78b042ef9ae5d6`)
- [observation/documented] The review feature lets users inspect diffs and approve agent changes with automated verification gates. -- evidence: [README.md#L91-L91](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L91-L91) (`clm_1eab3878d743e942695d9b8fb1ceac1e88844a72afebb582c02d1cd9ab0cb512`)
- [observation/documented] GitHub Issues or jam.dev bug reports can be ingested via webhooks, converting markdown plans into active jobs automatically. -- evidence: [README.md#L105-L105](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L105-L105) (`clm_55ab9ae2bb32dd957c5347aa88b26834fa28d9c0ef8bb7cb35aa7f729c18bc79`)

## design-choices (1 claim(s))

- [observation/documented] Tendril positions itself as a developer tool for the agentic era, described as replacing the IDE when AI agents write most of the code. -- evidence: [README.md#L13-L13](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L13-L13), [README.md#L15-L17](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L15-L17) (`clm_741863640740d061443bddee8d5b1062717bbb90059bf5d0ce484acfbab0ade3`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: all development work must target the 'development' branch as the PR base, with 'main' updated only by merging development for releases. -- evidence: [AGENTS.md#L5-L5](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/AGENTS.md#L5-L5) (`clm_1ca5741422a9c1f936c97c7b3e088e66872d4c3cd2f40c66124dbec5a9fa9d74`)
- [observation/documented] Repository development practice: merge conflicts must be resolved file-by-file without blanket 'ours/theirs' strategies or deleting untouched development files, then verified with 'dotnet build src/Ivy.Tendril/Ivy.Tendril.slnx'. -- evidence: [AGENTS.md#L11-L13](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/AGENTS.md#L11-L13) (`clm_b8ba4d054c7a780d4da3229d783cde6335d46d21647d85b25782b7e266f13525`)
- [observation/documented] Repository development practice: contributors must never use the em dash character (U+2014) in output, comments, commit messages, or documentation. -- evidence: [AGENTS.md#L17-L17](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/AGENTS.md#L17-L17) (`clm_5653095da1cd3c97d1873114bcc1cbf651a3d199ec00d8f30b0d0902097bc1a8`)

## skills-patterns (2 claim(s))

- [observation/documented] Official Tendril engineering and debugging skills can be installed with 'npx skills add ivy-interactive/ivy-tendril', optionally targeting a specific skill or agent such as github-copilot or cursor. -- evidence: [README.md#L138-L140](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L138-L140), [README.md#L155-L157](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L155-L157), [README.md#L132-L132](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L132-L132), [README.md#L221-L223](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L221-L223), [README.md#L144-L146](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L144-L146), [README.md#L136-L136](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L136-L136) (`clm_09c5c2f8bdb4a80d3e9f42572920679f4dda52e0bfd6e9a80d1395ef1e8775d1`)
- [observation/documented] Skills can also be installed as plugins for Claude Code, Codex, Gemini CLI, and Antigravity CLI, or copied into tool-specific skills directories. -- evidence: [README.md#L235-L239](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L235-L239), [README.md#L246-L249](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L246-L249), [README.md#L165-L165](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L165-L165), [README.md#L203-L205](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L203-L205), [README.md#L184-L187](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L184-L187), [README.md#L225-L225](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L225-L225) (`clm_a9f67df364557528557b570a1404f489f46f5424b8edbe0a840f577236587bda`)

## interfaces (3 claim(s))

- [observation/documented] Tendril works with any CLI agent that runs in a terminal, naming Claude Code, Codex, GitHub Copilot, Gemini, and OpenCode as examples. -- evidence: [README.md#L120-L120](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L120-L120), [README.md#L122-L129](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L122-L129) (`clm_3b6bb1e1b0ae88b5d7f36e43217cb0bad2646eee6b6662658bc9a5cbd7995a81`)
- [observation/documented] The CLI offers a desktop launch via 'tendril' and a headless web-server mode via 'tendril --web'. -- evidence: [README.md#L276-L279](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L276-L279), [README.md#L271-L274](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L271-L274), [README.md#L269-L269](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L269-L269) (`clm_c6b16b8b214a3fc22af021c847d8c935314b7c52c4d8ea37e08eb7398ad30114`)
- [observation/documented] Standalone desktop installers (.pkg, .AppImage, .exe) are published on GitHub Releases, with curl/powershell install scripts for macOS/Linux and Windows. -- evidence: [README.md#L262-L265](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L262-L265), [README.md#L255-L255](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L255-L255), [README.md#L257-L260](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L257-L260) (`clm_da4619d7627010f6c9c378317bbfc28d7a5bedd171d51aa0438c5865466e9dfa`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The installer bundles unmodified third-party runtimes including PowerShell Core, the .NET SDK, and OpenCode CLI, all MIT-licensed. -- evidence: [THIRD_PARTY_NOTICES.md#L15-L17](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L15-L17), [THIRD_PARTY_NOTICES.md#L9-L11](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L9-L11), [THIRD_PARTY_NOTICES.md#L21-L23](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L21-L23), [THIRD_PARTY_NOTICES.md#L3-L3](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L3-L3) (`clm_4e537199f4b768a33fd922b7749d97cf32fc30094c3237572df019bf21419bce`)
- [observation/documented] Tendril is source-available under the Functional Source License (FSL-1.1-ALv2). -- evidence: [README.md#L293-L293](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L293-L293) (`clm_f4b3f64dc4b0f2992d1bcd5d91eb9cfe6b0d1e09258dbeb06f7f06c90c440189`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

