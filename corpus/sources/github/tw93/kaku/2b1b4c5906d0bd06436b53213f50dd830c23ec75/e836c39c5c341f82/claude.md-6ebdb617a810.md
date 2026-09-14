# Kaku

Kaku is a macOS-native terminal emulator derived from WezTerm and tuned for AI-assisted terminal work.

## Agent Entry Points

- Read `AGENTS.md` first for the repository map, subsystem guides, risk areas, and verification matrix.
- Read the nearest crate-level `AGENTS.md` before changing code inside a crate.
- Use `.agents/skills/maintainer-sweep/SKILL.md` for GitHub issue/PR sweeps, CI-gated pushes, public replies, and closure decisions.
- Use `.agents/skills/bugs/SKILL.md` for proactive latent-bug / multi-entry UX sweeps with no reported symptom yet. After fixing one update or destructive-action surface, sibling-sweep the other entry points before declaring done.
- Keep private release credentials, local keychain setup, and machine-specific runbooks out of tracked documentation.

## Common Commands

```bash
make fmt-check
make check
make test
make app
./scripts/build.sh
./scripts/check_release_notes.sh
./scripts/check_release_config.sh
./scripts/check_config_release_readiness.sh
```

`make fmt` and `make fmt-check` both run `cargo +nightly fmt`, so both require the nightly toolchain. Use `make app` when the change touches GUI, rendering, windowing, input, or AI overlay behavior.

## Project-Specific Rules

Risk areas, the `config_version` release contract, startup-cache rules, and the verification matrix live in `AGENTS.md` (Current Risk Areas, Verification); this file does not restate them.

## Git and Maintainer Flow

- When the maintainer asks to commit or push, finish the requested git operation after the checks that match the change.
- For multiple unrelated bugs, prefer one commit per issue or behavior. Use subjects such as `fix(scope): #123 short summary` when an issue number exists.
- Public issue and PR replies should be drafted first unless the maintainer has already approved the wording, closure decision, and CI gate.
- After pushing a fix to `main`, wait for the new GitHub Actions run to pass before posting fixed/closed replies.
