# AGENTS.md

## Open-source hygiene

- Treat every tracked file as public. Never add personal, customer, employer, or debugging-session identifiers; local absolute paths; screenshots; credentials; or ephemeral deployment IDs.
- Use neutral fixtures and reserved domains such as `example.com`. Multilingual fixtures are welcome when they test encoding or i18n behavior, but they must not refer to a real private entity.
- Keep tests behavior-focused, deterministic, and portable. Do not depend on a contributor's machine, account, location, cached data, or a live third-party response.
- Keep documentation and UI copy useful to forks. Hard-code HashAgent's canonical URLs only where the official deployed product or source repository genuinely requires them; otherwise prefer configuration or neutral examples.
- Before handing off changes, run `npm run check`, `npm run build`, and `git diff --check`.
