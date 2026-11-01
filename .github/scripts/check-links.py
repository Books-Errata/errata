#!/usr/bin/env python3
"""检查构建结果中的站内链接：目标页面是否存在，#锚点是否存在。

用法：python3 .github/scripts/check-links.py public
只检查 <a href>；站外链接、mailto 等不检查（结果不稳定，交给人工）。
发现问题时以 GitHub Actions 注释的格式输出，并以非零状态退出。
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("id", "name"):
            if a.get(key):
                self.ids.add(a[key])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])


def parse(path, cache={}):
    if path not in cache:
        p = Page()
        p.feed(path.read_text(encoding="utf-8"))
        cache[path] = p
    return cache[path]


def resolve(root, page, href):
    """把链接解析成 public 下的文件；找不到返回 None。"""
    path = unquote(urlsplit(href).path)
    if not path:
        return page
    target = (root / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
    for cand in (target, target / "index.html", target.with_suffix(".html")):
        if cand.is_file():
            return cand
    return None


def main(root):
    root = Path(root)
    problems = 0
    for page in sorted(root.rglob("*.html")):
        if "pagefind" in page.parts:
            continue
        for href in parse(page).links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            rel = page.relative_to(root)
            target = resolve(root, page, href)
            if target is None:
                print(f"::error file={rel}::死链：{href}")
                problems += 1
                continue
            frag = unquote(parts.fragment)
            if frag and target.suffix == ".html" and frag not in parse(target).ids:
                print(f"::error file={rel}::锚点不存在：{href}")
                problems += 1
    print(f"站内链接检查完成，发现 {problems} 处问题。")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))
