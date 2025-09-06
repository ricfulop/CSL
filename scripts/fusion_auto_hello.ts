// Logs environment and runs a couple of selection/queries in Fusion ScriptJob
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
  // Create a 20x10 rectangle and extrude 5
  const sk = root.sketches.add(root.xYConstructionPlane);
  const lines = sk.sketchCurves.sketchLines;
  const p0 = a.core.Point3D.create(0, 0, 0);
  const p1 = a.core.Point3D.create(2, 1, 0);
  lines.addTwoPointRectangle(p0, p1);
  const profile = sk.profiles.item(0);
  const ext = root.features.extrudeFeatures;
  const extIn = ext.createInput(profile, a.fusion.FeatureOperations.NewBodyFeatureOperation);
  extIn.setDistanceExtent(false, a.core.ValueInput.createByReal(0.5));
  const body = ext.add(extIn).bodies.item(0);
  // Fillet all external edges so we have a feature to query by lineage
  const fil = root.features.filletFeatures;
  const ec = a.core.ObjectCollection.create();
  for (let i = 0; i < body.edges.count; i++) ec.add(body.edges.item(i));
  const def = fil.createConstantRadiusFilletDefinition(ec, a.core.ValueInput.createByReal(0.1), false);
  const f = fil.add(def);
  a?.log?.(`Created fillet feature: ${f?.entityToken || 'n/a'}`);
  // Report counts
  a?.log?.(`Bodies: ${root.bRepBodies.count}, Faces: ${body.faces.count}, Edges: ${body.edges.count}`);
})();

// Minimal Fusion Automation API (beta) script
// Intended to run in the Fusion Automation sandbox (TypeScript)

export default async function main(params: Record<string, unknown>) {
  // The beta runtime typically injects Fusion API bindings; here we just log.
  // Replace with actual Fusion API calls as docs solidify.
  const now = new Date().toISOString();
  const name = String(params?.name || "CSL Hello");
  console.log(`[Fusion Automation Hello] ${name} @ ${now}`);
  // Return an object that the service can store alongside logs
  return { ok: true, name, timestamp: now };
}


