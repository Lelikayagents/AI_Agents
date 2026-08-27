# Source playbook — where the non-obvious data actually is

The rule behind every entry here: **secondary sources are leads, not evidence.** A news article, an aggregator page, a Statista chart or a consultancy press release is useful for finding the document; the document is what gets cited. Statista in particular always names its underlying source — go to that source and cite it instead.

## Evidentiary weight

| Tier | What | Treat as |
|---|---|---|
| 1 | Filed financial statements, official registers, published acts, court decisions, procurement contracts, regulator enforcement files | Evidence. Cite directly. |
| 2 | Company's own operational artifacts: price lists, ToS, changelogs, job postings, investor decks, patent/trademark filings | Evidence about that company's behaviour. |
| 3 | Panel and telemetry data (Mediascope, Яндекс Радар, SimilarWeb, app-store trackers), industry-association statistics | Directional. Cite with the method caveat. |
| 4 | Trade press, analyst notes, aggregator profiles, expert interviews in media | Leads. Cite only when nothing better exists, and label it. |
| 5 | Vendor blogs, "market to reach $X bn by 2030" press releases, LLM-generated summaries | Not evidence. Use to find tier 1–2, never to support a number. |

Two outlets reprinting the same press release are one source. Corroboration means a second *independent* observation.

---

## Russia

### Company-level truth: registers and accounts

This cluster is the single biggest edge available on Russian markets, because filed accounts for every legal entity are public and free, and almost nobody reads them.

- **ГИР БО — `bo.nalog.ru`.** Annual accounting statements of every Russian legal entity from 2019 onward, downloadable. Revenue, cost of sales, gross and net profit, receivables, payables, fixed assets. This is how you get a named competitor's actual revenue and margin instead of an estimate. Multi-year series here reveal trajectory, and the explanatory notes (пояснения) where filed are where the segment detail hides.
- **ЕГРЮЛ/ЕГРИП — `egrul.nalog.ru`.** Free extract by ИНН/ОГРН: founders and their shares, director, registered address, ОКВЭД codes, and the dated history of changes. A change of owner or director is a leading indicator; a new ОКВЭД code is a stated intent to enter a business line.
- **Прозрачный бизнес — `pb.nalog.ru`.** Headcount, tax regime, taxes actually paid, aggregate income and expenses, arrears, special-regime status. Headcount here plus revenue from ГИР БО gives revenue per employee, which is often more diagnostic than either alone.
- **Единый реестр МСП — `rmsp.nalog.ru`.** Micro/small/medium classification with dates — a fast read on the size distribution of an entire ОКВЭД segment.
- **Aggregators — `rusprofile.ru`, `checko.ru`, `list-org.com`.** Faster to navigate and good for finding affiliated entities and group structure. Use them to locate; cite the underlying register.

### Prices and demand nobody publishes

- **ЕИС госзакупки — `zakupki.gov.ru`.** Contracts under 44-ФЗ and 223-ФЗ carry the specification, the winner, and the actual price paid. For B2B and B2G categories this is frequently the only public source of real transaction prices, and the contract history shows which buyers renew and which switch suppliers.
- **`torgi.gov.ru`** — state property auctions; useful for asset values in capital-heavy sectors.
- **Wordstat — `wordstat.yandex.ru`.** Search-query frequency with regional breakdown and month-over-month history. The best free proxy for demand in Russia, and the query wording itself is the customers' vocabulary (see the audience section of `analysis-frameworks.md`). Note it measures interest, not purchase.
- **СберИндекс — `sberindex.ru`.** Consumer spending by category and region, updated far faster than official statistics.

### Official statistics

- **Росстат — `rosstat.gov.ru`**, and **ЕМИСС — `fedstat.ru`** for indicator-level series by region and industry.
- **Банк России — `cbr.ru/statistics`.** Also publishes sector reviews (МФО, страхование, брокеры, НПФ) containing market shares and concentration measures that would be expensive to reconstruct.
- **ФТС — `customs.gov.ru`** for foreign-trade aggregates.

### Regulatory and legal signals

- **`publication.pravo.gov.ru`** — the citable text of laws, decrees and government resolutions. On any Russian legal point this outranks every summary. Retrieval recipes, including the publication-number scheme and the HTML-escaping trap, are in the sibling `legal-re-reserch` skill's `references/ru-primary-sources.md`.
- **`regulation.gov.ru`** — draft regulations in public consultation. This is regulation three to twelve months before it exists, and it is where a coming market shift is visible first.
- **ФАС — `fas.gov.ru`.** Decisions in competition cases routinely contain the regulator's own market-share calculations and market-boundary definitions for a specific product market — a level of detail that no commercial report will give away for free. Search enforcement decisions by the sector, not just by company name.
- **Licence and accreditation registers** — Росаккредитация (`fsa.gov.ru`), Росздравнадзор, Bank of Russia registers of licensed entities. A count of licence holders over time is a clean entry/exit series for a regulated market.
- **Courts.** `kad.arbitr.ru` and `ras.arbitr.ru` return HTTP 451 from this environment and there is no workaround; `sudact.ru` needs JavaScript. Fall back to specific reporting from «Право.ру», «Коммерсантъ», «Интерфакс», РБК and label the finding as resting on press reporting.

### Intent, brand and talent

- **Роспатент / ФИПС — `fips.ru`.** Open registers of trademarks and patents. A trademark application typically precedes a public launch by months, so filings map an incumbent's product roadmap before any announcement.
- **`hh.ru`.** Vacancy counts, salary bands, tech stack and locations. What a company hires for is its strategy stated in a form it cannot spin: a burst of hiring in one function is a bet, and a hiring freeze in another is a retreat.
- **Reviews as pain data** — Яндекс Карты and 2GIS for local businesses, `banki.ru` for financial products, `irecommend.ru` and `otzovik.com` for consumer goods, marketplace reviews for e-commerce. Read one- and two-star reviews first: they name the unsolved job.
- **Industry associations** publish the only category-level numbers in some sectors — АКИТ and Data Insight (e-commerce), АКАР (advertising), and the equivalents in autos, logistics and pharma.

---

## International

- **SEC EDGAR full-text search — `efts.sec.gov` / `sec.gov/edgar/search`.** For any listed player: segment reporting gives revenue and operating margin by business line; the risk-factors section is management's own written list of what could kill them; the MD&A explains volume-versus-price. Search the full text for a competitor's or customer's name to find who discloses a dependency on whom.
- **Earnings-call transcripts.** Analyst Q&A is where the numbers management left out of the deck get extracted. The questions asked repeatedly across quarters mark what the sell side thinks is fragile.
- **UN Comtrade** for trade flows by commodity code — the cleanest way to see who actually ships what to whom, including through re-export routes.
- **World Bank, OECD, Eurostat, IMF** for macro and cross-country comparators; **Our World in Data** for tidy long series.
- **Google Patents (`patents.google.com`), USPTO, WIPO Global Brand Database** — the international analogue of the ФИПС play.
- **Google Trends** for demand direction outside Russia; combine with Wordstat rather than substituting one for the other.
- **App-store charts and trackers** (Sensor Tower, appfigures, data.ai — the free tiers plus public rankings) for consumer-app categories; **SimilarWeb** for web traffic, always cited as an estimate with its method caveat.
- **Crunchbase, Dealroom, PitchBook** for funding — where capital went is a map of what informed people believe, and a category with rounds but no revenue disclosure is a category to be sceptical about.
- **Glassdoor, Levels.fyi, LinkedIn headcount trends** for cost structure and organisational shape.
- **G2, Capterra, TrustRadius, Trustpilot, Amazon reviews.** In B2B software especially, the review corpus is a free, continuously updated feature-gap and churn-reason dataset.
- **Communities where practitioners talk unguarded** — Reddit subject subreddits, Hacker News threads, niche Discord and Slack groups, professional forums. Treat as qualitative signal, quote sparingly, never as a statistic.
- **Wayback Machine — `web.archive.org`.** Underrated. Diff a company's pricing page, terms of service, careers page or homepage across years: a price rise, a removed free tier, a changed usage limit or a quietly dropped product line is a strategy change with a date attached, and it is almost never announced.

## Practical rules

- **Fetch every URL you cite.** A URL that looks right and was never opened is a fabrication, and it is the single most damaging error this skill can make.
- **Record the source at the moment you take the number**, not afterwards.
- **Note the unit, period and currency** every time. Mixing a calendar year with a fiscal year, or ₽ with $ at an unstated rate, silently corrupts every derived figure downstream.
- **When a source is paywalled or unreachable**, say so at the claim and state what it would have settled — do not quietly substitute a weaker source.
