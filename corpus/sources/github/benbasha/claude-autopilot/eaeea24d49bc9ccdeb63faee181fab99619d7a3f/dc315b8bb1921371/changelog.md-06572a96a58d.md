# Changelog

All notable changes to the Claude Autopilot extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.6] - 2025-08-21

### 🔧 Fixed

- **Enhanced Usage Limit Parsing**: Added support for new Claude limit message format "X-hour limit reached ∙ resets TIME"
- **Backward Compatibility**: Maintained compatibility with existing "reset at" format detection
- **Unicode Support**: Support for various bullet characters (∙, •, ·) in limit messages

## [0.1.5] - 2025-08-09

### 🔧 Fixed

- **Claude CLI Compatibility**: Adapted to Claude CLI changes by improving detection of CLI readiness with ANSI-styled prompt line recognition

## [0.1.4] - 2025-08-01

### ✨ Added

- **WSL Integration**: Comprehensive Windows Subsystem for Linux (WSL) integration for Win32 command execution
- **Cross-Platform Command Detection**: Enhanced command detection with WSL fallback support for Windows users

### 🔧 Improved

- **Windows Compatibility**: Better Windows development environment support through WSL integration
- **Command Execution**: More reliable command execution across different Windows configurations

## [0.1.3] - 2025-07-30

### 🔧 Fixed

- **Windows Claude CLI Detection**: Improved Claude CLI detection with PowerShell fallback for better Windows compatibility

### 📦 Changed

- **Package Size**: Removed ngrok dependency to reduce package size and improve installation performance

## [0.1.2] - 2025-07-29

### ✨ Added

- **Web Interface**: Mobile web interface with QR code access and external server support
- **File Explorer API**: Full file system browsing through web interface
- **Git Interface**: Complete git operations management through web interface
- **Claude Web Interface**: Direct Claude CLI interaction from mobile devices

### 🔧 Fixed

- **Python Missing Error on Windows**: Fixed Python detection issues (#11)

## [0.1.1] - 2025-07-15

### ✨ Added

-   **Message ID System**: Each queue message now has a unique identifier for better tracking and management
-   **History Visibility Controls**: New configuration option to show/hide history section in the UI
-   **Scheduled Session Start**: Added ability to schedule Claude Autopilot to start at specific times (HH:MM format)
-   **Enhanced UI Controls**: Replaced checkbox with sleek iOS-style toggle for skip permissions setting
-   **Complete Config Implementation**: Full configuration system with validation and real-time updates
-   **ID Generator Utility**: New utility service for generating unique message identifiers
-   **Security Service**: Enhanced security validation and XSS protection controls
-   **Scheduler Service**: New service for handling timed operations and session scheduling

### 🔧 Fixed

-   **Queue Persistence**: Resolved issues with pending queue not persisting across sessions
-   **Auto-start Issues**: Fixed problems with automatic session startup functionality
-   **History Saving**: Fixed bug where processing history was not being saved properly
-   **Multiline Message Handling**: Improved handling of multiline messages and Enter key submission
-   **Configuration References**: Updated README and documentation to use correct `claudeAutopilot.*` configuration keys

## [0.1.0] - 2025-07-15

### 🎉 Major Rebrand

-   **Extension Renamed**: Complete rebrand from "ClaudeLoop" to "Claude Autopilot"
-   **New Package Name**: Changed from `claude-loop` to `claude-autopilot`
-   **Updated Commands**: All commands now use `claude-autopilot.*` prefix
-   **New Repository**: Moved to `https://github.com/benbasha/Claude-Autopilot`

### ✨ Added

-   **Collaboration Guide**: Added comprehensive `COLLABORATION.md` with contribution guidelines
-   **Updated Configuration**: All settings now use `claudeAutopilot.*` namespace
-   **Consistent Branding**: Updated all UI text, documentation, and user-facing messages

### 🔧 Changed

-   **Breaking Change**: Configuration keys changed from `claudeLoop.*` to `claudeAutopilot.*`
-   **Command IDs**: Updated from `claude-loop.*` to `claude-autopilot.*`
-   **Repository URLs**: All links now point to new GitHub repository

### 📚 Documentation

-   **README**: Updated with new branding and repository links
-   **Architecture**: Updated CLAUDE.md with new command references
-   **Deployment**: Updated deployment guide with new package information

## [0.0.4] - 2025-07-14

### ✨ Added

-   **Cross-platform keyboard shortcuts**: Added Cmd+Enter (Mac) and Ctrl+Enter (Windows/Linux) support for adding messages to queue
-   **Visual keyboard hints**: Added helpful text showing available keyboard shortcuts in the interface
-   **Improved input layout**: Enhanced styling and layout of the message input section

### 🔧 Fixed

-   Better cross-platform compatibility for keyboard shortcuts
-   Improved user experience with visual feedback for available shortcuts

## [0.0.3] - 2025-07-13

### 🔧 Fixed

-   Fixed webview loading error in packaged extension
-   Improved extension reliability and stability

## [0.0.2] - 2025-07-13

### ✨ Added

-   **Beautiful icon**: Added professional icon representing automation while sleeping
-   **Visual branding**: Enhanced extension appearance in VS Code marketplace

### 🔧 Fixed

-   Updated icon and branding elements
-   Improved extension presentation

## [0.0.1] - 2025-07-13

### 🎉 Initial Alpha Release - Claude Code Task Management

This initial alpha release provides automated task management for Claude Code with intelligent queue processing and auto-resume functionality.

### ✨ Added

#### 🏗️ **Modular Architecture**

-   Complete refactor from monolithic (1900+ lines) to modular design (20+ focused modules)
-   Organized codebase with clear separation of concerns
-   Improved maintainability and extensibility

#### 🔧 **Robust Dependency Management**

-   Comprehensive Claude Code installation detection
-   Cross-platform Python detection with version validation (3.8+)
-   PTY wrapper file validation and error recovery
-   Platform-specific installation instructions
-   Automatic retry mechanisms with helpful error messages

#### ⚙️ **Advanced Configuration System**

-   Extensive configuration options with built-in validation
-   Real-time configuration change detection
-   Helpful error messages for invalid settings
-   Configuration reset functionality
-   Development mode with debugging features

#### 🛡️ **Comprehensive Error Handling**

-   Try-catch blocks throughout critical code paths
-   Proper error recovery with state cleanup
-   User-friendly error messages with suggested solutions
-   Automatic retry mechanisms with exponential backoff
-   Process management error recovery

#### 🔄 **Production-Ready Features**

-   Development mode features properly gated for production
-   Timer cleanup in extension deactivation
-   Process cleanup and resource management
-   Configuration validation on startup
-   Health monitoring and process recovery

### 🚀 **Enhanced Features**

#### 📋 **Queue Management**

-   Message size validation and truncation
-   Queue operations: add, remove, duplicate, edit, reorder
-   Automatic queue maintenance and cleanup
-   Memory usage monitoring and reporting
-   Queue history with filtering and search

#### 🖥️ **Cross-Platform Compatibility**

-   Windows, macOS, and Linux support
-   Platform-specific Python detection
-   Cross-platform sleep prevention methods
-   Platform-appropriate error messages and solutions

#### 📊 **User Interface Improvements**

-   Enhanced webview with better error handling
-   Real-time status updates and progress tracking
-   Configuration validation status display
-   Memory usage statistics (development mode)
-   Improved visual feedback and notifications

### 🔒 **Security & Privacy**

-   Input validation and XSS prevention
-   Content Security Policy implementation
-   No external data collection or transmission
-   Local-only processing and storage
-   Secure dependency validation

### 🛠️ **Developer Experience**

-   Development mode with advanced debugging features
-   Configuration validation tools
-   Memory usage monitoring
-   Process health diagnostics
-   Debug logging and diagnostics

### 📝 **Configuration Options**

All new configuration options with validation:

```json
{
    "claudeLoop.developmentMode": false,
    "claudeLoop.queue.maxSize": 1000,
    "claudeLoop.queue.maxMessageSize": 50000,
    "claudeLoop.queue.maxOutputSize": 100000,
    "claudeLoop.queue.retentionHours": 24,
    "claudeLoop.queue.autoMaintenance": true,
    "claudeLoop.session.autoStart": false,
    "claudeLoop.session.skipPermissions": true,
    "claudeLoop.session.healthCheckInterval": 30000,
    "claudeLoop.sleepPrevention.enabled": true,
    "claudeLoop.sleepPrevention.method": "auto",
    "claudeLoop.history.maxRuns": 20,
    "claudeLoop.history.autoSave": true,
    "claudeLoop.logging.enabled": false,
    "claudeLoop.logging.level": "info"
}
```

### 🔧 **Technical Improvements**

-   TypeScript strict mode compliance
-   Comprehensive type definitions
-   Modular imports and exports
-   Async/await patterns throughout
-   Promise-based error handling
-   Resource cleanup and memory management

### 🏃‍♂️ **Performance**

-   Reduced memory footprint
-   Faster startup times
-   Efficient queue processing
-   Optimized timer management
-   Better resource utilization

### 🧪 **Quality Assurance**

-   Comprehensive code review
-   Error handling validation
-   Cross-platform testing
-   Memory leak testing
-   Configuration validation testing

### 📦 **Packaging & Distribution**

-   Updated marketplace metadata
-   Comprehensive documentation
-   Installation guides for all platforms
-   Troubleshooting documentation
-   Development setup instructions

---

---

## Development Roadmap

### Future Enhancements (Planned)

-   📊 Usage analytics and telemetry (opt-in)
-   🧪 Comprehensive test suite
-   📱 Mobile-friendly webview
-   🔌 Plugin system for custom processors
-   📈 Performance monitoring and optimization
-   🌐 Multi-language support
-   🎨 Theme customization
-   📋 Template system for common tasks

### Community Requests

-   Integration with other AI CLI tools
-   Batch file processing
-   Export/import functionality
-   Advanced filtering and search
-   Collaboration features
-   Cloud synchronization (optional)

---

**Note**: Claude Autopilot is not affiliated with Anthropic or Claude AI. Claude Code is a product of Anthropic.
