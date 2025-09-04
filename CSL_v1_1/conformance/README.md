# CSL v1.0 Conformance Kit (Starter)

This folder defines *golden tests* to validate adapters.

## Test Set
1. **L-Bracket** (`examples/l_bracket.csl`)
   - Checks: mass/volume/area/BB stable; holes detected via `query.cylindrical_faces` (d≈6.5 mm).
2. **Threaded Plate** (`examples/threaded_plate.csl`)
   - Checks: hole callout present; cosmetic thread metadata present; face tags preserved.
3. **Lofted Connector** (`examples/lofted_connector.csl`)
   - Checks: continuity G1 respected; section/guide mapping correct.
4. **Assembly Plate+Spacers+Bolts** (`examples/assembly_plate_spacers_bolts.csl`)
   - Checks: mate connector placement; fasten joints; stable instance IDs.
5. **ECAD Board** (`examples/ecad_board_example.csl`)
   - Checks: board outline from sketch; components placed; DRC rules encoded.

## Expected Outputs
- For each test, emit a JSON IR (`.csl.json`) and backend artifacts (e.g., FeatureScript, FreeCAD doc, Blender .blend or GN json, KiCad .kicad_pcb).

## Validation
- Geometry: compare scalar props (mass/area/volume/bbox) within tolerance.
- Topology: re-evaluate saved queries; counts must match.
- IDs/Tags: Verify presence and mapping stability.
- Diagnostics: ambiguous selections must produce E12xx series codes.
