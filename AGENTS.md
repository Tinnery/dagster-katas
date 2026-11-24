# dagster-katas — Agent 工作规则

本仓库是 Dagster 学习练习的集合，每个练习聚焦一个概念，可独立运行和验证。

## 公共仓库文档禁令（硬约束）

本仓库是 public repo，以下规则优先于任何"按需写文档"的冲动：

1. **禁止文档目录**：不得新建或保留 `docs/`、`doc/`、`documentation/`、`deliverables/`、`reports/`、`notes/`、`decisions/`、`history/` 等文档或过程目录。
2. **禁止生成文字材料**：学习指南、练习说明、API 文档、报告、评审记录、笔记等文字文件（`.md` / `.rst` / `.pdf` / `.docx` 等）不得在本仓库生成或提交。机器验证的临时输出只能写入被忽略的 `.runtime/`，不作为文档维护。
3. **README.md 只做入口**：仅保留标题与一句话定位。`AGENTS.md` 只放规则与路由。
4. **文字材料唯一归属**：所有文字材料必须维护在私有仓库 `nooshare-design` 的 `implementation-docs/dagster-katas/` 下；本仓库只引用，不复制。
5. **违规处理**：发现本仓库出现上述目录或文字材料，不就地修订——先迁移到 nooshare-design，再删除本地文件，并更新下方索引表。

### 文字材料索引（nooshare-design）

| 材料 | 权威位置（nooshare-design） |
|------|------------------------------|
| 练习说明与学习指南 | `implementation-docs/dagster-katas/exercises/` |
| 概念解释与笔记 | `implementation-docs/dagster-katas/notes/` |
| README 原文归档 | `implementation-docs/dagster-katas/README-full.md` |

通过 `workspace.yaml` 定位 nooshare-design 的 checkout 路径后读取上述文件。

## Matrix Authority

- **nooshare-design**：系统角色与跨仓逻辑职责（architecture/matrix.md）。
- **nooshare-noos**：适用的已验证知识与工程 invariant。
- **nooshare-workenv**：工作区、主机、部署与操作授权（AGENTS.md、workspace.yaml）。

## Context Bootstrap

任务涉及以下情形时，向上索引对应权威：

| 触发条件 | 索引目标 | 读什么 |
|----------|----------|--------|
| 系统角色 / 跨仓职责变更 | nooshare-design | `architecture/matrix.md` |
| 工程 invariant / 已验证知识 | nooshare-noos | 相关 domain 文件 |
| 主机 / 部署 / 操作授权变更 | nooshare-workenv | `AGENTS.md` + `workspace.yaml` |

索引路径：通过 `workspace.yaml` 找到目标 Repo 的 checkout 路径，读取对应文件。

## Local Ownership

本仓库拥有：

- Python 练习代码（每个练习独立目录）
- 练习运行脚本和验证逻辑
- 测试（`tests/`）
- 依赖配置（`pyproject.toml`、`uv.lock`）

上游权威不替代这些本地契约。与权威要求冲突时，向拥有该问题的权威反馈，不在本地悄悄改写权威定义。

## Development

```bash
# 安装依赖
uv sync --locked

# 运行练习
uv run hello.py

# 运行测试
uv run pytest
```

## 结构纪律

- 每个练习独立成目录，包含自己的代码和验证逻辑
- 禁止预建 `core/`、`utils/`、`scripts/` 等额外目录，除非有真实业务边界
- 练习代码保持自包含，不引入不必要的抽象
- 测试必须可独立运行，不依赖外部服务
