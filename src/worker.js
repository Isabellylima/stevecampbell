/**
 * Steve Campbell Associates — Cloudflare Worker
 *
 * Serves the static site from /public and handles one API route:
 *   POST /api/subscribe  → adds a newsletter subscriber to MailerLite
 *
 * Secrets / variables (set in Cloudflare: Worker → Settings → Variables and Secrets):
 *   MAILERLITE_API_KEY   (secret, required)  MailerLite → Integrations → API
 *   MAILERLITE_GROUP_EN  (optional)          group ID for English-language subscribers
 *   MAILERLITE_GROUP_PT  (optional)          group ID for Portuguese-language subscribers
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}

async function readBody(request) {
  const type = request.headers.get('content-type') || '';
  if (type.includes('application/json')) return request.json();
  const form = await request.formData();
  return Object.fromEntries(form.entries());
}

async function subscribe(request, env) {
  if (request.method !== 'POST') return json({ error: 'Method not allowed' }, 405);

  let data;
  try {
    data = await readBody(request);
  } catch {
    return json({ error: 'Invalid request' }, 400);
  }

  // Honeypot: real visitors never fill this hidden field
  if (data.website) return json({ ok: true });

  const email = String(data.email || '').trim().toLowerCase();
  const name = String(data.name || '').trim().slice(0, 120);
  const company = String(data.company || '').trim().slice(0, 160);
  const lang = data.lang === 'pt' ? 'pt' : 'en';

  if (!EMAIL_RE.test(email) || email.length > 254) return json({ error: 'Invalid email' }, 400);
  if (!data.consent) return json({ error: 'Consent required' }, 400);
  if (!env.MAILERLITE_API_KEY) return json({ error: 'Newsletter not configured' }, 503);

  const group = lang === 'pt' ? env.MAILERLITE_GROUP_PT : env.MAILERLITE_GROUP_EN;
  const payload = { email, fields: { name, company } };
  if (group) payload.groups = [String(group)];

  const res = await fetch('https://connect.mailerlite.com/api/subscribers', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      accept: 'application/json',
      authorization: `Bearer ${env.MAILERLITE_API_KEY}`,
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    console.error('MailerLite error', res.status, await res.text());
    return json({ error: 'Subscription failed' }, 502);
  }
  return json({ ok: true });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // This Worker only runs for /api/* (see run_worker_first in wrangler.jsonc);
    // everything else is served straight from /public with _redirects and _headers applied.
    if (url.pathname === '/api/subscribe') return subscribe(request, env);
    if (url.pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);

    return env.ASSETS.fetch(request);
  },
};
