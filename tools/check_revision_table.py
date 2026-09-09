"""
偏离表机械核验，对应任务书 8.7。

用法：
    python check_revision_table.py <偏离表.jsonl> <终稿文件> [--registry 登记册.txt]

偏离表每行一个 JSON 对象：
    {"para": 3, "status": "改", "before": "初稿原句至少十字", "after": "改后句", "pattern": "P-012"}
    {"para": 4, "status": "无"}

核验四条：
    1. 终稿的每个段号都有对应行，段号集合完全一致；
    2. status 为改时，after 必须逐字出现在终稿中；
    3. status 为改时，before 必须不出现在终稿中（证明确实改了）；
    4. before 长度不少于十字，pattern 必须在登记册中。

任一条不满足即判定本次修订未执行，退回重跑。
"""
import json
import re
import sys
from pathlib import Path


def final_para_ids(text):
    return set(int(m) for m in re.findall(r'\[P(\d+)\]', text))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) < 2:
        print('用法: python check_revision_table.py <偏离表.jsonl> <终稿文件> [--registry 登记册.txt]')
        sys.exit(2)

    rows = []
    for ln, line in enumerate(Path(args[0]).read_text(encoding='utf-8').split('\n'), 1):
        line = line.strip()
        if not line or line.startswith('```'):
            continue
        try:
            rows.append((ln, json.loads(line)))
        except json.JSONDecodeError:
            print(f'  L{ln} [格式] 不是合法 JSON: {line[:60]}')
            sys.exit(1)

    final = Path(args[1]).read_text(encoding='utf-8')
    registry = set()
    if '--registry' in sys.argv:
        reg_path = Path(sys.argv[sys.argv.index('--registry') + 1])
        registry = set(re.findall(r'P-\d+', reg_path.read_text(encoding='utf-8')))

    problems = []
    seen = set()

    for ln, r in rows:
        pid = r.get('para')
        if pid is None:
            problems.append(f'L{ln} 缺 para 字段')
            continue
        seen.add(int(pid))
        if r.get('status') == '无':
            continue
        before, after = r.get('before', ''), r.get('after', '')
        if len(before) < 10:
            problems.append(f'P{pid} before 不足十字，无法核验')
        if after and after not in final:
            problems.append(f'P{pid} 改后句未逐字出现在终稿中，修订未落地')
        if before and before in final:
            problems.append(f'P{pid} 初稿原句仍在终稿中，实际未修改')
        if registry and r.get('pattern') not in registry:
            problems.append(f'P{pid} 模式编号 {r.get("pattern")} 不在登记册中')

    expected = final_para_ids(final)
    if expected:
        missing = expected - seen
        extra = seen - expected
        if missing:
            problems.append(f'漏报段落（未逐段全覆盖）: {sorted(missing)}')
        if extra:
            problems.append(f'表中段号在终稿不存在: {sorted(extra)}')
    else:
        print('[提示] 终稿没有 [Pxxx] 编号，跳过逐段全覆盖核验')

    if problems:
        print(f'[FAIL] 修订未通过核验，{len(problems)} 处问题：')
        for p in problems:
            print(f'  {p}')
        sys.exit(1)
    print(f'[PASS] 偏离表核验通过，共 {len(rows)} 行，其中实际修改 '
          f'{sum(1 for _, r in rows if r.get("status") != "无")} 处')


if __name__ == '__main__':
    main()
