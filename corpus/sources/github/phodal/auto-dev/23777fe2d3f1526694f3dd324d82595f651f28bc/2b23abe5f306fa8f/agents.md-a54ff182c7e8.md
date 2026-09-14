## Core Rules

- **Kotlin Multiplatform**: Always consider all platforms: JS, WASM, Desktop JVM, Android, iOS
- **Build & Test**: Always run build and tests before completing tasks
- **Preserve Intent**: If an existing solution doesn't work, preserve its intent
- **Module Clean**: Use `./gradlew :xxx:clean` instead of global clean, avoid polluting global caches.
- **Test Scripts**: Put temporary scripts under `docs/test-scripts`
- **Logs**: Check `~/.autodev/logs/autodev-app.log` for debugging
- Code comments should be in English, for documentation and user-facing strings should be followed user's langauge 

## KMP Best Practices

- Use `expect`/`actual` for platform-specific code, for example `Platform`
- Avoid emoji and UTF-8 in source code which **WASM** doesn't support
- **@JsExport**: Use concrete classes (not interfaces), `Promise` (not `Flow`)
- **i18n**: Run `./gradlew :mpp-ui:generateI18n4kFiles`

## Renderer System

When modifying `CodingAgentRenderer`, update ALL implementations:
- **Kotlin**: `DefaultCodingAgentRenderer`, `ComposeRenderer`, `JewelRenderer`, `ServerSideRenderer`, `JsRendererAdapter`
- **TypeScript**: `BaseRenderer.ts`, `CliRenderer.ts`, `ServerRenderer.ts`, `TuiRenderer.ts`
- **VSCode**: `mpp-vscode/src/bridge/mpp-core.ts`, `mpp-vscode/src/providers/chat-view.ts`
- **JVM CLI**: `CodingCliRenderer`, `ConsoleRenderer`

## Design System

- **CLI/TUI**: Use `semanticInk`/`semanticChalk` from `mpp-ui/src/jsMain/typescript/design-system/`
- **Compose**: Use `AutoDevColors` or `MaterialTheme.colorScheme`
- **NO hardcoded colors** - always use design tokens
- **Docs**: `docs/design-system-color.md`, `docs/design-system-compose.md`

## Quick Commands

**CLI Test:**
```bash
./gradlew :mpp-core:jsNodeProductionLibraryDistribution
cd mpp-ui && npm run build && npm run start
```

**IDEA Plugin:**

```bash
cd mpp-idea && ../gradlew compileKotlin
cd mpp-idea && ../gradlew test --tests "cc.unitmesh.devins.idea.renderer.JewelRendererTest"
cd mpp-idea && ../gradlew buildPlugin
```

**Release:**

```bash
# 1. Update version in gradle.properties
# 2. CLI: cd mpp-ui && npm publish:remote
# 3. Desktop: git tag compose-vX.X.X && git push origin compose-vX.X.X
# 4. gh release create compose-vX.X.X --draft
```

