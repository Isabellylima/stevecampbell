# Blog posts

One Markdown file per article. The file name becomes the web address (e.g. `party-wall-basics.md` → `/blog/party-wall-basics/`).

Each file starts with a header:

```
---
title: Article title
date: 2026-11-20
description: One or two sentences for Google, AI answers, the blog list and the RSS feed.
lang: en          # en → /blog/ and /feed.xml · pt → /pt/blog/ and /pt/feed.xml
draft: false      # true keeps the article unpublished
tags: [Party wall]
---
```

Then the article in Markdown: `## Heading`, `- list item`, `1. numbered`, `**bold**`, `*italic*`, `[link text](/contact/)`.

Publish: `python3 build/build.py`, then commit and push. Preview drafts locally: `BLOG_DRAFTS=1 python3 build/build.py` (do not commit that build).

The blog appears in the menu and footer automatically once a language has at least one published article. RSS feeds: `https://stevecampbellassociates.com/feed.xml` (English) and `/pt/feed.xml` (Portuguese).
