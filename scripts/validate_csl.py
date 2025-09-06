#!/usr/bin/env python3
"""Validate CSL JSON IR files against the specified schema (v1.1 or v1.2).

Usage:
  python scripts/validate_csl.py --schema CSL_v1_2/csl_v1_2_schema.json path/to/ir1.json [ir2.json ...]

If --schema is omitted, defaults to CSL_v1_2/csl_v1_2_schema.json.
Exits non-zero on any validation error.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

try:
    import jsonschema
    from jsonschema import Draft7Validator
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "jsonschema is required. Install with: pip install -r requirements-dev.txt\n"
        f"Import error: {exc}"
    )


def load_json(path: Path) -> object:
    return json.loads(path.read_text())


def validate_files(schema_path: Path, json_paths: List[Path]) -> int:
    schema = load_json(schema_path)
    validator = Draft7Validator(schema)
    failures = 0
    for p in json_paths:
        try:
            instance = load_json(p)
        except Exception as ex:
            print(f"[ERROR] {p}: failed to parse JSON: {ex}")
            failures += 1
            continue
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        if errors:
            print(f"[FAIL] {p}")
            for e in errors:
                loc = "/".join([str(x) for x in e.path]) or "<root>"
                print(f"  - at {loc}: {e.message}")
            failures += 1
        else:
            print(f"[OK]   {p}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Paths to CSL JSON IR files")
    parser.add_argument(
        "--schema",
        default=str(Path("CSL_v1_2") / "csl_v1_2_schema.json"),
        help="Path to JSON Schema file (default: v1.2 schema)",
    )
    args = parser.parse_args()

    schema_path = Path(args.schema)
    if not schema_path.is_file():
        print(f"Schema not found: {schema_path}")
        return 2

    json_paths = [Path(f) for f in args.files]
    missing = [p for p in json_paths if not p.is_file()]
    if missing:
        for p in missing:
            print(f"File not found: {p}")
        return 2

    failures = validate_files(schema_path, json_paths)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())


