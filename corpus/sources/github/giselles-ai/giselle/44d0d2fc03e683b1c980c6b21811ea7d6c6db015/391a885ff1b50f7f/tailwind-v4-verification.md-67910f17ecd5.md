# Tailwind v4 verification (non-breaking)

This document outlines the minimal checks to verify token readiness for Tailwind v4.

## Goals
- Confirm `@theme` primitives are present and consistent (`internal-packages/ui/styles/tokens.css`).
- Ensure v3 bridge (`aliases.css`) provides required semantic utilities.
- Validate CI color report JSON is generated and uploaded as artifact.

## Steps
1. Review tokens in `tokens.css` and confirm coverage for neutrals/brand/status.
2. Confirm semantic scaffold exists (`semantic-tokens.md`) and is not globally applied.
3. On any PR, download the `report-colors` artifact from CI and inspect counts.
4. Prepare an isolated playground branch for the actual v4 bump (separate PR).

No runtime changes in this PR.


