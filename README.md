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
| `src/worker.js` | Worker: `/api/subscribe` (newsletter → MailerLite); everything else is static |
| `wrangler.jsonc` | Cloudflare configuration |

## Editing content

1. Edit the page text in `build/pages_en.py` or `build/pages_pt.py` (contact details live in `build/sitecfg.py`).
2. Run `python3 build/build.py`.
3. Commit and push — Cloudflare Workers Builds deploys automatically.

## Deploy settings (Cloudflare → Workers & Pages → Create → Import a repository)

- Repository: `Isabellylima/stevecampbell`, branch `main`
- Build command: *(leave empty)*
- Deploy command: `npx wrangler deploy`

## Newsletter (MailerLite)

Set in Worker → Settings → Variables and Secrets:

- `MAILERLITE_API_KEY` (secret) — MailerLite → Integrations → MailerLite API
- `MAILERLITE_GROUP_EN`, `MAILERLITE_GROUP_PT` (optional) — group IDs to separate English and Portuguese subscribers

## SEO and AI discoverability

- Canonical URLs, `hreflang` pairs (en-GB / pt-PT / x-default), Open Graph
- JSON-LD: ProfessionalService, Person, Service, FAQPage, BreadcrumbList
- `sitemap.xml` with language alternates; `robots.txt` open to search and AI crawlers; `llms.txt` summary
- 301 redirects from the old WordPress URLs in `_redirects`
