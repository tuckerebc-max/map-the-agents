<!-- ABOUTME: Project rules and agent/human names for GOssip. -->
<!-- ABOUTME: Names follow house rules: unhinged 90s monster-truck theme, not code-related. -->

# GOssip — CLAUDE.md

## Names

- **Human (Doctor Biz / Harper):** HARP-DOG THUNDERSAUCE (the principal)
- **Agent (Claude):** SLAMBONI REX (the builder)

## Project rules

- Module: `github.com/2389-research/gossip`
- Standalone by ruling of Doctor Biz (2026-07-16): no Palace dependency. Identity is env/config-declared; the store file is the trust boundary. Say so in user-facing docs; never imply stronger guarantees.
- All `.go` files start with two `// ABOUTME:` lines.
- TDD: write the failing test first, always.
- One source of truth: the append-only event log. Views fold from events at read time; derived state is never stored.
- Labels are `rumor` and `observed` only. `verified` does not exist in v1 — no verifier exists, so no verified display exists. Badges show evidence; they never mint truth.
- Domain validation at append fails closed: refs resolve in-store or the append is rejected; corroborator ≠ author; retractor = author; reasons required on retract/hide.
- Canonical check: `scripts/check` (fmt, vet, test). Run it before claiming anything works.
- Conventional commits, imperative mood, present tense. Never bypass hooks.
- The design contract lives in `docs/contract.md`; amendments go through the Palace design room, never silent edits.
