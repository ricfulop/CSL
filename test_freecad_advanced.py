#!/usr/bin/env python3
"""
Advanced test script for FreeCAD backend - tests more features
Can be run directly in FreeCAD's Python console or standalone
"""
import sys
from pathlib import Path

# Add the CSL directory to path
csl_path = Path(__file__).parent
sys.path.insert(0, str(csl_path))

from triple_lindy.transpilers.freecad_backend import FreeCADBackend

def test_advanced_features():
    """Test advanced features with FreeCAD backend."""
    
    print("Testing FreeCAD Backend - Advanced Features")
    print("=" * 50)
    
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
    backend.open_session({"document": "AdvancedTest", "clear_existing": True})
    
    # Test 1: Create a part with multiple sketch entities
    print("\n1. Creating part with complex sketch...")
    
    csl_ir = {
        "csl": "1.3",
        "meta": {"name": "Complex Part", "units": "mm"},
        "sketches": [
            {
                "id": "complex_sketch",
                "on": "XY",
                "entities": [
                    {"type": "rect", "id": "outer", "p1": [0, 0], "p2": [100, 80]},
                    {"type": "circle", "id": "hole1", "center": [25, 40], "d": 20},
                    {"type": "circle", "id": "hole2", "center": [75, 40], "d": 20},
                    {"type": "line", "id": "centerline", "p1": [50, 0], "p2": [50, 80], "construction": True}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "base_body",
                "profile": "complex_sketch",
                "distance": 30,
                "op": "new_solid"
            }
        ]
    }
    
    result = backend.realize(csl_ir)
    print(f"Complex part result: {result}")
    
    # Test 2: Create a revolved part
    print("\n2. Creating revolved part...")
    
    csl_ir_revolve = {
        "csl": "1.3",
        "meta": {"name": "Revolved Part", "units": "mm"},
        "sketches": [
            {
                "id": "revolve_profile",
                "on": "XY",
                "entities": [
                    {"type": "line", "id": "l1", "p1": [20, 0], "p2": [40, 0]},
                    {"type": "line", "id": "l2", "p1": [40, 0], "p2": [40, 30]},
                    {"type": "line", "id": "l3", "p1": [40, 30], "p2": [25, 40]},
                    {"type": "line", "id": "l4", "p1": [25, 40], "p2": [20, 40]},
                    {"type": "line", "id": "l5", "p1": [20, 40], "p2": [20, 0]}
                ]
            }
        ],
        "features": [
            {
                "kind": "revolve",
                "id": "revolved_body",
                "profile": "revolve_profile",
                "axis": "Y",
                "angle": 360,
                "op": "new_solid"
            }
        ]
    }
    
    result2 = backend.realize(csl_ir_revolve)
    print(f"Revolve result: {result2}")
    
    # Test 3: Boolean operations
    print("\n3. Testing boolean operations...")
    
    csl_ir_boolean = {
        "csl": "1.3",
        "meta": {"name": "Boolean Test", "units": "mm"},
        "sketches": [
            {
                "id": "box1_sketch",
                "on": "XY",
                "entities": [
                    {"type": "rect", "id": "r1", "p1": [150, 0], "p2": [200, 50]}
                ]
            },
            {
                "id": "box2_sketch",
                "on": "XY", 
                "entities": [
                    {"type": "rect", "id": "r2", "p1": [175, 25], "p2": [225, 75]}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "box1",
                "profile": "box1_sketch",
                "distance": 50,
                "op": "new_solid"
            },
            {
                "kind": "extrude",
                "id": "box2",
                "profile": "box2_sketch",
                "distance": 50,
                "op": "new_solid"
            },
            {
                "kind": "boolean",
                "id": "union_result",
                "operation": "union",
                "targets": ["box1"],
                "tools": ["box2"]
            }
        ]
    }
    
    result3 = backend.realize(csl_ir_boolean)
    print(f"Boolean result: {result3}")
    
    # Test 4: Pattern feature
    print("\n4. Creating pattern...")
    
    csl_ir_pattern = {
        "csl": "1.3",
        "meta": {"name": "Pattern Test", "units": "mm"},
        "sketches": [
            {
                "id": "pattern_sketch",
                "on": "XY",
                "entities": [
                    {"type": "circle", "id": "seed_circle", "center": [250, 50], "d": 15}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "seed_body",
                "profile": "pattern_sketch",
                "distance": 20,
                "op": "new_solid"
            },
            {
                "kind": "pattern",
                "id": "linear_pattern",
                "pattern_type": "linear",
                "seed": "seed_body",
                "direction": [1, 0, 0],
                "spacing": 25,
                "count": 5
            }
        ]
    }
    
    result4 = backend.realize(csl_ir_pattern)
    print(f"Pattern result: {result4}")
    
    # Test 5: Circular pattern
    print("\n5. Creating circular pattern...")
    
    csl_ir_circular = {
        "csl": "1.3",
        "meta": {"name": "Circular Pattern", "units": "mm"},
        "sketches": [
            {
                "id": "circ_pattern_sketch",
                "on": "XY",
                "entities": [
                    {"type": "rect", "id": "seed_rect", "p1": [50, 150], "p2": [60, 160]}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "circ_seed",
                "profile": "circ_pattern_sketch",
                "distance": 10,
                "op": "new_solid"
            },
            {
                "kind": "pattern",
                "id": "circular_pattern",
                "pattern_type": "circular",
                "seed": "circ_seed",
                "axis": "Z",
                "count": 8
            }
        ]
    }
    
    result5 = backend.realize(csl_ir_circular)
    print(f"Circular pattern result: {result5}")
    
    # Query final state
    print("\n6. Querying final state...")
    state = backend.query_state()
    print(f"Document: {state.get('document')}")
    print(f"Total objects: {state.get('object_count')}")
    
    # Export all to STEP
    print("\n7. Exporting to STEP...")
    backend.export([{
        "format": "STEP",
        "path": "advanced_test_output.step"
    }])
    
    print("\n✅ Advanced test complete!")
    print("Check FreeCAD viewport for the created geometry")
    print("Exported to: advanced_test_output.step")
    
    return backend

if __name__ == "__main__":
    backend = test_advanced_features()
