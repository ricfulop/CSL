// Selection/Queries capability probe inside Fusion ScriptJob (TypeScript)
// Creates a box and a cylinder; logs largest face, tangent-connected flood size,
// cylindrical faces by radius/axis, loop edges count of outer loop, and a simple tag/attribute test.
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
  a?.log?.(`Fusion Version: ${app?.version}`);

  // Helpers
  const vi = a.core.ValueInput;
  const V = (x: number) => vi.createByReal(x);

  // Create box 2x1x0.5
  const sk = root.sketches.add(root.xYConstructionPlane);
  const p0 = a.core.Point3D.create(0, 0, 0);
  const p1 = a.core.Point3D.create(2, 1, 0);
  sk.sketchCurves.sketchLines.addTwoPointRectangle(p0, p1);
  const prof = sk.profiles.item(0);
  const ext = root.features.extrudeFeatures;
  const exIn = ext.createInput(prof, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  exIn.setDistanceExtent(false, V(0.5));
  const boxBody = ext.add(exIn).bodies.item(0);

  // Create cylinder: circle r=0.25 extrude height 1 along +Z
  const sk2 = root.sketches.add(root.xYConstructionPlane);
  sk2.sketchCurves.sketchCircles.addByCenterRadius(a.core.Point3D.create(3, 0.5, 0), 0.25);
  const prof2 = sk2.profiles.item(0);
  const ex2 = root.features.extrudeFeatures;
  const ex2In = ex2.createInput(prof2, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  ex2In.setDistanceExtent(false, V(1));
  const cylBody = ex2.add(ex2In).bodies.item(0);

  a?.log?.(`Bodies: box=${boxBody?.entityToken}, cyl=${cylBody?.entityToken}`);

  // Largest face by area across both bodies
  let largestFace = null as any;
  let largestArea = -1;
  const bodies = [boxBody, cylBody];
  for (const b of bodies) {
    for (let i = 0; i < b?.faces?.count; i++) {
      const f = b.faces.item(i);
      try {
        const ar = Number(f?.area ?? 0);
        if (ar > largestArea) {
          largestArea = ar;
          largestFace = f;
        }
      } catch {}
    }
  }
  a?.log?.(`largest_face_token=${largestFace?.entityToken || 'n/a'} area=${largestArea.toFixed(5)}`);

  // Tangent-connected flood starting from a random face on the box (expect small set)
  const seed = boxBody.faces.item(0);
  const tolDeg = 5.0;
  const toRad = (d: number) => (d / 180.0) * Math.PI;
  const visited = new Set<string>();
  const q: any[] = [];
  q.push(seed); visited.add(String(seed?.entityToken));
  while (q.length) {
    const f = q.shift();
    try {
      for (let ei = 0; ei < f.edges.count; ei++) {
        const e = f.edges.item(ei);
        for (let fi = 0; fi < e.faces.count; fi++) {
          const nf = e.faces.item(fi);
          const tok = String(nf?.entityToken);
          if (visited.has(tok)) continue;
          const ang = Math.abs(f.getAngleTo?.(nf) ?? 0);
          if (ang <= toRad(tolDeg)) {
            visited.add(tok); q.push(nf);
          }
        }
      }
    } catch {}
  }
  a?.log?.(`tangent_connected_count=${visited.size}`);

  // Cylindrical faces by radius≈ and axis≈Z
  let cylMatches = 0;
  for (let i = 0; i < cylBody.faces.count; i++) {
    const f = cylBody.faces.item(i);
    const g = f.geometry;
    const r = g?.radius;
    // radius should be ~0.25
    if (typeof r === 'number' && Math.abs(r - 0.25) < 1e-6) {
      // axis parallel to Z if present
      let isZ = true;
      try {
        const ax = g.axis || g.direction || g.axisVector;
        if (ax) {
          const dot = Math.abs(Number(ax?.z ?? 0));
          isZ = dot > 0.99;
        }
      } catch {}
      if (isZ) cylMatches++;
    }
  }
  a?.log?.(`cylindrical_faces_matches=${cylMatches}`);

  // Loop edges of a large planar face (outer loop only)
  let loopEdges = 0;
  try {
    const f0 = largestFace;
    const loops = f0?.loops;
    for (let li = 0; li < loops?.count; li++) {
      const lp = loops.item(li);
      const isOuter = Boolean(lp?.isOuter ?? false);
      if (!isOuter) continue;
      const eds = lp.edges;
      loopEdges = eds?.count ?? 0;
    }
  } catch {}
  a?.log?.(`outer_loop_edges_count=${loopEdges}`);

  // Simple tag via attributes: tag all outer faces of box with csl_tag="external"
  try {
    for (let i = 0; i < boxBody.faces.count; i++) {
      const f = boxBody.faces.item(i);
      const loops = f.loops;
      let hasOuter = false;
      for (let li = 0; li < loops.count; li++) {
        const lp = loops.item(li);
        if (lp?.isOuter) { hasOuter = true; break; }
      }
      if (hasOuter) {
        f.attributes?.add?.('CSL', 'csl_tag', 'external');
      }
    }
    // Count faces with tag
    let tagged = 0;
    for (let i = 0; i < boxBody.faces.count; i++) {
      const f = boxBody.faces.item(i);
      const attr = f.attributes?.itemByName?.('CSL', 'csl_tag');
      if (attr && String(attr.value) === 'external') tagged++;
    }
    a?.log?.(`by_tag_external_faces=${tagged}`);
  } catch {}

  a?.log?.('selection_queries_test_complete');
})();


