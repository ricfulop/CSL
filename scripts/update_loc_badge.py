#!/usr/bin/env python3
"""
Recompute LOC across the repo and update README badge line.
 - Totals across all files (excluding .git, out, __pycache__)
 - Python, Markdown, JSON subtotals
 - Fusion backend key file lines

Idempotent: updates only the badge line if values changed.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

def run(cmd: str) -> str:
    res = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(ROOT))
    return res.stdout.decode().strip()

def count_total() -> int:
    cmd = "find . -type f -not -path './.git/*' -not -path './out/*' -not -path '*/__pycache__/*' -print0 | xargs -0 cat | wc -l"
    out = run(cmd)
    return int(out)

def count_glob(glob: str, exclude: str = "") -> int:
    base = f"find . -type f -name '{glob}'"
    if exclude:
        base += f" -not -path '{exclude}'"
    base += " -print0 | xargs -0 cat | wc -l"
    return int(run(base))

def count_file(path: str) -> int:
    return int(run(f"wc -l {path} | awk '{{print $1}}'"))

def main() -> None:
    total = count_total()
    py = count_glob("*.py", "*/__pycache__/*")
    md = count_glob("*.md")
    jsn = count_glob("*.json")
    fusion_file = "triple_lindy/transpilers/fusion360_backend.py"
    fusion_loc = count_file(fusion_file)

    readme = README.read_text()
    badge_re = re.compile(r"^!\[LOC\]\(.*?\) .*?JSON%20LOC-\d+-informational\)\s*$", re.M)
    new_badge = (
        f"![LOC](https://img.shields.io/badge/LOC-{total}-blue) "
        f"![Python%20LOC](https://img.shields.io/badge/Python%20LOC-{py}-blue) "
        f"![Docs%20LOC](https://img.shields.io/badge/Docs%20LOC-{md}-lightgrey) "
        f"![JSON%20LOC](https://img.shields.io/badge/JSON%20LOC-{jsn}-informational)"
    )
    if badge_re.search(readme):
        updated = badge_re.sub(new_badge, readme)
    else:
        # Insert under the main title if not present
        lines = readme.splitlines()
        if lines:
            lines.insert(1, new_badge)
            updated = "\n".join(lines)
        else:
            updated = new_badge + "\n" + readme

    # Also update the Project size block numbers if present
    updated = re.sub(r"Total lines: \d+", f"Total lines: {total}", updated)
    updated = re.sub(r"Python lines: \d+", f"Python lines: {py}", updated)
    updated = re.sub(r"Markdown/docs lines: \d+", f"Markdown/docs lines: {md}", updated)
    updated = re.sub(r"JSON lines: \d+", f"JSON lines: {jsn}", updated)
    updated = re.sub(r"fusion360_backend.py`: \d+", f"fusion360_backend.py`: {fusion_loc}", updated)

    if updated != readme:
        README.write_text(updated)
        print("README LOC badges updated.")
    else:
        print("README LOC badges already up to date.")

if __name__ == "__main__":
    main()


