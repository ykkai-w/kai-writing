"""
常驻指令字符数卡口，对应任务书 8.8。

用法：
    python check_budget.py <常驻指令文件> [--quota 6000] [--slice 切片文件]

常驻指令设死定额（实测上限的八成，留粘贴余量）。超额不许发版，
否则第二轮起必然溢出，手工临时砍会让 skill 在轮次间来回震荡。
"""
import sys
from pathlib import Path


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print('用法: python check_budget.py <常驻指令文件> [--quota 6000] [--slice 切片文件]')
        sys.exit(2)

    quota = 6000
    if '--quota' in sys.argv:
        quota = int(sys.argv[sys.argv.index('--quota') + 1])

    core = Path(args[0]).read_text(encoding='utf-8')
    n = len(core)
    print(f'常驻指令 {n} 字符 / 定额 {quota}（{n / quota:.0%}）')

    total = n
    if '--slice' in sys.argv:
        sl = Path(sys.argv[sys.argv.index('--slice') + 1])
        m = len(sl.read_text(encoding='utf-8'))
        total = n + m
        print(f'章节切片 {m} 字符，部署包合计 {total} 字符')

    if n > quota:
        print(f'[FAIL] 超额 {n - quota} 字符，不许发版。'
              f'按换入换出对削减：每提一条新规则必须指名替换掉哪一条。')
        sys.exit(1)
    print('[PASS] 未超额')


if __name__ == '__main__':
    main()
