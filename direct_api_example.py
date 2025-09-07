#!/usr/bin/env python3
"""
Direct API Approach Example

This shows how to use Fusion 360's API directly without CSL.
This code would run inside a Fusion add-in or script.
"""

import adsk.core
import adsk.fusion

def create_three_cylinders():
    """Create three cylinders using direct Fusion API calls"""
    
    # Get the active design
    app = adsk.core.Application.get()
    design = app.activeProduct
    if not design:
        return
    
    root = design.rootComponent
    
    # Cylinder 1: At origin
    sketch1 = root.sketches.add(root.xYConstructionPlane)
    circle1 = sketch1.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(0, 0, 0),  # Center at origin
        1.0  # 1cm radius = 10mm
    )
    
    # Get profile and extrude
    prof1 = sketch1.profiles.item(0)
    ext1_input = root.features.extrudeFeatures.createInput(
        prof1, 
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation  # Create new body
    )
    ext1_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(3.0))  # 3cm height
    ext1 = root.features.extrudeFeatures.add(ext1_input)
    
    # Cylinder 2: Offset in X
    sketch2 = root.sketches.add(root.xYConstructionPlane)
    circle2 = sketch2.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(4, 0, 0),  # 4cm offset in X
        1.0  # 1cm radius
    )
    
    prof2 = sketch2.profiles.item(0)
    ext2_input = root.features.extrudeFeatures.createInput(
        prof2,
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation  # Create new body
    )
    ext2_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(3.0))
    ext2 = root.features.extrudeFeatures.add(ext2_input)
    
    # Cylinder 3: Offset in Y
    sketch3 = root.sketches.add(root.xYConstructionPlane)
    circle3 = sketch3.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(2, 3, 0),  # 2cm in X, 3cm in Y
        1.0  # 1cm radius
    )
    
    prof3 = sketch3.profiles.item(0)
    ext3_input = root.features.extrudeFeatures.createInput(
        prof3,
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation  # Create new body
    )
    ext3_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(3.0))
    ext3 = root.features.extrudeFeatures.add(ext3_input)
    
    # Zoom to fit
    app.activeViewport.fit()
    
    return {
        "cylinders_created": 3,
        "sketches": [sketch1.name, sketch2.name, sketch3.name],
        "extrudes": [ext1.name, ext2.name, ext3.name]
    }

# If running in Fusion:
# result = create_three_cylinders()
# print(f"Created: {result}")
