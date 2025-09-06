// Create a path and a profile; sweep with orientation variants
(async () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const a: any = (globalThis as any).adsk;
  const app = a?.core?.Application?.get?.();
  const design = app?.activeProduct;
  if (!design) { a?.log?.("No design"); return; }
  const root = design.rootComponent;

  // Path sketch
  let sk = root.sketches.add(root.xYConstructionPlane);
  const lines = sk.sketchCurves.sketchLines;
  const p0 = a.core.Point3D.create(0,0,0);
  const p1 = a.core.Point3D.create(2,0,0);
  const p2 = a.core.Point3D.create(2,1,0);
  lines.addByTwoPoints(p0, p1);
  lines.addByTwoPoints(p1, p2);
  const path = sk.profiles.item(0) ? sk.sketchCurves.asCurve3D() : sk.sketchCurves.sketchLines;

  // Profile sketch offset
  const plane = root.constructionPlanes.addOffset(root.xYConstructionPlane, a.core.ValueInput.createByReal(0.01));
  sk = root.sketches.add(plane);
  const circ = sk.sketchCurves.sketchCircles.addByCenterRadius(a.core.Point3D.create(0,0,0), 0.05);
  const profile = sk.profiles.item(0);

  const sw = root.features.sweepFeatures;
  const input = sw.createInput(profile, sk.profiles.item(0) || profile, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  try {
    const ori = a.fusion.SweepOrientationTypes || {};
    input.orientation = ori.PathOrientationType || ori.GuideRailOrientationType || ori.PerpendicularOrientationType;
  } catch {}
  sw.add(input);
  a.log?.("Sweep created");
})();


