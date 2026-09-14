# Contributing to Singulary

First of all, thank you for your interest in contributing to Singulary! Singulary is free, open source, and made better by other people poking at it.

## Getting Started Locally

Singulary is a monorepo managed with `pnpm`. You'll need **Node ≥ 22** and **pnpm 9** installed.

```bash
# Clone the repository
git clone https://github.com/sammwyy/singulary.git
cd singulary

# Install dependencies
pnpm install

# Start the development servers
pnpm dev
```

This will start:
- Frontend (Vite) at <http://localhost:5173>
- Backend API (Express) at <http://localhost:3000>

Vite is configured to automatically proxy `/api` requests to the backend.

### Creating an Admin User
If you need to test admin features locally, you can create an admin user from the CLI:

```bash
pnpm run admin:create -- --email admin@example.com --username admin
# A password will be generated and printed if --password is omitted
```

## Useful Commands

- `pnpm dev`: Start both frontend and backend development servers.
- `pnpm typecheck`: Run TypeScript type-checking across the repository.
- `pnpm build`: Build the frontend and backend for production.

## Making Changes

If you're planning a non-trivial change (like a major feature, an architecture refactor, or adding new runtime templates), **please open an issue first** so we can sketch out the shape of the feature together. This prevents wasted effort and ensures alignment with the project's vision.

Bug reports, small fixes, new templates, provider adapters, and docs improvements are all very welcome and can be submitted as Pull Requests directly.

## Development Guidelines

- **TypeScript**: We use strict TypeScript across the monorepo. Ensure `pnpm typecheck` passes.
- **Architecture**: Please review `ARCHITECTURE.md` to understand how the frontend and backend interact, as well as the data models (Workspaces, Projects, Services, Snapshots).
- **Agent Tools**: When adding new agent capabilities, define clear tool schemas and carefully consider the `risk_level` and `requires_approval` settings. Security is paramount when dealing with Docker socket access and code execution.
- **UI/UX**: The frontend is built with React and Tailwind CSS. Follow the existing component patterns in `apps/web/src/components/ui/`.

## Pull Request Process

1. Fork the repo and create your branch from `main`.
2. Make your changes and ensure your code is well-tested.
3. Run `pnpm typecheck` to catch any issues.
4. Open a PR describing what you changed, why, and how to test it.

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
