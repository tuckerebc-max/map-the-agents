
# Installing momo Code

> Detailed installation guide for first-time users.
> If you've already done `curl -fsSL https://momozi.cc/install | bash` and it worked, you can skip this file. If you hit issues, jump to [Troubleshooting](#troubleshooting).

## Requirements

| Requirement | Why | Check |
|-------------|-----|-------|
| **macOS or Linux** | the installer is bash + git + npm | `uname -s` |
| **Node.js ≥ 20** | runtime | `node -v` |
| **npm ≥ 9** | comes with Node | `npm -v` |
| **git** | clones the repo | `git --version` |
| **curl** | downloads the installer | `curl --version` |

Windows users: please run via WSL2 (Ubuntu/Debian).

## Method 1 — One-liner (recommended)

```bash
curl -fsSL https://momozi.cc/install | bash
```

What happens, step by step:

1. **Detect** your OS/arch (darwin/linux × x64/arm64)
2. **Try** to download a prebuilt binary from GitHub Releases
3. **Fall back** to "install from source": `git clone` into `~/.momo/lib/momo-code`, then `npm install` + `npm run build`
4. **Write** a small wrapper at `~/.momo/bin/momo`
5. **Append** `~/.momo/bin` to `~/.zshrc` (or `~/.bashrc` if you use bash)
6. **Print** where it landed + how to verify

You'll see (timings approximate on a modern Mac):

```
Installing momo version: 1.0.0
Release binary not available, installing from source...
Cloning from GitHub...
Installing dependencies (this may take a minute)...
Building from source...
Installed from source to /Users/<you>/.momo/lib/momo-code
Added /Users/<you>/.momo/bin to PATH in /Users/<you>/.zshrc
Run 'source /Users/<you>/.zshrc' to apply changes

momo Code v1.0.0 installed to /Users/<you>/.momo/bin/momo
Run 'momo --help' to get started
```

### After install — verify

**Open a new terminal** (or `source ~/.zshrc` in the current one), then:

```bash
momo --version           # → 1.0.0
momo --help              # shows the CLI menu
momo /evolve --demo      # exercises the experience loop end-to-end
momo /fine-tune          # shows training diagnosis
```

If `momo --version` works but `momo /evolve --demo` errors with `Cannot find module ...dist/cli/index.js`, your build didn't complete. Run:

```bash
cd ~/.momo/lib/momo-code/packages/opencode
npm install
npm run build
```

## Method 2 — From source (manual)

Use this when you want to hack on the code, or when the curl path fails.

```bash
# 1. clone
git clone https://github.com/momozi1996/momo-code.git
cd momo-code/packages/opencode

# 2. install deps (this installs typescript via devDependencies)
npm install

# 3. build (compiles TypeScript + fixes ESM paths)
npm run build

# 4. run
node bin/momo --version
node bin/momo --help

# 5. (optional) put on PATH
ln -s "$PWD/bin/momo" /usr/local/bin/momo
```

## First API call

momo Code talks to **any** OpenAI-compatible LLM API. Pick one:

### Anthropic (Claude)

```bash
export MOMO_PROVIDER=anthropic
export MOMO_ANTHROPIC_API_KEY=sk-ant-...
export MOMO_MODEL=claude-sonnet-4-20250514

momo "Refactor my login function to use async/await"
```

### OpenAI (GPT)

```bash
export MOMO_PROVIDER=openai
export MOMO_OPENAI_API_KEY=sk-...
export MOMO_MODEL=gpt-4.1

momo "What's wrong with this code?"
```

### Other built-in providers

`openrouter`, `google`, `minimax`, `zhipu`, `moonshot`, `doubao`, `stepfun`, `alibaba`, `mistral`, `groq`, `xai`.

Each uses `MOMO_<PROVIDER>_API_KEY` and (if needed) `MOMO_MODEL`. The generic `MOMO_API_KEY` is also honored.

### Self-evolution features (no API key needed)

These features work offline and only touch `~/.momo/experience/`:

```bash
momo /evolve --demo           # populate tactics from synthetic signals
momo /evolve --list           # show learned tactics with Bayesian stats
momo /fine-tune               # diagnose
momo /fine-tune run --auto    # full Curriculum → Train → Ratchet pipeline
```

## Where things live

```
~/.momo/
├── bin/
│   └── momo                       ← entry point (in your PATH)
├── lib/momo-code/                 ← cloned repo
│   └── packages/opencode/
│       ├── bin/momo               ← Node ESM entry
│       └── dist/                  ← compiled JavaScript
├── experience/
│   ├── tactics.json               ← learned tactics
│   └── ledger.jsonl               ← audit trail
└── finetune/
    ├── production.json            ← active production run pointer
    └── runs/<run-id>/             ← per-run artifacts
```

## Troubleshooting

### `command not found: momo` after install

Cause: PATH didn't pick up the new entry. Fix:

```bash
source ~/.zshrc      # for zsh users
source ~/.bashrc     # for bash users
```

If that still doesn't work, run directly:

```bash
~/.momo/bin/momo --version
```

If **that** works, the curl installer didn't write the PATH line. Add manually:

```bash
echo '' >> ~/.zshrc
echo '# momo Code CLI' >> ~/.zshrc
echo 'export PATH="$HOME/.momo/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Build fails with `tsc: command not found`

Cause: devDependencies didn't install (older npm or `--production` flag). Fix:

```bash
cd ~/.momo/lib/momo-code/packages/opencode
npm install            # NOT npm install --production
npm run build
```

### Build fails with `Cannot find module fix-esm.mjs`

The build step needs `scripts/fix-esm.mjs` to exist. Pull the latest main:

```bash
cd ~/.momo/lib/momo-code
git pull
```

### `momo /evolve` prints `0 tactics, 0 dedup hits`

Default `momo /evolve` waits for an input signal source. Use:

```bash
momo /evolve --demo     # built-in synthetic signals
momo /evolve --auto     # detect from cwd
```

### `momo "<prompt>"` prints nothing and returns 0

Cause: no `MOMO_API_KEY` (or provider-specific key) set. Fix:

```bash
export MOMO_API_KEY=sk-...     # generic
# or
export MOMO_PROVIDER=anthropic
export MOMO_ANTHROPIC_API_KEY=sk-ant-...
```

Then re-run.

### macOS Gatekeeper blocks the wrapper

If macOS complains about the unsigned wrapper script:

```bash
xattr -d com.apple.quarantine ~/.momo/bin/momo
```

### Re-install / upgrade

```bash
# safe re-install
rm -rf ~/.momo
curl -fsSL https://momozi.cc/install | bash
```

## Uninstall

```bash
# 1. remove install dir
rm -rf ~/.momo

# 2. clean up your shell rc (zsh)
sed -i.bak '/# momo Code CLI/,+1d' ~/.zshrc

# 2. or for bash
sed -i.bak '/# momo Code CLI/,+1d' ~/.bashrc

# 3. open a new terminal — `momo` should be gone
```

## Reporting issues

Open an issue: https://github.com/momozi1996/momo-code/issues

Useful info to include:
- `node -v` / `npm -v`
- `uname -sm`
- Output of `bash -x install 2>&1 | tail -50` (if install fails)
- Content of `/tmp/momo-install.log` (after our patch)
