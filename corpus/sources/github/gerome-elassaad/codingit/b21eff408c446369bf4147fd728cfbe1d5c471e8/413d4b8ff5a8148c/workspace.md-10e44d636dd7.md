# CodinIT.dev Workspace Guide

> **This is a pnpm workspace monorepo** containing two separate applications.

## 📦 Quick Overview

```
CodingIT/
├── @codinit/web (root)              - Next.js 14 web app → Vercel
└── @codinit/desktop (apps/desktop/) - Electron desktop app → Local installers
```

| Package | Location | Framework | Port | Deploy | Start |
|---------|----------|-----------|------|--------|-------|
| **@codinit/web** | `/` (root) | Next.js 14 | 3000 | Vercel | `pnpm dev` |
| **@codinit/desktop** | `/apps/desktop` | Remix + Electron | 5173 | Desktop | `pnpm desktop:dev` |

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pnpm install                    # Installs both workspaces
```

### 2. Configure Environment
```bash
# Web app
cp .env.example .env.local
# Edit .env.local with your API keys (E2B, Supabase, LLM providers)

# Desktop app (optional)
cd apps/desktop && cp .env.example .env
```

### 3. Start Development

**Web App:**
```bash
pnpm dev                        # http://localhost:3000
```

**Desktop App:**
```bash
pnpm desktop:dev                # http://localhost:5173
# OR: cd apps/desktop && pnpm dev
```

**Both Apps:**
```bash
# Terminal 1
pnpm dev

# Terminal 2
pnpm desktop:dev
```

---

## 📋 Command Reference

### Package Management
```bash
# Install all workspace dependencies
pnpm install

# Add dependency to web app
pnpm --filter @codinit/web add <package>

# Add dependency to desktop app
pnpm --filter @codinit/desktop add <package>

# Add dev dependency
pnpm --filter @codinit/web add -D <package>
```

### Development
```bash
# Web App
pnpm dev                        # Start with Turbopack (fast)
pnpm dev:webpack                # Start with Webpack
pnpm build                      # Build for production
pnpm start                      # Start production server
pnpm lint                       # Run ESLint

# Desktop App (from root)
pnpm desktop:dev                # Start desktop app
pnpm desktop:build              # Build desktop app
pnpm desktop:build:mac          # Build macOS .dmg
pnpm desktop:build:win          # Build Windows .exe
pnpm desktop:build:linux        # Build Linux .AppImage

# Or from apps/desktop/ directory
cd apps/desktop
pnpm dev                        # Start desktop app
pnpm build                      # Build desktop app
```

### Database
```bash
# Load schema in order (from supabase/ directory)
psql -f schemas/extensions.sql
psql -f schemas/sequences.sql
psql -f schemas/auth.sql
psql -f schemas/storage.sql
psql -f schemas/public.sql
```

---

## 🏗️ Architecture

### Visual Structure

```
┌─────────────────────────────────────────────────────┐
│           CodinIT (pnpm workspace)                  │
└─────────────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│  @codinit/web    │    │@codinit/desktop  │
│  (root)          │    │ (/desktop)       │
├──────────────────┤    ├──────────────────┤
│ Next.js 14       │    │ Remix + Electron │
│ Port: 3000       │    │ Port: 5173       │
│ E2B Sandboxes    │    │ WebContainer     │
│ Supabase         │    │ Cloudflare D1    │
│ Deploy: Vercel   │    │ Deploy: Desktop  │
└──────────────────┘    └──────────────────┘
```

### Directory Structure

```
CodinIT-2/
│
├── 📄 package.json                 # @codinit/web
├── 📄 pnpm-workspace.yaml          # Workspace config
├── 📄 pnpm-lock.yaml               # Unified lockfile
│
├── 📁 app/                         # Next.js app (web)
│   ├── [taskId]/                   # Task detail pages
│   ├── api/                        # API routes
│   │   ├── chat/                   # LLM chat endpoints
│   │   ├── tasks/                  # Task management
│   │   ├── sandbox/                # E2B sandbox control
│   │   └── github/                 # GitHub integration
│   └── settings/                   # Settings pages
│
├── 📁 components/                  # React components (web)
│   ├── ui/                         # shadcn/ui components
│   └── *.tsx                       # App components
│
├── 📁 lib/                         # Business logic (web)
│   ├── models.ts                   # LLM provider configs
│   ├── tasks.ts                    # Task management
│   ├── fragments.ts                # Code persistence
│   ├── sandbox.ts                  # E2B integration
│   └── supabase-*.ts               # Database clients
│
├── 📁 public/                      # Static assets (web)
├── 📁 supabase/                    # Database (shared)
├── 📁 sandbox-templates/           # E2B templates (shared)
│
└── 📁 apps/                        # Applications
    └── 📁 desktop/                 # @codinit/desktop
        ├── 📄 package.json         # Desktop package
        ├── 📁 app/                 # Remix app
        ├── 📁 electron/            # Electron processes
        └── 📁 build/               # Build output
```

### Technology Stack

| Feature | Web App | Desktop App |
|---------|---------|-------------|
| **Framework** | Next.js 14 (App Router) | Remix + Electron |
| **UI Library** | shadcn/ui + TailwindCSS | UnoCSS |
| **State** | React hooks | Nanostores |
| **Code Execution** | E2B Cloud Sandboxes | WebContainer (in-browser) |
| **Database** | Supabase (PostgreSQL) | Cloudflare D1 |
| **Auth** | Supabase Auth | Cookie-based |
| **AI SDK** | Vercel AI SDK | Vercel AI SDK |
| **Deployment** | Vercel, Docker | Desktop installers |
| **Build Output** | `.next/` | `build/` + Electron |

---

## 🚀 Deployment

### Web App → Vercel (Recommended)

**Automatic Setup:**
- Desktop app is **automatically excluded** via `.vercelignore`
- Only web app dependencies installed: `pnpm install --filter @codinit/web`
- Configured in `vercel.json`

**Vercel Dashboard Settings:**
| Setting | Value |
|---------|-------|
| Framework | Next.js (auto-detected) |
| Build Command | `pnpm build` |
| Install Command | `pnpm install --filter @codinit/web` |
| Output Directory | `.next` |
| Node.js Version | 18.x or 20.x |

**Environment Variables (set in Vercel Dashboard):**
```bash
# Required
E2B_API_KEY=xxx
SUPABASE_URL=xxx
SUPABASE_ANON_KEY=xxx

# LLM Providers (at least one)
OPENAI_API_KEY=xxx
ANTHROPIC_API_KEY=xxx
GOOGLE_AI_API_KEY=xxx
# ... others

# Optional
KV_REST_API_URL=xxx
KV_REST_API_TOKEN=xxx
NEXT_PUBLIC_POSTHOG_KEY=xxx
```

**Deploy:**
```bash
# Automatic via GitHub
git push origin main            # Auto-deploys to Vercel

# Manual via CLI
vercel --prod
```

**What Gets Deployed:**
- ✅ `/app`, `/components`, `/lib`, `/public`
- ✅ Root `package.json` (@codinit/web)
- ❌ `/apps` (excluded via `.vercelignore`)

### Desktop App → Native Installers

**NOT deployed to cloud platforms.**

```bash
# Build installers
pnpm desktop:build:mac          # macOS .dmg
pnpm desktop:build:win          # Windows .exe
pnpm desktop:build:linux        # Linux .AppImage

# Output
# desktop/dist/CodinIT-*.dmg
# desktop/dist/CodinIT Setup-*.exe
# desktop/dist/CodinIT-*.AppImage
```

**Distribute:**
- Upload installers to GitHub Releases
- Host on your website
- Distribute directly to users

---

## 🔧 Development Workflow

### Working on Web App

```bash
# Install dependencies
pnpm install

# Start dev server
pnpm dev                        # Port 3000

# Add dependency
pnpm --filter @codinit/web add axios

# Build
pnpm build

# Deploy
git push origin main            # Auto-deploys to Vercel
```

### Working on Desktop App

```bash
# Install dependencies
pnpm install

# Start dev server
pnpm desktop:dev                # Port 5173
# OR: cd apps/desktop && pnpm dev

# Add dependency
pnpm --filter @codinit/desktop add electron-store

# Build for testing
cd apps/desktop && pnpm build

# Build installer
pnpm desktop:build:mac
```

### Working on Both

```bash
# Terminal 1 - Web App
pnpm dev

# Terminal 2 - Desktop App
pnpm desktop:dev

# No port conflicts (3000 vs 5173)
```

---

## 📚 Additional Documentation

### Application-Specific Guides
- **Web App (Claude Code):** [CLAUDE.md](CLAUDE.md)
- **Desktop App (Claude Code):** [apps/desktop/CLAUDE.md](apps/desktop/CLAUDE.md)
- **Main README:** [README.md](README.md)

### Infrastructure
- **Database Schema:** [supabase/README.md](supabase/README.md)
- **API Setup:** [docs/api-setup.md](docs/api-setup.md)
- **GitHub Integration:** [docs/github-integration.md](docs/github-integration.md)

### Configuration Files
- `pnpm-workspace.yaml` - Workspace packages definition
- `vercel.json` - Vercel deployment config
- `.vercelignore` - Excludes apps/ from Vercel
- `.env.example` - Web app environment template
- `apps/desktop/.env.example` - Desktop app environment template

---

## 🐛 Troubleshooting

### Dependencies Won't Install

```bash
# Clear everything and reinstall
rm -rf node_modules apps/*/node_modules pnpm-lock.yaml
pnpm install
```

### Port Conflicts

Web and desktop apps use different ports (3000 vs 5173), so no conflicts should occur.

**Change ports if needed:**
- Web: Edit `package.json` dev script
- Desktop: Edit `desktop/package.json` dev script

### Vercel Deploys Desktop App

**Check:**
1. `.vercelignore` exists and contains `apps/`
2. `vercel.json` uses `pnpm install --filter @codinit/web`
3. Clear Vercel cache and redeploy

### Desktop Build Fails

```bash
cd apps/desktop
rm -rf node_modules dist build
pnpm install
pnpm build
```

### Environment Variables Missing

**Web App:**
- Copy `.env.example` to `.env.local`
- Set in Vercel Dashboard for production

**Desktop App:**
- Copy `apps/desktop/.env.example` to `apps/desktop/.env`

---

## 🎯 Key Features

### ✅ Workspace Benefits

**Shared Resources:**
- Single `pnpm-lock.yaml` for consistent dependencies
- Shared database schemas (`supabase/`)
- Shared E2B templates (`sandbox-templates/`)
- Single Git repository

**Independent Development:**
- Separate dependency trees
- Independent build processes
- Different deployment strategies
- No conflicts between apps

### ✅ Deployment Separation

**Web App (Cloud):**
- Vercel automatic deployment
- Desktop excluded via `.vercelignore`
- Fast cloud builds (only web dependencies)

**Desktop App (Local):**
- Native installers for each platform
- NOT deployed to cloud
- Distributed directly to users

---

## 📊 Comparison

| Aspect | Web App | Desktop App |
|--------|---------|-------------|
| **Package Name** | @codinit/web | @codinit/desktop |
| **Location** | `/` (root) | `/desktop` |
| **Framework** | Next.js 14 | Remix + Electron |
| **Runtime** | E2B Sandboxes | WebContainer |
| **Database** | Supabase | Cloudflare D1 |
| **Port** | 3000 | 5173 |
| **Deploy** | Vercel | Desktop installers |
| **Start** | `pnpm dev` | `pnpm desktop:dev` |
| **Build** | `pnpm build` | `pnpm desktop:build:*` |

---

## 🆘 Support

**Questions about:**
- **Workspace setup** → This file
- **Web app development** → [Webapp Docs](https://docs.codinit.dev)
- **Desktop app development** → [Desktop App Docs](https://gerome-elassaad.github.io/codinit-app)
- **Database** → [supabase/README.md](supabase/README.md)
- **Deployment** → Vercel section above

---

**Last Updated:** 2025-10-07
**Workspace Version:** 1.0
**Package Manager:** pnpm 10.18.0
