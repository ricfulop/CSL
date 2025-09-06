#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


STATUS_WEIGHT = {"[Done]": 1.0, "[Partial]": 0.5, "[Diag]": 0.2, "[Todo]": 0.0}

# Category weights reflect relative implementation complexity/importance
FEATURE_WEIGHTS = {
    "Sketch entities": 1.0,
    "Sketch constraints and dimensions": 1.5,
    "Extrude": 1.0,
    "Thin extrude": 0.5,
    "Rib": 0.5,
    "Revolve": 0.8,
    "Sweep": 1.2,
    "Loft": 1.5,
    "Shell": 0.8,
    "Draft": 0.8,
    "Fillet": 1.2,
    "Chamfer": 1.0,
    "Wrap/Emboss/Project": 1.5,
    "Hole": 1.0,
    "Threads": 1.0,
    "Patterns": 1.0,
    "Boolean": 1.0,
    "Move/Offset/Replace Face": 0.8,
    "Split body": 0.8,
    "Mirror": 0.5,
    "Surface Ops": 1.2,
    "Sheet Metal": 2.0,
    "Materials/PMI": 0.6,
    "Selection/Queries": 0.8,
    "Export/Thumbnail": 0.7,
    "APS Orchestration": 0.4,
}


def extract_grouped(md: str) -> dict[str, list[str]]:
    """Return mapping of category (top-level bullet) -> list of status tags for its sub-items."""
    grouped: dict[str, list[str]] = {}
    current_category: str | None = None
    for raw in md.splitlines():
        line = raw.rstrip("\n")
        # Count leading spaces
        leading = len(line) - len(line.lstrip(" "))
        m = re.match(r"^\s*-\s+(.+)$", line)
        if not m:
            continue
        text = m.group(1).strip()
        # Detect status
        status = None
        for tag in STATUS_WEIGHT:
            if tag in text:
                status = tag
                break
        if status is None:
            # Likely a category if no status and not indented (top-level)
            if leading == 0:
                current_category = text
                if current_category not in grouped:
                    grouped[current_category] = []
            continue
        # Sub-item with status; attribute to current category
        if current_category is None:
            # Fallback: treat the text itself as a category
            current_category = text
            if current_category not in grouped:
                grouped[current_category] = []
        grouped[current_category].append(status)
    return grouped


def compute_percentage_grouped(grouped: dict[str, list[str]]) -> float:
    if not grouped:
        return 0.0
    total_w = 0.0
    acc = 0.0
    for cat, statuses in grouped.items():
        if not statuses:
            continue
        # Average status for this category
        avg = sum(STATUS_WEIGHT.get(s, 0.0) for s in statuses) / float(len(statuses))
        w = FEATURE_WEIGHTS.get(cat, 1.0)
        acc += avg * w
        total_w += w
    if total_w == 0.0:
        return 0.0
    return (acc / total_w) * 100.0


def update_badge(md: str, pct: float) -> str:
    import urllib.parse as up
    val = f"{pct:.0f}%"
    color = "red"
    if pct >= 90:
        color = "brightgreen"
    elif pct >= 75:
        color = "green"
    elif pct >= 60:
        color = "yellowgreen"
    elif pct >= 40:
        color = "yellow"
    label = "Fusion Coverage"
    url = f"https://img.shields.io/badge/{up.quote(label)}-{up.quote(val)}-{color}"
    badge_md = f"![Coverage]({url})"
    if "![Coverage](" in md:
        return re.sub(r"!\[Coverage\]\([^)]*\)", badge_md, md, count=1)
    # Insert under title
    lines = md.splitlines()
    if lines and lines[0].startswith("# "):
        lines.insert(2, badge_md)
        return "\n".join(lines)
    return badge_md + "\n\n" + md


def main() -> None:
    path = Path("FUSION_FEATURE_COVERAGE.md")
    md = path.read_text(encoding="utf-8")
    grouped = extract_grouped(md)
    pct = compute_percentage_grouped(grouped)
    new_md = update_badge(md, pct)
    path.write_text(new_md, encoding="utf-8")
    print(f"fusion_feature_coverage_percent={pct:.2f}")


if __name__ == "__main__":
    main()


