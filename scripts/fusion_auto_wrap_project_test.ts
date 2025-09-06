// Wrap/Project quick validation for Automation ScriptJob
(async () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const a: any = (globalThis as any).adsk;
  const app = a?.core?.Application?.get?.();
  const design = app?.activeProduct;
  if (!design) { a?.log?.("No design"); return; }
  const root = design.rootComponent;
  a?.log?.(`Fusion Version: ${app?.version}`);

  // Base cylinder target
  const sk = root.sketches.add(root.xYConstructionPlane);
  sk.sketchCurves.sketchCircles.addByCenterRadius(a.core.Point3D.create(0, 0, 0), 1.0);
  const prof = sk.profiles.item(0);
  const ext = root.features.extrudeFeatures;
  const exIn = ext.createInput(prof, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  exIn.setDistanceExtent(false, a.core.ValueInput.createByReal(1.0));
  const body = ext.add(exIn).bodies.item(0);

  // Sketch to wrap: short line on XZ
  const sk2 = root.sketches.add(root.xZConstructionPlane);
  sk2.sketchCurves.sketchLines.addByTwoPoints(a.core.Point3D.create(-0.5, 0, 0), a.core.Point3D.create(0.5, 0, 0));

  // Emboss/Wrap where exposed
  const emb = root.features.embossFeatures;
  if (emb) {
    try {
      const faces = a.core.ObjectCollection.create();
      // pick a lateral face if possible
      let pick = body.faces.item(0);
      for (let i = 0; i < body.faces.count; i++) {
        const f = body.faces.item(i);
        const g = f.geometry;
        if (g && typeof g.radius === 'number') { pick = f; break; }
      }
      faces.add(pick);
      let ok = false;
      // Try createInput first
      if (emb.createInput) {
        const ein = emb.createInput(sk2, faces, true);
        ein.depth = a.core.ValueInput.createByReal(0.05);
        const ef = emb.add(ein);
        a?.log?.(`wrap_feature=${ef?.entityToken || 'n/a'}`);
        ok = true;
      }
      if (!ok && emb.createWrapFeatureInput) {
        const ein = emb.createWrapFeatureInput(sk2, faces, a.core.ValueInput.createByReal(0.05), true);
        const ef = emb.add(ein);
        a?.log?.(`wrap_feature=${ef?.entityToken || 'n/a'}`);
        ok = true;
      }
      if (!ok) a?.log?.('wrap_unavailable');
    } catch (e) {
      a?.log?.(`wrap_error=${String(e)}`);
    }
  } else {
    a?.log?.('emboss_api_unavailable');
  }

  a?.log?.('wrap_project_test_complete');
})();


