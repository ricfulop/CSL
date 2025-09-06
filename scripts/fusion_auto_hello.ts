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


