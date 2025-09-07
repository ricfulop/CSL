#!/usr/bin/env python3
"""
CSL Remote Control Script
Run CSL commands in Fusion 360 from command line.
"""
import argparse
import json
import sys
from pathlib import Path

# Add repo root to path
repo_root = Path(__file__).resolve().parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from triple_lindy.transpilers.fusion360_backend import FusionBackend

def run_example():
    """Run the example plate with hole"""
    try:
        backend = FusionBackend()
        backend.open_session()

        ir = {
            "csl": "1.1",
            "meta": {"name": "Remote Example", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "80 mm,60 mm"},
                    {"kind": "circle", "id": "h1", "center": "20 mm,20 mm", "d": "8 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate - h1", "distance": "8 mm", "op": "new_solid", "result": "part"},
                {"kind": "fillet", "id": "f", "edges": "query.edges(part)", "radius": "4 mm"}
            ]
        }

        mapping = backend.realize(ir)
        print(f"✅ Success! Created {len(mapping)} features in Fusion")
        return True

    except Exception as e:
        print(f"❌ Failed: {e}")
        return False

def run_ir_file(file_path):
    """Run IR from JSON file"""
    try:
        with open(file_path, 'r') as f:
            ir = json.load(f)

        backend = FusionBackend()
        backend.open_session()
        mapping = backend.realize(ir)

        print(f"✅ Success! Created {len(mapping)} features from {file_path}")
        return True

    except Exception as e:
        print(f"❌ Failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="CSL Remote Control for Fusion 360")
    parser.add_argument("command", choices=["example", "file"], help="Command to run")
    parser.add_argument("--file", help="JSON file containing CSL IR (for 'file' command)")

    args = parser.parse_args()

    if args.command == "example":
        success = run_example()
    elif args.command == "file":
        if not args.file:
            print("❌ Error: --file required for 'file' command")
            return 1
        success = run_ir_file(args.file)
    else:
        print("❌ Unknown command")
        return 1

    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
