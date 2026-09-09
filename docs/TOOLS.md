# 工具说明

五个 Python 脚本随写作规范提供，日常润色主要使用正文检查和修改记录核验，其余工具服务于开发过程。运行前先进入仓库目录。以下命令中的稿件和记录文件由操作者准备，不是仓库附带的数据。

## 正文检查与编号

先从模型回复中提取正式正文。不要把过程说明、代码围栏、书目目录和原样引用混进正文检查。

```sh
python3 tools/check_kaiwriting.py manuscript.txt
python3 tools/number_paragraphs.py manuscript.txt --out manuscript.numbered.txt
```

`check_kaiwriting.py` 的 `--fix` 会改写输入文件，仅在已有副本并检查修改范围后使用。编号工具产生供段落对照使用的 `[Pxxx]` 标签，不要求把这些标签留在发表正文中。

## 核对修改记录

偏离表为 JSONL，每个终稿段落对应一行。模式编号按当前所选章节使用，登记表包含在 `SKILL.md` 中。

```sh
python3 tools/check_revision_table.py revisions.jsonl manuscript.numbered.txt --registry SKILL.md
```

通过检查表示记录满足相应字面规则，不表示改稿已经通过事实核对或写作质量评估。事实核对仍需逐句回看研究材料。

## 开发辅助

`aggregate_diffs.py` 汇总结构化差异，`check_budget.py` 计算待部署指令的字符预算。它们需要各自的输入记录和配置，不属于普通润色的必经步骤。具体参数可查看脚本中的用法说明，字符定额由实际部署环境决定。
