# itayinbarr/little-coder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a9e467f2be43 @ c1c886905f97db58

## Summary (orientation draft, not independently verified)

README-only evidence for little-coder, a coding agent built on pi and tuned for small local models, describing its extension set, launcher behavior, shell permission gate, background-job tools, model configuration, and published benchmark results. Evidence coverage: 125 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] little-coder is built on pi as a plain dependency, adding roughly 30 extensions, 30 skill markdown files, and a Python benchmark harness under .pi/extensions/, skills/, and benchmarks/. -- evidence: [README.md#L14-L14](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L14-L14)
  - [observation/documented] ShellStart runs background jobs with wake_on triggers (exit, regex match, silence, every_n_matches), delivering bounded excerpts plus exit code, with ShellLog, ShellList, ShellSend, and ShellStop companions. -- evidence: [README.md#L307-L312](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L307-L312), [README.md#L314-L319](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L314-L319), [README.md#L321-L321](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L321-L321)
- design-choices (3 claim(s)):
  - [observation/documented] The launcher runs pi with --no-extensions and wires in only the bundled set, keeping cold-start context near 7k tokens and making loaded behavior fixed at ship time. -- evidence: [README.md#L16-L16](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L16-L16)
  - [observation/documented] Per-phase model selection lets planning and implementation use different models via /plan-model, /action-model, and /model-handover auto|manual, with handover deferred until implementation begins. -- evidence: [README.md#L331-L337](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L331-L337), [README.md#L341-L341](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L341-L341)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Users can opt into extra extensions via ~/.config/little-coder/extensions/, the LITTLE_CODER_EXTRA_EXTENSIONS variable, or a --with-pi-extensions relaunch; /extensions shows what loaded. -- evidence: [README.md#L18-L18](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L18-L18)
  - [observation/documented] The CLI accepts --model (e.g. llamacpp/qwen3.6-35b-a3b, anthropic/claude-haiku-4-5, ollama/qwen3.5, lmstudio/local-model) and --list-models; bare invocation launches the models.json default. -- evidence: [README.md#L48-L52](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L48-L52), [README.md#L56-L56](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L56-L56), [README.md#L60-L66](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L60-L66)
- memory-state (1 claim(s)):
  - [observation/documented] Background jobs outlive a turn but not the session: they run in their own process group, are reaped on shutdown, and carry a watchdog that kills the group if little-coder's pid disappears. -- evidence: [README.md#L323-L323](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L323-L323)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Shell calls are gated against a built-in safe-prefix whitelist before pi's confirmation flow; rm and sudo are excluded, and LITTLE_CODER_BASH_ALLOW adds prefixes per deployment. -- evidence: [README.md#L345-L345](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L345-L345)
  - [observation/documented] Every command in a chain is judged individually, and any shell write via redirects, tee, or dd of= is refused; LITTLE_CODER_PERMISSION_MODE offers auto, accept-all, and manual modes. -- evidence: [README.md#L349-L350](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L349-L350), [README.md#L356-L359](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L356-L359)
- evaluation (1 claim(s)):
More evidence: [full detail](little-coder.detail.md)

Metadata and full claim list: [full detail](little-coder.detail.md)
Human notes ([notes](little-coder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
