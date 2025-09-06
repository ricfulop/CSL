// Create a box, then apply fillet with feature-level uniform setback if possible
(async () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const a: any = (globalThis as any).adsk;
  const app = a?.core?.Application?.get?.();
  const design = app?.activeProduct;
  if (!design) {
    a?.log?.("No design");
    return;
  }
  const root = design.rootComponent;
  // Create a 10x10 rectangle and extrude 10
  const sk = root.sketches.add(root.xYConstructionPlane);
  const lines = sk.sketchCurves.sketchLines;
  const p0 = a.core.Point3D.create(0, 0, 0);
  const p1 = a.core.Point3D.create(1, 1, 0);
  lines.addTwoPointRectangle(p0, p1);
  const profile = sk.profiles.item(0);
  const ext = root.features.extrudeFeatures;
  const extIn = ext.createInput(profile, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  extIn.setDistanceExtent(false, a.core.ValueInput.createByReal(1));
  const body = ext.add(extIn).bodies.item(0);
  // Apply constant fillet with uniform setback if API supports
  const fil = root.features.filletFeatures;
  const edges = a.core.ObjectCollection.create();
  for (let i = 0; i < body.edges.count; i++) edges.add(body.edges.item(i));
  if (fil.createSetbackFilletDefinition) {
    const sdef = fil.createSetbackFilletDefinition(edges);
    // Set same setback for all unique vertices
    const seen = new Set<string>();
    for (let i = 0; i < body.vertices.count; i++) {
      const v = body.vertices.item(i);
      const id = String(v.entityToken || i);
      if (seen.has(id)) continue;
      seen.add(id);
      sdef.setSetbackDistance(v, a.core.ValueInput.createByReal(0.05)); // 0.5 mm
    }
    fil.add(sdef);
    a.log?.("Applied setback fillet");
  } else {
    const ec = a.core.ObjectCollection.create();
    for (let i = 0; i < body.edges.count; i++) ec.add(body.edges.item(i));
    const def = fil.createConstantRadiusFilletDefinition(ec, a.core.ValueInput.createByReal(0.2), false);
    fil.add(def);
    a.log?.("Applied constant fillet");
  }
})();




