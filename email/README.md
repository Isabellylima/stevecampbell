# Email campaigns

`campaign-construction-disputes.html` — campaign based on Steve's flyer (Nov 2026).

- Images are served from the website: `public/assets/email/` (crest, hero, three service photos).
- Written for HubSpot: `{{ personalization_token('contact.firstname', 'colleague') }}` and `{{ unsubscribe_link }}`.
  For Mailchimp replace them with `*|FNAME|*` and `*|UNSUB|*`.
- Tables and inline styles only, so it works in Outlook, Gmail and Apple Mail; three columns stack on mobile.
