"""Run a minimal Fusion 360 example using the FusionBackend stub.

This script demonstrates loading a small CSL IR and calling the adapter.
When Fusion is unavailable, it will run in dry-run mode and print mappings.
"""
from __future__ import annotations

import json
from pathlib import Path

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def main() -> None:
    # Write outputs to a user-writable location (Fusion sandbox safe)
    out_dir = Path.home() / "Documents" / "CSL" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    example_csl_ir = {
        "csl": "1.1",
        "meta": {"name": "Example", "units": "mm"},
        "sketches": [
            {"id": "s_base", "plane": "world.xy", "entities": [
                {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "80 mm, 60 mm"},
                {"kind": "circle", "id": "h1", "center": "15 mm, 15 mm", "d": "6.5 mm"},
                {"kind": "circle", "id": "h2", "center": "65 mm, 15 mm", "d": "6.5 mm"},
            ]}
        ],
        "features": [
            {"kind": "extrude", "id": "main", "profile": "plate - h1 - h2", "distance": "6 mm", "op": "new_solid", "result": "part"},
            {"kind": "fillet", "id": "f1", "edges": "query.edges(part)", "radius": "3 mm"}
        ],
        "export": [
            {"id": "stl_out", "format": "STL", "path": str(out_dir / "plate.stl"), "target": "part"}
        ],
        "thumbnail": [
            {"id": "preview", "path": str(out_dir / "preview.png"), "width": 800, "height": 600, "view": "iso", "style": "shaded"}
        ]
    }

    backend = FusionBackend()
    backend.open_session()
    mapping = backend.realize(example_csl_ir)
    backend.export(example_csl_ir.get("export", []))
    backend.thumbnail(example_csl_ir.get("thumbnail", []))

    (out_dir / "mapping.json").write_text(json.dumps(mapping, indent=2))
    print(f"Done. Mapping written to {out_dir / 'mapping.json'}")


if __name__ == "__main__":
    main()


