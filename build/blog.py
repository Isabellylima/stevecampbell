"""Blog: posts are Markdown files in content/blog/ with a YAML header.

---
title: Planning an extension? The Party Wall Act may apply
date: 2026-11-20
description: One or two sentences shown in Google, AI answers, the blog list and the RSS feed.
lang: en            # en or pt
draft: true         # true = not published
tags: [Party wall]
---
Article text in Markdown (## headings, - lists, **bold**, [links](https://...)).
"""
import datetime as dt
import glob
import html
import os
import re
from email.utils import format_datetime

import markdown
import yaml

from sitecfg import (BASE, ORG_ID, PERSON_ID, POSTNOMS, breadcrumb_schema, cta_band, esc, page_hero)

CONTENT = os.path.join(os.path.dirname(__file__), "..", "content", "blog")

L = {
    "en": dict(index="/blog/", feed="/feed.xml", home="/", home_name="Home", name="Blog",
               title="Blog: construction dispute insights | Steve Campbell Associates",
               desc="Practical articles by Steve Campbell on adjudication, arbitration, mediation, party wall procedure and construction claims.",
               lead="Practical notes by Steve Campbell on adjudication, arbitration, mediation, party wall procedure and construction claims.",
               empty="The first articles are on their way. Subscribe to the newsletter below to receive them by email.",
               read="Read article →", by="By", minutes="min read", feed_title="Steve Campbell Associates — Blog",
               about="Steve Campbell is a Chartered Construction Manager, international arbitrator, construction adjudicator, mediator, expert witness and party wall surveyor with more than 40 years in the construction industry.",
               about_link="/about/", about_cta="More about Steve", rss="RSS feed", inlang="en-GB",
               note="This article is general information, not legal advice for a specific matter."),
    "pt": dict(index="/pt/blog/", feed="/pt/feed.xml", home="/pt/", home_name="Início", name="Blog",
               title="Blog: litígios na construção | Steve Campbell Associates",
               desc="Artigos práticos do Steve Campbell sobre arbitragem, mediação, peritagem, contratos e reclamações na construção.",
               lead="Artigos práticos do Steve Campbell sobre arbitragem, mediação, peritagem, contratos e reclamações na construção.",
               empty="Os primeiros artigos estão a caminho. Subscreva a newsletter abaixo para os receber por e-mail.",
               read="Ler artigo →", by="Por", minutes="min de leitura", feed_title="Steve Campbell Associates — Blog",
               about="O Steve Campbell é gestor de construção certificado, árbitro internacional, mediador, perito e party wall surveyor, com mais de 40 anos no setor da construção.",
               about_link="/pt/sobre/", about_cta="Mais sobre o Steve", rss="Feed RSS", inlang="pt-PT",
               note="Este artigo é informação geral e não constitui aconselhamento jurídico para um caso concreto."),
}

MONTHS_PT = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
             "setembro", "outubro", "novembro", "dezembro"]


def fmt_date(d, lang):
    if lang == "pt":
        return f"{d.day} de {MONTHS_PT[d.month - 1]} de {d.year}"
    return d.strftime("%-d %B %Y")


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.U)
    return re.sub(r"[\s_]+", "-", s).strip("-")


def load_posts(include_drafts=False):
    posts = []
    for f in sorted(glob.glob(os.path.join(CONTENT, "*.md"))):
        if os.path.basename(f).lower() == "readme.md":
            continue
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
        if not m:
            raise ValueError(f"{f}: missing --- header ---")
        meta = yaml.safe_load(m.group(1)) or {}
        for k in ("title", "date", "description"):
            if not meta.get(k):
                raise ValueError(f"{f}: '{k}' is required in the header")
        if meta.get("draft") and not include_drafts:
            continue
        lang = "pt" if meta.get("lang") == "pt" else "en"
        date = meta["date"] if isinstance(meta["date"], dt.date) else dt.date.fromisoformat(str(meta["date"]))
        slug = meta.get("slug") or slugify(os.path.splitext(os.path.basename(f))[0])
        body_md = m.group(2).strip()
        words = len(re.findall(r"\w+", body_md))
        posts.append(dict(
            title=str(meta["title"]), description=str(meta["description"]), date=date, lang=lang,
            tags=list(meta.get("tags") or []), slug=slug,
            path=f"{L[lang]['index']}{slug}/",
            html=markdown.markdown(body_md, extensions=["extra", "sane_lists", "smarty"]),
            minutes=max(1, round(words / 220)),
        ))
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def post_card(p):
    t = L[p["lang"]]
    return (f'<div class="card"><p class="num">{fmt_date(p["date"], p["lang"])} · {p["minutes"]} {t["minutes"]}</p>'
            f'<h2 style="font-size:1.3rem"><a href="{p["path"]}" style="text-decoration:none;color:var(--ink)">{esc(p["title"])}</a></h2>'
            f'<p>{esc(p["description"])}</p><a class="more" href="{p["path"]}">{t["read"]}</a></div>')


def index_page(lang, posts):
    t = L[lang]
    crumbs = [(t["home_name"], t["home"]), (t["name"], t["index"])]
    mine = [p for p in posts if p["lang"] == lang]
    if mine:
        content = f'<div class="grid grid-3">{"".join(post_card(p) for p in mine)}</div>'
    else:
        content = f'<p class="lead" style="color:var(--muted)">{t["empty"]}</p>'
    body = (page_hero(t["name"], t["lead"], crumbs)
            + f'<section><div class="wrap">{content}<p style="margin-top:28px;font-size:.92rem"><a href="{t["feed"]}">{t["rss"]}</a></p></div></section>'
            + cta_band(lang))
    schema = {"@context": "https://schema.org", "@type": "Blog", "name": t["feed_title"], "url": BASE + t["index"],
              "inLanguage": t["inlang"], "publisher": {"@id": ORG_ID},
              "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": BASE + p["path"],
                            "datePublished": p["date"].isoformat()} for p in mine]}
    other = "pt" if lang == "en" else "en"
    return dict(lang=lang, path=t["index"], title=t["title"], description=t["desc"], body=body,
                alternates={"en-GB": L["en"]["index"], "pt-PT": L["pt"]["index"]}, alt_path=L[other]["index"],
                schemas=[schema, breadcrumb_schema(crumbs)], noindex=not mine)


def article_page(p):
    t = L[p["lang"]]
    crumbs = [(t["home_name"], t["home"]), (t["name"], t["index"]), (p["title"], p["path"])]
    meta = f'{t["by"]} <a href="{t["about_link"]}">Steve Campbell</a> · {fmt_date(p["date"], p["lang"])} · {p["minutes"]} {t["minutes"]}'
    hero = page_hero(esc(p["title"]), meta, crumbs)
    body = (hero + f'''<section><div class="wrap narrow">
<article class="prose">{p["html"]}
<p class="note" style="font-size:.9rem"><em>{t["note"]}</em></p></article>
<div class="author-box"><picture><source srcset="/assets/img/steve-campbell-2026.webp" type="image/webp"><img src="/assets/img/steve-campbell-2026.jpg" width="72" height="72" alt="Steve Campbell"></picture>
<div><strong>Steve Campbell</strong> <span style="color:var(--muted)">{POSTNOMS}</span><p>{t["about"]}</p><a href="{t["about_link"]}">{t["about_cta"]} →</a></div></div>
</div></section>''' + cta_band(p["lang"]))
    schema = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["description"], "url": BASE + p["path"],
        "mainEntityOfPage": BASE + p["path"], "inLanguage": t["inlang"],
        "datePublished": p["date"].isoformat(), "dateModified": p["date"].isoformat(),
        "author": {"@id": PERSON_ID, "@type": "Person", "name": "Steve Campbell", "url": BASE + "/about/"},
        "publisher": {"@id": ORG_ID}, "image": BASE + "/assets/img/og-image.jpg",
        "keywords": ", ".join(p["tags"]) or None,
    }
    schema = {k: v for k, v in schema.items() if v}
    return dict(lang=p["lang"], path=p["path"], title=f'{p["title"]} | Steve Campbell', description=p["description"],
                body=body, alternates={t["inlang"]: p["path"]}, alt_path=L["pt" if p["lang"] == "en" else "en"]["index"],
                og_type="article", schemas=[schema, breadcrumb_schema(crumbs)])


def rss(lang, posts):
    t = L[lang]
    mine = [p for p in posts if p["lang"] == lang]
    now = dt.datetime.now(dt.timezone.utc)
    items = []
    for p in mine:
        pub = dt.datetime.combine(p["date"], dt.time(9, 0), tzinfo=dt.timezone.utc)
        items.append(f'''  <item>
    <title>{html.escape(p["title"])}</title>
    <link>{BASE}{p["path"]}</link>
    <guid isPermaLink="true">{BASE}{p["path"]}</guid>
    <pubDate>{format_datetime(pub)}</pubDate>
    <dc:creator>Steve Campbell</dc:creator>
    <description>{html.escape(p["description"])}</description>
    <content:encoded><![CDATA[{p["html"]}]]></content:encoded>
{"".join(f"    <category>{html.escape(c)}</category>" + chr(10) for c in p["tags"])}  </item>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>{html.escape(t["feed_title"])}</title>
  <link>{BASE}{t["index"]}</link>
  <atom:link href="{BASE}{t["feed"]}" rel="self" type="application/rss+xml"/>
  <description>{html.escape(t["desc"])}</description>
  <language>{t["inlang"].lower()}</language>
  <lastBuildDate>{format_datetime(now)}</lastBuildDate>
  <image><url>{BASE}/icon-512.png</url><title>{html.escape(t["feed_title"])}</title><link>{BASE}{t["index"]}</link></image>
{chr(10).join(items)}
</channel>
</rss>
'''
