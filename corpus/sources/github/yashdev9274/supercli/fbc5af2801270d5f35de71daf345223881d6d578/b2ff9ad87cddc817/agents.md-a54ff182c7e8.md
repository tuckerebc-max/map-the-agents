# Agent Instructions for Supercode Monorepo

## Build Commands

```bash
# Root level commands
bun run dev          # Start all dev servers
bun run build        # Build all packages and apps
bun run lint         # Run linting across all packages
bun run typecheck    # Run TypeScript checks across all packages

# Individual app/package commands
bun run dev:web      # Start only web app (Next.js)
bun run dev:api      # Start only API app
bun run dev:cli      # Start only CLI app

# Package-specific commands (run from package directory)
cd packages/db && bun run db:generate    # Generate Prisma client
cd packages/db && bun run db:migrate     # Deploy Prisma migrations
```

**Note:** This project uses Bun as the package manager (`bun@1.2.21`).

## Testing

Uses `bun test` (Bun's built-in test runner). Test files use `*.test.ts` convention.

```bash
# Run all tests
bun test

# Run a single test file
bun test path/to/file.test.ts

# Run tests in watch mode
bun test --watch
```

## Code Style Guidelines

### Imports
- Use absolute imports with path aliases: `@/components/ui/button` for web app
- Use workspace imports for cross-package dependencies: `@super/db`, `@super/auth`
- Import order: React/Next → External libs → Internal aliases → Relative imports
- Group imports by category with blank lines between groups

### Formatting
- No semicolons at end of statements
- Use double quotes for strings
- 2-space indentation
- Trailing commas in multi-line objects/arrays
- No explicit return type on function components (inferred)

### Naming Conventions
- **Components:** PascalCase (e.g., `Button.tsx`, `HeroSection.tsx`)
- **Files:** kebab-case for non-component files (e.g., `utils.ts`, `query-provider.tsx`)
- **Functions:** camelCase (e.g., `signIn`, `getSession`)
- **Types/Interfaces:** PascalCase (e.g., `VariantProps`)
- **Constants:** UPPER_SNAKE_CASE for true constants

### Types & TypeScript
- Strict mode enabled (`strict: true` in tsconfig)
- Use `type` for type aliases when possible
- Export types explicitly when needed for consumers
- Use `interface` for object shapes that may be extended
- Prefer explicit return types on library functions

### Error Handling
- Use try-catch for async operations
- Validate with Zod for form/API inputs
- Return early pattern for guard clauses
- Use `!` operator sparingly; prefer proper null checks

### React Patterns
- Server Components by default (Next.js App Router)
- 'use client' directive only when needed (hooks, browser APIs)
- Composition pattern for component variants (see `buttonVariants` pattern)
- `forwardRef` pattern for component ref forwarding
- Destructure props in function parameters

### Styling (Tailwind CSS v4)
- Use `cn()` utility from `@/lib/utils` for conditional classes
- Prefer semantic CSS variables over hardcoded values
- Use `data-slot` attributes for component identification
- Follow CVA (class-variance-authority) pattern for variants

### Database (Prisma)
- Schema location: `packages/db/prisma/schema.prisma`
- Always regenerate client after schema changes: `bun run db:generate`
- Use `@map()` for custom table names in snake_case
- Add indexes for frequently queried foreign keys

### Monorepo Structure
```
apps/
  web/           # Next.js 16 web app (main)
  api/           # API app (scaffolded)
  supercode-cli/ # CLI app (scaffolded)
packages/
  db/            # Prisma database client
  auth/          # Better-Auth authentication
  secrets/       # Infisical secrets wrapper (@super/secrets)
  ui/            # Shared UI components (empty)
  sdk/           # SDK package (empty)
  config/        # Shared config (empty)
  dashboard/     # Dashboard components
```

### Environment Variables
- Web app: `apps/web/.env` or `apps/.env.local`
- Required for auth: `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, `NEXT_PUBLIC_BETTER_AUTH_URL`
- Required for DB: `DATABASE_URL`
- Voice/STT: `SMALLEST_API_KEY` (Smallest.ai Pulse STT — the only STT provider), `SMALLEST_MODEL`, `STT_LANGUAGE`. Voice TTS (spoken reply): `VOICE_REPLY` (`on`|`off`), `ELEVENLABS_VOICE_ID`, `ELEVENLABS_TTS_MODEL` (macOS `say` fallback when no key). Note `ELEVENLABS_API_KEY` doubles as both STT and TTS key historically; STT now always routes to Smallest.ai.
- Voice web search (server): `CONTEXT_DEV_API_KEY` (Context.dev — web search provider; fallback legacy alias `CONTEXTDEV_API_KEY`), `EXA_API_KEY` (web search provider; the server tries the provider the model picked, then falls back to the other), `FIRECRAWL_API_KEY` (Firecrawl web search provider — optional third provider; the voice agent may use context.dev, exa, or firecrawl depending on the request).
- Voice open-app tool (server): no key needed; the `/api/voice/chat` `open_app` tool runs `open` locally on the Mac the server runs on.
- Voice system-control tool (server): no key needed; the `/api/voice/chat` `system_control` tool runs locally on the Mac the server runs on — volume up/down/mute/unmute (osascript, no permission), lock screen (`CGSession -suspend`), sleep display (`pmset displaysleepnow`), quit app (osascript `tell application to quit`), and media play/pause/next/prev (System Events key codes — needs Accessibility permission).
- Voice screen-region selection (client): Cmd+drag over any window selects a screen region; Jarvis then crops its screen-vision frame to that region and sends `screenSelection: true` so the server tells the model to focus only on the selected content (e.g. select part of a page → "explain this"). Escape or a new Cmd+drag clears/replaces. Implemented in `apps/jarvis/Jarvis/managers/ScreenSelectionManager.swift` (borderless `.screenSaver` overlay windows that ignore mouse events; global + local event monitors — global drag end is detected via `NSEvent.pressedMouseButtons` since global monitors don't receive mouseUp) with crop math in `ScreenVisionManager.croppedScreenImageDataURL(rect:displayID:)`; server flag handled in the `/api/voice/chat` handler.
- Secrets: `INFISICAL_CLIENT_ID`, `INFISICAL_CLIENT_SECRET` (when Infisical is configured)

### Linting
- ESLint configured for web app only (`apps/web/eslint.config.mjs`)
- Uses `eslint-config-next/core-web-vitals` and `eslint-config-next/typescript`
- Run: `bun run lint` (from root) or `bun run lint` (from web directory)

### Git
- Branch naming: `supercli-#<issue-number>`
- No pre-commit hooks configured yet

## Key Dependencies
- **Framework:** Next.js 16, React 19, TypeScript 5
- **Auth:** Better-Auth with Prisma adapter
- **DB:** PostgreSQL with Prisma ORM
- **UI:** Radix UI primitives + Tailwind CSS v4
- **State:** TanStack Query (React Query)
- **Forms:** React Hook Form + Zod

## Conventions to Follow
1. Always run `bun run db:generate` after modifying `schema.prisma`
2. Use `workspace:*` for internal package dependencies
3. Keep components in `components/` folder, organized by feature
4. Use barrel exports (`index.ts`) for clean package APIs
5. Prefer Server Components; mark 'use client' only when necessary
6. Follow existing patterns in `apps/web/components/ui/` for new UI components


