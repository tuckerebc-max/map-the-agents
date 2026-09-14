# ivy-interactive/ivy-tendril

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3c17eb4573b3 @ 59bc3ebe842b1475

## Summary (orientation draft, not independently verified)

Evidence from README.md, AGENTS.md, and THIRD_PARTY_NOTICES.md documents Ivy Tendril as a desktop/CLI tool for running AI coding agents, with worktree isolation, tunneling, voice input, plan annotation, review gates, webhook ingestion, installable skills, and an FSL-1.1-ALv2 license; AGENTS.md supplies contributor workflow rules.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (6 claim(s)):
  - [observation/documented] The product runs agents in isolated git worktrees so the main branch stays clean until changes are reviewed, approved, and merged. -- evidence: [README.md#L35-L35](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L35-L35)
  - [observation/documented] Tendril can expose its server via Cloudflare Quick Tunnels so agent runs can be monitored and steered remotely. -- evidence: [README.md#L49-L49](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L49-L49)
- design-choices (1 claim(s)):
  - [observation/documented] Tendril positions itself as a developer tool for the agentic era, described as replacing the IDE when AI agents write most of the code. -- evidence: [README.md#L13-L13](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L13-L13), [README.md#L15-L17](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L15-L17)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: all development work must target the 'development' branch as the PR base, with 'main' updated only by merging development for releases. -- evidence: [AGENTS.md#L5-L5](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/AGENTS.md#L5-L5)
  - [observation/documented] Repository development practice: merge conflicts must be resolved file-by-file without blanket 'ours/theirs' strategies or deleting untouched development files, then verified with 'dotnet build src/Ivy.Tendril/Ivy.Tendril.slnx'. -- evidence: [AGENTS.md#L11-L13](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/AGENTS.md#L11-L13)
- skills-patterns (2 claim(s)):
  - [observation/documented] Official Tendril engineering and debugging skills can be installed with 'npx skills add ivy-interactive/ivy-tendril', optionally targeting a specific skill or agent such as github-copilot or cursor. -- evidence: [README.md#L138-L140](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L138-L140), [README.md#L155-L157](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L155-L157), [README.md#L132-L132](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L132-L132), [README.md#L221-L223](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L221-L223), [README.md#L144-L146](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L144-L146), [README.md#L136-L136](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L136-L136)
  - [observation/documented] Skills can also be installed as plugins for Claude Code, Codex, Gemini CLI, and Antigravity CLI, or copied into tool-specific skills directories. -- evidence: [README.md#L235-L239](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L235-L239), [README.md#L246-L249](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L246-L249), [README.md#L165-L165](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L165-L165), [README.md#L203-L205](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L203-L205), [README.md#L184-L187](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L184-L187), [README.md#L225-L225](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L225-L225)
- interfaces (3 claim(s)):
  - [observation/documented] Tendril works with any CLI agent that runs in a terminal, naming Claude Code, Codex, GitHub Copilot, Gemini, and OpenCode as examples. -- evidence: [README.md#L120-L120](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L120-L120), [README.md#L122-L129](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L122-L129)
  - [observation/documented] The CLI offers a desktop launch via 'tendril' and a headless web-server mode via 'tendril --web'. -- evidence: [README.md#L276-L279](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L276-L279), [README.md#L271-L274](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L271-L274), [README.md#L269-L269](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/README.md#L269-L269)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The installer bundles unmodified third-party runtimes including PowerShell Core, the .NET SDK, and OpenCode CLI, all MIT-licensed. -- evidence: [THIRD_PARTY_NOTICES.md#L15-L17](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L15-L17), [THIRD_PARTY_NOTICES.md#L9-L11](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L9-L11), [THIRD_PARTY_NOTICES.md#L21-L23](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L21-L23), [THIRD_PARTY_NOTICES.md#L3-L3](https://github.com/Ivy-Interactive/Ivy-Tendril/blob/3c17eb4573b3f28bac6d7db5b99a2f90d302a45a/THIRD_PARTY_NOTICES.md#L3-L3)
More evidence: [full detail](ivy-tendril.detail.md)

Metadata and full claim list: [full detail](ivy-tendril.detail.md)
Human notes ([notes](ivy-tendril.notes.md), never overwritten by build)

[Back to map index](../../index.md)
