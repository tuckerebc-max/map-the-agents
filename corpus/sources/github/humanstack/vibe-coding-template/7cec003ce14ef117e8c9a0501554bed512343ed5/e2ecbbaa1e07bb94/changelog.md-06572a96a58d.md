# Changelog

All notable changes to the Vibe Coding Template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive Cursor Rules system (`.cursor/rules/`) for AI-assisted development
- `AGENTS.md` file with consolidated AI agent instructions
- Context-aware development guidance that automatically applies based on file patterns
- Production-ready code templates for common patterns:
  - FastAPI endpoint template (`@api-endpoint-template`)
  - React component template (`@react-component-template`)
  - Service class template (`@service-class-template`)
- Backend-specific rules for FastAPI, Supabase integration, and LLM services
- Frontend-specific rules for Next.js, authentication, and API integration
- Database migration patterns and best practices
- Development workflow automation and troubleshooting guides

### Changed
- Updated README.md to include AI development support section
- Reorganized project structure to highlight AI-powered development features
- Enhanced documentation with links to new Cursor rules and agent instructions
- Marked legacy context files in `llm-context/` as superseded by Cursor rules

### Improved
- Development experience with automatic context-aware guidance
- Code consistency through enforced patterns and templates
- Onboarding for new developers with comprehensive AI assistance
- Development speed through template system and best practices

## [1.0.0] - Initial Release

### Added
- Full-stack application template with Next.js frontend and FastAPI backend
- Supabase integration for authentication, database, and storage
- LLM integration with OpenAI and Anthropic support
- Vector database integration with Qdrant
- Docker-based development environment
- Database migration system with Supabase CLI
- Authentication flows with OAuth providers (Google, LinkedIn)
- Comprehensive service layer architecture
- Type-safe API development with Pydantic models
- Responsive frontend with Tailwind CSS
- Development automation with Makefile commands
- First-time setup script for easy onboarding

### Features
- **Backend**: FastAPI with async/await patterns, service layer architecture
- **Frontend**: Next.js with TypeScript, Tailwind CSS, and authentication
- **Database**: Supabase PostgreSQL with Row Level Security (RLS)
- **Authentication**: Multi-provider OAuth with Supabase Auth
- **LLM Services**: Abstracted text generation and embedding services
- **Vector Database**: Semantic search with Qdrant integration
- **Development**: Docker Compose, hot-reload, automated migrations
- **Documentation**: Comprehensive guides and context files

---

## Release Notes

### Cursor Rules System (Latest)

The addition of the Cursor Rules system represents a significant enhancement to the development experience:

**Key Benefits:**
- **Automatic Context**: Rules automatically apply based on the files you're working with
- **Template System**: Production-ready code patterns accessible via `@template-name`
- **Consistency**: Enforced coding standards and architectural patterns
- **Speed**: Accelerated development through AI-assisted coding
- **Quality**: Built-in best practices and error handling patterns

**Migration from Legacy Context:**
- Legacy context files in `llm-context/` are still available but superseded
- New development should use Cursor rules for better integration
- `AGENTS.md` provides a simplified alternative for basic AI assistance

**Getting Started:**
1. Cursor rules work automatically - no setup required
2. Reference templates when creating new components or endpoints
3. Rules provide context-aware guidance based on current work
4. Customize rules as your project evolves

For detailed information about using the new system, see the [Cursor Rules Guide](./.cursor/rules/README.md).
