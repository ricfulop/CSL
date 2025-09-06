# Multi tool agentic control for CAD and engineering software: Plan and Architecture (Draft)

## Vision
An AI agent driven like experience for CAD and engineering software: natural language to complex, deterministic geometry and assemblies, across multiple CAD backends, with schema-validated CSL as the lingua franca.

## Core UX
- NL prompt → CSL (preview) → Validate → Run → CAD system operates and generates geometry in a remote control mode via the API + Diagnostics
- Editor-first (VS Code/Cursor like extension), upgrade to standalone app as needed
- Quick fixes for units/queries; capability-aware hints and fallbacks and maintains sync of history tree and units and other global settings with the CAD system via the API

## MVP 
- VS Code extension
  - CSL Language Server (LSP):
    - Validation via `CSL_v1_2/csl_v1_2_schema.json`
    - Hover docs from `CSL_GLOSSARY.md`
    - Code actions: add units, strengthen queries, insert headers
  - Commands:
    - “Generate CSL from Natural Language” (LLM)
    - “Validate CSL” (schema)
    - “Run with sselected CAD system” (exec backend; dry‑run fallback)
  - Artifact panel (webview): Three.js for STL/3MF; thumbnails + logs
- Agent service (Python/FastAPI)
  - NL → CSL → IR pipeline with retries/auto‑fixes
  - Capability planning using backend `get_capabilities()`
  - Execute via Fusion or alternate CAD backend (`triple_lindy/transpilers/fusion360_backend.py`)
  - Persist run outputs under `out/run_<ts>/`
- CI
  - Keep schema validation (already present)
  - Add extension lint/build job

## v1.0 
- Backends
  - Onshape: FeatureScript/API translation + export
  - FreeCAD: Python headless path
  - SolidWorks: Windows host shim (deferred if needed)
- Templates & recipes
  - Common part families (brackets/plates/shafts), threads/holes, patterns, sheet workflows
- Determinism guardrails
  - Auto‑tagging; query strengthening; ambiguous selection failure with guidance
- Project context
  - Param sheets, prior CSL, geometry snippets
- Billing with standard pricing plans to support paying for LLM and AI costs as well as high end Cerberas accelerated engineering option
- Stretch goal is implementation of lossless .cslx CAD export 

## v2.0 (Post‑PMF)
- Standalone desktop (Tauri/Electron) embedding Monaco + multi‑pane CAD UX (model tree, params, joints inspector)
- Rust microservices for heavy geometry/IR transforms; gRPC/Protobuf shared schemas
- Team features: artifact registry, role‑based access, SSO

## Architecture
- Editor Extension (TypeScript)
  - CSL LSP (schema validation, completions, hovers, actions)
  - Webview panel for artifacts (Three.js)
  - Commands → local HTTP calls to Agent
- Agent (Python/FastAPI)
  - Prompting → CSL generation (OpenAI/Anthropic SDKs, pluggable)
  - Validator (jsonschema) + auto‑fix
  - Capability planner (reads backend capabilities JSON)
  - Executor → Fusion backend (local add‑in or dry‑run)
  - Storage: `out/` files + optional SQLite for runs
- Future Services (Rust)
  - Geometry ops/query engine; long‑running planners
  - Expose via gRPC; Python/TS clients

## Open Source Leverage
- VS Code extension scaffolding (`yo code`, languageclient)
- JSON schema tooling (vscode-json-languageservice)
- Three.js loaders/viewers
- CAD API samples (Onshape FeatureScript, FreeCAD scripts)

## Security & Compliance
- Local‑first execution; opt‑in cloud
- Token management for CAD APIs (Fusion PAT, Onshape keys) using OS keychain
- Redaction for logs; usage telemetry with opt‑out

## Pricing/Packaging (tentative)
- Free: single backend, community support
- Pro: multi‑backend, team collaboration, artifact history
- Enterprise: on‑prem adapters, SSO, dedicated support

## Milestones & Acceptance
- MVP acceptance: generate, validate, and run CSL for three golden prompts; artifacts render in panel; CI green
- v1.0 acceptance: Onshape + FreeCAD adapters; 10 recipe templates; determinism guardrails enabled

## Risks & Mitigations
- CAD API differences → robust capability planner; fallbacks documented
- Topological drift → lineage + tagging + query strengthening
- Performance hotspots → move to Rust services post‑PMF

## Next Steps
- Scaffold extension + agent service
- Wire one end‑to‑end NL → CSL → Fusion demo with artifacts
- Add 5 golden prompts and regression tests
