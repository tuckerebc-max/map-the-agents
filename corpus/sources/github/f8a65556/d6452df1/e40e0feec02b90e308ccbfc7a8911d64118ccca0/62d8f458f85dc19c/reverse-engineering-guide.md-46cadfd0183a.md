# Claude Code 逆向工程参考指南

本指南提供从 Claude Code npm 包中提取和分析信息的系统化方法，适用于版本追踪和技术分析。

## 一、获取新版本

### 1.1 下载 tarball

```bash
# 从 npm registry 下载指定版本
npm pack @anthropic-ai/claude-code@2.1.91

# 下载最新版本
npm pack @anthropic-ai/claude-code

# 查看可用版本
npm view @anthropic-ai/claude-code versions --json | tail -20
```

### 1.2 tarball 结构

```
package/
├── cli.js              # 主 bundle（Bun 打包，~13MB）
├── cli.js.map          # Source map（v2.1.88 有，v2.1.89+ 已移除）
├── package.json        # 包元数据
├── sdk-tools.d.ts      # SDK 公开 API 类型定义
├── LICENSE.md
├── README.md
├── bun.lock            # Bun 锁文件（v2.1.88 有，v2.1.89+ 已移除）
└── vendor/             # 原生模块和工具
    ├── ripgrep/        # rg 二进制（各平台）
    ├── audio-capture/  # 音频采集 .node 模块
    ├── image-processor/# 图像处理 .node 模块
    ├── modifiers-napi/ # 键盘修饰键 .node 模块
    └── url-handler/    # URL 协议处理 .node 模块
```

### 1.3 Source Map 可用性

| 版本 | cli.js.map | 说明 |
|------|-----------|------|
| v2.1.88 | 有（57MB） | 可完整还原 4,756 个源文件 |
| v2.1.89+ | 无 | Anthropic 已移除 source map 分发 |

## 二、Source Map 路径（有 .map 文件时）

如果 tarball 中包含 `cli.js.map`，可以完整还原源码：

### 2.1 提取源码

```bash
# 解压 tarball
tar xzf anthropic-ai-claude-code-2.1.88.tgz

# 使用 source-map-explorer 可视化
npx source-map-explorer package/cli.js

# 使用 Node.js 提取所有源文件
node -e "
const fs = require('fs');
const { SourceMapConsumer } = require('source-map');

const map = JSON.parse(fs.readFileSync('package/cli.js.map', 'utf8'));
const sources = map.sources;
const contents = map.sourcesContent;

sources.forEach((src, i) => {
  if (contents[i]) {
    const outPath = 'restored-src/' + src.replace(/^\.\.\//g, '');
    fs.mkdirSync(require('path').dirname(outPath), { recursive: true });
    fs.writeFileSync(outPath, contents[i]);
  }
});
console.log('Extracted', sources.length, 'files');
"
```

### 2.2 与基线做 diff

```bash
# 使用 diff 对比两个版本的还原源码
diff -rq restored-src-v88/src/ restored-src-v91/src/ | head -50

# 使用 git 管理版本
cd restored-src && git init && git add . && git commit -m "v2.1.88"
# 覆盖新版本源码后
git diff --stat
```

## 三、无 Source Map 路径（v2.1.89+ 情况）

当 source map 不可用时，需要从 minified bundle 中提取信号。

### 3.1 可提取的信号（字符串常量挖掘）

使用 `scripts/extract-signals.sh` 自动提取：

```bash
# 提取所有信号
./scripts/extract-signals.sh package/cli.js

# 只提取 tengu 事件
./scripts/extract-signals.sh package/cli.js --section tengu

# 输出 JSON 格式
./scripts/extract-signals.sh package/cli.js --json
```

#### 信号类型详解

**1. Tengu 事件名（~860 个）**

所有遥测事件使用 `tengu_` 前缀。事件名直接反映功能模块：

```
tengu_api_query        → API 调用
tengu_compact          → 压缩系统
tengu_mcp_*            → MCP 协议
tengu_tool_use_*       → 工具执行
tengu_powerup_*        → 新功能（v2.1.91 新增）
```

变化含义：
- **新增事件** → 新功能或新追踪点
- **移除事件** → 功能废弃或重构
- **带实验代码名的事件**（如 `tengu_birch_trellis`）→ A/B 测试

**2. CLAUDE_CODE_* 环境变量（~180 个）**

环境变量控制运行时行为：

```
CLAUDE_CODE_AUTO_COMPACT_WINDOW  → 自动压缩窗口大小
CLAUDE_CODE_API_BASE_URL         → API 基础 URL
CLAUDE_CODE_BRIEF                → 简洁模式
CLAUDE_CODE_AGENT_COST_STEER     → 代理成本控制（v2.1.91 新增）
```

**3. GrowthBook 配置名（~17 个）**

Feature flag 和实验配置：

```
tengu_auto_mode_config           → YOLO 自动模式
tengu_prompt_cache_1h_config     → 1 小时缓存
tengu_sm_compact_config          → 会话内存压缩
```

**4. 工具名**

从工具注册代码中提取：Bash, Read, Write, Edit, Glob, Grep, Agent, Skill, ...

**5. API 端点路径**

```
/v1/messages                     → Claude API
/api/event_logging/batch         → 遥测事件导出
/api/oauth/usage                 → 使用量查询
/api/oauth/profile               → OAuth 用户资料
```

### 3.2 结构化差异分析

使用 `scripts/cc-version-diff.sh` 进行版本间对比：

```bash
# 两版本对比
./scripts/cc-version-diff.sh old.tgz new.tgz

# 与 v2.1.88 基线对比（单参数模式）
./scripts/cc-version-diff.sh new.tgz

# 输出到文件
./scripts/cc-version-diff.sh old.tgz new.tgz -o docs/version-diffs/report.md
```

报告包含：
- cli.js 大小变化
- Tengu 事件增删
- 环境变量增删
- GrowthBook 配置变化
- 包文件变化
- sdk-tools.d.ts 差异（公开 API 变化）
- package.json 差异

### 3.3 语义级分析方法

当需要更深入的分析时，可以手动搜索已知模式：

```bash
# 搜索 logEvent 调用附近的上下文
grep -b 'tengu_powerup' cli.js | head

# 搜索环境变量引用
grep -oE 'CLAUDE_CODE_[A-Z_]+' cli.js | sort -u

# 搜索 API 端点
grep -oE '"/v[0-9]/[a-z_/]+"' cli.js | sort -u

# 搜索版本信息
grep -oE '"version":"[0-9]+\.[0-9]+\.[0-9]+"' cli.js

# 搜索 feature() 调用（注意：Bun DCE 可能已消除）
grep -c 'feature(' cli.js  # 如果为 0，说明已被 DCE 消除

# 搜索唯一错误类名
grep -oE '[A-Z][a-zA-Z]+Error' cli.js | sort -u | head -20
```

## 四、锚点文件索引

详见 [anchor-points.md](./anchor-points.md) — 从 v2.1.88 源码中提取的 120+ 个子系统锚点。

锚点是在 minified bundle 中定位特定子系统的关键。每个锚点是一个唯一的字符串常量，在不同版本中通常保持一致。

示例使用：

```bash
# 确认 API 重试逻辑是否仍存在
grep -c 'tengu_api_retry' cli.js

# 检查 YOLO 分类器是否仍在使用
grep -c 'classify_result' cli.js

# 检查 Datadog 集成
grep -c 'datadoghq.com' cli.js

# 检查压缩阈值是否改变
grep -oE 'AUTOCOMPACT_BUFFER[^,}]+' cli.js
```

## 五、版本间差异速查

### v2.1.88 → v2.1.91 变化要点

| 指标 | v2.1.88 | v2.1.91 | 变化 |
|------|---------|---------|------|
| cli.js 大小 | 12.4MB | 12.5MB | +115KB |
| Source Map | 有 | 无 | 已移除 |
| Tengu 事件 | 827 | 860 | +39 / -6 |
| 环境变量 | 178 | 183 | +8 / -3 |
| GrowthBook 配置 | 17 | 18 | +1 |

**关键新增功能信号（v2.1.91）**：
- `tengu_powerup_lesson_*` — 学习/教程系统
- `tengu_cold_compact` — 冷压缩（新压缩策略）
- `tengu_memory_toggled` — 内存开关
- `tengu_message_rated` — 消息评分
- `tengu_ultraplan_*` — 超级计划功能
- `tengu_mcp_subagent_prompt` — MCP 子代理提示

**移除的功能信号**：
- `tengu_tree_sitter_*` — Tree-sitter 相关（已移除或重构）
- `tengu_basalt_` / `tengu_birch_trellis` — 实验结束

详细报告见 [version-diffs/v2.1.88-vs-v2.1.91.md](./version-diffs/v2.1.88-vs-v2.1.91.md)。

## 六、工作流建议

### 追踪新版本的标准流程

```
1. npm pack @anthropic-ai/claude-code@<新版本>
2. ./scripts/cc-version-diff.sh claude-code-<旧>.tgz claude-code-<新>.tgz -o docs/version-diffs/<旧>-vs-<新>.md
3. 审查差异报告，重点关注：
   a. 新增 tengu 事件 → 识别新功能
   b. 移除 tengu 事件 → 识别废弃功能
   c. 新增环境变量 → 识别新配置选项
   d. sdk-tools.d.ts 变化 → 识别公开 API 变化
4. 如需深入分析特定子系统，使用锚点在 cli.js 中定位
5. 将分析结果记录到 docs/version-diffs/ 目录
```

### 持续追踪建议

- 保留每个版本的 tarball 作为基线
- 维护 `docs/version-diffs/` 目录下的差异报告
- 当发现新的稳定锚点时，更新 `docs/anchor-points.md`
- 关注 `sdk-tools.d.ts` 的变化——这是唯一的官方公开 API 定义

---

*本指南基于 Claude Code v2.1.88（含 source map）的逆向工程经验编写*
