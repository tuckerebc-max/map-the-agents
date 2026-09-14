# Changelog

All notable changes to Routa.js will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.5] - 2026-03-15

### Added
- **Tauri Desktop Menu Enhancements**
  - Added "Toggle Tool Mode (Essential/Full)" to View menu with `Cmd+Shift+T` shortcut
  - Added new "Navigate" menu with keyboard shortcuts:
    - Dashboard (`Cmd+1`)
    - Kanban Board (`Cmd+2`)
    - Agent Traces (`Cmd+3`)
    - Settings (`Cmd+,`)
  - Smart workspace ID detection for navigation items
  - Developer Mode now accessible from system menu instead of UI toggle

### Fixed
- **Kanban Repository Lifecycle**
  - Fixed broken navigation loop when adding repositories from Kanban page
  - Replaced broken "Add in Settings" link with inline RepoPicker component
  - Users can now clone/select repositories directly from Kanban without navigation
  - Auto-refreshes codebase list after successful repository addition

- **Tauri Static Route Handling**
  - Fixed routing for non-workspace pages (`/traces`, `/mcp-tools`, `/settings`)
  - Added proper static route mapping in Rust backend fallback service
  - All static pages now load correctly in Tauri desktop app

### Changed
- Improved menu structure organization:
  - File: Reload, Quit
  - View: Toggle DevTools, Toggle Tool Mode
  - Navigate: Dashboard, Kanban, Traces, Settings
  - Tools: Install Agents, MCP Tools

### Technical
- Updated `apps/desktop/src-tauri/src/lib.rs` with enhanced menu system
- Updated `crates/routa-server/src/lib.rs` with static route handling
- Updated `src/app/workspace/[workspaceId]/kanban/kanban-tab.tsx` with inline RepoPicker
- All fitness checks passing at 100%

## [0.2.4] - 2026-03-14

### Added
- Initial Tauri desktop application support
- Rust backend server integration
- Kanban board functionality
- Agent Client Protocol (ACP) support
- Multi-agent coordination features

### Fixed
- Various routing and navigation issues
- Static file serving in Tauri environment

---

For detailed commit history, see the [Git log](https://github.com/phodal/routa-js/commits/main).

