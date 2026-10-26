# 发布版本流程

默认使用脚本化入口：

```bash
make release VERSION=X.Y.Z
```

这个命令会执行：

1. 检查 git worktree 必须干净
2. 检查本地 tag `vX.Y.Z` 不存在
3. 更新 `pyproject.toml` 中的 `version`
4. 执行本地校验
   - `uv build`
   - `uvx twine check dist/*`
5. 提交版本变更
   ```bash
   git commit -m "release: vX.Y.Z"
   ```
6. 创建本地 tag
   ```bash
   git tag vX.Y.Z
   ```

注意：`make release` 默认只做到本地 `commit + tag`，不会自动 push。

完成后手动执行：

```bash
git push && git push --tags
```

推送 `v*` tag 会自动触发 CI (`.github/workflows/publish.yml`)，执行：

- `uv build` 构建
- 发布到 PyPI
- 创建 GitHub Release

如果 tag 打错位置，可以手动修正：

```bash
git tag -d vX.Y.Z
git tag vX.Y.Z HEAD
git push origin vX.Y.Z --force
```
