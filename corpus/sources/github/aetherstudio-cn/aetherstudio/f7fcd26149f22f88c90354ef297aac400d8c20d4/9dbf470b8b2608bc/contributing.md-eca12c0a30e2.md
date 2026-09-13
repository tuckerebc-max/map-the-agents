# 代码提交规范

本文档总结本仓库的代码提交流程、检查清单与常见问题处理方案，供每次提交前参考。仓库成员与外部贡献者均可按此流程提交代码。

---

## 1. 外部贡献者 Fork 流程

如果你没有本仓库的直接写入权限，请通过 Fork 方式提交 Pull Request。

### 1.1 Fork 仓库

1. 打开仓库首页：[https://github.com/songdiyang/AetherStudio](https://github.com/songdiyang/AetherStudio)
2. 点击右上角 **Fork** 按钮，将仓库复制到你的 GitHub 账号下
3. 等待 Fork 完成后，进入你自己的 Fork 仓库页面

### 1.2 克隆你的 Fork

```powershell
git clone https://github.com/<你的用户名>/AetherStudio.git
cd AetherStudio
```

### 1.3 添加上游仓库

```powershell
git remote add upstream https://github.com/songdiyang/AetherStudio.git
git fetch upstream
```

### 1.4 同步上游最新代码

每次开发前，先将上游 `dev` 分支同步到你的 Fork：

```powershell
git checkout dev
git pull upstream dev
git push origin dev
```

### 1.5 创建功能分支

```powershell
git checkout -b temp/<简短描述>
```

### 1.6 提交并推送

```powershell
# ... 修改代码 ...
cargo fmt --all -- --check
cargo check -p aether-win32
cargo test --workspace --lib --no-fail-fast
git add -A
git commit -m "<type>(<scope>): <description>"
git push -u origin temp/<简短描述>
```

### 1.7 创建跨仓库 PR

1. 打开你的 Fork 仓库页面
2. 点击 **Compare & pull request**
3. 在创建页面选择：
   - **base repository**: `songdiyang/AetherStudio`
   - **base**: `dev`
   - **head repository**: `<你的用户名>/AetherStudio`
   - **compare**: `temp/<简短描述>`
4. 填写标题和描述，点击 **Create pull request**

### 1.8 保持 PR 更新

如果上游 `dev` 在你提交 PR 后又推进了代码，可能需要同步：

```powershell
git fetch upstream
git checkout temp/<简短描述>
git rebase upstream/dev
# 如有冲突则解决，然后强制推送
git push -f origin temp/<简短描述>
```

---

## 2. 仓库成员分支规范

| 场景 | 操作 |
|---|---|
| 日常开发 | 从 `dev` 切出临时分支：`git checkout -b temp/<简短描述>` |
| 修复 bug | 从 `dev` 切出分支：`git checkout -b fix/<问题描述>` |
| 提交目标 | **PR 必须合并到 `dev`**，不要直接合并到 `main` |
| 临时分支清理 | PR 合并后，删除本地与远程临时分支 |

### 禁止事项
- 不要直接在 `dev` 或 `main` 上提交改动
- 不要使用包含中文或空格的 branch 名

---

## 3. 提交前检查清单

每次 `git push` 前必须执行并全部通过：

```powershell
cargo fmt --all -- --check   # 1. 代码格式检查
cargo check -p aether-win32  # 2. 编译检查
cargo test --workspace --lib --no-fail-fast  # 3. 单元测试
```

> 如果 `cargo fmt -- --check` 报错，先运行 `cargo fmt --all` 自动修复，再重新检查。

---

## 3. 提交信息规范

使用 `<type>(<scope>): <简短描述>` 格式，正文说明改动点，结尾说明验证结果。

```text
perf(win32): 优化打开文件夹性能与内存安全

- 修复 window.rs 中 Rc::from_raw 重复调用问题
- WM_DESTROY 时清理 EDITOR_STATE thread-local 引用
- 将 open_folder 改为异步扫描，避免 UI 线程阻塞
- 文件树默认折叠，仅顶层目录展开
- 渲染文件树时复用 UTF-16 缓冲区

验证：
- cargo fmt --all -- --check 通过
- cargo check -p aether-win32 通过
- cargo test --workspace --lib --no-fail-fast 通过
```

### type 说明

| type | 用途 |
|---|---|
| `feat` | 新功能 |
| `fix` | bug 修复 |
| `perf` | 性能优化 |
| `refactor` | 代码重构 |
| `style` | 格式化、代码风格 |
| `test` | 测试相关 |
| `docs` | 文档更新 |
| `chore` | 构建、依赖、工具等杂项 |

---

## 4. PR 创建流程

1. 推送临时分支到远程：
   ```powershell
   git push -u origin temp/<branch-name>
   ```
2. 在浏览器打开 compare URL：
   ```
   https://github.com/songdiyang/AetherStudio/compare/dev...temp/<branch-name>
   ```
3. 确认：
   - **base** = `dev`
   - **compare** = `temp/<branch-name>`
4. 填写标题和描述，点击 **Create pull request**

---

## 6. CI 失败处理

### 5.1 Check formatting 失败

表现：GitHub Actions 显示 `Check formatting` 步骤红叉，diff 中显示缩进或换行问题。

处理：

```powershell
cargo fmt --all
git add -A
git commit -m "style(fmt): run cargo fmt"
git push -f origin temp/<branch-name>
```

### 5.2 cargo check 失败

- 查看 CI 日志中的具体错误文件和行号
- 本地执行 `cargo check -p aether-win32` 复现
- 修复后重新提交并推送

### 5.3 cargo test 失败

- 本地执行 `cargo test --workspace --lib --no-fail-fast`
- 针对性修复失败用例
- 不要跳过测试直接推送

---

## 6. 合并冲突处理

如果 PR 页面提示 `This branch has conflicts that must be resolved`：

1. 中止当前合并（如正在进行）：
   ```powershell
   git merge --abort
   ```
2. 拉取最新 dev：
   ```powershell
   git checkout dev
   git pull origin dev
   ```
3. 切回临时分支并变基或合并：
   ```powershell
   git checkout temp/<branch-name>
   git rebase dev
   # 或
   git merge dev
   ```
4. 手动解决冲突，确保保留 dev 新增功能
5. 冲突解决后执行完整检查清单
6. 强制推送：
   ```powershell
   git push -f origin temp/<branch-name>
   ```

> 如果冲突复杂，可以考虑放弃旧分支，基于最新 dev 重新切出 `temp/<branch-name>-v2` 并重新应用改动。

---

## 8. 网络问题处理

远程仓库地址：`https://github.com/songdiyang/Aether-Editor.git`（已重定向到 `AetherStudio`）。

如果推送失败：

- 检查 GitHub 连接：`Test-NetConnection -ComputerName github.com -Port 443`
- 连接失败时尝试 VPN 或代理
- 配置代理示例：
  ```powershell
  git config http.proxy http://127.0.0.1:7890
  git config https.proxy http://127.0.0.1:7890
  ```
- 网络恢复后重新 `git push`

---

## 8. 提交后清理

PR 合并后：

```powershell
git checkout dev
git pull origin dev
git branch -D temp/<branch-name>
git push origin --delete temp/<branch-name>
```

---

## 10. 快速参考

```powershell
# 完整提交流程
git checkout dev
git pull origin dev
git checkout -b temp/<branch-name>
# ... 修改代码 ...
cargo fmt --all -- --check
cargo check -p aether-win32
cargo test --workspace --lib --no-fail-fast
git add -A
git commit -m "<type>(<scope>): <description>"
git push -u origin temp/<branch-name>
# 然后去 GitHub 创建 PR：https://github.com/songdiyang/AetherStudio/compare/dev...temp/<branch-name>
```
