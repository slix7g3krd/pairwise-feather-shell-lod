# pairwise-feather-shell-lod

## 领域

游戏、图形与多媒体

## 主题

羽毛壳层透射与风动

## 说明

世界空间层距、透射相位函数、风相位持久化。

初始状态下 `graphics/feather_shell.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
