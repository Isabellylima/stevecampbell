/**
 * Steve Campbell Associates — Cloudflare Worker
 *
 * Serves the static site from /public and handles two API routes, both sent to
 * HubSpot forms through the HubSpot Forms API v3 (no API key needed):
 *   POST /api/subscribe  → newsletter sign-up (footer box and pop-up)
 *   POST /api/contact    → contact form enquiries
 *
 * Variables (Cloudflare: Worker → Settings → Variables and Secrets):
 *   HUBSPOT_PORTAL_ID        (required)  HubSpot account ID ("Hub ID")
 *   HUBSPOT_FORM_ID          (required)  newsletter form GUID (English)
 *   HUBSPOT_FORM_ID_PT       (optional)  newsletter form GUID (Portuguese) — falls back to HUBSPOT_FORM_ID
 *   HUBSPOT_CONTACT_FORM_ID  (required for /api/contact) contact form GUID
 *   HUBSPOT_SUBSCRIPTION_ID  (optional)  marketing subscription type ID, if the newsletter form uses GDPR consent options
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const SITE = 'https://stevecampbellassociates.com';

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

const clean = (v, max) => String(v || '').trim().slice(0, max);

function contextFor(request, data, pageName) {
  const ctx = {
    pageUri: new URL(clean(data.source, 200) || '/', SITE).toString(),
    pageName,
  };
  const ip = request.headers.get('cf-connecting-ip');
  if (ip) ctx.ipAddress = ip;
  return ctx;
}

async function submitToHubSpot(env, formId, payload) {
  const url = `https://api.hsforms.com/submissions/v3/integration/submit/${encodeURIComponent(env.HUBSPOT_PORTAL_ID)}/${encodeURIComponent(formId)}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    console.error('HubSpot error', formId, res.status, await res.text());
    return false;
  }
  return true;
}

async function parse(request) {
  if (request.method !== 'POST') return { error: json({ error: 'Method not allowed' }, 405) };
  let data;
  try {
    data = await readBody(request);
  } catch {
    return { error: json({ error: 'Invalid request' }, 400) };
  }
  // Honeypot: real visitors never fill this hidden field
  if (data.website) return { error: json({ ok: true }) };
  const email = clean(data.email, 254).toLowerCase();
  if (!EMAIL_RE.test(email)) return { error: json({ error: 'Invalid email' }, 400) };
  return { data, email, lang: data.lang === 'pt' ? 'pt' : 'en' };
}

async function subscribe(request, env) {
  const p = await parse(request);
  if (p.error) return p.error;
  const { data, email, lang } = p;
  if (!data.consent) return json({ error: 'Consent required' }, 400);

  const form = (lang === 'pt' && env.HUBSPOT_FORM_ID_PT) || env.HUBSPOT_FORM_ID;
  if (!env.HUBSPOT_PORTAL_ID || !form) return json({ error: 'Not configured' }, 503);

  const name = clean(data.name, 120);
  const company = clean(data.company, 160);
  const fields = [{ objectTypeId: '0-1', name: 'email', value: email }];
  if (name) fields.push({ objectTypeId: '0-1', name: 'firstname', value: name });
  if (company) fields.push({ objectTypeId: '0-1', name: 'company', value: company });

  const where = data.placement === 'popup' ? 'pop-up' : 'footer';
  const payload = {
    fields,
    context: contextFor(request, data, `Newsletter ${where} (${lang.toUpperCase()})`),
  };
  if (env.HUBSPOT_SUBSCRIPTION_ID) {
    payload.legalConsentOptions = {
      consent: {
        consentToProcess: true,
        text: CONSENT_TEXT[lang],
        communications: [{ value: true, subscriptionTypeId: Number(env.HUBSPOT_SUBSCRIPTION_ID), text: CONSENT_TEXT[lang] }],
      },
    };
  }
  return (await submitToHubSpot(env, form, payload)) ? json({ ok: true }) : json({ error: 'Subscription failed' }, 502);
}

async function contact(request, env) {
  const p = await parse(request);
  if (p.error) return p.error;
  const { data, email, lang } = p;

  const name = clean(data.name, 120);
  const message = clean(data.message, 5000);
  if (!name || !message) return json({ error: 'Missing fields' }, 400);
  if (!env.HUBSPOT_PORTAL_ID || !env.HUBSPOT_CONTACT_FORM_ID) return json({ error: 'Not configured' }, 503);

  const topic = clean(data.topic, 80);
  const fields = [
    { objectTypeId: '0-1', name: 'email', value: email },
    { objectTypeId: '0-1', name: 'firstname', value: name },
    { objectTypeId: '0-1', name: 'message', value: topic ? `[${topic}] ${message}` : message },
  ];
  const phone = clean(data.phone, 40);
  const company = clean(data.company, 160);
  if (phone) fields.push({ objectTypeId: '0-1', name: 'phone', value: phone });
  if (company) fields.push({ objectTypeId: '0-1', name: 'company', value: company });

  const payload = { fields, context: contextFor(request, data, `Contact form (${lang.toUpperCase()})`) };
  return (await submitToHubSpot(env, env.HUBSPOT_CONTACT_FORM_ID, payload)) ? json({ ok: true }) : json({ error: 'Send failed' }, 502);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // This Worker only runs for /api/* (see run_worker_first in wrangler.jsonc);
    // everything else is served straight from /public with _redirects and _headers applied.
    if (url.pathname === '/api/subscribe') return subscribe(request, env);
    if (url.pathname === '/api/contact') return contact(request, env);
    if (url.pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);
    return env.ASSETS.fetch(request);
  },
};
