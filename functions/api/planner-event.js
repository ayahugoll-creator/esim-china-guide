// Receives planner form submission events.
// POST body: { nationality, concern, hotspot, duration, esim, source }
// Logs to console (visible in `wrangler tail` / Cloudflare logs).

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const body = await request.json();

    const event = {
      type: "planner_submit",
      timestamp: new Date().toISOString(),
      nationality: body.nationality || "unknown",
      concern: body.concern || "unknown",
      hotspot: body.hotspot || "unknown",
      duration: body.duration || "unknown",
      esim: body.esim || "unknown",
      source: body.source || "unknown",
      userAgent: request.headers.get("user-agent") || "",
      country: request.headers.get("cf-ipcountry") || "XX"
    };

    // Log to Cloudflare request logs (visible in dashboard analytics)
    console.log(JSON.stringify(event));

    // If KV namespace is bound as `PLANNER_EVENTS`, store last 1000 events
    if (env && env.PLANNER_EVENTS) {
      const key = `event:${Date.now()}:${Math.random().toString(36).slice(2, 8)}`;
      await env.PLANNER_EVENTS.put(key, JSON.stringify(event), {
        expirationTtl: 60 * 60 * 24 * 90 // 90 days
      });
    }

    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { "content-type": "application/json", "access-control-allow-origin": "*" }
    });
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: e.message }), {
      status: 400,
      headers: { "content-type": "application/json", "access-control-allow-origin": "*" }
    });
  }
}

// Handle OPTIONS for CORS preflight
export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      "access-control-allow-origin": "*",
      "access-control-allow-methods": "POST, OPTIONS",
      "access-control-allow-headers": "content-type"
    }
  });
}
