# vendor 补丁记录

vendor 目录的文件是从 node_modules 手工拷出来的。重拷/升级前先看这里，否则补丁会被静默覆盖。

**当前状态（2026-07）：无在役补丁。** vendor/xterm 已升级到 @xterm/xterm 6.0.0 + addon-webgl 0.19.0 + addon-fit 0.11.0（为修 WebGL 字形图集致中文乱码），下面的 CapsLock 补丁已被上游 6.0.0 原生包含，按退场条件删除了补丁、文件头注释和 `check:vendor-patch`/`predist` 守卫。

## 【已退役】public/vendor/xterm/xterm.js — CapsLock 输入法双写修复

- **症状**：中文输入法 composition 进行中（如连打拼音 yaoda 未选字）按 CapsLock 切中英，落下「yao dayaoda」双写。
- **根因**：xterm 5.5.0 的 CompositionHelper.keydown 豁免名单只有 229 和 16/17/18，CapsLock(20) 会立即 finalizeComposition(false) 把候选框文本「yao da」当数据发出，随后输入法又正常提交「yaoda」。
- **补丁来源**：上游 xtermjs/xterm.js PR #5282（commit 0433fb8a4b，"Fixed CapsLock triggering input twice in MacOS."），已进 master / 5.6.0-beta，未进任何 stable。
- **改动**（minified 单行内查找替换，另在文件头加了 `FANBOX-PATCH` 注释）：
  - 查找：`if(229===e.keyCode)return!1;`（位于 `keydown(e){if(this._isComposing||this._isSendingComposition){` 之后）
  - 替换：`if(20===e.keyCode||229===e.keyCode)return!1;`
- **守卫**：package.json `check:vendor-patch`（predist 自动跑），补丁丢失时出包直接失败。
- **退场条件**：@xterm/xterm 发布 ≥5.6.0 stable 并升级重拷 vendor 后，删除本补丁、文件头注释和守卫脚本。注意文件头注释让 minified 代码下移一行——若日后给 vendor 配 `.map`，需同步删注释或重新生成 map，否则行号映射整体错一行。
- **未修的同类边界**：Meta/Cmd（91/92/93）在 composition 中同样会触发提前提交（上游也没修），频率远低于 CapsLock，暂不偏离上游。
