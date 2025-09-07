"""
Direct CSL test - Run this as a Fusion script
No WebSocket needed - uses your existing backend directly
"""
def run(context):
    import adsk.core
    import adsk.fusion
    import sys
    from pathlib import Path
    
    # Add CSL to path
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    sys.path.insert(0, str(repo_root))
    
    app = adsk.core.Application.get()
    ui = app.userInterface
    
    try:
        # Import your backend
        from triple_lindy.transpilers.fusion360_backend import FusionBackend
        
        # Create backend instance
        backend = FusionBackend()
        backend.open_session()
        
        # Define a test part
        ir = {
            "csl": "1.1",
            "meta": {"name": "CSL Direct Test", "units": "mm"},
            "sketches": [
                {
                    "id": "s1",
                    "plane": "world.xy",
                    "entities": [
                        {"kind": "rect", "id": "base", "p1": "0,0", "p2": "80 mm,50 mm"},
                        {"kind": "circle", "id": "hole1", "center": "20 mm,25 mm", "d": "10 mm"},
                        {"kind": "circle", "id": "hole2", "center": "60 mm,25 mm", "d": "10 mm"}
                    ]
                }
            ],
            "features": [
                {
                    "kind": "extrude",
                    "id": "ext1",
                    "profile": "base - hole1 - hole2",
                    "distance": "15 mm",
                    "op": "new_solid",
                    "result": "plate"
                },
                {
                    "kind": "fillet",
                    "id": "fil1",
                    "edges": "query.edges(plate).filter(length > 40 mm)",
                    "radius": "5 mm"
                },
                {
                    "kind": "chamfer",
                    "id": "cham1",
                    "edges": "query.edges(hole1) + query.edges(hole2)",
                    "distance": "2 mm"
                }
            ]
        }
        
        # Realize the design
        ui.progressBar.show("Creating CSL Design", "Processing...", 0, 3, 1)
        
        mapping = backend.realize(ir)
        
        ui.progressBar.hide()
        
        # Zoom to fit
        viewport = app.activeViewport
        if viewport:
            viewport.fit()
        
        # Show success
        ui.messageBox(
            f"✅ Success!\n\n" +
            f"Created {len(mapping)} features:\n" +
            f"• Plate with 2 holes\n" +
            f"• Rounded corners (fillet)\n" + 
            f"• Chamfered holes\n\n" +
            f"Your CSL backend is working perfectly!",
            "CSL Direct Test"
        )
        
    except Exception as e:
        if ui:
            ui.messageBox(f"Error: {str(e)}", "CSL Test Failed")
            import traceback
            print(traceback.format_exc())
