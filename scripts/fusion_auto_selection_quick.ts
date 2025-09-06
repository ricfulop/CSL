// Quick selection metrics: largest face, outer loop edges, tag count
(async () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const a: any = (globalThis as any).adsk;
  const app = a?.core?.Application?.get?.();
  const design = app?.activeProduct;
  if (!design) { a?.log?.("No design"); return; }
  const root = design.rootComponent;

  // Create a 1x1 rectangle and extrude 0.2
  const sk = root.sketches.add(root.xYConstructionPlane);
  const p0 = a.core.Point3D.create(0, 0, 0);
  const p1 = a.core.Point3D.create(1, 1, 0);
  sk.sketchCurves.sketchLines.addTwoPointRectangle(p0, p1);
  const prof = sk.profiles.item(0);
  const ext = root.features.extrudeFeatures;
  const exIn = ext.createInput(prof, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  exIn.setDistanceExtent(false, a.core.ValueInput.createByReal(0.2));
  const body = ext.add(exIn).bodies.item(0);

  // Largest face by area
  let largest: any = null; let maxA = -1;
  for (let i = 0; i < body.faces.count; i++) {
    const f = body.faces.item(i);
    const ar = Number(f?.area ?? 0);
    if (ar > maxA) { maxA = ar; largest = f; }
  }
  a?.log?.(`largest_face_token=${largest?.entityToken || 'n/a'} area=${maxA.toFixed(6)}`);

  // Outer loop edges count for largest face
  let outerEdges = 0;
  try {
    const loops = largest?.loops;
    for (let li = 0; li < (loops?.count ?? 0); li++) {
      const lp = loops.item(li);
      if (lp?.isOuter) { outerEdges = lp.edges?.count ?? 0; break; }
    }
  } catch {}
  a?.log?.(`outer_loop_edges_count=${outerEdges}`);

  // Tag outer faces with csl_tag=external and count
  let tagged = 0;
  try {
    for (let i = 0; i < body.faces.count; i++) {
      const f = body.faces.item(i);
      const loops = f.loops; let hasOuter = false;
      for (let li = 0; li < loops.count; li++) { if (loops.item(li)?.isOuter) { hasOuter = true; break; } }
      if (hasOuter) { f.attributes?.add?.('CSL', 'csl_tag', 'external'); }
      const attr = f.attributes?.itemByName?.('CSL', 'csl_tag');
      if (attr && String(attr.value) === 'external') tagged++;
    }
  } catch {}
  a?.log?.(`by_tag_external_faces=${tagged}`);

  a?.log?.('selection_quick_complete');
})();


