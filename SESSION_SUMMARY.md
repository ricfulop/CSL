## CSL Work Summary – v0.3.0 shipped, v1.3 (draft) + v0.4.0 dev

### Shipped (v0.3.0)
- Constraints parity, loft/fillet/patterns upgrades, surface ops (initial), stable IDs refresh, selection goldens, export tessellation, capability JSON, APS tooling, CI golden gate.

### Active (v1.3 draft + v0.4.0)
- Docs (v1.3): `CSL_v1_3/csl_v1_3_spec.md`, `CSL_v1_3/csl_v1_3_schema.json`, `CSL_v1_3/USER_GUIDE_v1_3.md`, `RELEASE_NOTES_v1.3.0-draft.md`.
- Surface ops: `patch/extend/trim/knit` implemented (best‑effort); conformance added.
- Assemblies/joints: implementing mate connectors and assembly patterns; damping/preload best‑effort with diagnostics.

### Open next (finish to 100%)
Below is the full TODO list with current status.

- [in_progress] Assemblies/joints (v04-assemblies)
  - Mate connectors (placement/orientation/tags)
  - Assembly patterns (per‑occ transforms)
  - Damping/preload (apply where supported)
- [completed] Surface ops (v04-surface-ops)
  - patch/extend/trim/knit implemented; improve fidelity as needed
- [pending] Sheet metal (v04-sheet-metal)
  - base flange, edge flange, bends, unfold/refold mapping
- [pending] Constraints completion (v04-constraints)
  - curvature continuity mapping where supported; remaining relations
- [pending] Selection determinism hardening (v04-selection-determinism)
  - reorder/suppress/regenerate; multi‑version tests
- [pending] Stable IDs cross‑version (v04-stable-ids-xver)
  - reconciliation and persisted mapping upgrades
- [pending] Exports parity (v04-exports)
  - STEP AP242 metadata; 3MF parity; round‑trip validations
- [pending] PMI/GD&T (v04-pmi-gdt)
  - extend notes; light GD&T placement rules
- [pending] ECAD extension (v04-ecad)
  - refine schema and adapter hooks
- [pending] APS DA pipeline (v04-aps-da)
  - automate appbundle/activity/workitem; hosted‑runner docs
- [pending] Capabilities publishing (v04-capabilities)
  - refine JSON; versioned capability file per release
- [pending] Docs/examples (v04-docs-examples)
  - demo gallery, coverage matrix, new CSL samples
- [pending] CI enhancements (v04-ci)
  - Fusion‑enabled runner; query fuzzing; perf baselines & gates
- [in_progress] CSL v1.3 docs scaffold (v13-docs-scaffold)
  - spec, schema, user guide
- [pending] Glossary & indices (v13-glossary-index)
- [pending] v1.3 release notes & changelog (v13-release-notes)
- [pending] README/coverage updates for v1.3 (v13-readme-coverage)

### Key files to open (split view)
- Backend: `triple_lindy/transpilers/fusion360_backend.py` (assemblies/joints ~2770+)
- Conformance: `scripts/conformance_harness.py`
- Docs/Schema: `CSL_v1_3/*`

### Quick commands
```bash
make golden-check
make aps-auth
make aps-da-list-engines
```

### Notes
### Next up
- Finish: assemblies/joints → then sheet metal → constraints completion → selection/stable IDs x‑version → exports/AP242/3MF → PMI/GD&T → APS DA → docs/coverage/CI.
- Diagnostics include repair hints (E12xx/E23xx) to strengthen queries/options.
- Capability snapshot writes to `out/capabilities_fusion.json` on golden pass.


