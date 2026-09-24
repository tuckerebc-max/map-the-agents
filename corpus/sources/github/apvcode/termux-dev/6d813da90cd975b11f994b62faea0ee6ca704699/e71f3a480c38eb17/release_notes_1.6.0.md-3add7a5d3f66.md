# devx v1.6.0

## English

- A clean, compact terminal interface is now the default on Linux, Termux, macOS, and Windows. The original interface remains available through `/settings` → `Interface`.
- The status line and command palette fit narrow terminals, including 28-column Termux screens. Long model names are shortened to the available width.
- `/clear` now clears the screen without deleting conversation history. Banner preferences are preserved when the interface redraws.
- Headless runs (`devx -p`) now initialize and close configured MCP servers, making their tools available to the agent.
- The CLI and package metadata are updated to v1.6.0. Build and 55 tests pass.

Install or update with `npm install -g termux-dev@1.6.0`.

## Русский

- На ПК и в Termux по умолчанию используется единый компактный интерфейс. Прежний вид доступен через `/settings` → `Interface`.
- Статус и меню команд помещаются в узком терминале, включая экран Termux шириной 28 колонок. Длинные названия моделей сокращаются по ширине.
- `/clear` очищает экран, сохраняя историю диалога. Выбранный баннер сохраняется при перерисовке.
- В режиме `devx -p` теперь запускаются и корректно закрываются настроенные MCP-серверы.
- Версия CLI и npm-пакета обновлена до v1.6.0; сборка и 55 тестов проходят.

Установка и обновление: `npm install -g termux-dev@1.6.0`.
