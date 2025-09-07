"""Fusion Script wrapper for run_fusion_example.

This provides the required run(context) entrypoint and bootstraps PYTHONPATH
to the repo root so we can import the existing script implementation.
"""
from __future__ import annotations

import sys
from pathlib import Path


def run(context) -> None:  # Fusion script entrypoint
    repo_root = Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    import adsk.core  # type: ignore
    import adsk.fusion  # type: ignore
    app = adsk.core.Application.get()
    ui = app.userInterface if app else None

    # Prefer backend example; fall back to direct Fusion demo.
    try:
        from scripts.run_fusion_example import main as real_main  # type: ignore
        try:
            real_main()
            try:
                if app and app.activeViewport:
                    app.activeViewport.fit()
            except Exception:
                pass
            if ui:
                ui.messageBox("CSL example completed via backend. Outputs written to repo 'out/'.")
            return
        except Exception as e:
            if ui:
                try:
                    ui.messageBox(f"Backend failed, using direct Fusion demo. Details: {e}")
                except Exception:
                    pass
    except Exception:
        pass

    # Direct Fusion demo (write any temp artifacts to Documents)
    try:
        design: adsk.fusion.Design = app.activeProduct  # type: ignore
        if not isinstance(design, adsk.fusion.Design):
            docs = app.documents
            docs.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
            design = app.activeProduct  # type: ignore
        root = design.rootComponent
        sk = root.sketches.add(root.xYConstructionPlane)
        sk.name = "CSL Demo Sketch"
        p1 = adsk.core.Point3D.create(0, 0, 0)
        p2 = adsk.core.Point3D.create(8, 6, 0)  # cm units by default
        _ = sk.sketchCurves.sketchLines.addTwoPointRectangle(p1, p2)
        prof = sk.profiles.item(0)
        ext = root.features.extrudeFeatures
        dist = adsk.core.ValueInput.createByReal(0.6)  # 6 mm in cm
        ein = ext.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ein.setDistanceExtent(False, dist)
        ext.add(ein)
        # Export STL and capture preview under Documents/CSL/out
        out_dir = Path.home() / "Documents" / "CSL" / "out"
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        try:
            exp = design.exportManager
            stl_path = str(out_dir / "demo_block.stl")
            try:
                opts = exp.createSTLExportOptions(root, stl_path)
            except Exception:
                opts = exp.createSTLExportOptions(root.bRepBodies, stl_path)
            exp.execute(opts)
        except Exception:
            pass
        try:
            vp = app.activeViewport if app else None
            if vp:
                vp.saveAsImageFile(str(out_dir / "demo_preview.png"), 800, 600)
        except Exception:
            pass
        try:
            if app and app.activeViewport:
                app.activeViewport.fit()
        except Exception:
            pass
        if ui:
            ui.messageBox(f"CSL example (direct Fusion) completed.\nFiles in: {out_dir}")
    except Exception as e:
        if ui:
            ui.messageBox(f"CSL example failed: {e}")


