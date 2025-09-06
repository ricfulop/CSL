// Create a box, then apply chamfer using distance/angle if supported, else equal-distance
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

  const ch = root.features.chamferFeatures;
  const edges = a.core.ObjectCollection.create();
  for (let i = 0; i < body.edges.count; i++) edges.add(body.edges.item(i));

  let def;
  if (ch.createDistanceAndAngleChamferDefinition) {
    def = ch.createDistanceAndAngleChamferDefinition(
      edges,
      a.core.ValueInput.createByReal(0.1),
      a.core.ValueInput.createByReal(Math.PI / 4.0), // 45 deg
      false
    );
  } else if (ch.createTwoDistancesChamferDefinition) {
    def = ch.createTwoDistancesChamferDefinition(
      edges,
      a.core.ValueInput.createByReal(0.1),
      a.core.ValueInput.createByReal(0.15),
      false
    );
  } else {
    def = ch.createEqualDistanceChamferDefinition(edges, a.core.ValueInput.createByReal(0.1), false);
  }
  ch.add(def);
  a.log?.("Applied chamfer");
})();




