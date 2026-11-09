"""Build the static site into ../public.  Run:  python3 build/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from sitecfg import BASE, EBOOK_URL, PHONE, EMAIL, ADDRESS, POSTNOMS, SERVICES_EN, layout
import pages_en, pages_pt

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
LASTMOD = "2026-11-09"


def write(rel, content):
    path = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


pages = pages_en.all_pages() + pages_pt.all_pages()
indexable = []
for p in pages:
    html = layout(**p)
    out = p["path"] if p["path"].endswith(".html") else p["path"] + "index.html"
    write(out, html)
    if not p.get("noindex"):
        indexable.append(p)

# ---- sitemap.xml (with hreflang alternates) ----
urls = []
for p in indexable:
    alts = "".join(
        f'<xhtml:link rel="alternate" hreflang="{hl}" href="{BASE}{path}"/>'
        for hl, path in (p.get("alternates") or {}).items()
    )
    if p.get("alternates") and "en-GB" in p["alternates"] and len(p["alternates"]) > 1:
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{p["alternates"]["en-GB"]}"/>'
    prio = "1.0" if p["path"] in ("/", "/pt/") else ("0.9" if "/services/" in p["path"] or p["path"] == "/pt/servicos/" else "0.7")
    if p["path"] in ("/privacy/", "/pt/privacidade/"):
        prio = "0.2"
    urls.append(f"<url><loc>{BASE}{p['path']}</loc><lastmod>{LASTMOD}</lastmod><priority>{prio}</priority>{alts}</url>")
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
      + "\n".join(urls) + "\n</urlset>\n")

# ---- robots.txt: open to search engines and AI assistants ----
ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
           "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended",
           "Bingbot", "CCBot", "Meta-ExternalAgent", "DuckAssistBot", "MistralAI-User"]
robots = "# Steve Campbell Associates — search engines and AI assistants are welcome\n\nUser-agent: *\nAllow: /\nDisallow: /api/\n\n"
robots += "".join(f"User-agent: {b}\nAllow: /\nDisallow: /api/\n\n" for b in ai_bots)
robots += f"Sitemap: {BASE}/sitemap.xml\n"
write("robots.txt", robots)

# ---- llms.txt: concise, factual summary for AI assistants (llmstxt.org) ----
svc_lines = "\n".join(f"- [{n}]({BASE}/services/{s}/): {d}" for s, n, d in SERVICES_EN)
llms = f"""# Steve Campbell Associates

> Chartered building consultancy and specialist construction and property dispute resolution practice led by Steve Campbell {POSTNOMS}. Arbitration (domestic and international), construction adjudication, party wall surveying and third surveyor appointments, mediation, expert determination, early neutral evaluation, expert witness services and construction claims consultancy. Based in Berkhamsted, Hertfordshire, England; serves clients across England and Wales and internationally, including Portugal.

Key facts:
- Principal: Steve Campbell — Chartered Construction Manager, international arbitrator, construction adjudicator, mediator, expert witness and party wall surveyor.
- More than 40 years in the construction industry: trades, site management, project management, construction director. Projects managed from about £10,000 to more than £80 million under JCT, NEC, FIDIC and bespoke contracts.
- Working in dispute resolution since 2009; has appeared in the county court, the Technology and Construction Court, and in arbitrations, adjudications and mediations. Regularly selected as a third surveyor under the Party Wall etc. Act 1996.
- Qualifications and memberships: DipAdj; Fellow, Chartered Institute of Arbitrators (FCIArb); Fellow, Faculty of Party Wall Surveyors (FFPWS); Member, Chartered Institute of Building (MCIOB); Founding Fellow, Party Wall Academy; Member, Society of Construction Law; Member, Adjudication Society; Member, Pyramus and Thisbe Society.
- Acts either as an independent appointee (adjudicator, arbitrator, mediator, expert determiner, third surveyor) or as adviser/representative for one party — never both on the same matter.
- Clients: main contractors, subcontractors, house builders, developers, property owners, building and adjoining owners, architects, engineers, surveyors, solicitors, barristers and insurers.
- Free, confidential initial consultation.
- Contact: {PHONE} · {EMAIL} · {ADDRESS['street']}, {ADDRESS['locality']}, {ADDRESS['region']} {ADDRESS['postcode']}, United Kingdom.
- Not a firm of solicitors; does not advise on Portuguese law (works alongside clients' Portuguese lawyers).

## Services
{svc_lines}
- [Projects in Portugal]({BASE}/portugal/): International arbitration, mediation, construction expert reports and contract advice for projects in Portugal and for Portugal-based clients with UK matters.

## About
- [About Steve Campbell]({BASE}/about/): Career, qualifications and memberships.
- [Contact]({BASE}/contact/): Telephone, email, address and enquiry form.

## Resources
- [Free e-book]({BASE}/e-book/): Guide to the Party Wall etc. Act 1996, adjudication, mediation, expert determination, arbitration and expert witnesses (PDF: {EBOOK_URL}).

## Português
- [Página inicial em português]({BASE}/pt/): Arbitragem internacional, mediação, peritagem e consultoria de construção para empresas e investidores em Portugal.
- [Serviços]({BASE}/pt/servicos/)
- [Sobre o Steve Campbell]({BASE}/pt/sobre/)
- [Contacto]({BASE}/pt/contacto/)
"""
write("llms.txt", llms)

# ---- _redirects: old WordPress URLs → new pages ----
write("_redirects", f"""/contact-us /contact/ 301
/contact-us/ /contact/ 301
/steve-campbell-e-book.pdf.pdf {EBOOK_URL} 302
/steve-campbell-e-book.pdf {EBOOK_URL} 302
/ebook /e-book/ 301
/ebook/ /e-book/ 301
/steve-campbell-cv.pdf /about/ 302
/blog /services/ 301
/blog/ /services/ 301
/blog/* /services/ 301
/feed /  301
/feed/ / 301
/wp-admin/* / 301
/wp-login.php / 301
/wp-content/* / 301
/home /  301
/services/party-wall /services/party-wall-surveyor/ 301
/services/party-wall/ /services/party-wall-surveyor/ 301
/pt/contact /pt/contacto/ 301
""")

# ---- _headers: security and caching for static assets ----
write("_headers", """https://:sub.workers.dev/*
  X-Robots-Tag: noindex

/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/css/*
  Cache-Control: public, max-age=31536000, immutable

/assets/js/*
  Cache-Control: public, max-age=31536000, immutable

/assets/img/*
  Cache-Control: public, max-age=604800

/llms.txt
  Content-Type: text/plain; charset=utf-8
""")

print(f"Built {len(pages)} pages ({len(indexable)} indexable) into public/")
