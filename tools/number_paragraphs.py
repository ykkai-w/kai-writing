"""
段落编号预处理，对应任务书 4.3。

用法：
    python number_paragraphs.py <输入文件> [--out 输出文件]

把正文按空行切成段落，逐段打上 [P001] 形式的编号。
A 与 C 的批处理、偏离表的逐段全覆盖核验都依赖这套编号。
"""
import sys
from pathlib import Path


def split_paragraphs(text):
    blocks, buf, in_fence = [], [], False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            buf.append(line)
            continue
        if not line.strip() and not in_fence:
            if buf:
                blocks.append('\n'.join(buf).strip())
                buf = []
        else:
            buf.append(line)
    if buf:
        blocks.append('\n'.join(buf).strip())
    return [b for b in blocks if b]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print('用法: python number_paragraphs.py <输入文件> [--out 输出文件]')
        sys.exit(2)
    src = Path(args[0])
    paras = split_paragraphs(src.read_text(encoding='utf-8'))
    out_lines = [f'[P{i:03d}] {p}' for i, p in enumerate(paras, 1)]
    result = '\n\n'.join(out_lines)

    if '--out' in sys.argv:
        dst = Path(sys.argv[sys.argv.index('--out') + 1])
        dst.write_text(result, encoding='utf-8')
        print(f'已编号 {len(paras)} 段，写入 {dst}')
    else:
        print(result)


if __name__ == '__main__':
    main()
