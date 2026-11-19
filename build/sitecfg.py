"""Shared site config, layout and helpers for the Steve Campbell Associates static build."""
import json, html
from urllib.parse import quote

BASE = "https://stevecampbellassociates.com"
EBOOK_URL = "https://drive.google.com/file/d/1uFtzRUFLmUJyXk4_7Kv8B6Zb5zn7euBj/view"
PHONE = "+44 7766 103543"
PHONE_HREF = "tel:+447766103543"
WHATSAPP = "447766103543"
WA_MSG = {
    "en": "Hello Steve, I found your website and would like to discuss a construction or property matter.",
    "pt": "Olá Steve, encontrei o seu site e gostaria de falar sobre uma questão de construção ou imobiliário.",
}
WA_ICON = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16.04 3C9 3 3.3 8.7 3.3 15.73c0 2.25.59 4.44 1.7 6.37L3.2 28.8l6.88-1.8a12.7 12.7 0 0 0 5.96 1.5h.01c7.03 0 12.74-5.7 12.74-12.73C28.8 8.7 23.08 3 16.04 3zm0 23.35h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-4.08 1.07 1.09-3.98-.25-.41a10.56 10.56 0 0 1-1.62-5.6c0-5.85 4.76-10.6 10.62-10.6 2.83 0 5.5 1.1 7.5 3.11a10.53 10.53 0 0 1 3.1 7.5c0 5.85-4.76 10.62-10.56 10.62zm5.82-7.94c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.72.16-.21.32-.82 1.04-1.01 1.25-.19.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.19-.32-.02-.49.14-.65.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.72-1.73-.98-2.37-.26-.62-.52-.54-.72-.55l-.61-.01c-.21 0-.56.08-.85.4-.29.32-1.12 1.09-1.12 2.66s1.15 3.09 1.31 3.3c.16.21 2.26 3.45 5.47 4.84.76.33 1.36.53 1.83.68.77.24 1.47.21 2.02.13.62-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37z"/></svg>'
EMAIL = "steve@stevecampbellassociates.com"
ADDRESS = {
    "street": "3 Claridge Court, Lower Kings Road",
    "locality": "Berkhamsted",
    "region": "Hertfordshire",
    "postcode": "HP4 2AE",
    "country": "GB",
}
SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/in/steve-campbell-4b22983b"),
    ("Facebook", "https://www.facebook.com/SteveCampbellAssociates/"),
    ("Instagram", "https://www.instagram.com/steve_campbell_associates/"),
]
ICONS = {
    "LinkedIn": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.79-1.7-2.79-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg>',
    "Facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.87.25-1.46 1.5-1.46h1.55V4.47A20.6 20.6 0 0 0 14.3 4.3c-2.24 0-3.8 1.37-3.8 3.9v2.3H8v3h2.5V21z"/></svg>',
    "Instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.2A4.8 4.8 0 1 0 12 16.8 4.8 4.8 0 0 0 12 7.2zm0 7.9a3.1 3.1 0 1 1 0-6.2 3.1 3.1 0 0 1 0 6.2zM17.1 5.8a1.1 1.1 0 1 0 0 2.2 1.1 1.1 0 0 0 0-2.2zM12 3c-2.44 0-2.75.01-3.71.05C5.03 3.2 3.2 5.02 3.05 8.29 3.01 9.25 3 9.56 3 12s.01 2.75.05 3.71c.15 3.27 1.98 5.09 5.24 5.24.96.04 1.27.05 3.71.05s2.75-.01 3.71-.05c3.26-.15 5.09-1.97 5.24-5.24.04-.96.05-1.27.05-3.71s-.01-2.75-.05-3.71C20.8 5.03 18.97 3.2 15.71 3.05 14.75 3.01 14.44 3 12 3zm0 1.62c2.4 0 2.69.01 3.64.05 2.44.11 3.58 1.27 3.69 3.69.04.95.05 1.24.05 3.64s-.01 2.69-.05 3.64c-.11 2.42-1.25 3.58-3.69 3.69-.95.04-1.23.05-3.64.05s-2.69-.01-3.64-.05c-2.45-.11-3.58-1.27-3.69-3.69-.04-.95-.05-1.24-.05-3.64s.01-2.69.05-3.64c.11-2.42 1.25-3.58 3.69-3.69.95-.04 1.24-.05 3.64-.05z"/></svg>',
}
IMPLEMENT_URL = "https://heyimplement.com/"

POSTNOMS = "DipAdj FCIArb FFPWS MCIOB"
VERSION = "20261119"

ORG_ID = BASE + "/#organization"
PERSON_ID = BASE + "/#steve-campbell"
WEBSITE_ID = BASE + "/#website"

SERVICES_EN = [
    ("adjudication", "Construction Adjudication",
     "Statutory adjudication under the Construction Act: payment disputes, smash and grab and true value claims, variations, delay and final accounts."),
    ("arbitration", "Arbitration",
     "Domestic and international construction and property arbitration, with Steve acting as arbitrator or as party representative."),
    ("party-wall-surveyor", "Party Wall Surveying",
     "Building owner's, adjoining owner's, agreed and third surveyor appointments under the Party Wall etc. Act 1996."),
    ("mediation", "Mediation",
     "Confidential, facilitated negotiation for construction, commercial and property disputes, before or during proceedings."),
    ("expert-determination-and-early-neutral-evaluation", "Expert Determination & Early Neutral Evaluation (ENE)",
     "Fast, binding expert decisions on defined technical questions, and non-binding early evaluations of the merits."),
    ("expert-witness", "Expert Witness",
     "Independent construction expert evidence for the courts, arbitration and adjudication, prepared under CPR Part 35."),
    ("construction-consultancy", "Construction Claims & Consultancy",
     "Claims preparation, extensions of time, delay analysis, loss and expense, contract advice and project management."),
]


def esc(s):
    return html.escape(s, quote=True)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": ORG_ID,
        "name": "Steve Campbell Associates",
        "description": "Chartered building consultancy and specialist construction and property dispute resolution practice: arbitration, adjudication, party wall surveying, mediation, expert determination and expert witness services.",
        "url": BASE + "/",
        "logo": BASE + "/icon-512.png",
        "image": BASE + "/assets/img/og-image.jpg",
        "telephone": PHONE,
        "email": EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDRESS["street"],
            "addressLocality": ADDRESS["locality"],
            "addressRegion": ADDRESS["region"],
            "postalCode": ADDRESS["postcode"],
            "addressCountry": ADDRESS["country"],
        },
        "areaServed": [
            {"@type": "Country", "name": "United Kingdom"},
            {"@type": "Country", "name": "Portugal"},
        ],
        "founder": {"@id": PERSON_ID},
        "employee": {"@id": PERSON_ID},
        "slogan": "Sine timore vel favore — without fear or favour",
        "knowsAbout": [
            "Construction adjudication", "Housing Grants, Construction and Regeneration Act 1996",
            "Arbitration", "International arbitration", "Party Wall etc. Act 1996", "Third surveyor",
            "Mediation", "Expert determination", "Early neutral evaluation", "Expert witness",
            "Extensions of time", "Delay analysis", "Loss and expense", "JCT contracts", "NEC contracts", "FIDIC contracts",
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Dispute resolution and construction consultancy services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": f"{BASE}/services/{s}/"}}
                for s, n, _ in SERVICES_EN
            ],
        },
        "sameAs": [u for _, u in SOCIAL],
    }


def person_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "Steve Campbell",
        "honorificSuffix": POSTNOMS,
        "jobTitle": "Principal — Chartered Construction Manager, Arbitrator, Adjudicator, Mediator and Party Wall Surveyor",
        "worksFor": {"@id": ORG_ID},
        "url": BASE + "/about/",
        "image": BASE + "/assets/img/steve-campbell-2026.jpg",
        "memberOf": [
            {"@type": "Organization", "name": "Chartered Institute of Arbitrators", "url": "https://www.ciarb.org/"},
            {"@type": "Organization", "name": "Faculty of Party Wall Surveyors", "url": "https://www.fpws.org.uk/"},
            {"@type": "Organization", "name": "Chartered Institute of Building", "url": "https://www.ciob.org/"},
            {"@type": "Organization", "name": "Society of Construction Law", "url": "https://www.scl.org.uk/"},
            {"@type": "Organization", "name": "Adjudication Society", "url": "https://www.adjudication.org/"},
            {"@type": "Organization", "name": "Party Wall Academy"},
        ],
        "knowsAbout": ["Construction adjudication", "Arbitration", "Party wall surveying", "Mediation",
                       "Expert witness evidence", "Construction management", "Quantity surveying"],
        "sameAs": [SOCIAL[0][1]],
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": WEBSITE_ID,
        "url": BASE + "/",
        "name": "Steve Campbell Associates",
        "publisher": {"@id": ORG_ID},
        "inLanguage": ["en-GB", "pt-PT"],
    }


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p}
            for i, (n, p) in enumerate(items)
        ],
    }


def service_schema(name, desc, path, lang="en-GB"):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": desc,
        "url": BASE + path,
        "inLanguage": lang,
        "provider": {"@id": ORG_ID},
        "areaServed": [{"@type": "Country", "name": "United Kingdom"}, {"@type": "Country", "name": "Portugal"}],
    }


def faq(items, lang="en"):
    """items: list of (question, answer_html). Returns (html, schema)."""
    import re
    title = "Frequently asked questions" if lang == "en" else "Perguntas frequentes"
    parts = [f'<section class="faq-section"><div class="wrap narrow faq"><h2>{title}</h2>']
    for q, a in items:
        parts.append(f"<details><summary>{esc(q)}</summary><div>{a}</div></details>")
    parts.append("</div></section>")
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", a)).strip()}}
            for q, a in items
        ],
    }
    return "".join(parts), schema


def crumbs_html(items):
    lis = []
    for i, (n, p) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            lis.append(f'<li><a href="{p}">{esc(n)}</a></li>')
    label = "Breadcrumb"
    return f'<nav class="crumbs" aria-label="{label}"><ol>{"".join(lis)}</ol></nav>'


def page_hero(title, lead, crumbs, eyebrow=None):
    eb = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""
    return (f'<header class="page-hero"><div class="wrap">{crumbs_html(crumbs)}{eb}'
            f'<h1>{title}</h1><p class="lead">{lead}</p></div></header>')


# ---------- Header / footer ----------

BLOG_LANGS = set()  # filled by build.py with languages that have published posts

NAV = {
    "en": [("/services/", "Services"), ("/about/", "About Steve"), ("/portugal/", "Portugal"), ("/e-book/", "E-book")],
    "pt": [("/pt/servicos/", "Serviços"), ("/pt/sobre/", "Sobre o Steve"), ("/pt/e-book/", "E-book")],
}


def header(lang, path, alt_path):
    items = []
    nav_items = list(NAV[lang])
    if lang in BLOG_LANGS:
        nav_items.insert(len(nav_items) - 1, ("/blog/" if lang == "en" else "/pt/blog/", "Blog"))
    for href, label in nav_items:
        cur = ' aria-current="page"' if path == href or (href != "/" and path.startswith(href) and href.count("/") > 1 and path != "/") else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    if lang == "en":
        switch = f'<a class="lang" href="{alt_path or "/pt/"}" hreflang="pt-PT" lang="pt-PT">PT</a>'
        cta = '<a class="btn" href="/contact/">Contact</a>'
        home, tag, menu, skip = "/", "Construction Dispute Resolution", "Menu", "Skip to content"
    else:
        switch = f'<a class="lang" href="{alt_path or "/"}" hreflang="en-GB" lang="en-GB">EN</a>'
        cta = '<a class="btn" href="/pt/contacto/">Contacto</a>'
        home, tag, menu, skip = "/pt/", "Resolução de Litígios na Construção", "Menu", "Saltar para o conteúdo"
    return f'''<a class="skip" href="#main">{skip}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{home}"><img src="/assets/img/crest-96.png" width="52" height="52" alt="" aria-hidden="true"><span>Steve Campbell Associates<small>{tag}</small></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">{menu}</button>
<nav class="nav" id="site-nav" aria-label="Main">{"".join(items)}{switch}{cta}</nav>
</div></header>'''


def newsletter(lang):
    if lang == "en":
        return f'''<section class="newsletter" id="newsletter" aria-labelledby="nl-title"><div class="wrap">
<div><p class="eyebrow" style="color:#e0c98f">Newsletter</p><h2 id="nl-title">Construction dispute insights, by email</h2>
<p>Occasional, practical notes from Steve on adjudication, arbitration, payment rules and party wall procedure — written for contractors, developers, consultants and property owners. No sales emails; unsubscribe at any time.</p></div>
<form data-newsletter action="/api/subscribe" method="post" novalidate>
<div class="row"><div class="field"><label for="nl-name">Name</label><input id="nl-name" name="name" type="text" autocomplete="name"></div>
<div class="field"><label for="nl-company">Company <span style="font-weight:400">(optional)</span></label><input id="nl-company" name="company" type="text" autocomplete="organization"></div></div>
<div class="field"><label for="nl-email">Work email</label><input id="nl-email" name="email" type="email" autocomplete="email" required></div>
<div class="hp" aria-hidden="true"><label for="nl-web">Website</label><input id="nl-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<div class="field"><label class="consent"><input type="checkbox" name="consent" value="yes" required> I agree to receive emails from Steve Campbell Associates and accept the <a href="/privacy/">privacy notice</a>.</label></div>
<button class="btn light" type="submit">Subscribe</button><p class="form-msg" role="status" aria-live="polite"></p>
</form></div></section>'''
    return f'''<section class="newsletter" id="newsletter" aria-labelledby="nl-title"><div class="wrap">
<div><p class="eyebrow" style="color:#e0c98f">Newsletter</p><h2 id="nl-title">Notas sobre litígios na construção, por e-mail</h2>
<p>Notas práticas e ocasionais do Steve sobre arbitragem, mediação, contratos internacionais de construção e gestão de reclamações — para empresas de construção, promotores, investidores e consultores. Sem e-mails comerciais; pode cancelar a qualquer momento.</p></div>
<form data-newsletter action="/api/subscribe" method="post" novalidate>
<div class="row"><div class="field"><label for="nl-name">Nome</label><input id="nl-name" name="name" type="text" autocomplete="name"></div>
<div class="field"><label for="nl-company">Empresa <span style="font-weight:400">(opcional)</span></label><input id="nl-company" name="company" type="text" autocomplete="organization"></div></div>
<div class="field"><label for="nl-email">E-mail profissional</label><input id="nl-email" name="email" type="email" autocomplete="email" required></div>
<div class="hp" aria-hidden="true"><label for="nl-web">Website</label><input id="nl-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<div class="field"><label class="consent"><input type="checkbox" name="consent" value="yes" required> Aceito receber e-mails da Steve Campbell Associates e li a <a href="/pt/privacidade/">política de privacidade</a>.</label></div>
<button class="btn light" type="submit">Subscrever</button><p class="form-msg" role="status" aria-live="polite"></p>
</form></div></section>'''


def popup(lang):
    if lang == "en":
        t = dict(eyebrow="Free e-book + newsletter", title="Practical notes on construction disputes",
                 text="Join Steve's newsletter for occasional, practical guidance on adjudication, payment rules, arbitration and party wall procedure. No sales emails; unsubscribe at any time.",
                 name="Name", email="Work email", consent='I agree to receive emails from Steve Campbell Associates and accept the <a href="/privacy/">privacy notice</a>.',
                 button="Subscribe", close="Close", later="No thanks",
                 after=f'While you wait, <a href="/e-book/">read Steve\'s free e-book</a>.')
    else:
        t = dict(eyebrow="E-book gratuito + newsletter", title="Notas práticas sobre litígios na construção",
                 text="Subscreva a newsletter do Steve para receber, de vez em quando, orientações práticas sobre arbitragem, mediação, contratos e reclamações. Sem e-mails comerciais; pode cancelar a qualquer momento.",
                 name="Nome", email="E-mail profissional", consent='Aceito receber e-mails da Steve Campbell Associates e li a <a href="/pt/privacidade/">política de privacidade</a>.',
                 button="Subscrever", close="Fechar", later="Agora não",
                 after='Entretanto, <a href="/pt/e-book/">leia o e-book gratuito do Steve</a>.')
    return f'''<dialog class="nl-popup" id="nl-popup" aria-labelledby="pop-title">
<div class="nl-popup-inner">
<button type="button" class="nl-close" data-close aria-label="{t['close']}">×</button>
<img src="/assets/img/crest-96.png" width="56" height="56" alt="" aria-hidden="true">
<p class="eyebrow">{t['eyebrow']}</p>
<h2 id="pop-title" tabindex="-1" autofocus>{t['title']}</h2>
<p>{t['text']}</p>
<form data-newsletter action="/api/subscribe" method="post" novalidate>
<input type="hidden" name="placement" value="popup">
<div class="field"><label for="pop-name">{t['name']}</label><input id="pop-name" name="name" type="text" autocomplete="name"></div>
<div class="field"><label for="pop-email">{t['email']}</label><input id="pop-email" name="email" type="email" autocomplete="email" required></div>
<div class="hp" aria-hidden="true"><label for="pop-web">Website</label><input id="pop-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<div class="field"><label class="consent"><input type="checkbox" name="consent" value="yes" required> {t['consent']}</label></div>
<div class="actions"><button class="btn" type="submit">{t['button']}</button><button type="button" class="btn ghost" data-close>{t['later']}</button></div>
<p class="form-msg" role="status" aria-live="polite"></p>
</form>
<p data-after-subscribe hidden>{t['after']}</p>
</div>
</dialog>'''


def footer(lang):
    social = '<div class="social">' + "".join(
        f'<a href="{u}" rel="me noopener" target="_blank" aria-label="Steve Campbell Associates on {n}" title="{n}">{ICONS[n]}</a>'
        for n, u in SOCIAL) + '</div>'
    made = f'<a class="made-by" href="{IMPLEMENT_URL}" target="_blank" rel="noopener">Made by Implement</a>'
    addr = f'{ADDRESS["street"]}<br>{ADDRESS["locality"]}, {ADDRESS["region"]}<br>{ADDRESS["postcode"]}, United Kingdom'
    if lang == "en":
        svc = "".join(f'<li><a href="/services/{s}/">{n}</a></li>' for s, n, _ in SERVICES_EN)
        return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div class="footer-brand"><img src="/assets/img/crest-white-96.png" width="70" height="70" alt="Steve Campbell Associates crest"><p><strong style="color:#fff">Steve Campbell Associates</strong><br>Chartered building consultancy and specialist dispute resolution practice.</p><p><em>Sine timore vel favore</em> — without fear or favour.</p></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Practice</h3><ul><li><a href="/about/">About Steve Campbell</a></li><li><a href="/portugal/">Clients in Portugal</a></li><li><a href="/e-book/">Free e-book</a></li>{'<li><a href="/blog/">Blog</a></li>' if "en" in BLOG_LANGS else ""}<li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy notice</a></li><li><a href="/pt/" hreflang="pt-PT">Português</a></li></ul></div>
<div><h3>Contact</h3><ul><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{addr}</li></ul><h3 style="margin-top:18px">Follow</h3>{social}</div>
</div>
<div class="footer-bottom"><span>© 2026 Steve Campbell Associates. All rights reserved.</span><span>Information on this website is general guidance, not legal advice for a specific matter.</span><span>{made}</span></div>
</div></footer>'''
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div class="footer-brand"><img src="/assets/img/crest-white-96.png" width="70" height="70" alt="Brasão Steve Campbell Associates"><p><strong style="color:#fff">Steve Campbell Associates</strong><br>Consultoria de construção e prática especializada em resolução de litígios.</p><p><em>Sine timore vel favore</em> — sem medo nem favor.</p></div>
<div><h3>Serviços</h3><ul><li><a href="/pt/servicos/#arbitragem">Arbitragem</a></li><li><a href="/pt/servicos/#mediacao">Mediação</a></li><li><a href="/pt/servicos/#peritagem">Perito independente</a></li><li><a href="/pt/servicos/#consultoria">Consultoria e reclamações</a></li><li><a href="/pt/servicos/#reino-unido">Litígios no Reino Unido</a></li></ul></div>
<div><h3>Empresa</h3><ul><li><a href="/pt/sobre/">Sobre o Steve Campbell</a></li><li><a href="/pt/e-book/">E-book gratuito</a></li>{'<li><a href="/pt/blog/">Blog</a></li>' if "pt" in BLOG_LANGS else ""}<li><a href="/pt/contacto/">Contacto</a></li><li><a href="/pt/privacidade/">Política de privacidade</a></li><li><a href="/" hreflang="en-GB">English</a></li></ul></div>
<div><h3>Contacto</h3><ul><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{addr.replace("United Kingdom", "Reino Unido")}</li></ul><h3 style="margin-top:18px">Redes sociais</h3>{social}</div>
</div>
<div class="footer-bottom"><span>© 2026 Steve Campbell Associates. Todos os direitos reservados.</span><span>A informação deste site é de carácter geral e não constitui aconselhamento jurídico.</span><span>{made}</span></div>
</div></footer>'''


def layout(*, lang, path, title, description, body, alternates=None, schemas=(), alt_path=None, og_type="website", noindex=False):
    """alternates: dict like {"en-GB": "/about/", "pt-PT": "/pt/sobre/"} — only for true equivalents."""
    html_lang = "en-GB" if lang == "en" else "pt-PT"
    canonical = BASE + path
    alt_links = ""
    if alternates:
        for hl, p in alternates.items():
            alt_links += f'<link rel="alternate" hreflang="{hl}" href="{BASE + p}">'
        if "en-GB" in alternates:
            alt_links += f'<link rel="alternate" hreflang="x-default" href="{BASE + alternates["en-GB"]}">'
    og_locale = "en_GB" if lang == "en" else "pt_PT"
    og_alt = "pt_PT" if lang == "en" else "en_GB"
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'
    base_schemas = [organization_schema(), website_schema()]
    all_ld = "".join(ld(s) for s in base_schemas + list(schemas))
    return f'''<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
<link rel="canonical" href="{canonical}">
<link rel="alternate" type="application/rss+xml" title="Steve Campbell Associates — Blog" href="{BASE}{"/pt/feed.xml" if lang == "pt" else "/feed.xml"}">
{alt_links}
<meta name="theme-color" content="#4b167f">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Steve Campbell Associates">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{og_locale}"><meta property="og:locale:alternate" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,600&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={VERSION}">
{all_ld}
</head>
<body>
{header(lang, path, alt_path)}
<main id="main">
{body}
</main>
{newsletter(lang)}
{popup(lang)}
<a class="wa-float" href="https://wa.me/{WHATSAPP}?text={quote(WA_MSG[lang])}" target="_blank" rel="noopener" aria-label="{"Fale com o Steve no WhatsApp" if lang == "pt" else "Chat with Steve on WhatsApp"}" title="WhatsApp">{WA_ICON}<span>WhatsApp</span></a>
{footer(lang)}
<script src="/assets/js/site.js?v={VERSION}" defer></script>
<!-- Metricool web analytics (cookieless) -->
<script>function loadScript(a){{var b=document.getElementsByTagName("head")[0],c=document.createElement("script");c.type="text/javascript",c.src="https://tracker.metricool.com/resources/be.js",c.onreadystatechange=a,c.onload=a,b.appendChild(c)}}loadScript(function(){{beTracker.t({{hash:"9a57335884b44fb6e9cb9e19b0d10d4b"}})}});</script>
</body>
</html>
'''


def cta_band(lang="en"):
    if lang == "en":
        return f'''<section class="cta-band"><div class="wrap"><div><h2>Discuss your matter in confidence</h2>
<p>Tell Steve what has happened and where things stand. He will explain the realistic options — including whether a formal process is needed at all. The initial consultation is free.</p></div>
<div class="actions"><a class="btn light" href="/contact/">Make an enquiry</a><a class="btn outline-light" href="{PHONE_HREF}">Call {PHONE}</a></div></div></section>'''
    return f'''<section class="cta-band"><div class="wrap"><div><h2>Fale connosco com total confidencialidade</h2>
<p>Explique a situação e o ponto em que se encontra. O Steve indica as opções realistas — incluindo se é mesmo necessário avançar para um processo formal. A primeira consulta é gratuita.</p></div>
<div class="actions"><a class="btn light" href="/pt/contacto/">Pedir contacto</a><a class="btn outline-light" href="{PHONE_HREF}">Ligar {PHONE}</a></div></div></section>'''
