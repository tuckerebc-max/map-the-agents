# harnessrouter/harnessrouter -- full detail

[Back to orientation](harnessrouter.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/harnessrouter/harnessrouter/5637717816b5923c58bb3b1779e1ccab7359349f/c748d5b31d944b02.json](../../../wiki/dossiers/harnessrouter/harnessrouter/5637717816b5923c58bb3b1779e1ccab7359349f/c748d5b31d944b02.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] One Docker container runs three parts: Console on :3000 (only published port, entry point for UI and API), Gateway on :8080 (Responses API and harness lifecycle), and Runner on :8081 (runs harnesses in session workspaces). -- evidence: [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323) (`clm_2a264bdbc6cf7163747479e2563d2228f99b90f244d17babfdf5157d928a6687`)
- [observation/documented] A /data volume persists the database, files, secrets, installed harness CLIs, and workspaces across container restarts. -- evidence: [README.md#L76-L76](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L76-L76), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323) (`clm_ac540355f2735fe65cf002c40adb78b1a4296b55c27a4b2df42bce2c6f52b610`)

## design-choices (2 claim(s))

- [observation/documented] Sessions use separate workspaces and operating-system users rather than separate containers; the Console and Gateway run unprivileged while the entrypoint and Runner need root to manage per-session users. -- evidence: [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L85-L85](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L85-L85) (`clm_657c66e3b5e815c686d892e912afcd550d020ee23108a4b89c83e268f42d7bb5`)
- [observation/documented] Community Edition disables the Console analytics pipeline, and provider keys, sessions, files, and workspaces remain under the self-hosting operator's control. -- evidence: [README.md#L286-L289](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L286-L289) (`clm_59a33dbb925a14a8fbe3d177e149e105fa0e75556ea8ff4bdb6514de67cc0801`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: substantial changes require an issue describing problem, proposal, and impact before implementation; small obvious fixes may go straight to a pull request. -- evidence: [CONTRIBUTING.md#L27-L29](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L27-L29), [CONTRIBUTING.md#L31-L32](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L31-L32) (`clm_6818878674cdb7981e0b6b0d1dc21b436eecb27c306161c6448b4c93e55cb09e`)
- [observation/documented] Repository development practice: protocol changes follow a UEP process (issue labelled 'uep' with Problem, Proposal, Compatibility, Alternatives; maintainer response within 10 working days; accepted UEPs land as one PR updating spec, schema, implementation, conformance test, and changelog). -- evidence: [CONTRIBUTING.md#L36-L42](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L36-L42) (`clm_09d7b48b2c01a0ef2e3b11cc39a9f9512bcbab4e757179e2fc64210528c9a519`)
- [observation/documented] Repository development practice: main accepts PRs only with one approval and all checks green, no self-approval; agent-driven PRs are opened via an 'open-pr' workflow as github-actions[bot]. -- evidence: [CONTRIBUTING.md#L82-L85](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L82-L85), [CONTRIBUTING.md#L87-L90](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L87-L90) (`clm_bc2992af2dd306609af118971956e4ac9ffc32f9531edee8beca8ea0b72d0ac7`)
- [observation/documented] Repository development practice: contributor checks include npm type-check/test/build for the console, pytest for the gateway, and building the image plus walking the self-hosted flow for container changes. -- evidence: [CONTRIBUTING.md#L72-L73](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L72-L73), [CONTRIBUTING.md#L68-L70](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L68-L70), [CONTRIBUTING.md#L58-L64](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L58-L64) (`clm_d8e73c1c1a9f59525009408ae781e7da160376e5a67f1eacb55ac5e7b637e8fb`)
- [observation/documented] Repository development practice: harness-support changes must be measured against five scenarios per harness and model plus a custom harness with its own skill and tool policy, judged by code-enforced rules per docs/harness-verification.md. -- evidence: [CONTRIBUTING.md#L12-L17](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L12-L17) (`clm_814b17e26d0e35ca4d7c41029c87f04f4e9f0754d75c68d61551b1ecb28d470e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes an OpenAI Responses-compatible API; callers select a harness via metadata.harness_id and can set stream:true for server-sent events. -- evidence: [README.md#L197-L206](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L197-L206), [README.md#L35-L35](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L35-L35), [README.md#L186-L186](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L186-L186), [README.md#L208-L208](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L208-L208) (`clm_46969869d5117528e88af70833f12218724ee8f9b629dc8ba5408d72b9f51c67`)
- [observation/documented] The API surface supports starting tasks, continuing sessions with previous_response_id, streaming progress, file attach/retrieve, cancellation, and structured errors/traces. -- evidence: [README.md#L214-L224](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L214-L224) (`clm_0ef56bd52ff2bf8205a1a36f75be03098f132cdb4686b54255baec8170b14aec`)
- [observation/documented] The project implements the Unified Harness Protocol (UHP), a versioned public contract whose task surface is deliberately compatible with the OpenAI Responses API, with spec, schemas, and conformance suite in the repo. -- evidence: [README.md#L335-L335](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L335-L335), [README.md#L337-L337](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L337-L337), [README.md#L339-L348](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L339-L348) (`clm_564a3e27b3b8e5aa588df1507c7b532302b9daf74f19c5773dd2d7036aa38347`)

## memory-state (1 claim(s))

- [observation/documented] The product handles persistent sessions: follow-up instructions can be sent with previous_response_id, and tasks with transcripts appear in the same Console workspace. -- evidence: [README.md#L214-L224](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L214-L224), [README.md#L35-L35](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L35-L35), [README.md#L208-L208](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L208-L208) (`clm_c5ae0912b8e34c7e43b1d00d5502955ab37192f70074d5ffe7c83d78183ba3cb`)

## orchestration (1 claim(s))

- [observation/documented] The Runner executes harnesses inside per-session workspaces, and the first container launch installs the enabled harness CLIs. -- evidence: [README.md#L97-L97](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L97-L97), [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323) (`clm_b2ebb52efb770194de9e23493e8876977bfbf858ba75e5de184bac5f92c854fd`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] README benchmark figures compare eight harness-and-model configurations on the same task, reporting best-vs-worst cost (223 to 0.47 credits) and end-to-end latency (4m36s to 1m25s), with methodology linked externally. -- evidence: [README.md#L46-L46](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L46-L46), [README.md#L41-L44](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L41-L44) (`clm_be401918ae212601f9cda08dc2055f173efdb60890bd1a5a5be51c93279a548a`)

## dependencies (2 claim(s))

- [observation/documented] Running the Community Edition requires Docker, about 4 GB of disk, and a user-supplied provider API key; no bundled model or trial key is included. -- evidence: [README.md#L65-L65](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L65-L65), [README.md#L63-L63](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L63-L63) (`clm_1ba4e3d95ad2157d7ab1d5e9a8b16acafcc9e7575b5ecf7620b3470880328033`)
- [observation/documented] Agent harness CLIs are installed on first launch and remain governed by their respective upstream licenses; the edition itself is Apache 2.0. -- evidence: [README.md#L97-L97](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L97-L97), [README.md#L379-L379](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L379-L379) (`clm_c80f2ec2b4c6b97e415d39d84c23f1409741682ebcba03ae75f09919f7239cf1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

