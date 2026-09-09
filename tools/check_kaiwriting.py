"""
kaiwriting 硬规则自查脚本，学术中文加固版。

用法：
    python check_kaiwriting.py <文件路径>
    python check_kaiwriting.py <文件路径> --fix
    python check_kaiwriting.py <文件路径> --all

违规分两级。确定违例是中文字符与 ASCII 标点直接相邻这类无歧义的情形，退出码只看它。
疑似违例列在下方供人工判断，默认只显示前若干条，--all 显示全部。
--fix 只对确定违例做替换，不碰疑似。

被屏蔽的区间不参与检查：代码块、行内代码、行内公式、URL、文件路径、
纯 ASCII 内容的括号（文献引用、变量说明）、小数与千分位、英文缩写。
"""
import re
import sys
from pathlib import Path

CJK = re.compile(r'[一-鿿㐀-䶿]')
FULLWIDTH_PUNCT = '，。；：？！（）、《》""''—…'

EMOJI = re.compile(
    '['
    '\U0001F300-\U0001F9FF'
    '\U0001F600-\U0001F64F'
    '\U0001F680-\U0001F6FF'
    '\U00002600-\U000027BF'
    ']'
)

DINGBATS = '✓✗★☆►◆❖✔✘'

CHAT_PHRASES = [
    '希望这对您有帮助', '希望对您有用', '请告诉我', '如有疑问',
    '好问题', '您说得对', '完全正确', '不客气',
    '我已经为您', '请注意以下', '请确认是否',
    'Hope this helps', 'Let me know if', 'Feel free to',
]

VERSION_PATTERNS = [
    r'#\s*v\d', r'#\s*Updated\s+\d', r'#\s*CHANGELOG',
    r'#\s*Modified by', r'#\s*之前', r'#\s*改成了',
    r'#\s*试过了', r'#\s*原来是',
]

CODE_EXTS = {'.py', '.js', '.ts', '.go', '.rs', '.cpp', '.c',
             '.h', '.r', '.sh', '.rb', '.java'}

# 屏蔽区间的匹配顺序有讲究，长的先来，否则会被短的切碎。
MASK_PATTERNS = [
    r'```.*?```',
    r'~~~.*?~~~',
    r'`[^`\n]+`',
    r'\$\$.*?\$\$',
    r'(?<!\$)\$[^$\n]+\$(?!\$)',
    r'\\\(.*?\\\)',
    r'\\\[.*?\\\]',
    r'https?://\S+',
    r'\b[\w.\-]+/[\w./\-]+',                    # 路径
    r'\b\w+\.(?:py|md|json|jsonl|csv|txt|tex|xlsx|docx|pdf|ya?ml|sh|ipynb)\b',
    r'\d+(?:\.\d+)+',                            # 小数、版本号
    r'\d{1,3}(?:,\d{3})+',                       # 千分位
    r'\b(?:e\.g|i\.e|et al|cf|vs|Fig|Eq|Tab|No|Vol|pp)\.',
    r'\b[A-Za-z_][\w]*\([^)\n]*\)',              # 函数调用
]

# 纯 ASCII 内容的半角括号，内部标点不算违例（文献引用 (Smith, 2020) 是最常见的一类）。
ASCII_PAREN = re.compile(r'\([\x20-\x7E]*\)')


def build_mask(text):
    """返回与 text 等长的布尔表，True 表示该字符处于屏蔽区间。"""
    mask = [False] * len(text)
    for pat in MASK_PATTERNS:
        for m in re.finditer(pat, text, flags=re.DOTALL):
            for i in range(m.start(), m.end()):
                mask[i] = True
    # 括号本身仍要判定（中文里应改全角），只屏蔽括号内部。
    for m in ASCII_PAREN.finditer(text):
        for i in range(m.start() + 1, m.end() - 1):
            mask[i] = True
    return mask


def line_of(text, idx):
    return text.count('\n', 0, idx) + 1


def context(text, idx, span=18):
    lo = max(0, idx - span)
    hi = min(len(text), idx + span)
    return text[lo:hi].replace('\n', ' ')


def chinese_lines(text):
    """返回集合，元素是含中文字符的行号。"""
    out = set()
    for no, line in enumerate(text.split('\n'), 1):
        if CJK.search(line):
            out.add(no)
    return out


def is_cjk(ch):
    return bool(CJK.match(ch)) or ch in FULLWIDTH_PUNCT


PUNCT_MAP = {',': '，', '.': '。', ';': '；', ':': '：',
             '?': '？', '!': '！', '(': '（', ')': '）'}


def check_text(text, mask):
    """硬规则 1、2、5。返回 (确定违例, 疑似违例)。"""
    definite, suspect = [], []
    cn_lines = chinese_lines(text)

    for i, ch in enumerate(text):
        if mask[i]:
            continue
        ln = line_of(text, i)

        if ch == '"':
            definite.append((ln, 'R1 直双引号', context(text, i), i))
        elif ch == "'":
            prev = text[i - 1] if i else ''
            nxt = text[i + 1] if i + 1 < len(text) else ''
            if prev.isalpha() and nxt.isalpha():
                definite.append((ln, 'R1 英文撇号', context(text, i), i))
            else:
                definite.append((ln, 'R1 直单引号', context(text, i), i))
        elif ch in PUNCT_MAP and ln in cn_lines:
            prev = text[i - 1] if i else ''
            nxt = text[i + 1] if i + 1 < len(text) else ''
            if is_cjk(prev) or is_cjk(nxt):
                definite.append((ln, 'R2 中英标点混用', context(text, i), i))
            else:
                suspect.append((ln, 'R2 疑似标点混用', context(text, i), i))

    for m in EMOJI.finditer(text):
        definite.append((line_of(text, m.start()), 'R5 emoji', m.group(), m.start()))

    for i, ch in enumerate(text):
        if ch in DINGBATS and not mask[i]:
            definite.append((line_of(text, i), 'R5 装饰符号', context(text, i), i))

    for phrase in CHAT_PHRASES:
        for m in re.finditer(re.escape(phrase), text):
            definite.append((line_of(text, m.start()), 'R5 聊天语气', phrase, m.start()))

    return definite, suspect


def check_code(text):
    """硬规则 3，只看注释行。"""
    issues = []
    for ln, line in enumerate(text.split('\n'), 1):
        idx = line.find('#')
        if idx < 0:
            continue
        comment = line[idx:]
        if re.search(r'#\s*[=*\-#/_]{4,}', comment):
            issues.append((ln, 'R3 ASCII 装饰', comment.strip(), 0))
        if re.search(r'#\s*[─━═]{2,}', comment):
            issues.append((ln, 'R3 Unicode 装饰', comment.strip(), 0))
        for pat in VERSION_PATTERNS:
            if re.search(pat, comment, re.IGNORECASE):
                issues.append((ln, 'R3 版本痕迹', comment.strip(), 0))
                break
    return issues


def check_docx(path):
    try:
        from docx import Document
    except ImportError:
        return [(0, '依赖缺失', '请先 pip install python-docx', 0)]

    issues = []
    doc = Document(path)

    def scan(runs, where):
        for run in runs:
            color = run.font.color.rgb
            if color is None:
                continue
            if (color[0], color[1], color[2]) != (0, 0, 0):
                issues.append((0, 'R4 非黑',
                               f'{where} 颜色 {tuple(color)} 文本 {run.text[:30]}', 0))

    for i, p in enumerate(doc.paragraphs):
        scan(p.runs, f'paragraph {i}')
    for ti, table in enumerate(doc.tables):
        for ri, row in enumerate(table.rows):
            for ci, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    scan(p.runs, f'table {ti} cell {ri},{ci}')
    return issues


def fix_text(text, mask):
    """只修确定违例。直引号按段落配对成弯引号，中文邻接的 ASCII 标点转全角。"""
    chars = list(text)
    double_open = True
    single_open = True
    prev_blank = False

    for i, ch in enumerate(chars):
        if mask[i]:
            continue
        if ch == '\n':
            prev_blank = i + 1 < len(chars) and chars[i + 1] == '\n'
            if prev_blank:
                double_open = single_open = True
            continue
        if ch == '"':
            chars[i] = '“' if double_open else '”'
            double_open = not double_open
        elif ch == "'":
            prev = chars[i - 1] if i else ''
            nxt = chars[i + 1] if i + 1 < len(chars) else ''
            if prev.isalpha() and nxt.isalpha():
                chars[i] = '’'
            else:
                chars[i] = '‘' if single_open else '’'
                single_open = not single_open

    text2 = ''.join(chars)
    cn_lines = chinese_lines(text2)
    chars = list(text2)
    for i, ch in enumerate(chars):
        if mask[i] or ch not in PUNCT_MAP:
            continue
        if line_of(text2, i) not in cn_lines:
            continue
        prev = chars[i - 1] if i else ''
        nxt = chars[i + 1] if i + 1 < len(chars) else ''
        if is_cjk(prev) or is_cjk(nxt):
            chars[i] = PUNCT_MAP[ch]
    return ''.join(chars)


def report(definite, suspect, show_all):
    if definite:
        print(f'[FAIL] 确定违例 {len(definite)} 处：')
        for ln, rule, ctx, _ in sorted(definite)[:80]:
            print(f'  L{ln} [{rule}] {ctx}')
        if len(definite) > 80:
            print(f'  ... 还有 {len(definite) - 80} 处未显示')
    else:
        print('[PASS] 无确定违例')

    if suspect:
        limit = len(suspect) if show_all else 15
        print(f'\n[疑似] {len(suspect)} 处，需人工判断（公式、引用、变量内的标点本就该保留）：')
        for ln, rule, ctx, _ in sorted(suspect)[:limit]:
            print(f'  L{ln} [{rule}] {ctx}')
        if len(suspect) > limit:
            print(f'  ... 还有 {len(suspect) - limit} 处，加 --all 查看')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}

    if not args:
        print('用法: python check_kaiwriting.py <文件路径> [--fix] [--all]')
        sys.exit(2)

    path = Path(args[0])
    if not path.exists():
        print(f'文件不存在: {path}')
        sys.exit(2)

    if path.suffix.lower() == '.docx':
        issues = check_docx(path)
        report(issues, [], '--all' in flags)
        sys.exit(1 if issues else 0)

    text = path.read_text(encoding='utf-8')
    mask = build_mask(text)

    if '--fix' in flags:
        fixed = fix_text(text, mask)
        if fixed == text:
            print('无可自动修复的确定违例')
        else:
            path.write_text(fixed, encoding='utf-8')
            before, _ = check_text(text, mask)
            after, _ = check_text(fixed, build_mask(fixed))
            print(f'已修复：确定违例 {len(before)} 处降至 {len(after)} 处')
        sys.exit(0)

    definite, suspect = check_text(text, mask)
    if path.suffix.lower() in CODE_EXTS:
        definite += check_code(text)

    report(definite, suspect, '--all' in flags)
    sys.exit(1 if definite else 0)


if __name__ == '__main__':
    main()
