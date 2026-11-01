#!/usr/bin/env python3
"""给还没有 date 的条目补上收录日期，取该文件第一次提交进仓库的日期。

在仓库根目录运行：
    python3 .github/scripts/backfill-dates.py          # 只列出将要做的修改
    python3 .github/scripts/backfill-dates.py --write  # 实际写入
尚未提交的文件用今天的日期。date 插在 title 那一行的后面。
"""
import subprocess
import sys
from datetime import date
from pathlib import Path


def first_added(path):
    out = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A",
         "--format=%ad", "--date=format:%Y-%m-%d", "--", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return out[-1] if out else date.today().isoformat()


def main(write):
    changed = 0
    for path in sorted(Path("content/books").glob("*/*.md")):
        if path.name == "_index.md":
            continue
        lines = path.read_text(encoding="utf-8").split("\n")
        if not lines or lines[0].strip() != "---":
            print(f"跳过（没有 YAML front matter）：{path}")
            continue
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is None:
            print(f"跳过（front matter 没有结束的 ---）：{path}")
            continue
        front = lines[1:end]
        if any(l.startswith("date:") for l in front):
            continue
        at = next((i for i, l in enumerate(front, 1) if l.startswith("title:")), end - 1)
        d = first_added(path)
        print(f"{path}：date: {d}")
        if write:
            lines.insert(at + 1, f"date: {d}")
            path.write_text("\n".join(lines), encoding="utf-8")
        changed += 1
    action = "已写入" if write else "将写入（加 --write 实际写入）"
    print(f"共 {changed} 个条目{action}。")


if __name__ == "__main__":
    main("--write" in sys.argv)
