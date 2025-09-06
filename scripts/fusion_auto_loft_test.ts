// Create two circular profiles and loft with continuity/orientation hints
(async () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const a: any = (globalThis as any).adsk;
  const app = a?.core?.Application?.get?.();
  const design = app?.activeProduct;
  if (!design) { a?.log?.("No design"); return; }
  const root = design.rootComponent;

  // Sketch 1 on XY
  let sk = root.sketches.add(root.xYConstructionPlane);
  sk.sketchCurves.sketchCircles.addByCenterRadius(a.core.Point3D.create(0,0,0), 0.3);
  const p1 = sk.profiles.item(0);

  // Sketch 2 on offset plane
  const plane = root.constructionPlanes.addOffset(root.xYConstructionPlane, a.core.ValueInput.createByReal(1));
  sk = root.sketches.add(plane);
  sk.sketchCurves.sketchCircles.addByCenterRadius(a.core.Point3D.create(0,0,0), 0.5);
  const p2 = sk.profiles.item(0);

  const lf = root.features.loftFeatures;
  const input = lf.createInput(a.fusion.FeatureOperations.NewBodyFeatureOperation);
  const sections = input.loftSections;
  sections.add(p1);
  sections.add(p2);

  // Orientation/continuity best-effort
  try {
    if (input.hasOwnProperty('isSolid')) input.isSolid = true;
    if (input.hasOwnProperty('centerLineOrRails')) input.centerLineOrRails = false;
    const cont = (a.fusion.SurfaceContinuityTypes || a.fusion.ContinuityTypes || a.fusion.LoftSectionContinuityTypes);
    if (cont && input.loftSections && input.loftSections.count >= 2) {
      // Set continuity on first/last if possible
      const cG1 = cont.G1Tangency || cont.G1 || cont.Tangency;
      try { input.loftSections.item(0).continuity = cG1; } catch {}
      try { input.loftSections.item(1).continuity = cG1; } catch {}
    }
  } catch {}

  lf.add(input);
  a.log?.("Loft created");
})();




