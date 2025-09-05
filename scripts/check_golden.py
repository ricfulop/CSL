#!/usr/bin/env python3
import json
import sys
from pathlib import Path

summary_path = Path('out/golden_summary.json')
report_path = Path('out/conformance_report.json')
if not summary_path.exists():
    print('golden_summary.json not found. Run the conformance harness first.', file=sys.stderr)
    sys.exit(2)

summary = json.loads(summary_path.read_text())

# Prefer detailed report to ignore environment-only diagnostics (E3000)
ignore_env_codes = {"E3000"}
case_errors = {}
if report_path.exists():
    report = json.loads(report_path.read_text())
    for c in report.get('cases', []):
        cid = c.get('id')
        errs = [e for e in (c.get('errors') or []) if str(e.get('code')) not in ignore_env_codes]
        case_errors[cid] = len(errs)

ok = bool(summary.get('ok'))
fail_cases = []
for c in summary.get('cases', []):
    cid = c.get('id')
    cok = c.get('ok')
    errs = int(c.get('errors') or 0)
    # Override with filtered counts when available
    if cid in case_errors:
        errs = case_errors[cid]
    if not cok or errs > 0:
        fail_cases.append((cid, errs))

if ok and not fail_cases:
    print('Golden check: PASS')
    sys.exit(0)

if fail_cases:
    print('Golden check: FAIL')
    for cid, errs in fail_cases:
        print(f' - {cid}: errors={errs}')
    sys.exit(1)

print('Golden check: FAIL (unknown)')
sys.exit(1)
