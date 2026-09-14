# Releasing mole

Everything is derived from the tag. `git tag v0.1.0 && git push origin v0.1.0`
builds every artifact, publishes a **draft** release, updates the Homebrew tap, and
pushes `mole-research-bin` to the AUR.

The release is a draft on purpose: it is the one artifact that cannot be recalled
once somebody's installer has cached it, so it gets a human look before it exists.

```sh
make release-check          # full pipeline locally, publishes nothing
git tag v0.1.0
git push origin v0.1.0      # CI does the rest
```

## One-time setup

Four things must exist before the first tag, and three of them cannot be created
from inside this repository.

### 1. `lajosdeme/homebrew-mole`

A public GitHub repository with that exact name — Homebrew resolves
`brew install lajosdeme/mole/mole` to `github.com/lajosdeme/homebrew-mole`. It can be
empty; GoReleaser writes `Formula/mole.rb` into it.

### 2. `HOMEBREW_TAP_GITHUB_TOKEN` secret

A fine-grained PAT with **contents: write** on the tap repository only.

The default `GITHUB_TOKEN` cannot do this — it is scoped to the repository running
the workflow, and the formula lives in another one. Scope the PAT to the tap alone;
a token that can also push to `mole` would let a compromised release workflow
rewrite the source it was built from.

### 3. AUR account and `AUR_KEY` secret

Register at [aur.archlinux.org](https://aur.archlinux.org), add an SSH public key
to your account, then:

```sh
# The private half, as a repository secret named AUR_KEY.
cat ~/.ssh/aur   # paste into GitHub → Settings → Secrets → Actions
```

The `mole-research-bin` package is created on first push. The **source** package
(`mole-research`) is
maintained by hand, because a source build has nothing to verify against but the
tag:

```sh
git clone ssh://aur@aur.archlinux.org/mole.git aur-mole
cp packaging/aur/mole-research/PKGBUILD aur-mole/
cd aur-mole
# Update pkgver, then:
updpkgsums
makepkg --printsrcinfo > .SRCINFO
makepkg -si                     # build it once before publishing it
git commit -am "mole 0.1.0" && git push
```

`sha256sums` is `SKIP` in the committed PKGBUILD, which is fine for a template and
**not** fine for a published package. `updpkgsums` fills it in from the real tag
archive.

### 4. Decide about macOS signing

Unsigned binaries are what this pipeline produces. On macOS, a user who downloads
one may meet Gatekeeper — *"cannot be opened because the developer cannot be
verified"* — and have to clear the quarantine attribute by hand:

```sh
xattr -d com.apple.quarantine /usr/local/bin/mole
```

Fixing it properly needs an Apple Developer ID ($99/year), codesigning in CI, and
notarization. Until then it is worth a line in the release notes rather than
letting macOS users discover it themselves.

## What a tag produces

| artifact | consumed by |
|---|---|
| `mole_<version>_<os>_<arch>.tar.gz` | the install script, Homebrew |
| `checksums.txt` | the install script's verification step |
| `mole_<version>_<arch>.deb` / `.rpm` | Debian, Ubuntu, Fedora |
| `Formula/mole.rb` in the tap | `brew install` |
| `mole-research-bin` PKGBUILD + .SRCINFO on the AUR | `yay -S mole-research-bin` |

Both binaries ship in one archive. `mole-mcp` is useless without the daemon `mole`
provides, and a user who gets one and not the other sees a confusing failure from
their editor rather than from a command they ran.

## Checks worth running before tagging

```sh
make check                  # vet + race suite
make release-check          # every platform builds, packages, formula, PKGBUILD
./install.sh --dry-run      # the installer resolves the right archive name
```

The installer's checksum verification has negative tests worth repeating by hand
after any change to it: tamper with an archive and confirm nothing is installed.

## Versioning

Tags are `vX.Y.Z`; archives drop the `v`. The install script handles both, and
`main.version` is stamped from the tag so `mole version` and the archive name
cannot disagree.

Pre-1.0, treat the minor as breaking: the database schema migrates forward
automatically but has no down-migrations, so a downgrade across a schema change
means restoring a copy of the database.
