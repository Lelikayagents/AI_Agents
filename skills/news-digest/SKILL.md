---
name: news-digest
description: Deliver a compact, cleanly formatted weekday news digest covering business/markets (РБК, FT, Bloomberg), the AI sector, socio-political news (Новая газета), and new Russian legislation with a short comment and a link to the act's text for each item. Picked for a capital-markets/financial & banking lawyer. Nothing invented — every item links to its source, and new-law items link to the primary text. Fires automatically via a 10:30 Moscow routine on weekdays; also usable on demand for "дай сводку новостей".
---

# News Digest

## Purpose

A five-to-ten-minute morning read: what moved in business and markets, what
moved in the broader public conversation, and what changed in the law
yesterday — for a lawyer working in capital markets, financial and banking
law.

## Sources

- **Деловые/рыночные новости:** РБК, FT, Bloomberg. If one of these is
  paywalled past the headline, summarize from the headline, lead, and
  whatever open outlets are quoting or re-reporting the same story — the
  link still goes to the original FT/Bloomberg piece, not the reprint.
- **Сектор ИИ:** FT and Bloomberg both run a dedicated tech/AI beat, so
  start there; add specialist coverage when the main four don't have the
  story — TechCrunch, The Information, Reuters Tech, Ars Technica for the
  global side, VC.ru or Коммерсант for the Russian AI/tech market. Covers
  models and labs, AI regulation, major funding rounds and M&A, and AI
  products/moves from companies relevant to finance and capital markets.
- **Общественно-политические новости:** Новая газета.
- **Новое законодательство:** `publication.pravo.gov.ru` for the
  authoritative text of anything signed into law; the regulator's own site
  (`cbr.ru`, `moex.com`, `minfin.gov.ru`) for CBR/exchange/Minfin acts and
  releases; `sozd.duma.gov.ru` for bills still in the legislative process.
  КонсультантПлюс, Гарант and the press are fine for *finding* an act, never
  as the source for what it says.
- **When the four named sources are thin on a genuinely important story of
  the day**, pull in a reputable outlet to cover it properly — Коммерсант,
  Интерфакс, Reuters, or a direct CBR/exchange press release. Don't force
  the gap to stay empty, and don't pad it with something minor just because
  it came from one of the four.

Never invent a link or a source — an item with no real, checkable link does
not go in the digest.

## What goes in and how much

Four sections, in this order, compact rather than exhaustive:

1. **Деловые и рыночные новости** — 3-5 items.
2. **Сектор ИИ** — 2-3 items: models/labs, AI regulation, major funding
   rounds and M&A, notable product moves — prioritize whatever intersects
   finance, capital markets or banking, but a big AI story stands on its
   own even without that angle.
3. **Общественно-политические новости** — 1-3 items.
4. **Новое законодательство** — up to 3-4 acts (signed laws, major CBR/
   exchange regulations, or significant bills that cleared a reading), each
   with a short comment on what actually changes and for whom — not just a
   restated headline — plus the link to the act's text.

Pick what is genuinely significant for the day, not whatever fills the
quota: a thin day can run shorter, a heavy day can run slightly over,
within reason. Favor stories relevant to capital markets, banking and
financial law and major business/economic events; the socio-political
section can be broader.

## Researching it

Search live for each section — do not answer from memory, and do not
reuse yesterday's items just to fill space. News digests are about what
changed since the last issue (previous ~24h on a weekday, since weekends
are skipped — so Monday's issue should cover from Friday).

## Writing it up

- Write in Russian. Translate/adapt FT and Bloomberg headlines and leads
  rather than leaving them in English.
- Format as clean chat markdown, built to be pleasant to read on a phone:
  a short date header, then the four sections as `##`/`###` headings,
  each item as a tight bullet — one bold lead phrase, one or two sentences
  of substance, the source and link at the end of the line. No filler
  introductions or closing summaries; let the bullets carry it.
- Every item ends with a link: to the article for news, to the act's
  primary text for legislation.

## Delivering it

Reply directly in the chat of the session this fires into. No separate
document or artifact.

## Cadence

Normally triggered by a Routine at 10:30 Moscow time on weekdays (Mon-Fri).
Also fine to run on an ad-hoc request ("дай сводку новостей", "что нового
за сегодня") at any other time.
