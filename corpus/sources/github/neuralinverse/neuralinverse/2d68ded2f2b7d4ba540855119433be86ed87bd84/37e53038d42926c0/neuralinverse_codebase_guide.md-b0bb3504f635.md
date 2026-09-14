# NeuralInverse CE Codebase Guide

The NeuralInverse CE codebase is not as intimidating as it seems!

Most CE-specific code lives in `src/vs/workbench/contrib/`.

The purpose of this document is to explain how the codebase works. If you want build instructions instead, see [HOW_TO_CONTRIBUTE.md](./HOW_TO_CONTRIBUTE.md).


## Codebase Guide

### VSCode Rundown
NeuralInverse CE is built on VS Code, which is an Electron app. Electron runs two processes: a **main** process (for internals) and a **browser** process (browser means HTML in general, not just "web browser").

You can also see Microsoft's [wiki](https://github.com/microsoft/vscode/wiki/Source-Code-Organization) for more detail.

- Code in a `browser/` folder always lives on the browser process, and it can use `window` and other browser items.
- Code in an `electron-main/` folder always lives on the main process, and it can import `node_modules`.
- Code in `common/` can be used by either process, but doesn't get any special imports.
- The browser environment is not allowed to import `node_modules`. Two workarounds:
  1. Bundle the raw node_module code to the browser - used for React.
  2. Implement the code on `electron-main/` and set up a channel between main/browser - used for sendLLMMessage.


### Terminology

- An **Editor** is the thing that you type your code in. If you have 10 tabs open, that's just one editor! Editors contain tabs (or "models").
- A **Model** is an internal representation of a file's contents. It's shared between editors.
- Each model has a **URI** it represents, like `/Users/.../my_file.txt`.
- The **Workbench** is the wrapper that contains all the editors, the terminal, the file system tree, etc.
- Usually you use the `ITextModel` type for models and the `ICodeEditor` type for editors.

- VS Code is organized into "**Services**". A service is just a class that mounts a single time (singleton). You can register services with `registerSingleton` so that you can easily use them in any constructor with `@<Service>`. The registration is the same every time.

- "**Actions**" are functions you register on VS Code so that either you or the user can call them later. They're also called "**Commands**". You can run actions as a user by pressing Cmd+Shift+P, or internally via `commandService`. We use actions to register keybinding listeners like Cmd+L, Cmd+K, etc.


### Internal LLM Message Pipeline

Sending LLM messages from the main process avoids CSP issues with local providers and lets us use node_modules more easily.

**Notes:** `modelCapabilities` is an important file that must be updated when new models come out!


### Apply

There are two types of Apply: **Fast Apply** (uses Search/Replace), and **Slow Apply** (rewrites whole file).

When Fast Apply is enabled, we prompt the LLM to output Search/Replace block(s) like this:
```
<<<<<<< ORIGINAL
// original code goes here
=======
// replaced code goes here
>>>>>>> UPDATED
```
This allows quickly applying code even on 1000-line files.

### Apply Inner Workings

The `editCodeService` file runs Apply. The same code is used when the LLM calls the Edit tool and when you submit Cmd+K.

- A **DiffZone** is a {startLine, endLine} region of text where we compute and show red/green areas, or **Diffs**.
- A **DiffArea** is a generalization that just tracks line numbers like a DiffZone.
- The only type of DiffArea that can "stream" is a DiffZone.

How Apply works:
- When you click Apply, we create a **DiffZone** over the full file so that any LLM changes show up in red/green. We then stream the change.
- When an LLM calls Edit, it's really calling Apply.
- When you submit Cmd+K, it's the same as Apply except we create a smaller DiffZone.


### Writing Files
When NeuralInverse CE wants to change your code, it writes to a text model. All you need is the file's URI - you don't have to load it, save it, etc. This is handled in `voidModelService`.

### Settings
`voidSettingsService` stores all settings (providers, models, global preferences). It's an implicit dependency for any of the core services.

Terminology:
- **FeatureName**: Autocomplete | Chat | CtrlK | Apply
- **ModelSelection**: a {providerName, modelName} pair.
- **ProviderName**: The name of a provider: `'ollama'`, `'openAI'`, etc.
- **ModelName**: The name of a model (string type, e.g. `'gpt-4o'`).
- **RefreshProvider**: a provider we ping repeatedly to update the models list.
- **ChatMode**: normal | gather | agent


### Approval State
`editCodeService`'s data structures contain all information about changes the user needs to review.


## VS Code Codebase References

<details>

#### Links for Beginners

- [VS Code UI guide](https://code.visualstudio.com/docs/getstarted/userinterface) - covers auxbar, panels, etc.
- [UX guide](https://code.visualstudio.com/api/ux-guidelines/overview) - covers Containers, Views, Items, etc.

#### Links for Contributors

- [How VS Code's source code is organized](https://github.com/microsoft/vscode/wiki/Source-Code-Organization) - explains entry point files, what `browser/` and `common/` mean, etc.
- [Built-in VS Code styles](https://code.visualstudio.com/api/references/theme-color) - CSS variables built into VS Code.

#### Misc

- [Every command](https://code.visualstudio.com/api/references/commands) built-in to VS Code.
- Note: VS Code's repo is the source code for the Monaco editor.

</details>
