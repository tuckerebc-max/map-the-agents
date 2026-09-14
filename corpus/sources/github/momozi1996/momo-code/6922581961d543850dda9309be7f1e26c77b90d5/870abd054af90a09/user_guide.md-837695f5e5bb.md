# MOMO CODE 终端操作指南

> 面向初学用户 — 从零开始在终端使用 momo-code

---

## 一、安装

### 1. 克隆仓库
```bash
cd ~
git clone https://github.com/momozi1996/momo-code.git
```

### 2. 安装依赖并构建
```bash
cd momo-code/packages/opencode
npm install
npm run build
```

### 3. 验证安装
```bash
node bin/momo --version
```
输出 `1.0.0` 即安装成功。

---

## 二、配置 API Key

momo-code 需要 AI 模型的 API Key 才能工作。**（必填）**

### 方式 1：通用 Key（推荐）
```bash
export MOMO_API_KEY=sk-你的API密钥
```

### 方式 2：指定服务商
```bash
export MOMO_OPENAI_API_KEY=sk-你的OpenAI密钥
export MOMO_ANTHROPIC_API_KEY=sk-ant-你的Anthropic密钥
export MOMO_MINIMAX_API_KEY=sk-你的MiniMax密钥
```

### 支持的 AI 服务商
| 服务商 | 环境变量 |
|--------|---------|
| OpenAI | `MOMO_OPENAI_API_KEY` |
| Anthropic (Claude) | `MOMO_ANTHROPIC_API_KEY` |
| Google (Gemini) | `MOMO_GOOGLE_API_KEY` |
| MiniMax | `MOMO_MINIMAX_API_KEY` |
| Moonshot (Kimi) | `MOMO_MOONSHOT_API_KEY` |
| Zhipu (GLM) | `MOMO_ZHIPU_API_KEY` |
| DeepSeek | `MOMO_DEEPSEEK_API_KEY` |
| 其他 OpenAI 兼容 | `MOMO_API_KEY` |

### 指定服务商
```bash
export MOMO_PROVIDER=openai       # 用 OpenAI
export MOMO_PROVIDER=anthropic    # 用 Claude
export MOMO_PROVIDER=minimax      # 用 MiniMax
export MOMO_PROVIDER=openrouter   # 用 OpenRouter
```

### 指定模型 / Tier
```bash
export MOMO_MODEL=ultra      # Claude Sonnet 4
export MOMO_MODEL=standard   # GPT-4.1
export MOMO_MODEL=lite       # GPT-4.1-mini
```

### 让配置永久生效
编辑 `~/.zshrc`（或 `~/.bashrc`）：
```bash
# momo-code 配置
export MOMO_API_KEY=sk-你的API密钥
export MOMO_PROVIDER=openai
export MOMO_MODEL=standard
```

---

## 三、基础命令

### 查看帮助
```bash
node bin/momo
```
或
```bash
node bin/momo --help
```
显示 MOMO CODE 的 Banner 和所有可用命令。

---

### 单轮对话（最基本的用法）
```bash
node bin/momo "写一个 Python 函数，计算斐波那契数列"
```
输出：AI 的回复（流式输出，逐字显示）

```bash
node bin/momo "解释一下 React useEffect 的用法"
```

> **注意**：这是单轮对话，没有上下文记忆。每次发送都是独立请求。

---

## 四、进阶命令

### 切换 AI 服务商或模型

**用环境变量**：
```bash
MOMO_PROVIDER=anthropic node bin/momo "写一个 TypeScript 接口"
MOMO_MODEL=ultra node bin/momo "设计一个分布式系统架构"
```

**或同时指定**：
```bash
MOMO_PROVIDER=openai MOMO_MODEL=standard node bin/momo "修复这个 bug"
```

---

## 五、经验进化系统（/evolve）

这是 momo-code 的独特功能：通过运行 `/evolve`，它会从你的使用经验中**自动学习策略**，并在下次对话时**自动注入**到 AI 的指令中，让它更擅长你的编码风格。

### 5.1 生成示例经验
```bash
node bin/momo /evolve --demo
```
用 9 条模拟信号生成初始经验，适合第一次体验。

**输出示例**：
```
🧬 momo Experience Evolution
  Tactics: 2  Promoted: 0  Verdict: ~
  Storage: ~/.momo/experience/
```

---

### 5.2 查看学到的策略
```bash
node bin/momo /evolve --list
```

**输出示例**：
```
📚 Learned Tactics

  DRAFT (1)
    ✎ tac_global_dd04ac2f  Apply accepted edits with verification
       winRate=0.750  α=3 β=1  uses=2

  ACTIVE (1)
    ✓ tac_global_d57a5d64  Ensure tests pass after bash changes
       winRate=0.857  α=6 β=1  uses=5
```

| 状态 | 含义 |
|------|------|
| `DRAFT` | 草稿策略，还在观察期 |
| `ACTIVE` | 已激活策略，会在对话中自动注入 |

---

### 5.3 测试策略注入
```bash
node bin/momo /evolve --inject "Run tests after making changes"
```
查看哪些 ACTIVE 策略会被注入到对话中。

---

### 5.4 从当前项目自动学习（真正执行测试）
```bash
# 先进入你的项目目录
cd /path/to/your/project

# 然后运行（会自动执行 npm test 和 tsc 类型检查）
node /path/to/momo-code/packages/opencode/bin/momo /evolve --auto
```

这会：
1. 执行 `npm test` → 根据结果记录 pass/fail
2. 执行 `npx tsc --noEmit` → 检查类型错误
3. 自动学习并更新策略

---

### 5.5 手动添加信号
```bash
node bin/momo /evolve --solidify tac_global_d57a5d64 pass
```
手动确认某个策略是好的（`pass`）或坏的（`fail`）。

---

## 六、策略优化（/fine-tune）

对 `/evolve` 学到的策略进行统计优化和状态提升。

### 6.1 诊断当前状态
```bash
node bin/momo /fine-tune
```

**输出示例**：
```
🔬 /fine-tune Diagnosis
  Tactics: 2 total
    draft: 2  active: 0  promoted: 0  retired: 0
  Ledger:  1 entries

  💡 Need more tactics. Run: momo /evolve --demo
```

---

### 6.2 执行策略优化
```bash
node bin/momo /fine-tune run
```

**输出示例**：
```
🏋️ /fine-tune Training
  Run ID: run_xxxxxx

  Step 1/5: 📚 Curriculum
    Gold: 0  Replay: 1  Hard-negative: 0
  Step 2/5: 🧪 Baseline Eval
    pass@1: 75.0%
  Step 3/5: ⚡ Train (Priors)
    1 status transition(s)
  Step 5/5: 🔒 Ratchet Gate
    Δ = +0.0%  regressions: 0

  ✓ Ratchet PASS — candidate staged
```

---

### 6.3 查看运行记录
```bash
node bin/momo /fine-tune status
```

**输出示例**：
```
📊 /fine-tune Status
  run_xxxxxx  🟡 staged  7/4/2026
```

---

### 6.4 提升策略（将 candidate 转为正式）
```bash
node bin/momo /fine-tune promote run_xxxxxx
```
把优化后的候选策略提升为正式策略。

**输出**：
```
✅ Promoted run_xxxxxx → tactics.json
```

---

## 七、查看模型列表

### 列出所有可用的 AI 模型
```bash
node bin/momo models list
```

**输出示例**：
```
Available Models
================

Built-in Tiers:
  Ultra:    claude-sonnet-4, gpt-5, gemini-2.5-pro
  Standard: claude-sonnet-4, gpt-4.1, gemini-2.5-flash
  Lite:     claude-haiku, gpt-4.1-mini, gemini-2.5-flash-lite
```

---

## 八、完整工作流示例

### 日常编码工作流
```bash
# 1. 配置 API
export MOMO_API_KEY=sk-你的密钥
export MOMO_MODEL=standard

# 2. 先运行 evolve 学习
node bin/momo /evolve --demo

# 3. 正常编码对话
node bin/momo "帮我写一个 Express.js 的中间件"

# 4. 从项目自动学习（进入你的项目目录后）
cd my-project
node ~/momo-code/packages/opencode/bin/momo /evolve --auto

# 5. 优化策略
node ~/momo-code/packages/opencode/bin/momo /fine-tune run

# 6. 查看状态并提升
node ~/momo-code/packages/opencode/bin/momo /fine-tune status
node ~/momo-code/packages/opencode/bin/momo /fine-tune promote run_xxxxxx

# 7. 继续对话，此时学到的策略会自动注入
node bin/momo "再帮我优化一下那个中间件"
```

---

## 九、文件存储位置

momo-code 在你的电脑上存储以下文件：

```
~/.momo/
├── momo.jsonc              # 配置文件
├── experience/
│   ├── tactics.json        # 学到的策略
│   └── ledger.jsonl        # 操作日志
├── sessions/               # 会话记录
├── finetune/
│   └── runs/               # 训练记录
└── prompts/                # 自定义系统提示
```

---

## 十、常见问题

### Q: 提示 "No API key configured"
```bash
export MOMO_API_KEY=sk-你的密钥
```

### Q: 提示 "Build output not found"
```bash
cd packages/opencode
npm run build
```

### Q: `/evolve --auto` 运行测试很慢
这是正常的，它在真正执行 `npm test` 和类型检查。可以设置超时：
```bash
# 测试简单项目，缩短超时
# 目前默认 120 秒，暂不支持自定义
```

### Q: 怎么知道 tactic 是否被注入了？
运行对话时，如果 `~/.momo/experience/tactics.json` 中有 `ACTIVE` 状态的策略，它们会自动注入到 system prompt 中。你可以用 `/evolve --inject` 测试哪些策略会被选中。

---

*文档版本: v1.0.0 | 适用于 momo-code main 分支*
