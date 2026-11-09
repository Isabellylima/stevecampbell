/**
 * Steve Campbell Associates — Cloudflare Worker
 *
 * Serves the static site from /public and handles one API route:
 *   POST /api/subscribe  → submits the newsletter sign-up to a HubSpot form
 *                          (HubSpot Forms API v3 — no API key required)
 *
 * Variables (Cloudflare: Worker → Settings → Variables and Secrets):
 *   HUBSPOT_PORTAL_ID      (required)  HubSpot account ID ("Hub ID")
 *   HUBSPOT_FORM_ID        (required)  form GUID for English sign-ups
 *   HUBSPOT_FORM_ID_PT     (optional)  form GUID for Portuguese sign-ups (falls back to HUBSPOT_FORM_ID)
 *   HUBSPOT_SUBSCRIPTION_ID (optional) subscription type ID, if the form uses GDPR consent options
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

const CONSENT_TEXT = {
  en: 'I agree to receive emails from Steve Campbell Associates and accept the privacy notice.',
  pt: 'Aceito receber e-mails da Steve Campbell Associates e li a política de privacidade.',
};

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
  const source = String(data.source || '/').slice(0, 200);

  if (!EMAIL_RE.test(email) || email.length > 254) return json({ error: 'Invalid email' }, 400);
  if (!data.consent) return json({ error: 'Consent required' }, 400);

  const portal = env.HUBSPOT_PORTAL_ID;
  const form = (lang === 'pt' && env.HUBSPOT_FORM_ID_PT) || env.HUBSPOT_FORM_ID;
  if (!portal || !form) return json({ error: 'Newsletter not configured' }, 503);

  const fields = [{ objectTypeId: '0-1', name: 'email', value: email }];
  if (name) fields.push({ objectTypeId: '0-1', name: 'firstname', value: name });
  if (company) fields.push({ objectTypeId: '0-1', name: 'company', value: company });

  const payload = {
    fields,
    context: {
      pageUri: new URL(source, 'https://stevecampbellassociates.com').toString(),
      pageName: lang === 'pt' ? 'Newsletter (PT)' : 'Newsletter (EN)',
    },
  };
  const ip = request.headers.get('cf-connecting-ip');
  if (ip) payload.context.ipAddress = ip;

  if (env.HUBSPOT_SUBSCRIPTION_ID) {
    payload.legalConsentOptions = {
      consent: {
        consentToProcess: true,
        text: CONSENT_TEXT[lang],
        communications: [{ value: true, subscriptionTypeId: Number(env.HUBSPOT_SUBSCRIPTION_ID), text: CONSENT_TEXT[lang] }],
      },
    };
  }

  const res = await fetch(
    `https://api.hsforms.com/submissions/v3/integration/submit/${encodeURIComponent(portal)}/${encodeURIComponent(form)}`,
    { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(payload) }
  );

  if (!res.ok) {
    console.error('HubSpot error', res.status, await res.text());
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
