## Documentation Index

A concise map of key documents in this repository. See `docs_index.json` for a machine-readable index.

### Root
- [README.md](README.md)
  - Summary: AI agent-driven meta-parametric design across CAD/CAE/CAM, BOM, factory automation; Fusion-first multi-backend.
  - Keywords: CSL, AI agent, meta-parametric, Fusion 360, Onshape, SolidWorks, FreeCAD, Blender

- [LICENSE](LICENSE)
  - Summary: MIT License (c) 2025 Ric Fulop.
  - Keywords: license, MIT

- [Triple Lindy – Complete Zero-Shot Implementation (v1.0)](./triple_lindy_complete%20with%20CSL.md)
  - Summary: Fusion-first implementation with multi-backend support; add-in setup, file implementations, and tests for a chat-driven CAD/EDA agent. FreeCAD remains supported as an optional backend.
  - Keywords: Triple Lindy, Fusion 360, Onshape, SolidWorks, Blender, workbench, agent, zero-shot, pytest, implementation

- [BACKEND_GAP_ANALYSIS.md](BACKEND_GAP_ANALYSIS.md)
  - Summary: Coverage comparison and gaps between CSL v1.1 and Fusion 360, Onshape, SolidWorks, Blender. Includes fallbacks and roadmap.
  - Keywords: gap analysis, Fusion 360, Onshape, SolidWorks, Blender, capabilities

### CSL v1.1
- [Specification: `CSL_v1_1/csl_v1_1_spec.md`](CSL_v1_1/csl_v1_1_spec.md)
  - Summary: Full language spec for CSL v1.1. Covers goals, headers/metadata, parameters, sketches, features, robust selection/query language, materials, assemblies, ECAD extension, new export/thumbnail ops, backend capabilities, security, and cheatsheet.
  - Key Sections: 0) Goals & Scope; 1) File Header & Metadata; 2) Core Concepts; 3) Parameters & Expressions; 4) Coordinate Frames & Planes; 5) Sketches/Constraints/Dimensions; 6) Features (incl. 6.1 Export & Visualization, 6.2 Geometry); 7) Selection & Query; 8) Materials & Properties; 9) Assemblies & Joints; 10) ECAD; 11) Backend Adapter Hints; 12) Errors/Determinism/IDs; 13) Minimal Grammar; 14) Canonical JSON IR; 15) Cross-Tool Mapping; 16) Backend Capabilities; 17) Security; 18) Version History; 19) Quick Reference.
  - Keywords: CSL, v1.1, spec, parameters, sketches, features, export, thumbnail, queries, assemblies, ECAD, backend capabilities

- [JSON Schema: `CSL_v1_1/csl_v1_1_schema.json`](CSL_v1_1/csl_v1_1_schema.json)
  - Summary: Canonical JSON IR schema for CSL v1.1 including export and thumbnail operations and backend capability structure.
  - Keywords: schema, JSON, IR, validation, export, thumbnail, capabilities

### Conformance
- [Conformance Kit README](CSL_v1_1/conformance/README.md)
  - Summary: Golden tests to validate adapters (geometry, topology, IDs/tags, diagnostics). Tests: L-Bracket, Threaded Plate, Lofted Connector, Assembly Plate+Spacers+Bolts, ECAD Board.
  - Keywords: conformance, tests, validation, adapters, golden tests

### Examples (`CSL_v1_1/examples`)
- [`l_bracket.csl`](CSL_v1_1/examples/l_bracket.csl)
  - Summary: Parametric L-bracket. Extrude plate with two holes, fillet edges, assign material.
  - Keywords: example, bracket, extrude, fillet, material

- [`threaded_plate.csl`](CSL_v1_1/examples/threaded_plate.csl)
  - Summary: Plate with through hole and cosmetic thread metadata.
  - Keywords: example, hole, thread, cosmetic

- [`lofted_connector.csl`](CSL_v1_1/examples/lofted_connector.csl)
  - Summary: Loft between circular and rectangular sections with G1 continuity.
  - Keywords: example, loft, continuity, profiles

- [`assembly_plate_spacers_bolts.csl`](CSL_v1_1/examples/assembly_plate_spacers_bolts.csl)
  - Summary: Simple assembly using mate connectors and fasten joints with stable instance IDs.
  - Keywords: example, assembly, mate connector, fasten, IDs

- [`ecad_board_example.csl`](CSL_v1_1/examples/ecad_board_example.csl)
  - Summary: ECAD extension example: board outline from sketch, stackup, DRC, component placement, routing hints.
  - Keywords: example, ECAD, KiCad, board, placement, DRC


