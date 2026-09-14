# v1.1.0 - Dashboard Deal Wizard

This release makes the dashboard much more usable for first-time open source users by moving core setup into the product itself.

## Highlights

- Added a dashboard-based New Deal Wizard for guided deal creation
- Added a saved deal library for drafts, ready deals, and shipped sample deals
- Added explicit saved-deal launch paths instead of relying on a single shared `config/deal.json`
- Added Playwright end-to-end coverage for the key dashboard flows
- Strengthened the dashboard build to typecheck both server and client TypeScript

## Included Dashboard Flows

- Create and save a draft deal
- Reopen and edit a saved draft
- Create a launch-ready deal and launch it from the wizard
- Launch a shipped sample deal from the deal library

## Verification

- `dashboard\\npm run build`
- `dashboard\\npm run test:e2e`
- `npm test`
- `dashboard\\npm audit --json` -> 0 vulnerabilities

## Notes

- Existing sample/demo flows remain available
- The new dashboard workflow is additive and does not remove manual config-based usage
