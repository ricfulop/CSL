// Fusion Automation script to create a tiny sheet metal base, unfold, then refold
(async () => {
  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const a: any = (globalThis as any).adsk;
    if (!a) {
      console.log("adsk API not available");
      return;
    }
    const app = a.core?.Application?.get?.();
    const design = app?.activeProduct;
    if (!design || design.classType?.() !== "adsk::fusion::Design") {
      a.log?.("No active Fusion design; creating sketch-less operations may fail");
    }

    const root = design.rootComponent;
    const sk = root.sketches.add(root.xYConstructionPlane);
    const lines = sk.sketchCurves.sketchLines;
    const p0 = a.core.Point3D.create(0, 0, 0);
    const p1 = a.core.Point3D.create(1, 1, 0); // 1 cm square
    lines.addTwoPointRectangle(p0, p1);
    const profile = sk.profiles.count > 0 ? sk.profiles.item(0) : null;
    if (!profile) {
      a.log?.("No profile created");
      return;
    }

    const feats = root.features;
    const smFeats = (feats as any).sheetMetalFeatures;
    if (!smFeats || !smFeats.baseFeatures) {
      a.log?.("SheetMetal features not available in this Fusion version");
      return;
    }
    const th = a.core.ValueInput.createByReal(0.15); // 1.5 mm -> 0.15 cm
    const bfIn = smFeats.baseFeatures.createInput(profile, th);
    const bf = smFeats.baseFeatures.add(bfIn);
    a.log?.("Created sheet metal base feature");

    const bodies = bf.bodies || root.bRepBodies;
    const body = bodies && bodies.count > 0 ? bodies.item(0) : null;
    const face = body && body.faces && body.faces.count > 0 ? body.faces.item(0) : null;
    const unfoldFeats = feats.unfoldFeatures;
    const refoldFeats = feats.refoldFeatures;
    if (!unfoldFeats || !refoldFeats) {
      a.log?.("Unfold/Refold features are not available");
      return;
    }
    const bends = a.core.ObjectCollection.create();
    let uIn;
    try {
      uIn = unfoldFeats.createInput(face, bends, true);
    } catch (e) {
      try {
        uIn = unfoldFeats.createInput(face, bends);
      } catch {
        uIn = undefined;
      }
    }
    const uf = uIn ? unfoldFeats.add(uIn) : null;
    if (!uf) {
      a.log?.("Failed to create unfold feature");
      return;
    }
    a.log?.("Unfolded sheet metal");

    let rf;
    try {
      const rIn = refoldFeats.createInput?.();
      rf = rIn ? refoldFeats.add(rIn) : refoldFeats.add();
    } catch (e) {
      try {
        rf = refoldFeats.add();
      } catch {
        rf = undefined;
      }
    }
    if (!rf) {
      a.log?.("Failed to create refold feature");
      return;
    }
    a.log?.("Refolded sheet metal");
  } catch (e) {
    console.log("Error:", e);
  }
})();


