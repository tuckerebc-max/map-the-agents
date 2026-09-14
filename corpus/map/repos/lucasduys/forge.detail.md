# lucasduys/forge -- full detail

[Back to orientation](forge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lucasduys/forge/642c60b104f0d5dae9782dd4b54f12df407c9697/6c3a4dda31584cbd.json](../../../wiki/dossiers/lucasduys/forge/642c60b104f0d5dae9782dd4b54f12df407c9697/6c3a4dda31584cbd.json)

## specifications (1 claim(s))

- [observation/documented] The brainstorm phase turns a one-line idea into an R-numbered spec with testable acceptance criteria, and every task must map to at least one R-number. -- evidence: [README.md#L121-L121](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L121-L121), [README.md#L39-L43](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L39-L43) (`clm_f6c319071be93e39acc6028b2c95c01675ea56733979472c08e65d3d5d8891fc`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The pipeline is strictly sequential (brainstorm → plan → execute), enforced programmatically via an approval gate, frontier validation, and validateWorkflowPrerequisites(); users cannot skip phases or bypass the approval gate. -- evidence: [docs/architecture.md#L96-L103](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L96-L103), [README.md#L121-L121](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L121-L121) (`clm_588e39db7c286b8c93bb7da4fa10d054f0796c34c399e4070238090e7e917fca`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors fork, create a feature branch, make changes, run tests via node scripts/run-tests.cjs, and open a pull request, with details in CONTRIBUTING.md. -- evidence: [README.md#L212-L216](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L212-L216), [README.md#L218-L218](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L218-L218) (`clm_bfd22f57d63d5e22c703f937550a37f9a51d53257b9196c648c8eec54f58ba07`)

## skills-patterns (1 claim(s))

- [observation/documented] Three cross-cutting skills run automatically across agents: Karpathy guardrails inlined into executor/reviewer/planner, graphify knowledge-graph integration, and DESIGN.md design-system support — the latter two degrade gracefully when their inputs are absent. -- evidence: [docs/architecture.md#L85-L92](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L85-L92), [docs/architecture.md#L76-L83](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L76-L83), [docs/architecture.md#L70-L74](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L70-L74) (`clm_4977431eac43653209ff0a689d311348494eb9135cbf0a43ea8e801e6828e2be`)

## interfaces (2 claim(s))

- [observation/documented] Users drive Forge through slash commands such as /forge brainstorm, /forge plan, /forge execute --autonomy full, plus read-only /forge watch and /forge status --json, and /forge resume for recovery. -- evidence: [README.md#L62-L66](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L62-L66), [README.md#L166-L177](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L166-L177) (`clm_bc672e8177971df89a04bba9462ece25460b908b1047b3f2dade6df745b7ae96`)
- [observation/documented] Collaboration defines a transport interface (read, cas, del, list, publish/subscribe/sendTargeted) with two backends: Ably WebSocket pub/sub (sub-second) and a zero-setup polling backend over a git branch (~2.5s). -- evidence: [docs/architecture.md#L115-L115](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L115-L115), [docs/architecture.md#L117-L120](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L117-L120) (`clm_fbd0c35540ca633f028dc65e8f032c328568e2fedd1ed77189c18ace4180f505`)

## memory-state (1 claim(s))

- [observation/documented] Loop state lives on disk in a .forge directory rather than in the conversation, so crashes, context resets, and OOMs can recover by restarting the state machine from disk. -- evidence: [README.md#L45-L45](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L45-L45) (`clm_88ab7ddbabbfd84bd3c844bcbf6949ce082fd9147a997987816ddb136a6c5a6b`)

## orchestration (1 claim(s))

- [observation/documented] Tasks execute in their own git worktrees with TDD, and passing tasks are squash-merged atomically; a streaming topological scheduler dispatches tasks as soon as their dependencies complete. -- evidence: [docs/architecture.md#L27-L64](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L27-L64), [README.md#L39-L43](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L39-L43), [docs/architecture.md#L9-L9](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L9-L9) (`clm_696ada2127727a365c79c22631e5bfa307de7a143e6ae6eb0aa5e0e4aff4e957`)

## tools-permissions (1 claim(s))

- [observation/documented] In gated (default) mode Forge pauses before installing new dependencies or calling paid APIs; full mode assumes prior consent for those, but both modes require explicit approval to push to a remote and refuse destructive git ops unless the spec requests them. -- evidence: [README.md#L125-L136](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L125-L136), [README.md#L138-L138](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L138-L138) (`clm_4466f295dd87052bbb8e2612d5e6539d4107514e336d52c9fb64ccd51145bb7e`)

## evaluation (1 claim(s))

- [observation/documented] The docs report measured token-savings results for the product's optimization filters, including a real A/B run where filtering a git diff cut Claude token use from 59,600 to 42,402 (28.9% fewer), and caveman compression benchmarks of 26.8% prose reduction. -- evidence: [docs/caveman.md#L33-L34](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/caveman.md#L33-L34), [README.md#L154-L162](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L154-L162) (`clm_3242efdd939c21cc39092d49baed1aa494578b6fcb95023d79531923b623a84e`)

## dependencies (1 claim(s))

- [observation/documented] Forge requires Claude Code v1.0.33+; the solo path needs no npm install, and Ably is an optional dependency only for multiplayer collaboration. -- evidence: [README.md#L56-L56](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L56-L56), [README.md#L49-L49](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L49-L49), [docs/architecture.md#L117-L120](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L117-L120) (`clm_158884c1c06613fbae3b1ea498ac501ce1122204075e3ceafef6cb79b45577d5`)

## limitations (1 claim(s))

- [observation/documented] The docs acknowledge that FORGE_COMPLETE only means tasks done, tests green, reviewer and verifier satisfied; a feature passing all four can still look broken in a browser because unit tests don't render pixels. -- evidence: [README.md#L142-L142](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L142-L142) (`clm_74e177d8ffb796d82c7a26823ea64e1acb904ef33835517ff19c10900941513a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

