# Retrieving Russian primary sources

Concrete recipes for getting to the published text of an act. Read this before starting retrieval — several of these are non-obvious and each one costs real time to rediscover.

## Contents

- [publication.pravo.gov.ru](#publicationpravogovru) — laws, decrees, government resolutions
- [Bank of Russia](#bank-of-russia) — ukazaniya, positions, drafts, consultation reports
- [Court decisions](#court-decisions) — and what to do when the databases are blocked
- [Reading scanned and broken PDFs](#reading-scanned-and-broken-pdfs)
- [Cross-checks that need no source](#cross-checks-that-need-no-source)

## publication.pravo.gov.ru

The official publication portal. Every federal law, presidential decree and government resolution appears here on the day of publication, and this is the citable text.

**Publication numbers.** Each document has a 16-digit `eoNumber`: `0001` + `YYYYMMDD` + a 4-digit index within that day. So the ninth document published on 24 August 2026 is `0001202608240009`.

- Document page: `http://publication.pravo.gov.ru/document/{eoNumber}`
- PDF: `http://publication.pravo.gov.ru/file/pdf?eoNumber={eoNumber}`

Other URL shapes (`/document/pdf/...`, `/api/Document/GetPdf`) return 404 — use the two above.

**Finding the number when you only have "Указ № 550 от 04.08.2026".** Enumerate the day: request `/document/0001{YYYYMMDD}{index}` for index 1…~150 and read the `<title>`, which contains the act type, date and number. Documents are not in numeric order within a day — 548, 551, 552 can precede 550 — so scan the whole range rather than stopping at the first near-miss.

**The gotcha that will silently break this.** Page titles are returned HTML-escaped (`&#x423;&#x43A;&#x430;&#x437;` for «Указ»). A plain substring match for Cyrillic finds nothing and returns a clean empty result that looks like "this document doesn't exist." Unescape the title before matching. If a scan returns zero hits across several days, suspect this before concluding the act isn't there.

**Fetching.** The portal returns 503 to some URL-fetching tools but serves a plain `curl` with an ordinary browser User-Agent. Prefer `curl` here.

## Bank of Russia

**Registered normative acts** (указания, положения). Search `https://www.cbr.ru/search/?text=<номер>` — e.g. `7402-У`. The results HTML contains a link of the form `/ref/analytics/na_vr/file/NNNN`, which is the act's PDF. The `/na/?la.Search=...` page is JavaScript-rendered and returns nothing useful to a plain fetch.

**News and press releases**: `https://www.cbr.ru/press/event/?id=NNNNN`. Useful for dating a publication and for the regulator's own framing, but the operative detail is in the attached document.

**Draft acts for public consultation**: linked from the press release as `/StaticHtml/File/NNNNN/....pdf`. These have a real text layer. The **пояснительная записка at the end of the file** is where the consultation window, the planned adoption quarter, and the planned entry-into-force dates live — check digest claims about those against that note, not against news coverage.

Note that explanatory notes are themselves a known source of wrong citations to the act being replaced. Verify the replaced act independently.

**Consultation reports** ("Отчёт об итогах публичного обсуждения доклада") are published under `/Content/Document/File/NNNNNN/report_DDMMYYYY.pdf` and have a clean text layer. The "Ключевые направления" section near the front is usually what a digest is summarising.

## Court decisions

`kad.arbitr.ru` and `ras.arbitr.ru` return **HTTP 451** from most non-Russian networks, including this environment. There is no workaround — do not spend time on it. `sudact.ru` requires JavaScript for search.

What to do instead:

- Reputable outlets reporting specifics — «Деловой Петербург», ПРАЙМ, «Интерфакс», РБК, «Право.ру», «Коммерсантъ» — are the best available evidence for case number, date, parties, amounts and outcome. Label such findings as resting on press reporting rather than on the text of the decision.
- Constitutional Court and Supreme Court positions cited *inside* a digest can usually be confirmed through legal-commentary coverage, which quotes them; confirming that the cited position exists and says roughly what the digest claims is worth doing even when the full text is out of reach.
- Say plainly in the report which court items you could not reach. An unverified case number is a real residual risk for the editor.

## Reading scanned and broken PDFs

**Scans with no text layer.** Most `publication.pravo.gov.ru` PDFs are page images: text extraction returns zero characters. There is no OCR binary in this environment (`pdftoppm`, `tesseract` are absent), so render pages to PNG with PyMuPDF and read the images directly.

```python
import pymupdf
d = pymupdf.open("act.pdf")
for i, p in enumerate(d):
    p.get_pixmap(dpi=170).save(f"act_p{i+1}.png")
```

170 dpi is legible without being wasteful. Read page 1 (title, preamble, first operative paragraph) and the **last page** (entry into force, signature, date and number) first — that pair settles most claims. `pypdf` may fail to import here because the `cryptography` backend is broken; PyMuPDF has no such dependency.

**Broken font encoding.** Some Bank of Russia PDFs have a text layer whose Cyrillic cmap is wrong: the text extracts as garbage like `квaлифициpoBaIIнЬIМ иIrBесTopoМ`. Do not discard it. Digits, Latin script, punctuation and document structure survive intact, and those are usually exactly what you are checking — thresholds, article references, periods, certificate names in Latin. Grep the garbled text for numbers and for `статьи`/`пункта` fragments; the surrounding words are readable with a little effort.

## Cross-checks that need no source

When the primary text is out of reach, arithmetic can still discriminate.

**State fee against claim value** (arbitration, ст. 333.21 НК РФ, scale in force since 09.09.2024):

| Цена иска | Пошлина |
|---|---|
| до 100 000 ₽ | 10 000 ₽ |
| 100 001 – 1 000 000 ₽ | 10 000 ₽ + 5% свыше 100 000 |
| 1 000 001 – 10 000 000 ₽ | 55 000 ₽ + 3% свыше 1 000 000 |
| 10 000 001 – 50 000 000 ₽ | 325 000 ₽ + 1% свыше 10 000 000 |
| свыше 50 000 000 ₽ | 725 000 ₽ + 0,5% свыше 50 000 000 (не более 10 000 000) |

A reported fee pins the claim value to within a rounding error, which independently corroborates or contradicts the amount a digest states — including across a currency conversion.

**Entry into force by default rule**, where the act itself is silent:

- Federal laws — 10 days after official publication, unless the law says otherwise (ФЗ от 14.06.1994 № 5-ФЗ).
- Presidential and government acts affecting rights, freedoms and duties, or the legal status of federal bodies and organisations — 7 days after first official publication; other such acts — from the day of signing (Указ Президента РФ от 23.05.1996 № 763, п. 6).
- Registered Bank of Russia acts — normally 10 days after official publication, but the act states its own rule in the final chapter; read it rather than assuming.

A digest that states one of these without the act saying it is making a correct inference, not quoting — flag it as such.

**Act numbering as a plausibility check.** Bank of Russia acts are numbered sequentially and continuously. A «Положение № 534-П» cannot date from 2020, because by January 2020 the series had reached 710-П. When a cited number and date are inconsistent with the series, one of them is wrong — usually the date.

**Period arithmetic.** "По истечении N дней после дня официального опубликования" counts from the day *after* publication, and the act takes effect on the day after the period ends. 180 days from publication on 4 August 2026 puts entry into force on 1 February 2027, not 31 January.
