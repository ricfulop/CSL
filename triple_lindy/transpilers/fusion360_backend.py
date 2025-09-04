"""Fusion 360 Backend Adapter (stub)

Implements the minimal BackendAdapter shape for Fusion-first development.
If Fusion's `adsk` modules are unavailable, methods will no-op or print guidance.
"""
from __future__ import annotations

import os
from typing import Dict, List, Any


class FusionBackend:
    """Minimal Fusion backend adapter stub."""

    def __init__(self, session_config: Dict[str, Any] | None = None) -> None:
        self.session_config = session_config or {}
        self._fusion_available = self._check_fusion()

    def _check_fusion(self) -> bool:
        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore
            _ = adsk.core  # silence lints
            _ = adsk.fusion
            return True
        except Exception:
            return False

    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "csl": "1.1",
            "backend": "fusion",
            "supports": {
                "brep": True,
                "mesh": True,
                "params": True,
                "queries": True,
                "features": {
                    "extrude": True,
                    "fillet": True,
                    "hole": True,
                    "loft": True,
                    "shell": True,
                    "draft": True,
                    "pattern": ["linear", "circular", "rect"],
                    "boolean": ["union", "subtract", "intersect"],
                    "thread_cosmetic": True,
                    "thread_modeled": True,
                },
                "export": ["STEP", "STL", "IGES", "3MF", "OBJ"],
                "thumbnail": {"enabled": True, "views": ["iso", "top", "front", "right"], "styles": ["shaded", "wireframe"]},
            },
        }

    def open_session(self, session_config: Dict[str, Any] | None = None) -> None:
        if session_config:
            self.session_config.update(session_config)
        # Load APS env if provided (for future cloud ops)
        self.session_config.setdefault("aps_client_id", os.getenv("APS_CLIENT_ID"))
        self.session_config.setdefault("aps_client_secret", os.getenv("APS_CLIENT_SECRET"))
        if not self._fusion_available:
            print("[FusionBackend] Fusion API not available in this environment; running in dry-run mode.")

    def close_session(self) -> None:
        return

    def realize(self, csl_ir: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a minimal subset: create extrude from first sketch profile, add holes/fillets if present.

        Stub: when Fusion is not available, return a plausible mapping.
        """
        mapping: Dict[str, str] = {}
        if not self._fusion_available:
            # Return a minimal stable mapping for CI/doc examples.
            for feat in csl_ir.get("features", []):
                if isinstance(feat, dict) and "id" in feat:
                    mapping[feat["id"]] = f"fusion:{feat['id']}"
            return mapping

        # Real implementation would use adsk.core/adsk.fusion to construct design
        # and keep a mapping from CSL IDs to Fusion entity tokens.
        # TODO: implement extrude/hole/fillet + export/thumbnail
        return mapping

    def export(self, export_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run export: {export_ops}")
            return
        # TODO: use ExportManager to perform requested exports
        return

    def thumbnail(self, thumb_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run thumbnail: {thumb_ops}")
            return
        # TODO: capture viewport images according to ops
        return


