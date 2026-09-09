"""
diff 频次聚合，对应任务书 7.1 与 7.2。

用法：
    python aggregate_diffs.py <diff目录或文件...> [--min-papers 3] [--grid]

频次一律在本地算好再喂给蒸馏员。模型在只看到片段时会编造计数，
这是全流程最大的静默降质点。

入库阈值按论文去重，不按出现次数：同一篇论文的三个章节凑三次不算数。
英文轨额外要求跨两本以上期刊。信息不对称类不计入。
"""
import json
import sys
from collections import defaultdict
from pathlib import Path


def load(paths):
    recs = []
    for p in paths:
        p = Path(p)
        files = sorted(p.glob('*.jsonl')) if p.is_dir() else [p]
        for f in files:
            for line in f.read_text(encoding='utf-8').split('\n'):
                line = line.strip()
                if not line or line.startswith('```'):
                    continue
                try:
                    recs.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return recs


def key_of(r):
    return (r.get('pattern') or r.get('essence') or r.get('差异本质') or '未命名').strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print('用法: python aggregate_diffs.py <diff目录或文件...> [--min-papers 3] [--grid]')
        sys.exit(2)

    min_papers = 3
    if '--min-papers' in sys.argv:
        min_papers = int(sys.argv[sys.argv.index('--min-papers') + 1])

    recs = load(args)
    kept = [r for r in recs if r.get('type', r.get('类型', '纯表达')) != '信息不对称']
    dropped = len(recs) - len(kept)

    buckets = defaultdict(lambda: {'papers': set(), 'journals': set(),
                                   'layers': set(), 'grids': set(), 'n': 0})
    for r in kept:
        b = buckets[key_of(r)]
        b['papers'].add(r.get('paper_id', '?'))
        b['journals'].add(r.get('journal', '?'))
        b['layers'].add(r.get('layer', r.get('层级', '?')))
        b['grids'].add(f"{r.get('lang','?')}-{r.get('section','?')}")
        b['n'] += 1

    rows = []
    for k, b in buckets.items():
        lang_en = any(g.startswith('en') for g in b['grids'])
        ok = len(b['papers']) >= min_papers and (not lang_en or len(b['journals']) >= 2)
        rows.append((len(b['papers']), b['n'], k, b, ok))
    rows.sort(reverse=True, key=lambda x: (x[0], x[1]))

    print(f'读入 {len(recs)} 条，信息不对称类剔除 {dropped} 条，剩 {len(kept)} 条')
    print(f'入库阈值：不少于 {min_papers} 篇不同论文（英文轨另需跨 2 本以上期刊）\n')
    print('== 达标，可交蒸馏 ==')
    for npapers, n, k, b, ok in rows:
        if ok:
            print(f'  [{npapers}篇/{len(b["journals"])}刊/{n}次] {"、".join(sorted(b["layers"]))} | {k[:60]}')
    print('\n== 未达标，本轮不入库 ==')
    for npapers, n, k, b, ok in rows:
        if not ok:
            print(f'  [{npapers}篇/{len(b["journals"])}刊/{n}次] {k[:60]}')

    if '--grid' in sys.argv:
        print('\n== 分格（语言×章节），供分格预聚类会话使用 ==')
        grid = defaultdict(int)
        for r in kept:
            grid[f"{r.get('lang','?')}-{r.get('section','?')}"] += 1
        for g, c in sorted(grid.items()):
            print(f'  {g}: {c} 条')


if __name__ == '__main__':
    main()
