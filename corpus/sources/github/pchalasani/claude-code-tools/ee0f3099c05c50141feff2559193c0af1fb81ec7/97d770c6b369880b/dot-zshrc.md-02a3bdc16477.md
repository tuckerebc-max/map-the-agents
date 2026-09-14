# Zsh Shell Setup Guide

This guide covers the essential setup for a productive Zsh environment with
Oh My Zsh, plugins, and Starship prompt.

## Prerequisites

1. **Install Homebrew** (macOS package manager)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Zsh** (usually pre-installed on macOS)
   ```bash
   brew install zsh
   ```

## Oh My Zsh Installation

Install Oh My Zsh framework for managing Zsh configuration:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

This creates `~/.oh-my-zsh` directory and a basic `~/.zshrc` file.

## Essential Plugins

### 1. Zsh Autosuggestions

Suggests commands as you type based on history and completions:

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
```

### 2. Zsh Syntax Highlighting

Provides syntax highlighting for the shell:

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 3. Configure Plugins in .zshrc

Add to your `~/.zshrc`:

```bash
# Oh My Zsh path
export ZSH="$HOME/.oh-my-zsh"

# Plugins configuration
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

# Source Oh My Zsh (commented out if using Starship)
# source $ZSH/oh-my-zsh.sh

# Source autosuggestions manually if needed
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
```

## Starship Prompt

Starship is a minimal, blazing-fast, and customizable prompt for any shell.

### Installation

```bash
curl -sS https://starship.rs/install.sh | sh
```

### Configuration

Add to the end of your `~/.zshrc`:

```bash
eval "$(starship init zsh)"
```

### Starship Configuration File

You can customize starship by creating/editing `~/.config/starship.toml`.

I recommend this `catppuccin` preset:

```bash
starship preset catppuccin-powerline -o ~/.config/starship.toml
```

But if you want to tweak it, see the starship config docs.
https://starship.rs/guide/

## Enhanced Directory Listings with eza

Eza is a modern replacement for `ls` with colors, icons, and Git integration.

### Installation

```bash
brew install eza
```

### Configuration

Add these aliases to your `~/.zshrc` to replace default `ls` commands:

```bash
# Replace ls with eza for beautiful directory listings
alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons --group-directories-first --header'
alias la='eza -la --icons --group-directories-first --header'
alias lt='eza --tree --icons --level=2'
alias ltd='eza --tree --icons --level=2 --only-dirs'

# Extended eza aliases
alias l='eza -lbF --git --icons'                # list with git status
alias llm='eza -lbGd --git --sort=modified'     # long list, modified date sort
alias lls='eza -lbhHigmuSa --time-style=long-iso --git --color-scale'  # full details
```

### Features

- **Icons**: Shows file type icons (requires a Nerd Font)
- **Colors**: Color-codes files by type and permissions
- **Git Integration**: Shows git status in listings
- **Tree View**: Built-in tree view with `--tree` flag
- **Sorting**: Groups directories first by default

### Usage Examples

```bash
ls              # Basic listing with icons
ll              # Long format with details
la              # Show hidden files
lt              # Tree view (2 levels)
l               # List with git status indicators
```

## Terminal Title Management

Add custom terminal title that shows current directory:

```bash
# Disable auto-setting terminal title
DISABLE_AUTO_TITLE="true"

# Set terminal title to current directory
function precmd () {
  echo -ne "\033]0;$(print -rD $PWD)\007"
}
precmd

# Show command being executed in title with rocket emojis
function preexec () {
  print -Pn "\e]0;🚀 $(print -rD $PWD) $1 🚀\a"
}
```

## History Search Enhancement

### Option 1: Atuin (Modern Shell History)

Install Atuin for enhanced history search:

```bash
brew install atuin
```

Configure in `~/.zshrc`:

```bash
export ATUIN_NOBIND="true"
eval "$(atuin init zsh)"
# Bind to up arrow keys (depends on terminal)
bindkey '^[[A' _atuin_search_widget
bindkey '^[OA' _atuin_search_widget
```

### Option 2: HSTR (Simple History Search)

```bash
brew install hstr
```

Configure in `~/.zshrc`:

```bash
alias hh=hstr
setopt histignorespace           # skip cmds w/ leading space from history
export HSTR_CONFIG=hicolor       # get more colors
bindkey -s "\C-r" "\C-a hstr -- \C-j"  # bind hstr to Ctrl-r
```

## Useful Aliases

Add these productivity aliases to your `~/.zshrc`:

```bash
# Git aliases
alias gsuno="git status -uno"        # git status without untracked files
alias gspu="git stash push -m"       # stash with message
alias gspop="git stash pop"          # pop stash
alias gsl="git stash list"           # list stashes

# Quick git commit amend and push
function gcpq() {
  ga -u
  git commit --amend --no-edit
  git push origin main --force-with-lease
}

# Tmux aliases
alias tmnew="tmux new -s "
alias tmls="tmux ls"
alias tma="tmux a -t "
alias tmk="tmux kill-session -t "
alias tmd="tmux detach"
```

## Completion System

Enable advanced tab completion:

```bash
autoload -Uz compinit
zstyle ':completion:*' menu select
fpath+=~/.zfunc
```

## Environment Variables

Set common environment variables:

```bash
export EDITOR="nano"  # or "vim", "code", etc.
export TERM=xterm-256color
```

## Final .zshrc Structure

Your `~/.zshrc` should follow this general structure:

```bash
# 1. Oh My Zsh configuration
export ZSH="$HOME/.oh-my-zsh"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# 2. Source additional files
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# 3. Environment variables
export EDITOR="nano"
export TERM=xterm-256color

# 4. Aliases and functions
alias gsuno="git status -uno"
# ... more aliases

# 5. Terminal title customization
DISABLE_AUTO_TITLE="true"
function precmd () { ... }
function preexec () { ... }

# 6. History search tool (Atuin or HSTR)
eval "$(atuin init zsh)"

# 7. Completion system
autoload -Uz compinit
zstyle ':completion:*' menu select

# 8. Starship prompt (at the very end)
eval "$(starship init zsh)"
```

## Verification

After setup, verify everything works:

```bash
# Reload shell configuration
source ~/.zshrc

# Test autosuggestions (type a partial command and see suggestions)
# Test syntax highlighting (commands should be colored)
# Test Starship prompt (should see a styled prompt)
```

## Troubleshooting

1. **Slow shell startup**: Comment out unused plugins and features
2. **Autosuggestions not working**: Ensure the plugin is properly cloned and
   sourced
3. **Starship not showing**: Make sure it's the last line in `.zshrc`
4. **Terminal title not updating**: Check if `DISABLE_AUTO_TITLE="true"` is set

## Additional Resources

- [Oh My Zsh Documentation](https://github.com/ohmyzsh/ohmyzsh/wiki)
- [Starship Documentation](https://starship.rs/config/)
- [Zsh Autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [Atuin Documentation](https://github.com/atuinsh/atuin)