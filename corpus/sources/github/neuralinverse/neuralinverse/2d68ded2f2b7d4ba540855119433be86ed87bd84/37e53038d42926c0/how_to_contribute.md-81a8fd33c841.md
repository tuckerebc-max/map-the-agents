# Contributing to NeuralInverse CE

Welcome! We're glad you're here. NeuralInverse CE is open source and contributions of all kinds are welcome.

There are a few ways to contribute:

- Fix bugs or build new CE features - see [Issues](https://github.com/NeuralInverse/neuralinverse/issues)
- Improve documentation
- Report bugs or suggest features via [GitHub Issues](https://github.com/NeuralInverse/neuralinverse/issues/new/choose)
- Start a discussion in [GitHub Discussions](https://github.com/NeuralInverse/neuralinverse/discussions)


## Codebase overview

NeuralInverse CE is built on [VS Code](https://github.com/microsoft/vscode). The codebase is large but most CE-specific code lives in a few folders:

- `src/vs/workbench/contrib/void/` - AI chat and agent infrastructure
- `src/vs/workbench/contrib/powerMode/` - Power Mode agentic workflows
- `src/vs/workbench/contrib/neuralInverseModernisation/` - Legacy code modernization
- `src/vs/workbench/contrib/neuralInverseFirmware/` - Firmware datasheet tooling

We recommend reading the [VS Code codebase guide](https://github.com/microsoft/vscode/wiki/Source-Code-Organization) to get oriented.


## Setting up your dev environment

### Prerequisites

**macOS**: Python and Xcode (usually pre-installed)

**Windows**: Install [Visual Studio 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community) with these workloads:
- `Desktop development with C++`
- `Node.js build tools`

And these individual components:
- `MSVC v143 - VS 2022 C++ x64/x86 Spectre-mitigated libs (Latest)`
- `C++ ATL for latest build tools with Spectre Mitigations`
- `C++ MFC for latest build tools with Spectre Mitigations`

**Linux**:
- Debian/Ubuntu: `sudo apt-get install build-essential g++ libx11-dev libxkbfile-dev libsecret-1-dev libkrb5-dev python-is-python3`
- Fedora: `sudo dnf install @development-tools gcc gcc-c++ make libsecret-devel krb5-devel libX11-devel libxkbfile-devel`
- openSUSE: `sudo zypper install patterns-devel-C-C++-devel_C_C++ krb5-devel libsecret-devel libxkbfile-devel libX11-devel`

**Node version**: Use Node `20.18.2` (see `.nvmrc`). With nvm: `nvm install && nvm use`


## Running in developer mode

1. Clone the repo:
   ```bash
   git clone https://github.com/NeuralInverse/neuralinverse
   cd neuralinverse
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the build watcher (inside VS Code or NeuralInverse CE):
   - Windows/Linux: `Ctrl+Shift+B`
   - macOS: `Cmd+Shift+B`

   Or from terminal: `npm run watch`

   Wait until you see:
   ```
   [watch-extensions] Finished compilation with 0 errors
   [watch-client    ] Finished compilation with 0 errors
   ```

4. Open the dev window:
   - macOS/Linux: `./scripts/code.sh`
   - Windows: `./scripts/code.bat`

5. After making changes, reload with `Ctrl+R` / `Cmd+R` inside the dev window.


## Building a local executable

This takes ~25 minutes. Make sure you've run the dev mode steps above first.

**macOS**:
```bash
npm run gulp vscode-darwin-arm64   # Apple Silicon
npm run gulp vscode-darwin-x64     # Intel
```

**Windows**:
```bash
npm run gulp vscode-win32-x64
npm run gulp vscode-win32-arm64
```

**Linux**:
```bash
npm run gulp vscode-linux-x64
npm run gulp vscode-linux-arm64
```

Output appears in a folder outside the repo (e.g. `../VSCode-darwin-arm64/`).


## Common issues

- **Node version mismatch**: Run `nvm install && nvm use` to match `.nvmrc`
- **Path with spaces**: Make sure the repo path has no spaces
- **`TypeError: Failed to fetch dynamically imported module`**: Check all imports end with `.js`
- **React build error**: Run `NODE_OPTIONS="--max-old-space-size=8192" npm run buildreact`
- **Missing styles**: Wait a few seconds and reload
- **`libtool` error on macOS**: Install GNU libtool (`brew install libtool`)
- **SUID sandbox error on Linux**: Run `sudo chown root:root .build/electron/chrome-sandbox && sudo chmod 4755 .build/electron/chrome-sandbox`


## Submitting a pull request

- Fork the repo and create a branch for your change
- Keep PRs focused - one fix or feature per PR
- Make sure the build passes before submitting
- **Do not use non-ASCII characters in TypeScript/JavaScript string literals** - this breaks the release build
- Fill in the PR template
- Submit against `main`


## Questions?

Open a [GitHub Discussion](https://github.com/NeuralInverse/neuralinverse/discussions) or email github@neuralinverse.com.
