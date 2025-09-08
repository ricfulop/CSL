#!/usr/bin/env python3
"""
Simple test script for FreeCAD backend
Can be run directly in FreeCAD's Python console or standalone
"""
import sys
from pathlib import Path

# Add the CSL directory to path
csl_path = Path(__file__).parent
sys.path.insert(0, str(csl_path))

from triple_lindy.transpilers.freecad_backend import FreeCADBackend

def test_basic_shapes():
    """Test basic shape creation with FreeCAD backend."""
    
    print("Testing FreeCAD Backend...")
    print("-" * 40)
    
    # Initialize backend
    backend = FreeCADBackend()
    
    # Check availability
    caps = backend.get_capabilities()
    print(f"FreeCAD available: {caps['available']}")
    
    if not caps['available']:
        print("FreeCAD is not available. Please run this script in FreeCAD.")
        return
    
    # Open session
    print("\nOpening session...")
    backend.open_session({"document": "TestDoc", "clear_existing": True})
    
    # Create a simple box using CSL IR
    print("\nCreating box from CSL IR...")
    
    csl_ir = {
        "csl": "1.3",
        "meta": {"name": "Test Box", "units": "mm"},
        "sketches": [
            {
                "id": "box_profile",
                "on": "XY",
                "entities": [
                    {"type": "rect", "id": "base", "p1": [0, 0], "p2": [60, 40]}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "box_body",
                "profile": "box_profile",
                "distance": 30,
                "op": "new_solid"
            }
        ]
    }
    
    result = backend.realize(csl_ir)
    print(f"Result: {result}")
    
    # Create a cylinder
    print("\nCreating cylinder...")
    
    csl_ir_cylinder = {
        "csl": "1.3",
        "meta": {"name": "Test Cylinder", "units": "mm"},
        "sketches": [
            {
                "id": "cylinder_profile",
                "on": "XY",
                "entities": [
                    {"type": "circle", "id": "circ", "center": [100, 20], "d": 40}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "cylinder_body",
                "profile": "cylinder_profile",
                "distance": 50,
                "op": "new_solid"
            }
        ]
    }
    
    result2 = backend.realize(csl_ir_cylinder)
    print(f"Result: {result2}")
    
    # Query state
    print("\nQuerying state...")
    state = backend.query_state()
    print(f"Document: {state.get('document')}")
    print(f"Objects created: {len(state.get('objects', []))}")
    print(f"Bodies: {len(state.get('bodies', []))}")
    
    # Export to STEP
    print("\nExporting to STEP...")
    backend.export([{
        "format": "STEP",
        "path": "test_output.step"
    }])
    
    print("\n✅ Test complete!")
    print("Check FreeCAD viewport for the created geometry")
    
    return backend

if __name__ == "__main__":
    backend = test_basic_shapes()
