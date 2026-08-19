# Translation Pattern Bank (RU ↔ EN)

This file is the memory of *how this user translates*. It is not a general legal
dictionary — it records the specific choices this user has made or approved, so
that the same source wording gets the same target wording every time, across
documents and across sessions.

**Standing priority, stated explicitly by the user (2026-08-19): meaning fidelity
comes before fluency.** When reviewing or producing a translation, actively hunt
for places where the target text says something different from the source —
homonym traps (e.g. «Акция» = Share vs. promotion — verify by context every
time), reversed agency/classification direction, collapsed legal distinctions
(e.g. отказ vs расторжение vs прекращение all flattened to "terminate"),
undefined-term references introduced by inconsistent rendering of a defined
term, and outright invented content (e.g. a currency added to a blank the
source left unspecified). Flag these as meaning-level defects, not style notes —
they outrank terminology-consistency and register concerns when the two
conflict.

**Git commit/push cadence, stated by the user (2026-08-19):** keep editing this
file locally after every turn as usual, but only `git commit` + `git push` once
every 5 messages/turns (not after every single edit) to save tokens. Track
turns-since-last-push mentally; batch the accumulated edits into one commit
when the count is reached, or sooner if the user asks to see it pushed.

## How to use this file

**Before translating** — read Sections A–E. If a source term or construction has
an entry here, use that rendering. A locked entry (Section A) overrides your own
instinct, a standard dictionary, and the defaults in Section F. Do not "improve"
a locked rendering for style.

**Lookup workflow for single-word requests, stated by the user (2026-08-19):**
when the user gives a single word/term to translate, check this file first. If
it isn't already recorded here, look it up on multitran.com (via WebFetch),
preferring the юридический (legal/juridical) sense of the entry over general
or other-domain senses. Record the result afterward per the workflow below.

**After translating** — when the user corrects, replaces, or confirms a
rendering, write it into this file in the same turn. A correction that is not
recorded will be made again next week. Every entry needs a date and a short
source note (which document it came from) so a later disagreement can be traced
back.

**Precedence when entries conflict:** A (locked) → C (corrections) → B
(provisional) → F (defaults). Newer entry beats older within the same section.

---

## A. Locked renderings — confirmed by the user

Terms the user has explicitly approved or supplied. Bind unconditionally.

| RU | EN | Direction | Note | Added | Source |
|---|---|---|---|---|---|
| правопреемники и лица, принявшие права и/или обязанности Стороны | legal successors and assignees | EN→RU | User picked over «цессионарии» (too narrow — rights only) and over a full descriptive gloss (too long); keeps the two-part structure of the source while covering both cession and перевод долга | 2026-08-14 | successors clause, chat |
| требование | demand | RU→EN | Confirmed twice now: «претензии и (или) требования» → «claims and (or) demands» (governing-law clause), and again by position in «жалоб, требований, предписаний, претензий, судебных исков» → «complaints, demands, orders, claims, lawsuits» (confidentiality clause, 2026-08-18). Supersedes the earlier (wrong) provisional guess требования=claims | 2026-08-14 | governing-law/dispute-resolution + confidentiality clauses, parallel text |
| претензия | claim | RU→EN | Confirmed twice — see требование row above for the second confirmation. Note: a separate occurrence elsewhere («внедоговорные требования» → «non-contractual claims») uses требования=claims instead — the user's own text is not fully consistent there; flagged, not silently resolved | 2026-08-14 | governing-law/dispute-resolution + confidentiality clauses, parallel text |
| жалоба | complaint | RU→EN | New, from the same five-item list confirming требование/претензия above. Note this is the word my very first (wrong) guess had mapped to «претензия» instead — closes that loop | 2026-08-18 | confidentiality clause, parallel text |
| предписание | order | RU→EN | Same five-item list | 2026-08-18 | confidentiality clause, parallel text |
| судебный иск | lawsuit | RU→EN | Same five-item list | 2026-08-18 | confidentiality clause, parallel text |
| SAPA | SAPA | EN→RU | Explicit user instruction: leave untranslated/untransliterated as a term, both directions | 2026-08-18 | chat |
| абзац | paragraph (generic contexts) / indent (this document family) | RU→EN | REVISED 2026-08-19 per user: collides with the already-locked «Параграф» (capitalized) = "Paragraph" (structural term, Interpretation clause). To avoid confusing the two in this document family, render generic «абзац» as lowercase "indent" instead (also a valid multitran legal-category sense) whenever «Параграф»/"Paragraph" is also in play in the same document. Outside that collision risk, lowercase "paragraph" is fine | 2026-08-19 | word-list lookup, chat |
| Арбитражный суд города Москвы | the Commercial Court of the city of Moscow | RU→EN | Locked as a model-good pattern: avoids the classic false-friend "Arbitration Court" — «арбитражный суд» is Russia's state commercial-court system, not private arbitration. Use "Commercial Court" (or transliterated "Arbitrazh Court"), never "Arbitration Court" | 2026-08-14 | governing-law/dispute-resolution clause, parallel text |
| третейское разбирательство / третейский суд | arbitration / arbitration proceedings | RU→EN | Confirms the distinction above: this is genuine private arbitration (unlike «арбитражный суд») and is correctly rendered "arbitration", not "Commercial Court" | 2026-08-18 | liability/termination clauses, parallel text |
| Статья N (whole-number, incl. cited statute articles e.g. ГК РФ) | Clause N | RU→EN | CONFIRMED AUTHORITATIVELY 2026-08-18: the document's own Interpretation clause (1.1) states «Статья» maps into "Clause" directly. No longer an inference from usage — it's the document's own definition. Previously also confirmed by repeated usage incl. Civil Code citations | 2026-08-18 | liability/termination/expenses + Interpretation clauses, parallel text |
| Пункт N.M / N.M(x) (decimal, incl. sub-items) | Clause N.M / Clause N.M(x) ("sub-clause") | RU→EN | CONFIRMED AUTHORITATIVELY 2026-08-18: the Interpretation clause (1.1) explicitly defines «Пункт» as "sub-clause", collectively covered by "Clause" together with «Статья». NOTE: clause 1.12 of the same Interpretation section appears to violate its own rule — it renders «пунктов» as "paragraphs" instead of "sub-clauses"/"Clauses", conflicting with 1.1. Flag this as a likely error in 1.12 rather than a second valid rendering | 2026-08-18 | Interpretation clause, parallel text |
| Покупная Цена | the Purchase Price | RU→EN | Confirmed by real usage (was provisional from an earlier fragment, now locked) | 2026-08-18 | liability clause, parallel text |
| Закрытие | Completion | RU→EN | UK/international M&A register — not "Closing" | 2026-08-18 | termination clause, parallel text |
| Приложение (this document) | Schedule | RU→EN | CONFIRMED AUTHORITATIVELY by the Interpretation clause (1.1) for this document family. Distinct from an earlier, document-less "annex" entry in Section B — that one stands only for unrelated/generic contexts, not this document | 2026-08-18 | Interpretation clause, parallel text |
| Преамбула | Recitals | RU→EN | Singular RU / plural EN — standard convention, confirmed by the Interpretation clause | 2026-08-18 | Interpretation clause, parallel text |
| Параграф | Paragraph | RU→EN | Structural level within a Schedule/Приложение, distinct from Статья/Пункт | 2026-08-18 | Interpretation clause, parallel text |
| Часть (structural, within a Schedule) | Part | RU→EN | Structural level within a Schedule/Приложение, distinct from Статья/Пункт | 2026-08-18 | Interpretation clause, parallel text |
| as amended, restated or consolidated from time to time | с вносимыми время от времени изменениями, в новой редакции или с учетом консолидации | both | Standard, correctly matched boilerplate triad for statute-reference clauses | 2026-08-18 | Interpretation clause, parallel text |

Format for new rows: `| исходный термин | chosen rendering | RU→EN / EN→RU / both | why this one, what it displaces | YYYY-MM-DD | doc or turn |`

---

## B. Provisional renderings — chosen by me, not yet confirmed

Choices made in the absence of a user pattern. Keep using them for consistency,
but they are open to correction — surface them to the user when the term is
load-bearing, and promote to Section A once approved.

| RU | EN | Direction | Why chosen | Added | Source |
|---|---|---|---|---|---|
| настоящим | hereby | EN→RU | Standard opener for a self-executing declaration; not «этим», not dropped | 2026-08-14 | release clause, chat |
| безусловно и безотзывно | unconditionally and irrevocably | EN→RU | Doublet kept as two adverbs rather than collapsed into one | 2026-08-14 | release clause, chat |
| заявляет | declares | EN→RU | Unilateral declaration; deliberately not «заверяет», which invokes ст. 431.2 ГК РФ representations | 2026-08-14 | release clause, chat |
| требования и/или претензии | demands and/or claims | EN→RU | REVISED 2026-08-14 (see Section C): parallel-text evidence shows требования=demands, претензии=claims, not the original claims/complaints guess | 2026-08-14 | release clause, chat |
| каких бы то ни было | whatsoever | EN→RU | Intensifier rendered explicitly, not dropped as untranslatable | 2026-08-14 | release clause, chat |
| в отношении | with respect to | EN→RU | Over «касательно» / «применительно к» | 2026-08-14 | release clause, chat |
| не вправе отказаться от исполнения Соглашения | shall not have the right to terminate the Agreement | RU→EN | Applies this document's confirmed real practice (терминировать, not "withdraw from") to the fuller ст. 450.1-style phrasing «отказаться от исполнения», not just the shorter «отказаться от Соглашения» seen before | 2026-08-19 | conditions clause, chat |
| ACRA | ACRA | RU→EN | Left untranslated, like SAPA — Singapore's Accounting and Corporate Regulatory Authority, a recognizable acronym | 2026-08-19 | conditions clause, chat |
| если (и в той части/степени, в которой) | if (and to the extent that) | RU→EN | Recurring construction, confirmed twice (earlier "circumstances... remedied" clause and this Purchase Price distribution clause) | 2026-08-19 | chat |
| настоящий Договор | this Agreement | EN→RU | Defined term; «настоящий», not «данный» | 2026-08-14 | release clause, chat |
| Вклад | the Contribution | EN→RU | Provisional — final choice depends on the contract's definition (вклад в уставный капитал / вклад в имущество / взнос) | 2026-08-14 | release clause, chat |
| Во избежание сомнений | For the avoidance of doubt | EN→RU | Standard boilerplate opener; clean equivalent, not flagged | 2026-08-14 | chat |
| приложение | annex | EN→RU | Standard, clean equivalent | 2026-08-14 | chat |
| Бизнес-план | the Business Plan | EN→RU | Defined term, direct calque; capitalized as in source | 2026-08-14 | chat |
| Банк России | CBR / Central Bank of Russia | EN→RU | Provisional — official current name used over the more colloquial «ЦБ РФ»; will recur, needs confirmation for consistency | 2026-08-14 | consents clause, chat |
| денежный взнос | cash contribution (lowercase) | EN→RU | Deliberately distinct from «Вклад» (locked for capitalized defined term «the Contribution») — do not merge the two unless confirmed they refer to the same thing | 2026-08-14 | consents clause, chat |
| Акции | Shares | EN→RU | Defined term, capitalized | 2026-08-14 | consents clause, chat |
| Покупатель | the Buyer | EN→RU | Defined term, capitalized | 2026-08-14 | consents clause, chat |
| Согласия | the Consents | EN→RU | Defined term introduced by this clause, plural, capitalized | 2026-08-14 | consents clause, chat |
| отказ от настоящего Договора | withdrawal from this Agreement | EN→RU | Functional match to unilateral отказ от исполнения договора, ст. 450.1 ГК РФ. NOTE 2026-08-19: real document usage (Warranties/Indemnity clauses) instead renders «отказаться от Соглашения» as "terminate", and further collapses the separate «требовать расторжения» into "termination" too — see the Section E flag on this. This EN→RU entry may not reflect this document's actual RU→EN practice; treat as unconfirmed for this document | 2026-08-14 | withdrawal clause, chat |
| прекращает действие | shall cease to have effect | EN→RU | Standard | 2026-08-14 | withdrawal clause, chat |
| убытки | damages | EN→RU | Standard, ст. 15 ГК РФ | 2026-08-14 | withdrawal clause, chat |
| Продавец | the Seller | EN→RU | Defined term, capitalized | 2026-08-14 | withdrawal clause, chat |
| Покупная цена | the Purchase Price | EN→RU | Promoted to Section A (locked) 2026-08-18 — confirmed by real parallel text | 2026-08-14 | withdrawal clause, chat |
| заём | loan | EN→RU | Standard term under Ch. 42 ГК РФ, not «кредит» (bank-specific) | 2026-08-14 | Contribution/loan clause, chat |
| не является | does not / shall not constitute | EN→RU | Declarative negative, present tense in RU regardless of EN modal «shall» | 2026-08-14 | Contribution/loan clause, chat |
| иной доход | other return | EN→RU | Kept consistent across both occurrences in the excerpt | 2026-08-14 | Contribution/loan clause, chat |
| возврат займа | repayment of a loan | EN→RU | Over «погашение», which reads as bank-credit register | 2026-08-14 | Contribution/loan clause, chat |
| уплата процентов | payment of interest | EN→RU | Standard | 2026-08-14 | Contribution/loan clause, chat |
| Стороны | the Parties | EN→RU | Defined term, capitalized in RU as in source | 2026-08-14 | successors clause, chat |
| распространяется на | shall apply to | EN→RU | Standard for scope/applicability clauses | 2026-08-14 | successors clause, chat |
| сторона SAPA | a/the SAPA party | EN→RU | Kept "SAPA" untranslated per user instruction, "party" translated normally | 2026-08-18 | chat |
| waived (a condition) | отказалась от соблюдения (условия) | EN→RU | Not «отменены» — «waive a condition» is a party's election not to insist on it, not cancelling the condition itself | 2026-08-18 | chat |
| Мерчант | Merchant | EN→RU | Provisional, open question — transliteration (fintech/payments industry usage) chosen over the formal regulatory term «торгово-сервисное предприятие» (ТСП, used in CBR/payment-system rules). Central, recurring defined term — confirm before it propagates further | 2026-08-18 | Transferred Merchants clause, chat |
| Переданные Мерчанты | Transferred Merchants | EN→RU | Defined term | 2026-08-18 | Transferred Merchants clause, chat |
| Мерчанты, Требующие Согласия | Consent-Required Merchants | EN→RU | Defined term | 2026-08-18 | Transferred Merchants clause, chat |
| Замещающие Мерчанты | Substitution Merchants | EN→RU | Defined term | 2026-08-18 | Transferred Merchants clause, chat |
| Существенный Передаваемый Договор | Material Transferred Contract | EN→RU | Defined term | 2026-08-18 | Transferred Merchants clause, chat |
| Согласие Третьего Лица | Third Party Consent | EN→RU | Defined term, capitalized — matches the earlier "Third Party Claim"/«Требование третьего лица» capitalization convention | 2026-08-18 | Transferred Merchants clause, chat |
| Существенное Соглашение | Material Agreement | EN→RU | Defined term, distinct from Material Transferred Contract | 2026-08-18 | Transferred Merchants clause, chat |
| Группа Покупателя | the Purchaser Group | EN→RU | Defined term | 2026-08-18 | Third Party Consents condition, chat |
| GMV Paid | GMV Paid | EN→RU | Provisional — left untranslated like SAPA; fintech-specific metric (paid Gross Merchandise Value) with no settled RU equivalent. Confirm before it recurs further | 2026-08-18 | Third Party Consents condition, chat |
| действующего разумно | acting reasonably | EN→RU | Standard M&A reasonableness qualifier for a party's consent/acceptance | 2026-08-18 | Third Party Consents condition, chat |
| Соглашение о Расторжении | the Termination Agreement | EN→RU | Provisional — uses «Соглашение» per this document's locked word for "Agreement", not «Договор» | 2026-08-18 | chat |
| Дата Закрытия | the Completion Date | EN→RU | Provisional — matches the locked Закрытие=Completion pair | 2026-08-18 | chat |
| к разумному удовлетворению X и Сторон | to X's and the Parties' reasonable satisfaction | EN→RU | Standard M&A boilerplate construction | 2026-08-18 | chat |
| Соглашение о присоединении | the Deed of Adherence | EN→RU | Provisional — standard RU rendering for the common-law "deed of adherence" (a party acceding to an existing agreement) | 2026-08-18 | chat |
| подписан(о) и передан(о) | executed and delivered | EN→RU | Standard doublet for common-law contract execution formalities | 2026-08-18 | chat |
| Передаточное распоряжение | the Transfer Instrument | RU→EN | Defined term, capitalized | 2026-08-18 | governing-law/dispute-resolution clause, parallel text |
| Документы по Сделке | the Transaction Documents | RU→EN | Defined term, plural, capitalized; «Сделка» = Transaction | 2026-08-18 | governing-law/dispute-resolution clause, parallel text |
| Спор | the Dispute | RU→EN | Singular defined term collectively covering the plural list (disputes, disagreements, claims, demands) preceding it | 2026-08-18 | governing-law/dispute-resolution clause, parallel text |
| Соглашение | the Agreement | RU→EN | This document's word for "Agreement" — note it uses «Соглашение», not «Договор» (locked separately for other documents); both map to "Agreement", track which source document uses which | 2026-08-18 | governing-law/dispute-resolution clause, parallel text |
| Применимое Законодательство | Applicable Legislation | RU→EN | Defined term, capitalized both sides, consistent throughout. Distinct from the earlier governing-law heading question — that was about jurisdiction-selection "law" (lowercase, external), this is the substantive defined term used across the operative articles; not actually a conflict | 2026-08-18 | liability/termination/validity clauses, parallel text |
| Имущественные Потери | Property Losses | RU→EN | Defined term, capitalized, consistent throughout | 2026-08-18 | liability clause, parallel text |
| Событие(-я) Возмещения Потерь | Indemnification Event(s) | RU→EN | Defined term, capitalized, consistent | 2026-08-18 | liability clause, parallel text |
| Требование третьего лица | the Third Party Claim | RU→EN | Defined term, introduced by definition then used consistently | 2026-08-18 | liability clause, parallel text |
| Требование о Возмещении Потерь | the Indemnity Claim | RU→EN | Defined term (only one occurrence seen so far — confirm on next appearance) | 2026-08-18 | liability clause, parallel text |
| Уведомление о расторжении | the Termination Notice | RU→EN | Defined term, consistent | 2026-08-18 | termination clause, parallel text |
| Предельная дата расторжения | the Termination Long Stop Date | RU→EN | Idiomatic M&A term ("long stop date") chosen over a literal "deadline/limit date" — good pattern, not flagged | 2026-08-18 | termination clause, parallel text |
| ГК РФ | the CC RF | RU→EN | Abbreviation convention observed consistently (not spelled out as "Civil Code of the Russian Federation" after first use) | 2026-08-18 | liability/termination clauses, parallel text |
| Покупатель | the Purchaser | RU→EN | This document's word for "Buyer" — conflicts with an earlier provisional entry (Покупатель = the Buyer) from a different fragment/document; do not assume they're the same contract — confirm which document uses which before merging | 2026-08-18 | liability clause, parallel text |
| Уведомление | the Notice | RU→EN | Base defined term (distinct from «Уведомление о расторжении»/"Termination Notice", already locked) | 2026-08-18 | notices clause, parallel text |
| направляющая Сторона | the sending Party | RU→EN | Complementary defined pair with получающая Сторона below | 2026-08-18 | notices clause, parallel text |
| получающая Сторона | the receiving Party | RU→EN | Complementary defined pair with направляющая Сторона above | 2026-08-18 | notices clause, parallel text |
| надлежащим образом / в надлежащем порядке | duly | RU→EN | Consistent adverb choice for this register, confirmed twice in the same clause | 2026-08-18 | notices clause, parallel text |
| акт приема-передачи (документов) | the act of acceptance and transfer (of documents) | RU→EN | Provisional/flag — no clean EN equivalent; this is a literal calque of a Russian civil-law document type. Alternative seen in practice: "handover certificate" / "delivery-acceptance certificate". Confirm before locking | 2026-08-18 | notices clause, parallel text |
| Аффилированные Лица | Affiliates | RU→EN | Defined term, capitalized; idiomatic EN short form, not a literal "Affiliated Persons" calque | 2026-08-18 | confidentiality clause, parallel text |
| Конфиденциальная Информация | Confidential Information | RU→EN | Defined term introduced by this clause | 2026-08-18 | confidentiality clause, parallel text |
| Государственные Органы | State Authorities | RU→EN | Defined term, capitalized both sides | 2026-08-18 | confidentiality clause, parallel text |
| Банковская гарантия | the Bank Guarantee | RU→EN | Defined term | 2026-08-18 | confidentiality clause, parallel text |
| Поручитель | the Guarantor | RU→EN | Defined term | 2026-08-18 | confidentiality clause, parallel text |
| Эскроу-агент | the Escrow Agent | RU→EN | Defined term | 2026-08-18 | confidentiality clause, parallel text |
| Акционерное соглашение | the SHA | RU→EN | Rendered as an acronym (Shareholders' Agreement), not spelled out — presumably defined earlier in the document; keep as SHA if so | 2026-08-18 | confidentiality clause, parallel text |
| Квази-акционерное соглашение | the Quasi-Shareholders Agreement | RU→EN | Defined term, direct calque of the "quasi-" prefix | 2026-08-18 | confidentiality clause, parallel text |

---

## C. Corrections — what the user rejected and what they used instead

The highest-value section: each row is a mistake already made once.

| Source term | I wrote | User uses | What the correction teaches | Added | Source |
|---|---|---|---|---|---|
| требования и/или претензии (from EN "claims and/or complaints") | требования=claims, претензии=complaints | требования=demands, претензии=claims | This wasn't a live user correction but a self-caught error from a supplied parallel text: my original EN→RU guess for this pair was backwards. «Претензия» ≈ claim (not the weaker "complaint"); «требование» ≈ demand. Generalization: don't assume near-synonym pairs in RU legal doublets map to near-synonym pairs in EN in the same order — check a real parallel example before locking either half. | 2026-08-18 | governing-law/dispute-resolution clause, parallel text |

When a row is added here, check whether the correction generalizes — if the user
replaces one calque, they usually reject the whole family of calques. Write the
generalization into Section E rather than waiting to be corrected term by term.

---

## D. Structural and formatting conventions

How the user wants the non-prose layer rendered. Fill in from observed practice;
until an entry is filled, follow Section F.

- **Clause numbering** — observed (parallel text, 2026-08-18): RU numbers carry no trailing period ("1.1"), EN numbers do ("1.1."). Provisional — treat as this document's convention; confirm before assuming it's universal.
- **Section-heading style, RU→EN** — observed: a RU heading noun-phrase like «порядок разрешения споров» (lit. "procedure for dispute resolution") compresses to just "Dispute Resolution" in the EN heading — «порядок» is dropped as a heading-only simplification, not a general license to drop it in body text.
- **Governing-law heading: "право" vs "законодательство"** — _(mostly resolved, 2026-08-18)_: a later parallel-text sample shows «Применимое Законодательство»/"Applicable Legislation" is a consistent, capitalized, document-wide defined term used across the operative articles — separate from the earlier one-off heading («ПРАВО» → "Legislation" in a section title, next to lowercase "the laws of X" for jurisdiction-selection). So the defined-term mapping законодательство=Legislation is solid; only the section-heading wording ("Governing Law" vs "Governing Legislation" as a title) remains an open stylistic question, not a substantive one.
- **Date format (RU→EN / EN→RU)** — _(unrecorded)_
- **Money: digits + spelled-out redundancy** — _(unrecorded)_
- **Periods/deadlines: digit + spelled-out redundancy for days/months/years/hours/time-of-day** — confirmed by repeated real usage: «5 (пяти) Рабочих дней» → "5 (five) Business Days", «2 (двух) месяцев» → "2 (two) months", «3 (трех) лет» → "3 (three) years", «10 (десяти) Рабочих Дней» → "10 (ten) Business Days", «24 (двадцать четыре) часа» → "24 (twenty-four) hours", «00:00 (ноля часов ноля минут)» → "00:00 (zero hours zero minutes)" — matches Section F default exactly, now backed by real examples across days, months, years, hours, and clock times. «Рабочий день»/"Business Day" is itself a capitalized defined term. EXCEPTION observed 2026-08-18: «до 24:00 последнего дня» → "before 24:00 of the last day" — no spelled-out gloss here, unlike the notices-clause clock times. Not universal; treat case by case.
- **«ГК РФ» abbreviation — CONFIRMED inconsistent.** Sometimes "CC RF" (liability/termination clauses), sometimes spelled out in full "the Civil Code of the Russian Federation" (Interpretation clause, 1.7). Needs a decision on which is the standing convention.
- **Thousands separator and decimal mark** — _(unrecorded)_
- **Party name transliteration (ГОСТ / BGN / passport spelling)** — _(unrecorded)_
- **Entity forms (ООО / АО / ИП): translate, transliterate, or keep + gloss** — _(unrecorded)_
- **Registration identifiers (ИНН, ОГРН, КПП, EIN)** — _(unrecorded)_
- **Statute/clause citation style, RU→EN (this document family)** — **resolved 2026-08-18**, see Section A: «Статья N» and «Пункт N.M» both → "Clause N" / "Clause N.M", including citations to external statute articles (ГК РФ). One EN word covers everything numbered, regardless of RU word or whether it's contract-internal or statutory.
- **Statute/clause citation style, EN→RU (translating INTO Russian)** — still _(open, 2026-08-14)_: the earlier single-sentence fragment "Article 2.1" / "Section 3" was a *different* document (uses «Договор», not «Соглашение» — see the separate note on that word), so the RU→EN resolution above doesn't necessarily transfer to it. Defaulted "Article 2.1" → «п. 2.1» and "Section 3" → «Раздел 3»; still needs its own confirmation, independently of the resolved document above.
- **Defined-term marking (Capitalization, «quotes», bold)** — _(unrecorded)_
- **When a plain RU word would collide with an already-locked defined-term rendering, use a different EN word for the plain sense.** Pattern established 2026-08-19 with «Параграф» (locked defined term → "Paragraph") vs. plain «абзац» (→ "indent" instead of "paragraph", to avoid collision). Check new single-word lookups against existing locked defined-term entries before finalizing — a generic dictionary sense can silently collide with a structural term already in use.
- **RU source sometimes embeds an English gloss inline in parens** — e.g. «гербовые сборы (stamp duty)», «преимущественного права покупки (Right of First Refusal)». When this happens, use exactly that embedded English term as the EN rendering rather than translating independently — it's the drafter's own intended equivalence, not just a parenthetical aside.
- **Addresses: transliterate or translate street types** — _(unrecorded)_
- **Signature blocks and seal notations** — _(unrecorded)_

---

## E. Register and syntax patterns

Sentence-level habits, not single terms — the things that make a translation read
as *this user's* work rather than generically correct.

- **Modality (обязан / должен / вправе → shall / must / may / is entitled to)** — observed: `shall be entitled to` → «вправе»; `shall [+ verb of obligation]` → «обязан» (e.g. `shall refund` → «обязан вернуть»). Keep the two distinct — don't collapse both to «обязан» or both to «вправе».
- **Doublets in RU legal lists don't map term-for-term by position** — from parallel text (2026-08-18): «претензии и (или) требования» → «claims and (or) demands» is claim=2nd RU word / demand=1st-position-in-source-order-reversed pairing, not a naive left-to-right match. Never lock a doublet pairing without a real parallel-text example; a guessed pairing (see Section C) can be exactly backwards.
- **"Исполнение" — CONFIRMED inconsistent, needs a decision.** Now observed in at least three places across this document: «неисполнение или ненадлежащее исполнение Соглашения» → "failure to **perform** or improper **performance**" (liability clause); «его исполнением» (заключение/исполнение/прекращение list) → "its **execution**" (expenses clause); and in the confidentiality clause alone, both happen side by side — «об их исполнении» / «(ii) их исполнения» → "their **execution**" (1.1), but «для целей исполнения Соглашения» → "for the purposes of **performing** the Agreement" (1.3(a)), same clause, same word, two renderings. Recommend standardizing on "performance" — awaiting user confirmation before treating either as the locked default.
- **«Обязательства из причинения вреда» → "obligations for damages"** — _(open, 2026-08-18)_: functionally close but not exact; "tortious obligations" / "obligations in tort" is the more standard EN legal-family term for гл. 59 ГК РФ delictual obligations. Note, not yet a confirmed correction.
- **Same RU phrase, two different EN renderings within one document** — two more instances observed 2026-08-18, worth watching as a pattern of drift rather than one-off typos: (1) «не имеет/имеют права на» → both "shall not be entitled to" (1.4) and "do not have the right to" (2.1); (2) «компетентного суда апелляционной инстанции» → both "a competent appellate court" (1.6(d)) and "a competent court of appeal" (1.7, same phrase). Neither is wrong on its own, but a defined/recurring phrase drifting like this is worth a consistency pass before final delivery.
- **Определённый термин, потерявший консистентность: «Заверения» → Warranty vs Representation.** Predominant rendering across the document is "Warranties" but "Representation" recurs repeatedly (at least 6 confirmed instances by 2026-08-19, including the dedicated Warranties clause itself: 1.4, 1.5, twice in 1.8). THIS IS NOW A MEANING-LEVEL DEFECT, not just style: "Purchaser's/Seller's Representation" is never itself defined anywhere in the document — only "...Warranties" is. A translation that uses "Representation" is referencing an undefined term. Treat "Warranties" as the only correct rendering; "Representation" should be corrected on sight, not treated as an acceptable variant.
- **HIGH-VALUE TRAP: «Акция» is a homonym (Share / marketing promotion) — verify by context every time, don't pattern-match on the word alone.** Confirmed real error 2026-08-19 (Indemnity clause, 2.2(a)(i)(1)): «какой-либо Акцией» → "any **Promotion**" instead of "any **Share**" — a clear mistranslation, inconsistent with the correct "Share" rendering used one and two lines later for the identical word. In an M&A/share-purchase document «Акция» is essentially always "Share"; treat "Promotion" as almost certainly wrong unless the surrounding context is genuinely about marketing.
- **Direction of "признание X Y-instrumental" (recognition/classification) — watch for reversed agency in EN.** RU «признание X Y-ом» = "X being classified/recognized AS Y" (X is the one being classified). Confirmed mistranslation 2026-08-19 (sanctions-indemnity clause, 2.2(b)): «признания Покупателя ... иностранными лицами» → "recognition of the Purchaser ... **by** foreign persons" instead of "recognition of the Purchaser ... **as** a foreign person" — this reverses who is doing the classifying, a real meaning inversion in a sanctions-sensitive clause. Check this construction carefully whenever "признание X Y-instr" appears — "by" is very likely wrong, "as" is very likely right.
- **Garbled duplicate phrase: "performance execution".** Appears twice (2.2(a)(i)(3), Indemnity clause, 2026-08-19) for plain «исполнение» (performance) — looks like an edit artifact where "execution" was left in after being replaced by "performance". Should just be "performance".
- **Don't add a currency to an unfilled blank that has none in the source.** 2.6(c) (Indemnity clause, 2026-08-19): RU leaves a bare blank «превышает \_\_» with no currency word; EN supplies "exceeds \_\_ **roubles**" — an invented addition not present in source. The parallel blank in 2.6(b) correctly stays currency-less in both languages. Don't infer a currency for an unfilled amount unless the source actually states one nearby.
- **British vs American spelling mixed in the same document.** _(flag, 2026-08-18)_: «authorised» person/representative/bodies (BrE spelling, notices clause and again in the confidentiality clause's 1.8) coexists with «recognized» courier service/organization (AmE, notices clause) and «organizations» (AmE, confidentiality clause 1.3(e)), plus a third wobble on «electronic mail» / «email» / «E-mail». New data point 2026-08-18: «рубли» → "**roubles**" (BrE spelling) in the Interpretation clause — this leans the balance toward BrE being the intended house style, with the AmE instances ("recognized", "organizations") being the outliers. Still not silently resolved — confirm with the user before treating BrE as locked.
- **«уведомление о вручении»** — same RU phrase rendered as both "return receipt requested" and "acknowledgment of receipt" within one document (notices clause, 2026-08-18). Another instance of the recurring drift pattern noted above (Заверения, appellate court, entitled-to) — same underlying issue: a phrase gets retranslated fresh each time it recurs instead of reusing the first rendering.
- **Missing closing parentheses (proofreading, not style) — Interpretation clause, 2026-08-18.** Two instances where the EN drops the closing ")" that the RU has: 1.3 "...whether or not they are separate legal entities." and 1.9 "...including communications by e-mail." Both are objective punctuation errors, easy fixes, worth a pass before delivery.
- **1.11 of the Interpretation clause: one of four quoted expressions appears to be missing in EN.** RU lists four quoted trigger-phrases for the non-limiting "including" interpretation rule: «включает», «включая», «среди прочего», «в том числе». EN lists only three: "include", "including", "inter alia". If the dropped RU phrase appears verbatim elsewhere in the contract, this interpretive rule may not formally cover it — worth restoring the fourth term rather than treating it as covered by "inter alia".
- **«цессионарии» reappears for generic "permitted assigns" boilerplate, contradicting the user's earlier explicit choice for the negotiated "assignees" clause.** In the Interpretation clause 1.16: «правопреемников и разрешенных цессионариев» → "successors and permitted assigns". Earlier (successors clause) the user picked a broader construction over «цессионарии» specifically because it under-covers obligations, not just rights. Flag whether the same concern applies to this generic interpretive boilerplate, or whether «цессионарии» is acceptable here as a different, narrower context.
- **«корпоративный договор» → "shareholders' agreement"** — _(open, 2026-08-18)_: possibly narrower than the RU concept. «Корпоративный договор» (ст. 67.2 ГК РФ) can be entered into by participants of any corporate entity, not just shareholders of a joint-stock company — "corporate agreement" or "shareholders'/participants' agreement" may be more accurate depending on context.
- **Impersonal RU constructions → active or passive EN** — _(unrecorded)_
- **Nominalization: keep the RU noun-chain or verbalize it in EN** — _(unrecorded)_
- **Sentence splitting: preserve long RU periods or break them** — _(unrecorded)_
- **Tolerance for calques vs. functional rewording** — _(unrecorded)_
- **"Настоящий Договор" → "this Agreement" / "the present Agreement"** — _(unrecorded)_
- **Doublets (terms and conditions, null and void) in RU→EN** — _(unrecorded)_

---

## F. Standing defaults

Used only where Sections A–E are silent. These are conventional legal-translation
practice, not user preferences — replace them the moment the user shows otherwise.

- Keep the source numbering scheme exactly (`4.2.1` stays `4.2.1`); never renumber
  or flatten, even where the target language would nest differently.
- Preserve digit + spelled-out redundancy in both directions:
  `100 000 (сто тысяч) рублей` ↔ `100,000 (one hundred thousand) rubles`.
- RU→EN numbers: comma as thousands separator, period as decimal mark. EN→RU:
  non-breaking space and comma respectively.
- Dates: spell the month in both directions to avoid 03/04 ambiguity
  (`12 марта 2024 г.` ↔ `12 March 2024`).
- One defined term, one rendering, every occurrence — consistency is what makes
  the definition binding.
- Party names, addresses, and registration numbers: copy verbatim; transliterate
  the same way at every occurrence in the document.
- `обязуется` → `shall` (obligation), `вправе` → `may` / `is entitled to`
  (permission); do not collapse the two into `shall` everywhere.
- Company forms: keep the Russian form and gloss on first use
  (`ООО «Ромашка»` → `OOO Romashka (limited liability company)`), then the short
  form thereafter — this avoids the false equivalence of `LLC`.
- No-clean-equivalent concepts (неустойка, существенные условия, consideration,
  estoppel): closest functional equivalent in the body, yellow highlight at the
  occurrence, entry in the flagged-terms appendix.

---

## Intake: extracting patterns from a parallel text

When the user supplies a source and their own translation of it — the fastest way
to learn their style — work through it deliberately rather than reading for a
general impression:

1. Align the two texts clause by clause and list every term where the user's
   rendering differs from what you would have written. Those differences are the
   entries; the matches are not informative.
2. For each difference, decide whether it is a **term** (→ Section A) or a
   **habit** (→ Section E). A single term choice can be idiosyncratic to one
   document; a habit shows up three or more times and generalizes.
3. Record the structural layer separately — numbering, dates, money, names — into
   Section D, since these are usually house rules the user applies uniformly and
   never mentions.
4. Note what the user *omits or adds* relative to the source: a translator who
   consistently drops `настоящий` or adds `hereby` is showing a register
   preference worth recording.
5. Write only what the parallel text actually shows. An inferred preference that
   never appeared is worse than an empty row — it will silently override the
   user's real choice later.
