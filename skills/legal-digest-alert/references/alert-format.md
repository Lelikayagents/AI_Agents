# Alert / brief format ("SBL Alert" and, by extension, a "справка")

An Alert is a deep, single-topic analysis written for a client who needs to understand exactly what changed and what it means for them — the whole point is to demonstrate that the firm caught the change fast and understands it in depth. Where the digest reports, the Alert *advises*.

Use this same shape for a **справка** (a memo answering one specific client legal question) — treat the question itself as the "development" the Alert would normally open with, and keep the closing recommendations section, since a справка without a practical answer at the end isn't useful to the client.

This file was revised after a partner edit-pass over a real Alert draft. Where the partner's markup contradicted the earlier version of this file, the markup wins and is recorded below.

## Output medium

Word `.docx` built on the firm's template, not a slide deck. Reuse the template's `styles.xml`, header and footer rather than building a document from scratch — see "Word styles" below for the exact style IDs. (Slide decks remain the medium for periodic digests; an Alert is a memo.)

## Document structure

**Title.** Paragraph style `SBLParaHeadingv1` (plain bold paragraph) — *not* the `Title` style, and no horizontal rule. Keep it short and generic rather than packing the instrument's number and a "what changes" clause into it. "Изменение законодательства о раскрытии информации эмитентом ценных бумаг" is the register; "Новая редакция Положения Банка России № 714-П: что меняется в раскрытии информации при первичном размещении акций" is too long and too specific for the title line — that detail belongs in the opening paragraph.

**No date line on the cover.** The template header already carries "Конфиденциально / Проект от [дата]" as an auto-updating field. Do not add a centred date under the title.

**Opening paragraph.** What happened, when, who did it, full citation of the instrument with its number, and the short defined name introduced via `(далее - «[Name]»)`. Include a hyperlink to the source document where one exists, rendered as `(см. >>>)` with `>>>` carrying the link.

**Second paragraph: an explicit roadmap.** State in the first person what the Alert will cover, and introduce the remaining defined terms there. Example shape: *"Мы разберем как новое Положение снижает регуляторную нагрузку … и одновременно расширяет требования к раскрытию информации: составление резюме проспекта (далее - «Резюме») …, включение в него прогноза проспекта (далее - «Прогноз») и расширение случаев опубликования эмитентом сообщений о существенном факте."* This paragraph is expected; don't jump straight from the opening into the first section.

**Body sections.** Paragraph style `SBLRUSL1` ("SBL_RUS L1") — bold with automatic numbering, so sections read 1, 2, 3… **Sections are numbered.** (An earlier version of this file said headings are unnumbered; that was wrong.) Headers are topical, one line, no sub-numbering scheme like the digest's `1.1`.

**Closing section.** Always the last numbered section, titled "Наши предложения и рекомендации" — see below.

## Word styles (from the firm template)

| Element | Style ID |
|---|---|
| Alert title | `SBLParaHeadingv1` |
| Numbered section heading | `SBLRUSL1` |
| Body text | `BodyText` |
| Lettered recommendations (a), (b)… | `BodyText` (plain paragraphs, not a list style) |

Bulleted lists use the template's bullet numbering definitions; nested bullets are used where the source has that nesting (e.g. blocks 1.12 and 1.13 nested under a parent bullet covering 1.12–1.13).

## Text conventions

These are hard rules, taken from the partner markup:

- **No "ё".** Write "прошел", "еще", "объем", "отчетность", "зеленые".
- **No em dash "—" anywhere.** Use a hyphen with spaces: `(далее - «Положение»)`, `Период прогноза - не менее 12 месяцев`, `IPO - наименее подходящий момент`. An en dash "–" is fine inside numeric ranges (`1.2–1.5`). If a sentence wants an em dash for emphasis, rewrite it — e.g. "Срок раскрытия … это риск для графика сделки", not "Срок раскрытия … — риск для графика сделки".
- **Defined terms in bold italic** at the point of definition: ***«Положение»***, ***«Резюме»***, ***«Прогноз»***, ***«lock-up»***, ***«соглашение о стабилизации»***. Define generously — anything used more than twice earns a defined term.
- **Placeholders highlighted yellow** so the reviewer cannot miss them: `[ДД.ММ.ГГГГ]`, `[со дня его принятия]`. The instrument's number placeholder is written `[●]`, not `[___]`.
- **Bold lead-ins** are used to open a paragraph or bullet that covers a named sub-topic (**«Аллокация.»**, **«Стабилизация.»**, **«раздел о лицах, подписавших проспект»**).
- **Russian term before the English one** in headings and at first use: "ограничение на обращение акций (lock-up)", not "lock-up (ограничение на обращение акций)".
- **"и" before the final item** of a lettered list: `(d) … ; и` then `(e) …`.
- No grey-italic "caveat" formatting for unverified points. Either state the point plainly or leave it out; open questions go into the recommendations section.

## Use lists, not dense prose

Enumerations belong in bulleted lists, including nested ones. A paragraph that runs through six or eight items separated by semicolons should be a list instead. This applies to structural walk-throughs (the thirteen blocks of a prospectus summary), to sets of required disclosures, and to the closing recommendations.

## What to leave out

The partner pass cut all of the following. Treat these as default exclusions:

- **Drafting-history comparisons.** "Обсуждавшийся на консультациях 2025 года лимит в 7 страниц смягчен", "а не календарный год, как обсуждалось", "хотя на консультациях предлагалось именно это". The client needs the rule as adopted, not the negotiation history. Mention an earlier proposal only when the gap between it and the final text creates a live practical question.
- **Regulator statistics and background citations** that don't change what the client should do (e.g. the number of an information letter plus the share of issuers that ignored it).
- **Evaluative preambles** — "Самое существенное содержательное изменение:", "Наиболее значимое нововведение". Open with the rule.
- **Meta-commentary on market consultation** ("участники рынка указывали Банку России на этот риск").
- Analysis that restates a point already made in another section.

Analytical depth still belongs in the Alert — where a provision is ambiguous, internally inconsistent, or silent on something the client must decide (e.g. a disclosure requirement with no prescribed calculation methodology), walk through it and say what to do. That is the product's value. What gets cut is background, not analysis.

## Closing section: "Наши предложения и рекомендации"

Mandatory. Structure:

1. One lead-in paragraph saying why the change matters to this client's role specifically.
2. Lettered recommendations `(a)`, `(b)`, `(c)`… — concrete actions, each tied to a provision discussed above. "и" before the last one.
3. A closing paragraph naming the risk of inaction in specific terms, tied to the effective date.

## Citation discipline

Every legal instrument named gets its full official title, number, and date, verbatim, at the point it's introduced — never paraphrase a title or drop a number. Article and clause references are reproduced exactly as they appear in the source (`п. 1 ст. 29.6 Федерального закона «О рынке ценных бумаг»`).

## Footer and contacts

The firm template's header and footer carry the confidentiality marking and page numbers. Where an Alert is issued as a deck rather than a memo, reproduce on every content slide after the cover:

> © ООО «Стоунбридж Лигал», [year]. Сведения и материалы, представленные в настоящем документе, подготовлены исключительно в информационных целях и не являются юридической консультацией или заключением.

Firm contact details for a closing contact slide:

```
+7 495 785 30 00
marketing@stonebridgelegal.ru

119017, Россия, Москва
Кадашёвская наб, д. 14, к. 2
```
