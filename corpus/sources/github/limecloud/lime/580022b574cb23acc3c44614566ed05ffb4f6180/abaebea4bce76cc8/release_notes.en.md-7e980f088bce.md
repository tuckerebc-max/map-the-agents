## Lime v1.144.1

Simplified Chinese release notes are the primary version.

### New Features

- None.

### Fixes

- Fixed the Windows CLI npm build by enabling the `windows-sys` `Win32_System_IO` feature required by `WriteFile`.

### Improvements and Refactoring

- None.

### Testing and Quality

- Re-ran TUI Rust tests, formatting checks, and version consistency gates; GitHub Actions validates the cross-platform CLI artifacts.

### Documentation

- None.

### Other

- This patch release does not move the already published `v1.144.0` tag; CLI npm publishing continues through GitHub Actions npm Trusted Publishing.

**Full changes**: `v1.144.0` -> `v1.144.1`
