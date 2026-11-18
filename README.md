# Steve Campbell Associates — website

Static, bilingual (en-GB / pt-PT) site for https://stevecampbellassociates.com, served by a Cloudflare Worker with static assets.

## Structure

| Path | What it is |
| --- | --- |
| `build/sitecfg.py` | Contact details, services list, layout (header, footer, newsletter), JSON-LD schema |
| `build/pages_en.py` | English pages |
| `build/pages_pt.py` | Portuguese pages |
| `build/build.py` | Generates `public/` — HTML pages, `sitemap.xml`, `robots.txt`, `llms.txt`, `_redirects`, `_headers` |
| `public/` | The built site (committed, so Cloudflare deploys it without a build step) |
| `public/assets/` | CSS, JS, images |
| `src/worker.js` | Worker: `/api/subscribe` (newsletter → HubSpot form); everything else is static |
| `wrangler.jsonc` | Cloudflare configuration |

## Editing content

1. Edit the page text in `build/pages_en.py` or `build/pages_pt.py` (contact details live in `build/sitecfg.py`).
2. Run `python3 build/build.py`.
3. Commit and push — Cloudflare Workers Builds deploys automatically.

## Deploy settings (Cloudflare → Workers & Pages → Create → Import a repository)

- Repository: `Isabellylima/stevecampbell`, branch `main`
- Build command: *(leave empty)*
- Deploy command: `npx wrangler deploy`

## Forms (HubSpot)

The newsletter box, the newsletter pop-up and the contact form send to HubSpot forms through the Forms API (no API key needed). If HubSpot is not configured yet, the contact form falls back to opening the visitor's email app.

Set in Worker → Settings → Variables and Secrets:

- `HUBSPOT_PORTAL_ID` — HubSpot account ID (Hub ID)
- `HUBSPOT_FORM_ID` — newsletter form GUID (fields: email, firstname, company)
- `HUBSPOT_FORM_ID_PT` (optional) — separate newsletter form for Portuguese sign-ups
- `HUBSPOT_CONTACT_FORM_ID` — contact form GUID (fields: email, firstname, phone, company, message)
- `HUBSPOT_SUBSCRIPTION_ID` (optional) — marketing subscription type ID, only if the newsletter form has GDPR consent options enabled

The pop-up opens on exit intent (desktop) or after 30 seconds, once per visitor (not again for 30 days after closing, never after subscribing), and never on the contact or privacy pages.

## SEO and AI discoverability

- Canonical URLs, `hreflang` pairs (en-GB / pt-PT / x-default), Open Graph
- JSON-LD: ProfessionalService, Person, Service, FAQPage, BreadcrumbList
- `sitemap.xml` with language alternates; `robots.txt` open to search and AI crawlers; `llms.txt` summary
- 301 redirects from the old WordPress URLs in `_redirects`
