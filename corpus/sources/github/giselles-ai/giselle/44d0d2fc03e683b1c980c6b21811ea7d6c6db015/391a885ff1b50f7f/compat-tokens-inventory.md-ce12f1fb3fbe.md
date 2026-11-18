### Compat tokens inventory (snapshot)

Targets: `--color-white-900`, `--color-black-600`, `--color-black-850`, `--color-white-850` (excluding `tokens.css`)

Run: `pnpm report:compat-tokens`

Sample output

```
Token: --color-white-900
  ./apps/playground/app/globals.css:32:  --color-white-900: hsl(220, 60%, 98%);
  ./apps/playground/app/globals.css:139:   color: var(--color-white-900);
  ./apps/playground/app/globals.css:243:   color: var(--color-white-900);
  ./apps/studio.giselles.ai/app/globals.css:32:  --color-white-900: hsl(220, 60%, 98%);
  ./apps/studio.giselles.ai/app/globals.css:39:  --color-white: var(--color-white-900);
  ... (more)

Token: --color-black-600
  ./apps/playground/app/globals.css:15:  --color-black-600: hsl(222, 17%, 53%);
  ./apps/studio.giselles.ai/app/globals.css:15:  --color-black-600: hsl(222, 17%, 53%);

Token: --color-black-850
  ./apps/playground/app/globals.css:12:  --color-black-850: hsl(231, 62%, 6%);
  ./apps/studio.giselles.ai/app/globals.css:12:  --color-black-850: hsl(231, 62%, 6%);

Token: --color-white-850
  ./apps/playground/app/globals.css:33:  --color-white-850: hsl(0, 0%, 96%);
  ./apps/studio.giselles.ai/app/globals.css:33:  --color-white-850: hsl(0, 0%, 96%);

Compat tokens references (excluding tokens.css): 18
```

Notes
- Mostly from `globals.css`; candidates for staged removal after semantic migration.
- Next steps: move to scopes/semantic and plan to reduce compat token references to zero.


