# Contributing to Orbit Editor
### Welcome! 👋
This is the official guide on how to contribute to Orbit Editor. We want to make it as easy as possible to contribute, so if you have any questions or comments, reach out via [GitHub issues](https://github.com/ashish200729/orbiteditor/issues) or join our [Discord server](https://discord.gg/ZPYkjPCDj8)!

There are a few ways to contribute:

- 💫 Complete items on the [Project Board](https://github.com/ashish200729/orbiteditor/projects).
- 💡 Make suggestions in [GitHub Issues](https://github.com/ashish200729/orbiteditor/issues).
- 🪴 Start new Issues — see [Issues](https://github.com/ashish200729/orbiteditor/issues).

### Codebase Guide

Orbit Editor is a fork of [Void Editor](https://github.com/voideditor/void), which is itself a fork of [VS Code](https://github.com/microsoft/vscode).

We [highly recommend reading this](./ORBIT_CODEBASE_GUIDE.md) guide that we put together on Orbit's source code if you'd like to add new features.

The repo is not as intimidating as it first seems if you read the guide!

Most of Orbit's code lives in the folder `src/vs/workbench/contrib/orbit/`.

## Editing Orbit's Code

If you're making changes to Orbit's code as a contributor, you'll want to run a local version of Orbit to make sure your changes worked. Developer mode lets you do this. Here's how to use it.

### a. Mac - Prerequisites

If you're using a Mac, you need Python and XCode. You probably have these by default.

### b. Windows - Prerequisites

If you're using a Windows computer, first get [Visual Studio 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community) (recommended) or [VS Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools) (not recommended). If you already have both, you might need to run the next few steps on both of them.

Go to the "Workloads" tab and select:
- `Desktop development with C++`
- `Node.js build tools`

Go to the "Individual Components" tab and select:
- `MSVC v143 - VS 2022 C++ x64/x86 Spectre-mitigated libs (Latest)`
- `C++ ATL for latest build tools with Spectre Mitigations`
- `C++ MFC for latest build tools with Spectre Mitigations`

Finally, click Install.

### c. Linux - Prerequisites

First, run `npm install -g node-gyp`. Then:

- Debian (Ubuntu, etc): `sudo apt-get install build-essential g++ libx11-dev libxkbfile-dev libsecret-1-dev libkrb5-dev python-is-python3`.
- Red Hat (Fedora, etc): `sudo dnf install @development-tools gcc gcc-c++ make libsecret-devel krb5-devel libX11-devel libxkbfile-devel`.
- SUSE (openSUSE, etc): `sudo zypper install patterns-devel-C-C++-devel_C_C++  krb5-devel libsecret-devel libxkbfile-devel libX11-devel`.
- Others: see [How to Contribute](https://github.com/microsoft/vscode/wiki/How-to-Contribute).

### Developer Mode Instructions

Here's how to start changing Orbit's code. These steps cover everything from cloning Orbit, to opening a Developer Mode window where you can play around with your updates.

1. `git clone https://github.com/ashish200729/orbiteditor` to clone the repo.
2. `npm install` to install all dependencies.
3. Open VSCode or another editor, and initialize Developer Mode (this can take ~5 min to finish, it's done when 2 of the 3 spinners turn to check marks):
   - Windows: Press <kbd>Ctrl+Shift+B</kbd>.
   - Mac: Press <kbd>Cmd+Shift+B</kbd>.
   - Linux: Press <kbd>Ctrl+Shift+B</kbd>.
4. Open the Orbit Developer Mode window:
   - Windows: `./scripts/code.bat`.
   - Mac: `./scripts/code.sh`.
   - Linux: `./scripts/code.sh`.
5. You're good to start editing Orbit's code!
   - You won't see your changes unless you press <kbd>Ctrl+R</kbd> (<kbd>Cmd+R</kbd>) inside the new window to reload. Alternatively, press <kbd>Ctrl+Shift+P</kbd> and `Reload Window`.
   - You might want to add the flags `--user-data-dir ./.tmp/user-data --extensions-dir ./.tmp/extensions` to the command in step 4, which lets you reset any IDE changes you made by deleting the `.tmp` folder.
   - You can kill any of the build scripts by pressing `Ctrl+D` in its terminal. If you press `Ctrl+C` the script will close but will keep running in the background.

If you get any errors, scroll down for common fixes.

#### Common Fixes

- Make sure you followed the prerequisite steps above.
- Make sure you have Node version `20.18.2` (the version in `.nvmrc`).
    - You can do this without changing your global Node version using [nvm](https://github.com/nvm-sh/nvm): run `nvm install`, followed by `nvm use` to install the version in `.nvmrc` locally.
- Make sure the path to your Orbit folder does not have any spaces in it.
- If you get `"TypeError: Failed to fetch dynamically imported module"`, make sure all imports end with `.js`.
- If you get an error with React, try running `NODE_OPTIONS="--max-old-space-size=8192" npm run buildreact`.
- If you see missing styles, wait a few seconds and then reload.
- If you get errors like `npm error libtool:   error: unrecognised option: '-static'`,  when running ./scripts/code.sh, make sure you have GNU libtool instead of BSD libtool (BSD is the default in macos)
- If you get errors like `The SUID sandbox helper binary was found, but is not configured correctly` when running ./scripts/code.sh, run
`sudo chown root:root .build/electron/chrome-sandbox && sudo chmod 4755 .build/electron/chrome-sandbox` and then run `./scripts/code.sh` again.
- If you have any other questions, feel free to [submit an issue](https://github.com/ashish200729/orbiteditor/issues/new). You can also refer to VSCode's complete [How to Contribute](https://github.com/microsoft/vscode/wiki/How-to-Contribute) page.

#### Building Orbit from Terminal

To build Orbit from the terminal instead of from inside VSCode, follow the steps above, but instead of pressing <kbd>Cmd+Shift+B</kbd>, run `npm run watch`. The build is done when you see something like this:

```
[watch-extensions] [00:37:39] Finished compilation extensions with 0 errors after 19303 ms
[watch-client    ] [00:38:06] Finished compilation with 0 errors after 46248 ms
[watch-client    ] [00:38:07] Starting compilation...
[watch-client    ] [00:38:07] Finished compilation with 0 errors after 5 ms
```

### Distributing

Orbit's maintainers distribute Orbit on [orbiteditorai.com](https://orbiteditorai.com). The build pipeline is based on the VS Code and Void Editor build systems, with GitHub Actions for packaging, signing, and auto-update.

If you want to completely control Orbit's build pipeline for your own internal usage, which comes with a lot of time cost (and is typically not recommended), you may need to set up your own build infrastructure. See [docs/BUILD_MACOS.md](./docs/BUILD_MACOS.md) for macOS release builds.

#### Building a Local Executable
We don't usually recommend building a local executable of Orbit — typically you should follow the steps above to distribute a complete executable, or you should just use Developer Mode to run Orbit locally which is much faster. If you're certain this is what you want, see details below.

<details>
	<summary> Building Locally (not recommended)</summary>
If you're certain you want to build a local executable of Orbit, follow these steps. It can take ~25 minutes.

Make sure you've already entered Developer Mode with Orbit first, then run one of the following commands. This will create a folder named `Orbit-darwin-arm64` or similar outside of the orbiteditor/ repo (see below).


##### Mac
- `npm run gulp vscode-darwin-arm64` - most common (Apple Silicon)
- `npm run gulp vscode-darwin-x64` (Intel)

##### Windows
- `npm run gulp vscode-win32-x64` - most common
- `npm run gulp vscode-win32-arm64`

##### Linux
- `npm run gulp vscode-linux-x64` - most common
- `npm run gulp vscode-linux-arm64`


##### Local Executable Output

The local executable will be located in a folder outside of `orbiteditor/`:
```bash
workspace/
├── orbiteditor/         # Your Orbit fork
└── Orbit-darwin-arm64/  # Generated output
```

</details>

## Pull Request Guidelines

- Please submit a pull request once you've made a change.
- No need to submit an Issue unless you're creating a new feature that might involve multiple PRs.
- Please don't use AI to write your PR 🙂
- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before participating.
